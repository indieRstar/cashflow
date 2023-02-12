import json

from flask import Flask, request, make_response
from flask_restx import Api, Resource
from cashflow import predict

