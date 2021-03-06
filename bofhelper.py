from flask import Flask, render_template
app = Flask(__name__, static_url_path='', static_folder='web/static', template_folder='web/templates')   

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    try:
        app.run(host= '127.0.0.1', port=5000, debug=True)
    except Exception, e:
        print str(e)
