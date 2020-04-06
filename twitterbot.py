import tweepy
import urllib.request, json, time
from requests_html import HTMLSession
import time

consumer_key = 'EdyjDMPpfrI7F5bck0YvSQuIz'
consumer_secret = 'Pn8fnn5j0H7KpshdnIPWq5etZEUWAZqkq9BSJTQpPGRI6NR4ki'
access_token = '1246887673937252352-rKDKtaSnAmdgs3uXl2C8azeM6PYLtC'
access_token_secret = '5lH9reUFc9y1XidYoptps1iXkKKLT3oxQM7gny3Ql5Jno'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def cotacao(tempo=1):
    session = HTMLSession()
    r = session.get('https://www.google.com/search?q=cota%C3%A7%C3%A3o+d%C3%B3lar&oq=cota%C3%A7%C3%A3o+d%C3%B3lar&aqs=chrome..69i57j0l5j69i61l2.3295j1j7&sourceid=chrome&ie=UTF-8')
    selector = '<span class="DFlfde SwHCTb" data-precision="2" data-value="5.34415">5,34</span>'
    valor = r.html.find(selector, first=True).text
    nova_cotacao = True
    print(f'1 Dólar vale {valor} reais.')
    api.update_status(f'1 Dólar vale {valor} reais.')
    while True:
        valor_atual = (r.html.find(selector, first=True).text)
        if valor_atual < valor:
            print(f'Preço do Dólar CAINDO: 1 dólar vale {valor_atual} reais')
            api.update_status(f'Preço do Dólar CAINDO: 1 dólar vale {valor_atual} reais')
            nova_cotacao = True
        elif valor_atual > valor:
            print(f'Preço do Dólar SUBINDO: 1 dólar vale {valor_atual} dólares!')
            api.update_status(f'Preço do Dólar SUBINDO: 1 dólar vale {valor_atual} dólares!')
            nova_cotacao = True
        else:
            if nova_cotacao == True:
                print('Aguardando uma nova cotação...')
                nova_cotacao = False
        valor = valor_atual
        time.sleep(tempo)

cotacao()
