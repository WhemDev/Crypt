import os
import shutil
import time
import random
import matplotlib.style
import discord.ext
import discord
import json
import requests
from discord import app_commands
from model import *
from environments import *
from matplotlib.pyplot import figure
from discord.ext import commands
from rich import print
from binance.client import Client
from binance.spot import Spot
import sys
import pandas as pd
import plotly.graph_objects as go
from IPython.display import display
import plotly as plt
import kaleido
import plotly.io as pio
import plotly.express as px
import datetime as dt
import requests
import pandas as pd
from time import sleep
import matplotlib as mpl
import discord.http
import matplotlib.pyplot as plt
from matplotlib import pyplot as pltt
import matplotlib.dates as mdates
from matplotlib.animation import FuncAnimation
from time import *  # To reproduce the error
import typing  # For typehinting
import numpy
import functools

if not os.path.exists("images"):
    os.mkdir("images")

base_url = "https://api.binance.com"
key = "https://api.binance.com/api/v3/ticker/price?symbol="

spot_client = Spot(base_url=base_url)


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await Bot.sync()
            self.synced = True
        print(f"We have logged in as {self.user}.")


client = aclient()
Bot = app_commands.CommandTree(client)


def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
    # return string
    return str1


def removeZeros(input):
    # print(input)
    STRprice = str(input)
    arr = list(STRprice)
    # print(arr)
    for i in range(len(arr)):
        if arr[-1] == '0':
            arr.pop()
        elif arr[-1] == '.':
            arr.pop()
    # print(arr)
    return listToString(arr)

    #   ETH     1h           24


def createGraph(typee: str, timee: str, lmt: int, w, ww, fw, fww, dat: str, fs=15):
    btcusd_history = spot_client.klines(str(typee), str(timee), limit=int(lmt))
    display(btcusd_history[:2])

    # show as DataFrame
    columns = ['time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades',
               'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore']
    history_df = pd.DataFrame(btcusd_history, columns=columns)
    # isitgonnawork = history_df.pivot(index="time", columns=columns, values=btcusd_history)
    # isitgonnawork.head()
    history_df['time'] = pd.to_datetime(history_df['time'], unit='ms')
    # index = history_df['time']
    history_df.groupby(history_df['time'].dt.hour)
    history_df.set_index('time', inplace=True)
    display(history_df)
    # print(history_df["time"])
    # print(type(history_df["time"])) #<class 'pandas.core.series.Series'>
    mpl.rcParams['grid.color'] = 'k'
    mpl.rcParams['grid.linestyle'] = ':'
    mpl.rcParams['grid.linewidth'] = 0.5
    mpl.rcParams['font.size'] = fs
    f = plt.figure()
    f.set_figwidth(fw)
    f.set_figheight(fww)

    # Temps = history_df.set_index('time')
    # print("Temps: ", Temps)
    # plt.figure()

    width = w  # .035
    width2 = ww  # .01
    # print(type(history_df))
    # print(type(history_df.close))
    up = history_df[history_df.close >= history_df.open]
    # up.set_index('time')
    # up.groupby(pd.Grouper(key='time', axis=0,
    # freq='1H')).sum()
    down = history_df[history_df.close < history_df.open]
    # down.set_index('time')
    # down.groupby(pd.Grouper(key='time', axis=0,
    # freq='1H')).sum()
    # print("INDEX AMK INDEX YETRER AMCIK EV LADI TARIK NITE 1970 GÖSTERİYON AMIN OĞLU O ZMAN ETH Mİ VARDI GÖTÜNE ETH SOKTUĞUM", up.index)
    # print(down.index)
    # print(history_df["time"])
    # print("1111111111111111111111111")
    # print(history_df["time"].index)
    # print("1111111111111111111111111111")
    # print(down)
    # print(type(down.index))
    # print(type(history_df["time"].index))
    # print("1111111111111111111122222222211")

    # print("1111111111111111111111111111")
    # print(history_df.time)
    col1 = '#27AE60'
    col2 = 'red'

    plt.rcParams["figure.figsize"] = (15, 8)
    up.close = pd.to_numeric(up.close)
    up.open = pd.to_numeric(up.open)
    up.high = pd.to_numeric(up.high)
    up.low = pd.to_numeric(up.low)
    down.close = pd.to_numeric(down.close)
    down.open = pd.to_numeric(down.open)
    down.high = pd.to_numeric(down.high)
    down.low = pd.to_numeric(down.low)

    # volum.volume = pd.to_numeric(volum.volume)

    # <class 'pandas.core.series.Series'>
    # print("--------------")
    # print(up.close)
    # ax = plt.axes()
    fig, ax = plt.subplots()
    ax2 = ax.twinx()
    history_df['SMA7'] = history_df['close'].rolling(7).mean()
    ax.plot(history_df.index, history_df['SMA7'], color='orange', label='SMA7')
    history_df['SMA25'] = history_df['close'].rolling(25).mean()
    ax.plot(history_df.index, history_df['SMA25'], color='purple', label='SMA25')
    history_df['SMA99'] = history_df['close'].rolling(99).mean()
    ax.plot(history_df.index, history_df['SMA99'], color='blue', label='SMA99')

    # ax2.plot(volum.index, volum.volume, color='blue', label='Volume')
    # print("*******************")
    # print(history_df['volume'])
    # print("*******************")
    sma99 = history_df.iloc[-1]['SMA99']
    sma25 = history_df.iloc[-1]['SMA25']
    sma7 = history_df.iloc[-1]['SMA7']
    # change = ((float(history_df.iloc[0]['close']) - float(history_df.iloc[-1]['close']) ) / (float(history_df.iloc[-1]['close']) ) * 100
    print("CLOSE 0: ", history_df.iloc[0]['close'])
    print("CLOSE -1: ", history_df.iloc[-1]['close'])
    chance = 100 * ((float(history_df.iloc[-1]['close']) - float(history_df.iloc[0]['close'])) / float(
        history_df.iloc[-1]['close']))
    print("CHANGE: ", int(chance))
    maxPrice = history_df['close'].max()
    minPrice = history_df['close'].min()
    # plot up prices
    plt.bar(up.index, up.close - up.open, width, bottom=up.open, color=col1)
    plt.bar(up.index, up.high - up.close, width2, bottom=up.close, color=col1)
    plt.bar(up.index, up.low - up.open, width2, bottom=up.open, color=col1)

    # plot down prices
    plt.bar(down.index, down.close - down.open, width, bottom=down.open, color=col2)
    plt.bar(down.index, down.high - down.open, width2, bottom=down.open, color=col2)
    plt.bar(down.index, down.low - down.close, width2, bottom=down.close, color=col2)

    # bottom_plt = plt.subplot2grid((5, 4), (3, 0), rowspan=1, colspan=4)
    # bottom_plt.bar(history_df.index, history_df['volume'])
    # plt.axis.Axis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    # plt.bar(history_df.index, history_df['time'], width=25, align='center')

    # rotate x-axis tick labels
    # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    # plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
    # plt.gcf().autofmt_xdate()
    plt.xlabel('Time')
    ax.set_ylabel('Price as USDT')
    ax2.set_ylabel('Volume')
    plt.xticks(rotation=45, ha='right')
    plt.title(f'{typee} Graph for {dat}')

    # display candlestick chart
    # plt.show()
    return plt, sma7, sma25, sma99, maxPrice, minPrice, chance

    """
    # plot results
    fig = go.Figure(data=[go.Candlestick(x=history_df['time'],
                                         open=history_df['open'],
                                         high=history_df['high'],
                                         low=history_df['low'],
                                         close=history_df['close'])])
    fig.update_layout(title = f'{typee} Price Graph',
               yaxis_title = f'{typee} Price USD ($)',
               xaxis_title = 'Date',
               xaxis_rangeslider_visible = False)
    return fig
    """


