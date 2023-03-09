import requests
from bs4 import BeautifulSoup
import json
import html

def steam_discussion_to_json(url, start_page=1):
    print(f"url: {url}")
    # Lista que vai conter todos os comentários
    comments = []

    # Variável que controla a página atual da discussão
    current_page = start_page

    # Loop para percorrer todas as páginas da discussão
    while True:
        # URL da página atual da discussão
        page_url = f"{url}?ctp={current_page}"

        # Faz uma solicitação HTTP para a página da discussão
        response = requests.get(page_url)

        # Analisa o HTML da página usando o BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        for br in soup.find_all("br"):
            br.replace_with("\n\n")

        # Encontra todos os comentários na página
        comment_divs = soup.find_all('div', {'class': 'commentthread_comment'})

        # Se não houver mais comentários, saia do loop
        if len(comment_divs) == 0:
            break

        # Loop para percorrer todos os comentários da página
        for comment_div in comment_divs:
            # Extrai as informações do comentário
            author = comment_div.find('a', {'class': 'commentthread_author_link'}).text.strip()
            date = comment_div.find('span', {'class': 'commentthread_comment_timestamp'}).text.strip()
            # text = comment_div.find('div', {'class': 'commentthread_comment_text'}).get_text(strip=True)
            html = comment_div.find('div', {'class': 'commentthread_comment_text'}).get_text().strip()
            

            # Adiciona o comentário à lista de comentários
            comments.append({'author': author, 'date': date, 'text': html})
            # print(html)
            # print("\n\n------")

        # Incrementa a página atual
        current_page += 1

    # Retorna a lista de comentários como um objeto JSON
    return comments, current_page-1
