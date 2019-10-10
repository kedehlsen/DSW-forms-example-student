from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    favorite_color = request.args['color'] #get user's input for color input
    if (favorite_color == "green") or (favorite_color == "Green"):
           response = "That's my favorite color, too!"
    elif(favorite_color == "blue") or (favorite_color == "Blue"):
           response =  "Talk about overrated."
    else:
           response = "That's cool. My favorite color is green."
    return render_template('response.html', responseFromServer=response)
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
