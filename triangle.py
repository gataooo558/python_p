from turtle import *
from collections import deque
len = 600 #600進む
stX = -250 #x座標は250 
stY = -250 #Y座標は250

#スタート地点に戻る
def setHome():
    setheading(0)#東に向きを設定
    penup()
    setposition(stX,stY)#stX,stYへ戻る
    pendown()
#指定した場所に移動して方向を水平に変更
def setXY(x,y):
    setheading(0)#東に向きを設定
    penup()
    setposition(x,y)#stX,stYへ戻る
    pendown()

#最初に一度だけ描く大きい三角形
def drawBigTri(l):#大きい三角形を描く
    setHome()
    fillcolor('blue')#青で塗りつぶし
    begin_fill()
    for _ in range(3):#3回繰り返す
        fd(l)
        rt(240)#右に向きを変える
    end_fill()

#再帰で小さい三角形を描画
def drawTri(l):#三角形を描く
    l /= 2
    qq = []#qqに[]を代入する
    for q in Q:
        qq.append(q)#最後にqを追加する
    for q in qq:
        setXY(q[0],q[1])
        fd(l)#前に進む
        rt(300)#右に向きを変える
        Q.append(list(position()))
        fillcolor('white')#白で塗りつぶし
        begin_fill()
        for i in range(3):#3回繰り返す
            if i == 2: Q.append(list(position()))#iと2が等しい場合Qを原点に戻す
            fd(l)
            rt(240)#右に向きを変える
        end_fill()
    drawTri(l)#三角形を描く

speed(0)
drawBigTri(len)
Q = deque()
Q.append([stX,stY])#座標のX,Yを追加
drawTri(len)
done()