def graphPng(figu, name: str):
    # print("converting to png")
    figu.savefig(fr'images\{name}', dpi=100)
    # figure.savefig(f"{name}.jpg")       #1017509524317425694
    # print("done")
    return True
    # figure.show()
    # img_bytes = figure.to_image(format="png")          #https://towardsdatascience.com/the-simplest-way-to-create-an-interactive-candlestick-chart-in-python-ee9c1cde50d8


# region All

# region Week

@Bot.command(name="week", description="Weekly price of a Cyrpto Currency USAGE: /week BTC 1/2 or /week btc 1/2")
async def weekly(interaction: discord.Interaction, coin: str, howmany: int) -> None:
    print(howmany)
    if howmany > 2 or howmany < 1:
        embed = discord.Embed(title="Error!",
                              description="For now you can only get 1 and 2 weeks of data. For more, use **/month** or **/year**.")
        await interaction.response.send_message(embed=embed)
    else:
        messageID = interaction.id
        url = key + coin.upper() + "USDT"
        data = requests.get(url)
        data = data.json()
        name = coin.upper() + "USDT"
        defaul = 1 * howmany
        a = .038
        b = 0.007
        if howmany == 2:
            a = .048
            b = 0.014
        result = createGraph(name, f"{defaul}h", 168, a, b, 16, 10, 'WEEKLY')
        sma7 = result[1]
        sma25 = result[2]
        sma99 = result[3]
        maxP = result[4]
        minP = result[5]
        chance = result[6]
        embed_edited = discord.Embed(title=f"{howmany} WEEKS OF {coin.upper()}|USDT GRAPH",
                                     url=f"https://www.binance.com/en/trade/{coin.upper()}_USDT",
                                     description=f"**CHANCE:   {int(chance)}%**\n \n**SMA7**, Orange Line = **{removeZeros(float(sma7))} USDT**\n**SMA25**, Purple Line = **{removeZeros(float(sma25))} USDT**\n**SMA99**, Blue Line = **{removeZeros(float(sma99))} USDT**\n \nMax Price: **{removeZeros(maxP)} USDT**\nMin Price: **{removeZeros(minP)} USDT**\nCurrent Price: **{removeZeros(data['price'])} USDT**",
                                     colour=discord.Color.blue())

        # plt = createGraph(name, "1h", 168, .035, .01)
        plt = result[0]
        print(messageID)

        if graphPng(plt, str(messageID)):
            print("success")
            file = discord.File(rf"c:\Users\ardag\Desktop\notnotnotntoBOT\images\{messageID}.png")
            embed_edited.set_image(url=f"attachment://{messageID}.png")
            await interaction.response.send_message(file=file, embed=embed_edited)
            shutil.rmtree(rf"c:\Users\ardag\Desktop\notnotnotntoBOT\images")


