# бот погоды v 2.0

import pyowm
import telebot

owm = pyowm.OWM( '1497f11e6aaf6ebabe90829f6d47a0bf', language = "ru" )
bot = telebot.TeleBot( "1080076453:AAHr8DbGWLER1w6jObvFOiVeweJzhzTLAr8" )

@bot.message_handler( content_types=['text'] )
def send_echo( message ):
    observation = owm.weather_at_place( message.text )
    w = observation.get_weather()
    temp = w.get_temperature( 'celsius' )["temp"]
    answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
    answer += "Температура где-то " + str(temp) + " градусов!" + "\n\n"
    
    if temp < 5:
        answer += "Снаружи дикий дубак, завернись поплотнее..."
    elif temp < 10:
        answer += "Еще чуть-чуть и будет тепло! От зимнего пальто не стоит избавляться."
    elif temp < 20:
        answer += "Погода просто топ - легкая куртка и кроссы будут кстати."
    else:
        answer += "Почти жара... Куртку можно оставить дома :)"

    bot.send_message( message.chat.id, answer )

bot.polling( none_stop = True )
