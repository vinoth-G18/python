from datetime import datetime 
import pygame

pygame.init()
pygame.mixer.init()
user_input=input("enter the alarm time : HH:MM:SS:am or pm :")
alarm_hour=user_input[0:2]
alarm_min=user_input[3:5]
alarm_sec=user_input[6:8]
alarm_period=user_input[9:11].upper()

print("======alarm setted========")
while True:
    now=datetime.now()
    if alarm_period==now.strftime("%p"):
        if alarm_hour==now.strftime("%H"):
            if alarm_min==now.strftime("%M"):
                if alarm_sec==now.strftime("%S"):
                    print("wake up!!!!")
                    pygame.mixer.music.load("alarm.mp3")
                    pygame.mixer.music.play()
                    
                    while pygame.mixer.music.get_busy():
                        pass
    
                    
 
    
 
