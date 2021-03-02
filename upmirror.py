#!/bin/python3
"""
upmirror.py is a script to help you update mirrorlist
 written by:Mohammed Alhoussainy
 2021
 """
import os
import locale
import glob
# get syste locale
loc = locale.getdefaultlocale()
lang = loc[0]
arabic =["جار الترقية","وجد الملف ","تم حذف الملف","تم حفظ المرايا بنجاح ","للاسف فشل حفظ المرايا وهناك خطأ ما. "," لا حاجة للترقية"]
english=["Upgrading Start","found","file deleted","Mirrors saved successfully","Something wrong , mirrors not saved","No UPGREADE NEEDED"]
def upgrade_system():
    upg = os.system("sudo pacman -Syu")
    return upg
if (lang[0:2]) == 'ar':
    list1=arabic
    #
else:
    list1=english
    #  
while True: 
      try:    
         os.system("sudo reflector --verbose --latest 40 --protocol https --protocol http --sort rate --save /etc/pacman.d/mirrorlist") 
         print(list1[3])
         os.chdir("/var/lib/pacman/")
         for file in glob.glob("db.lck"):
             print(file,list1[1])
             os.system("sudo rm db.lck")
             print(list1[2])
             upgrade_system()
             break
         else:    
             upgrade_system()
             break
      except ValueError:
        print(list1[4])

    
