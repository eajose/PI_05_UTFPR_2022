from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return "Homepage"


@app.route('/inicio')
def map_polygon():
    markers=[
        {
        'lat':-1.397746, 
        'lon':-48.473087,
        'popup':'This is the middle of the map.'
        }
    ]
    return render_template('map.html', markers=markers)


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')
