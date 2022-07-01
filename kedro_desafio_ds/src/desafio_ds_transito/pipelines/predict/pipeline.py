"""
This is a boilerplate pipeline 'predict'
generated using Kedro 0.18.0
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import batch_predict

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = batch_predict,
            inputs = ['model_regressor', 'X_test', 'label_encoder'],
            outputs = 'predictions',
            name = "batch_predict"
        )
    ])
