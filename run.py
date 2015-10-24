from flask import Flask, request, redirect
import twilio.twiml
from utils import mWebLookup, wikiLookup

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
	message = request.values.get('Body', None)
	message_list = message.split(" ")

	action = "".join(message_list[0])
	value = " ".join(message_list[1:])

	resp = twilio.twiml.Response()
	if action.upper() == "DEFINE":
		definition = mWebLookup(value)
		resp.message("The definition of " + value + "is " + definition)
	# elif action.upper() == "SOLVE":
	# 	resp.message("Solution is simple m8: " + value)
	# elif action.upper() == "SEARCH":
	# 	resp.message("Google it you lazy fuck " + WikiLookup(value))
	return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
