# sage-challenge


This project is part of the Sage Makers Challenge.


###### MAIN ROUTES

1.a GET  /jokes/

1.b GET  /jokes/{joke_source}

1.c POST /jokes/

1.d PUT /jokes/{joke_id}

1.e DELETE /jokes/{joke_id}

2.a GET /nums/lcm/
2. b GET /nums/next/

To interact and see more details about this endpoints (what can be done with them and which are their query and body params), 
please go to the docs section at http://{...}/docs.


###### SET UP the project

There are two ways to run the project in order to be able to use this api.

1. It can be done with Uvicorn. Open your console, clone this repo,
   go to the root folder and in the console follow these steps:

  a. Create a virtualenvironment 
      ``` python3 -m venv env ```
  b. Install the required packages, listed in requirements.txt
      ``` pip install -r requirements.txt ```
  c. In the root folder of the project create an .env file with the following constants. First one
     let the project initialize, while the second connects with the Mongo DB (invited user credentials provided).
      
      PROJECT_NAME = "SageMakersChallenge"
      MONGO_URL = "mongodb+srv://invited:pJuCaIBrq7TeqXTL@clusterh.338j7rl.mongodb.net/?retryWrites=true&w=majority"

  d. Run uvicorn in the console with the following command:
      ``` uvicorn src.main:app --reload ```
  e. Now you can go to localhost:8000/docs to see details about the API
     and interact with the endpoints.
     
     
2. It is also possible to run the project with Docker.

  a. Download the image from docker hub: ``` docker pull horaciochiarella/sage-challenge:latest ````
  b. Execute the image with ``` docker run -d --name mycontainer -p 80:80 horaciochiarella/sage-challenge ```
  

###### What else?

There are many features that could be implemented and that would improve the project in a very significative way. 
Next I summarize a list with the most important ones:


###### Tests Suite

The nest big step would be to have all this endpoints, services and queries tested.
- Unit tests to test Routes, helpers and well some services.
- Integration tests repositories and some services.

It could be used pytest library to execute the tests, and coverage library to know how much of our code is test covered.


###### Endpoints & Routes

- The endpoints that get jokes about chuck norris and dads could be improved to use all the functionalities that this third party apis offer
  (like searching by category or by text).
- There is no endpoint to get the jokes stored in the sqlite database.
- More sophisticades schemas and validations could be appliead at many part of the code.
- More exceptions could be catched, and more personalized messages could be offered for some errors. 


###### Databases

- The sqlite database should be improved to a postgress version.
- Ids in sqlite could be managed with UUID library in postgres.
- Database models are very poor, and Schemas as well. A table for the source of joke could be added and new attributes could be added to
  the joke table. For instance, there is no check to know the joke is repeated, so the same joke can be stored many many many times 
  ('till is not funny anymore!)
- Bulk Operations could be added, as far as only is possible to work with one object at the moment.


As it is clear there are many improvement opportunitites. But the implementation is enough to show how many things can be done in so many different ways.
Please, in case of any doubt don't hesitate to write me at horacio.chiarella@gmail.com

