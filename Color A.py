import customtkinter
from tkinter import *
import time
import threading
import numpy as np
#importation des bibliothéques de couleurs

import matplotlib.colors as mcolors
import matplotlib





#gestion de la suggestion de la suggestion
def get_similar_colors(color):
    if color.startswith('#'):  
        rgb = np.array([int(color[i+1:i+3], 16) for i in (0, 2, 4)])
    else: 
        index = colorNameBase.index(color)
        rgb = rgb_values[index]
    distances = [np.linalg.norm(rgb - rgb_value) for rgb_value in rgb_values] 

    # Si la couleur est noire, ne considérez que les couleurs grises et noires
    if color == 'black':
        gray_black_indices = [i for i, color_name in enumerate(colorNameBase) if 'gray' in color_name or 'black' in color_name]
        distances = [distances[i] if i in gray_black_indices else float('inf') for i in range(len(distances))]

    indices = np.argsort(distances)[1:6]  # Commencer à partir de l'index 1

    similar_colors = [(colorNameBase[i], HexcolorBase[i]) for i in indices]

    # Création des tableaux pour stocker les noms de couleurs et les valeurs hexadécimales
    similaire = []
    similaire_hex = []

    screens = [screen2, screen3, screen4, screen5, screen6]
    titres = [titresc1,titresc2,titresc3,titresc4,titresc5]
    for i in range(5):
        screens[i].create_rectangle(0,0,100,100, fill=similar_colors[i][1])
        titres[i].configure(text = similar_colors[i])
        # Ajout des noms de couleurs et des valeurs hexadécimales aux tableaux
        similaire.append(similar_colors[i][0])
        similaire_hex.append(similar_colors[i][1])

    return similaire, similaire_hex

 #creation de la premiére base de couleur

HexcolorBase = [None] *148 #code en hexa de chaque couleur de nos bibliothéque
colorNameBase = [None]*148 #nom en anglais de chaque couleur de nos bibliothéque

HexcolorBase = list(matplotlib.colors.cnames.values()) 
colorNameBase = list(matplotlib.colors.cnames.keys())

rgb_values = [np.array([int(hexcode[i+1:i+3], 16) for i in (0, 2, 4)]) for hexcode in HexcolorBase if len(hexcode) == 7]

#creation des sous groupes
    #groupe bleu
bleus = ['aliceblue', 'blue', 'cadetblue', 'cornflowerBlue', 'blueViolet', 'darkslateblue', 'mediumslateblue', 'slateblue', 'steelblue','mediumturquoise','aqua','aquamarine']
Hexbleus = ['#F0F8FF', '#0000FF', '#5F9EA0', '#6495ED', '#8A2BE2', '#483D8B', '#7B68EE', '#6A5ACD', '#4682B4',' #48D1CC']

for i in range(len(colorNameBase)):
    if 'blue' in colorNameBase[i].lower():
        bleus.append(colorNameBase[i])
        Hexbleus.append(HexcolorBase[i])

        
    #groupe rouge
rouges = ['crimson', 'darkred', 'firebrick', 'indianred', 'lightcoral', 'maroon', 'red', 'salmon', 'deeppink', 'pink', 'lightpink', 'hotpink']
Hexrouges = ['#DC143C', '#8B0000', '#B22222', '#CD5C5C', '#F08080', '#800000', '#FF0000', '#FA8072', '#FF1493', '#FFC0CB', '#FFB6C1', '#FF69B4']

for i in range(len(colorNameBase)):
    if 'red' in colorNameBase[i].lower():
        rouges.append(colorNameBase[i])
        Hexrouges.append(HexcolorBase[i])
        
    #groupe vert
verts = ['chartreuse', 'darkgreen', 'forestgreen', 'green']
Hexverts = ['#7FFF00', '#006400', '#228B22', '#008000']

for i in range(len(colorNameBase)):
    if 'green' in colorNameBase[i].lower():
        verts.append(colorNameBase[i])
        Hexverts.append(HexcolorBase[i])
    #groupe jaunes
jaunes = ['gold', 'lemonchiffon', 'Lightgoldenrodyellow', 'lightyellow', 'yellowgreen', 'greenyellow', 'yellow']
Hexjaunes = ['#FFD700', '#FFFACD', '#FAFAD2', '#FFFFE0', '#9ACD32', '#ADFF2F']

