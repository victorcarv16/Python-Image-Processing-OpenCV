import  cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import mahotas
from tkinter import*
import os
import os.path
from matplotlib import pyplot as plt

#Função para arredondar numeros reais
def arredondar(num):
    return float( '%g' % ( num ) )
#Função para facilitar a escrita nas imagem
def escreve(img, texto, cor=(255,0,0)):
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, texto, (10,20), fonte, 0.5, cor, 0, cv2.LINE_AA)

# Converter BGR em HSV
img  =  cv2 . imread ( 'scara7.png' )
filtro=0
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
largura, altura, canais = img.shape
#Função que define o limite de cor para o pixel


#Função que define o limite de cor para o pixel
def verde():
    print(  'verde')
    lower = np.array([32,35,40])
    upper = np.array([173,255,255])
     # Limite a imagem HSV para obter apenas cores selecionadas
    mask = cv2.inRange(hsv, lower, upper)
     # Mascara bit a bit-AND e imagem original
    res = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow('mascara',mask)#mascara  
    cv2.imshow('resultado',res) #resultado
    #Passo 1: Conversão para tons de cinza
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
     #VARIÁVEL RECEBE A IMAGEM
    print ("tamanho da imagem e' (Altura, Largura, Canais de cor)\n ",img.shape)
    #Passo 2: Blur/Suavização da imagem
    suave = cv2.blur(gray, (9, 9))
    #Passo 3: Binarização resultando em pixels brancos e pretos
    T = mahotas.thresholding.otsu(suave)
    bin = suave.copy()
    bin[bin > T] = 255
    bin[bin < 255] = 0
    bin = cv2.bitwise_not(bin)

        #HISTOGRAMA
    plt.hist(img.ravel(),256,[0,256])
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
    print ("/n Largura,    Altura,")
    X=arredondar (X)
    Y=arredondar (Y)
    print (X, Y)
    print ("/n Area do Objeto Alvo,")
    print (mass,'mm²')

    
    #Passo 4: Detecção de bordas com Canny
    bordas = cv2.Canny(bin, 70, 150)
#Passo 5: Identificação e contagem dos contornos da imagem
#cv2.RETR_EXTERNAL = conta apenas os contornos externos
    
    (objetos, lx) = cv2.findContours (bordas.copy(),
    cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
    #A variável lx (lixo) recebe dados que não são utilizados
    
    escreve(gray, "Imagem em tons de cinza", 0)
    escreve(suave, "Suavizacao com Blur", 0)
    escreve(bin, "Binarizacao com Metodo Otsu", 255)
    escreve(bordas, "Detector de bordas Canny", 255)
    temp = np.vstack([ np.hstack([gray, suave]), np.hstack([bin, bordas]) ])
    cv2.imshow("Quantidade de objetos: "+str(len(objetos)), temp)
    print('OBJETOS ENCONTRADOS')
    print(len(objetos))
    
    cv2.waitKey(0)
    imgC2 = img.copy()
    cv2.imshow("Imagem Original", img)
    cv2.drawContours(imgC2, objetos, -1, (255, 0, 0), 2)
    escreve(imgC2, str(len(objetos))+" objetos encontrados!")
    cv2.imshow("Resultado", imgC2)
    cv2.waitKey(0)
    
    
    #Botões e Janelas da interface
    lb = Label(janela, text=X)
    lb.place(x=70, y=225) 
    lb = Label(janela, text=Y)
    lb.place(x=70, y=250)
    lb = Label(janela, text='s',mass)
    lb.place(x=230, y=275)

    plt . show ()
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    plt . show ()

janela =Tk()

janela.title('QUANTIFICADOR DE ÁREAS ARBORIZADAS')


#LARGURA x ALTURA +DISTÂNCIA DA ESQUERDA DO VÍDEO+ESQUERDA DO TOPO DO VÍDEO  
janela.geometry('450x300+100+100')
lb = Label(janela, text='RASTREAR ÁREAS')
lb.place(x=165, y=50)
lb = Label(janela, text='COORDENADAS DA ÁRVORE')
lb.place(x=40, y=200)
lb = Label(janela, text='X=  ')
lb.place(x=40, y=225) 
lb = Label(janela, text='Y=')
lb.place(x=40, y=250)
lb = Label(janela, text='ÁREA SUPERFICIAL DAS ÁRVORES=')
lb.place(x=40, y=275)
        
bt = Button(janela, width=20, text= 'Verde', command=verde)
bt.place(x=145, y=100)
bt['bg'] = 'green'
bt['fg'] = 'white'


janela.mainloop()
