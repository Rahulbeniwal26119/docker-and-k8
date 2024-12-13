FROM php:7.4-fpm-alpine

WORKDIR /var/www/html

RUN docker-php-ext-install pdo pdo_mysql

COPY src .

RUN chown -R www-data:www-data /var/www/html
