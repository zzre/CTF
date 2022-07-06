#include <stdio.h>
#include <unistd.h>

int ROM[0xff];
int S = 0;

int R[8] = {0};
int Z[8] = {0};
int X[8] = {0};
int Y[8] = {0};
int B[8] = {0};
int Q[8] = {0};
int I[8] = {0};
int C[8] = {0};
int O[8] = {0};
int P[8] = {0};
int A[8] = {0};
int M[8] = {0};
int l[8] = {0};
int N[8] = {0};

int c;

char flag[28] = "CTF{write_flag_here_please}";
int INVALID_FLAG = 0;

void Initialize() {
    ROM[0] = 0xbb;
    ROM[1] = 0x55;
    ROM[2] = 0xab;
    ROM[3] = 0xc5;
    ROM[4] = 0xb9;
    ROM[5] = 0x9d;
    ROM[6] = 0xc9;
    ROM[7] = 0x69;
    ROM[8] = 0xbb;
    ROM[9] = 0x37;
    ROM[10] = 0xd9;
    ROM[11] = 0xcd;
    ROM[12] = 0x21;
    ROM[13] = 0xb3;
    ROM[14] = 0xcf;
    ROM[15] = 0xcf;
    ROM[16] = 0x9f;
    ROM[17] = 0x9;
    ROM[18] = 0xb5;
    ROM[19] = 0x3d;
    ROM[20] = 0xeb;
    ROM[21] = 0x7f;
    ROM[22] = 0x57;
    ROM[23] = 0xa1;
    ROM[24] = 0xeb;
    ROM[25] = 0x87;
    ROM[26] = 0x67;
    ROM[27] = 0x23;
    ROM[28] = 0x17;
    ROM[29] = 0x25;
    ROM[30] = 0xd1;
    ROM[31] = 0x1b;
    ROM[32] = 0x8;
    ROM[33] = 0x64;
    ROM[34] = 0x64;
    ROM[35] = 0x35;
    ROM[36] = 0x91;
    ROM[37] = 0x64;
    ROM[38] = 0xe7;
    ROM[39] = 0xa0;
    ROM[40] = 0x6;
    ROM[41] = 0xaa;
    ROM[42] = 0xdd;
    ROM[43] = 0x75;
    ROM[44] = 0x17;
    ROM[45] = 0x9d;
    ROM[46] = 0x6d;
    ROM[47] = 0x5c;
    ROM[48] = 0x5e;
    ROM[49] = 0x19;
    ROM[50] = 0xfd;
    ROM[51] = 0xe9;
    ROM[52] = 0xc;
    ROM[53] = 0xf9;
    ROM[54] = 0xb4;
    ROM[55] = 0x83;
    ROM[56] = 0x86;
    ROM[57] = 0x22;
    ROM[58] = 0x42;
    ROM[59] = 0x1e;
    ROM[60] = 0x57;
    ROM[61] = 0xa1;
    ROM[62] = 0x28;
    ROM[63] = 0x62;
    ROM[64] = 0xfa;
    ROM[65] = 0x7b;
    ROM[66] = 0x1b;
    ROM[67] = 0xba;
    ROM[68] = 0x1e;
    ROM[69] = 0xb4;
    ROM[70] = 0xb3;
    ROM[71] = 0x58;
    ROM[72] = 0xc6;
    ROM[73] = 0xf3;
    ROM[74] = 0x8c;
    ROM[75] = 0x90;
    ROM[76] = 0x3b;
    ROM[77] = 0xba;
    ROM[78] = 0x19;
    ROM[79] = 0x6e;
    ROM[80] = 0xce;
    ROM[81] = 0xdf;
    ROM[82] = 0xf1;
    ROM[83] = 0x25;
    ROM[84] = 0x8d;
    ROM[85] = 0x40;
    ROM[86] = 0x80;
    ROM[87] = 0x70;
    ROM[88] = 0xe0;
    ROM[89] = 0x4d;
    ROM[90] = 0x1c;

    for (int i=0; i<27; i++) {
        for (int j=0; j<8; j++) {
            if (flag[i] & (1<<j)) {
                ROM[0x80+i] |= 1<<j;
            }
            else {
                ROM[0x80+i] &= (0b11111111 ^ (1<<j));
            }
        }
    }
}

int LD(int arr[], int i) {
    int x = 0;

    for (int j=0; j<8; j++) {
        if (arr[j] == 1)
            x += (1<<j);
    }

    return (ROM[x] >> i) & 1;
}

