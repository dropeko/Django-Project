from django.db import models
from django.contrib.auth.models import User

# Onde ficam os modelos para manipulação das BDs do APP
class Evento(models.Model):#Criando uma classe representando uma tabela para manipular a aplicação(que terá função de agenda)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)#Parametro para aceitar valores em branco e nulos
    data_evento = models.DateTimeField(verbose_name='Data do Evento') #Parametro para como sera o nome da aplicação web
    data_registro = models.DateTimeField(auto_now=True, verbose_name='Data do Registro')#Parametro para como sera o nome da aplicação web
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #Se o usuario dono desse EVENTO for exlcuido, exclui TODOS os eventos dele

    class Meta:#Cria uma classe para sempre nomear a tabela como EVENTO
        db_table = 'EVENTO'

    def __str__(self): #Função para acessar o objeto e retornar o TITULO
        return  self.titulo

