from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
# Try adding your own number to this list!
callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
    "+5109902644": "YJ",
}
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
	message = request.values.get('Body', None)
	message_list = message.split(" ")

	action = "".join(message_list[0])
	value = " ".join(message_list[1:])

	resp = twilio.twiml.Response()
	if action.upper() == "DEFINE":
		definition = MWebLookup(value)
		resp.message("The definition of " + value + "is " + definition)
	# elif action.upper() == "SOLVE":
	# 	resp.message("Solution is simple m8: " + value)
	# elif action.upper() == "SEARCH":
	# 	resp.message("Google it you lazy fuck " + WikiLookup(value))
	return str(resp)

def MWebLookup(s):
	from lxml import etree
	import requests
	import sys
	import re
	page = requests.get('http://www.merriam-webster.com/dictionary/' + s)
	text = page.text.encode('ascii', 'ignore').decode('ascii')
	a = text.find('ssens')
	b = text.find('>', a)
	c = text.find('</span>', b+3)
	#print text[b+1:c]
	text = re.sub('(<.*?>)|(&lt)|(&gt)', '', text[b+1:c])
	text = re.sub('\s+', ' ', text);
	text = text[text.find(":")+1:]
	if(text.find('{ var') != -1):
		return 'Err: ' +s + ' could not be found. Check your spelling and try again'
	else:
		return text

def WikiLookup(s):
	page = requests.get('https://en.wikipedia.org/wiki/'+s)
	text = page.text.encode('ascii', 'ignore').decode('ascii')
	a = text.find('<p>')
	b = text.find('>', a)
	c = text.find('</p>', b+3)
	#print text[b+1:c]
	text = re.sub('(<.*?>)|(&lt)|(&gt)', '', text[b+1:c])
	text = re.sub('\s+', ' ', text);
	text = text[text.find(":")+1:]
	if(text.find('{ var') != -1 or len(text) < 3):
		return 'Err: ' +s + ' could not be found. Check your spelling and try again'
	else:
		return text

if __name__ == "__main__":
    app.run(debug=True)
