import customtkinter
from tkinter import *
import time
#importation des bibliothéques de couleurs

import matplotlib.colors as mcolors
import matplotlib


 #creation de la premiére base de couleur

HexcolorBase = [None] *148 #code en hexa de chaque couleur de nos bibliothéque
colorNameBase = [None]*148 #nom en anglais de chaque couleur de nos bibliothéque

HexcolorBase = list(matplotlib.colors.cnames.values()) 
colorNameBase = list(matplotlib.colors.cnames.keys())


#creation des sous groupes
    #groupe bleu
bleus = ['aliceblue', 'blue', 'cadetblue', 'cornflowerBlue', 'blueViolet', 'darkslateblue', 'mediumslateblue', 'slateblue', 'steelblue','mediumturquoise','aqua','aquamarine']
Hexbleus = ['#F0F8FF', '#0000FF', '#5F9EA0', '#6495ED', '#8A2BE2', '#483D8B', '#7B68EE', '#6A5ACD', '#4682B4',' #48D1CC']
    #groupe rouge
rouges = ['crimson', 'darkred', 'firebrick', 'indianred', 'lightcoral', 'maroon', 'red', 'salmon', 'deeppink', 'pink', 'lightpink', 'hotpink']
Hexrouges = ['#DC143C', '#8B0000', '#B22222', '#CD5C5C', '#F08080', '#800000', '#FF0000', '#FA8072', '#FF1493', '#FFC0CB', '#FFB6C1', '#FF69B4']
    #groupe vert
verts = ['chartreuse', 'darkgreen', 'forestgreen', 'green']
Hexverts = ['#7FFF00', '#006400', '#228B22', '#008000']
    #groupe jaunes
jaunes = ['gold', 'lemonchiffon', 'Lightgoldenrodyellow', 'lightyellow', 'yellowgreen', 'greenyellow', 'yellow']
Hexjaunes = ['#FFD700', '#FFFACD', '#FAFAD2', '#FFFFE0', '#9ACD32', '#ADFF2F']
    #groupe violets
violets = ['blueviolet', 'darkmagenta', 'darkslateblue', 'indigo', 'mediumorchid', 'mediumpurple','plum','palevioletred','violet','purple','darkviolet']
Hexviolets = ['#8A2BE2','#8B008B','#483D8B','#4B0082','#BA55D3','#9370DB','#DDA0DD','#DB7093']
    #groupe oranges
oranges = ['coral','darkorange','orange','tomato','sandybrown']
Hexoranges = ['#FF7F50','#FF8C00','#FFA500','#FF6347','#F4A460']
    #groupes marrons
marrons = ['brown','burlywood','rosybrown','saddlebrown']
Hexmarrons = ['#A52A2A','#DEB887','#BC8F8F','#8B4513']
    #groupes gris
gris = ['dimgray','darkgray','gainsboro','lightgray','grey']
Hexgris = ['#696969','#A9A9A9','#DCDCDC','#D3D3D3']
    #groupe blanc
blancs = ['azure','beige','floralwhite','ghostwhite','honeydew','ivory','lavenderblush','linen','mintcream','white']
Hexblancs = ['#F0FFFF','#F5F5DC','#FFF0F5','#00FFFF','#98FB98','#F0FFF0','#FFFFF0','#FAF0E6','#F5DEB3']

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

         
    #fonction de recuperation / affichage (temporaire)
