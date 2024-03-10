from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('index.html')

prompts = []

@app.route('/chat', methods=('GET', 'POST'))
def chat():
    return render_template('chat.html', prompts=prompts)

@app.route('/sign-up', methods=('GET', 'POST'))
def login():
    return render_template('login.html', prompts=prompts)

@app.route('/about', methods=('GET', 'POST'))
def about():
    return render_template('about.html', prompts=prompts)

def get_specific_response(prompt):
    if "money" in prompt.lower():
        return "Yes, I love money."
    elif "spongebob" in prompt.lower():
        return "Spongebob is a sponge."
    elif "crabby patties" in prompt.lower():
        return "You wanna help me make some crabby patties?"
    elif "bikini bottom" in prompt.lower():
        return "Bikini bottom is like my home. I live in it."
    elif "will smith" in prompt.lower():
        return "Will Smith more like Won't Smith."
    else:
        return "I'm sorry, I don't have a specific response for that."

@app.route('/get_response', methods=['GET'])
def get_response():
    if request.method == 'GET':
        rp = request.args["roleplaying"]
        prompt = request.args["msg"]
        print(prompt)
        print(rp)

        result = get_specific_response(prompt)

        prompts.append(prompt)
        prompts.append(result)

        return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)