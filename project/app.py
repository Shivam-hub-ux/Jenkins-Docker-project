from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to My CI/CD Project!</h1>
    <h2>GitHub + Jenkins + Docker</h2>
    <p>Application deployed successfully!</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
