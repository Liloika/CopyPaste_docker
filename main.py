from flask import Flask, request, redirect, url_for
import uuid

app = Flask(__name__)

storage = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        paste_id = str(uuid.uuid4())[:8]
        storage[paste_id] = text
        return f'Your text is available at: {request.host_url}{paste_id}'
    return '''
        <form method="post">
            <textarea name="text"></textarea><br>
            <button type="submit">Save</button>
        </form>
    '''

@app.route('/<paste_id>')
def get_paste(paste_id):
    text = storage.pop(paste_id, None)
    if text is None:
        return 'Text not found or already deleted.', 404
    return f'<pre>{text}</pre>'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
