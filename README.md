# Mtcars-Flask-Api - Nils Berzins

Inside this repository includes the flask server script (server.py) along with the linear regression and prediction script (model.py).These scripts were deployed to a docker image which was then pushed to Google's cloud run through a docker hub repository.  

To standup the API and interact with the mtcars linear regression prediction, use the curl command below (feel free to alter the predictor values to your liking). 


curl -X POST https://mtcars-flask-api-173754053169.us-west1.run.app/predict_mpg   -H "Content-Type: application/json"   -d '{"cyl":6,"disp":160,"hp":110,"drat":3.9,"wt":2.62,"qsec":16.46,"vs":0,"am":1,"gear":4,"carb":4}'

**Output for the above command:**

"predicted mpg: ": 22.599505761262385



