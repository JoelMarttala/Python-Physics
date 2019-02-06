#Joel Marttala ja Heidi Teinonen
import math
import matplotlib.pyplot as plt

G = 9.81        #painovoima

TWARP = 0.2     #ajan muutos





xp1 = -0.5                      #kulmien koordinaatit 
xp2 = 0.5
xp3 = 0.5
xp4 = -0.5
yp1 = 1.5
yp2 = 1.5
yp3 = 2.5
yp4 = 2.5

x1,y1 = [xp1,xp2],[yp1,yp2]     #kulmien koordinaatit alussa
x2,y2 = [xp2,xp3],[yp2,yp3]
x3,y3 = [xp3,xp4],[yp3,yp4]
x4,y4 = [xp4,xp1],[yp4,yp1]

plt.plot(x1,y1,x2,y2,x3,y3,x4,y4, color='green')  #piirretään ensimmäinen neliö


x = 0       #massakeskipisteen x-koordinaatti
y = 2       #massakeskipisteen y-koordinaatti

mxlist = [x]    

mylist = [y]

vax = 4.0   #monikulmion vauhdin x-komponentti
vay = 6.7   #monikulmion vauhdin y-komponentti
r = 3*TWARP #pyörimisnopeus


   
while (mylist[-1]> 0):
    

    ex1 = xp1 - x           #kulmien ja massakeskipisteen erotus
    ex2 = xp2 - x
    ex3 = xp3 - x
    ex4 = xp4 - x
    ey1 = yp1 - y
    ey2 = yp2 - y
    ey3 = yp3 - y
    ey4 = yp4 - y
    
    vlx = vax               #päivitetään massakeskipisteen nopeuden komponentit
    vly = vay-G*TWARP
    x = mxlist[-1]+(vax+vlx)/2*TWARP       #lasketaan massakeskipisteen uusi paikka 
    y = mylist[-1]+(vay+vly)/2*TWARP

    
    

    kx1 = ex1*math.cos(r) - ey1*math.sin(r)   #jokaisen kulman kääntölauseke
    ky1 = ex1*math.sin(r) + ey1*math.cos(r)
    kx2 = ex2*math.cos(r) - ey2*math.sin(r)
    ky2 = ex2*math.sin(r) + ey2*math.cos(r)
    kx3 = ex3*math.cos(r) - ey3*math.sin(r)
    ky3 = ex3*math.sin(r) + ey3*math.cos(r)
    kx4 = ex4*math.cos(r) - ey4*math.sin(r)
    ky4 = ex4*math.sin(r) + ey4*math.cos(r)

    xp1 = x+kx1             #kärkien kulmien koordinaatit käännön jälkeen
    xp2 = x+kx2
    xp3 = x+kx3
    xp4 = x+kx4
    yp1 = y+ky1
    yp2 = y+ky2
    yp3 = y+ky3
    yp4 = y+ky4
    
    
    x1,y1 = [xp1,xp2],[yp1,yp2]     #loppulliset kulmien koordinaatit
    x2,y2 = [xp2,xp3],[yp2,yp3]
    x3,y3 = [xp3,xp4],[yp3,yp4]
    x4,y4 = [xp4,xp1],[yp4,yp1]
   
    mxlist.append(x)            #lisätään massakeskipisteen koordinaatit listaan
    mylist.append(y)
    
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4, color='green') # piirretään kärkien välille viivat
    
    
    vax = vlx       #asetetaan uudet nopeusarvot alkuarvoiksi
    vay = vly

plt.plot(x1,y1,x2,y2,x3,y3,x4,y4, color='green')    #piirretään viimeinen neliö
plt.plot(mxlist, mylist, "o")       #piirretään massakeskipisteet

plt.show()      #näytetään grafiikka

    
