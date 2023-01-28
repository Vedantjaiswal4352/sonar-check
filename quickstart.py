from json import dumps

from httplib2 import Http


def main():
    """Hangouts Chat incoming webhook quickstart."""
    url = 'https://chat.googleapis.com/v1/spaces/7D8la4AAAAE/messages?key=' \
          'AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=' \
          'HulDviWFMz6R5FW-GwlO4INCW1cZGDDExuWVaEbbr_g%3D'
    bot_message = {
        'text': 'Hello from a Python script!'}
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
    print(response)


if __name__ == '__main__':
    main()
