#######################################################################################
#                                                                                     #
#                               Fonction compteur                                     #
#                                                                                     #
#######################################################################################
import interactions
from actions.Ajouter import Ajouter
from actions.Podium import Podium
from actions.Historique import Historique
from actions.Quotidien import Quotidien


class Caca(interactions.Extension):
    def __init__(self, client):
        self.client: interactions.Client = client

    @interactions.extension_command(
        name="caca",
        description="caca",
        options=[
            interactions.Option(
                name="action",
                description="action",
                type=interactions.OptionType.STRING,
                choices=[
                    interactions.Choice(name="Ajouter", value="ajouter"),
                    interactions.Choice(name="Historique", value="historique"),
                    interactions.Choice(name="Podium", value="podium")
                    #interactions.Choice(name="Quotidien", value="quotidien"),
                    ], #Ajouter par défaut
                required=False
            ),
            interactions.Option(
                name="date",
                description="jj/mm/aaaa hh:mm",
                type=interactions.OptionType.STRING,
                required=False,
                autocomplete=False
            ),
            interactions.Option(
                name="public",
                description="Réponse visible de tous",
                type=interactions.OptionType.BOOLEAN,
                required=False
            )
        ]
    )
    async def Caca(self, ctx: interactions.CommandContext, action = "ajouter" , date = "now", public = 1):

        user_id = str(ctx.user.id)
        name = ctx.user.username

        match action:
            case "ajouter":
                await Ajouter.Ajouter(ctx,name,user_id, date, public)
            case "podium":
                await Podium.Podium(ctx,user_id, public)
            case "historique":
                await Historique.Historique(ctx,user_id)
            case "quotidien":
                await Quotidien.Quotidien(ctx)
            case _:
                None
    


#######################################################################################
#                               Listeners BOUTONS                                     #
#######################################################################################


    @interactions.extension_component("Podium_First_Page")
    async def PodiumFirstPageButton(self,ctx: interactions.ComponentContext):
        await Podium.change_page(ctx, "First")
        
    
    @interactions.extension_component("Podium_Prev_Page")
    async def PodiumPrevPageButton(self,ctx: interactions.ComponentContext):
        await Podium.change_page(ctx, "Prev")

    @interactions.extension_component("Podium_Next_Page")
    async def PodiumNextPageButton(self,ctx: interactions.ComponentContext):
        await Podium.change_page(ctx, "Next")

    @interactions.extension_component("Podium_Last_Page")
    async def PodiumLastPageButton(self,ctx: interactions.ComponentContext):
        await Podium.change_page(ctx, "Last")


    @interactions.extension_component("Histo_First_Page")
    async def HistoFirstPageButton(self,ctx: interactions.ComponentContext):
        await Historique.change_page(ctx, "First")
        
    @interactions.extension_component("Histo_Prev_Page")
    async def HistoPrevPageButton(self,ctx: interactions.ComponentContext):
        await Historique.change_page(ctx, "Prev")

    @interactions.extension_component("Histo_Next_Page")
    async def HistoNextPageButton(self,ctx: interactions.ComponentContext):
        await Historique.change_page(ctx, "Next")

    @interactions.extension_component("Histo_Last_Page")
    async def HistoLastPageButton(self,ctx: interactions.ComponentContext):
        await Historique.change_page(ctx, "Last")
 
def setup(client):
    Caca(client)



