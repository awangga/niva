# niva
Non-Invasive Vascular Analyzer

# Installation Compiler
gcc -Wall -fPIC -c flags.c
gcc -shared -Wl,-install_name,libflags.so.1 -o libflags.so flags.o


if in linux use soname rather than install_name