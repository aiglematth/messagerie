# Modules fais main
from new_crypto import *
from netsocket import *
from save import *
from constantes import *
# Modules python
from tkinter import *
from shlex import split
from time import sleep
import socket
import tkinter.scrolledtext as st
import sys
import threading

message = ''

class Interface_chat(Tk):

    def __init__(self, connexion):
        Tk.__init__(self)

        self.connexion = connexion

        self.ancien_mess = 'ancien_mess'
        self.ancien_mess_2 = 'ancien_mess_2'

        self.ecrire = ''

        self.afficher = ''

        self.button = ''

        self.button_2 = ''

        self.recup_ecrire = StringVar()
        self.env_ecrire = StringVar()

        self.main()

    def main(self):
        self.title(title)
        self.geometry(taille)
        self.resizable(width=resiz[0], height=resiz[1])
        self.configure(bg=font_color)

        self.widgets(self, self.f_envoyer, self.f_fin)

    def widgets(self, fenetre, func_env, func_fin):
        self.ecrire = st.ScrolledText(fenetre, width=ecrire_width, height=ecrire_heigth, wrap='word', bg=text_color, fg=z_text_color)
        self.ecrire.place(x=ecrire_x, y=ecrire_y)

        self.afficher = st.ScrolledText(fenetre, width=afficher_width, height=afficher_heigth, wrap='word', bg=text_color, fg=z_text_color)
        self.afficher.place(x=afficher_x, y=afficher_y)

        self.button = Button(fenetre, text='Envoyer', command=func_env, width=button_width, height=button_heigth, fg=z_text_color)
        self.button.place(x=button_x, y=button_y)

        self. button_2 = Button(fenetre, text='Fin de la connexion', width=button_width, height=button_heigth, command=func_fin, fg=z_text_color)
        self.button_2.place(x=button_2_x, y=button_2_y)

        thaff = ThrAFF(self.f_afficher)
        thaff.start()

    def f_afficher(self):
        c=0
        while c<10000:
            if self.ancien_mess != message and self.ancien_mess_2 != self.ancien_mess:
                self.afficher.insert(END, message+'\n')
                self.bell()
                self.ancien_mess_2 = self.ancien_mess
                self.ancien_mess = message
                print('message', c)
            else:
                pass
            c+=1
            sleep(0.1)

    def f_envoyer(self):
        c = Crypto()
        mess = self.ecrire.get('0.0', 'end')
        mess = '{} : '.format(login) + mess
        mess = c.encrypt(mess).encode()
        print(mess, type(mess))
        try:
            self.connexion.send(mess)
            self.afficher.insert(END, c.decrypt(mess.decode())+'\n')
        except:
            self.afficher.insert(END, 'Echec de l\'envoi, la communication a pu être rompue.\n')

    def f_fin(self):
        c = Crypto()
        self.destroy()
        self.connexion.send(c.encrypt('Fin de la connexion...Veuillez quitter la messagerie.').encode())
        self.connexion.close()
        t = ThrATT(Interface_mainmenu)
        t.start()

