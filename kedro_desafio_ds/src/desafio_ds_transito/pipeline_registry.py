"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline
from desafio_ds_transito.pipelines import data_processing
from desafio_ds_transito.pipelines import data_engineering as de
from desafio_ds_transito.pipelines import data_science as ds
from desafio_ds_transito.pipelines import data_science

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    data_processing_pipeline = data_processing.create_pipeline()
    data_engineering_pipeline = de.create_pipeline()
    data_science_pipeline = ds.create_pipeline()

    return {"dp": data_processing_pipeline,
            "de": data_engineering_pipeline,
            "ds": data_science_pipeline,
            "prepare_and_engineer": (data_processing_pipeline+data_engineering_pipeline),
            "__default__": data_processing_pipeline + data_engineering_pipeline + data_science_pipeline
    }
