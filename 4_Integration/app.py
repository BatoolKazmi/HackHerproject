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

# def get_specific_response(prompt):
#     if "hello" in prompt.lower():
#         return "Hello, my name is Amy, how can I help?"
#     elif "I suffered through a hate crime today" in prompt.lower():
#         return "I'm so sorry to hear that! This is a very unfortunate incident and it is unacceptable.\nHate crimes are illegal, unethical, and hurtful acts that can have a significant impact on the mental and physical well-being of the victims. \nI can offer some resources if you need support, but please know that you are not alone, and there are many organizations and people who can help and provide assistance. \nPlease consider reaching out to the police and reporting this crime. There are also organizations that provide crisis support, and I can help you find some, like National Hate Crimes Hotline - a safe and confidential space to report hate crimes and receive support. \nRemember, you are not alone, and I'm here to help you find the right resources.  Please do not hesitate to ask if there is any support I can help source."
#     elif "Can you please give me some recourses" in prompt.lower():
#         return "Absolutely! I can provide you with some resources and also guide you to some support systems. I will provide some general resources, but these may not be specific to your situation, and I recommend tailoring resources to your specific needs. Here are some resources: \n1. National Hate Crimes Hotline: 1-800-222-5468 \n2. Anti-Defamation League (ADL): This organization provides support and education to fight discrimination and hate. \n3. Southern Poverty Law Center: This is an organization dedicated to fighting white supremacy, hate, and bigotry through legal action, education, and advocacy. \n4. Report Hate Crimes to the FBI: The FBI takes hate crime reports very seriously and can be contacted to report any incidents. \n5. National Alliance on Mental Illness (NAMI): This organization provides support and resources for mental health issues, which can be very helpful in dealing with the trauma of hate crimes. \n6. Crisis Text Line: Texting 741741 will connect you with a crisis counselor for support.\nRemember, you are not dealing with this alone; there are many people and organizations that can help.  I recommend reaching out to a few of these organizations; they can provide both immediate and long-term support and resources.\nPlease feel free to ask any further questions about accessing these resources and any other support you may need.  It is important to seek help and utilize these resources as soon as possible."
#     elif "bikini bottom" in prompt.lower():
#         return "Bikini bottom is like my home. I live in it."
#     elif "will smith" in prompt.lower():
#         return "Will Smith more like Won't Smith."
#     else:
#         return "I'm sorry, I don't have a specific response for that."

def get_specific_response(prompt):
    respond_crime = ["report", "hatecrime", "suffered"]
    respond_sources = ["give", "resources", "help", "sources"]

    if "hello" in prompt.lower():
        return "Hello, my name is Amy, how can I help?"
    elif "I suffered through a hate crime today" in prompt.lower():
         return "I'm so sorry to hear that! This is a very unfortunate incident and it is unacceptable.\nHate crimes are illegal, unethical, and hurtful acts that can have a significant impact on the mental and physical well-being of the victims. \nI can offer some resources if you need support, but please know that you are not alone, and there are many organizations and people who can help and provide assistance. \nPlease consider reaching out to the police and reporting this crime. There are also organizations that provide crisis support, and I can help you find some, like National Hate Crimes Hotline - a safe and confidential space to report hate crimes and receive support. \nRemember, you are not alone, and I'm here to help you find the right resources.  Please do not hesitate to ask if there is any support I can help source."

    prompt_list = prompt.lower().split(" ")

    count = 0
    for a in range(len(respond_crime)):
        count = count+1

    count2 = 0
    for a in range(len(respond_sources)):
        count = count+1
   
   
    if ("hello" in prompt_list) and (count == 0) and (count2 == 0):
            return "Hello, my name is Amy, how can I help?"
    
    for a in range(len(respond_crime)):
        if (respond_crime[a] and "i") in prompt_list:
            return "I'm so sorry to hear that! This is a very unfortunate incident and it is unacceptable." + "\n Hate crimes are illegal, unethical, and hurtful acts that can have a significant impact on the mental and physical well-being of the victims." + "\n I can offer some resources if you need support, but please know that you are not alone, and there are many organizations and people who canelp and provide assistance."+"\n Please consider reaching out to the police and reporting this crime. There are also organizations that provide crisis support, and I can help you find some, like National Hate Crimes Hotline - a safe and confidential space to report hate crimes and receive support."
    
    for a in range(len(respond_sources)):  
        if (respond_sources[a]) in prompt_list:
            return ("Absolutely! I can provide you with some resources and also guide you to some support systems. I will provide some general resources, but these may not be specific to your situation, and I recommend tailoring resources to your specific needs. Here are some resources: \n1. National Hate Crimes Hotline: 1-800-222-5468 \n2. Anti-Defamation League (ADL): This organization provides support and education to fight discrimination and hate. \n3. Southern Poverty Law Center: This is an organization dedicated to fighting white supremacy, hate, and bigotry through legal action, education, and advocacy."
                    "\n4. Report Hate Crimes to the FBI: The FBI takes hate crime reports very seriously and can be contacted to report any incidents. \n5. National Alliance on Mental Illness (NAMI): This organization provides support and resources for mental health issues, which can be very helpful in dealing with the trauma of hate crimes."
                    "\n6. Crisis Text Line: Texting 741741 will connect you with a crisis counselor for support.\nRemember, you are not dealing with this alone; there are many people and organizations that can help.  I recommend reaching out to a few of these organizations; they can provide both immediate and long-term support and resources. "
                    "\nPlease feel free to ask any further questions about accessing these resources and any other support you may need.  It is important to seek help and utilize these resources as soon as possible.")

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