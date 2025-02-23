# CopyPaste

A simple service for storing text snippets. Built with Flask and Docker.

## How it works
1. Paste your text into the form.
2. Get a unique link.
3. The text is automatically deleted after being viewed.

## Requirements
Install: 
[Docker](https://docs.docker.com/get-docker/)
[Docker Compose](https://docs.docker.com/compose/install/).

##Start the containers
'docker-compose up -d'

##Configuration
1. Edit nginx.conf to configure Nginx.
2. Use Certbot for HTTPS.

##Open in your browser
'http://your-domain.com'
