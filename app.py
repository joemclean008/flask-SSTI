from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['input']
        template = '''
                    <form action="/" method="post">
                        <input name="input" type="text">
                        <input name="submit" type="submit">
                    </form>
                    <h1>Hello, %s  !</h1>
                    ''' % name
        return render_template_string(template)
    else:
        template = '''
                    <form action="/" method="post">
                        <input name="input" type="text">
                        <input name="submit" type="submit">
                    </form>
                    '''
        return render_template_string(template)


if __name__ == '__main__':
    app.run()
