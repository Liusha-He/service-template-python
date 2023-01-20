# Entity Extraction API

## Introduction

This repo implements an entity extraction API using poetry and FastAPI.


## Build 

To install poetry and all dependencies locally, you just need to run

```shell
$ make build
```

## Test

To run the unit tests, you just need to run

```shell
$ poetry run python nltk_data_init.py
$ make unit-test
```

## Local run

To run the app locally, you can run

```shell
$ make run
```

## Run with Docker compose

there's is a local-compose.yaml to let you extend the app with other services, such as database, load balancer, etc.

## Contribute

Before commit and push your changes, make sure you run the following

```shell
$ make lint
% make format
```
