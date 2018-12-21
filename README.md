# Journal-Rank
Journal-Rank


Work-in-progress website that allows users to submit opinion reviews for academic journals.
Far from complete, but does have basic, unpolished functionality now. Progress on this project can be tracked by
setting up on Linux with the following:

1. Cloning repo.
2. Installing requirements `$pip install -r requirements.txt`
3. Setting Flask environment variable: `$export FLASK_APP=journal-rank.py`
4. Running the Flask app `$flask run`

Which launches the landing page:

![picture alt](/readme_images/index.png)

Users can register with a .edu containing email and leave ratings for journals, which are logged in a database.

![picture alt](/readme_images/journal_info.png)



References:

SCImago, (n.d.). SJR — SCImago Journal & Country Rank [Portal]. Retrieved 12/14/18, from http://www.scimagojr.com
