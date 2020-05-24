FROM python:3.8-slim
RUN pip install --no-cache-dir matplotlib pandas

FROM mongo:latest

CMD [ "python" ]