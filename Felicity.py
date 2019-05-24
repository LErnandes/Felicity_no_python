# Importando os Módulos.
from datetime import datetime
import pyttsx3
import os
import math
import re
import cv2
from urllib.request import urlopen
import webbrowser
from time import sleep
import wikipedia

wikipedia.set_lang('pt')

falador = pyttsx3.init()

yr = 'desmute'
def fala(text):
    if yr == 'desmute':
        falador.say(text)
        falador.runAndWait()
result = None
results = None # Resultado
now = datetime.now()
feli = 'Felicity: '
hr = now.hour
sq = 'raiz quadrada de '

if 6 <= hr < 12:
    gda = 'Bom dia'
elif 12 <= hr < 19:
    gda = 'Boa tarde'
elif hr >= 19 or hr < 6:
    gda = 'Boa noite'

print(feli + gda)
fala(gda)

while True:
    try:
        pw = 0
        print('')
        resq = input('Você: ').lower()
        print('')

        # Comandos
        if resq == 'ajuda' or resq == 'comandos':
            print('Comandos: ')
            print('')
            print('Pesquisar Wiki')
            print('')
            print('Calculadora')
            print('')
            print('Mute')
            print('')
            print('Desmute')
            print('')
            print('Contagem')
            print('')
            print('Contagem Regressiva')
            print('')
            print('Hora/Data')
            print('')
            print('CMD')
            print('')
            print('Arquivos')
            print('')
            print('Fechar')
            print('')
            print('Desligar')
            print('')
            print('Musica')
            print('')
            print('Escrever')
            print('')
            print('Ajuda Windows')
            print('')
            print('Bloco de Notas')
            print('')
            print('Converter Medidas')
            print('')
            print('Cotacao')
            print('')
            print('Converter Moedas')
            print('')
            print('Mapa Caracteres')
            print('')
            print('Painel Controle')
            print('')
            print('Som')
            print('')
            print('Informacoes Sistema')
            print('')
            print('Lupa')
            print('')
            print('Clima')
            print('')
            pw = 1

        if resq == 'lupa':
            os.startfile('magnify')
            lp = 'Lupa aberta.'
            fala(lp)
            pw = 1
            po = 0

        if sq in resq:
            srq = float(resq.replace(sq, ''))
            nsr = round(math.sqrt(srq), 2)
            nsrq = str(nsr)
            print(feli + nsrq)
            fala(nsrq)
            pw = 1
            po = 0
        
        if resq == 'mapa caracteres':
            os.startfile('charmap')
            mpc = 'Mapa de Caracteres aberto.'
            fala(mpc)
            pw = 1
            po = 0

        if resq == 'calculadora':
            os.startfile('calc')
            cal = 'Calculadora aberta.'
            fala(cal)
            pw = 1
            po = 0

        if resq == 'informacoes sistema':
            os.startfile('msinfo32')
            infs = 'Informações do Sistema aberto.'
            fala(infs)
            pw = 1
            po = 0

        if resq == 'painel controle':
            os.startfile('control')
            pan = 'Painel de Controle aberto.'
            fala(pan)
            pw = 1
            po = 0

        if resq == 'som':
            os.startfile('SndVol')
            snd = 'Mixer de Volume aberto.'
            fala(snd)
            pw = 1
            po = 0
            
        if resq == 'pesquisar wiki':
            t = input('Pesquisa: ')
            if t != '':
                print('')
                print('')
                results = wikipedia.summary(t)
                print(feli + results)
                fala(results)
                pw = 1
                po = 0

        if resq == 'mute':
            yr = 'mute'
            mtt = 'Estou sem voz.'
            print(feli + mtt)
            pw = 1
            po = 0

        if resq == 'desmute':
            yr = 'desmute'
            mdt = 'Estou com voz.'
            fala(mdt)
            pw = 1
            po = 0

        if resq == 'converter medidas':
            print('O que deseja converter?')
            print('')
            fala('O que deseja converter?')
            oq = input('Você: ').lower()
            pw = 1
            po = 0
            
            if oq == 'c para f':
                ce_1 = int(input('Graus Celcius: '))
                fe_1 = ((ce_1 / 5) * 9) + 32
                fe_11 = round(fe_1, 1)
                fe_12 = str(fe_11)
                print(feli + fe_12 + '°F.')
                if fe_12 > 1:
                    fala(fe_12 + ' grau fahrenheit')
                else:
                    fala(fe_12 + ' graus fahrenheit')
                
            if oq == 'f para c':
                fe_2 = int(input('Graus Fahrenheit: '))
                ce_2 = ((fe_2 -32) / 9) * 5
                ce_21 = round(ce_2, 1)
                ce_22 = str(ce_21)
                print(feli + ce_22 + '°C.')
                if ce_22 > 1:
                    fala(ce_22 + ' grau Celcius')
                else:
                    fala(ce_22 + ' graus Celcius')
                
            if oq == 'm para p':
                m_1 = float(input('Você: '))
                p_1 = m_1 * 3,28084
                if p_1 == 1:
                    print('Felicity: ' + p_1 + ' pé.')
                    fala(p_1 + 'pé')
                else:
                    print(feli + p_1 + ' pés.')
                    fala(p_1 + ' pés')
                    
            if oq == 'p para m':
                p_2 = float(input('Você: '))
                m_2 = p_2 / 3,28084
                print(feli + m_2 + ' m.')
                if m_1 == 1:
                    fala(m_2 + ' metro')
                else:
                    fala(m_2 + ' metros')

            if oq == 'q para l':
                q_1 = float(input('Você: '))
                l_1 = q_1 * 2,20462
                print(feli + l_1 + ' lb.')
                if l_1 == 1:
                    fala(l_1 + ' libra')
                else:
                    fala(l_1 + ' libras')

            if oq == 'l para q':
                l_1 = float(input('Você: '))
                q_1 = l_1 * 2,20462
                print(feli + q_1 + ' kg.')
                if q_1 == 1:
                    fala(q_1 + ' quilo') 
                else:
                    fala(q_1 + ' quilos')
                
        if resq == 'cotacao':
            CURRENCY = {
                'Dólar': 'http://dolarhoje.com/',
                'Euro': 'http://dolarhoje.com/euro/',
                'Libra': 'http://dolarhoje.com/libra-hoje/',
                'Bitcoin': 'http://dolarhoje.com/bitcoin-hoje/',
                'Ouro': 'http://dolarhoje.com/ouro-hoje/',
                'Yuan': 'http://dolarhoje.com/yuan-hoje/',
                'Peso': 'http://dolarhoje.com/peso-argentino/'
            }
            DEFAULT_REGEX = r'<input type="text" id="nacional" value="([^"]+)"/>'
            def exchange_rate(url):
                response = urlopen(url).read().decode('utf-8')
                result = re.search(DEFAULT_REGEX, response)
                if result:
                    return result.group(1)
            for currency, url in CURRENCY.items():
                cot = '{}: R${}'.format(currency, exchange_rate(url))
                print(cot)
                fala(cot)
            pw = 1
            po = 0

        if resq == 'converter moeda':
            prm = 'Para que moeda quer converter?'
            print(feli + prm)
            print('')
            fala(prm)
            moeda = input('Você: ')
            print('')
            url = 'http://' + moeda + 'hoje.com/'
            DEFAULT_REGEX = r'<input type="text" id="nacional" value="([^"]+)"/>'
            def exchange_rate(url):
                response = urlopen(url).read().decode('utf-8')
                result = re.search(DEFAULT_REGEX, response)
                if result:
                    return result.group(1)
            rrs = exchange_rate(url)
            rrrs = rrs.replace(',', '.')
            rs = float(rrrs)
            qnc = 'Quantos reais quer converter?'
            print(qnc)
            fala(qnc)
            print('')
            qrs = float(input('Você: '))
            nrs = rs * qrs
            if moeda == 'dolar':
                moeda = 'dólares'
            print('')
            print('R$ {} são {} {}.'.format(qrs, nrs, moeda))
            fala('{} reais são {} {}'.format(qrs, nrs, moeda))
            pw = 1
            po = 0

        if resq == 'clima':
            cliurl = 'https://www.google.com/search?q=weather'
            webbrowser.open_new_tab(cliurl)
            cma = 'Clima aberto.'
            print('')
            fala(cma)
            pw = 1
            po = 0
                     
        if resq == 'contagem':
            fala('Até quanto?')
            df = int(input('Você: '))
            print('')
            df += 1
            dff = 0
            while df > dff:
                print(dff)
                fala(dff)
                dff += 1
                sleep(1)
            pw = 1
            po = 0

        if resq == 'contagem regressiva':
            fala('De quanto?')
            df = int(input('Você: '))
            print('')
            dff = 0
            while df > dff:
                print(df)
                fala(df)
                df -= 1
                sleep(1)
            print('0')
            fala('0')
            pw = 1
            po = 0
        
        if resq == 'fechar':
            tc = 'Até mais.'
            fala(tc)
            os._exit(0)
            pw = 1
            po = 0

        if resq == 'musica':
            os.startfile('wmplayer')
            omp = 'Música aberta.'
            yr = 'mute'
            pw = 1
            po = 0

        if resq == 'cmd':
            os.startfile('cmd')
            ocmd = 'CMD aberto.'
            fala(ocmd)
            pw = 1
            po = 0
        
        if resq == 'arquivos':
            os.startfile('explorer')
            oar = 'Explorador de Arquivos aberto,.'
            fala(oar)
            pw = 1
            po = 0

        if resq == 'ajuda windows':
            os.startfile('Help Pane')
            ohp = 'Help Pane aberto.'
            fala(ohp)
            pw = 1
            po = 0

        if resq == 'escrever':
            os.startfile('write')
            oes = 'Write aberto.'
            fala(oes)
            pw = 1
            po = 0

        if resq == 'py':
            os.startfile('py')
            opy = 'Python aberto.'
            fala(opy)
            pw = 1
            po = 0
            
        if resq == 'bloco de notas':
            os.startfile('Notepad')
            obl = 'Bloco de Notas aberto.'
            fala(obl)
            pw = 1
            po = 0

        if resq == 'cls':
            os.system(['clear','cls'][1])
            fala('Tela limpa')
            pw = 1
            
        if resq == 'desligar':
            check = input("Felicity: Quer mesmo desligar o PC?: ")
            if check == 'sim':
                os.system("shutdown /s /t 1")
                adm = 'Adeus'
                fala(adm)
            pw = 1
            po = 0

        if resq == 'hora/data':
            now = datetime.now()
            oii = now.hour
            oiu = now.minute
            oio = now.day
            oiq = now.month
            oir = now.year
                     
            ii = str(oii)
            iu = str(oiu)
            io = str(oio)
            iq = str(oiq)
            ir = str(oir)
            
            if oii < 10:
                ii = '0' + ii
            if oiu < 10:
                iu = '0' + iu
            if oio < 10:
                io = '0' + io
            if oiq < 10:
                iq = '0' + iq
            agr = 'Agora é {}:{} de {}/{}/{}' .format(ii, iu, io, iq, ir)
            print(feli + agr)
            fala(agr)
            pw = 1
            po = 0
            
        
        # Conversa Normal
        if resq == 'oi':
            ola = 'Olá'
            print(feli + ola)
            fala(ola)
            pw = 1
            
        if resq == 'quem é você?':
            assis = 'Eu sou a Feliciri  - Sua assistente'
            print(feli + assis)
            fala(assis)
            pw = 1
            
        if resq == 'o que você faz?':
            oqvf = 'Eu estou aqui para servir a você.'
            print(feli + oqvf)
            fala(oqvf)
            pw = 1
            
        if resq == 'como vai você?':
            cvc = 'Vou bem, e você?'
            print(feli + cvc)
            fala(cvc)
            pw = 1
            
        if resq == 'vou bem':
            good = 'Fico feliz em saber que você está bem. Espero que amanhã, fique bem também.'
            print(feli + good)
            fala(good)
            pw = 1
            
        if resq == 'vou mal':
            bad = 'Fico triste em saber que você está mal. Espero que amanhã, seja bem melhor.'
            print(feli + bad)
            fala(bad)
            pw = 1
            
        if resq == 'em que linguagem você é feita?':
            pyt = 'Python'
            print(feli + pyt)
            fala(pyt)
            pw = 1
            
        if resq == 'quem fez você?':
            eu = 'Luis Ernandes.'
            print(feli + eu)
            fala(eu)
            pw = 1
            
        if resq == 'você é minha amiga?':
            fr = 'Sempre serei sua amiga.'
            print(feli + fr)
            fala(fr)
            pw = 1
            
        if resq == 'eu sou seu pai':
            stw = 'Não. Não. Não é verdade. Isso é impossivel. Naaaaaaaaaaaaaaaaao.'
            print(feli + stw)
            fala(stw)
            pw = 1
            
        if resq == 'o que você acha da microsoft?':
            micro = 'Adoro usar o Word para escrever a sua magnitude.'
            print(feli + micro)
            fala(micro)
            pw = 1
            
        if resq == 'o que você acha da apple?':
            apple = 'Adoro. Principalmente porque a linguagem que fui feito já vêm no MacBook, mas queria saber quem mordeu aquela maça.'
            print(feli + apple)
            fala(apple)
            pw = 1
            
        if resq == 'o que você acha do linux?':
            linux = 'Ótimo, amo pinguins e software livre.'
            print(feli + linux)
            fala(linux)
            pw = 1
            
        if resq == 'o que você acha do ampere?':
            amp = 'A intensidade da corrente elétrica pode me machucar.'
            print(feli + amp)
            fala(amp)
            pw = 1
            
        if resq == 'o que você acha do wall-e?':
            wall = 'Adoro Wall-E, mas acho que daqui a um tempo posso ficar com o emprego dele'
            print(feli + wall + ':(.')
            fala(wall)
            pw = 1
            
        if resq == 'o que você acha da pixar?':
            pix = 'Não tenho tempo para assistir os longas, mas os curtas são ótimos. O que eu mais gosto é aquele dos guarda-chuvas.'
            print(feli + pix)
            fala(pix)
            pw = 1
  
        if pw == 0:
            webbrowser.open_new_tab('https://www.google.com/search?q=' + resq)
            po = 0

        if po == 0:
            os.system(['clear','cls'][1])

    except:
        print('')
