from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    resp = twilio.twiml.Response()
    resp.message("Text Us With What You Want To Learn. Define: { word }")

    with resp.gather(action="/gather") as g:
    	g.sms("Here you go: " )
    resp.pause()
    resp.redirect("/")
    return str(resp)


@app.route("/gather", methods=['GET', 'POST'])
def gather():
	resp = twilio.twiml.Response()

	body = request.form["Body"]

	resp.message(body)
	return str(body)

if __name__ == "__main__":
    app.run(debug=True)