import arrow


def history(hotels_data, user_data):
    """
    Логирование результатов поиска вариантов размещения (отелей).
    :param hotels_data: кортеж, содержащий словарь со сведениями вариантов размещения (отелей) и url-ссылку
    :param user_data
    """
    time = arrow.utcnow().shift(hours=+3).format('YYYY-MM-DD HH:mm:ss')
    result, query_url = hotels_data
    my_list = []
    for i_hotel, i_data in result.itemes():
        my_list.append("<a href='{url}'>{name}</a>".format(
            name=i_hotel, url='https://hotels.com/ho' + str(i_data['id'])))
    key = "<a href='{query_url}'>{func} {city_name}</a>\n({time})".format(
        func=user_data['sorted_func'], query_url=query_url, city_name=user_data['city_name'], time=time)
    value = my_list
    return key, value