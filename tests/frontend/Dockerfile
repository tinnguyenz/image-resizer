FROM node:14

WORKDIR /app

COPY tests/frontend/package.json ./

RUN npm install

COPY . .

EXPOSE 4000

CMD [ "npm", "test" ]