#import os
#from subprocess import Popen
#os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /usr/share/backgrounds/Stargazing_by_Marcel_Kächele.jpg")
#Popen("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /usr/share/backgrounds/Sky_Sparkles_by_Joe_Thompson.jpg")


from subprocess import Popen
import random

lst = ["Beijling_park_burial_path_by_Mattias_Andersson.jpg","Ermine_lines_by_Gustavo_Brenner.png","Flight_dive_by_Nicolas_Silva.png","Frozen_sunset_on_the_lake_by_Manuel_Arslanyan.jpg",
"Origin_of_nature_by_Julian_Tomasini.jpg"]

picture_path = "//usr//share//backgrounds//" + random.choice(lst)
Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format(picture_path), shell=True)