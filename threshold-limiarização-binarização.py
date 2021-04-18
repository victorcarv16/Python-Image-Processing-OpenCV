import  cv2 # É A BIBLIOTECA OPEN CV QUE É UTILIZA PARA PROCESSAR IMAGENS
import numpy as np # É A BIBLIOTECA PARA FAZER OPERAÇÕES COM MATRIZES (INVERSA, TRANSPOSTA, DETERMINANTE)
import matplotlib.pyplot as plt #É A BIBLIOTECA PARA FAZER OPERAÇÕES MATEMATICAS DE PLOTAGEM DE GRÁFICOS (2D E 3D), TABELAS E ETC..  
import tkinter as tk # BIBLIOTECA PARA CRIAR INTERFACE GRÁFICA= BOTÕES, JANELAS, TEXTOS E ABAS. 
import mahotas # É UMA BIBLIOTECA COM OPERAÇÕES/FUNÇES PROGRAMADAS DE MATRIZES 
from tkinter import*
import os # É UMA BIBLIOTECA COM FUNÇÕES DO SISTEMA OPERACIONAL (TIME, REÓGIO, CONTADOR, ABRIR PASTA, BUSCA EM PASTA, EECUTAR ARQUIVOS)
import os.path
from matplotlib import pyplot as plt

img  =  cv2 . imread ( 'scara12.jpeg' )
img = img[::2,::2] # DIVIDE O TAMANHO DA IMAGEM EM 2. 

largura, altura, canais = img.shape

print('largura, altura,canais de cor ')
print(largura,      altura,     canais)


#Se o valor do pixel for maior do que um valor limite, é atribuído um valor (pode ser branco),
#caso contrário, é atribuído outro valor (pode ser preto). A função usada é:  cv2.threshold .


#O primeiro argumento é a imagem de origem, que deve ser uma imagem em tons de cinza .
#O segundo argumento é o valor limite que é usado para classificar os valores de pixel.
#O terceiro argumento é o maxVal, que representa o valor a ser dado se o valor do
#pixel for maiorque (às vezes menor que) o valor limite. OpenCV fornece diferentes estilos de
#limiar e é decidido pelo quarto parâmetro da função.Diferentes tipos são:

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

#-------------------------------------------------------------------------------------------
img = cv2.medianBlur(img,5)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)

th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


#-----------------------------------------------------------------------------------------------------


# global thresholding
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Otsu's thresholding
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# plot all the images and their histograms
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Imagem Original com ruído ','Histograma','Limiarização de Global (v=127)',
          ' Imagem Original com ruído ','Histograma',"Limiarização de Otsu's ",
          'Imagem com Filtro Gaussiano ','  Histograma',"Limiarização de Otsu's"]

for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()








