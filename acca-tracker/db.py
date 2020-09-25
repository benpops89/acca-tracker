import os
from neo4j import GraphDatabase

def connect(func):
    def func_wrapper(*args, **kwargs):
        driver = GraphDatabase.driver(
            f'neo4j://neo4j:7687',
            auth=('neo4j', 'SmellyRhino@89')
        )
        return func(driver, *args, **kwargs)
    return func_wrapper
