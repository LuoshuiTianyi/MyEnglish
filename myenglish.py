#!/usr/bin/python3
from random import *
import string
import os
words = []
lse = []
lsz = []
def FileInput():
    while True:
        os.system("clear")
        print("请输入笔记文件日期: (year,month,day)")
        year=input()
        month=input()
        day=input()
        try:
            fl=open("/home/luoshuitianyi/Notebook/English/%s/%s/%s.note"%(year,month,day), "r")
        except FileNotFoundError:
            print("没有这份笔记!")
        else:
            break
        finally:
            pass
    note=fl.readlines()
    n=len(note)//2
    global words
    words=[[note[i * 2].strip(), note[i * 2 + 1].strip()] for i in range(0,n)]
def Init():
    os.system("clear")
    print("以下是这份笔记的内容：")
    print()
    for word in words:
        print(word[0].ljust(50), word[1])
    input()
    os.system("clear")
    lim=int(input("请输入记忆次数：").strip())
    for i in range(0, lim):
        lse.extend(words)
        lsz.extend(words)
    for i in range(0, 100000):
        x=randint(0, lim - 1)
        y=randint(0, lim - 1)
        lse[x], lse[y] = lse[y], lse[x]
        lsz[x], lsz[y] = lsz[y], lsz[x]
FileInput()
Init()
while len(lse):
    os.system("clear")
    print("第一轮：en -> zh  (rest : %s)"%len(lse))
    now = choice(lse)
    cnt = 0;
    for i in now[1]:
        if i not in string.printable:
            cnt += 1;
    print()
    print(" ----------------------------------------------")
    print("|                                              |")
    print("|                                              |")
    print("|%s|"%now[0].center(46))
    print("|                                              |")
    print("|                                              |")
    print(" ----------------------------------------------")
    print()
    print()
    res = input("记得吗? (y/n):  ")
    print()
    print("------------- 以下是它的中文意思 --------------")
    print()
    print()
    print(" ----------------------------------------------")
    print("|                                              |")
    print("|                                              |")
    print("|%s|"%now[1].center(46 - cnt))
    print("|                                              |")
    print("|                                              |")
    print(" ----------------------------------------------")
    print()
    print()
    if len(res) == 0 or res[0] == "y":
        res = input("真的记清楚了吗?(y/n):  ")
        if len(res) == 0 or res[0] == "y":
            lse.remove(now)
    else:
        input()
        lse.append(now)
while len(lsz):
    os.system("clear")
    print("第二轮：zh -> en  (rest : %s)"%len(lsz))
    print()
    now = choice(lsz)
    cnt = 0;
    for i in now[1]:
        if i not in string.printable:
            cnt += 1;
    print(" ----------------------------------------------")
    print("|                                              |")
    print("|                                              |")
    print("|%s|"%now[1].center(46 - cnt))
    print("|                                              |")
    print("|                                              |")
    print(" ----------------------------------------------")
    print()
    print()
    word = input("请输入单词->   ")
    if word == now[0]:
        print("\nAccept!")
        input()
        lsz.remove(now)
    else:
        print("\nWrong!")
        print("正确单词 ->    %s"%now[0])
        input()
