# Clasico

This is a Full Stack web application that compares statistics between different soccer players and teams.

We utilized several Python modules such as `matplotlib`, `pandas`, and `numpy` to perform the statistical analysis between two players or teams
and to customize the algorithm for player ratings.

We leveraged the `Django REST Framework` to create an API that connects our database to a `React/Redux` frontend. 

We cached API results from external soccer related APIs into `sqlite3` to reduce the number of calls and increase response time.

We used `AWS S3` and `boto3` to store the graphs created by `matplotlib`.

We containerized the backend using `Docker` and deployed the container to `Heroku`. Finally, we deployed the frontend to `Netlify`.
