import os
import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as bs
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

my_secret = os.environ['ditbot']
bot = telebot.TeleBot(my_secret)

#message start
print("Bot telegram DitBOT telah dinyalakan... \nUntuk Menutup, Silahkan menggunakan CTRL+C")
	
# print(cont.prettify())
waktuFC = {'Dini Hari': '', 'Pagi': '' , 'Siang': '', 'Malam': '','Dini Hari1': '', 'Pagi1': '' , 'Siang1': '', 'Malam1': '','Dini Hari2': '', 'Pagi2': '' , 'Siang2': '', 'Malam2': ''}
kode = {
'0': '\U00002600 Cerah / Clear Skies',
'1': '\U000026C5 Cerah Berawan / Partly Cloudy',
'2': '\U000026C5 Cerah Berawan / Partly Cloudy ',
'3': '\U000026C5 Berawan / Mostly Cloudy',
'4': '\U00002601 Berawan Tebal / Overcast ',
'5': '\U0001F301 Udara Kabur / Haze ',
'10': '\U0001F525 Asap / Smoke',
'45': '\U0001F301 \U0001F301 Kabut / Fog',
'60': '\U0001F4A7 Hujan Ringan / Light Rain',
'61': '\U00002614 Hujan Sedang / Rain',
'63': '\U00002614 \U00002614 Hujan Lebat / Heavy Rain ',
'80': '\U00002614 Hujan Lokal / Isolated Shower',
'95': '\U0001F4A8 Hujan Petir / Severe Thunderstorm',
'97': '\U0001F4A8 Hujan Petir / Severe Thunderstorm'
}

sendhelp = str(
	'Untuk masukkan silahkan kontak @Amardfajri' +
	'\n\nCommand List' +
	'\n /start - Menampilkan Menu' +
	'\n /lagu - Memberikan link youtube lagu secara acak' +
	'\n /cat - Memberikan gambar kucing random [Cat As A Service]' +
	'\n /help - Menampilkan bantuan'
	)

# FCcuaca = ""

def Fcuaca():
  url = "https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-Banten.xml"
  response = requests.request("GET",url,verify=False)
  r = response.text
  cont = bs(r,"xml")
  contTang = cont.find(id="5002333")
  TangWeat = contTang.find(id="weather")
  # Tangerang 
  Tangh0 = TangWeat.find(h='0')
  h0 = Tangh0.value.string
  waktuFC['Dini Hari'] = kode[h0]
  Tangh6 = TangWeat.find(h='6')
  h6 = Tangh6.value.string
  waktuFC['Pagi'] = kode[h6]
  Tangh12 = TangWeat.find(h='12')
  h12 = Tangh12.value.string
  waktuFC['Siang'] = kode[h12]
  Tangh18 = TangWeat.find(h='18')
  h18 = Tangh18.value.string
  waktuFC['Malam'] = kode[h18]
  Tangh24 = TangWeat.find(h='24')
  h24 = Tangh24.value.string
  waktuFC['Dini Hari1'] = kode[h24]
  Tangh30 = TangWeat.find(h='30')
  h30 = Tangh30.value.string
  waktuFC['Pagi1'] = kode[h30]
  Tangh36 = TangWeat.find(h='36')
  h36 = Tangh36.value.string
  waktuFC['Siang1'] = kode[h36]
  Tangh42 = TangWeat.find(h='42')
  h42 = Tangh42.value.string
  waktuFC['Malam1'] = kode[h42]
  Tangh48 = TangWeat.find(h='48')
  h48 = Tangh48.value.string
  waktuFC['Dini Hari2'] = kode[h48]
  Tangh54 = TangWeat.find(h='54')
  h54 = Tangh54.value.string
  waktuFC['Pagi2'] = kode[h54]
  Tangh60 = TangWeat.find(h='60')
  h60 = Tangh60.value.string
  waktuFC['Siang2'] = kode[h60]
  Tangh66 = TangWeat.find(h='66')
  h66 = Tangh66.value.string
  waktuFC['Malam2'] = kode[h66]

  FCcuaca = str(
  "Cuaca [Tangerang Kota]\n-Hari ini- \n Dini Hari : " + 
  waktuFC['Dini Hari'] +
  "\n Pagi : " +
  waktuFC['Pagi'] +
  "\n Siang : " +
  waktuFC['Siang'] +
  "\n Malam : " +
  waktuFC['Malam'] +
  "\n-Besok- \n Dini Hari : " + 
  waktuFC['Dini Hari1'] +
  "\n Pagi : " +
  waktuFC['Pagi1'] +
  "\n Siang : " +
  waktuFC['Siang1'] +
  "\n Malam : " +
  waktuFC['Malam1'] +
  "\n-Lusa- \n Dini Hari : " + 
  waktuFC['Dini Hari2'] +
  "\n Pagi : " +
  waktuFC['Pagi2'] +
  "\n Siang : " +
  waktuFC['Siang2'] +
  "\n Malam : " +
  waktuFC['Malam2'] +

  "\n\nSumber : BMKG"

  )
  return FCcuaca

def cataas():
  catpic = requests.get("https://cataas.com/cat").content
  return catpic

@bot.message_handler(commands=['cat'])
def send_cat(message):
	chat_id = message.chat.id
	catpic = cataas()
	bot.send_photo(chat_id, photo=catpic,caption="cataas.com")

@bot.message_handler(commands=["start"])
def inline(message):
	key = types.InlineKeyboardMarkup()
	but_1 = types.InlineKeyboardButton(text="Help", callback_data="Help")
	but_2 = types.InlineKeyboardButton(text="Cuaca", callback_data="cuaca")
	but_3 = types.InlineKeyboardButton(text="Hiburan", callback_data="Hiburan")
	but_4 = types.InlineKeyboardButton(text="Sispak", callback_data="Sispak")
	but_menu = types.InlineKeyboardButton(text="Main Menu", callback_data="MainMenu")
	key.add(but_1, but_2, but_3, but_4, but_menu)
	bot.send_message(message.chat.id, "Halo Bos!, Sehat & Semangat!", reply_markup=key)

@bot.callback_query_handler(func=lambda c:True)
def inline(c):
  if c.data == 'Help':
    bot.send_message(c.message.chat.id, sendhelp)
  if c.data == 'cuaca':
    text = Fcuaca()
    bot.send_message(c.message.chat.id, text)
  if c.data == 'Hiburan':
    bot.send_message(c.message.chat.id, 'Hiburan\n')
  if c.data == 'Kala2':
    bot.send_message(c.message.chat.id, 'Kala2\n')
  if c.data == 'MainMenu':
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Help",callback_data="Help")
    but_2 = types.InlineKeyboardButton(text="Cuaca", callback_data="Cuaca")
    but_3 = types.InlineKeyboardButton(text="Hiburan", callback_data="Hiburan")
    but_4 = types.InlineKeyboardButton(text="Sispak", callback_data="Sispak")
    but_menu = types.InlineKeyboardButton(text="Main Menu", callback_data="MainMenu")
    key.add(but_1, but_2, but_3, but_4, but_menu)
    bot.send_message(c.message.chat.id, "Main Menu", reply_markup=key)


@bot.message_handler(commands=['cuaca'])
def send_weather(message):
  text = Fcuaca()
  bot.reply_to(message, text)

@bot.message_handler(commands=['cat'])
def send_weather(message):
  text = Fcuaca()
  bot.reply_to(message, text)

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, sendhelp)

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)

bot.polling()