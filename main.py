import discord
import os
import random
from keepalive import keep_alive

client = discord.Client()



channel_list = []

lastmsg = []

ends = ['.', ',', '?', '!', '\n']

goodbot = ["Thank you peko!", "I know peko!", "Arigato peko!", "Thanks, you to peko!", "Even better than my older sister peko?"]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event


async def on_message(message):
  #recursion defense
  if message.author == client.user:
    return


  #Pain peko feture
  if message.content==('pain'):
    await message.channel.send('pain peko.')


  #main pekofy feature
  if message.content==('!pekofy'):
    if (message.channel.id in channel_list):
      location = channel_list.index(message.channel.id)
      old_text = lastmsg[location]

      stop1 = old_text.replace('.', ' peko.')
      stop2 = stop1.replace('?', ' peko?')
      stop3 = stop2.replace('!', ' peko!')
      stop4 = stop3.replace(',', ' peko,')
      new_text = stop4.replace('\n',' peko \n')
      if new_text.endswith(tuple(ends)):
        await message.channel.send(new_text)
      else:
        await message.channel.send(new_text + ' peko')


  
  #good/bad bot
  if message.content.startswith ('good bot'):
    await message.channel.send(random.choice(goodbot))


  #troubleshoot command
  #if message.content == ('check'):
  #  await message.channel.send(channel_list)
  #  await message.channel.send(lastmsg)


  #channel + last msg additions
  if (message.channel.id in channel_list):
    location = channel_list.index(message.channel.id)
    del lastmsg [location]
    lastmsg.insert(location, message.content)
    return
  channel_list.append(message.channel.id)
  lastmsg.append(message.content)


keep_alive()
client.run(os.getenv('TOKEN'))
