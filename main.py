from ctypes import *

mylib=CDLL("./libflags.dll")
#mylib=WinDLL("./libflag.dll")
asalpesan="saya ganteng"
mylib.welcome_msg(asalpesan.encode("ascii"))
mylib.echo.restype = c_char_p
pesan=mylib.echo(asalpesan.encode("ascii"))
mylib.set_flag(777)
bendera=mylib.get_flag()
print(pesan.decode("utf-8"))
print(bendera)

