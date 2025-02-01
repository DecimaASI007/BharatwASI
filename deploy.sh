#!/bin/bash
docker build -t bharatwasi .
docker run -d -p 8000:8000 --name bharatwasi_container bharatwasi
