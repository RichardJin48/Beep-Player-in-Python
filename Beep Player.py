def tempo(t):
    time = 4 * 60000 / t
    return time

def key(k):
    keyName = {"C":0, "Db":1, "D":2, "Eb":3, "E":4, "F":5, "Gb":6, "G":-5, "Ab":-4, "A":-3, "Bb":-2, "B":-1}
    base = (2 ** (1 / 12)) ** keyName[k]
    return base

def note(x,y,k,t):
    from winsound import Beep
    base = key(k)
    pitch = {-1:262, -2:294, -3:330, -4:349, -5:392, -6:440, -7:494, 1:523, 2:587, 3:659, 4:698, 5:784, 6:880, 7:988, 11:1046, 12:1175, 13:1318, 14:1397, 15:1568, 16:1760, 17:1976}
    if x == 0:
        x = 20000
    else:
        x = int(pitch[x] * base)
    time = tempo(t)
    timeType = y % 10
    if timeType == 0:
        y = y // 10
        y = int(time // y * 1.5)
    elif timeType == 3:
        y = y // 10
        y = int(time // y * (2 / 3))
    else:
        y = int(time // y)
    Beep(x,y)

def playMusic(name):
    file = open(name + ".txt")
    lines = file.readlines()
    for line in lines:
        line = line.strip("\n")
        line = line.split(",")
        line[1] = int(line[1])
        if line[0].isalpha():
            k = line[0]
            t = line[1]
        else:
            line[0] = int(line[0])
            x = line[0]
            y = line[1]
            note(x,y,k,t)
    file.close()

print("欢迎使用Beep Player")
while True:
    print("主菜单: ")
    print("1. 播放音乐")
    print("2. 退出")
    do = int(input("请输入操作序号: "))
    if do == 1:
        name = input("请输入乐谱文件名: ")
        print("正在播放")
        playMusic(name)
        print("播放结束")
    if do == 2:
        break
print("程序已退出，感谢使用！")
