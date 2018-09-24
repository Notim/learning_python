from televisoes import Televisao

tv = Televisao(2, 50)
while True:
    opt = input()
    if(opt == "d"):
        tv.Ch("d")

    elif(opt == "a"):
        tv.Ch("u")

    elif (opt == "o"):
        tv.off()

    else:
        tv.changeCh(opt)

