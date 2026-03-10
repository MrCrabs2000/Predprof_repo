from typing import Optional
import requests
import json


def api_post(url: str, data: Optional[dict] = None, headers: Optional[dict] = None):
    try:
        response = requests.post(
            url,
            json=data or {},
            headers=headers or {}
        )
        if (response.status_code != 204 and response.content) and response.status_code in [200, 201, 202, 204]:
            return response.json()
        else:
            print(f'Статус код POST запроса {response.status_code}: {response.text[:200]}')
            return None

    except Exception as e:
        print(f'POST запрос для API: {url}, вызвал ошибку: {e}')


def api_get(url: str, params: Optional[dict] = None, headers: Optional[dict] = None, time_out = 10):
    try:
        response = requests.get(
            url,
            headers=headers or {},
            params=params or {},
            timeout=time_out
        )
        if response.status_code == 200:
            return response.json()
        else:
            return None

    except requests.exceptions.Timeout:
        print(f'Таймаут GET запроса к API :{url}')
        return None

    except Exception as e:
        print(f'GET запрос для API: {url}, вызвал ошибку: {e}')
        return None

