import os
import hashlib
import time
import json
import telegram
from dotenv import load_dotenv
from steam import steam_discussion_to_json


# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa o bot do Telegram
bot = telegram.Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))

if not os.path.exists('data'):
    os.makedirs('data')

# Nome do arquivo para armazenar os hashes dos comentários
HASHES_FILENAME = './data/comment_hashes.txt'


def main():
    # URL da discussão da Steam
    url = os.getenv('STEAM_URL')

    # Verifica a última página processada da discussão
    try:
        with open('./data/current_page.txt', 'r') as f:
            start_page = int(f.read())
    except FileNotFoundError:
        start_page = 1

    # Carrega os hashes dos comentários já enviados
    try:
        with open(HASHES_FILENAME, 'r') as f:
            comment_hashes = set(f.read().splitlines())
    except FileNotFoundError:
        comment_hashes = set()

    # Processa os comentários da discussão
    comments, current_page = steam_discussion_to_json(url, start_page=start_page)


    # Verifica se cada comentário já foi enviado e envia se não tiver sido
    for comment in comments:
        # Calcula o hash do comentário
        comment_hash = hashlib.md5(comment['text'].encode('utf-8')).hexdigest()

        # Se o hash do comentário já estiver na lista de hashes, pula para o próximo comentário
        if comment_hash in comment_hashes:
            print("jafoi")
            continue

        # Adiciona o hash do comentário à lista de hashes
        comment_hashes.add(comment_hash)

        # Envia o comentário por telegram
        bot.send_message(chat_id=os.getenv('TELEGRAM_CHAT_ID'), text=comment['text'])
        print(f"--> { comment['text'] }")

        # Salva o novo hash na lista de hashes
        with open(HASHES_FILENAME, 'a') as f:
            f.write(comment_hash + '\n')

    # Salva a última página processada
    with open('./data/current_page.txt', 'w') as f:
        f.write(str(current_page))

    # Aguarda o tempo configurado na variável de ambiente WAIT
    wait_time = int(os.getenv('WAIT', '300'))
    print(f'\n\nWaiting: {int(wait_time)} minutes')
    time.sleep(wait_time * 60)

    # Recomeça o processo
    main()


main()