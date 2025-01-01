#######################################################################################
#                                                                                     #
#                                   Classe Ajouter                                    #
#                                                                                     #
#######################################################################################
import datetime, interactions
from shared.Data import Data

class Ajouter():


    async def Ajouter(ctx,username, userid, date):
        nbr = Ajouter.GetCacaNumber(userid,username)
        res = True
        dt = datetime.datetime.now()

        if(date != "now"):
            format = "%d/%m/%Y %H:%M"       
            try:
                dt = datetime.datetime.strptime(date,format)
            except ValueError:
                res = False
            
        debutannee = datetime.datetime.combine(datetime.date(int(Data.get_annee()),1,1),datetime.time(0,0))

        #si date dans le futur ou avant début année en cours
        if(dt > datetime.datetime.now() or dt < debutannee):
            res = False

        titre = ctx.member.name    


        if(res):
            Ajouter.AddCaca(userid, date)
            Ajouter.Save()
            embed = interactions.Embed(color=10632204,title=titre,description="💩 Vous avez chié "+str(nbr +1)+" fois depuis le 1er janvier "+Data.get_annee()+".")

        else:
            embed = interactions.Embed(color=10632204,title=titre,description="🤮 Erreur de formatage ou de valeur de la date.\n=> jj/mm/aaaa hh:mm")        
        embed.set_footer(text="CacaCorp")
        await ctx.send(embeds=embed, ephemeral=True)


#######################################################################################
#                     Fonction de récupération des données                            #
#######################################################################################

    def GetCacaNumber(userid,username):

        if(Data.get_user(userid) == None):
            Data.add_user(userid,username)
            return 0
        else:
            return Data.get_user(userid).get_kk_number()
        
    def AddCaca(userid, date):
        if(Data.get_user(userid) != None):
            Data.get_user(userid).add_kk(date)

    def Save():
        Data.save_data()