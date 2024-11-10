import requests
from loguru import logger
import random

# URL de l'API de Geonode pour récupérer des proxies
geonode_proxy_url = "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc"

# Configuration de Loguru pour un log détaillé dans un fichier log.txt
logger.add("log.txt", format="{time} {level} {message}", level="INFO")

# Fonction pour récupérer les proxies via l'API
def get_proxies_from_geonode():
    try:
        response = requests.get(geonode_proxy_url)
        if response.status_code == 200:
            proxies_data = response.json()['data']

            # Filtrer les proxies avec les protocoles 'http', 'https', 'socks4', 'socks5'
            proxies = []
            for proxy in proxies_data:
                for protocol in proxy['protocols']:
                    if protocol in ['http', 'https', 'socks4', 'socks5']:
                        proxies.append({
                            protocol: f"{protocol}://{proxy['ip']}:{proxy['port']}"
                        })
            logger.info(f"Nombre de proxies récupérés : {len(proxies)}")
            return proxies
        else:
            logger.error(f"Échec lors de la récupération des proxies, statut HTTP : {response.status_code}")
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des proxies : {e}")
    return []

# Fonction pour récupérer un proxy aléatoire
def get_random_proxy():
    proxies = get_proxies_from_geonode()
    if proxies:
        random.shuffle(proxies)
        return proxies[0]  # Retourner un proxy aléatoire
    else:
        logger.error("Aucun proxy n'a été récupéré.")
        return None
