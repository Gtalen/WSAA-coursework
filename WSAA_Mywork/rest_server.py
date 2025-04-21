# flask lab

# very simple flask server

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
        return "Hello Mamm\zdf\sdfy"

@app.route('/blah2')
def blah():
        return "this is blah2"


#mapping 

@app.route('/books', methods=['GET'])
def getall():
       return "get all books"

@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id): 
       return f"find by id {id}"

#create 
@app.route('/books', methods=['POST']) 
def create(): 
        # read json from the body 
        #jsonstring = request.json 
        return "create a book" #
        





if __name__ == "__main__":
    app.run(debug = True)
