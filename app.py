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

if(__name__=="__main__"):
    app.run()