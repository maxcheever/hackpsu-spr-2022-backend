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

def sentiment_analysis_example(client):

    documents = [
        "He would have gotten a 3/5 but since the average is bad, I have curved his rating to 4/5. Just like he curved the final by 13% (actual number remains a mystery). This is one of those classes where the effort you put in does not seem proportional to your grade. However, if you put in the work you will pass.",
        "I agreed with the one star comment below. Although the final curve for this class was 23%, there were still so many people did not pass.",
        "Simple, bad professor with notes, final exam average was 52/111, which is 46%. You need a C for graduation, which is 70 %. He didn't curve the grades even a bit. He's a nice person, but pretty bad at teaching.",
        "Failed it with a D. Guess going to take Mingfu next semester.",
        "The most recent 1 star reviews are giving him poor rating because of how the course is set up and not his actual teaching. He is an amazing lecturer and is very clear when explaining concepts. He always makes sure that students understand his lectures. I do agree that it's annoying that they are not telling us the curve until after finals.",
        "He curved the entire class for 15 percent so I was able to pass with a C+. That's why I'm going to curve his rating as well.",
        "David is decent at lecturing material for this class, but the curriculum is extremely tough and many of the homework questions and curriculum are taken straight from Berkeley's CS170's course. He also does not give out any grading scale or any hint of a curve. For context, David taught CMPSC 360, where the final average was 59 percent and he curved 1%.",
        "Amazing lectures. Promised with a 15 percent class curve and is really funny when it comes to algorithms. A true professor that cares about academic and people.",
        "The homeworks are tough and not related to the lectures. For the second homework, I spent too much time on it and as a result I fell behind on everything else. The office hours are useless too. I don't know how the TAs did well. I literally can't sleep worrying that I will fail",
        "Would not recommend this professor for future students when taking 360 and 465. Although he is a good teacher, the curriculum is very tough. The tests are 74 percent of our grade and the homeworks are very difficult. Took him for 360 as well and received a 1 percent curve with an impossible final. If you slip up in this class you are done."
        ]
        
    response = client.analyze_sentiment(documents=documents)
    j = 1
    for i in response:
        print(f'Sentence {j}:')
        print("Sentiment: {}".format(i.sentiment))
        print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
            i.confidence_scores.positive,
            i.confidence_scores.neutral,
            i.confidence_scores.negative,
        ))
        j += 1

    full = [' '.join(documents)] 
    
    fullText = client.analyze_sentiment(documents=full)[0]
    print("Document Sentiment: {}".format(fullText.sentiment))
    print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
        fullText.confidence_scores.positive,
        fullText.confidence_scores.neutral,
        fullText.confidence_scores.negative,
    ))
          
sentiment_analysis_example(client)


# if(__name__=="__main__"):
#     app.run()