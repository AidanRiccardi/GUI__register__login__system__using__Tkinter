#This program runs an application that can create a login using Tkinter
#Developed by Daniel Ademeso


from tkinter import *
import os

def delete2():
    screen3.destroy()
    
def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()
    
def delete6():
    screen15.destroy()


def  logout():
    screen7.destroy()
    
def savednow():
    screen10 = Toplevel(screen)
    screen10.title("Saved")
    screen10.geometry("150x150")
    Label(screen10, text = "Saved", fg ='green', font = ("calibri", 11)).pack()
    Label(screen10, text = "").pack()

def save():
    filename = raw_filename.get()
    notes = raw_notes.get()
    data = open(filename, "w")
    data.write(notes)
    data.close()
    savednow()

def create_note():
    global raw_filename
    raw_filename = StringVar()
    global raw_notes
    raw_notes = StringVar()
    
    screen9 = Toplevel(screen)
    screen9.title("Info")
    screen9.geometry("350x300")
    Label(screen9, text = "Please enter a filename for the note below : ", fg ='red', font = ("calibri", 11)).pack()
    Label(screen9, text = "").pack()
    Entry(screen9, textvariable = raw_filename).pack()
    Label(screen9, text = "Please enter the content below : ", fg ='red', font = ("calibri", 11)).pack()
    Label(screen9, text = "").pack()
    Entry(screen9, textvariable = raw_notes).pack()
    Label(screen9, text = "").pack()
    Button(screen9, text = "    Save    ", command =save).pack()

def view_note1():
    filename1 = raw_filename1.get()
    data = open(filename1, "r")
    data1 = data.read()
    screen12 = Toplevel(screen)
    screen12.title("Notes")
    screen12.geometry("450x450")
    Label(screen12, text = "").pack()
    Label(screen12, text = data1).pack()
    data.close()
   
def view_note():
    screen11 = Toplevel(screen)
    screen11.title("Info")
    screen11.geometry("600x600")
    Label(screen11, text = "").pack()
    all_files = os.listdir()
    Label(screen11, text = "Please view file below : ", fg ='green', font = ("calibri", 11)).pack()
    Label(screen11, text = all_files).pack()
    global raw_filename1
    raw_filename1 = StringVar()
    Entry(screen11, textvariable = raw_filename1).pack()
    Label(screen11, text = "").pack()
    Button(screen11, command = view_note1, text = "View Note").pack()

def note_not_found():
    global screen15
    screen15 = Toplevel(screen)
    screen15.title("Note not found")
    screen15.geometry("400x100")
    Label(screen15, text = "The filename entered is not found in the directory", fg ='red', font = ("calibri", 11)).pack()
    Button (screen15, text = "OK", command = delete6).pack()

def delete_note1():
    try:
        filename3 = raw_filename2.get()
        os.remove(filename3)
        screen13 = Toplevel(screen)
        screen13.title("Delete Note")
        screen13.geometry("450x450")
        Label(screen13, text = "").pack()
        Label(screen13, text = filename3 + " removed").pack()
    except FileNotFoundError:
        note_not_found()
    
def delete_note():
    screen14 = Toplevel(screen)
    screen14.title("Info")
    screen14.geometry("600x600")
    Label(screen14, text = "").pack()
    all_files1 = os.listdir()
    Label(screen14, text = "Please type file to be deleted below : ", fg ='green', font = ("calibri", 11)).pack()
    Label(screen14, text = all_files1).pack()
    global raw_filename2
    raw_filename2= StringVar()
    Entry(screen14, textvariable = raw_filename2).pack()
    Label(screen14, text = "").pack()
    Button(screen14, command = delete_note1, text = "Delete Note").pack()



def session():
    screen8 = Toplevel(screen)
    screen8.title("Dashboard")
    screen8.geometry("450x450")
    Label(screen8, text = "Welcome to the Dashboard", fg ='Blue', font = ("calibri", 11)).pack()
    Label(screen8, text = "").pack()
    Button(screen8, text = "Create Note", command = create_note).pack()
    Label(screen8, text = "").pack()
    Button(screen8, text = "View Note  ", command = view_note).pack()
    Label(screen8, text = "").pack()
    Button(screen8, text = "Delete Note", command = delete_note).pack()
    Label(screen8, text = "").pack()

def login_success():
    session()

def password_not_recognized():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Password not recognized")
    screen.geometry("150x100")
    Label(screen4, text = "Password not recognized", fg ='red', font = ("calibri", 11)).pack()
    Button (screen4, text = "OK", command = delete3).pack()

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("User not found")
    screen.geometry("150x100")
    Label(screen5, text = "User not found", fg ='red', font = ("calibri", 11)).pack()
    Button (screen5, text = "OK", command = delete4).pack()

def register_user ():
    username_info = username.get()
    password_info = password.get()
    
    file = open (username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info + "\n")
    file.close()
    
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(screen1, text = "Registration complete", fg ='green', font = ("calibri", 11)).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open (username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognized()
    else:
       user_not_found() 

        
def register ():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    
    Label(screen1, text = "Please enter your Username and Password").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username *").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password *").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = "10", height = "1", command = register_user).pack()
    
def login ():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Register")
    screen2.geometry("300x250")
    Label(screen2, text = "Please enter your Username and Password").pack()
    Label(screen2, text = "").pack()

    global username_verify
    global password_verify
    
    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1
    Label(screen2, text = "Username *").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Password *").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width = "10", height = "1", command = login_verify).pack()
    
    

def main_screen ():
    global screen
    screen=Tk()
    screen.geometry("300x250")
    screen.title("Note Application")
    Label(text = "Note Application", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text = "").pack()
    Button(text = "Register", height = "2", width = "30", command = register).pack()
    
    screen.mainloop() 
    
main_screen()






