# SahayaSoochi Deployment Guide

This guide provides instructions for deploying the SahayaSoochi app on different platforms.

## Local Development Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Microphone access (for voice recording feature)

### Installation Steps

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd sahayasoochi_voice_app
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Access the app**
   - Open your browser and go to `http://localhost:8501`
   - The app should now be running locally

## Docker Deployment

### Using Docker

1. **Create a Dockerfile**
   ```dockerfile
   FROM python:3.9-slim
   
   WORKDIR /app
   
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   
   COPY . .
   
   EXPOSE 8501
   
   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Build and run the Docker container**
   ```bash
   docker build -t sahayasoochi .
   docker run -p 8501:8501 sahayasoochi
   ```

## Cloud Deployment Options

### Streamlit Cloud (Recommended)

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository and main branch
   - Set the path to your app: `app.py`
   - Click "Deploy"

### Heroku

1. **Create a `Procfile`**
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. **Create `setup.sh`**
   ```bash
   mkdir -p ~/.streamlit/
   echo "\
   [server]\n\
   headless = true\n\
   port = $PORT\n\
   enableCORS = false\n\
   \n\
   " > ~/.streamlit/config.toml
   ```

3. **Deploy to Heroku**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### Google Cloud Platform

1. **Create `app.yaml`**
   ```yaml
   runtime: python39
   
   entrypoint: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   
   env_variables:
     STREAMLIT_SERVER_PORT: 8501
   ```

2. **Deploy to GCP**
   ```bash
   gcloud app deploy
   ```

## Environment Variables

You can configure the app using environment variables:

```bash
export STREAMLIT_SERVER_PORT=8501
export STREAMLIT_SERVER_ADDRESS=0.0.0.0
export STREAMLIT_SERVER_HEADLESS=true
```

## Troubleshooting

### Common Issues

1. **Audio recording not working**
   - Ensure microphone permissions are granted
   - Check if `sounddevice` and `soundfile` are properly installed
   - On some systems, you may need to install additional audio libraries

2. **Speech recognition errors**
   - Internet connection required for Google Speech Recognition
   - Check if the language code "te-IN" is supported
   - Consider using offline speech recognition for better privacy

3. **Port already in use**
   ```bash
   # Kill existing process
   lsof -ti:8501 | xargs kill -9
   
   # Or use a different port
   streamlit run app.py --server.port=8502
   ```

4. **Dependencies installation issues**
   ```bash
   # Upgrade pip
   pip install --upgrade pip
   
   # Install with verbose output
   pip install -r requirements.txt -v
   ```

### Performance Optimization

1. **For production deployment**
   - Use a production WSGI server like Gunicorn
   - Enable caching for better performance
   - Consider using a CDN for static assets

2. **Memory optimization**
   - Limit the number of concurrent users
   - Implement session cleanup
   - Monitor memory usage

## Security Considerations

1. **Data privacy**
   - The app saves user data locally in CSV and JSON files
   - Consider implementing data encryption
   - Implement user authentication if needed

2. **Input validation**
   - Validate all user inputs
   - Sanitize text inputs to prevent injection attacks
   - Implement rate limiting

3. **File permissions**
   - Ensure proper file permissions for generated files
   - Implement secure file handling

## Monitoring and Logging

1. **Add logging to the app**
   ```python
   import logging
   
   logging.basicConfig(level=logging.INFO)
   logger = logging.getLogger(__name__)
   ```

2. **Monitor app performance**
   - Track response times
   - Monitor error rates
   - Set up alerts for critical issues

## Backup and Recovery

1. **Regular backups**
   - Backup `corpus.csv` and `letter_history.json` files
   - Implement automated backup scripts
   - Store backups in secure locations

2. **Disaster recovery**
   - Document recovery procedures
   - Test backup restoration
   - Maintain multiple backup copies

## Support and Maintenance

1. **Regular updates**
   - Keep dependencies updated
   - Monitor for security vulnerabilities
   - Update letter templates as needed

2. **User support**
   - Provide clear documentation
   - Set up user feedback channels
   - Monitor user issues and requests

For additional support, please refer to the main README.md file or create an issue in the project repository. 