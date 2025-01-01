#######################################################################################
#                                                                                     #
#                                   Classe Chieur                                     #
#                                                                                     #
#######################################################################################
from shared.Travail import Travail
import arrow, json

class Chieur():

    def __init__(self,username,userid,data=""):
        self.username = username
        self.discord = userid
        self.kk = []

        if(data != ""):
            for kk in data['kk']:  
                self.kk.append(Travail(kk['date'],kk['heure'],kk['id']))


#######################################################################################
#                                     Getter                                          #
#######################################################################################


    def get_kk_number(self):
        return len(self.kk)

    

#######################################################################################
#                                     Setter                                          #
#######################################################################################

    def add_kk(self, _date):

        id = len(self.kk) + 1

        if(_date == "now"):
            date = arrow.utcnow().to('Europe/Paris').format('DD/MM/YYYY')
            heure = arrow.utcnow().to('Europe/Paris').format('HH:mm')
        else:
            date = _date.split(" ")[0]
            heure = _date.split(" ")[1]
        self.kk.append(Travail(date, heure, id))

