FROM node:14
WORKDIR /app
COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["npm", "run", "start"]