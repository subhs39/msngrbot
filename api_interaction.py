import apiai

CLIENT_ACCESS_TOKEN = 'be61ca5be7a54207899ece0128214bdd'


def ret_resp(text_message):

    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.query = text_message

    response = request.getresponse()

    return (response.read())
