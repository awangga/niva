from ctypes import *

mylib=CDLL("./libflags.so")
mylib.welcome_msg("saya ganteng")
pesan=mylib.echo("saya ganteng")
mylib.set_flag(777)
bendera=mylib.get_flag()
print(pesan)
print(bendera)

