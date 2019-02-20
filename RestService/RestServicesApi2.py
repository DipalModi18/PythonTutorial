from flask import Flask, jsonify, request, redirect, url_for

app = Flask(__name__)
app.config["DEBUG"] = True
# while the application is under development, it should be restarted manually for each change in the code.
#  To avoid this inconvenience, enable debug support.


books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, '
                       'the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

# The route() function of the Flask class is a decorator,
#       which tells the application which URL should call the associated function.


@app.route('/', methods=['GET'])
def trialMethod():
    return """<h1>Hello world</h1>"""


@app.route('/books/all', methods=['GET'])
def getall():
    # jsonify function that allows us to convert lists and dictionaries to JSON format.
    return jsonify(books)


@app.route('/book', methods=['GET'])  # 127.0.0.1:5000/api/v1/resources/book?id=0
def bookById():
    if'id' in request.args:
        id = int(request.args['id'])
    else:
        return "No ID provided"
    print('Requested book: ', id)
    results = []
    for book in books:
        print(book['id'])
        if book['id'] == id:
            results.append(book)

    return jsonify(results)


@app.route('/book/<int:bookid>', methods=['GET'])  # 127.0.0.1:5000/api/v1/resources/book?id=0
def bookById2(bookid):
    print('Requested book: ', bookid)
    results = []
    for book in books:
        if book['id'] == bookid:
            results.append(book)

    return jsonify(results)


@app.route('/greetme/<name>', methods=['GET'])  # default string variable part
def greetings(name):
    return "<h3>Hello " + name + "</h3>"


@app.route('/getbook/<quantity>', methods=['GET'])
def getBook(quantity):
    if quantity == 'all':
        return redirect(url_for('getall'))
    elif quantity == 'one':
        return redirect(url_for('bookById', id=1))
    # url_for() function is very useful for dynamically building a URL for a specific function.
    # The function accepts the name of a function as first argument,
    # and one or more keyword arguments, each corresponding to the variable part of URL.


# Data received by POST method is not cached by server.
@app.route('/addbook', methods=['POST'])
def createBook():
    print('Got request to add book: ', request.args)
    books.append({
        'id': request.args['id'],
         'title': request.args['title'],
        'author': 'Samuel R. Delany',
        'first_sentence': 'to wound the autumnal city.',
        'published': '1975'})
    return jsonify(books)


@app.route('/getpost', methods=['GET', 'POST'])
def getORpost():
    if request.method == 'GET':
        return "<h3>In GET</h3>"
    elif request.method == 'POST':
        return "<h3>In POST</h3>"


@app.errorhandler(404)
def pageNotFound(e):
    return "<h1>The resource could not be found</h1>"


app.run(port='8000')
