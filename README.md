# niva
Non-Invasive Vascular Analyzer

# System Requirements
Please make sure you have same architecture between python and GCC compiler (MinGW in windows). 
If you have installed python 64-bit, make sure you had install MinGW-w64.
## Installation Specification
  - Python 3.6.6 64-bit
  - mingw-w64 x86_64-8.1.0-posix-seh-rt_v6-rev0
  
## How to Compile C Source Code
on macOS

```sh
$ gcc -Wall -fPIC -c flags.c
$ gcc -shared -Wl,-install_name,libflags.so.1 -o libflags.so flags.o
```

on Linux 

```sh
$ gcc -Wall -fPIC -c flags.c
$ gcc -shared -Wl,-soname,libflags.so.1 -o libflags.so flags.o
```

on Windows

```sh
> gcc -Wall -fPIC -c flags.c
> gcc -shared -Wl,-soname,libflags.so.1 -o libflags.dll flags.o
```