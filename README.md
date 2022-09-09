## About
JobBoard is a backend to handle logic that will power a job board website

## Architecture
The service implements `Clean Architecture` which helps to separate concerns by organizing code into several layers with a very explicit rule which enables us to create a testable and maintainable project.  [The Clean Architecture](https://blog.8thlight.com/uncle-bob/2012/08/13/the-clean-architecture.html). 


### The project will be divided into five layers:
#### 1. Presentation
This represents logic that consume the business logic from the `Usecase Layer`
and renders to the view. Here you can choose to render the view in e.g `rest` 

#### 2. Usecases
The code in this layer contains application specific business rules. 
This represents the pure business logic of the application.
The rules of the application also shouldn't rely on the UI or the persistence frameworks being used.

#### 3. Interfaces
Clean architecture dictates that dependandency should only point inwards therefore the inner layers(the usecase layer) should not have any idea of the implementations of the database, third party interactions. So this is just an interface.
This will ensures that the system is independent of a database and any third party agencies making it easier to switch them without affecting the business logic.

#### 4. Infrastructure
These are the `ports` that allow the system to talk to 'outside things' which
could be a `database` for persistence or a `web server` for the UI. None of
the inner use cases or domain entities should know about the implementation of
these layers and if we choose to change them they should not cause change to any of our business rules.

#### 5. Domain
Here we have `business objects` or `entities` and should represent and encapsulate the fundamental business rules.


## Technologies
 - Python3.8
 - FasAPI (https://fastapi.tiangolo.com/)

## How to use it

1. First clone the codefrom the repository 
```bash
    dev@dev:~$ git clone 
```
2. Create and activate a virtual environment:
 
   ```sh
   $ python3.8 -m venv venv && source venv/bin/activate
   ```
3. Install the requirements:

   ```sh
   (venv)$ pip install -r requirements.txt
   ```

4. Export the required env variables
   Make sure to explicitly export these variables when running locally to sign download urls else the app will break

   ```sh
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/key.json"
   export IS_LOCAL="true"
   ```
5. Run the server:
   ```sh
   (venv)$ uvicorn main:app
   ```

   ###### To run the application under a reload environment use -- reload

```sh
 $ uvicorn main:app --reload

```

Navigate to [http://localhost:8000](http://localhost:8000).


## Features
1. Create a user
2. Create a job post
3. Retrieve a job post given the id
4. Retrieve a list of jobs post
5. Update a job post
6. Delete a job post