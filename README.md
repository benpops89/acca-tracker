# acca-tracker
Keep track of NFL bets

## Build
Clone the repository and run `docker-compose build` to build the docker images

## Deployment
To bring the docker containers up run `docker-compose up -d`

## Getting bets from SkyBet
There are two types of accas that can be retrieved from SkyBet
1. Open Bets
2. Settled Bets

### Open Bets
To retrieve open bets issue the following curl request
```
curl -X POST http://<ip_address>:5000/bets \
-H 'Content-Type: application/json; charset=utf-8' \
-d @- << EOF

{
    "username": "<skybet username>",
    "pin": "<skybet pin>"
}
EOF
```

### Settled Bets
To retrieve settled bets issue the following curl request
```
curl -X POST http://<ip_address>:5000/bets \
-H 'Content-Type: application/json; charset=utf-8' \
-d @- << EOF

{
    "username": "<skybet username>",
    "pin": "<skybet pin>",
    "period": "<period>"
}
EOF
```

where period is the month and year specified in the YYYY-MM format e.g. 2018-10

## Bet Response
The cURL request will respond with a job id, as the actual process of getting the bets is sent off to a worker. To check if the worker has finished go to `http://<ip_address>:5000/results/<job_id>`. If the bet has been retrieved it will be displayed. However, if the bet is still processing then that reponse will be **Nay!** If the bet is not ready refresh the page every 10 seconds to keep checking