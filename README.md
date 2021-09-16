# Python-image processing-Processamento-de-imagem
<h1> Wooded Area Tracker </h1> 

> Status: Developing⚠️

### PDI image processing programs.

## This is software to track wooded areas (green) on any GoogleMaps image.

### To perform the image treatment I used the following processes:

+ Filters
+ color space conversion
+ tracking
+ binarization
+ thresholding
+ contour counting 
+ multiple centers of mass and graphical interface.


# For this project it will be necessary to upload an image of a wooded location (with green vegetation), and a photo with the respective scale that was used.

## In this project I used the following technologies (libraries):
<table> 
  <tr>
    <td>Python</td>
    <td>OpenCV</td>
    <td>Numpy</td>
    <td>Tkinter</td>
    <td>mahotas</td>
    <td>matplotlib</td>
    <td> OS</td>
    <td>colorysys</td>
  </tr>
  
  <tr>
    <td> 3.*</td>
    <td> 2</td>
    <td> 1</td>
    <td> 1</td>
    <td> 1</td>
    <td> 1</td>
    <td> 1</td>
    <td> 1</td>
  </tr>
</table>

# How to use this project?
## Follow the following steps:
1-Upload image for scale reference (scale factor) taken from the lower right corner of GoogleMaps.
![Part1 upload  escale](https://github.com/victorcarv16/assets/blob/main/uploadescala.PNG)

Image of Escale
![Part2 upload  escale](https://github.com/victorcarv16/assets/blob/main/escala_20_test.PNG)

2-Upload the image taken from Google Maps in the chosen scale.
![Part1 upload image](https://github.com/victorcarv16/assets/blob/main/uploadimage.PNG)

2.1-To test I chose this image.

![Part2 upload image](https://github.com/victorcarv16/assets/blob/main/Condominio1_escala_20.PNG)

2.2-Resume.
![Part upload archive](https://github.com/victorcarv16/assets/blob/main/Upload%20arquivo.gif)


3-Then click on "QUANTIFICAR".

![Part3 QUANTIFY](https://github.com/victorcarv16/assets/blob/main/quantify.PNG)

3.1-Resume.
![Part3.1 QUANTIFY](https://github.com/victorcarv16/assets/blob/main/quantify.gif)


4-With this we will obtain the values ​​of the real area of ​​the terrain, percentage of green area in the terrain, coordinates of the wooded region, total surface area of ​​the trees.

![Part4 RESULTS](https://github.com/victorcarv16/assets/blob/main/results.PNG)

5- Results 
![Part5 center of mass](https://github.com/victorcarv16/assets/blob/main/center%20of%20mass.PNG)

5.1- Results of process
![Part5 process](https://github.com/victorcarv16/assets/blob/main/process.gif)
