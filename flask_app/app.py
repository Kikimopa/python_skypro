import utils
from flask import Flask

candidates = utils.load_file()

app = Flask(__name__)

def handle_bad_request():
    return 'такой страницы не существует', 400

app.register_error_handler(404, handle_bad_request())

@app.route("/")
def page_index():
     output = "<pre>\n"
     for candidate in candidates:
         output += f"{candidate['name']}\n"
         output += f"{candidate['position']}\n"
         output += f"{candidate['skills']}\n"
         output+= "\n"

     output += "<pre>\n"
     return output


@app.route("/candidate/<int:id>/")
def page_candidate(id):
    output = "<pre>\n"
    for candidate in candidates:
        if candidate["id"] == id:
            output += f"<img src = {candidate['picture']}\n"
            output += f"{candidates[id]['name']}\n"
            output += f"{candidates[id]['position']}\n"
            output += f"{candidates[id]['skills']}\n"
            output += "<pre>\n"
    return output

@app.route("/skills/<skill>")
def page_skills(skill):
    output = "<pre>\n"
    flag = False
    for candidate in candidates:
        if skill.lower() in candidate["skills"].lower().split(", "):
            flag = True
            output += f"{candidate['name']}\n"
            output += f"{candidate['position']}\n"
            output += f"{candidate['skills']}\n<pre>\n"
    if flag == False:
        output+= "Ничего не найдено =(<pre>\n"
    return output

app.run()