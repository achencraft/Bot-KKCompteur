#######################################################################################
#                                 KKCOMPTEUR                                          #
#                                                                                     #
#                                   Imports                                           #
#######################################################################################
from dotenv import dotenv_values
import interactions
from shared.Data import Data
import asyncio


#######################################################################################
#                                 Définitions                                         #
#######################################################################################
config = dotenv_values(".env")
TOKEN = config['BOT_TOKEN']


EXTENSIONS = [
    'extensions.caca'
    ]

async def set_activity():
    activity = interactions.PresenceActivity(name="Sur le trône",type=0)
    await bot.change_presence(interactions.ClientPresence(activities=[activity]))


#######################################################################################
#                               Initialisations                                       #
#######################################################################################
Data.Charger_chieurs(config)
bot = interactions.Client(token=TOKEN)
asyncio.run(set_activity())
quot = ""



#######################################################################################
#                          chargement des extensions                                  #
#######################################################################################
for ext in EXTENSIONS:
    bot.load(ext)


#######################################################################################
#                                     Démarrage                                       #
#######################################################################################

bot.start()

