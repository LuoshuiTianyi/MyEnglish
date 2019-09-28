#!/usr/bin/python3
from random import *
import os
words = []
lse = []
lsz = []
def FileInput():
    os.system("clear")
    print("请输入笔记文件日期: (year,month,day)")
    year=input()
    month=input()
    day=input()
    fl=open("/home/luoshuitianyi/Notebook/English/%s/%s/%s.note"%(year,month,day), "r")
    note=fl.readlines()
    n=len(note)//2
    for i in range(0,n):
        words.append([note[i * 2].strip("\n"), note[i * 2 + 1].strip("\n")])
    os.system("clear")
def Init():
    print("以下是这份笔记的内容：")
    print()
    for word in words:
        print(word[0].ljust(50), word[1])
    os.system("clear")
    lim=int(input("请输入记忆次数："))
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
    print("第一轮：en -> zh  (rest : %s)\n----------------------------------------------"%len(lse))
    now = choice(lse)
    print(now[0])
    res = input("记得吗? (y/n):  ")
    print()
    print("----------------------------------------------")
    print("以下是它的中文意思：\n")
    print(now[1], end="\n\n\n")
    if res[0] == "y":
        res = input("真的记清楚了吗?(y/n):  ")
        if res[0] == "y":
            lse.remove(now)
    else:
        lse.append(now)
while len(lsz):
    os.system("clear")
    print("第二轮：zh -> en  (rest : %s)\n----------------------------------------------"%len(lsz))
    now = choice(lsz)
    print(now[1], "\n")
    word = input("请输入单词:  ")
    if word == now[0]:
        print("\nAccept!")
        input()
        lsz.remove(now)
    else:
        print("\nWrong!")
        input()