for i in range(len(colorNameBase)):
    if 'yellow' in colorNameBase[i].lower():
        jaunes.append(colorNameBase[i])
        Hexjaunes.append(HexcolorBase[i])
    #groupe violets
violets = ['blueviolet', 'darkmagenta', 'darkslateblue', 'indigo', 'mediumorchid', 'mediumpurple','plum','palevioletred','violet','purple','darkviolet']
Hexviolets = ['#8A2BE2','#8B008B','#483D8B','#4B0082','#BA55D3','#9370DB','#DDA0DD','#DB7093']

for i in range(len(colorNameBase)):
    if 'purple' in colorNameBase[i].lower():
        violets.append(colorNameBase[i])
        Hexviolets.append(HexcolorBase[i])
    #groupe oranges
oranges = ['coral','darkorange','orange','tomato','sandybrown']
Hexoranges = ['#FF7F50','#FF8C00','#FFA500','#FF6347','#F4A460']

for i in range(len(colorNameBase)):
    if 'orange' in colorNameBase[i].lower():
        oranges.append(colorNameBase[i])
        Hexoranges.append(HexcolorBase[i])
    #groupes marrons
marrons = ['brown','burlywood','rosybrown','saddlebrown']
Hexmarrons = ['#A52A2A','#DEB887','#BC8F8F','#8B4513']

for i in range(len(colorNameBase)):
    if 'brown' or 'sienna' in colorNameBase[i].lower():
        marrons.append(colorNameBase[i])
        Hexmarrons.append(HexcolorBase[i])
    #groupes gris
gris = ['dimgray','darkgray','gainsboro','lightgray','grey']
Hexgris = ['#696969','#A9A9A9','#DCDCDC','#D3D3D3']



for i in range(len(colorNameBase)):
    if 'grey or gray' in colorNameBase[i].lower():
        gris.append(colorNameBase[i])
        Hexgris.append(HexcolorBase[i])
    #groupe blanc
blancs = ['azure','beige','floralwhite','ghostwhite','honeydew','ivory','lavenderblush','linen','mintcream','white']
Hexblancs = ['#F0FFFF','#F5F5DC','#FFF0F5','#00FFFF','#98FB98','#F0FFF0','#FFFFF0','#FAF0E6','#F5DEB3']


for i in range(len(colorNameBase)):
    if 'white' in colorNameBase[i].lower():
        blancs.append(colorNameBase[i])
        Hexblancs.append(HexcolorBase[i])
    #groupe noir
noirs = ['black']
Hexnoirs = ['#000000']



#defnition des diferentes fonctions:

 #fonction d'ecriture du texte par la machine
def type_text(widget, text):
    for i in range(len(text)):
         widget.insert(END, text[i])
         widget.after(100, widget.update)
         time.sleep(0.1)
         


         
    #fonction de recuperation, d'attribution du groupe et d'affichage de la couleur
    # lorsqu'on recupere le nom ou le code de la couleur on retourne le nom de la couleur et le groupe auquel il appartient
