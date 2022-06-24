from django.contrib import admin
from core.models import Evento #Importando classe/model para fazer o registro

class adminEvento(admin.ModelAdmin): #Classe para listagem do nome do evento, data e data de registro
    list_display = ('titulo', 'data_evento', 'data_registro')
    list_filter = ('usuario',)


admin.site.register(Evento, adminEvento)#Comando para adicionar a tabela a aplicação e associando o view a classe
