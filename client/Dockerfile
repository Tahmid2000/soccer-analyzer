FROM node:14.4.0-alpine3.10
WORKDIR /usr/src/app

COPY package*.json ./

# Installing dependencies
RUN npm install --silent

# Copy files over
COPY . .

# Expose port
EXPOSE 3000

CMD [ "npm", "start" ]