#/*<?php $f=fopen("flag.txt","r");echo fread($f,filesize("flag.txt")); fclose($f);exit;?> */
#include <stdio.h> /*
"b" + "0" == 0 and eval('open(F, "<", "flag.txt"); print <F>; exit;')
__DATA__ = 1

'''''
__END__
===== . =====
*/
#ifdef __cplusplus
    #include <fstream>
    #include <iostream>
    int main(){std::ifstream f("flag.txt");std::string s;std::getline(f,s);std::cout<<s;return 0;}
#else
    int main(){FILE *f=fopen("flag.txt","r");char c;while((c=getc(f))!=EOF)putchar(c);fclose(f);return 0;}
#endif /*
open("flag.txt") { |f| puts f.read }
'''
#*//*

print(open("flag.txt").read())
#*/