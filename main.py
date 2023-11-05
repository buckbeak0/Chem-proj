from flask import Flask, request, render_template
import periodictable
import wikipediaapi

app = Flask(__name__)

wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent="YourAppName/1.0 (your@email.com)"  # Replace with your app name and email
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    atomic_number = int(request.form['atomicNumber'])
    
    if atomic_number > 118:
        return "Element Not Found. <a href='/'>Go Back</a>"

    element = periodictable.elements[atomic_number]

    # Retrieve element properties
    name = element.name.capitalize()
    symbol = element.symbol
    atomic_mass = element.mass
    atomic_number = element.number

    # Fetch a summary from Wikipedia
    page = wiki_wiki.page(name)
    summary = page.summary

    return render_template('element.html', name=name, symbol=symbol, atomic_mass=atomic_mass, atomic_number=atomic_number, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
