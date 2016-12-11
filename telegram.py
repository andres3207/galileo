#!/usr/bin/python

import telepot
import time

def handle(msg):
   chat_id=msg['chat']['id']
   msg_rec=msg['text']
   if(msg_rec.lower()=="prender"):
      write_led(1)
      msg="LED ACTIVADO"
      bot.sendMessage(chat_id,msg)
   elif(msg_rec.lower()=="apagar"):
      write_led(0)
      msg="LED DESACTIVADO"
      bot.sendMessage(chat_id,msg)
   else:
      msg="Comando no reconocido"
      bot.sendMessage(chat_id,msg)



def pins_export():
    try:
        pin1export = open("/sys/class/gpio/export","w")
        pin1export.write("3")
        pin1export.close()
    except IOError:
        print "INFO: GPIO 3 already exists, skipping export"

    fp1 = open( "/sys/class/gpio/gpio3/direction", "w" )
    fp1.write( "out" )
    fp1.close()

def write_led( value ):
    fp2 = open( "/sys/class/gpio/gpio3/value", "w" )
    fp2.write( str( value ) )
    fp2.close()


pins_export()




bot=telepot.Bot('309247031:AAFn9TktR2vsHxLC-1a5A_kZ5hrh6QWIR0o')
bot.message_loop(handle)
while 1:
   time.sleep(10)
