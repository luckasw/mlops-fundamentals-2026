# What I did

I cleaned up the work directory by moving everything into its appropriate folders, like data,models,scripts and reports. I also had to move the code out of jupyter notebooks for it to be usable in the pipeline.

Then i created a basic dvc.yaml without params and ran it with dvc repro. After some changes to the model building function i added params. 

After installing dvclive i tried running experiments. This is i think the best part to see how cool dvc really is and makes it all come together.

Finally i setup a backblaze bucket and pushed everything there.

# What I learned

I learned how to use DVC, which is git for large files basically, and have version control for data and models. How to use DVC to create a end to end pipeline for a machine learning project. Also how to make the pipeline easily manageable/testable with paramaters. Lastly of course I learned how to store all this data in a bucket system on backblaze.

# Best experiment
| pred_time  | r2      | rmse    | training_time |
|------------|---------|---------|---------------|
| 1.02568    | 0.86324 | 5.09258 | 29.87686      |

[Repo](https://github.com/luckasw/mlops-fundamentals-2026)
