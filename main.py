'''Read  Paragraph from the user and count the number of words and frequancy of word appearing and search for a specific word'''
import tkinter as tk
from customtkinter import *
from tkinter.scrolledtext import ScrolledText
from PIL import Image,ImageTk

#creating the main window
window=tk.Tk()
#window=CTk()
window.title('Search for a specific word ')
window.config(bg='grey39')
window.geometry('400x600')

image2 = Image.open("background image path")
photo2 = ImageTk.PhotoImage(image2)

blabel=tk.Label(window,image=photo2,bg="white")
blabel.place(relwidth=1,relheight=1)
#photo=tk.PhotoImage(file=r"c:\\Users\\shrin\\OneDrive\\Documents")
#window.create_image(0,0,image=photo,anchor=NW)
#college logo
image = Image.open("InstitutionLogopath")
newsize=(60,60)
rimage=image.resize(newsize)

# Convert the Pillow Image to a PhotoImage
photo = ImageTk.PhotoImage(rimage)

# Create a label in the Tkinter window and set the image
label2 = tk.Label(window, image=photo,bg="white")
label2.pack(anchor='nw')
#Createing a main heading 
main_heading = tk.Label(window, text="Name College of Engineering. city", font=("Times New Roman", 14),bg='White')
main_heading.pack()


# Create and place secondary heading with an even smaller font size
secondary_heading = tk.Label(window, text="Name : ", font=("Times New Roman", 10),bg='white')
secondary_heading.pack(pady=10)

#third heading
third_heading=tk.Label(window,text='Enter a paragraph',font=('Times New Roman',10))
third_heading.pack()

st1=ScrolledText(window,width=40,height=5)
st1.pack(pady=5)
label=tk.Label(window,text="Result",font=('Times New Roman',10),bg='lightblue2')
label.pack(pady=5)

st2=ScrolledText(window,width=40,height=5)
st2.pack()

label3=tk.Label(window,text="Enter the word to search",font=("Times New Roman",10),bg="lightblue2")
label3.pack()
entry=tk.Entry(window,font=("times New Roman",15),bg="skyblue")
entry.pack(padx=5,pady=5)

def manupulate():
     strg = st1.get('1.0', tk.END)
     print(str)

     #split() method splits the string into list
     #The len function finds the list count

     wordcount=len(strg.split())
     counts=dict()
     words=strg.split()
     print(words)
     #insert
     print(counts)

     for word in words:
         if word in counts:
            counts[word]=counts[word]+1
         else:
            counts[word]=1
         st2.insert('1.0',"{0} found {1} times\n".format(word,counts[word]))

     #Run the loop to display the words count
     #Print the dictionary content and occurence using counts
     #input string words to search

def search():
    strg = st1.get('1.0', tk.END)
    words = strg.split()
    print(words)
    w=0
    searchw=entry.get()
    for i in range(0,len(words)):
        if searchw==words[i]:
            w=w+1
    if w>0:
        text="Search Result "+f"{searchw} found {w} times."

    else:
        text="Search Result "+f"{searchw} not found!"
    label4=tk.Label(text=text,font=("Times New Roman",15),bg="lightskyblue")
    label4.pack(pady=5)

button=CTkButton(window,text="go",corner_radius=32,command=manupulate)
button.place(anchor="sw",relx=0.5,rely=0.5)


btns = Image.open("search icon image path")
newsize=(20,20)
bimage=btns.resize(newsize)
srch = ImageTk.PhotoImage(bimage)

button2=tk.Button(window,image=srch,command=search,anchor='se')
button2.pack(padx=5,pady=5)

for widget in (label2,main_heading,secondary_heading,st1,button,st2,entry, button2):
    widget.pack_configure(anchor='center')


window.mainloop()