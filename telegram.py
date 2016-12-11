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
  elif(msg_rec.lower()=="temperatura"):
    n_adc0=A0_read()
    #print n_adc0
    temp=500*float(n_adc0)/4095
    #print temp
    temp="{0:0.1f}".format(temp)
    #print temp
    msg=str(temp)
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

  try:
    pinA0export = open("/sys/class/gpio/export","w")
    pinA0export.write("37")
    pinA0export.close()
  except IOError:
    print "INFO: AN0 already exists, skipping export"

  fA0 = open("/sys/class/gpio/gpio37/direction","w")
  fA0.write("out")
  fA0.close()

  f2A0 = open("/sys/class/gpio/gpio37/value","w")
  f2A0.write("0")
  f2A0.close()

def write_led( value ):
  fp2 = open( "/sys/class/gpio/gpio3/value", "w" )
  fp2.write( str( value ) )
  fp2.close()

def A0_read():
  fA0=open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw","r")
  dato=fA0.read()
  return dato



pins_export()




bot=telepot.Bot('309247031:AAFn9TktR2vsHxLC-1a5A_kZ5hrh6QWIR0o')
bot.message_loop(handle)
while 1:
  time.sleep(10)
