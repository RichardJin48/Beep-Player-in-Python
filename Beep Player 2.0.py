def tempo(t):
    time = 4 * 60000 / t
    return time

def key(k):
    keyName = {"C":0, "Db":1, "D":2, "Eb":3, "E":4, "F":5, "Gb":6, "G":-5, "Ab":-4, "A":-3, "Bb":-2, "B":-1}
    base = (2 ** (1 / 12)) ** keyName[k]
    return base

def note(x,y,k,t):
    base = key(k)
    pitch = {1:523, 2:587, 3:659, 4:698, 5:784, 6:880, 7:988}
    octave = x // 10
    if octave >= 0:
        tune = x % 10
        if tune == 8:
            tune = octave % 10
            octave = octave // 10
            x = int(pitch[tune] * base * (2 ** octave) / (2 ** (1 / 12)))
        elif tune == 9:
            tune = octave % 10
            octave = octave // 10
            x = int(pitch[tune] * base * (2 ** octave) * (2 ** (1 / 12)))
        elif tune == 0:
            x = 20000
        else:
            x = int(pitch[tune] * base * (2 ** octave))
    elif octave < 0:
        tune = 10 - x % 10        
        if tune == 8:
            tune = 9 - octave % 10
            octave = octave // 10
            x = int(pitch[tune] * base * (2 ** octave) / (2 ** (1 / 12)))
        elif tune == 9:
            tune = 9 - octave % 10
            octave = octave // 10
            x = int(pitch[tune] * base * (2 ** octave) * (2 ** (1 / 12)))
        else:
            x = int(pitch[tune] * base * (2 ** octave))
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
    note = [x,y]
    return note

def playNote(x,y,k,t):
    from winsound import Beep
    n = note(x,y,k,t)
    Beep(n[0],n[1])

def writeNote(x,y,k,t):
    n = note(x,y,k,t)
    x = str(n[0])
    y = str(n[1])
    if x != "20000":
        write = "    tone(buzzerPin," + x + ");" + "\n" + "    delay(" + y + ");" + "\n"
    else:
        write = "    noTone(buzzerPin);" + "\n" + "    delay(" + y + ");" + "\n"
    return write

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
            playNote(x,y,k,t)
    file.close()

def arduino(name):
    file = open(name + ".txt")
    newFile = open(name + ".ino","w")
    newFile.write("const int buzzerPin = 7;" + "\n")
    newFile.write("int fre;" + "\n" + "\n")
    newFile.write("void setup() {" + "\n")
    newFile.write("  pinMode(buzzerPin,OUTPUT);" + "\n" + "}" + "\n" + "\n")
    newFile.write("void loop() {" + "\n")
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
            write = writeNote(x,y,k,t)
            newFile.write(write)
    newFile.write("}")
    file.close()
    newFile.close()

print("欢迎使用Beep Player 2.0")
while True:
    print("主菜单: ")
    print("1. 播放音乐")
    print("2. 生成 Arduino 代码")
    print("3. 退出")
    do = int(input("请输入操作序号: "))
    if do == 1:
        name = input("请输入乐谱文件名: ")
        print("正在播放")
        playMusic(name)
        print("播放结束")
    if do == 2:
        name = input("请输入乐谱文件名: ")
        print("正在生成代码")
        arduino(name)
        print("完成！")
    if do == 3:
        break
print("程序已退出，感谢使用！")
