You need [docker](https://docs.docker.com/get-docker/) and[docker-compose](https://docs.docker.com/compose/install/) to run this project.

1. After downloading use `git submodule init` and `git submodule update`
2. Use `python.env.SAMPLE` to create a `python.env` file and set variable `RAPIDAPI_KEY`
3. `docker-compose build && docker-compose run --rm web makemigrations && docker-compose run --rm web migrate`
4. Use `docker-compose up` to run the project

