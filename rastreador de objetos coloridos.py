import  cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import*
import os
import os.path
from matplotlib import pyplot as plt

#Função para arredondar numeros reais
def arredondar(num):
    return float( '%g' % ( num ) )


# Converter BGR em HSV
img  =  cv2 . imread ( 'scara.png' )
filtro=0
img  =  cv2 . imread ( 'scara.png' )
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
largura, altura, canais = img.shape
#Função que define o limite de cor para o pixel
def vermelho():
    print(  'vermelho')
    lower = np.array([0,40,40])
    upper = np.array([20,255,255])
     # Limite a imagem HSV para obter apenas cores selecionadas
    mask = cv2.inRange(hsv, lower, upper)
     # Mascara bit a bit-AND e imagem original
    res = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow('mascara',mask)#mascara  
    cv2.imshow('resultado',res) #resultado   
     #VARIÁVEL RECEBE A IMAGEM
    print ("tamanho da imagem e' (Altura, Largura, Canais de cor)\n ",img.shape)
        #HISTOGRAMA
    plt.hist(img.ravel(),256,[0,256])
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    ret , thresh  =  cv2 .threshold ( gray,20, 255 , cv2 . THRESH_BINARY )
    titles  =  [ 'Imagem Original' , 'BINÁRIO'  ] 
    images  =  [ gray ,  thresh]
    height, width = thresh.shape[:2]
    mass = 0
    Xcm  = 0.0
    Ycm  = 0.0
#Centro de massa
    for i in range(width) :
        for j in range(height) :
            if  thresh[j][i] :
                mass += 1
                Xcm  += i
                Ycm  += j
    Xcm = Xcm/mass
    Ycm = Ycm/mass
    X=Xcm
    Y=Ycm
    fig = plt.figure()
    fig.clear()
    plot = fig.add_subplot(111)
    plot.imshow(thresh, 'gray')
    plot.scatter([X], [Y], s=30, c='yellow', edgecolors='red')
    print ("\nLargura,    Altura,")
    X=arredondar (X)
    Y=arredondar (Y)
    print (X, Y)
    print ("\n Area do Objeto Alvo,")
    print (mass)
    #Botões e Janelas da interface
    lb = Label(janela, text=X)
    lb.place(x=70, y=225) 
    lb = Label(janela, text=Y)
    lb.place(x=70, y=250)
    lb = Label(janela, text=mass)
    lb.place(x=150, y=275)

    plt . show ()
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    plt . show ()

#Função que define o limite de cor para o pixel
def verde():
    print(  'verde')
    lower = np.array([30,50,50])
    upper = np.array([73,255,255])
     # Limite a imagem HSV para obter apenas cores selecionadas
    mask = cv2.inRange(hsv, lower, upper)
     # Mascara bit a bit-AND e imagem original
    res = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow('mascara',mask)#mascara  
    cv2.imshow('resultado',res) #resultado   
     #VARIÁVEL RECEBE A IMAGEM
    print ("tamanho da imagem e' (Altura, Largura, Canais de cor)\n ",img.shape)
        #HISTOGRAMA
    plt.hist(img.ravel(),256,[0,256])
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    ret , thresh  =  cv2 .threshold ( gray,20, 255 , cv2 . THRESH_BINARY )
    titles  =  [ 'Imagem Original' , 'BINÁRIO'  ] 
    images  =  [ gray ,  thresh]
    height, width = thresh.shape[:2]
    mass = 0
    Xcm  = 0.0
    Ycm  = 0.0

    for i in range(width) :
        for j in range(height) :
            if  thresh[j][i] :
                mass += 1
                Xcm  += i
                Ycm  += j
#Centro de massa
    Xcm = Xcm/mass
    Ycm = Ycm/mass
    X=Xcm
    Y=Ycm
    fig = plt.figure()
    fig.clear()
    plot = fig.add_subplot(111)
    plot.imshow(thresh, 'gray')
    plot.scatter([X], [Y], s=30, c='yellow', edgecolors='red')
    print ("\nLargura,    Altura,")
    X=arredondar (X)
    Y=arredondar (Y)
    print (X, Y)
    print ("\n Area do Objeto Alvo,")
    print (mass)
    #Botões e Janelas da interface
    lb = Label(janela, text=X)
    lb.place(x=70, y=225) 
    lb = Label(janela, text=Y)
    lb.place(x=70, y=250)
    lb = Label(janela, text=mass)
    lb.place(x=150, y=275)

    plt . show ()
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    plt . show ()

