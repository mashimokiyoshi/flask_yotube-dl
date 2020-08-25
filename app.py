from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from download import download

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def downloads():
    url = request.form.get('url')
    filename = request.form.get('filename')
    ismp3 = request.form.get('ismp3')


    if url == '':
        error = 'urlを入力してください'
        return render_template('index.html', errorMsg=error)
    elif filename == '':
        error = '保存ファイル名を入力してください'
        return render_template('index.html', errorMsg=error)

    dobject = download(url, filename, ismp3)
    result = dobject.execute()

    return result

def page_not_found(error):
    return render_template('page_not_found.html'), 500

app.register_error_handler(500, page_not_found)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)
