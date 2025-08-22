Contributing to SahayaSoochi

Thank you for your interest in contributing to SahayaSoochi! 🙏
We’re building an AI-powered app to help people in Telangana and Andhra Pradesh easily generate official government application letters in Telugu and English.

Table of Contents

Code of Conduct

How Can I Contribute?

Development Setup

Making Changes

Submitting Changes

Style Guidelines

Community

Code of Conduct
Our Pledge

We pledge to make participation in SahayaSoochi a harassment-free experience for everyone, regardless of background, gender, language, or technical expertise.

Expected Behavior

Be respectful and inclusive

Welcome newcomers and help them get started

Respect cultural sensitivities, especially when handling Telugu government letter formats

Focus on constructive criticism

Give credit where it’s due

Unacceptable Behavior

Harassment or discrimination

Sharing offensive or inappropriate content

Trolling, insults, or derogatory remarks

Publishing others’ personal information without consent

How Can I Contribute?
1. 📝 Letter Templates

Add more official government application templates (Telugu + English)

Improve formatting and grammar in existing letters

Translate templates between Telugu and English

2. 🐛 Bug Reports

Check if the issue already exists before reporting

Include OS, browser, Streamlit version, and error messages

Bug report format:

Description

Steps to Reproduce

Expected Behavior

Actual Behavior

Screenshots (if applicable)

3. ✨ Feature Requests

Suggest new input modes (voice/video integration)

Recommend new letter categories (complaints, leave letters, applications, etc.)

Propose user experience improvements

4. 💻 Code Contributions

Areas we need help with:

Frontend: Streamlit UI improvements

Backend: Corpus collection, API integration

AI/ML: Improving template filling, Telugu NLP support

DevOps: Deployment on Hugging Face/GitLab CI/CD

Docs: Improving guides and tutorials

Development Setup
Prerequisites

Python 3.9+

Streamlit

Git

Local Setup
# Clone the repository
git clone https://code.swecha.org/Karthikeya_gundu/sahaya-soochi.git
cd sahaya-soochi

# Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

Making Changes
1. Fork and Branch
git checkout -b feature/your-feature-name

2. Development Workflow

Write clean, documented code

Update docs/templates when adding features

Keep commits focused and clear

3. Commit Messages

Use conventional commits:

feat: new feature

fix: bug fix

docs: documentation changes

style: formatting changes

test: testing additions

chore: maintenance

Submitting Changes

Keep your branch updated:

git fetch origin
git rebase origin/main


Push changes:

git push origin feature/your-feature-name


Create a Merge Request with:

Clear title & description

Reference to related issues

Screenshots/videos if UI changes

Test results if applicable

Style Guidelines
Python Style

Follow PEP8

Use type hints where possible

Keep functions small and readable

Streamlit Style

Keep components modular and reusable

Use session state for persistent user data

Follow Streamlit best practices

Documentation Style

Clear, simple language

Add code snippets where helpful

Keep README and docs updated

Community

Issues: Report bugs or request features

Discussions: Share ideas or improvements

Email: sahayasoochi-team@swecha.org

Contributors will be:

Listed in CONTRIBUTORS.md (future)

Mentioned in release notes

Appreciated in the community ❤️

💡 Together, let’s make SahayaSoochi the go-to app for official government application letters in Telugu and English! 🚀