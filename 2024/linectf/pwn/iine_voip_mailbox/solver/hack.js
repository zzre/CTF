// by osori
var hook = Module.getExportByName("WS2_32.dll", "send");
var hook2 = Module.getExportByName("WS2_32.dll", "recv");
console.log(hook, hook2)

function toHex(str) {
  var result = '';
  for (var i=0; i<str.length; i++) {
    result += str.charCodeAt(i).toString(16);
  }
  return result;
}

function stringToByteArray(str) {
  var byteArray = [];
  for (var i = 0; i < str.length; ++i) {
      var charCode = str.charCodeAt(i);
      byteArray.push(charCode & 0xFF);
  }
  return byteArray;
}

function byteArrayToHex(byteArray) {
  return Array.prototype.map.call(byteArray, function(byte) {
    return ('0' + (byte & 0xFF).toString(16)).slice(-2);
  }).join('');
}

function splitByteArray(byteArray, delimiter) {
  var result = [];
  var startIndex = 0;
  for (var i = 0; i < byteArray.length; i++) {
      var isDelimiterFound = true;
      for (var j = 0; j < delimiter.length; j++) {
          if (byteArray[i + j] !== delimiter[j]) {
              isDelimiterFound = false;
              break;
          }
      }
      if (isDelimiterFound) {
          result.push(byteArray.slice(startIndex, i));
          startIndex = i + delimiter.length;
          i += delimiter.length - 1;
      }
  }
  if (startIndex < byteArray.length) {
      result.push(byteArray.slice(startIndex));
  }
  return result;
}

var buf;
Interceptor.attach(hook2, {
  onEnter(args) {        
    buf = args[1];
      
  },
  
  onLeave(result) {
    try
    {
        result = Number(result.toString())
        if (result != 0xffffffff)
        {            
            var bbuffer = new Uint8Array(Memory.readByteArray(buf, result));            
            bbuffer = splitByteArray(bbuffer, [0x0d, 0x0a]);
            bbuffer = bbuffer[bbuffer.length - 1];
            //console.log(tmp);
            if (bbuffer.byteLength != 0)
            {
                send({'message': byteArrayToHex(bbuffer)});
            }
        }
    }
    catch(ex)
    {
        console.log(ex);
    }
  }
});