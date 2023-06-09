# Базовый образ
FROM python:3.8-slim-buster
 
# Установка зависимостей
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt
 
# Копирование исходного кода
COPY . /app
 
# Команда для запуска приложения
CMD ["streamlit", "run", "/app/app.py", "--server.port", "8501"]
