﻿#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
from telebot import types
from telebot import util
import re
import time
from time import sleep
import sys
import json
import os
import logging
import subprocess
import requests
import requests as req
import random
from random import randint
import base64
import urllib
from urllib import urlretrieve as dw
import urllib2
import redis
reload(sys)
sys.setdefaultencoding("utf-8")

#########################################################################################################################################################################

TOKEN = '277679081:AAGk3IXlId9PKUn3n_5wrfrUIR_mgsUVCeE'
bot = telebot.TeleBot(TOKEN)
is_sudo = '242361127'
redis = redis.StrictRedis(host='localhost', port=6379, db=0)

f = "\n \033[01;30m Bot Firstname: {} \033[0m".format(bot.get_me().first_name)
u = "\n \033[01;34m Bot Username: {} \033[0m".format(bot.get_me().username)
i = "\n \033[01;32m Bot ID: {} \033[0m".format(bot.get_me().id)
c = "\n \033[01;31m Bot Is Online Now! \033[0m"
print(f + u + i + c)
bn = "\n Bot Firstname: {} ".format(bot.get_me().first_name)
bu = "\n Bot Username: {} ".format(bot.get_me().username)
bi = "\n Bot ID: {} ".format(bot.get_me().id)
bc = "\n Bot Is Online Now!"
bot.send_message(is_sudo, 'ًں‘‹\n{} {} {} {}'.format(bn,bu,bi,bc))

#########################################################################################################################################################################

markupstart = types.InlineKeyboardMarkup()
markupstart.add(types.InlineKeyboardButton('ًں‡®ًں‡·ظپط§ط±ط³غŒًں‡®ًں‡·', callback_data='farsi'))
markupstart.add(types.InlineKeyboardButton('ًں‡؛ًں‡¸Englishًں‡؛ًں‡¸', callback_data='english'))
markupstartfa = types.InlineKeyboardMarkup()
#markupstartfa.add(types.InlineKeyboardButton()
#markupstartfa.add(types.InlineKeyboardButton()
#markupstartfa.add(types.InlineKeyboardButton()
markupstartfa.add(types.InlineKeyboardButton('ط²ظ…ط§ظ†', callback_data='timefa'))
markupstartfa.add(types.InlineKeyboardButton('ط±ظپطھظ† ط¨ظ‡ ط­ط§ظ„طھ ط§غŒظ†ظ„ط§غŒظ†', switch_inline_query=''))
markupstarten = types.InlineKeyboardMarkup()
#markupstarten.add(types.InlineKeyboardButton()
#markupstarten.add(types.InlineKeyboardButton()
#markupstarten.add(types.InlineKeyboardButton()
markupstarten.add(types.InlineKeyboardButton('date', callback_data='timeen'))
markupstarten.add(types.InlineKeyboardButton('Inline mode', switch_inline_query=''))
markupback = types.InlineKeyboardMarkup()
markupback.add(types.InlineKeyboardButton('ًں”™ط¨ط±ع¯ط´طھ', callback_data='backfa'))
markupbacken = types.InlineKeyboardMarkup()
markupbacken.add(types.InlineKeyboardButton('ًں”™Back', callback_data='backen'))
markupreload = types.InlineKeyboardMarkup()
markupreload.add(types.InlineKeyboardButton('ًں”ƒreload', callback_data='reload'))
markupredatefa = types.InlineKeyboardMarkup()
markupredatefa.add(types.InlineKeyboardButton('ط¨ط±ظˆط² ع©ط±ط¯ظ†', callback_data='refa'))
markupredateen = types.InlineKeyboardMarkup()
markupredateen.add(types.InlineKeyboardButton('refersh', callback_data='reen'))

@bot.message_handler(commands=['start'])
def start(message):
    id = message.chat.id
    redis.sadd('startmebot',id)
    if redis.hget("lang:{}".format(message.chat.id),"farsi"):
        bot.send_message(message.chat.id, '*Hi*_\nWelcome To TestBot_*\nPlease Select Your Language*\n`\nط³ظ„ط§ظ…\nط¨ظ‡ ط±ظˆط¨ط§طھ طھط³طھ ط®ظˆط´ ط¢ظ…ط¯غŒط¯\nظ„ط·ظپط§ ط²ط¨ط§ظ† ط®ظˆط¯ ط±ط§ ط§ظ†طھط®ط§ط¨ ع©ظ†غŒط¯`', parse_mode='markdown', reply_markup=markupstart)
    elif redis.hget("lang:{}".format(message.chat.id),"english"):
        bot.send_message(message.chat.id, '*Hi*_\nWelcome To TestBot_*\nPlease Select Your Language*\n`\nط³ظ„ط§ظ…\nط¨ظ‡ ط±ظˆط¨ط§طھ طھط³طھ ط®ظˆط´ ط¢ظ…ط¯غŒط¯\nظ„ط·ظپط§ ط²ط¨ط§ظ† ط®ظˆط¯ ط±ط§ ط§ظ†طھط®ط§ط¨ ع©ظ†غŒط¯`', parse_mode='markdown', reply_markup=markupstart)
    else:
        bot.send_message(message.chat.id, '*Hi*_\nWelcome To TestBot_*\nPlease Select Your Language*\n`\nط³ظ„ط§ظ…\nط¨ظ‡ ط±ظˆط¨ط§طھ طھط³طھ ط®ظˆط´ ط¢ظ…ط¯غŒط¯\nظ„ط·ظپط§ ط²ط¨ط§ظ† ط®ظˆط¯ ط±ط§ ط§ظ†طھط®ط§ط¨ ع©ظ†غŒط¯`', parse_mode='markdown', reply_markup=markupstart)

