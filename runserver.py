from webapp import application

if __name__ == '__main__':
    # Added guard block to prevent multiple
    # instances of flask from running
    #app.run(host='0.0.0.0')
    application.run()