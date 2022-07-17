from flask import Flask, render_template, request
from utils.search_trend import search

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def map_polygon():
    try:
        markers = search(request.form.get('trend'))
        return render_template('map.html', markers=markers)
    except KeyError:
        return render_template('map.html')


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')
