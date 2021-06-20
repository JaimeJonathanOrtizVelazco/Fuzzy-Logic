%% Método de la montaña. Versión corregida 2015.
%% Dra. Yesenia E. González Navarro
close all; clear all; clc;
%% Distribución de datos
P=[0.36 0.65 0.62 0.50 0.35 0.90 1.00 0.99 0.83 0.88;
   0.85 0.89 0.55 0.75 1.00 0.35 0.24 0.55 0.36 0.43];
figure (1),
for x=1:length(P)
    plot(P(1,x),P(2,x),'o');   
    hold on
end
xlim([0,1]);ylim([0,1]);
grid on
%% Generación de nodos. Se propone un rango de 0 a 1 con incrementos de 0.2
F(1,:)=0:0.2:1;
C(1,:)=0:0.2:1;
alpha=5.4;
beta=5.4;
delta=1;
suma=0;
%Obtención de la primera matriz M
tic
for x=1:length(F)
    for y=1:length(C)
        for z=1:length(P)
            d=sqrt((P(1,z)-F(1,x))^2+(P(2,z)-C(1,y))^2);  
            m=exp(-alpha*d);
            M(y,x)=suma+m;  
            suma=M(y,x);
        end
        suma=0;        
    end     
end
M1=M;
figure(2)
X=0:.2:1;Y=X;
surf(X,Y,M1)
toc
k=1;
% for epoca=1:5  %(Recuerden siempre probar con un número finito de 
                 % iteraciones antes de usar while)
while delta < 2   
    c(k)=max(max(M)) %aumenta c dependiendo el número de cluster donde nos encontremos
    for x=1:length(F)
        for y=1:length(C)
            if M(x,y)==c(k)
                pf(k)=x;  %Se conoce la posición en fila y columna del pico de montaña
                pc(k)=y;
            end
        end
    end
    for x=1:length(F)
        for y=1:length(C)
            for z=1:k
                dc(z)=sqrt((F(1,pf(z))-F(1,x))^2+(C(1,pc(z))-C(1,y))^2); 
                g(z)=exp(-beta*dc(z));
            end
            mc=sum(g);      
            M2(x,y)=M(x,y)-M(pf(k),pc(k))*mc;      
            M2=max(M2,0);  %Debido al efecto de inhibición, esta instrucción evita valores negativos en M.
        end
    end
    Mactual(:,:,k)=M2;
    k=k+1;
    c2=max(max(M2))
    delta(k-1)=c(1)/c2 %Condición de paro. Razón de pico mayor entre actual.
    M=M2;  
end
% M
figure(3)
X=0:.2:1;Y=X;
surf(X,Y,Mactual(:,:,1))
figure (1),
for c=1:k-1
    plot(F(1,pf(c)),C(1,pc(c)),'m*');
end