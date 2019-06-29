from tkinter import Tk,scrolledtext,Menu,filedialog,END,messagebox
#from tkinter import *
import tkinter .scrolledtext as ScrolledText

root=Tk(className="  EDITOR-USE ME !!!")          #root for window
textArea=ScrolledText.ScrolledText(root,width=100,height=80)

#for OPEN menu option
def openfile():
    file=filedialog.askopenfile(parent=root,mode='rb',title='SELECT A FILE')
    if(file!=None):
        content=file.read()
        textArea.insert('1.0',content)
        file.close()
#for SAVE menu option
def savefile():
    #slice off the
    file=filedialog.asksavefile(mode="w")
    data=textArea.get('1.0',END+'-lc')
    file.write(data)
    file.close
#for EXIT menu option
def exiting():
    if(messagebox.askyesno("quit?","This is a python IDE")):
        root.destroy()
#for ABOUT menu option
def about():
    label=messagebox.showinfo("About!!")


# adding menu options
menu=Menu(root)
root.config(menu=menu)
fileMenu=Menu(menu)
menu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="NEW")
fileMenu.add_command(label="OPEN",command=openfile)   # will redirect to open file
fileMenu.add_command(label="SAVE",command=savefile)
fileMenu.add_command(label="SAVE AS")
fileMenu.add_separator()
fileMenu.add_command(label="EXIT",command=exiting)
helpMenu=Menu(menu)
menu.add_cascade(label="Help")
menu.add_cascade(label="About",command=about)


textArea.pack()

root.mainloop() #to open
