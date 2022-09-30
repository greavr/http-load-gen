# http-load-gen
Http Load Gen

## Run Code Locally
```
pip3 install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
pip3 install -r src/requirements.txt
python3 src/main.py
```

**Deactivate the environment** 
Run the following command
```
deactivate
```
## Environment Variables ##
The following environment variables can be set:
  - **TARGET_URL** - REQUIRED, should be fully formed url, example: http://google.com
  - **AVERAGE_RPS** - Baseline request per second count, default is **10** (RPS)
  - **MAX_RPS** - Max request per second count, default is **100** (RPS)
  - **DURATION** - Time from Average to Max, default is **60** (in seconds)
  - **LOOPS** - INT Of number of cycles, defaults to **0** which is forever