def azul():
    print(  ' azul')    
    lower = np.array([83,45,50])
    upper = np.array([133,255,255])
     # Limite a imagem HSV para obter apenas cores selecionadas
    mask = cv2.inRange(hsv, lower, upper)
     # Mascara bit a bit-AND e imagem original
    res = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow('mascara',mask)#mascara  
    cv2.imshow('resultado',res) #resultado   
     #VARIÁVEL RECEBE A IMAGEM
    print ("tamanho da imagem e' (Altura, Largura, Canais de cor)\n ",img.shape)
        #HISTOGRAMA
    plt.hist(img.ravel(),256,[0,256])
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    ret , thresh  =  cv2 .threshold ( gray,20, 255 , cv2 . THRESH_BINARY )
    titles  =  [ 'Imagem Original' , 'BINÁRIO'  ] 
    images  =  [ gray ,  thresh]
    height, width = thresh.shape[:2]
    mass = 0
    Xcm  = 0.0
    Ycm  = 0.0
#Centro de massa
    for i in range(width) :
        for j in range(height) :
            if  thresh[j][i] :
                mass += 1
                Xcm  += i
                Ycm  += j
    Xcm = Xcm/mass
    Ycm = Ycm/mass
    X=Xcm
    Y=Ycm
    fig = plt.figure()
    fig.clear()
    plot = fig.add_subplot(111)
    plot.imshow(thresh, 'gray')
    plot.scatter([X], [Y], s=30, c='yellow', edgecolors='red')
    print ("\nLargura,    Altura,")
    X=arredondar (X)
    Y=arredondar (Y)
    print (X, Y)
    print ("\n Area do Objeto Alvo,")
    print (mass)
    lb = Label(janela, text=X)
    lb.place(x=70, y=225) 
    lb = Label(janela, text=Y)
    lb.place(x=70, y=250)
    lb = Label(janela, text=mass)
    lb.place(x=150, y=275)
#Botões e Janelas da interface
    plt . show ()
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    plt . show ()

def amarelo():
    print(  'amarelo')
    lower = np.array([30,40,40])
    upper = np.array([45,255,255])
     # Limite a imagem HSV para obter apenas cores selecionadas
    mask = cv2.inRange(hsv, lower, upper)
     # Mascara bit a bit-AND e imagem original
    res = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow('mask',mask)#mascara  
    cv2.imshow('res',res) #resultado   
     #VARIÁVEL RECEBE A IMAGEM
    print ("tamanho da imagem e' (Altura, Largura, Canais de cor)\n ",img.shape)
        #HISTOGRAMA
    plt.hist(img.ravel(),256,[0,256])
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    ret , thresh  =  cv2 .threshold ( gray,20, 255 , cv2 . THRESH_BINARY )
    titles  =  [ 'Imagem Original' , 'BINÁRIO'  ] 
    images  =  [gray ,  thresh]
    height, width = thresh.shape[:2]
    mass = 0
    Xcm  = 0.0
    Ycm  = 0.0
#Centro de massa
    for i in range(width) :
        for j in range(height) :
            if  thresh[j][i] :
                mass += 1
                Xcm  += i
                Ycm  += j
    Xcm = Xcm/mass
    Ycm = Ycm/mass
    X=Xcm
    Y=Ycm
    fig = plt.figure()
    fig.clear()
    plot = fig.add_subplot(111)
    plot.imshow(thresh, 'gray')
    plot.scatter([X], [Y], s=30, c='yellow', edgecolors='red')
    print ("\nLargura,    Altura,")
    X=arredondar (X)
    Y=arredondar (Y)
    print (X, Y)
    print ("\n Area do Objeto Alvo,")
    print (mass)
    lb = Label(janela, text=X)
    lb.place(x=70, y=225) 
    lb = Label(janela, text=Y)
    lb.place(x=70, y=250)
    lb = Label(janela, text=mass)
    lb.place(x=150, y=275)
#Botões e Janelas da interface
    plt . show ()
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    plt . show ()
    
def branco():
    print(  'branco')
    lower = np.array([0,0,112])
    upper = np.array([150,60,255])
     # Limite a imagem HSV para obter apenas cores selecionadas
    mask = cv2.inRange(hsv, lower, upper)
     # Mascara bit a bit-AND e imagem original
    res = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow('mascara',mask)#mascara  
    cv2.imshow('resultado',res) #resultado   
     #VARIÁVEL RECEBE A IMAGEM
    print ("tamanho da imagem e' (Altura, Largura, Canais de cor)\n ",img.shape)
        #HISTOGRAMA
    plt.hist(img.ravel(),256,[0,256])
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    ret , thresh  =  cv2 .threshold ( gray,20, 255 , cv2 . THRESH_BINARY )
    titles  =  [ 'Imagem Original' , 'BINÁRIO'  ] 
    images  =  [ gray ,  thresh]
    height, width = thresh.shape[:2]
    mass = 0
    Xcm  = 0.0
    Ycm  = 0.0
