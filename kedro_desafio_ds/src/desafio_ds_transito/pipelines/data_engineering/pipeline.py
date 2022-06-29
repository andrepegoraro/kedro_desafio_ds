"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.0
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import encode_variable


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=encode_variable,
            inputs="preprocessed_traffic",
            outputs=[
                "encoded_traffic_dataset", 
                "label_encoder"
            ]
        ),

    ])
