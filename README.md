# Journal-Rank
Journal-Rank


Work-in-progress website that allows users to submit opinion reviews for academic journals.
Far from complete, but does have basic, unpolished functionality now. Progress on this project can be tracked by
setting up on Linux with the following:

1. Cloning repo.
2. Installing requirements `$pip install -r requirements.txt`
3. Run the setup script to setup redis `$bash setup.sh`
4. Setup up flask recaptcha w/ google recaptcha (https://www.youtube.com/watch?v=VrH0eH4nE-c)
5. Enter the private and public key for recaptcha in config.py 
6. Add gmail username and password to config.py (optional, but required for login, will require allowing your gmail to use less secure apps https://support.google.com/accounts/answer/6010255?hl=en)
7. Running the Flask app `$flask run`

Which launches the landing page:

![picture alt](/readme_images/index.png)

Users can register with a .edu containing email and leave ratings for journals, which are logged in a database.

![picture alt](/readme_images/journal_info.png)



References:

SCImago, (n.d.). SJR — SCImago Journal & Country Rank [Portal]. Retrieved 12/14/18, from http://www.scimagojr.com
