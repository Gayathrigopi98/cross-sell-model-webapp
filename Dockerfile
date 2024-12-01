FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 82

ENTRYPOINT ["streamlit" , "run" , "webview.py" , "--server.port=82" , "--server.address=0.0.0.0"]

