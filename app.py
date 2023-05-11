from flask import Flask, render_template, request, jsonify
import openai
openai.api_key = ""

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/email-generator')
def email_generator():
    return render_template('email-generator.html')


def email_writer(recipient, addressor, style, content):
    prompt = f'Please write an email for me. The recipient is {recipient}.The addressor is {addressor}. The style of email is {style}. The content is {content}.'
    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        max_tokens=250
    )
    email = response['choices'][0]['message']['content']
    return email


@app.route('/generate-email', methods=['POST'])
def generate_email():
    data = request.json
    recipient = data['recipient']
    addressor = data['addressor']
    style = data['style']
    content = data['content']

    # Generate email based on input data
    email = email_writer(recipient, addressor, style, content)

    # Return generated email as JSON response
    return jsonify({'email': email})


if __name__ == '__main__':
    app.run(debug=True)
