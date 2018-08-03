from uagame import Window
from time import sleep

window = Window("Hacking",500,600)
window.set_font_color("green")
window.set_font_size(18)
window.set_font_name("couriernew")

string_height = window.get_font_height()
y_coord = 0

window.draw_string ("ENTER A PASSWORD", 0, y_coord)
y_coord = y_coord + string_height
window.update()
sleep(0.3)

window.draw_string ("YOU HAVE ONE ATTEMPT", 0, y_coord)
y_coord = y_coord + string_height
window.update()
sleep(0.3)

window.draw_string ("", 0, y_coord)
y_coord = y_coord + string_height
window.update()
sleep(0.3)

password_list = ['SHARKS', 'COOKIE', 'COMPUTER', 'HELLO', 'PURPLE', '']
for password in password_list:
    window.draw_string (password, 0, y_coord)
    y_coord = y_coord + string_height
    window.update()
    sleep(0.3) 
    
correct_answer = 'COMPUTER'

guesses_taken = window.input_string('ENTER A PASSWORD ->',0,y_coord)
y_coord = y_coord + string_height

if correct_answer == guesses_taken:
    window.draw_string ('ACCESS GRANTED!', 0, y_coord)
    y_coord = y_coord + string_height
    window.update()
    sleep(0.3)    
else:
    window.draw_string ("HAHAHAHAHAHAHAHAHAHAHAHA YOU'LL NEVER GET IN!", 0, y_coord)
    y_coord = y_coord + string_height
    window.update()
    sleep(0.3)    



window.close()