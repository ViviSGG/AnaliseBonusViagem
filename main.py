# vídeo de referência: https://youtu.be/GQpQha2Mfpg 
# bibliotecas necessárias: pandas, openpyxl, twilio

# Descrição: Este programa ler 6 bases de dados Excel e notifica por SMS quando algum vendedor bate a meta de vendas de 55 mil. Com foco no aumento das vendas, o primeiro vendedor a bater a meta receberá uma viagem de incentivo. 

import pandas as pd # pd - abreviação de pandas para chamada no código
from twilio.rest import Client

# conexão com a conta twilio
# SID da minha conta em twilio.com/console
account_sid = "AC231cc8f8b3d7e4214935c50de0c3c4ba"
# meu Token de autenticação em twilio.com/console
auth_token  = "164c41ab054101292c08304a004253b0"

client = Client(account_sid, auth_token)

lista_meses = ['janeiro','fevereiro','março','abril','maio','junho'] # toda lista no python fica entre colchetes

# para cada mês dentro da lista de meses execute
for mes in lista_meses:

    #lendo o arquivo de forma dinâmica
    tabela_vendas = pd.read_excel(f'base-de-dados\{mes}.xlsx') # f - formatar (técnica de edição de texto)

    # se aglum valor da coluna da tabela vendas é maior que 55.000 faça
    if (tabela_vendas['Vendas'] > 55000).any(): # any - "algum" em inglês

        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0] # loc - localização / .values - puxa apenas o valor e não a tebela inteira
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0] # loc - localização / .values - puxa apenas o valor e não a tebela inteira

        print(f'No mês de {mes} alguém bateu a meta de R$55.000! \nVendedor: {vendedor} \nVendas: {vendas}')

        message = client.messages.create(
            to="+5581999346600", 
            from_="+18593408415",
            body=f'No mês de {mes} alguém bateu a meta de R$55.000! \nVendedor: {vendedor} \nVendas: {vendas}')
        print('Código do SMS: '+ message.sid) # printa o código da mensagem enviada 
