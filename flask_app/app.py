import utils
from flask import Flask, render_template

candidates = utils.load_file()

app = Flask(__name__)

def handle_bad_request():
    return 'такой страницы не существует', 400

app.register_error_handler(404, handle_bad_request())

@app.route("/")
def page_index():
     return render_template("candidate_list.html", item=candidates)


@app.route("/candidate/<int:id>/")
def page_candidate(id):
    candidate = utils.get_candidate(id)
    return render_template("card.html", item=candidate)

@app.route("/search/<name>/")
def page_search_by_name(name):
    candidates = utils.get_candidates_by_name(name)
    return render_template("search.html", items=candidates, len=len)

@app.route("/skills/<skill>")
def page_skills(skill):
    candidates = utils.get_candidates_by_skill(skill)
    return render_template("skills.html", items=candidates, len=len)


app.run()