@bot.message_handler(commands=['reload'])
def reload(m):
    cid = m.chat.id
    bot.send_message(cid, 'reload command:', reply_markup=markupreload)
    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "farsi":
          redis.hset("lang:{}".format(call.message.chat.id),"farsi",True)
          redis.hdel("lang:{}".format(call.message.chat.id),"english")
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="ط²ط¨ط§ظ† ط´ظ…ط§ ط¨ط§ ظ…ظˆظپظ‚غŒطھ ط¨ظ‡ ظپط§ط±ط³غŒ ط§ظ†طھط®ط§ط¨ ط´ط¯\n\nظ„ط·ظپط§ غŒع©ط¯ط§ظ… ط§ط² ط¯ع©ظ…ظ‡ ظ‡ط§غŒ ط²غŒط± ط±ط§ ط§ظ†طھط®ط§ط¨ ع©ظ†غŒط¯ًں‘‡", reply_markup=markupstartfa)
          bot.answer_callback_query(callback_query_id=call.id,text="ط®ظˆط´ ط¢ظ…ط¯غŒط¯ًںکٹ")
    if call.message:
        if call.data == "english":
          redis.hset("lang:{}".format(call.message.chat.id),"english",True)
          redis.hdel("lang:{}".format(call.message.chat.id),"farsi")
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Your language selected to englishًں‡؛ًں‡¸\nPlease select one of the buttonًں‘‡", reply_markup=markupstarten)
          bot.answer_callback_query(callback_query_id=call.id,text="Wellcomeًںکٹ")
    if call.message:
        if call.data == "backfa":
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="ط¨ظ‡ ط¹ظ‚ط¨ ط¨ط±ع¯ط´طھغŒط¯ًں”™\n\nظ„ط·ظپط§ غŒع©ط¯ط§ظ… ط§ط² ط¯ع©ظ…ظ‡ ظ‡ط§غŒ ط²غŒط± ط±ط§ ط§ظ†طھط®ط§ط¨ ع©ظ†غŒط¯ًں‘‡", reply_markup=markupstartfa)
          bot.answer_callback_query(callback_query_id=call.id, text="ط¨ظ‡ ط¹ظ‚ط¨ ط¨ط±ع¯ط´طھغŒط¯ًں”™")
    if call.message:
        if call.data == "backen":
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Come backedًں”™\nPlease select one of the buttonًں‘‡", reply_markup=markupstarten)
          bot.answer_callback_query(callback_query_id=call.id, text="Come backedًں”™")
    if call.message:
        if call.data == "reload":
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="reload: [â–†____________]")
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="reload: [â–†â–†___________]")
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="reload: [â–†â–†â–†__________]")
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="reload: [â–†â–†â–†â–†_________]")
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="reload: [â–†â–†â–†â–†â–†________]")
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="reload: [â–†â–†â–†â–†â–†â–†_______]")
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="reload: [â–†â–†â–†â–†â–†â–†â–†______]")
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="reload: [â–†â–†â–†â–†â–†â–†â–†â–†_____]")
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="reload: [â–†â–†â–†â–†â–†â–†â–†â–†â–†____]")
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="reload: [â–†â–†â–†â–†â–†â–†â–†â–†â–†â–†___]")
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="reload: [â–†â–†â–†â–†â–†â–†â–†â–†â–†â–†â–†__]")
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="reload: [â–†â–†â–†â–†â–†â–†â–†â–†â–†â–†â–†â–†_]")
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="reload: [â–†â–†â–†â–†â–†â–†â–†â–†â–†â–†â–†â–†â–†]")
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="reloaded!", reply_markup=markupreload)
    if call.message:
        if call.data == "timefa":
            reqa = urllib2.Request('http://api.gpmod.ir/time/')
            openera = urllib2.build_opener()
            fa = openera.open(reqa)
            parsed_jsona = json.loads(fa.read())
            FAtime = parsed_jsona['FAtime']
            FAdate = parsed_jsona['FAdate']
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="طھط§ط±غŒط®: {} \nط³ط§ط¹طھ: {}".format(FAdate,FAtime), reply_markup=markupredatefa)
    if call.message:
        if call.data == "timeen":
           reqa = urllib2.Request('http://api.gpmod.ir/time/')
           openera = urllib2.build_opener()
           fa = openera.open(reqa)
           parsed_jsona = json.loads(fa.read())
           ENtime = parsed_jsona['ENtime']
           ENdate = parsed_jsona['ENdate']
           bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="date: {} \ntime: {}".format(ENdate,ENtime), reply_markup=markupredateen)
    if call.message:
       if call.data == "refa":
            reqa = urllib2.Request('http://api.gpmod.ir/time/')
            openera = urllib2.build_opener()
            fa = openera.open(reqa)
            parsed_jsona = json.loads(fa.read())
            FAtime = parsed_jsona['FAtime']
            FAdate = parsed_jsona['FAdate']
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="طھط§ط±غŒط®: {} \nط³ط§ط¹طھ: {}".format(FAdate,FAtime), reply_markup=markupredatefa)
    if call.message:
        if call.data == "reen":
           reqa = urllib2.Request('http://api.gpmod.ir/time/')
           openera = urllib2.build_opener()
           fa = openera.open(reqa)
           parsed_jsona = json.loads(fa.read())
           ENtime = parsed_jsona['ENtime']
           ENdate = parsed_jsona['ENdate']
           bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="date: {} \ntime: {}".format(ENdate,ENtime), reply_markup=markupredateen)

bot.polling(none_stop=True, timeout=20)
