import os
from neo4j import GraphDatabase

HOST = os.environ['NEO4J_HOST']

def connect(func):
    def func_wrapper(*args, **kwargs):
        driver = GraphDatabase.driver(
            f'neo4j://{HOST}',
            auth=('neo4j', 'SmellyRhino@89')
        )
        return func(driver, *args, **kwargs)
    return func_wrapper
