// gcc -o test test.c -march=native -mavx512f
#include <stdint.h>
#include <stdio.h>
#include <immintrin.h>

typedef uint64_t v4_int64 __attribute__((vector_size(32)));
typedef uint32_t v4_int32 __attribute__((vector_size(16)));

void go(v4_int32 *state, v4_int32 *round_key) {
    asm volatile (
        "vaesenc %2, %1, %0 \n"
        // "aesimc %0, %0 \n"
        // "vaesdec %2, %1, %0 \n"
        : "+v"(*state)
        : "v"(*state), "v"(*round_key)
    );

    // asm volatile (
    //     "vaesimc %0, %0"
    //     : "+v"(*round_key)
    // );

    // asm volatile (
    //     // "aesdec %1, %0 \n"
    //     "vaesdeclast %1, %0, %0 \n"
    //     // "vaesdec %1, %0, %0 \n"
    //     // "vaesdec %1, %0, %0 \n"
    //     : "+v"(*state)
    //     : "v"(*round_key)
    // );
}

int main() {
    v4_int64 target_state = {0x142a26a0be0fcc51, 0x1c46fdec3089756d, 0x06c9628b79b4a30f, 0xc4f2c72abe03ea68};

    // v4_int64 state = {0x7d697234376e3463, 0x6c41796772656e34, 0x6b69676567453766, 0x697237357b534e49};
    // v4_int64 round_key = {0x259005b5a190300, 0x5e01095c01150300, 0xd42064d160d5342, 0xf540b633a425227}; // fixed
    // go(&state, &round_key);

    // printf("key: %016lx %016lx %016lx %016lx\n", round_key[0], round_key[1], round_key[2], round_key[3]);
    // printf("state: %016lx %016lx %016lx %016lx\n", state[0], state[1], state[2], state[3]);

    v4_int32 state = {0x6c636572, 0x7d353534, 0x70306335, 0x65756869};
    // v4_int32 state = {0xbe0fcc51, 0x142a26a0, 0x3089756d, 0x1c46fdec};
    v4_int32 round_key = {0x5a190300, 0x259005b, 0x1150300, 0x5e01095c};
    go(&state, &round_key);

    printf("key: %08x %08x %08x %08x\n", round_key[0], round_key[1], round_key[2], round_key[3]);
    printf("state: %08x %08x %08x %08x\n", state[0], state[1], state[2], state[3]);

    return 0;
}
