import requests
import json

page='EAAGeqbKAeBsBANoM8kD01gIRR4XzfZBhxCbuqcpZC8AHo6OXUSz3vPOMIXN4Pw2UBS31KRdIvMKBRSmjFKQTLeSHvjWfaFZCZARXteuEQKZCIRXoZCWBysb2qzbg0DAa7fIdXWG4yZBcz0WMpZAedfShv2545GiGa9PsI7JSXe6RuaiCVVNrFy3v'

def get_name(sender):
	url="https://graph.facebook.com/v2.6/{}?fields=first_name,last_name,profile_pic&access_token={}".format(sender,page)
	r=requests.get(url)
	final=r.text
	final=json.loads(final)

	name = final['first_name']


	return name
