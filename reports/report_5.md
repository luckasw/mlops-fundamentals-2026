# What we did

We created a simple flask app that connects to a mongo db if specified. We dockerize the project with a dockerfile. Then we can spin up a couple containers making sure they are in the same network: Mongo container, mongo-express container and one for our flask app. To make deployment more convenient we created a docker compose file. In the compose file it is also convenient to define volumes for the data.

When all that was done we uploaded the image to the UT-s registry.

# What i learned 

Well I would say I was comfortable with docker before this class. That being said it is always good to go over the basics. So it was a pleasant refresher for all the steps that I have completed quite a few times before.
