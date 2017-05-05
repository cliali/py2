#-*- coding: utf-8 -*-
import telebot
from telebot import util
import time
from time import sleep
import random
from random import randint
import requests
import requests as req
import redis
import redis as r
import redis as redis
import logging
import base64
import json
import os
import re
import commands
import urllib2
import urllib
import telebot
import subprocess
import ConfigParser
from telebot import types
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
token = '277679081:AAGk3IXlId9PKUn3n_5wrfrUIR_mgsUVCeE' #توکن شما
bot = telebot.TeleBot(token)
redis = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
is_sudo = '242361127' #ایدی شما

print "ربات روشن شد😃"
     
markupstart = types.InlineKeyboardMarkup()
markupstart.add(types.InlineKeyboardButton('فارسی🇮🇷', callback_data='farsi'))
markupstart.add(types.InlineKeyboardButton('English🇺🇸', callback_data='english'))
markupstartfa = types.InlineKeyboardMarkup()
markupstartfa.add(types.InlineKeyboardButton('😂جک😂', callback_data='getjoke'))
markupstartfa.add(types.InlineKeyboardButton('⭕️ارسال جک به ما⭕️', callback_data='sendjoke'))#, types.InlineKeyboardButton('📆زمان📆', callback_data='timefa'))
markupstartfa.add(types.InlineKeyboardButton('👤توسعه دهنده👤', url='https://telegram.me/CliAli'), types.InlineKeyboardButton('📢کانال📢', url='https://telegram.me/TeleStarTeam'))
markupstartfa.add(types.InlineKeyboardButton('رفتن به حالت اینلاین', switch_inline_query=''))
markupstarten = types.InlineKeyboardMarkup()
markupstarten.add(types.InlineKeyboardButton('😂Joke😂', callback_data='getjokeen'))
markupstarten.add(types.InlineKeyboardButton('⭕️Send us joke⭕️', callback_data='sendjokeen'))#, types.InlineKeyboardButton('📆Time📆', callback_data='timeen'))
markupstarten.add(types.InlineKeyboardButton('👤Developer👤', url='https://telegram.me/CliAli'), types.InlineKeyboardButton('📢Channel📢', url='https://telegram.me/TeleStarTeam'))
markupstarten.add(types.InlineKeyboardButton('Inline mode', switch_inline_query=''))
markupjoke = types.InlineKeyboardMarkup()
markupjoke.add(types.InlineKeyboardButton('🔘بعدی🔘', callback_data='joke'))
markupjoke.add(types.InlineKeyboardButton('🔙برگشت', callback_data='back'))
markupchuk = types.InlineKeyboardMarkup()
markupchuk.add(types.InlineKeyboardButton('🔘Next🔘', callback_data='chuk'))
markupchuk.add(types.InlineKeyboardButton('🔙Back', callback_data='backen'))
markupavfa = types.InlineKeyboardMarkup()
markupavfa.add(types.InlineKeyboardButton('🔃تغیر زبان🔃', callback_data='avazfa'))
markupaven = types.InlineKeyboardMarkup()
markupaven.add(types.InlineKeyboardButton('🔃Change language🔃', callback_data='avazen'))
markupback = types.InlineKeyboardMarkup()
markupback.add(types.InlineKeyboardButton('🔙برگشت', callback_data='back'))
markupbacken = types.InlineKeyboardMarkup()
markupbacken.add(types.InlineKeyboardButton('🔙Back', callback_data='backen'))

#################################################################################################################################################################################################

@bot.message_handler(commands=['send'])
def send(m):
        text = m.text.replace('/send ','')
        user = m.from_user.username
        name = m.from_user.first_name
        id = m.chat.id
        bot.send_message(is_sudo, "پیام جدید:\n\nمتن پیام:\n{}\n\nاز طرف:\nیوزرنیم: @{}\nایدی: {}\nاسم: {}".format(text, user, id, name))
        if redis.hget("lang:{}".format(m.chat.id),"farsi"):
            bot.send_message(m.chat.id, "پیام یا انتقاد شما به ما ارسال شد و ما به سروقت به آن رسیدگی میکنیم😊", parse_mode="Markdown")
        elif redis.hget("lang:{}".format(m.chat.id),"english"):
            bot.send_message(m.chat.id, "Your message has been sent and we answer your message soon😊", parse_mode="Markdown")

