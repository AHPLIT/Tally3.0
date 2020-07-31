#!/bin/bash
app="tally3"
docker kill ${app}
docker rm ${app}
