"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.0
"""

from kedro.pipeline import Pipeline, node, pipeline
from desafio_ds_transito.pipelines.data_processing.nodes import preprocess_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_data,
                inputs="traffic",
                outputs="preprocessed_traffic",
                name="preprocessed_traffic_node"
            )
    ])
