<h1 align="center">Docker System Dashboard</h1>
<h4 align="center">A speed dial for your server</h4>
<p align="center">
  <a href="/LICENSE.md"><img src="https://img.shields.io/github/license/bearlike/docker-web-dashboard.svg?color=blue"></a>
  <a href="https://deepsource.io/gh/bearlike/docker-web-dashboard/?ref=repository-badge" target="_blank"><img alt="DeepSource" title="DeepSource" src="https://deepsource.io/gh/bearlike/docker-web-dashboard.svg/?label=active+issues&show_trend=true"/></a>
</p>


 ## Getting Started
 Execute `build-run.sh` to automatically build and deploy the container. Default Username is `admin` and Password is `admin`.
 ```bash
 git clone https://github.com/bearlike/docker-web-dashboard.git
 cd docker-web-dashboard
 bash build-run.sh
 ```


## Configuration via environment variables
- `DASH_USERNAME` (default: admin) Name of the Dashboard user.
- `DASH_PASSWORD` (default: admin) Password for the Dashboard user.
- `OWNER_URL` (Optional) Specify the URL for the owner's profile 


## Questions / Issues
If you got any questions or problems using the image, please visit our [Github Repository](https://github.com/bearlike/docker-web-dashboard/) and write an [issue](https://github.com/bearlike/docker-web-dashboard/issues).


## Acknowledgments
- [Bootstrap Login Page Template](https://github.com/nauvalazhar/bootstrap-4-login-page)
- Hat tip to anyone whose code was used.


<p align="center">
  Made with ❤️ by <a href="https://github.com/bearlike">Krishna Alagiri</a>
</p>