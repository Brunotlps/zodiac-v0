import requests
from typing import Optional, Dict, Any
from datetime import date
import config



def get_daily_horoscope(sign: str, timeout: int = 10) -> Dict[str, Any]:
    """
    Fetches the daily horoscope for a given zodiac sign.
    Args:
        sign (str): The zodiac sign (e.g., 'aries', 'taurus', etc.).
        timeout (int): Timeout for the API request in seconds. Defaults to 10.
    Returns:
        Dict[str, Any]: The JSON response from the API containing the horoscope data.
    """

    current_date = date.today()
    formated_date = current_date.strftime("%Y-%m-%d")

    payload = {"api_key": config.API_KEY, "date": formated_date, "sign": sign}
    
    try:
        resp = requests.post(config.API_URL, headers=config.HEADERS, data=payload, timeout=timeout)
        status = resp.status_code
        try: 
            body = resp.json()
        except ValueError:
            body = resp.text
        

        if 200 <= status < 300:
            return {"ok": True, "status_code": status, "data": body}
        else:
            return {"ok": False, "status_code": status, "error": body}
    

    except requests.Timeout:
        return {"ok": False, "status_code": None, "error": "timeout"}
    except requests.ConnectionError:
        return {"ok": False, "status_code": None, "error": "connection_error"}
    except requests.RequestException as e:
        return {"ok": False, "status_code": None, "error": str(e)}


