import pyautogui, time
import keyboard

b = True


lista = []


print("when you end the text press enter two time")
print("dont leave any white line")
print("\nwrote text: ")
while True:
    customized_file = open('customized', "w")
    t = input()
    if t:
        lista.append(t)
    else:
        break
k = '\n'.join(lista)
y = customized_file.write(k)
customized_file.close()
p = 'customized'

print("\nfor activate the bot go on a chat, or a notpad,... and press the letter 'b' 'o' and 't' simultaneously ")
print("and than just look what happend ;-)")

#breakpoint()

while b:
    if keyboard.is_pressed('b') and keyboard.is_pressed('o') and keyboard.is_pressed('t'):
        time.sleep(1)
        file = open(p, "r")
        for i in file:
            pyautogui.typewrite(i)
            pyautogui.press("enter")