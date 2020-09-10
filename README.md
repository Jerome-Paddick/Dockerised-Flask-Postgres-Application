

To RUN:

1. docker-compose up -d --build
2. docker exec -it flask-app sh  
3. python dbmanager.py db upgrade
4. python dbmanager.py populate_db
5. Head over to -> http://localhost:5000/api/api_documentation.html

---
Improvements

Obviously theres much that could be done to improve this, but short of turning it into a fully fledged application, I would add:
 - Users, and seperate gift lists
 - Authentication 
 - A central logging system instead of returning errors from api endpoints, 
 - an actual server program like nginx instead of the basic flask dev server
 - a better understanding of fine tuned functionality (eg. can a user delete a purchased gift)
 - a persistent volume for the postgres server (Im on a windows machine atm and its a pain to create a docker postgres volume with a windows filesystem)
 - auto-scaling, high availability, and a custom url on AWS for example
 - better more integrated tests
 - Passing in sensetive data (DB connection info) using environment variables instead of hard coding
 
 ---
 Tests
 
 - run "python tests/psycopg2_connection_test.py" to test db connection
 - run "pytest" to automatically run tests in test/test_endpoints.py
 