def recup():
    res=entre1.get()
    if res:
        suggestion = get_similar_colors(res)
        print(get_similar_colors(res))
        if((res in HexcolorBase) or (res in colorNameBase)):
             print(res)
             if ((res in bleus) or (res in Hexbleus)):
                 print("Groupe des bleus")
                 infoGrp = " \n elle est une dérivé de la couleur bleu \n"                             
                 discussion_1 = "\n les couleurs que je peux vous suggerer sont :\n - la couleur :  " +suggestion[0][0]+" qui a pour code   " +suggestion[1][0]+":\n - la couleur :  " +suggestion[0][1]+" qui a pour code  " + suggestion[1][1]+":\n - la couleur :  " +suggestion[0][2]+" qui a pour code  " + suggestion[1][2]+":\n - la couleur :  " +suggestion[0][3]+" qui a pour code  " + suggestion[1][3]+":\n - la couleur :  " +suggestion[0][4]+" qui a pour code  " + suggestion[1][4]    

                 
                 txt="\n la couleur selectionner est la couleur :"
                 txt = txt + res+infoGrp+discussion_1
                 
                 thread_type_text = threading.Thread(target=type_text, args=(texte2, txt))
                 thread_type_text.start()
             elif((res in rouges )or( res in Hexrouges)):
                print("Groupe des rouge")
                infoGrp="\n elle est une dérivé de la couleur Rouge \n"
                discussion_1 = "\n les couleurs que je peux vous suggerer sont :\n - la couleur :  " +suggestion[0][0]+" qui a pour code   " +suggestion[1][0]+":\n - la couleur :  " +suggestion[0][1]+" qui a pour code  " + suggestion[1][1]+":\n - la couleur :  " +suggestion[0][2]+" qui a pour code  " + suggestion[1][2]+":\n - la couleur :  " +suggestion[0][3]+" qui a pour code  " + suggestion[1][3]+":\n - la couleur :  " +suggestion[0][4]+" qui a pour code  " + suggestion[1][4]    

                txt="\n  la couleur selectionner est la couleur :"
                txt = txt + res+infoGrp+discussion_1 
                thread_type_text = threading.Thread(target=type_text, args=(texte2, txt))
                thread_type_text.start()
             elif((res in verts )or( res in Hexverts)):
                print("Groupe des verts")
                infoGrp="\n elle est une dérivé de la couleur Verte \n"
                discussion_1 = "\n les couleurs que je peux vous suggerer sont :\n - la couleur :  " +suggestion[0][0]+" qui a pour code   " +suggestion[1][0]+":\n - la couleur :  " +suggestion[0][1]+" qui a pour code  " + suggestion[1][1]+":\n - la couleur :  " +suggestion[0][2]+" qui a pour code  " + suggestion[1][2]+":\n - la couleur :  " +suggestion[0][3]+" qui a pour code  " + suggestion[1][3]+":\n - la couleur :  " +suggestion[0][4]+" qui a pour code  " + suggestion[1][4]    

                txt="\n  la couleur selectionner est la couleur :"
                txt = txt + res+infoGrp+discussion_1 
                thread_type_text = threading.Thread(target=type_text, args=(texte2, txt))
                thread_type_text.start()
             elif((res in jaunes )or( res in Hexjaunes)):
                print("Groupe des jaunes")
                infoGrp="\n elle est une dérivé de la couleur Jaune  \n"
                discussion_1 = "\n les couleurs que je peux vous suggerer sont :\n - la couleur :  " +suggestion[0][0]+" qui a pour code   " +suggestion[1][0]+":\n - la couleur :  " +suggestion[0][1]+" qui a pour code  " + suggestion[1][1]+":\n - la couleur :  " +suggestion[0][2]+" qui a pour code  " + suggestion[1][2]+":\n - la couleur :  " +suggestion[0][3]+" qui a pour code  " + suggestion[1][3]+":\n - la couleur :  " +suggestion[0][4]+" qui a pour code  " + suggestion[1][4]    

                txt="\n  la couleur selectionner est la couleur :"
                txt = txt + res+infoGrp+discussion_1 
                thread_type_text = threading.Thread(target=type_text, args=(texte2, txt))
                thread_type_text.start()
             elif((res in violets )or( res in Hexviolets)):
                print("Groupe des violets")
                infoGrp="\n elle est une dérivé de la couleur Violette  \n"
                discussion_1 = "\n les couleurs que je peux vous suggerer sont :\n - la couleur :  " +suggestion[0][0]+" qui a pour code   " +suggestion[1][0]+":\n - la couleur :  " +suggestion[0][1]+" qui a pour code  " + suggestion[1][1]+":\n - la couleur :  " +suggestion[0][2]+" qui a pour code  " + suggestion[1][2]+":\n - la couleur :  " +suggestion[0][3]+" qui a pour code  " + suggestion[1][3]+":\n - la couleur :  " +suggestion[0][4]+" qui a pour code  " + suggestion[1][4]    

                txt="\n  la couleur selectionner est la couleur :"
                txt = txt + res+infoGrp+discussion_1
                thread_type_text = threading.Thread(target=type_text, args=(texte2, txt))
                thread_type_text.start()
             elif((res in oranges )or( res in Hexoranges)):
                print("Groupe des oranges")
                infoGrp="\n elle est une dérivé de la couleur Orange \n"
                discussion_1 = "\n les couleurs que je peux vous suggerer sont :\n - la couleur :  " +suggestion[0][0]+" qui a pour code   " +suggestion[1][0]+":\n - la couleur :  " +suggestion[0][1]+" qui a pour code  " + suggestion[1][1]+":\n - la couleur :  " +suggestion[0][2]+" qui a pour code  " + suggestion[1][2]+":\n - la couleur :  " +suggestion[0][3]+" qui a pour code  " + suggestion[1][3]+":\n - la couleur :  " +suggestion[0][4]+" qui a pour code  " + suggestion[1][4]    

                txt="\n  la couleur selectionner est la couleur : "
                txt = txt + res+infoGrp+discussion_1 
                thread_type_text = threading.Thread(target=type_text, args=(texte2, txt))
                thread_type_text.start()
             elif((res in marrons )or( res in Hexmarrons)):
                print("Groupe des marrons")
                infoGrp="\n elle est une dérivé de la couleur Marrone \n"
                discussion_1 = "\n les couleurs que je peux vous suggerer sont :\n - la couleur :  " +suggestion[0][0]+" qui a pour code   " +suggestion[1][0]+":\n - la couleur :  " +suggestion[0][1]+" qui a pour code  " + suggestion[1][1]+":\n - la couleur :  " +suggestion[0][2]+" qui a pour code  " + suggestion[1][2]+":\n - la couleur :  " +suggestion[0][3]+" qui a pour code  " + suggestion[1][3]+":\n - la couleur :  " +suggestion[0][4]+" qui a pour code  " + suggestion[1][4]    

                txt="\n  la couleur selectionner est la couleur :"
                txt = txt + res+infoGrp+discussion_1 
                thread_type_text = threading.Thread(target=type_text, args=(texte2, txt))
                thread_type_text.start()
             elif((res in gris)or( res in Hexgris)):
                print("Groupe des gris")
                infoGrp="\n elle est une dérivé de la couleur Grise \n"
                discussion_1 = "\n les couleurs que je peux vous suggerer sont :\n - la couleur :  " +suggestion[0][0]+" qui a pour code   " +suggestion[1][0]+":\n - la couleur :  " +suggestion[0][1]+" qui a pour code  " + suggestion[1][1]+":\n - la couleur :  " +suggestion[0][2]+" qui a pour code  " + suggestion[1][2]+":\n - la couleur :  " +suggestion[0][3]+" qui a pour code  " + suggestion[1][3]+":\n - la couleur :  " +suggestion[0][4]+" qui a pour code  " + suggestion[1][4]    

                txt="\n  la couleur selectionner est la couleur :"
                txt = txt + res+infoGrp +discussion_1
                thread_type_text = threading.Thread(target=type_text, args=(texte2, txt))
                thread_type_text.start()
             elif((res in blancs )or( res in Hexblancs)):
                 print("Groupe des blancs")
                 infoGrp="\n elle est une dérivé de la couleur blanche \n" 
                 discussion_1 = "\n les couleurs que je peux vous suggerer sont :\n - la couleur :  " +suggestion[0][0]+" qui a pour code   " +suggestion[1][0]+":\n - la couleur :  " +suggestion[0][1]+" qui a pour code  " + suggestion[1][1]+":\n - la couleur :  " +suggestion[0][2]+" qui a pour code  " + suggestion[1][2]+":\n - la couleur :  " +suggestion[0][3]+" qui a pour code  " + suggestion[1][3]+":\n - la couleur :  " +suggestion[0][4]+" qui a pour code  " + suggestion[1][4]    

                 txt="\n  la couleur selectionner est la couleur "
                 txt = txt + res+infoGrp+discussion_1 
                 thread_type_text = threading.Thread(target=type_text, args=(texte2, txt))
                 thread_type_text.start()
             elif((res in noirs) or ( res in Hexnoirs)):
                 print("noirs")
                 infoGrp="\n elle est une dérivé de la couleur noire \n"
                 discussion_1 = "\n les couleurs que je peux vous suggerer sont :\n - la couleur :  " +suggestion[0][0]+" qui a pour code   " +suggestion[1][0]+":\n - la couleur :  " +suggestion[0][1]+" qui a pour code  " + suggestion[1][1]+":\n - la couleur :  " +suggestion[0][2]+" qui a pour code  " + suggestion[1][2]+":\n - la couleur :  " +suggestion[0][3]+" qui a pour code  " + suggestion[1][3]+":\n - la couleur :  " +suggestion[0][4]+" qui a pour code  " + suggestion[1][4]    

                 txt="\n  la couleur selectionner est la couleur :"
                 txt = txt + res+infoGrp+discussion_1 
                 thread_type_text = threading.Thread(target=type_text, args=(texte2, txt))
                 thread_type_text.start()
             else:
                 print("Couleur inconnue Master")
                  

             #creation du rectangle avec la couleur entrez par l'utilisateur 
             screen1.create_rectangle(0,0,100,100, fill =res )
             

             
        else:
            print("Couleur inconnue Master")
    else:
        print("erreur 440!")
    #fonction d'annulation
