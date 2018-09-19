from ctypes import *

mylib=CDLL("./libflags.so")
asalpesan="saya ganteng"
mylib.welcome_msg(asalpesan.encode("ascii"))
pesan=mylib.echo(asalpesan.encode("ascii"))
mylib.set_flag(777)
bendera=mylib.get_flag()
print(pesan)
print(bendera)

