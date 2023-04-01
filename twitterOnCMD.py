######################################################
##### AIXÓ HA ESTAT PROGRAMAT AMB UN GOS A SOBRE #####
######################################################

import tweepy
import textwrap
from prettytable import PrettyTable
import os
import time

# Col·loca les teves credencials de Twitter developer
consumer_key = '<>'
consumer_secret = '<>'
access_token = '<>'
access_token_secret = '<>'

# Autentica amb l'API de Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Crea una connexió a l'API de Twitter
api = tweepy.API(auth)

# Defineix la mida màxima per a cada línia de text
max_line_length = 40

# Defineix la mida de la taula
table = PrettyTable(['Usuari', 'Tuit'])

while True:
    # Netegem la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')

    # Obtenim els últims 10 tuits del Time Line
    tweets = api.home_timeline(count=30, tweet_mode='extended')

    # Afegeix cada tuit a la taula
    for tweet in tweets:
        # Trunquem el text del tuit a una longitud màxima, de manera que cada línia de la taula no superi una certa longitud
        truncated_text = tweet.full_text
        # Divideix el text truncat del tuit en diferents línies perquè s'ajusti a la mida de la columna
        wrapped_text = textwrap.wrap(truncated_text, width=max_line_length)
        # Afegeix una fila per a cada línia del tuit
        for i, line in enumerate(wrapped_text):
            # Només alineem la primera línia amb el nom d'usuari, les altres les deixem sense alineació
            if i == 0:
                table.add_row([tweet.user.name, line])
            else:
                table.add_row(['', line])

    # Imprimeix la taula
    print(table)

    # Pausa de 30 segons abans de netejar la pantalla i tornar a executar l'script
    time.sleep(30)
