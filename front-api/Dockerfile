FROM node:16-alpine

# Wrking directory to /app
WORKDIR /app

COPY package.json .

# Install the dependencies
RUN npm install
RUN apk add --no-cache curl

COPY . .

# ENV variable for The Photos API URL
#ENV FLASK_API_URL=http://flask-api:3000

# Expose port 4000 for the API
EXPOSE 4000

# Start the front API
CMD [ "npm", "start" ]
