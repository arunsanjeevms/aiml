from flask import Flask, render_template, request
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(hi|hello|hey)",
        ["Hello! How can I assist you today?", "Hi there! What can I help you with?"]
    ],
    [
        r"(what are the library hours|library hours)",
        ["The library at M.Kumarasamy College of Engineering is open from 8 AM to 8 PM on weekdays and 9 AM to 5 PM on weekends."]
    ],
    [
        r"(where is m\.kumarasamy college located|location of mkce|college location)",
        ["M.Kumarasamy College of Engineering is located in Thalavapalayam, Karur, Tamil Nadu, India."]
    ],
    [
        r"(what courses are offered|coursesoffered|departments)",
        ["MKCE offers a variety of courses, including B.E., B.Tech., M.E., MBA, and Ph.D. programs in disciplines like Computer Science, Mechanical Engineering, and Civil Engineering."]
    ],
    [
        r"(what is the admission process|admission process)",
        ["The admission process at MKCE involves applying through TNEA for undergraduate courses and GATE/TANCET for postgraduate programs."]
    ],
    [
        r"(hostel facilities|is there a hostel|hostel details)",
        ["Yes, MKCE provides hostel facilities for boys and girls with amenities like Wi-Fi, mess, and security."]
    ],
    [
        r"(placement opportunities|placements)",
        ["MKCE has an excellent placement record with top recruiters like TCS, Wipro, Infosys, and Cognizant visiting the campus every year."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't have information on that. Can you try rephrasing your question?",
         "Please contact the admin office for further assistance."]
    ]
]

chatbot = Chat(pairs, reflections)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def chatbot_response():
    user_input = request.args.get('msg') 
    response = chatbot.respond(user_input)
    return response

if __name__ == "__main__":
    app.run(debug=True)
