close all;
clear all;
clc;

Foto=imread('paisaje.jpg');
imshow(Foto)
Foto1=imresize(Foto,[480,640]);
%%figure,imshow(Foto1)
%figure,imshow(Foto1(:,:,1));
%figure,imshow(Foto1(:,:,2));
%figure,imshow(Foto1(:,:,3));

Gris=rgb2gray(Foto1);
figure,imshow(Gris);

Binario1= Gris>150;
figure,imshow(Binario1)

Binario2= Gris<150;
figure,imshow(Binario2)

E=edge(Gris,'sobel');
figure,imgshow(E);
