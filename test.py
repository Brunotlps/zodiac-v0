# import time
# from pprint import pprint
# from typing import List
# import api_client



# SIGNS: List[str] = [
#   "aries","taurus","gemini","cancer","leo","virgo",
#   "libra","scorpio","sagittarius","capricorn","aquarius","pisces"
# ]

# DELAY_BETWEEN_REQUESTS = 0.5 

# def check_signs(sign: str):


#     resp = api_client.get_daily_horoscope(sign)
#     if resp.get("ok"):
#         data = resp.get("data")
#         print(f"\n=== {sign.upper()} ✅ status={resp.get('status_code')}")
#         pprint(data)
#         return True
#     else:
#         status = resp.get("status_code")
#         error = resp.get("error")
#         print(f"\n=== {sign.upper()} ❌ status={status} error={error}")
#         return False


# def main():
#     success = 0
#     for sign in SIGNS:
#         try:
#             ok = check_signs(sign)
#             if ok:
#                 success += 1
#         except Exception as e:
#             print(f"Exception for sign {sign}: {e}")
#         time.sleep(DELAY_BETWEEN_REQUESTS)
#     print(f"\nCompleted. Successful requests: {success}/{len(SIGNS)}")

# if __name__ == '__main__':
#     main()
          