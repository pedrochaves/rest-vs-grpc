FROM php:7.1-cli

ADD ./ /app
WORKDIR /app

RUN apt-get update && \
    apt-get install -y git-core php-pear zlib1g-dev zip unzip automake autoconf autogen libtool shtool && \
    apt-get clean
RUN pecl install grpc && \
    docker-php-ext-enable grpc

# Sets up composer
RUN curl -sS https://getcomposer.org/installer | php
RUN mv /app/composer.phar /usr/local/bin/composer
RUN chmod +x /usr/local/bin/composer
