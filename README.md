1. After downloading use `git submodule init` and `git submodule update`
2. `pip install -r requirements.txt`
3. `pip install pip install "uvicorn[standard]"`
4. [Install redis](https://redis.io/docs/getting-started/) and make sure redis-server is running in port 6379
5. Set environment variables `RAPIDAPI_HOST` and `RAPIDAPI_KEY`
6. `uvicorn main:app --reload`

Application can now be accessed in localhost:8000
