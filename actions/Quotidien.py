#######################################################################################
#                                                                                     #
#                                  Classe Quotidien                                   #
#                                                                                     #
#######################################################################################
import interactions, threading, asyncio, arrow
from shared.Data import Data
import nest_asyncio

class Quotidien():

    Channel = ""
    NextExecution = ""

    async def Podium(ctx):
        guild = ctx.guild
        channel = ""
        for g in guild:
            if g.id == Quotidien.get_GuildChannel()[0]:
                for c in await g.get_all_channels():
                    if c.id == Quotidien.get_GuildChannel()[1]:
                        channel = c    
        if(channel == ""):
            print("Erreur, pas de channel")
            exit()
        Quotidien.start_quotidien(channel)

    async def start_quotidien(channel):    
        quot = threading.Thread(target=Quotidien.between_callback,args=(channel,))
        quot.start()
        Quotidien.Channel = channel

    def between_callback(bot):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(Quotidien.lancement())
        loop.close()



    async def lancement():
            nest_asyncio.apply()

            loop = asyncio.new_event_loop()
            loop.create_task(Quotidien.wait_until())
            try:
                loop.run_forever()
            finally:
                loop.run_until_complete(loop.shutdown_asyncgens())
                loop.close()

    async def wait_until():
        print("Lancement du thread quotidien.")
        while True:            
            #définit la date à demain minuit
            #Quotidien.NextExecution = arrow.utcnow().to('Europe/Paris').shift(days=1).replace(hour=0, minute=0, second=0)
            Quotidien.NextExecution = arrow.utcnow().to('Europe/Paris').shift(seconds=10)
            diff = Quotidien.NextExecution - arrow.utcnow().to('Europe/Paris')
            print(diff)
            await asyncio.sleep(diff.total_seconds())
            await Quotidien.afficher_resume()
            print('echo')
    
    async def afficher_resume():
        titre = "🏆 Chieur Of The Day 💩"
        Chieur = Quotidien.getChieurOfTheDay()

        if(len(Chieur) > 0):
            
            if(len(Chieur) > 1):
                content = "Il y a égalité !\n Les chieurs du jour sont :"
            else:
                content = "Le chieur du jour est :"
            
            for c in Chieur:
                content += f'\n🥇 {c[0]}'

            content += "\navec "+str(Chieur[0][1])+" KK aujourd'hui !"

            embed = interactions.Embed(color=10632204,title=titre, description=content)

            footer = 'CacaCorp'
            embed.set_footer(text=footer)

            print(Quotidien.channel)

            await Quotidien.channel.send("test")
            #await channel.send(embeds=embed)

        else:
            text = "🚫 Personne n'a chié aujourd'hui. 🚫"
            await Quotidien.channel.send(content=text)


#######################################################################################
#                     Fonction de récupération des données                            #
#######################################################################################

    def getChieurOfTheDay():
        return Data.getChieurOfTheDay()           
    
    def get_GuildChannel():
        return Data.get_GuildChannel()
      
def setup(client):
    Quotidien(client)