def Nvm():
    res = entre1.get()
    if res:
            entre1.delete(0, "end")
            print("Removed")
    else:
            print("Nothing to move Master")

 
#creation des threads dans une fonction
 
     
#creation de l'hote
app = customtkinter.CTk()
app.title("Color Bind")
app.geometry("850x600")

#creation de la fenetre destiné a la selection :
    #creation du premier cadre:
cadre1 = customtkinter.CTkFrame( master=app)
cadre1.grid(row =0, column = 0, padx = 10, pady = 10, sticky = "nsew")
 
texte1 = customtkinter.CTkLabel(cadre1, text = "Veuillez entrez le code hexadecimal (Majuscule) ou le nom(minuscule) en anglais de la couleur")
texte1.grid(row = 1, column = 1, columnspan = 2,padx = 10, pady = 10)

entre1 = customtkinter.CTkEntry(cadre1, width = 250, height = 10, corner_radius = 2)
entre1.grid(row=2, column = 2 )

bouton1 = customtkinter.CTkButton(cadre1, text="valider !", height = 10,corner_radius = 2,width = 100,command = recup )
bouton1.grid(row = 2, column=1, padx = 10)
 
bouton2 = customtkinter.CTkButton(cadre1, fg_color = "red",text = "annuler",hover_color = "white", text_color = "black", command = Nvm)
bouton2.grid(row = 3, column = 2, pady = 20)

    #creation du deuxieme cadre:
