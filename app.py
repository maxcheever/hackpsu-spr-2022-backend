from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json
from flask_cors import CORS

app = Flask(__name__)
json = FlaskJSON(app)
CORS(app)

@app.route("/")
def home():
    profs = [
        {'name':"Antonio Blanca",
         'rating':"3.3/5",
         'description':"I felt Np Complete after each of his lectures",
         'src':"ratemyprof/antonioblanca"
        },

        {'name':"David Kosclicki",
         'rating':"2.0/5",
         'description':"I thought professor koslicki was a nice guy. He actually incredibly incompetent!",
          'src':"ratemyprof/davidkosclicki"
        },

        {'name':"Yanling Wang",
         'rating':'0.5/5',
         'description':"I felt like I was being tortured. A hundred shivers ran down my spine, as if the devil himself appeared before me.",
          'src':"ratemyprof/yanlingwang"
        }
    ]

    return json_response(professors = profs, status=200)

key = '8a340f693d644fa1af78d87de98548c3'
endpoint = 'https://hackpsu-spr-2022.cognitiveservices.azure.com/'

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Authenticate the client using your key and endpoint 
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=ta_credential)
    return text_analytics_client

client = authenticate_client()


if(__name__=="__main__"):
    app.run()