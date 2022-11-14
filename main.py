from app import app


@app.route('/api/saludo')
def saludo():
    return "hola todos"

if __name__=="__main__":
    #app.run()
    app.run(debug=True)