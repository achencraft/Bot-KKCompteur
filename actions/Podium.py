#######################################################################################
#                                                                                     #
#                                   Classe Podium                                     #
#                                                                                     #
#######################################################################################
import interactions, copy
from shared.Data import Data

class Podium():

    nbr_classement_per_page = 2
    buttons = []
    buttons.append(
        interactions.Button(
        style=interactions.ButtonStyle.PRIMARY,
        label="Première page",
        custom_id="Podium_First_Page",
        )
    )
    buttons.append(
        interactions.Button(
        style=interactions.ButtonStyle.PRIMARY,
        label="Page précédente",
        custom_id="Podium_Prev_Page",
        )
    )
    buttons.append(
        interactions.Button(
        style=interactions.ButtonStyle.PRIMARY,
        label="Page suivante",
        custom_id="Podium_Next_Page",
        )
    )
    buttons.append(
        interactions.Button(
        style=interactions.ButtonStyle.PRIMARY,
        label="Dernière Page",
        custom_id="Podium_Last_Page",
        )
    )



    async def Podium(ctx,userid):
        titre = "🏆 Classement des chieurs "+Data.get_annee()+" 💩"
        Classements = Podium.getPodium(userid)

        if(len(Classements) > 0):
            
            nbr_page = len(Classements)//Podium.nbr_classement_per_page
            if(len(Classements)%Podium.nbr_classement_per_page > 0):
                nbr_page = nbr_page+1
          
            if(nbr_page > 1):
                titre = titre + f" - page 1/{nbr_page}"

            content = ""
            classement_to_show = [s for  s in Classements[:Podium.nbr_classement_per_page]]

            compteur = 0
            emojis = ["🥇","🥈","🥉","🚾"]
            for classement in classement_to_show:
                content += f'\n'
                if(compteur < 3):
                    content += emojis[compteur]
                else:
                    content += emojis[3]


                if(classement.discord == userid):
                    content += f'**{classement.username} --- {str(len(classement.kk))}**'
                else:
                    content += f'{classement.username} --- {str(len(classement.kk))}'
                compteur += 1


            embed = interactions.Embed(color=10632204,title=titre, description=content)

            footer = 'CacaCorp:1'
            embed.set_footer(text=footer)

            boutons = copy.deepcopy(Podium.buttons)
            if nbr_page == 1:
                boutons = []
            else:
                boutons[0].disabled = True
                boutons[1].disabled = True

            await ctx.send(embeds=embed, components=boutons, ephemeral=True)

        else:
            text = "🚫 Personne n'a chié cette année. 🚫"
            await ctx.send(content=text, ephemeral=True)


#######################################################################################
#                     Fonction de récupération des données                            #
#######################################################################################

    def getPodium(userid):
        return Data.getPodium(userid)           
        

#######################################################################################
#                              Changement de page                                     #
#######################################################################################

    async def change_page(ctx, mode):

        data = ctx.message.embeds[0]
        boutons = copy.deepcopy(Podium.buttons)
        footer = data.footer.text
        page_actuelle =  int(footer.split(':')[1])


        Classements = Podium.getPodium(str(ctx.user.id))

        nbr_page = len(Classements)//Podium.nbr_classement_per_page
        if(len(Classements)%Podium.nbr_classement_per_page > 0):
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


        debut = (nouvelle_page - 1)*Podium.nbr_classement_per_page
        fin = debut + Podium.nbr_classement_per_page

        titre = "🏆 Classement des chieurs "+Data.get_annee()+" 💩"
        titre = titre + f" - page {nouvelle_page}/{nbr_page}"

        content = ""
        classement_to_show = [s for  s in Classements[debut:fin]]
        
        compteur = debut
        emojis = ["🥇","🥈","🥉","🚾"]
        for classement in classement_to_show:
            content += f'\n'
            if(compteur < 3):
                content += emojis[compteur]
            else:
                content += emojis[3]


            if(classement.discord == str(ctx.user.id)):
                content += f'**{classement.username} --- {str(len(classement.kk))}**'
            else:
                content += f'{classement.username} --- {str(len(classement.kk))}'
            compteur += 1


        embed = interactions.Embed(title=titre, description=content)

        footer = 'CacaCorp'
        footer = footer + f':{nouvelle_page}'

        embed.set_footer(text=footer)
        await ctx.edit(embeds=embed, components=boutons)
             





def setup(client):
    Podium(client)



