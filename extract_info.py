import json

response=(b'{\n  "id": "ee41768a-82ed-408f-b9d0-5c87083b9a79",\n  "timestamp": "2017-1'
 b'2-07T10:49:48.672Z",\n  "lang": "en",\n  "result": {\n    "source": "domain'
 b's",\n    "resolvedQuery": "hello",\n    "action": "smalltalk.greetings.hel'
 b'lo",\n    "actionIncomplete": false,\n    "parameters": {},\n    "contexts"'
 b': [],\n    "metadata": {},\n    "fulfillment": {\n      "speech": "Howdy.",'
 b'\n      "messages": [\n        {\n          "type": 0,\n          "speech": '
 b'"Good day!"\n        }\n      ]\n    },\n    "score": 1.0\n  },\n  "status'
 b'": {\n    "code": 200,\n    "errorType": "success",\n    "webhookTimedOut":'
 b' false\n  },\n  "sessionId": "fd05a1657a684667a41f02b83359017e"\n}')


"""4 cases
	1> a fallback action just let it be
	2> a greetings action just repeat greeting with name back to pymessenger
	3> a get-phone action just to subscribe (keep it aside for now)
	4> a get-person action [pass it on to wikiquotes api to get quotes back]
					and then pass it to pymessenger

			That's it

	Next task make it interactive  Upgrade button,menu,profile pic, etc etc
	add subscribers"""
def extract_info(response):
    parameters=None
    response=json.loads(response)

    new_resp=response['result']

    if new_resp['action'] == "smalltalk.greetings.hello" :
        speech=new_resp['fulfillment']
        speech=speech['speech']             #confusing !
        return (speech,parameters)
    elif new_resp['action'] == "get-phone" :
        parameters=new_resp['parameters']['phone-number']
        parameters=parameters[0]
        speech=new_resp['fulfillment']
        speech=speech['speech']
        return (speech,parameters)
    elif new_resp['action'] == "get-person" :
        speech=new_resp['fulfillment']
        speech=speech['speech']
        parameters=new_resp['parameters']
        if len(parameters['any']) is not 0:
            return(speech,parameters['any'][0])
        else:
            return(speech,parameters['given-name'][0])
