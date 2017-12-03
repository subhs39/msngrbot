from flask import Flask, request

PAGE_ACCESS_TOKEN = 'EAAJZCH7lRa4EBAHnaFLPFp83cXZCOO84ZB47FxtGtHHbkFxDMb025Qrxpbny7JS06UmGygqcmwpbvVjadRZCDqwZAMQV5ZCXOYeXcwa9tuXGIbtky2992RjJckScMx0xlQOPRBJjGdqy87LLve4HWzngN6PNsPFfDZBCSDQD3REzwTF5cyJLen3'
VERIFY_TOKEN = 'messi'

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    # Once the endpoint is added as a webhook, it must return back
    # the 'hub.challenge' value it receives in the request arguments
    """if (request.args.get('hub.verify_token', '') == VERIFY_TOKEN):
        print("Verified")
        return request.args.get('hub.challenge', '')
    else:
        print('wrong verification token')
        return "Error, Verification Failed"  """
    #another way of doing it
    if request.args.get('hub.mode')=="subscribe" and request.args.get('hub.challenge'):
    	if not request.args.get('hub.verify_token') == "messi":
    		return "Verification token mismatch",403
    	return request.args["hub.challenge"], 200
    return "OK", 200


@app.route('/', methods=['POST'])
def handle_message():
    '''
    Handle messages sent by facebook messenger to the applicaiton
    '''
    data = request.get_json()

    log(data)
    return "OK"

def log(message):
	print(message)
	sys.stdout.flush()


if __name__=="__main__":
	app.run(debug=True)