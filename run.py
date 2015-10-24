from flask import Flask, request, redirect
import twilio.twiml
import utils

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
		definition = utils.MWebLookup(value)
		resp.message("The definition of " + value + "is " + definition)
	# elif action.upper() == "SOLVE":
	# 	resp.message("Solution is simple m8: " + value)
	# elif action.upper() == "SEARCH":
	# 	resp.message("Google it you lazy fuck " + WikiLookup(value))
	return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
