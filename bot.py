import discord
import json
import os

from discord.ext import commands

description = 'A cool/fun bot for the CCS discord server'
help_attrs = dict(hidden=True)

#   Please never do this. lol. If it breaks the char limit in pep8 just dont...
#   Also there are better ways, but meh it works.
extensions = ["cogs." + os.path.split('cogs/{}'.format(i))[1].replace('.py','') for i in os.listdir('cogs') if i.endswith('.py') and '_' not in i]

#   The above list comprehension is basically this, but both are unoptimized and bad.
#   def get_cogs(extensions):
#    for i in os.listdir('cogs'):
#        if i.endswith('py') and '_' not in i:
#           cog = "cogs.{0.path.split('cogs/{}'.format(i))[1]}".format(os)
#            cog.replace('.py', '')
#            extensions.append(cog)
#    return extensions

bot = commands.Bot(command_prefix=commands.when_mentioned_or(), description = description, pm_help=False, help_attrs=help_attrs)

@bot.event
async def on_ready():
    print('------')
    print('Username: ' + bot.user.name)
    print('ID: ' + bot.user.id)
    
    print("\nConnected to:")
    print(str(len(bot.servers)) + " servers")
    print(str(len(set(bot.get_all_channels()))) + " channels")
    print(str(len(set(bot.get_all_members()))) + " users")
    print('------')

    for extension in extensions:
        try:
            bot.load_extension(extension)
            print('Loaded {}'.format(extension))
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))

@bot.event
async def on_command(command, ctx):
    destination = None
    
    if ctx.message.channel.is_private:
        destination = 'Private Message'
    else:
        destination = '#{0.channel.name} ({0.server.name})'.format(ctx.message)

    print('{0.timestamp}: {0.author.name} in {1}: {0.clean_content}'.format(ctx.message, destination))

def load_settings():
    with open('settings.json') as f:
        return json.load(f)

if __name__ == '__main__':
    settings = load_settings()
    bot.run(settings['token'])
    