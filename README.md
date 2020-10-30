# DirectLineGroup
Direct Line Insurance Group PLC

## Software engineer python test
Create a REST endpoint that return the sum of a list of numbers e.g. [1,2,3] => 1+2+3 = 6 You are free to use any
Python 3 framework, however, try and keep the usage of the third- party library to a minimum.

The list of numbers is expected to arrive from a backend service and for this test you can hard code the list using
the following line.
```:python
numbers_to_add = list(range(10000001))
```

The url of the endpoint and the sample response is as follows:
Request: http://localhost:5000/total

Response:
```
{
 "total": 6
}
```

Please provide the source code, tests, documentations and any assumptions you have made.
Note: We are looking for the candidate’s “Software Engineering” ability not just the Python programming skills.

## Environment
To set up the working environment the following commands must be run:

```bash
$ pip install -r requirements.txt
$ pip install -r requirements-test.txt
```

## Tests
This application benefits from `pytest` tests. To run the tests:
```bash
$ pytest tests
```

## Postman
Under `DirectLineGroup/postman` there is a file `DirectLineGroup-postman_collection.json` ready to be imported
into Postman to run manual tests.