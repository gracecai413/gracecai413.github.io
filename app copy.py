from flask import Flask, render_template, request
import openai
openai.api_key = "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"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Call your Python script to process the input and get the output
# Replace this with your own code
output = response['choices'][0]['message']['content']
@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.form['user_input']
    
    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ],
        temperature=0,
    )
    # Call your Python script to process the input and get the output
    # Replace this with your own code
    output = response['choices'][0]['message']['content']
    
    return output

if __name__ == '__main__':
    app.run(debug=True)
