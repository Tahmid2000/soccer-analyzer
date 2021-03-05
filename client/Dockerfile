FROM node:14.4.0-alpine3.10
USER root
WORKDIR /frontend

COPY . /frontend

# Installing dependencies
RUN npm install --silent
RUN npm run build

# Expose port
# EXPOSE 3000

# CMD [ "npm", "start" ]