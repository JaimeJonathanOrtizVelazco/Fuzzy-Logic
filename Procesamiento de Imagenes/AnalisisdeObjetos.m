close all;
clear all;
clc;
tic
Foto=imread('IndividualIdentification/Im1.jpeg');
imshow(Foto)
Foto1=imresize(Foto,[480,640]);
%figure,imshow(Foto1)
%figure,imshow(Foto1(:,:,1));
%figure,imshow(Foto1(:,:,2));
%figure,imshow(Foto1(:,:,3));

Gris=rgb2gray(Foto1);
%figure,imshow(Gris);

Binario2= Gris<160;
figure,imshow(Binario2)
toc