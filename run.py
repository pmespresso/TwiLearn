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
    """Respond and greet the caller by name."""
 
    message = request.values.get('Body', None)
    message_list = message.split(" ")

    # action = message_list[0]
    # value = message_list[1:]
 
 	# if action == "Define":
 	# 	define(value)
 	# else:
 	# 	resp = twilio.twiml.Response()
 	# 	resp.message("fuck you")

    resp = twilio.twiml.Response()
    resp.message(message_list)
    # resp.message("The definition of " + value + "is " + "fuck off")
 
    return str(resp)

@app.route("/define", methods=['GET'])
def define():
	return
 
if __name__ == "__main__":
    app.run(debug=True)



# def default():
# 	resp = twilio.twiml.Response()
# 	resp.message("hello there, what do you want from me?")

# 	message = request.args.get('Body')
# 	resp.message("was this your message? ")
# 	resp.message(message)
# 	return str(resp)


# def sms_reply():
#     # Retrieve the body of the text message.
#     message_body = request.values.get('Body', None)

#     # Create a TwiML response object to respond to the text message.
# 	resp = Response()
#     message_response = 'Message received! Manipulating memory now.'

#     # Create a list of all words in the message body.
#     message_list = message_body.split(' ')
#  	error_message = "Yo that shit too short nigguh"

#     # Make sure the message is in the right format.
#     if not len(message_list) > 0:
#         message_response = error_message
#     else:
#         # The first word should be the desired action. i.e. Define:
#         action = message_list[0]

#         # The second word should be the value to write to the action.
#         value = message_list[1]

#         message_response = action
 
#     resp.message(message_response)
#     return str(resp)

    # resp.message("Text Us With What You Want To Learn. Define: { word }")

    # with resp.gather(action="/gather") as g:
    # 	g.sms("Here you go: " )
    # resp.pause()
    # resp.redirect("/")
    # return str(resp)


# @app.route("/gather", methods=['GET', 'POST'])
# def gather():
# 	resp = twilio.twiml.Response()

# 	body = request.form["Body"]

# 	resp.message(body)
# 	return str(body)

if __name__ == "__main__":
    app.run(debug=True)