class Interface_login(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.label = ''

        self.entre_log = ''

        self.entre_pass = ''

        self.button_con = ''

        self.label_log = ''

        self.label_pass = ''

        self.login_get = StringVar()
        self.password_get = StringVar()

        self.main()

    def main(self):
        self.title(title)
        self.geometry(taille)
        self.resizable(width=resiz[0], height=resiz[1])
        self.configure(bg=font_color)

        self.widgets(self.func_env)

    def widgets(self, func_env):
        self.label = Label(self, text='Bienvenu sur la page de login.', width=label_width, fg=z_text_color, bg=font_color)
        self.label.place(x=label_x, y=label_y)

        self.label_log = Label(self, text='Login :', width=entre_width, fg=z_text_color, bg=font_color)
        self.label_log.place(x=label_log_x, y=label_log_y)

        self.entre_log = Entry(self, textvariable=self.login_get, width=entre_width, fg=z_text_color)
        self.entre_log.place(x=entre_log_x, y=entre_log_y)

        self.label_pass = Label(self, text='Password :', width=entre_width, fg=z_text_color, bg=font_color)
        self.label_pass.place(x=label_pass_x, y=label_pass_y)

        self.entre_pass = Entry(self, textvariable=self.password_get, width=entre_width, show='*', fg=z_text_color)
        self.entre_pass.place(x=entre_pass_x, y=entre_pass_y)

        self.button_con = Button(self, text='Confirmer', width=button_con_width, height=button_con_height, command=func_env, fg=z_text_color)
        self.button_con.place(x=button_con_x, y=button_con_y)

    def func_env(self):
        logpass = (login, password) = (self.login_get.get(), self.password_get.get())
        return logpass

class Interface_mainmenu(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.label = ''

        self.button_att = ''

        self.button_com = ''

        self.options = ''

        self.main()

    def main(self):
        self.title(title)
        self.geometry(taille)
        self.resizable(width=resiz[0], height=resiz[1])
        self.configure(bg=font_color)

        self.widgets(self.func_att, self.func_com, self.func_options)

    def widgets(self, func_att, func_com, func_options):
        self.label = Label(self, text='Bienvenu sur le menu principal de l\'application.', width=label_main_width, fg=z_text_color, bg=font_color)
        self.label.place(x=label_main_x, y=label_main_y)

        self.button_att = Button(self, text='Attendre une comunication', width=button_width, height=button_heigth, command=func_att, fg=z_text_color)
        self.button_att.place(x=button_att_x, y=button_att_y)

        self.button_com = Button(self, text='Lancer une comunication', width=button_width, height=button_heigth, command=func_com, fg=z_text_color)
        self.button_com.place(x=button_com_x, y=button_com_y)

        self.options = Button(self, text='Options', width=button_width, height=button_heigth, command=func_options, fg=z_text_color)
        self.options.place(x=options_x, y=options_y)

    def func_att(self):
        self.destroy()
        t = ThrATT(Interface_att_t)
        t.start()

        Serv = Serveur(ip, port)
        conn = Serv.serveur()
        clientandinfo = Serv.open_serveur(conn)
        client = clientandinfo[0]

        thfen = ThrGUI(client, Interface_chat)
        th = Threcv(client)
        th.start()
        thfen.start()

    def func_com(self):
        self.destroy()
        t = Interface_com()
        t.mainloop()

    def func_options(self):
        self.destroy()
        t = Interface_options()
        t.mainloop()

class Interface_com(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.label = ''

        self.entre_log = ''

        self.button = ''

        self.button_retour = ''

        self.login_get = StringVar()

        self.label_login = ''

        self.main()

    def main(self):
        self.title(title)
        self.geometry(taille)
        self.resizable(width=resiz[0], height=resiz[1])
        self.configure(bg=font_color)

        self.widgets(self.func_com, self.func_retour)

    def widgets(self, func_com, func_retour):
        self.label = Label(self, text='Avec qui voulez vous communiquer ?', width=label_avec_qui_width, fg=z_text_color, bg=font_color)
        self.label.place(x=label_avec_qui_x, y=label_avec_qui_y)

        self.label_login = Label(self, text='Login : ', width=label_login_width, fg=z_text_color, bg=font_color)
        self.label_login.place(x=label_login_x, y=label_login_y)

        self.entre_log = Entry(self, textvariable=self.login_get, width=entre_avec_qui_width, fg=z_text_color)
        self.entre_log.place(x=entre_avec_qui_x, y=entre_avec_qui_y)

        self.button = Button(self, text='Communiquer', width=button_avec_qui_width, height=button_avec_qui_height, command=func_com, fg=z_text_color)
        self.button.place(x=button_avec_qui_x, y=button_avec_qui_y)

        self.button_retour = Button(self, text='Retour', width=button_retour_width, height=button_retour_height, command=func_retour, fg=z_text_color)
        self.button_retour.place(x=button_retour_x, y=button_retour_y)

    def have(self):
        self.login_get.set(self.login_get.get())

    def func_com(self):
        self.have()
        print(self.login_get.get())
        self.destroy()

        client = Client('localhost', 4444)
        conn = client.client()
        client.connect_client(conn)

        t = Interface_chat
        thfen = ThrGUI(client, t)
        th = Threcv(client)
        th.start()
        thfen.start()

    def func_retour(self):
        self.destroy()
        t = Interface_mainmenu()
        t.mainloop()

class Interface_att_t(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Mise en attente...')
        self.geometry('800x200')
        self.resizable(width=False, height=False)
        self.configure(bg=font_color)

        self.label = ''

        self.main()

    def main(self):
        self.label = Label(self, text='Mise en attente...vous pouvez fermer ce message, votre ordinateur attends des connexions.', fg=z_text_color, bg=font_color)
        self.label.place(x=40, y=90)

class Interface_options(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.button = ''

        self.label_font_color = ''

        self.font_color = ''

        self.v_font_color = StringVar()

        self.label_text_color = ''

        self.text_color = ''

        self.v_text_color = StringVar()

        self.z_text_color = ''

        self.v_z_text_color = StringVar()

        self.label_z_text_color = ''

        self.button_retour = ''

        self.main()

    def main(self):
        self.title(title)
        self.geometry(taille)
        self.resizable(width=resiz[0], height=resiz[1])
        self.configure(bg=font_color)

        self.widgets(self.func_save, self.func_retour)

    def widgets(self, func_save, func_retour):
        self.button = Button(self, text='sauvegarder', height=button_save_height, width=button_save_width, command=func_save, fg=z_text_color)
        self.button.place(x=button_save_x, y=button_save_y)

        self.label_font_color = Label(self, text='Couleur du fond', width=label_font_color_width, fg=z_text_color, bg=font_color)
        self.label_font_color.place(x=label_font_color_x, y=label_font_color_y)

        self.label_z_text_color = Label(self, text='Couleur du texte', width=label_z_text_color_width, fg=z_text_color, bg=font_color)
        self.label_z_text_color.place(x=label_z_text_color_x, y=label_z_text_color_y)

        self.label_text_color = Label(self, text='Couleur de la zone d\'affichage du texte', width=label_text_color_width, fg=z_text_color, bg=font_color)
        self.label_text_color.place(x=label_text_color_x, y=label_text_color_y)

        self.button_retour = Button(self, text='Retour', width=button_retour_width, height=button_retour_height, command=func_retour, fg=z_text_color)
        self.button_retour.place(x=button_retour_x, y=button_retour_y)

        for i in range(len(values)):
            self.font_color = Radiobutton(self, text=couleurs[i], value=values[i], variable=self.v_font_color, fg=z_text_color, bg=font_color)
            self.font_color.place(x=font_color_x, y=font_color_y+30*i)

        for i in range(len(values)):
            self.text_color =  Radiobutton(self, text=couleurs[i], value=values[i], variable=self.v_text_color, fg=z_text_color, bg=font_color)
            self.text_color.place(x=text_color_x, y=text_color_y+30*i)

        for i in range(len(values)):
            self.z_text_color =  Radiobutton(self, text=couleurs[i], value=values[i], variable=self.v_z_text_color, fg=z_text_color, bg=font_color)
            self.z_text_color.place(x=z_text_color_x, y=z_text_color_y+30*i)

    def func_save(self):
        data = {}
        if self.v_font_color.get() != '':
            data['font_color'] = self.v_font_color.get()
        else:
            pass

        if self.v_text_color.get() != '':
            data['text_color'] = self.v_text_color.get()
        else:
            pass

        if self.v_z_text_color.get() != '':
            data['z_text_color'] = self.v_z_text_color.get()
        else:
            pass

        s = Save()
        s.ChangeData('constantes.txt', data)



    def func_retour(self):
        self.destroy()
        t = Interface_mainmenu()
        t.mainloop()

class Threcv(threading.Thread):
    def __init__(self, connexion):
        threading.Thread.__init__(self)
        self.connexion = connexion
    def run(self):
        global message
        c=0
        while c<10000:
            print('c', c)
            try:
                d = Crypto()
                message = self.connexion.recv(1024)
                message = d.decrypt(message.decode())
                print(message)
                if message.upper() == 'FIN':
                    break
                else:
                    pass
                print(message, type(message))
            except socket.error:
                print('b')
                break
            except:
                pass
            c+=1

class ThrGUI(threading.Thread):
    def __init__(self, connexion, fen):
        threading.Thread.__init__(self)
        self.connexion = connexion
        self.fen = fen
    def run(self):
        fen = self.fen(self.connexion)
        fen.mainloop()

class ThrAFF(threading.Thread):
    def __init__(self, callback):
        threading.Thread.__init__(self)
        self.callback = callback
    def run(self):
        self.callback()

class ThrATT(threading.Thread):
    def __init__(self, fen):
        threading.Thread.__init__(self)
        self.fen = fen
    def run(self):
        self.fen().mainloop()


if __name__ == '__main__':
    t = Interface_mainmenu()
    t.mainloop()



    """Serv = Serveur('localhost', 4444)
    conn = Serv.serveur()
    clientandinfo = Serv.open_serveur(conn)
    client = clientandinfo[0]

    thfen = ThrGUI(client)
    th = Threcv(client)
    th.start()
    thfen.start()
"""
