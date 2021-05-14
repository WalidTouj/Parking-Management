'''
# initialiser le dictionnaire 
parking={1:"libre",2:"libre",3:"libre",4:"libre",5:"libre",6:"libre",7:"libre",8:"libre",9:"libre",10:"libre"}

#entree voiture
barriereentre=0
barrieresortie=0
detventree=0
detvsortie=0
print(parking)
while(True):
    
    detventree=int(input('donner valeur de capteur de l entree'))

    if detventree==1 :
        print('bienvenu')
#verification de place
        for i in parking:
            #if parking.get(i)=="libre":
            if check() != []:    



            
                print("votre place est: ",i)
                parking[i]="occupé"
                barriereentre=1
                print(parking)
                break

        else :
            print("desole pas de place")


#sortie voiture
   

'''
import sqlite3
conn = sqlite3.connect('parking.db')
c = conn.cursor() # RUN THE QUERIES






from tkinter import *
from random import *
from  PIL import ImageTk,Image
      




window= Tk()

window.title("Parking")

window.geometry("800x500")
window.config(background='#a3a3a3')
window.iconbitmap("parking.ico")

#création image
'''
pic= ImageTk.PhotoImage("img.png")
label_i=Label(window,image=pic)
label_i.pack()


'''


frame=Frame(window,background='#a3a3a3')


label=Label(window,text='Bienvenue',font=("Helvetica",40),bg='#E61155',fg='white')

label.pack()


'''
width = 300
height = 300
image= PhotoImage(file="img.png").zoom(10).subsample(32)
Canvas=Canvas(frame, width= width , height= height , bg = "#a3a3a3" , bd=0 , highlightthickness= 0)
Canvas.create_image(width/2, height/2, image=image)
#Canvas.grid(row=0, column= 0, sticky= W )
Canvas.pack()
'''
'''
#bg
bg = PhotoImage(file = "img.png")# //////// emplacement fichier
#create a canvas
my_canvas = Canvas(window, width=900, height=600)
my_canvas.pack(fill ="both", expand=True )

#set image in canvas
my_canvas.create_image(500,300, image =bg)  
my_canvas.create_text(500, 120,text='Welcome', font =('Helvetica', 50), fill ='light grey')
'''
'''
button1 = Button(window, text='Propriétaire')
button2 = Button(window, text='Chauffeur')
button3 = Button(window, text='Drifter :-P')
button_quit = Button(window , text='Exit', command=window.quit)'''



'''button3_window = my_canvas.create_window(465,300,anchor="nw", window=button3)
button_quit = my_canvas.create_window(885,580,anchor="nw", window=button_quit)'''


           
def check():
    
    var=0   
    #result = c.execute(''' SELECT id FROM place  WHERE etat = 'libre' ''')
    #print ('Check ****')
    #print(result.fetchall())
    #print ('votre place est : ')
    result1 = c.execute(''' SELECT id FROM place WHERE etat = 'libre' ORDER BY id ''')
   
    var=result1.fetchone()[0]
    bu_entry.delete(0,END)
        

    bu_entry.insert(0,var)
    
    return(var)         

bu=Button(frame,text='Cliquer ici',font=("Helvetica",20),bg='#E61155',fg='white',command=check)
bu.pack()

bu_entry=Entry(frame,font=("Helvetica",20),fg='black',borderwidth=5,width=1)

bu_entry.pack()
'''bu = my_canvas.create_window(460,200,anchor="nw", window=bu)
bu_entry= my_canvas.create_window(465,250,anchor="nw", window=bu_entry)'''


frame.pack(expand=YES)







def initialiser_BD(x):
        parking=[]
        d1={}
        
        
        parking =[{"id":i,"etat":'libre'} for i in range(1,x+1)]
                        
                        
                
                
        
        print(parking)
        
        #Create table " place "
        c.execute('''CREATE TABLE place (id number primary key ,
                    etat varchar(10) check (etat in ("libre","occupeé")))''')    

        # Insert information into table " place "
        for i in parking:
            c.execute('''INSERT INTO place (id,etat) VALUES(:id,:etat)''',i)
            conn.commit() #Save after modification




x=int(input('donner nombre de place '))
initialiser_BD(x)


# Print result on screen python IDLE
BD=c.execute('SELECT * FROM place ')
print(BD.fetchall())
code=0

while(True):
     
        detventree=int(input('donner valeur de capteur de l entree'))  
        if detventree==1 :
                
                    
                    
                #verification de place
                    c.execute('''SELECT etat FROM place ''')
                    rows=c.fetchall()
                    row=('libre',)
                    
                            
                    
                    if row in rows:
                            print('bienvenu')
                            NB=c.execute('''SELECT COUNT (*) FROM place WHERE etat='libre' ''')
                            print("les palces vides sont: ",NB.fetchone()[0])
                            
                            conn.commit()
                            print("votre place est:",check())
                            v=check()
                            c.execute('''UPDATE place SET etat=? WHERE id=?  ''',('occupeé',v))
                            conn.commit()
                                            
                    else:
                            print("desoooooolééééééééééé")
                            
                
           
                     
                        
        detvsortie=int(input('donner valeur de capteur de sortie'))
        if detvsortie==1 :
            
            while(True):
                    
                code=int(input("saisir votre code: "))
                if code in range(1,x+1):
                        break



                
            c.execute('''UPDATE place SET etat=? WHERE id=? ''',('libre',code))
            conn.commit()
            barrieresortie=1
            print("Good Bye")
            c.execute('''SELECT * FROM place''')
            s=c.fetchall()
            print(s)
            break
            


window.mainloop()
c.close()
conn.close() # completely done