@bot.message_handler(commands=['toall'])
def toall(m):
    if str(m.from_user.id) == is_sudo:
        text = m.text.replace('/toall','')
        rd = redis.smembers('startmebot')
        for id in rd:
            try:
                bot.send_message(id, "{}".format(text), parse_mode="Markdown")
            except:
                redis.srem('startmebot',id)

@bot.message_handler(commands=['msg'])
def member(m):
    if str(m.from_user.id) == is_sudo:
        id = m.text.split()[1] #ایدی کاربر
        text = m.text.split()[2] #متن
        bot.send_message(id, "{}".format(text), parse_mode="Markdown")

@bot.message_handler(commands=['stats'])
def stats(m):
    if str(m.from_user.id) == is_sudo:
        stats = redis.scard('startmebot')
        bot.send_message(m.chat.id, "`تعداد کاربران`👇\n*{}*".format(stats), parse_mode="Markdown")

@bot.message_handler(commands=['start'])
def start(m):
    id = m.chat.id
    redis.sadd('startmebot',id)
    if redis.hget("lang:{}".format(m.chat.id),"farsi"):
        bot.send_message(m.chat.id, 'زبان فعلی شما فارسی است🇮🇷\nمیتوانید با زدن دکمه ی زیر زبان خود را تغییر دهید🇺🇸', reply_markup=markupavfa)
    elif redis.hget("lang:{}".format(m.chat.id),"english"):
        bot.send_message(m.chat.id, 'Your language now is english🇺🇸\nYou can press down button to set persian language🇮🇷', reply_markup=markupaven)
    else:
        bot.send_message(m.chat.id, "زبان خود را انتخاب کنید👇\nSelect your language👇", reply_markup=markupstart)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "farsi":
          redis.hset("lang:{}".format(call.message.chat.id),"farsi",True)
          redis.hdel("lang:{}".format(call.message.chat.id),"english")
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="زبان شما با موفقیت به فارسی انتخاب شد\n\nلطفا یکدام از دکمه های زیر را انتخاب کنید👇", reply_markup=markupstartfa)
          bot.answer_callback_query(callback_query_id=call.id,text="خوش آمدید😊")
    if call.message:
        if call.data == "english":
          redis.hset("lang:{}".format(call.message.chat.id),"english",True)
          redis.hdel("lang:{}".format(call.message.chat.id),"farsi")
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Your language selected to english🇺🇸\nPlease select one of the button👇", reply_markup=markupstarten)
          bot.answer_callback_query(callback_query_id=call.id,text="Wellcome😊")
    if call.message:
        if call.data == "joke":
          f = open("joke.db")
          text = f.read()
          text1 = text.split(",")
          last = random.choice(text1)
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="{}".format(last), reply_markup=markupjoke, parse_mode="Markdown")
    if call.message:
        if call.data == "chuk":
          url = "http://tambal.azurewebsites.net/joke/random"
          res = urllib.urlopen(url)
          parsed_json = json.loads(res.read())
          joke = parsed_json['joke']
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="{}".format(joke), reply_markup=markupchuk, parse_mode="Markdown")
    if call.message:
        if call.data == "avazfa":
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="زبان خود را انتخاب کنید 👇\nSelect your language👇", reply_markup=markupstart)
    if call.message:
        if call.data == "avazen":
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Select your language👇\nزبان خود را انتخاب کنید 👇", reply_markup=markupstart)
    if call.message:
        if call.data == "getjoke":
          f = open("joke.db")
          text = f.read()
          text1 = text.split(",")
          last = random.choice(text1)
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="{}".format(last), reply_markup=markupjoke, parse_mode="Markdown")
    if call.message:
        if call.data == "sendjoke":
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="برای ارسال جک یا انتقاد یا پیشنهاد به ما طبق دستورالعمل زیر عمل کنید👇\n/send متن", reply_markup=markupback)
    if call.message:
        if call.data == "getjokeen":
          url = "http://tambal.azurewebsites.net/joke/random"
          res = urllib.urlopen(url)
          parsed_json = json.loads(res.read())
          joke = parsed_json['joke']
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="{}".format(joke), reply_markup=markupchuk, parse_mode="Markdown")
    if call.message:
        if call.data == "sendjokeen":
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="For send us rate or joke please send👇\n/Send Text", reply_markup=markupbacken)
    if call.message:
        if call.data == "back":
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="به عقب برگشتید🔙\n\nلطفا یکدام از دکمه های زیر را انتخاب کنید👇", reply_markup=markupstartfa)
    if call.message:
        if call.data == "backen":
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Come backed🔙\nPlease select one of the button👇", reply_markup=markupstarten)
 #   if call.message:
 #       if call.data == "timefa":
 #          url = req.get('http://api.gpmod.ir/time/')
 #          data = url.json()
 #          ENdate = data['ENdate']
 #          ENtime = data['ENtime']
 #         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="{} \n {}".format(ENtime.ENdate), reply_markup=markupback)
 #   if call.message:
 #       if call.data == "timeen":
 #          url = req.get('http://api.gpmod.ir/time/')
 #          data = url.json()
 #          ENdate = data['ENdate']
 #          ENtime = data['ENtime']
 #         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="{} \n {}".format(ENtime.ENdate), reply_markup=markupbacken)

