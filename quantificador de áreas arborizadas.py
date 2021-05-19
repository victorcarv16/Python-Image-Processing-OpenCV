import  cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import mahotas
from tkinter import*
import os
import os.path
from matplotlib import pyplot as plt
import colorsys

#Função para arredondar numeros reais
def arredondar(num):
    return float( '%.2g' % ( num ) )
#Função para facilitar a escrita nas imagem
def escreve(img, texto, cor=(255,0,0)):
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, texto, (10,20), fonte, 0.5, cor, 0, cv2.LINE_AA)

#Calculando a escala
escala  =  cv2 . imread ( 'escala_20.png' )
escalay, escalax, c = escala.shape
fator_de_escala = (400/(escalax*escalax))
print ("fator de escala é ",fator_de_escala)
#20m=97pixels=>Área=20m*20m= 400m² =77*77=5929p²
#(400/5929)=>1p² = 0,06746500253m²


# Converter BGR em HSV
img  =  cv2 . imread ( 'Condominio1_escala_20.png' )
print ("tamanho da escala é (Altura, Largura, Canais de cor) ",escala.shape)
print ("tamanho da image é (Altura, Largura, Canais de cor) ",img.shape)
filtro=0
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
altura, largura, canais = img.shape


#Função que define o limite de cor para o pixel
def verde():
    print(  'Filtro de áreas verdes')
    #lower = np.array([76,35,35])
    lower = np.array([55,40,28])
    upper = np.array([103,98,96])

     # Limite a imagem HSV para obter apenas cores selecionadas
    mask = cv2.inRange(hsv, lower, upper)
     # Mascara bit a bit-AND e imagem original
    res = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow('mascara',mask)#mascara  
    cv2.imshow('resultado',res) #resultado
    #Passo 1: Conversão para tons de cinza
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
     #VARIÁVEL RECEBE A IMAGEM
    area_real = round(altura*largura*(fator_de_escala), 3)
    print ("Àrea real do território analisado  é ",area_real, 'm²')
    #Passo 2: Blur/Suavização da imagem
    suave = cv2.blur(gray, (11,11))
    #Passo 3: Binarização resultando em pixels brancos e pretos
    T = mahotas.thresholding.otsu(suave)
    bin = suave.copy()
    bin[bin > T] = 255
    bin[bin < 255] = 0
    bin = cv2.bitwise_not(bin)

        #HISTOGRAMA
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
    print (" Largura,    Altura do centro de massa do sistema")
    X=arredondar (X)
    Y=arredondar (Y)
    print (X, Y)
    print ("Àrea verde (arborizada) total: ,")
    print (round(mass*fator_de_escala, 3) ,'m²')
    print ("Percentual de área verde do terreno: ,")
    print (100*round(mass*fator_de_escala, 3)/(area_real) ,'%')
    
    #Passo 4: Detecção de bordas com Canny
    bordas = cv2.Canny(bin, 40, 180)
    
#cv2.RETR_EXTERNAL = conta apenas os contornos externos
    (objetos, lx) = cv2.findContours (bordas.copy(),
    cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
    #A variável lx (lixo) recebe dados que não são utilizados
    
    escreve(gray, "Imagem em tons de cinza", 0)
    escreve(suave, "Suavizacao com Blur", 0)
    escreve(bin, "Binarizacao com Metodo Otsu", 255)
    escreve(bordas, "Detector de bordas Canny", 255)
    temp = np.vstack([ np.hstack([gray, suave]), np.hstack([bin, bordas]) ])
    cv2.imshow(" Quantidade de objetos: "+str(len(objetos)), temp)
    print(' OBJETOS ENCONTRADOS ')
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
    lb = Label(janela, text=round(mass*fator_de_escala, 3))
    lb.place(x=270, y=275)
    lb = Label(janela, text=100*round(mass*fator_de_escala/area_real, 5))
    lb.place(x=290, y=175)
    lb = Label(janela, text=area_real)
    lb.place(x=190, y=150)

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
lb = Label(janela, text='COORDENADAS DA REGIÃO ARBORIZADA')
lb.place(x=40, y=200)
lb = Label(janela, text='X=')
lb.place(x=40, y=225) 
lb = Label(janela, text='Y=')
lb.place(x=40, y=250)
lb = Label(janela, text='ÁREA SUPERFICIAL TOTAL DAS ÁRVORES=')
lb.place(x=40, y=275)
lb = Label(janela, text='m²')
lb.place(x=317, y=275)
lb = Label(janela, text='PERCENTUAL DE ÁREA VERDE DO TERRENO=')
lb.place(x=40, y=175)
lb = Label(janela, text='%')
lb.place(x=320, y=175)
lb = Label(janela, text='ÁREA REAL DO TERRENO=')
lb.place(x=40, y=150)
lb = Label(janela, text='m²')
lb.place(x=245, y=150)

bt = Button(janela, width=20, text= 'QUANTIFICAR', command=verde)
bt.place(x=145, y=100)
bt['bg'] = 'green'
bt['fg'] = 'white'


janela.mainloop()
