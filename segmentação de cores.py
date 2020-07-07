import  cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import os.path
from matplotlib import pyplot as plt

def arredondar(num):
    return float( '%g' % ( num ) )

   # Converter BGR em HSV
def show_image():
    filtro=0
    img  =  cv2 . imread ( 'scara2.png' )
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    print ("tamanho da imagem e' (altura,largura)\n ",img.shape)
    while True:

        largura, altura, canais = img.shape
 
        if filtro == 0:
            cv2.imshow('Estudo OpenCV- Filtro', img)
            print ('nada')

        if filtro == 1:#FILTRA OBJETOS VERDES
            # define faixa de cor verde em HSV
            lower_blue = np.array([30,50,50])
            upper_blue = np.array([73,255,255])
            print ('filtro verde')
            
        if filtro == 2:#FILTRA OBJETOS AZUIS
         
            # define faixa de cor azul em HSV
            lower_blue = np.array([115,50,50])
            upper_blue = np.array([125,255,255])
            print ('filtro azul')
            
        if filtro == 6:#FILTRA OBJETOS VERMELHOS
         # define faixa de cor vermelha em HSV
            lower_blue = np.array([0,40,40])
            upper_blue = np.array([20,255,255])
            print ('filtro vermelho')

 
        if filtro == 7:#FILTRA OBJETOS AMARELOS
             # define faixa de cor amarela em HSV
            lower_blue = np.array([30,40,40])
            upper_blue = np.array([45,255,255])
            print ('filtro amarelo')

            
        if filtro == 8:#FILTRA OBJETOS  PRETOS
                # define faixa de cor preto em HSV
            lower_blue = np.array([0,00,00])
            upper_blue = np.array([40,255,100])
            print ('filtro preto')

            
        if filtro ==4:#FILTRA OBJETOS BRANCOS
          # define faixa de cor branco em HSV
            lower_blue = np.array([0,0,112])
            upper_blue = np.array([150,60,255])
            print ('filtro de branco')

        if filtro ==3:
            lower_blue = np.array([0,0,112])
            upper_blue = np.array([150,60,255])
            print ('filtro de branco')

        ret= cv2.waitKey(1)
        if ret==27:
            break
 
        elif ret==-1:
           continue
 
        elif ret== 49:
           filtro= 1
 
        elif ret== 50:
           filtro= 2
 
        elif ret== 54:
           filtro= 6
 
        elif ret== 55:
          filtro= 7
 
        elif ret== 56:
          filtro= 8
          
        elif ret== 57:
          filtro= 4
 
    # Limite a imagem HSV para obter apenas cores azuis
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
     # Mascara bit a bit-AND e imagem original
    res = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow('mask',mask)#mascara  
    cv2.imshow('res',res) #resultado

    print ("tamanho da result e' (altura,largura)\n ",res.shape)
    ret , thresh  =  cv2 .threshold ( mask ,155, 255 , cv2 . THRESH_BINARY )
    titles  =  [ 'Imagem Original' , 'BINÁRIO'  ] 
    images  =  [ mask,  thresh]
    height, width = thresh.shape[:2]

    mass = 0
    Xcm  = 0.0
    Ycm  = 0.0

    for i in range(width) :
        for j in range(height) :
            if not thresh[j][i] :
                mass += 1
                Xcm  += i
                Ycm  += j

    Xcm = Xcm/mass
    Ycm = Ycm/mass
    print ("\n Xcm e Ycm\n", Xcm)
    print ("", Ycm)
    X=Xcm-200
    Y=250-Ycm
    fig = plt.figure()
    fig.clear()
    plot = fig.add_subplot(111)
    plot.imshow(thresh, 'gray')
    plot.scatter([Xcm], [Ycm], s=30, c='yellow', edgecolors='red')
        
    print ("\nlargura, altura")
    X=arredondar (X)
    Y=arredondar (Y)
    print (X, Y)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    plt . show ()    
cv2.destroyAllWindows()


def main():
    show_image()
    return 0

if __name__ == '__main__':
    main()
