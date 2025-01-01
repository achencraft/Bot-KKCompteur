#######################################################################################
#                                                                                     #
#                                 Classe Historique                                   #
#                                                                                     #
#######################################################################################
import interactions, copy
from shared.Data import Data

class Historique():

    nbr_classement_per_page = 15
    buttons = []
    buttons.append(
        interactions.Button(
        style=interactions.ButtonStyle.PRIMARY,
        label="Première page",
        custom_id="Histo_First_Page",
        )
    )
    buttons.append(
        interactions.Button(
        style=interactions.ButtonStyle.PRIMARY,
        label="Page précédente",
        custom_id="Histo_Prev_Page",
        )
    )
    buttons.append(
        interactions.Button(
        style=interactions.ButtonStyle.PRIMARY,
        label="Page suivante",
        custom_id="Histo_Next_Page",
        )
    )
    buttons.append(
        interactions.Button(
        style=interactions.ButtonStyle.PRIMARY,
        label="Dernière Page",
        custom_id="Histo_Last_Page",
        )
    )



    async def Historique(ctx,userid):
        titre = "⌛ Historique "+Data.get_annee()+" de mes KK 💩"
        data = Historique.getData(userid)

        if(len(data) > 0):
            
            nbr_page = len(data)//Historique.nbr_classement_per_page
            if(len(data)%Historique.nbr_classement_per_page > 0):
                nbr_page = nbr_page+1
          
            if(nbr_page > 1):
                titre = titre + f" - page 1/{nbr_page}"

            content = ""
            data_to_show = [s for  s in data[:Historique.nbr_classement_per_page]]

            
            for d in data_to_show:
                content += f'\n 💩 {d.date} {d.heure}'


            embed = interactions.Embed(color=10632204,title=titre, description=content)

            footer = 'CacaCorp:1'
            embed.set_footer(text=footer)

            boutons = copy.deepcopy(Historique.buttons)
            if nbr_page == 1:
                boutons = []
            else:
                boutons[0].disabled = True
                boutons[1].disabled = True

            await ctx.send(embeds=embed, components=boutons, ephemeral=True)

        else:
            text = "🚫 Vous n'avez pas chié cette année. 🚫"
            await ctx.send(content=text, ephemeral=True)


#######################################################################################
#                     Fonction de récupération des données                            #
#######################################################################################

    def getData(userid):
        return Data.getHisto(userid)           
        

#######################################################################################
#                              Changement de page                                     #
#######################################################################################

    async def change_page(ctx, mode):

        data = ctx.message.embeds[0]
        boutons = copy.deepcopy(Historique.buttons)
        footer = data.footer.text
        page_actuelle =  int(footer.split(':')[1])


        data = Historique.getData(str(ctx.user.id))

        nbr_page = len(data)//Historique.nbr_classement_per_page
        if(len(data)%Historique.nbr_classement_per_page > 0):
            nbr_page = nbr_page+1

        match mode:
            case "First":
                nouvelle_page = 1
            case "Prev":
                nouvelle_page = page_actuelle - 1
            case "Next":
                nouvelle_page = page_actuelle + 1
            case "Last":
                nouvelle_page = nbr_page

        if nouvelle_page == 1:
            boutons[0].disabled = True
            boutons[1].disabled = True
            boutons[2].disabled = False
            boutons[3].disabled = False
        elif nouvelle_page == nbr_page:
            boutons[0].disabled = False
            boutons[1].disabled = False
            boutons[2].disabled = True
            boutons[3].disabled = True
        else:
            boutons[0].disabled = False
            boutons[1].disabled = False
            boutons[2].disabled = False
            boutons[3].disabled = False


        debut = (nouvelle_page - 1)*Historique.nbr_classement_per_page
        fin = debut + Historique.nbr_classement_per_page

        titre = "⌛ Historique "+Data.get_annee()+" de mes KK 💩"
        titre = titre + f" - page {nouvelle_page}/{nbr_page}"

        content = ""
        data_to_show = [s for  s in data[debut:fin]]
        for d in data_to_show:
            content += f'\n 💩 {d.date} {d.heure}'

        embed = interactions.Embed(title=titre, description=content)

        footer = 'CacaCorp'
        footer = footer + f':{nouvelle_page}'

        embed.set_footer(text=footer)
        await ctx.edit(embeds=embed, components=boutons)
             





def setup(client):
    Historique(client)



