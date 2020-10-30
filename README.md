# FyberTest
Python Flask & Jenkins for Covid-19 statistics.

I wrote app.py file written in Python and service with Flask.

The service will:

    ● Response with JSON format on any request (support error handling).
    
    ● Scrapes data from an external free API https://corona.lmao.ninja to retrieve Covid-19 data.
    
    ● Serves 4 endpoints:
        ○ newCasesPeak function - Returns the date and value of the highest peak of new
          Covid-19 cases in the last 30 days for a required country.
        ○ recoveredPeak function - Returns the date and value of the highest peak of recovered
          Covid-19 cases in the last 30 days for the required country.
        ○ deathsPeak function - Returns the date and value of the highest peak of death Covid-19
          cases in the last 30 days for a required country.
        ○ dataFromDic function - help function that calculates the max value and return of each case 
        the data in json format.
        ○ status function - Returns a value of success/fail to contact the backend API.
        
    Examples:    
    When you run the service from PyCharm use commands on the terminal: 
    curl localhost:8080/status
    curl localhost:8080/newCasesPeak?country=israel (or any other country)
    curl localhost:8080/recoveredPeak?country=israel (or any other country)
    curl localhost:8080/deathsPeak?country=israel (or any other country)
    
   BE AWARE! 
   
   If you run the app.py file from cmd using a Flask the port is: 5000
   
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In addition I want to create a jenkins job using a Jenkinsfile.

The Jenkinsfile will query my service with several country values. The request to the service &
results for each of the queries will be shown on the job console view in jenkins.