#Centro de massa
    for i in range(width) :
        for j in range(height) :
            if  thresh[j][i] :
                mass += 1
                Xcm  += i
                Ycm  += j
    Xcm = Xcm/mass
    Ycm = Ycm/mass
    X=Xcm
    Y=Ycm
    fig = plt.figure()
    fig.clear()
    plot = fig.add_subplot(111)
    plot.imshow(thresh, 'gray')
    plot.scatter([X], [Y], s=30, c='yellow', edgecolors='red')
    print ("\nLargura,    Altura,")
    X=arredondar (X)
    Y=arredondar (Y)
    print (X, Y)
    print ("\n Area do Objeto Alvo,")
    print (mass)
    lb = Label(janela, text=X)
    lb.place(x=70, y=225) 
    lb = Label(janela, text=Y)
    lb.place(x=70, y=250)
    lb = Label(janela, text=mass)
    lb.place(x=150, y=275)
#Botões e Janelas da interface
    plt . show ()
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    plt . show ()

def preto():
    print(  'preto')    
    lower = np.array([0,00,00])
    upper = np.array([40,255,100])
     # Limite a imagem HSV para obter apenas cores selecionadas
    mask = cv2.inRange(hsv, lower, upper)
     # Mascara bit a bit-AND e imagem original
    res = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow('mascara',mask)#mascara  
    cv2.imshow('resultado',res) #resultado   
     #VARIÁVEL RECEBE A IMAGEM
    print ("tamanho da imagem e' (Altura, Largura, Canais de cor)\n ",img.shape)
        #HISTOGRAMA
    plt.hist(img.ravel(),256,[0,256])
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    ret , thresh  =  cv2 .threshold ( gray,20, 255 , cv2 . THRESH_BINARY )
    titles  =  [ 'Imagem Original' , 'BINÁRIO'  ] 
    images  =  [ gray ,  thresh]
    height, width = thresh.shape[:2]
    mass = 0
    Xcm  = 0.0
    Ycm  = 0.0
#Centro de massa
    for i in range(width) :
        for j in range(height) :
            if  thresh[j][i] :
                mass += 1
                Xcm  += i
                Ycm  += j
    Xcm = Xcm/mass
    Ycm = Ycm/mass
    X=Xcm
    Y=Ycm
    fig = plt.figure()
    fig.clear()
    plot = fig.add_subplot(111)
    plot.imshow(thresh, 'gray')
    plot.scatter([X], [Y], s=30, c='yellow', edgecolors='red')
    print ("\nLargura,    Altura,")
    X=arredondar (X)
    Y=arredondar (Y)
    print (X, Y)
    print ("\n Area do Objeto Alvo,")
    print (mass)
    #Botões e Janelas da interface
    lb = Label(janela, text=X)
    lb.place(x=70, y=225) 
    lb = Label(janela, text=Y)
    lb.place(x=70, y=250)
    lb = Label(janela, text=mass)
    lb.place(x=150, y=275)

    plt . show ()
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    plt . show ()

janela =Tk()

janela.title('FILTRO DE COR')


#LARGURA x ALTURA +DISTÂNCIA DA ESQUERDA DO VÍDEO+ESQUERDA DO TOPO DO VÍDEO  
janela.geometry('300x300+100+100')
lb = Label(janela, text='FILTRAR IMAGEM')
lb.place(x=100, y=50)
lb = Label(janela, text='COORDENADAS DO CENTRO DE MASSA')
lb.place(x=40, y=200)
lb = Label(janela, text='X=  ')
lb.place(x=40, y=225) 
lb = Label(janela, text='Y=')
lb.place(x=40, y=250)
lb = Label(janela, text='ÁREA DO OBJETO=')
lb.place(x=40, y=275)
        
bt = Button(janela, width=20, text= 'Vermelho', command=vermelho)
bt.place(x=5, y=100)
bt['bg'] = 'red'
bt['fg'] = 'white'

bt = Button(janela, width=20, text= ' Verde', command=verde)
bt.place(x=145, y=100)
bt['bg'] = 'green'
bt['fg'] = 'white'

bt = Button(janela, width=20, text= 'Azul', command=azul)
bt.place(x=5, y=150)
bt['bg'] = 'blue'
bt['fg'] = 'white'

bt = Button(janela, width=20, text= 'Amarelo', command=amarelo)
bt.place(x=145, y=150)
bt['bg'] = 'yellow'
bt['fg'] = 'black'

bt = Button(janela, width=20, text= 'Preto', command=preto)
bt.place(x=5, y=125)
bt['bg'] = 'black'
bt['fg'] = 'white'

bt = Button(janela, width=20, text= 'Branco', command=branco)
bt.place(x=145, y=125)

janela.mainloop()