# endregion

# region Month

@Bot.command(name="month", description="Monthly price of a Cyrpto Currency USAGE: /month BTC 1/3/6 or /month btc 1/3/6")
async def month(interaction: discord.Interaction, coin: str, howmany: int) -> None:
    if howmany == 1 or 3 or 6:
        messageID = interaction.id
        url = key + coin.upper() + "USDT"
        data = requests.get(url)
        data = data.json()
        name = coin.upper() + "USDT"
        default = 4 * howmany
        a = .12
        b = 0.035
        if howmany == 3:
            a = .26
            b = 0.045
            result = createGraph(name, f"{default}h", 180, a, b, 16, 12, 'MONTHLY', 17)
        elif howmany == 1:
            result = createGraph(name, f"{default}h", 180, a, b, 16, 12, 'MONTHLY', 17)
        elif howmany == 6:
            a = .7
            b = 0.2
            result = createGraph(name, f"1d", 180, a, b, 16, 12, 'MONTHLY', 17)
        sma7 = result[1]
        sma25 = result[2]
        sma99 = result[3]
        maxP = result[4]
        minP = result[5]
        chance = result[6]
        embed_edited = discord.Embed(title=f"{howmany} MONTHS OF {coin.upper()}|USDT GRAPH",
                                     url=f"https://www.binance.com/en/trade/{coin.upper()}_USDT",
                                     description=f"**CHANCE:   {int(chance)}%**\n \n**SMA7**, Orange Line = **{removeZeros(float(sma7))} USDT**\n**SMA25**, Purple Line = **{removeZeros(float(sma25))} USDT**\n**SMA99**, Blue Line = **{removeZeros(float(sma99))} USDT**\n \nMax Price: **{removeZeros(maxP)} USDT**\nMin Price: **{removeZeros(minP)} USDT**\nCurrent Price: **{removeZeros(data['price'])} USDT**",
                                     colour=discord.Color.blue())

        plt = result[0]
        print(messageID)

        if graphPng(plt, str(messageID)):
            print("success")
            file = discord.File(rf"c:\Users\ardag\Desktop\notnotnotntoBOT\images\{messageID}.png")
            embed_edited.set_image(url=f"attachment://{messageID}.png")
            await interaction.response.send_message(file=file, embed=embed_edited)
            shutil.rmtree(rf"c:\Users\ardag\Desktop\notnotnotntoBOT\images")
            # os.remove(rf"c:\Users\ardag\Desktop\notnotnotntoBOT\{messageID}.png")
    else:
        embed = discord.Embed(title="**Error!**",
                              description="For now you can only get **1, 3 and 6 months** of data. For more (or less), use **/week** and **/year**.")
        await interaction.response.send_message(embed=embed)


# endregion

# region Year