#################################################################################################################################################################################################
#################################################################################################################################################################################################
#################################################################################################################################################################################################

@bot.inline_handler(lambda q: q.query)
def inline(query):
    if query.query.split()[0] == 'markdown':
        text = query.query.replace('markdown','')
        markdown1 = types.InlineQueryResultArticle('1','Bold', types.InputTextMessageContent('*{}*'.format(text), parse_mode='Markdown'))
        markdown2 = types.InlineQueryResultArticle('2','Italic', types.InputTextMessageContent('_{}_'.format(text), parse_mode='Markdown'))
        markdown3 = types.InlineQueryResultArticle('3','Code', types.InputTextMessageContent('`{}`'.format(text), parse_mode='Markdown'))
        bot.answer_inline_query(query.id, [markdown1, markdown2, markdown3], cache_time="1")

    if query.query.split()[0] == 'nagaeedam':
     try:
       nagaeedam = query.query.replace('nagaeedam','')
       text = urllib.urlencode({u'txtclr': u'000000', u'txt': nagaeedam + u" نـگاییـدم", u'txtfit': u'max', u'txtsize' : u'200', u'txtfont' : u'PT Serif,Bold'})
       text2 = text.replace(u"+",u"%20")
       link = u"http://copierteam.imgix.net/e642-t.png?{}".format(text2)
       urllib.urlretrieve(link, "naga.png")
       filee = open("naga.png","rb")
       mess = bot.send_sticker(242361127,filee)
       sticker = mess.sticker.file_id
       r = types.InlineQueryResultCachedSticker('1', sticker)
       r1 = types.InlineQueryResultArticle('2', u'Introduce Me To Your Friends!', types.InputTextMessageContent(u"روبات تست!\n@TeleUR_robot\nاستارت کن و از کارایی هاش لذت ببر!"))
       bot.answer_inline_query(query.id,[r,r1], switch_pm_text='Start bot')
     except IndexError:
       err_tmp = 'https://storage.pwrtelegram.xyz/TeleUR_robot/photo/file_38.jpg'
       err = types.InlineQueryResultArticle('1', 'Error', types.InputTextMessageContent('*Error 404 Not Found!*', parse_mode='Markdown'),thumb_url=err_tmp)
       bot.answer_inline_query(query.id, [err],cache_time="1")

    if query.query.split()[0] == 'music':
     try:
        oo = query.query
        input = oo.replace("music ","")
        t5 = input.replace(" ","%20")
        eeqq = urllib.quote(input)
        req = urllib2.Request("http://api.gpmod.ir/music.search/?v=2&q={}&count=30".format(eeqq))
        opener = urllib2.build_opener()
        f = opener.open(req)
        parsed_json = json.loads(f.read())
        yy1 = random.randrange(10)
        yy2 = random.randrange(10)
        yy3 = random.randrange(10)
        yy4 = random.randrange(10)
        yy5 = random.randrange(10)
        rrrr1 = parsed_json['response'][yy1]['link']
        rrrr2 = parsed_json['response'][yy2]['link']
        rrrr3 = parsed_json['response'][yy3]['link']
        rrrr4 = parsed_json['response'][yy4]['link']
        rrrr5 = parsed_json['response'][yy5]['link']
        rrrr01 = parsed_json['response'][yy1]['title']
        rrrr11 = parsed_json['response'][yy2]['title']
        rrrr21 = parsed_json['response'][yy3]['title']
        rrrr41 = parsed_json['response'][yy4]['title']
        rrrr51 = parsed_json['response'][yy5]['title']
        pic = types.InlineQueryResultAudio('1', rrrr1 ,'{}'.format(rrrr01))
        pic1 = types.InlineQueryResultAudio('2', rrrr2 ,'{}'.format(rrrr11))
        pic2 = types.InlineQueryResultAudio('3', rrrr3 ,'{}'.format(rrrr21))
        pic3 = types.InlineQueryResultAudio('4', rrrr4 ,'{}'.format(rrrr41))
        pic4 = types.InlineQueryResultAudio('5', rrrr5 ,'{}'.format(rrrr51))
        bot.answer_inline_query(query.id, [pic,pic1,pic2,pic3,pic4], cache_time="15")
     except IndexError:
        error_tmp = 'https://storage.pwrtelegram.xyz/TeleUR_robot/photo/file_38.jpg'
        error = types.InlineQueryResultArticle('1', 'Error', types.InputTextMessageContent('*Error 404 Not Found!*', parse_mode='Markdown'),thumb_url=error_tmp)
        bot.answer_inline_query(query.id, [error],cache_time="1")

