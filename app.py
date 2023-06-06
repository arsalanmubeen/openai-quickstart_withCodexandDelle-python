from flask import Flask, request, render_template
import openai
import requests
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        prompt = request.form['prompt']
        generated_form = generate_form(prompt + ' FORM IN HTML CODE')
        generated_image = generate_image(prompt+ ' background image')
        return render_template('index.html', form=generated_form, image_url=generated_image)
    return render_template('index.html')

def generate_form(prompt):
    completion = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.6,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        best_of=1
    )
    generated_form = completion.choices[0].text.strip()
    return generated_form

def generate_image(prompt):
    completion = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = completion['data'][0]['url']
    return image_url

if __name__ == '__main__':
    app.run()

