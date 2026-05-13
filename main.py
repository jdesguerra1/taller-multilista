try:
    from flask import Flask, render_template
except ImportError:
    raise ImportError("Flask is not installed. Please install it with: pip install flask")

if __name__ != '__main__':
    import sys
    sys.exit(1)

app=Flask(__name__)
@app.route('/')
def root():
    markers=[
        {
        'lat':0,
        'lon':0,
        'popup':'This is the middle of the map.'
        }
    ]
    return render_template('index.html',markers=markers )
if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)