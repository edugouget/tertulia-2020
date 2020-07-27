# -*- coding: utf-8 -*-

import pandas as pd
import math
from datetime import datetime
import os.path

############ EDITAR AQUI ##########
excel_file = 'Tertulias (falta 2012).xlsx'
arquivo_xml = "tertulias.xml"
meu_servidor = 'https://gouget.com.br/teste/'
diretorio = 'img/'
###################################

tertulias = pd.read_excel(excel_file, sheet_name=0)
f = open(arquivo_xml, "wb")

a = tertulias['LINK MP3'].notnull() 
filtro = tertulias[a]
filtro = filtro.sort_values(by='Data',ascending=False)
linha, coluna = filtro.shape

mydate = datetime.now()
mes = mydate.strftime("%B")[:3]
semana = mydate.strftime("%A")[:3]
DATA = semana + ', ' + str(mydate.day) + ' ' + mes + ' ' + str(mydate.year) + ' ' + mydate.strftime("%H") +  ':' + mydate.strftime("%M") + ':' + mydate.strftime("%S") +' -0300'

##### Escreve cabeçalho
description = "As Tertúlias Conscienciológias são as aulas-debate sobre 1 verbete da Enciclopédia da Conscienciologia, organizada pelo Prof. Waldo Vieira. Ocorrem diariamente no Tertuliarium, construído especialmente para esta atividade, localizado no Centro de Altos Estudos da Conscienciologia - CEAEC, em Foz do Iguaçu, Paraná, Brasil."
texto = '<?xml version="1.0" encoding="UTF-8"?>\n<rss xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:atom="http://www.w3.org/2005/Atom" version="2.0">\n<channel>\n<title>Tertúlia On-Line - Conscienciologia</title>\n<link>'+ meu_servidor +'</link>\n<itunes:author>Tertuliarium</itunes:author>\n<description>'+ description +'</description>\n<atom:link href="'+ meu_servidor + arquivo_xml +'" rel="self" type="application/rss+xml"/>\n<pubDate>'+DATA+'</pubDate>\n<language>pt-br</language>\n<itunes:category text="Education">\n<itunes:category text="Self-Improvement"/>\n</itunes:category>\n<itunes:category text="Science">\n<itunes:category text="Social Sciences"/>\n</itunes:category>\n<itunes:explicit>no</itunes:explicit>\n<image><url>'+ meu_servidor + 'tertuliarium.jpg</url></image>\n'
#print(type(texto))
f.write(texto.encode("utf-8", errors="ignore"))
      
##### Gera dados do XML
for i in range(linha):
    x = filtro.iloc[i]
    texto = "\n<item><title>Tertúlia " + str(int(x['Tertúlia'])) + " - " + x['Título do Verbete'] + "</title>"
    f.write(texto.encode("utf-8", errors="ignore"))
    texto = '\n<description><![CDATA[ <b>Tertúlia:</b> ' + str(int(x['Tertúlia'])) +'<br><b>Titulo:</b> '+ x['Título do Verbete'] +'<br><b>Especialidade:</b> '+ x['Especialidade'] +'<br><b>Autor(a):</b> '+ x['Verbetógrafo'] +'<br><b>Data:</b> '+ str(str(x['Data'])[:10]) +' <br><a href="'+x['PDF']+'">Baixe aqui o verbete em PDF.</a> <br> <iframe width="560" height="315" src="https://www.youtube.com/embed/'+ x['YOUTUBE'][-11:] +'" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> ]]></description>'
    f.write(texto.encode("utf-8", errors="ignore"))
    texto = '\n<author>'+ x['Verbetógrafo'] +'</author>'
    f.write(texto.encode("utf-8", errors="ignore"))
    texto = '\n<itunes:image href="' + meu_servidor + diretorio + str(int(x['Tertúlia'])) +'.jpg"/>'
    f.write(texto.encode("utf-8", errors="ignore"))
    texto = '\n<enclosure type="audio/mpeg" url="'+ x['LINK MP3'] +'"/>'
    f.write(texto.encode("utf-8", errors="ignore"))
    texto = '\n<itunes:duration>7081</itunes:duration>'
    f.write(texto.encode("utf-8", errors="ignore"))
    a = str(x['Data'])[:10]
    mydate = datetime.strptime(a, '%Y-%m-%d').date()
    #mydate = datetime.now()
    mes = mydate.strftime("%B")[:3]
    semana = mydate.strftime("%A")[:3]
    DATA = semana + ', ' + str(mydate.day) + ' ' + mes + ' ' + str(mydate.year) + ' 12:30:00 -0300'
    texto = '\n<pubDate>'+ DATA +'</pubDate></item>\n'
    f.write(texto.encode("utf-8", errors="ignore"))

##### Finaliza XML
texto = '</channel>\n</rss>'
f.write(texto.encode("utf-8", errors="ignore"))
f.close()

##### verifica se o arquivo da thumb exite, caso não, faz download
existe = os.path.isdir(diretorio)
if not existe:
    os.system('mkdir '+diretorio)
for i in range(linha):
    x = filtro.iloc[i]
    arquivo = diretorio + str(int(x['Tertúlia'])) +'.jpg'
    existe = os.path.isfile(arquivo)
    if not existe:
        os.system('wget -c '+x['Thumb']+' -O '+ diretorio + arquivo +'.jpg && sleep 3')
        os.system('convert '+ diretorio + arquivo +'.jpg -resize 512x512 -background black -gravity center -extent 512x512 '+ diretorio + arquivo +'.jpg')
