print("  ____              _____           _  ") 
print(" |  _ \  _____  __ |_   _|__   ___ | |") 
print(" | | | |/ _ \ \/ /   | |/ _ \ / _ \| |") 
print(" | |_| | (_) >  <    | | (_) | (_) | |") 
print(" |____/ \___/_/\_\   |_|\___/ \___/|_|") 
print("                         by natrix    ")

print('Nom de la vitime:')
name = input()
print('Ok, I am searching informations about ' + name)

# HTTP REQUESTS : (require module http) 
# from http import *
# http.requestURL{instagram, tiktok, snapchat, discord, github, telegram}with name==[name]
# replace $true="✅", $false="❌" else: 
#   exit()

print(' ____________________________')
print('| Instagram: @'+name+'   ✅  |')
print('| TikTok:    @'+name+'   ✅  |')
print('| Snapchat:  @'+name+'   ✅  |')
print('| Discord:   @'+name+'   ❌  |')
print('| Github:    @'+name+'   ❌  |')
print('| Telegram:  @'+name+'   ✅  |')
print('|____________________________|')

print("🕵️Work Done 🕵️")
