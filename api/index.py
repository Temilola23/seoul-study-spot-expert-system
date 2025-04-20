from flask import Flask, request, render_template
from pyswip import Prolog
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.abspath(os.path.join(base_dir, '..', 'templates'))
static_dir = os.path.abspath(os.path.join(base_dir, '..', 'static'))

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

prolog = Prolog()

# Load expert system
KB_PATH = os.path.join(os.path.dirname(__file__), "..", "study_system.pl")
prolog.query(f'consult("{KB_PATH}")')


@app.route("/")
def home():
    return render_template("index.html")


def format_fallback_results(raw_list, user_inputs):
    formatted = []
    for score, name, link, explanation in raw_list:
        summary, _, match_bar = compute_match_info(user_inputs, score, explanation)
        formatted.append({
            "name": name,
            "score": score,
            "link": link,
            "summary": summary,
            "match_bar": match_bar,
            "explanation": [e.strip() for e in explanation.split(".") if e.strip()]
        })
    return formatted


@app.route("/search", methods=["POST"])
def search():
    data = request.form
    mode = data.get("mode")
    
    query = ""  # build based on mode and inputs
    if mode == "strict":
        query = f"""
        recommend_spot(
            {data['origin']},
            {data['max_minutes']},
            {data['work_type']},
            {data['outlet_pref']},
            {data['vibe_pref']},
            {data['seating_pref']},
            {data['price_pref']},
            {data['open_late']},
            Name, Link)
        """
        results = list(prolog.query(query))
        return render_template("results.html", results=results, mode="strict")

    else:  # fallback
        query = f"""
        find_top_study_spots(
            {data['origin']},
            {data['max_minutes']},
            {data['travel_weight']},
            {data['work_type']}, {data['work_weight']},
            {data['outlet_pref']}, {data['outlet_weight']},
            {data['vibe_pref']}, {data['vibe_weight']},
            {data['seating_pref']}, {data['seating_weight']},
            {data['price_pref']}, {data['price_weight']},
            {data['open_late']}, {data['late_weight']},
            "{data['explain_mode']}",
            {data['top_n']},
            Results)
        """
        raw_results = list(prolog.query(query))
        if raw_results:
            formatted_results = format_fallback_results(raw_results[0]["Results"], data)
        else:
            formatted_results = []
        return render_template("results.html", results=formatted_results, mode="fallback")


if __name__ == "__main__":
    app.run(debug=True)
