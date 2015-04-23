from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the <a href='/hello'>home page</a>."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi There!</title>
        </head>
        <body>
            <h1>Hi There!</h1>
            <form action="/greet">
                <label>What's your name? <input type="text" name="person"></label><br>
                <label>Compliment: 
                    <select name="compliments">
                        <option value="awesome">awesome</option>
                        <option value="terrific">terrific</option>
                        <option value="fantastic">fantastic</option>
                        <option value="neato">neato</option>
                        <option value="fantabulous">fantabulous</option>
                        <option value="wowza">wowza</option>
                        <option value="oh-so-not-meh">oh-so-not-meh</option>
                        <option value="brilliant">brilliant</option>
                        <option value="ducky">ducky</option>
                        <option value="coolio">coolio</option>
                        <option value="incredible">incredible</option>
                        <option value="wonderful">wonderful</option>
                        <option value="smashing">smashing</option>
                        <option value="lovely">lovely</option>
                    </select></label><br>
                    and
                        <input value="smelly" name="insult" type="radio">smelly
                        <input value="ugly" name="insult" type="radio">ugly
                        <input value="terrible" name="insult" type="radio">terrible
                        <input value="no good" name="insult" type="radio">no good
                        <input value="gross" name="insult" type="radio">gross
                        <input value="yucky" name="insult" type="radio">yucky
                        <input value="bleh" name="insult" type="radio">bleh
                        <input value="meh" name="insult" type="radio">meh
                        <input value="grimy" name="insult" type="radio">grimy
                        <input value="slimy" name="insult" type="radio">slimy
                        <input value="too loud" name="insult" type="radio">too loud
                        <input value="gnarly" name="insult" type="radio">gnarly
                        <input value="annoying" name="insult" type="radio">annoying
                        <input value="negative" name="insult" type="radio">negative
                <br><br>
                      <label>What's your favorite color? <input type="text" name="color"></label>    
                <br>
                <input type="submit">

            </form>
        </body>
    </html>

    """

@app.route('/greet')
def greet_person():
    player = request.args.get("person")
    compliment = request.args.get("compliments")
    insult = request.args.get("insult")
    colorchoice = request.args.get("color")   
    # AWESOMENESS = [
    #     'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    #     'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    # compliment = choice(AWESOMENESS)

    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>A Compliment</title>
            # <style>
            #     body{
            #         color: %s; % colorchoice
            #     }
            # </style>
        </head>
        <body>
            Hi %s I think you're %s and %s!
        </body>
    </html>""" % (player, compliment, insult)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
