# adding docker file for node
FROM node:18.14.1-buster-slim

WORKDIR /frontend

COPY ./package.json ./

RUN npm install

COPY . ./

# RUN npm run build

EXPOSE 3000

CMD ["npm", "run", "start"]