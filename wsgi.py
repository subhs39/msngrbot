from flask import Flask, request, render_template, g
import os, sys
import psycopg2

PAGE_ACCESS_TOKEN = 'EAAGeqbKAeBsBANoM8kD01gIRR4XzfZBhxCbuqcpZC8AHo6OXUSz3vPOMIXN4Pw2UBS31KRdIvMKBRSmjFKQTLeSHvjWfaFZCZARXteuEQKZCIRXoZCWBysb2qzbg0DAa7fIdXWG4yZBcz0WMpZAedfShv2545GiGa9PsI7JSXe6RuaiCVVNrFy3v'
VERIFY_TOKEN = 'messi'

app = Flask(__name__)

def connect_db():
    return psycopg2.connect(os.environ.get('DATABASE_URL'))

@app.before_request
def before_request():
    g.db_conn = connect_db()

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


    cur= g.db_conn.cursor()

    cur.execute("insert into subscribers (Name) values (%s);",('subz'))

    cur.execute("select * from subscribers;")
    subs=cur.fetchall()

    return render_template('main.html',subs=subs)
    # return "OK", 200


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
	app.run()