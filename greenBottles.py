import time

bottles = -1
while bottles <0:
    bottles = int(input("how many green bottles?"))

for x in range(bottles,0,-1):
    print("{0} green bottles hanging on the wall.\n{0} green bottles hangijng on the wall.".format(x))
    print("and if 1 green bottle should accidently fall, \nThere'll be {0} green bottles hanging on the wall.\n".format(x-1))
    time.sleep(1.5)
