FROM node:14 as client
WORKDIR /client
COPY ./client/package*.json .
RUN npm install
COPY ./client .
ENV HOST=https://appfast.herokuapp.com

FROM python:3.8-slim-buster
WORKDIR /app
COPY ./server/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY --from=client /client/build /client/build
COPY ./server/src .
ENV ENIVORNMENT=production
ENV HOST=https://appfast.herokuapp.com
CMD ["python3", "main.py"]