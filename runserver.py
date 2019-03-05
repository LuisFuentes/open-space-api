#!flask/bin/python
from webapp import webapp
# Run in Dev/Testing
webapp.run(debug=True) #Runs locally, private
# Run in Production
#app.run(host='0.0.0.0', port=5000) #Runs externally, public
