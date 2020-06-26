#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tabula
import pandas as pd
import numpy as np


# In[2]:



def organiza_pdf(data):
    df1 = data.drop(['Unnamed: 0','Unnamed: 1'], axis = 1)
    df1 = df1.drop([0,1,2,3,4,66])
    df1.columns = ['Municipio','Notificados','Confirmados','Clinico Epidemiologico','Participacao por Municipio','Incidencia',' Obitos','Letalidade','Mortalidade']
    
    
    temp = data.loc[3:4]
    temp = temp.drop(['Unnamed: 0','Unnamed: 9'], axis=1)
    temp.columns = ['Municipio','Notificados','Confirmados','Clinico Epidemiologico','Participacao por Municipio','Incidencia',' Obitos','Letalidade','Mortalidade']
    
    
    dados = df1.append(temp)
    dados = dados.sort_index()
    
    return dados

def organiza_pdf2(data):
    df1 = data.drop(['Unnamed: 0','Unnamed: 1'], axis = 1)
    df1 = df1.drop([0,1,2,64])
    df1.columns = ['Municipio','Notificados','Confirmados','Clinico Epidemiologico','Participacao por Municipio','Incidencia',' Obitos','Letalidade','Mortalidade']
    
    
    temp = data.loc[1:2]
    temp = temp.drop(['Unnamed: 0','Unnamed: 7'], axis=1)
    temp.columns = ['Municipio','Notificados','Confirmados','Clinico Epidemiologico','Participacao por Municipio','Incidencia',' Obitos','Letalidade','Mortalidade']
    
    
    dados = df1.append(temp)
    dados = dados.sort_index()
    
    return dados

def organiza_pdf3(data):
    df1 = data.drop(['Unnamed: 0'], axis = 1)
    df1 = df1.drop([0,1,2,3,4])
    df1.columns = ['Municipio','Notificados','Confirmados','Clinico Epidemiologico','Participacao por Municipio','Incidencia',' Obitos','Letalidade','Mortalidade']
    
    
    temp = data.loc[3:4]
    temp = temp.drop(['Unnamed: 8'], axis=1)
    temp.columns = ['Municipio','Notificados','Confirmados','Clinico Epidemiologico','Participacao por Municipio','Incidencia',' Obitos','Letalidade','Mortalidade']
    
    
    dados = df1.append(temp)
    dados = dados.sort_index()
    
    return dados


def insere_data(df,data):
    df['Data'] = data
    df['Data'] = pd.to_datetime(df['Data'].astype(str), format='%d-%m-%Y')
    
    return df


def geraCSV(destino,operacao,dfLeitos,csv_completo):
    if(operacao == 'n'):
        nome = str(destino+'CASOS_COVID.csv')
        dfLeitos.to_csv(nome)
        print('Finalizada a criação do csv!')
    else:
        #recupera o df completo a ser concatenado
        dfCompleto = pd.read_csv(csv_completo)
        dfFinal = pd.concat([dfLeitos,dfCompleto], ignore_index = True)
        dfFinal = dfFinal.drop('Unnamed: 0', axis = 1)
        nome = str(csv_completo)
        dfFinal.to_csv(nome)
        print('Finalizada a concatenação do csv!')


    
    


# In[4]:


continua = 'y'

while (continua == 'y'):
    operacao = input('(c) Concatenar | (n) Criar novo csv: ')

    operacao = operacao.lower()

    if(operacao == 'n'):
        origem = input('Digite o caminho para o PDF: ')

        data = input('Digite a data do arquivo (MM-DD-YYYY): ')

        destino = input('Digite o caminho para ser salvo: ')
        dia = int(data[0]+data[1])
    
    #gera o df
    
        if(dia<=5):
            dfLeitos = tabula.read_pdf(origem, area = [90,10,600,600], pages ='1',lattice = True)
            dfLeitos = organiza_pdf(dfLeitos[0])
        
        elif(dia == 6):
            dfLeitos = tabula.read_pdf(origem, area = [90,10,1150,1050], pages ='1',lattice = True)
            dfLeitos = organiza_pdf2(dfLeitos[0])
        
        elif(dia == 7):
            dfLeitos = tabula.read_pdf(origem, area = [90,10,1150,1050], pages ='1', lattice = True)
            dfLeitos = organiza_pdf3(dfLeitos[0])
            
        else:
            dfLeitos = tabula.read_pdf(origem, area = [90,10,1150,1050], pages ='1', lattice = True)
            dfLeitos = organiza_pdf(dfLeitos[0])
            
        dfLeitos = insere_data(dfLeitos,data)
    
    #gera o csv
        geraCSV(destino,operacao,dfLeitos,0)
    
    else:
        
        origem = input('Digite o caminho para o PDF: ')

        data = input('Digite a data do arquivo (DIA-MES-ANO): ')

        csv_completo = input('Digite o nome do arquivo .CSV a ser concatenado: ')
    
        dia = int(data[0]+data[1])

    #cria o novo df
        if(dia<=5):
            dfLeitos = tabula.read_pdf(origem, area = [90,10,600,600], pages ='1',lattice = True)
            dfLeitos = organiza_pdf(dfLeitos[0])
        
        elif(dia == 6):
            dfLeitos = tabula.read_pdf(origem, area = [90,10,1150,1050], pages ='1',lattice = True)
            dfLeitos = organiza_pdf2(dfLeitos[0])
        
        elif(dia == 7):
            dfLeitos = tabula.read_pdf(origem, area = [90,10,1150,1050], pages ='1', lattice = True)
            dfLeitos = organiza_pdf3(dfLeitos[0])
            
        else:
            
            dfLeitos = tabula.read_pdf(origem, area = [90,10,1150,1050], pages ='1', lattice = True)
            dfLeitos = organiza_pdf(dfLeitos[0])
            
        dfLeitos = insere_data(dfLeitos,data)
    
        #salva o CSV
        geraCSV(0,operacao,dfLeitos,csv_completo)
    
    continua = input('Realizar outra operação? (Y/n)')
    continua = continua.lower()


# In[5]:


#entra com o nome do pdf


dados = pd.read_csv('dataCASOS_COVID.csv')
dados


# In[ ]:




