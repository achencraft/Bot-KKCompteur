#######################################################################################
#                                                                                     #
#                                   Classe Data                                     #
#                                                                                     #
#######################################################################################
import os, json, arrow
from shared.Chieur import Chieur


class Data():


    chieurs = []
    conf = ""
    channel = ""

    def Charger_chieurs(config):
        Data.conf = config

        if os.path.exists(config['JSON_DATA']):
            data = json.load(open(config['JSON_DATA']))
            for chieur in data['chieurs']:
                Data.chieurs.append(Chieur(chieur['username'],chieur['discord'],chieur))


#######################################################################################
#                                     Getter                                          #
#######################################################################################


    def get_user(userid):
        for c in Data.chieurs:
            if c.discord == userid:
                return c
        return None
            
    def add_user(userid,username):
        Data.chieurs.append(Chieur(username,userid))

    def get_annee():
        return Data.conf['ANNEE']
    
    def get_GuildChannel():
        return (Data.conf['GUILD_ID'],Data.conf['CHANNEL_ID'])
    

    def getPodium(user_id):
        return sorted(Data.chieurs, key=lambda x: len(x.kk),reverse=True)
    
    def getChieurOfTheDay():
        maxKKNbr = 0
        people = []
        date = arrow.utcnow().to('Europe/Paris').shift(hours=-6).format('DD/MM/YYYY')

        for c in Data.chieurs:
            if len(c.kk) > maxKKNbr:
                maxKKNbr = len(c.kk)
                people = []
                people.append((c.username,maxKKNbr))
            elif len(c.kk) == maxKKNbr:
                people.append((c.username,maxKKNbr))
            
        return people

    def getHisto(user_id):
        if(Data.get_user(user_id) != None):
            return sorted(Data.get_user(user_id).kk, key=lambda x: x.id)
        else:
            return []


#######################################################################################
#                                     Setter                                          #
#######################################################################################

    def set_user(userid,username):
        Data.chieurs.append(Chieur(username,userid))


#######################################################################################
#                                     Utils                                           #
#######################################################################################

    def save_data():

        with open(Data.conf['JSON_DATA'], "w") as outfile:

            out = '{"chieurs":['

            for c in Data.chieurs:
                

                out = out + '{"username":"' + c.username+'","discord":"'+c.discord +'","kk":['
                
                for k in c.kk:
                    out = out + '{"date":"' + k.date+'","heure":"'+k.heure +'","id":"'+str(k.id)+'"},'
                out = out[:-1]
                out = out + ']},'
            out = out[:-1]
            out = out + ']}'
        
            outfile.write(out)