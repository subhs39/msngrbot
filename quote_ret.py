import wikiquotes

def quotes_person(para):
	quote=wikiquotes.get_quotes(para, "english")
	return quote
def day_quote():
	quote=wikiquotes.quote_of_the_day("english")
	person=quote[1]
	quote=quote[0]
	return quote,person