int main(void)
{
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
    
    printf("> ");
    read(0, flag, 27);

    Initialize();
    
    int count = 0;
    while (S != -1)
    {
        if (S == 0) {
            S = 24;
        }

        if (S == 1) {
            S = 2;
            
            for (int i=0; i<8; i++) {
                if (R[i] == 1) {
                    R[i] = 0;
                }

                else {
                    R[i] = 1;
                }
            }
        }

        if (S == 2) {
            S = 3;

            Z[0] = 1;
            for (int i=1; i<8; i++) {
                Z[i] = 0;
            }
        }

        if (S == 3) {
            S = 4;
            c = 0;

            for (int i=0; i<8; i++) {
            if (R[i] == 0) {
                if (Z[i] == 0) {
                    if (c == 1) {
                        R[i] = 1;
                        c = 0;
                    }
                }

                else {
                    if (c == 0) {
                        R[i] = 1;
                        c = 0;
                    }
                }
            }

            else {
                if (Z[i] == 0) {
                    if (c == 1) {
                        R[i] = 0;
                        c = 1;
                    }
                }

                else {
                    if (c == 0) {
                        R[i] = 0;
                        c = 1;
                    }
                }
            }
            }
        }

        if (S == 4) {
            S = 5;

            for (int i=0; i<8; i++) {
            if (R[i] == 0) {
                if (Z[i] == 0) {
                    if (c == 1) {
                        R[i] = 1;
                        c = 0;
                    }
                }

                else {
                    if (c == 0) {
                        R[i] = 1;
                        c = 0;
                    }
                }
            }

            else {
                if (Z[i] == 0) {
                    if (c == 1) {
                        R[i] = 0;
                        c = 1;
                    }
                }

                else {
                    if (c == 0) {
                        R[i] = 0;
                        c = 1;
                    }
                }
            }
            }
        }

        if (S == 5) {
            S = 6;

            int check = 0;
            for (int i=0; i<8; i++) {
                if (R[i] == 1) {
                    check = 1;
                }
            }

            if (check == 0) {
                S = 38;
            } 
        }

        if (S == 6) {
            S = 7;
            c = 0;

            for (int i=0; i<8; i++) {
            if (R[i] == 0) {
                if (Z[i] == 0) {
                    if (c == 1) {
                        R[i] = 1;
                        c = 0;
                    }
                }

                else {
                    if (c == 0) {
                        R[i] = 1;
                        c = 0;
                    }
                }
            }

            else {
                if (Z[i] == 0) {
                    if (c == 1) {
                        R[i] = 0;
                        c = 1;
                    }
                }

                else {
                    if (c == 0) {
                        R[i] = 0;
                        c = 1;
                    }
                }
            }
            }
        }

        if (S == 7) {
            S = 8;

            int check = 0;
            for (int i=0; i<8; i++) {
                if (R[i] == 1) {
                    check = 1;
                }
            }

            if (check == 0) {
                S = 59;
            } 
        }

        if (S == 8) {
            S = 9;
            c = 0;

            for (int i=0; i<8; i++) {
            if (R[i] == 0) {
                if (Z[i] == 0) {
                    if (c == 1) {
                        R[i] = 1;
                        c = 0;
                    }
                }

                else {
                    if (c == 0) {
                        R[i] = 1;
                        c = 0;
                    }
                }
            }

            else {
                if (Z[i] == 0) {
                    if (c == 1) {
                        R[i] = 0;
                        c = 1;
                    }   
                }

                else {
                    if (c == 0) {
                        R[i] = 0;
                        c = 1;
                    }
                }
            }
            }
        }

        if (S == 9) {
            S = 10;

            int check = 0;
            for (int i=0; i<8; i++) {
                if (R[i] == 1) {
                    check = 1;
                }
            }

            if (check == 0) {
                S = 59;
            }    
        }

        if (S == 10) {
            S = 11;

            printf("BUG\n");
            break;
        }

        if (S == 11) {
            S = -1;
        }

        if (S == 12) {
            S = 13;

            for (int i=0; i<8; i++) {
                X[i] = 0;
            }
            X[0] = 1;
        }

        if (S == 13) {
            S = 14;

            for (int i=0; i<8; i++) {
                Y[i] = 0;
            }
        }

        if (S == 14) {
            S = 15;

            int check = 0;
            for (int i=0; i<8; i++) {
                if (X[i] == 1) {
                    check = 1;
                }
            }

            if (check == 0) {
                S = 22;
            }    
        }

        if (S == 15) {
            S = 16;

            for (int i=0; i<8; i++) {
                if (X[i] == 1) {
                    Z[i] = 1;
                }

                else {
                    Z[i] = 0;
                }
            }
        }

        if (S == 16) {
            S = 17;

            for (int i=0; i<8; i++) {
            if (Z[i] == 1) {
                if (B[i] == 0) {
                    Z[i] = 0;
                }
            }
            }
        }

        if (S == 17) {
            S = 18;

            int check = 0;
            for (int i=0; i<8; i++) {
                if (Z[i] == 1) {
                    check = 1;
                }
            }

            if (check == 0) {
                S = 19;
            }
        }

        if (S == 18) {
            S = 19;
            c = 0;

            for (int i=0; i<8; i++) {
            if (Y[i] == 0) {
                if (A[i] == 0) {
                    if (c == 1) {
                        Y[i] = 1;
                        c = 0;
                    }
                }

                else {
                    if (c == 0) {
                        Y[i] = 1;
                        c = 0;
                    }
                }
            }

            else {
                if (A[i] == 0) {
                    if (c == 1) {
                        Y[i] = 0;
                        c = 1;
                    }
                }

                else {
                    if (c == 0) {
                        Y[i] = 0;
                        c = 1;
                    }
                }
            }
            }
        }

        if (S == 19) {
            S = 20;
            c = 0;

            for (int i=0; i<8; i++) {
            if (X[i] == 0) {
                if (X[i] == 0) {
                    if (c == 1) {
                        X[i] = 1;
                        c = 0;
                    }
                }

                else {
                    if (c == 0) {
                        X[i] = 1;
                        c = 0;
                    }
                }
            }

            else {
                if (X[i] == 0) {
                    if (c == 0) {
                        X[i] = 0;
                        c = 1;
                    }
                }

                else {
                    if (c == 0) {
                        X[i] = 0;
                        c = 1;
                    }
                }
            }
            }
        }

        if (S == 20) {
            S = 21;
            c = 0;

            for (int i=0; i<8; i++) {
            if (A[i] == 0) {
                if (A[i] == 0) {
                    if (c == 1) {
                        A[i] = 1;
                        c = 0;
                    }
                }

                else {
                    if (c == 0) {
                        A[i] = 1;
                        c = 0;
                    }
                }
            }

            else {
                if (A[i] == 0) {
                    if (c == 1) {
                        A[i] = 0;
                        c = 1;
                    }
                }

                else {
                    if (c == 0) {
                        A[i] = 0;
                        c = 1;
                    }
                }
            }
            }
        }

        if (S == 21) {
            S = 14;
        }

        if (S == 22) {
            S = 23;

            for (int i=0; i<8; i++) {
            if (Y[i] == 1) {
                A[i] = 1;
            }

            else {
                A[i] = 0;
            }
            }
        }

        if (S == 23) {
            S = 1;
        }

        if (S == 24) {
            S = 25;

            for (int i=0; i<8; i++) {
                I[i] = 0;
            }
        }

        if (S == 25) {
            S = 26;

            for (int i=0; i<8; i++) {
                M[i] = 0;
            }
        }

        if (S == 26) {
            S = 27;

            for (int i=0; i<8; i++) {
                N[i] = 0;
            }
            N[0] = 1;
        }

        if (S == 27) {
            S = 28;

            for (int i=0; i<8; i++) {
                P[i] = 0;
            }
        }

        if (S == 28) {
            S = 29;

            for (int i=0; i<8; i++) {
                Q[i] = 0;
            }
        }

        if (S == 29) {
            S = 30;

            B[0] = 1;
            B[1] = 0;
            B[2] = 1;
            B[3] = 0;
            B[4] = 0;
            B[5] = 1;
            B[6] = 1;
            B[7] = 1;
        }      

        if (S == 30) {
            S = 31;
            c = 0;

            for (int i=0; i<8; i++) {
            if (B[i] == 0) {
                if (I[i] == 0) {
                    if (c == 1) {
                        B[i] = 1;
                        c = 0;
                    }
                }

                else {
                    if (c == 0) {
                        B[i] = 1;
                        c = 0;
                    }
                }
            }
            
            else {
                if (I[i] == 0) {
                    if (c == 1) {
                        B[i] = 0;
                        c = 1;
                    }
                }

                else {
                    if (c == 0) {
                        B[i] = 0;
                        c = 1;
                    }
                }
            }
            }
        }  

        if (S == 31) {
            S = 32;

            int check = 0;
            for (int i=0; i<8; i++) {
                if (B[i] == 1) {
                    check = 1;
                }
            }

            printf("[+] count_%d : ", count++);
            for(int j=7; j>=0; j--) {
                printf("%d", Q[j]);
            }
            printf("\n");

            if (check == 0) {
                S = 56;
            }
        }

        if (S == 32) {
            S = 33;

            for (int i=0; i<8; i++) {
                B[i] = 0;
            }
            B[7] = 1;
        }

        if (S == 33) {
            S = 34;
            c = 0;

            for (int i=0; i<8; i++) {
            if (B[i] == 0) {
                if (I[i] == 0) {
                    if (c == 1) {
                        B[i] = 1;
                        c = 0;
                    }
                }

                else {
                    if (c == 0) {
                        B[i] = 1;
                        c = 0;
                    }
                }
            }

            else {
                if (I[i] == 0) {
                    if (c == 1) {
                        B[i] = 0;
                        c = 1;
                    }
                }

                else {
                    if (c == 0) {
                        B[i] = 0;
                        c = 1;
                    }
                }
            }
            }
        }

        if (S == 34) {
            S = 35;

            for (int i=0; i<8; i++) {
            l[i] = 0;

            if (B[i] == 1) {
                l[i] = 1;
            }

            else {
                l[i] = 0;
            }
            }

            for (int i=0; i<8; i++) {
            if (LD(l, i) == 1) {
                A[i] = 1;
            }

            else {
                A[i] = 0;
            }
            }
        }

        if (S == 35) {
            S = 36;

            for (int i=0; i<8; i++) {
            l[i] = 0;
            if (I[i] == 1) {
                l[i] = 1;
            }

            else {
                l[i] = 0;
            }
            }

            for (int i=0; i<8; i++) {
            if (LD(l, i) == 1) {
                B[i] = 1;
            }

            else {
                B[i] = 0;
            }
            }
        }

        if (S == 36) {
            S = 37;

            R[0] = 1;
            for (int i=1; i<8; i++) {
                R[i] = 0;
            }
        }

        if (S == 37) {
            S = 12;
        }

        if (S == 38) {
            S = 39;

            for (int i=0; i<8; i++) {
            if (M[i] == 1) {
                O[i] = 1;
            }

            else {
                O[i] = 0;
            }
            }
        }

        if (S == 39) {
            S = 40;
            c = 0;

            for (int i=0; i<8; i++) {
            if (O[i] == 0) {
                if (N[i] == 0) {
                    if (c == 1) {
                        O[i] = 1;
                        c = 0;
                    }
                }

                else {
                    if (c == 0) {
                        O[i] = 1;
                        c = 0;
                    }
                }
            }

            else {
                if (N[i] == 0) {
                    if (c == 1) {
                        O[i] = 0;
                        c = 1;
                    }
                }

                else {
                    if (c == 0) {
                        O[i] = 0;
                        c = 1;
                    }
                }
            }
            }
        }

        if (S == 40) {
            S = 41;
            
            for (int i=0; i<8; i++) {
            if (N[i] == 1) {
                M[i] = 1;
            }

            else {
                M[i] = 0;
            }
            }
        }

        if (S == 41) {
            S = 42;

            for (int i=0; i<8; i++) {
            if (O[i] == 1) {
                N[i] = 1;
            }

            else {
                N[i] = 0;
            }
            }
        }

        if (S == 42) {
            S = 43;
            c = 0;

            for (int i=0; i<8; i++) {
            if (A[i] == 0) {
                if (M[i] == 0) {
                    if (c == 1) {
                        A[i] = 1;
                        c = 0;
                    }
                }

                else {
                    if (c == 0) {
                        A[i] = 1;
                        c = 0;
                    }
                }
            }

            else {
                if (M[i] == 0) {
                    if (c == 1) {
                        A[i] = 0;
                        c = 1;
                    }
                }

                else {
                    if (c == 0) {
                        A[i] = 0;
                        c = 1;
                    }
                }
            }
            }
        }

        if (S == 43) {
            S = 44;

            for (int i=0; i<8; i++) {
                B[i] = 0;
            }

            B[5] = 1;
        }

        if (S == 44) {
            S = 45;
            c = 0;

            for (int i=0; i<8; i++) {
            if (B[i] == 0) {
                if (I[i] == 0) {
                    if (c == 1) {
                        B[i] = 1;
                        c = 0;
                    }
                }

                else {
                    if (c == 0) {
                        B[i] = 1;
                        c = 0;
                    }
                }
            }

            else {
                if (I[i] == 0) {
                    if (c == 1) {
                        B[i] = 0;
                        c = 1;
                    }                    
                }

                else {
                    if (c == 0) {
                        B[i] = 0;
                        c = 1;
                    }
                }
            }
            }
        }

        if (S == 45) {
            S = 46;

            for (int i=0; i<8; i++) {
            l[i] = 0;
            if (B[i] == 1) {
                l[i] = 1;
            }

            else {
                l[i] = 0;
            }
            }

            for (int i=0; i<8; i++) {
            if (LD(l, i) == 1) {
                C[i] = 1;
            }
            
            else {
                C[i] = 0;
            }
            }
        }

        if (S == 46) {
            S = 47;

            for (int i=0; i<8; i++) {
            if (C[i] == 1) {
                if (A[i] == 1) {
                    A[i] = 0;
                }

                else {
                    A[i] = 1;
                }
            }
            }
        }

        if (S == 47) {
            S = 48;
            c = 0;

            for (int i=0; i<8; i++) {
            if (P[i] == 0) {
                if (A[i] == 0) {
                    if (c == 1) {
                        P[i] = 1;
                        c = 0;
                    }
                }

                else {
                    if (c == 0) {
                        P[i] = 1;
                        c = 0;
                    }
                }
            }

            else {
                if (A[i] == 0) {
                    if (c == 1) {
                        P[i] = 0;
                        c = 1;
                    }
                }

                else {
                    if (c == 0) {
                        P[i] = 0;
                        c = 1;
                    }
                }
            }
            }
        }

        if (S == 48) {
            S = 49;

            for (int i=0; i<8; i++) {
                B[i] = 0;
            }

            B[6] = 1;
        }

        if (S == 49) {
            S = 50;
            c = 0;

            for (int i=0; i<8; i++) {
            if (B[i] == 0) {
                if (I[i] == 0) {
                    if (c == 1) {
                        B[i] = 1;
                        c = 0;
                    }
                }

                else {
                    if (c == 0) {
                        B[i] = 1;
                        c = 0;
                    }
                }
            }

            else {
                if (I[i] == 0) {
                    if (c == 1) {
                        B[i] = 0;
                        c = 1;
                    }
                }

                else {
                    if (c == 0) {
                        B[i] = 0;
                        c = 1;
                    }
                }
            }
            }
        }

        if (S == 50) {
            S = 51;
            
            for (int i=0; i<8; i++) {
            l[i] = 0;
            if (B[i] == 1) {
                l[i] = 1;
            }

            else {
                l[i] = 0;
            }
            }

            for (int i=0; i<8; i++) {
            if (LD(l, i) == 1) {
                A[i] = 1;
            }

            else {
                A[i] = 0;
            }
            }
        }

        if (S == 51) {
            S = 52;

            for (int i=0; i<8; i++) {
            if (P[i] == 1) {
                if (A[i] == 1) {
                    A[i] = 0;
                }

                else {
                    A[i] = 1;
                }
            }
            }
        }

        if (S == 52) {
            S = 53;

            for (int i=0; i<8; i++) {
            if (Q[i] == 0) {
                if (A[i] == 1) {
                    Q[i] = 1;
                }
            }
            }
        }

        if (S == 53) {
            S = 54;

            for (int i=0; i<8; i++) {
                A[i] = 0;
            }

            A[0] = 1;
        }

        if (S == 54) {
            S = 55;
            c = 0;

            for (int i=0; i<8; i++) {
            if (I[i] == 0) {
                if (A[i] == 0) {
                    if (c == 1) {
                        I[i] = 1;
                        c = 0;
                    }
                }
                
                else {
                    if (c == 0) {
                        I[i] = 1;
                        c = 0;
                    }
                }
            }

            else {
                if (A[i] == 0) {
                    if (c == 1) {
                        I[i] = 0;
                        c = 1;
                    }
                }

                else {
                    if (c == 0) {
                        I[i] = 0;
                        c = 1;
                    }
                }
            }
            }

            
        }

        if (S == 55) {
            S = 29;
        }
        
        if (S == 56) {
            S = 57;

            int check = 0;
            for (int i=0; i<8; i++) {
                if (Q[i] == 1) {
                    check = 1;
                }
            }

            if (check == 0) {
                S = 58;
            }
        }

        if (S == 57) {
            S = 58;
            INVALID_FLAG = 1;
            //printf("INVALID_FLAG\n");
            break;
        }

        if (S == 58) {
            S = -1;
        }
    } // while

    if (INVALID_FLAG == 1) {
        printf("FAILURE\n");
    }

    else {
        printf("SUCCESS\n");
    }
}