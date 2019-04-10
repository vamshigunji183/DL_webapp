from flask import request
from flask import jsonify
from flask import Flask


app = Flask(__name__)
# methods parameter equals to a list contains the string 'POST'
# the methods parameter specifics what kind of HTTP requests are allowed for this endpoint
# with 'POST' request the client application will send the data to the web server along the request


@app.route('/hello',methods=['POST'])

def hello():
    """
    This method specify the what to do when 'POST' request is recieved by this endpoint.
    Here, we return the a greeting `Hello, <name>!`.
    """
    #   message is a variable recieved from the client. 
    #   'request' which is imported in the top access the data sent to this endpoint i.e., '/hello'.
    #   the `get_json` helps to pull the data in the form a json format.
    #   `force` is true, for always parse the JSON request for any data type. 
    message = request.get_json(force=True)
    #  `message` is expecting atleast one string from client called 'name'
    #  the message is stored in the name
    name = message['name']
    #  here the response is the form of a greeting
    response = {'greeting':'Hello,'+ name +'!'}
    
    #  Here this method returns the reponse is converted to JSON by jsonify 
    #  The JSON file is send to the client request

    return jsonify(response)
                          