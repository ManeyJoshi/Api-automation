1. API Automation (Playwright + Pytest)
Purpose
-To test the API endpoint https://jsonplaceholder.typicode.com/posts for correctness, data structure, and response time.
Tools:
-Python 3.13
-Pytest
-Playwright

-Tested API Endpoints
-GET /posts — retrieve all posts
-POST /posts — create a new post

Test Steps
-Setup Playwright API context with base URL.
-Run GET /posts request and validate:
-Status code = 200
-Response time < 2 seconds
-Response body is a list of dictionaries
-Each post contains userId, id, title, body
Run POST /posts request with payload:
{
  "userId": 1,
  "title": "Automated test post",
  "body": "This is a test post using Playwright + Pytest."
}
-Validate status code = 201
-Response time < 2 seconds
-Response body contains the same keys as payload

Results
-GET /posts returned 200 and valid data.
-POST /posts returned 201 with correct data.
-Response times were under 2 seconds.

Conclusion
-The API automation tests passed successfully. The endpoints return correct data and are fast.

2. JMeter Load Testing Report

Purpose
-The goal of this test was to see how well the API at https://jsonplaceholder.typicode.com/posts handles multiple users at the same time. We wanted to check its speed, stability, and whether it can manage high traffic without errors or delays.

Test Setup
-We used Apache JMeter to test the /posts endpoint. The test included both GET and POST requests. We ran the tests with two different user loads: 20 and 50 users.

For the setup:
-We created a test plan named API Load Test – JSONPlaceholder.
-Added a Thread Group to simulate multiple users.
-Configured the base URL for all HTTP requests.
-Added listeners like View Results Tree, Summary Report, and Graph Results to monitor performance.

Scenario 1 – 20 Users
-We first tested with 20 users. The ramp-up period was 10 seconds, and each user made one request.

Results & Observations:
-All 20 requests were successful, with 0% errors.
-The average response time was 68 milliseconds, and most requests finished in under 63 milliseconds.
-One request took 450 milliseconds, which was an unusual spike.
-Throughput and data transfer were stable, and there were no bottlenecks or timeouts.
-This shows the API handled moderate traffic very well.

Scenario 2 – 50 Users
-Next, we tested with 50 users, ramping up over 15 seconds. Each user made one request.
Results & Observations:
-All 50 requests were successful, again with 0% errors.
-Average response time slightly improved to 47 milliseconds, which means the API handled more users smoothly.
-Most requests finished under 57 milliseconds, with the slowest at 115 milliseconds.
-Throughput increased to 2.54 requests per second.
-This shows the API performed even better under higher load, staying fast and stable.

Conclusion

-Overall, the /posts API is stable, fast, and reliable. It handled both 20 and 50 concurrent users without any errors or performance issues. The response times were very low, and throughput scaled well with the number of users.

In short, this API can manage moderate to high traffic efficiently, making it dependable for real-world use.