#################################################################################################################################################################################################

@bot.inline_handler(lambda query: len(query.query) is 0)
def query_text(query):
    user = query.from_user.username
    name = query.from_user.first_name
    lname = query.from_user.last_name
    uid = query.from_user.id
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('{}'.format(name), url="https://telegram.me/{}".format(user)))
    thumb_url = 'http://www.hopsten.de/assets/images/iNFO_LOGO.jpg'
    info = types.InlineQueryResultArticle('1','Your Info ',types.InputTextMessageContent('*Username : @{}\nYour First Name : {}\nYour Last Name : {}\nYour ID :  {}*'.format(user,name,lname,uid), parse_mode="Markdown"),reply_markup=markup,thumb_url=thumb_url)
    
    tumsss = 'http://images.clipartpanda.com/contact-clipart-contact-phone-md.png'
    random_text = random.randint(1, 1000)
    tmpp = 'http://static.nautil.us/3006_5f268dfb0fbef44de0f668a022707b86.jpg'
    randowm = types.InlineQueryResultArticle('2', 'Random Number',types.InputTextMessageContent('Random Number : {}'.format(random_text)), thumb_url=tmpp)

    req = urllib2.Request("http://umbrella.shayan-soft.ir/txt/joke.db")
    opener = urllib2.build_opener()
    f = opener.open(req)
    text = f.read()
    text1 = text.split(",")
    last = random.choice(text1)
    joke = types.InlineQueryResultArticle('3', 'Joke', types.InputTextMessageContent(last.replace('@UmbrellaTeam',"")),thumb_url='http://up.persianscript.ir/uploadsmedia/5b63-download-2-.png')


    reqa = urllib2.Request('http://api.gpmod.ir/time/')
    openera = urllib2.build_opener()
    fa = openera.open(reqa)
    parsed_jsona = json.loads(fa.read())
    ENtime = parsed_jsona['ENtime']
    FAtime = parsed_jsona['FAtime']
    ENdate = parsed_jsona['ENdate']
    FAdate = parsed_jsona['FAdate']
    time_tmp = 'http://a4.mzstatic.com/us/r30/Purple49/v4/c4/bf/0b/c4bf0bbe-f71c-12be-6017-818ab2594c98/icon128-2x.png'
    timesend = types.InlineQueryResultArticle('4', 'Time', types.InputTextMessageContent('`{}` : *ساعت* `{}` \n\n `{}` *Time* : `{}`'.format(FAdate,FAtime,ENdate,ENtime), parse_mode='Markdown'), thumb_url=time_tmp)


    req = urllib2.Request("http://umbrella.shayan-soft.ir/txt/danestani.db")
    opener = urllib2.build_opener()
    f = opener.open(req)
    text = f.read()
    text1 = text.split(",")
    last = random.choice(text1)
    logo = 'https://d2vvqscadf4c1f.cloudfront.net/R1H3Ms7QSQOwRpTbUImd_science.jpg'
    since = types.InlineQueryResultArticle('5', 'Danestani', types.InputTextMessageContent(last.replace('@UmbrellaTeam',"")),thumb_url=logo)

    url = urllib2.Request('http://exchange.nalbandan.com/api.php?action=json')
    openerb = urllib2.build_opener()
    fb = openera.open(url)
    parsed_jsonb = json.loads(fb.read())
    date = parsed_jsonb['dollar']['date']
    dollar = parsed_jsonb['dollar']['persian']
    dollar1 = parsed_jsonb['dollar']['value']
    dollar_rasmi = parsed_jsonb['dollar_rasmi']['persian']
    dollar_rasmi1 = parsed_jsonb['dollar_rasmi']['value']
    euro = parsed_jsonb['euro']['persian']
    euro1 = parsed_jsonb['euro']['value']
    gold_per_geram = parsed_jsonb['gold_per_geram']['persian']
    gold_per_geram1 = parsed_jsonb['gold_per_geram']['value']
    coin_new = parsed_jsonb['coin_new']['persian']
    coin_new1 = parsed_jsonb['coin_new']['value']
    pond = parsed_jsonb['pond']['persian']
    pond1 = parsed_jsonb['pond']['value']
    derham = parsed_jsonb['coin_old']['persian']
    derham1 = parsed_jsonb['coin_old']['value']
    coin_old = parsed_jsonb['coin_old']['persian']
    coin_old1 = parsed_jsonb['coin_old']['value']
    time_tmp = 'http://uupload.ir/files/66yl_download_(2).png'
    dollar = types.InlineQueryResultArticle('6', 'Dollar', types.InputTextMessageContent("قیمت ارز رایج کشور در تاریخ : ``` {}``` \n به شرح زیر است : \n\n `{}` به قیمت *{}* تومن \n\n `{}` به قیمت *{}* تومن \n\n `{}` به قیمت *{}* تومن  \n\n `{}` به قیمت *{}* تومن  \n\n `{}` به قیمت *{}* تومن  \n\n `{}` به قیمت *{}* تومن  \n\n `{}` به قیمت *{}* تومن  \n\n `{}` به قیمت *{}* تومن  ".format(date,dollar,dollar1,dollar_rasmi,dollar_rasmi1,euro,euro1,gold_per_geram,gold_per_geram1,coin_new,coin_new1,pond,pond1,derham,derham1,coin_old,coin_old1), parse_mode='Markdown'), thumb_url=time_tmp)    

    hi_tmp = 'https://d85wutc1n854v.cloudfront.net/live/products/600x375/WB0PGGM81.png?v=1.0'
    hi = types.InlineQueryResultArticle('7', 'Music', types.InputTextMessageContent('*@TeleUR_robot music [Music name]*', parse_mode='Markdown'), thumb_url=hi_tmp)

    url1 = urllib2.Request('http://api.khabarfarsi.net/api/news/latest/1?tid=*&output=json')
    openerc = urllib2.build_opener()
    fc = openerc.open(url1)
    parsed_jsonc = json.loads(fc.read())
    title = parsed_jsonc['items'][0]['title']
    link = parsed_jsonc['items'][0]['link']
    title2 = parsed_jsonc['items'][1]['title']
    link2 = parsed_jsonc['items'][1]['link']
    title3 = parsed_jsonc['items'][2]['title']
    link3 = parsed_jsonc['items'][2]['link']
    markup = types.InlineKeyboardMarkup()
    li1 = types.InlineKeyboardButton('Link 1.',url=link)
    li2 = types.InlineKeyboardButton('Link 2.',url=link2)
    li3 = types.InlineKeyboardButton('Link 3.',url=link3)
    markup.add(li1)
    markup.add(li2)
    markup.add(li3)
    news_tmp = 'http://seattlefreepress.org/wp-content/uploads/2015/11/In-the-news-icon.png'
    news = types.InlineQueryResultArticle('8', 'News', types.InputTextMessageContent('1. :'+title+'\n\n2. :'+title2+'\n\n3. :'+title3), reply_markup=markup, thumb_url=news_tmp)

    mark_tmp = 'https://storage.pwrtelegram.xyz/TeleUR_robot/photo/file_555.jpg'
    markdown = types.InlineQueryResultArticle('9', 'Markdown', types.InputTextMessageContent('*@TeleUR_robot markdown [Your Text]*', parse_mode='Markdown'), thumb_url=mark_tmp)

    naga_tmp = 'http://s6.uplod.ir/i/00837/hhny23vekf7d.jpg'
    nagaeedam = types.InlineQueryResultArticle('10', 'Nagaeedam', types.InputTextMessageContent('*@TeleUR_robot nagaeedam [Your Text]*', parse_mode='Markdown'), thumb_url=naga_tmp)

    bot.answer_inline_query(query.id, [info, dollar, randowm, joke, since, timesend, news, hi, markdown, nagaeedam], cache_time=5, switch_pm_text='Start bot')

#################################################################################################################################################################################################

bot.polling(True)
