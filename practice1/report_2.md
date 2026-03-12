# Data version control

I use local storage with dvc as dvc is blocked by google.

# Testing model on new data

### New scores

RMSE - 4.228507841631464

R2 score - 0.9040582693131516

### Old scores

RMSE - 5.209677543060735

R2 score - 0.8563294462847166

It seems that the model still performs well on totally new data which is good.

# Training new rfr model on v2 data

### V2 model scores trained on v2 data

RMSE - 5.128875116435849

R2 score - 0.8588510938751694

Having more training data has not improved the model. 

# Version 3 deployment

a) I would monitor the input features and look out for data drift and retrain the model when new data starts looking a different from training data.

b) I would keep and eye on the RMSE metric.

c) Average prediction times and if these go too high compared to previous models i would rollback or retrain the model.
