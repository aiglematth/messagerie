from save import *
chemin_csv = 'constantes.txt' # A EDITER
hex_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

s = Save()
ldata = s.LoadData(chemin_csv)
font_color = ldata['font_color']
z_text_color = ldata['z_text_color']
text_color = ldata['text_color']
login = ldata['login']

title = 'Messagerie'
taille = "1200x800"
resiz = (False, False)

""" Constantes à mettre dans la sauvegarde...c'est provisoire """
ip = 'localhost' # POUR LES TESTS
port = 4444      # POUR LES TESTS

""" Constantes de la classe Interface_chat """
ecrire_width = 64
ecrire_heigth = 40
ecrire_x = 640
ecrire_y = 10

afficher_width = 64
afficher_heigth = 45
afficher_x = 10
afficher_y = 10

button_width = 32
button_heigth = 3
button_x = 900
button_y = 720

button_2_x = 640
button_2_y = 720

""" Constantes de la classe Interface_login """
label_width = 32
label_x = 480
label_y = 200

label_log_x = 480
label_log_y = 320

label_pass_x = 480
label_pass_y = 390

entre_width = 32

entre_log_x = 480
entre_log_y = 350

entre_pass_x = 480
entre_pass_y = 420

button_con_width = 32
button_con_height = 2
button_con_x = 470
button_con_y = 450

""" Constantes de la classe Interface_mainmenu """
label_main_width = 64
label_main_x = 350
label_main_y = 10

button_att_x = 480
button_att_y = 150

button_com_x = 480
button_com_y = 250

options_x = 480
options_y = 350

""" Constantes de la classe Interface_com """
label_avec_qui_width = 64
label_avec_qui_x = 350
label_avec_qui_y = 10

entre_avec_qui_width = 32
entre_avec_qui_x = 480
entre_avec_qui_y = 250

button_avec_qui_width = 32
button_avec_qui_height = 3
button_avec_qui_x = 480
button_avec_qui_y = 350

button_retour_width = 10
button_retour_height = 1
button_retour_x = 1
button_retour_y = 1

label_login_width = 32
label_login_x = 380
label_login_y = 220

""" Constantes de la classe Interface_options """
couleurs = ['rouge', 'bleu', 'vert', 'blanc', 'gris', 'noir', 'rose', 'jaune']
values = ['#bb0000', '#0039bd', '#4bff48', '#ffffff', '#2b303c', '#000000', '#ff00cd', '#fff300']

font_color_x = 40
font_color_y = 300

text_color_x = 900
text_color_y = 300

z_text_color_x = 500
z_text_color_y = 300

label_z_text_color_width = 32
label_z_text_color_x = 490
label_z_text_color_y = 250

button_save_height = 3
button_save_width = 32
button_save_x = 480
button_save_y = 700

label_font_color_width = 32
label_font_color_x = 30
label_font_color_y = 250

label_text_color_width = 64
label_text_color_x = 750
label_text_color_y = 250
