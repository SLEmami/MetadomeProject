from flask import render_template, request

def add_routes(app):
    @app.route('/', methods=['GET'])
    def home():
        return render_template('index.html')

    @app.route('/query', methods=['POST'])
    def query():
        user_input = request.form.get('user_input')
        # Here you can handle the user input, for example, print it
        print(user_input)
        return 'Query received: ' + user_input