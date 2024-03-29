emoji = {'low': '\U00002198',
         'high': '\U00002197',
         'best': '\U00002705',
         'history': '\U0001F4D3',
         'hotel': '\U0001F3E8',
         'address': '\U0001F4CD',
         'price': '\U0001F4B0',
         'landmarks': '\U0001F3AF',
         'link': '\U0001F4CE',
         'settings': '\U0001F527'}

dictionary = {
    'started_message': {
        'ru_RU': 'Выбери команду: '
        '\n\n {} /lowprice - Узнать топ самых дешёвых отелей в городе'
        '\n\n {} /highprice - Узнать топ самых ддорогих отелей в городе'
        '\n\n {} /bestdeal - Узнать топ отелей, наиболее подходящих по цене и'
                 ' расположению от центра (самые дешевые и расположены ближе'
                 ' всего к центру'
        '\n\n {} /history - Узнать историю поиска отелей'
        '\n\n {} /settings (по желанию) - Установить параметры поиска'
                 ' (язык, валюта)',
        'en_US': 'Choose a command: '
        '\n\n {} /lowprice - Find the top cheapest hotels in the city'
        '\n\n {} /highprice - Find the top most expensive hotels in the city'
        '\n\n {} /highprice - Find the top hotels most suitable for the price'
                 ' and location from the center (the cheapest and the closest'
                 ' to the center'
        '\n\n {} /history - View the history of hotel search'
        '\n\n {} /settings (optional) - Set search parameters'
                 ' (language, currency)'
    },
    'set_lang': {
        'ru_RU': 'Установить язык по умолчанию:',
        'en_US': 'Set the default language:'
    },
    'set_cur': {
        'ru_RU': 'Установить валюту по умолчанию:',
        'en_US': 'Set the default currency',
    },
    'search': {
        'ru_RU': 'Выполняю поиск...',
        'en_US': 'Searching'
    },
    'ask_for_city': {
        'ru_RU': 'Какой город Вас интересует?',
        'en_US': 'Which city are you interested in?',
    },
    'hotels_value': {
        'ru_RU': 'Сколько отелей смотрим? (не более 10)',
        'en_US': 'How many hotels are we looking at? (max 10)'
    },
    'photo_needed': {
        'ru_RU': 'Показывать фотографии отелей?',
        'en_US': 'Show photos of the hotels?'
    },
    'photos_value': {
        'ru_RU': 'Сколько фотографий по каждому отелю?',
        'en_US': 'How many photos for each hotel?'
    },
    'city_results': {
        'ru_RU': 'Предлагаю немного уточнить запрос:',
        'en_US': 'I propose to clarify the request:'
    },
    'pos': {
        'ru_RU': 'Да',
        'en_US': 'Yes'
    },
    'neg': {
        'ru_RU': 'Нет',
        'en_US': 'No'
    },
    'ready_to_result': {
        'ru_RU': 'Найдены следующие варианты...',
        'en_US': 'The following options have been found ...'
    },
    'main_results': {
        'ru_RU': "\n\n{e_hotel}{name}{e_hotel}"
                 "\n\n{e_address}<a href='{address_link}'>{address}</a>"
                 "\n\n{e_dist}Ориентиры: {distance}"
                 "\n\n{e_price}Цена за ночь: {price}"
                 "\n\n{e_link}<a href='{link}'>Подробнее на hotels.com</a>",
        'en_US': "\n\n{e_hotel}{name}{e_hotel}"
                 "\n\n{e_address}<a href='{address_link}'>{address}</a>"
                 "\n\n{e_dist}Landmarks: {distance}"
                 "\n\n{e_price}Price per night: {price}"
                 "\n\n{e_link}<a href='{link}'>More на hotels.com</a>"
    },
    'additionally': {
        'ru_RU': 'Не нашли подходящий вариант?\nЕщё больше отелей по вашему запросу\\: [смотреть]({link})'
                 '\nХотите продолжить работу с ботом? /help',
        'en_US': "Didn't find a suitable option?\nMore hotels on your request\\: [view]({link})"
                 "\nDo you want to continue working with the bot? /help"
    },
    'val_err': {
        'ru_RU': 'Необходимо ввести целое число (не более 10):',
        'en_US': 'You must enter an integer (no more than 10):'
        },
    'crt_err': {
        'ru_RU': 'Что-то пошло не так, перезагружаюсь...',
        'en_US': 'Something went wrong, restart...'
    },
    'rng_err': {
        'ru_RU': 'Необходимо ввести два целых положительных отличных'
                 ' друг от друга числа:',
        'en_US': 'It is necessary to enter two positive integers that are'
                 ' different from each other:'
    },
    'ask_price': {
        'ru_RU': 'Уточните ценовой диапазон ({cur}):'
                 '\n(Например: "от 1000 до 2000", "1000-2000", "1000 2000")',
        'en_US': 'Specify the price range ({cur}):'
                 '\n(As example: "from 1000 to 2000", "1000-2000", "1000 2000")'
    },
    'ask_dist': {
        'ru_RU': 'Уточните диапазон расстояния, на котором находится отель от'
                 ' центра (км):'
                 '\n(Например: "от 1 до 3" / "1-3" / "1 3")',
        'en_US': 'Specify the range of the distance at which the hotel is'
                 ' located from the center (mile)'
                 '\n(As example: "from 1 to 3" / "1-3" / "1 3"'
    },
    'no_options': {
        'ru_RU': 'По вашему запросу ничего не найдено...\n/help',
        'en_US': 'Nothing was found for your query...\n/help'
    },
    'operations_for_history': {
        'ru_RU': ('Очистить', 'Скрыть'),
        'en_US': ('Clear', 'Hide')
    },
    'clr_history': {
        'ru_RU': 'Ваша история поиска пуста!',
        'en_US': 'Your search history is empty!'
    },
}