import requests
import json
import re


def bestdeal(user_city_id, lang, cur, hotels_value, hotel_url, headers, today, price_range, dist_range):
    """
    HTTP-запрос к Hotels API (rapidapi.com) (запрос вариантов отелей).
    :param user_city_id: id города
    :param lang: язык пользователя
    :param cur: валюта пользователя
    :param hotels_value: кол-во отелей
    :param hotel_url: url-ссылка на отель
    :param headers: headers
    :param price_range: ценовой диапазон
    :param dist_range: диапазон расстояния
    :param today: акутальная дата
    :return: кортеж, содержащий словарь со сведениями об отелях и url-ссылку
    """
    querystring = {"destinationId": user_city_id, "pageNumber": "1", "pageSize": str(hotels_value),
                   "checkIn": today, "checkOut": today, "adults1": "1",
                   "locale": "{}".format(lang), "currency": cur, "sortOrder": "DISTANCE_FROM_LANDMARK",
                   'priceMin': min(price_range), 'priceMax': max(price_range)}

    url = f'https://hotels.com/search.do?destination-id={user_city_id}&q-check-in={today}&q-check-out={today}' \
          f'&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&f-price-min={min(price_range)}' \
          f'&f-price-max={max(price_range)}&f-price-multiplier=1&sort-order={querystring["sortOrder"]}'

    hotels_list = []

    while len(hotels_list) < hotels_value:
        try:
            response = requests.request('GET', hotel_url, headers=headers, params=querystring, timeout=10)
            data = json.loads(response.text)
            list_result = data['data']['body']['searchResults']['results']
            if not list_result:
                return None, None
            for i_hotel in list_result:
                distance = re.findall(r'\d[,.]?\d', i_hotel['landmarks'][0]['distance'])[0].replace(',', '.')
                if float(distance) > max(dist_range):
                    raise ValueError('Превышено максимальное расстояние от центра города')
                elif float(distance) >= min(dist_range):
                    hotels_list.append(i_hotel)

            querystring['pageNumber'] = str(int(querystring.get('pageNumber')) + 1)

        except ValueError:
            break

    hotels_dict = {hotel['name']: {'id': hotel['id'], 'name': hotel['name'], 'address': hotel['address'],
                                   'landmarks': hotel['landmarks'], 'price': hotel['ratePlan']['price'].get(
            'current') if hotel.get('ratePlan', None) else '-', 'coordinate': '+'.join(
            map(str, hotel['coordinate'].values()))}
                   for hotel in hotels_list}

    return hotels_dict, url