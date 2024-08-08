import streamlit as st
from src.auth.profile import profile

def logout():
  if st.session_state.logged_in:
    profile()
    if st.button("Log out"):
      st.session_state.logged_in = False
      st.rerun()

logout_page = st.Page(logout, title="My Profile", icon=":material/account_circle:")
sign_up_page = st.Page("src/auth/signup.py", title="Sign up", icon=":material/person_add:")

# /apps
dashboard = st.Page("src/apps/dashboard.py", title="Dashboard", icon=":material/dashboard:")

# /apps/pages/automations
websites = st.Page("src/apps/pages/automations/website.py", title="Websites", icon=":material/web:")

# /apps/pages/models
chatBotModels = st.Page("src/apps/pages/models/chatBotModel.py", title="Chat Bot Models", icon=":material/smart_toy:")
healthCareModels = st.Page("src/apps/pages/models/healthCareModel.py", title="Health Care Models", icon=":material/health_and_safety:")

# /apps/pages/programs
simplePrograms = st.Page("src/apps/pages/programs/simpleProgram.py", title="Simple Programs", icon=":material/emoji_objects:")
apiPrograms = st.Page("src/apps/pages/programs/apiProgram.py", title="API Programs", icon=":material/api:")
imagePrograms = st.Page("src/apps/pages/programs/imageProgram.py", title="Image Programs", icon=":material/image:")
games = st.Page("src/apps/pages/programs/games.py",title="Games",icon=":material/casino:")
studyPrograms = st.Page("src/apps/pages/programs/studyProgram.py", title="Study Programs", icon=":material/school:")

# /apps/pages/contributors
contributors = st.Page("src/apps/pages/contributors.py", title="Contributors", icon=":material/people:")

def load_functions():
  pages = {
    "": [dashboard],
    "Account": [logout_page],
    "Automations": [websites],
    "Models": [chatBotModels, healthCareModels],
    "Programs": [apiPrograms, games, imagePrograms, simplePrograms, studyPrograms],
    "Contributors": [contributors],
  }

  return pages
