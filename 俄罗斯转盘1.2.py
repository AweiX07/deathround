#俄罗斯转盘————基于tkinter图形化库的PLUS实现
#提示：最好使用命令控制台窗口运行本程序（在Thonny中可以按Ctrl+T）
#version=1.2
#作者：<Duan Yuyang @ AweiX07@163.com>
#如要引用，请删除作者信息

if __name__ != "__main__":#先看一眼自己是不是 被 骗 了
    exit()

def qrror(text):#报错退出函数
    print(text)
    exit()

def extra_text_file():#Debug
    e=open("test.txt","wb")
    e.write("This is a test file.".encode("UTF-8"))
    e.close()

def trytofix(m):#基于pip
    if input("是否尝试自动修复(使用pip)？(Y/n)") == "Y":
        from os import system
        system("pip install "+m)
        return 1
    else:return 0

#导入相关模块
modulelist=["tkinter",
            "os",
            "sys",
            "random",
            "time",
            "platform",
            #"t"#debug
            ]
for i in modulelist:
    try:exec("import "+i)
    except ModuleNotFoundError:
        print("错误：导入库文件“"+i+"”失败")
        if trytofix(i):
            print("导入重试中...")
            try:exec("import "+i)
            except ModuleNotFoundError:
                print("修复失败")
                qrror("程序启动失败，请尝试安装相关依赖库")
        else:qrror("程序启动失败，请尝试安装相关依赖库")
    except Exception as e:qrror("程序启动时遇到了未知错误:"+str(e))
sysname=platform.system()
del platform#再也用不到

def die():#随机惩罚函数
    global random
    global os
    global tkinter
    def shutdown():#让关机跨平台
        global sysname
        global os
        global random
        if sysname == "Windows":os.system("shutdown /s /t "+str(random.randint(0,120)))
        else:os.system("shutdown -h "+str(random.randint(0,2)))#通常Unix操作系统用的都是这个命令
    def hidefiles():#文件"消失术"（原理很糙，在Windows下无效）
        global os
        targets=os.listdir(os.getcwd())
        for i in targets:
            os.rename(i,"."+i)#在Linux和macOS下，隐藏文件就是在文件名前加一个点
    #def close_window():#关闭窗口
    #    global exc
    #    exc.destroy()
    execution_list=[
        ("shutdown()","你的电脑将在一定时间内关机（也可能是立即）\n你可以想办法终止关机进程，\n比如运行shutdown -a或者shutdown -c"),
        ("os.system(\"xflock4\")","你在使用xfce4吗？\n是的话可能会被锁屏哦 :)"),#Linux无桌面用户表示无所畏惧（然而我不是QAQ）
        #("hidefiles","刚才变了个魔法，\n快去看看你的文件（嘻嘻）"),#实在太恐怖了，所以注释掉不做演示
        ("print(\"\",end=\"\")","不是吧哥们，\n你怎么能这么菜？\n（无情嘲笑）")#啊啊啊实在想不出来啦！！！
        ]
    execution=random.choice(execution_list)
    exc=tkinter.Tk()
    exc.title("==EXECUTION==")
    exc.geometry("350x100")
    text=tkinter.Label(exc,text=execution[1])
    text.pack()
    #print(execution)#debug
    exec(execution[0])#执行惩罚，如果不需要请注释掉
    #print(execution[0])
    exc.protocol("WM_DELETE_WINDOW",quit)
    exc.mainloop()
    exit()
'''
#FilesDocter.py
#hidefiles()这是一个很恶心的惩罚。
#如果这个惩罚对您造成了不幸，请将以下代码复制到同目录下的新Python代码文件中运行:
import os
targets=os.listdir(os.getcwd())
for i in targets:
    if i[0] == ".":
        os.rename(i,i[1:])
        print("FIXED:"+i+" => "+i[1:])
print("finish")
'''

def DEATH():#古希腊掌管死亡的神
    global random
    lister=[]
    i=0#总数
    t=0#有弹数
    while i <= random.randint(3,30):#其实这是把巨轮手枪(Doge)
        lister.append([0,1][random.randint(0,1)])#0为无，1为有
        if lister[-1]:t+=1
        i+=1
    #print(i)
    #print(lister)
    return(t,i,lister)

gui=tkinter.Tk()#GUI图形化
gui.title("俄罗斯转盘")#设置标题
gui.geometry("300x260")

#生成轮盘
b=0
a=0
checker=1
#总得给人留条活路
while b == a or checker:
    b,a,g=DEATH()#弹，总，枪
    checker=a-b<b#在这种情况下，按玩法根本不可能获胜

title=tkinter.Label(gui,text="俄罗斯转盘\n玩法：打掉一发弹掉一发")
title.pack()

matter=tkinter.Label(gui,text="该枪可装"+str(a)+"发子弹\n有"+str(b)+"实弹")
matter.pack()

result=tkinter.Label(gui,text="游戏开始 =)",fg="blue")
result.pack()

def bun():#玩家开枪啦！
    global b
    global a
    global g
    global random
    global time
    global result
    if g[0]:
        result.configure(text=random.choice(["呃啊！","中枪了！","哦不！","是实弹！","很不幸..."]),fg="red")
        time.sleep(0.5)
        die()
        '''
        b=0
        a=0
        while b == a:b,a,g=DEATH()
        result=tkinter.Label(gui,text="新的一轮 =)",fg="blue")
        result.pack()
        '''
    else:
        result.configure(text=random.choice(["逃过一劫","空的","空弹","诶嘿没事"]),fg="green")
        g=g[1:]
        if len(g) <= 1:
            global fire
            fire.destroy()
            global sch
            sch.configure(text="退出",command=quit)
            result.configure(text="恭喜你通过了死神的考验！",fg="yellow")
        else:
            g=g[1:]
            result.configure(text=random.choice(["逃过一劫","空的","空弹","诶嘿没事"]),fg="green")
        #print(g)#debug
def swich():
    #print("swiching")#debug
    global g
    global a
    global random
    global result
    for i in range(1,random.randint(1,10),1):
        i=random.randint(0,a)
        g=g[i:]+g[:i]
        #print("running")#debug
    #print("OK")#debug
    #print(g)#debug
    result.configure(text=random.choice(["呼...","幸运之神，眷顾我！","感觉好点了","你又充满了决心","现在不怕了","滚轮停下了"]),fg="blue")

fire=tkinter.Button(gui,text="开一枪！",command=bun)
fire.pack()

sch=tkinter.Button(gui,text="风水轮流转！",command=swich)
sch.pack()

gui.mainloop()#开始程序主循环