def recup():
    res=entre1.get()
    if res:
        if((res in HexcolorBase) or (res in colorNameBase)):
             print(res)
             if ((res in bleus) or (res in Hexbleus)):
                 print("Groupe des bleus")
                 infoGrp = " \n elle est une dérivé de la couleur bleu"                             
                 
                 txt="\n la couleur selectionner est la couleur :"
                 txt = txt + res+infoGrp
                 type_text(texte2, txt) 
             elif((res in rouges )or( res in Hexrouges)):
                print("Groupe des rouge")
                infoGrp="\n elle est une dérivé de la couleur Rouge"
                
                txt="\n  la couleur selectionner est la couleur :"
                txt = txt + res+infoGrp
                type_text(texte2, txt)
             elif((res in verts )or( res in Hexverts)):
                print("Groupe des verts")
                infoGrp="\n elle est une dérivé de la couleur Verte"
                 
                txt="\n  la couleur selectionner est la couleur :"
                txt = txt + res+infoGrp
                type_text(texte2, txt)
             elif((res in jaunes )or( res in Hexjaunes)):
                print("Groupe des jaunes")
                infoGrp="\n elle est une dérivé de la couleur Jaune "
                
                txt="\n  la couleur selectionner est la couleur :"
                txt = txt + res+infoGrp
                type_text(texte2, txt)
             elif((res in violets )or( res in Hexviolets)):
                print("Groupe des violets")
                infoGrp="\n elle est une dérivé de la couleur Violette"
                
                txt="\n  la couleur selectionner est la couleur :"
                txt = txt + res+infoGrp
                type_text(texte2, txt)
             elif((res in oranges )or( res in Hexoranges)):
                print("Groupe des oranges")
                infoGrp="\n elle est une dérivé de la couleur Orange"
                
                txt="\n  la couleur selectionner est la couleur :"
                txt = txt + res+infoGrp
                type_text(texte2, txt)
             elif((res in marrons )or( res in Hexmarrons)):
                print("Groupe des marrons")
                infoGrp="\n elle est une dérivé de la couleur Marrone"
                txt="\n  la couleur selectionner est la couleur :"
                txt = txt + res+infoGrp
                type_text(texte2, txt)
             elif((res in gris)or( res in Hexgris)):
                print("Groupe des gris")
                infoGrp="\n elle est une dérivé de la couleur Grise"
                txt="\n  la couleur selectionner est la couleur :"
                txt = txt + res+infoGrp
                type_text(texte2, txt)
             elif((res in blancs )or( res in Hexblancs)):
                 print("Groupe des blancs")
                 infoGrp="\n elle est une dérivé de la couleur blanche" 
                 txt="\n  la couleur selectionner est la couleur "
                 txt = txt + res+infoGrp
                 type_text(texte2, txt)
             elif((res in noirs) or ( res in Hexnoirs)):
                 print("noirs")
                 infoGrp="\n elle est une dérivé de la couleur noire"
                
                 txt="\n  la couleur selectionner est la couleur :"
                 txt = txt + res+infoGrp
                 type_text(texte2, txt)
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
   
     

        
#creation de l'hote
app = customtkinter.CTk()
app.title("Color Bind")
app.geometry("720x420")

#creation de la fenetre destiné a la selection :
    #creation du premier cadre:
cadre1 = customtkinter.CTkFrame( master=app)
cadre1.grid(row =0, column = 0, padx = 10, pady = 10, sticky = "nsew")
 
texte1 = customtkinter.CTkLabel(cadre1, text = "Veuillez entrez le code hexadecimal (Majuscule) ou le nom(minuscule) en anglais de la couleur")
texte1.grid(row = 1, column = 1, columnspan = 2,padx = 10, pady = 10)

entre1 = customtkinter.CTkEntry(cadre1, width = 250, height = 10, corner_radius = 2)
entre1.grid(row=2, column = 2 )

bouton1 = customtkinter.CTkButton(cadre1, text="valider !", height = 10,corner_radius = 2,width = 100,command = recup)
bouton1.grid(row = 2, column=1, padx = 10)

bouton2 = customtkinter.CTkButton(cadre1, fg_color = "red",text = "annuler",hover_color = "white", text_color = "black", command = Nvm)
bouton2.grid(row = 3, column = 2, pady = 20)

    #creation du deuxieme cadre:
cadre2 = customtkinter.CTkFrame(app)
cadre2.grid(row = 0, column = 1)

screen1 = Canvas(cadre2, height = 100, width = 100)
screen1.grid(row = 0, column = 0)
 


#------------------------------------------------------
base2 = customtkinter.CTkFrame( master = app)
base2.grid(row = 2, padx = 10, pady = 10)
texte3 = customtkinter.CTkLabel(base2, text=" Reponse de l'IA :")
texte3.grid(row = 1, padx = 5, pady = 5)
texte2 = Text( base2)
texte2.grid(row = 2, padx = 10, pady = 10)
texte2.configure(width = 70, height = 10)


app.mainloop()
