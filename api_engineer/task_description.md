
You need to create a script that will run a simple power flow calculation using pandapower https:// github.com/e2nIEE/pandapower and present its results via a REST API. The task is expected to take between 2-4 hours. 
You can find the Python module with the simulation code that you need to use here https://github.com/gridsingularity/interview_tasks/blob/master/api_engineer/test_sim.py. You do not need to create your own simulation script, you can use the one provided (test_sim.py), and only expose its results via a REST API. The only function that you will need to use is the run_simulation function, which performs the power flow calculation and returns a tuple, containing the active and reactive power of the load. The API that you will create will use these 2 values (active and reactive power).

The API needs to expose 3 endpoints:
1. POST request that launches the simulation using the aforementioned Python module. The response should include the active and reactive power of the load in JSON format
2. GET request that reads the active power of the previously executed simulation 
3. GET request that reads the reactive power of the previously executed simulation 

You can use any Python framework you like for the REST API (Flask, DRF, Bottle). The results of the past simulation runs (active/reactive power, and also the time that the simulation was launched) should be persisted in a database. 

Bonus points if you use GraphQL instead of REST for implementing the API. 

Also, the results of the simulation needs to be reported asynchronously whenever a new simulation is launched. In order to achieve that, a websocket needs to be created in order to send the updated active/reactive power values. Any webosocket library (e.g. Django Channels) is acceptable. The websocket should report the existing active/reactive power values on connect. When a new set of active/reactive values is generated a message should be sent through the websocket that reports the updated values. The format of the results should be JSON, same as the REST API. 

Finally, a Dockerfile has to be created that would install all the dependencies automatically and serve the API once the container is started. 

In order to submit your solution to this task a fork of this repo has to be created, and the solution can be committed to the fork. 