cadre2 = customtkinter.CTkFrame(app)
cadre2.grid(row = 0, column = 1)

screen1 = Canvas(cadre2, height = 100, width = 100)
screen1.grid(row = 0, column = 0)
 


#creation de la deuxieme section 
base2 = customtkinter.CTkFrame( master = app)
base2.grid(row = 2, padx = 10, pady = 10)
texte3 = customtkinter.CTkLabel(base2, text=" Reponse de l'ordinateur :")
texte3.grid(row = 1, padx = 5, pady = 5)
texte2 = Text( base2)
texte2.grid(row = 2, padx = 10, pady = 10)
texte2.configure(width = 70, height = 10)


#creation de la section des résultat des couleurs:

base3 = customtkinter.CTkFrame(master = app)
base3.grid(row = 3, column = 0,padx = 10, pady = 10)

titresc1 = Label(base3, text="")
titresc1.grid(row = 0, column =0, padx = 15, pady = 15)
screen2 = Canvas(base3,height = 100, width = 100)
screen2.grid(row = 1, column = 0,padx = 10, pady = 10)
titresc2 = Label(base3, text="")
titresc2.grid(row = 0, column =1, padx = 15, pady = 15)
screen3 = Canvas(base3,height = 100, width = 100)
screen3.grid(row = 1, column = 1,padx = 10, pady = 10)
titresc3 = Label(base3, text="")
titresc3.grid(row = 0, column =2, padx = 15, pady = 15)
screen4 = Canvas(base3,height = 100, width = 100)
screen4.grid(row = 1, column = 2,padx = 10, pady = 10)
titresc4 = Label(base3, text="")
titresc4.grid(row = 0, column =3, padx = 15, pady = 15)
screen5 = Canvas(base3,height = 100, width = 100)
screen5.grid(row = 1, column = 3,padx = 10, pady = 10)
titresc5 = Label(base3, text="")
titresc5.grid(row = 0, column =4, padx = 15, pady = 15)
screen6 = Canvas(base3,height = 100, width = 100)
screen6.grid(row = 1, column = 4,padx = 10, pady = 10)

thread_recup = threading.Thread(target=recup)
thread_recup.start()

app.mainloop()
