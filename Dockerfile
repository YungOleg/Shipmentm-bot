FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
COPY . .
# RUN alembic revision --m "main" --autogenerate
# RUN alembic upgrade head
# CMD ["python", "bot/__main__.py"]
ENTRYPOINT ["bot/__main__.py"]