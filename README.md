# Docker System Dashboard
 A speed dial for your server

 ## Getting Started
 ```bash
 git clone https://github.com/bearlike/docker-web-dashboard.git
 cd docker-web-dashboard
 docker build -t krishna/docker-system-dash .
 docker run -d -t --name cluster-dash-dev01 -p 26689:80 krishna/docker-system-dash
 ```