@Bot.command(name="year", description="Yearly price of a Cyrpto Currency USAGE: /year BTC 1/3 or /year btc 1/3/")
async def year(interaction: discord.Interaction, coin: str, howmany: int) -> None:
    if howmany == 1 or 3:

        messageID = interaction.id
        url = key + coin.upper() + "USDT"
        data = requests.get(url)
        data = data.json()
        name = coin.upper() + "USDT"
        default = 1 * howmany
        a = .8
        b = 0.25
        if howmany == 3:
            a = 2.0
            b = 0.85
        result = createGraph(name, f"{default}d", 365, a, b, 24, 15, 'YEARLY', 20)
        sma7 = result[1]
        sma25 = result[2]
        sma99 = result[3]
        maxP = result[4]
        minP = result[5]
        chance = result[6]
        embed_edited = discord.Embed(title=f"{howmany} YEARS OF {coin.upper()}|USDT GRAPH",
                                     url=f"https://www.binance.com/en/trade/{coin.upper()}_USDT",
                                     description=f"**CHANCE:   {int(chance)}%**\n \n**SMA7**, Orange Line = **{removeZeros(float(sma7))} USDT**\n**SMA25**, Purple Line = **{removeZeros(float(sma25))} USDT**\n**SMA99**, Blue Line = **{removeZeros(float(sma99))} USDT**\n \nMax Price: **{removeZeros(maxP)} USDT**\nMin Price: **{removeZeros(minP)} USDT**\nCurrent Price: **{removeZeros(data['price'])} USDT**",
                                     colour=discord.Color.blue())

        plt = result[0]
        print(messageID)

        if graphPng(plt, str(messageID)):
            print("success")
            file = discord.File(rf"c:\Users\ardag\Desktop\notnotnotntoBOT\images\{messageID}.png")
            embed_edited.set_image(url=f"attachment://{messageID}.png")
            await interaction.response.send_message(file=file, embed=embed_edited)
            shutil.rmtree(rf"c:\Users\ardag\Desktop\notnotnotntoBOT\images")
            # os.remove(rf"c:\Users\ardag\Desktop\notnotnotntoBOT\{messageID}.png")
    else:
        embed = discord.Embed(title="**Error!**",
                              description="For now you can only get **1 and 3 years** of data.")
        await interaction.response.send_message(embed=embed)


# endregion

# region Price

@Bot.command(name="price", description="Get price of a Cyrpto Currency USAGE: /price BTC / btc")
async def self(interaction: discord.Interaction, coin: str) -> None:
    url = key + coin.upper() + "USDT"
    data = requests.get(url)
    data = data.json()
    print(data)
    print(data['price'])
    print(type(data['price']))
    embed1 = discord.Embed(title=f"{coin.upper()}|BUSD", url=f"https://www.binance.com/en/trade/{coin.upper()}_BUSD",
                           description="", color=discord.Color.green())
    embed1.add_field(name=f"**{removeZeros(data['price'])}**",
                     value=f"{data['symbol']} price is **{removeZeros(data['price'])}**",
                     inline=False)
    await interaction.response.send_message(embed=embed1)
    # file = discord.File(rf"c:\Users\ardag\Desktop\notnotnotntoBOT\1017925287159279637.png")
    # embed1.set_image(url=f"attachment://1017925287159279637.png")
    # await interaction.response.send_message(file=file, embed = embed1)
    # await interaction.response.send_message(f"{data['symbol']} price is **{removeZeros(data['price'])}**")


# endregion

# endregion
a = 0




@Bot.command(name="alert", description="Alerts you when a crypto coin past a price.")
async def alert(interaction: discord.Interaction, symbol: str, targetprice: float) -> None:
    user = get_user_or_false(interaction.user.id)
    if user:
        if user.alert_symbol2 is None:

            if user.alert_symbol1 is None:

                if user.alert_symbol is None:
                    user.alert_symbol = symbol
                    user.alert_price = targetprice
                    await interaction.response.send_message("done")

                elif user.alert_symbol is not None:
                    user.alert_symbol1 = symbol
                    user.alert_price1 = targetprice
            elif user.alert_symbol1 is not None:
                user.alert_symbol2 = symbol
                user.alert_price2 = targetprice
        elif user.alert_symbol2 is not None:
            await interaction.response.send_message("Alert limit is 3")

    else:
        person = Person(interaction.user.id, symbol, targetprice).save()
        await interaction.response.send_message(f"1 {person.alert_price}")

    db.commit()


# region DevCommand
@Bot.command(name="devs", description="Devs who developt this bot and web.")
async def devs(interaction: discord.Interaction) -> None:
    embed1 = discord.Embed(title=f"**Crypto Currency Bot**",
                           description="This bot was developed by,", url="https://cryptocurrencybot.com/",
                           color=discord.Color.random())
    embed1.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/877175555559129150/1018510411617800272/unknown.png")
    # embed1.set_author(name="/CCBot")
    embed1.add_field(name=f"whem#0001",
                     value=f"APIs\nGraphs",
                     inline=False)
    embed1.add_field(name=f"Ahmet Aga 225 Bench#7031",
                     value=f"Website\nAPIs",
                     inline=False)
    embed1.add_field(name=f"bora155#0001",
                     value=f"Website\nGraphs",
                     inline=False)
    await interaction.response.send_message(embed=embed1)


# endregion


client.run('MTAxNzA1NzEyNzUwNTg3MDkzOQ.GSuQ9G.T2PTDPaLmkT8erc141E5zqxO9mFIZEiF95Ercw')