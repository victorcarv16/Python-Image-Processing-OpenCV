import  cv2 # É A BIBLIOTECA OPEN CV QUE É UTILIZA PARA PROCESSAR IMAGENS
import numpy as np # É A BIBLIOTECA PARA FAZER OPERAÇÕES COM MATRIZES (INVERSA, TRANSPOSTA, DETERMINANTE)
import matplotlib.pyplot as plt #É A BIBLIOTECA PARA FAZER OPERAÇÕES MATEMATICAS DE PLOTAGEM DE GRÁFICOS (2D E 3D), TABELAS E ETC..  
import tkinter as tk # BIBLIOTECA PARA CRIAR INTERFACE GRÁFICA= BOTÕES, JANELAS, TEXTOS E ABAS. 
import mahotas # É UMA BIBLIOTECA COM OPERAÇÕES/FUNÇES PROGRAMADAS DE MATRIZES 
from tkinter import*
import os # É UMA BIBLIOTECA COM FUNÇÕES DO SISTEMA OPERACIONAL (TIME, REÓGIO, CONTADOR, ABRIR PASTA, BUSCA EM PASTA, EECUTAR ARQUIVOS)
import os.path
from matplotlib import pyplot as plt




img = cv2.imread('scara12.jpeg')
img = img[::2,::2]
'''
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converte para cinza
'''
suave = cv2.GaussianBlur(img, (9, 9), 0) # aplica blur/borrão por gaussiana



suave1 = cv2.blur(img, (9, 9)) # aplica blur/borrão por média aritmética



#É importante notar que este método não cria novas cores, como pode acontecer com
#os ateriores, pois ele sempre altera a cor do pixel atual com um dos valores da vizinhança.
suave2 = cv2.medianBlur(img, 9)  # aplica blur/borrão por mediana



suave3 = cv2.bilateralFilter(img, 3, 21, 21) # aplica blur/borrão duplo filtro gaussiano



#Este método é mais lento para calcular que os anteriores mas como vantagem
#apresenta a preservação de bordas e garante que o ruído seja removido.
#Para realizar essa tarefa, além de um filtro gaussiano do espaço ao redor do pixel

#também é utilizado outro cálculo com outro filtro gaussiano que leva em conta a
#diferença de intensidade entre os pixels, dessa forma, como resultado temos uma
#maior manutenção das bordas das imagem. A função usada é cv2.bilateralFilter() e
#o código usado segue abaixo:


cv2.imshow('GAUSSIANO',suave)
cv2.imshow('MEDIA ARITMETICA',suave1)
cv2.imshow('MEDIANA',suave2)
cv2.imshow('BILATERAL',suave3)


'''
bin1 = cv2.adaptiveThreshold(suave, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 5) bin2 = cv2.adaptiveThreshold(suave, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,
21, 5)
resultado = np.vstack([ np.hstack([img, suave]), np.hstack([bin1, bin2]) ])
cv2.imshow("Binarização adaptativa da imagem", resultado) cv2.waitKey(0)

'''
