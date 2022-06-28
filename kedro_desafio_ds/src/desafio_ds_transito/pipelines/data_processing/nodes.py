"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.0
"""
import pandas as pd

def change_names_module(df, col_names):
    df.rename(columns = col_names, inplace=True)

def change_to_category(df):
    df = df.astype('category')
    return df

def parse_percentage(df):
    df = df.div(100)
    return df

def preprocess_data(traffic: pd.DataFrame) -> pd.DataFrame:
    """
    This function processes the data to make it better to be analyzed

    Args:
        traffic: raw data.
    Returns:
        Preprocessed data with:
            - All column names changed;
            - The right column types converted into category types;
            - `slowness_in_traffic` variable converted into percentage without "%";

    """
    change_names_module(traffic, 
                        col_names = {    
                            "Hour..Coded.": "hour_coded", 
                            "Immobilized.bus": "immobilized_bus",
                            "Broken.Truck": "broken_truck",
                            "Vehicle.excess": "vehicle_excess",
                            "Accident.victim": "accident_victim",
                            "Running.over": "running_over",
                            "Fire.vehicles": "fire_vehicles",
                            "Occurrence.involving.freight": "freight_occurrence",
                            "Incident.involving.dangerous.freight": "dangerous_freight_incident",
                            "Lack.of.electricity": "lack_of_electricity",
                            "Fire": "fire",
                            "Point.of.flooding": "point_of_flooding",
                            "Manifestations": "manifestations",
                            "Defect.in.the.network.of.trolleybuses": "trolleybus_deffect",
                            "Tree.on.the.road": "tree",
                            "Semaphore.off": "semaphore_off",
                            "Intermittent.Semaphore": "intermittent_semaphore",
                            "Slowness.in.traffic....": "slowness_in_traffic"
                        })
    traffic["hour_coded"] = change_to_category(traffic["hour_coded"])
    traffic["vehicle_excess"] = change_to_category(traffic["vehicle_excess"])
    traffic["freight_occurrence"] = change_to_category(traffic["freight_occurrence"])
    traffic["dangerous_freight_incident"] = change_to_category(traffic["dangerous_freight_incident"])
    traffic["fire"] = change_to_category(traffic["fire"])

    traffic["slowness_in_traffic"] = parse_percentage(traffic["slowness_in_traffic"])

    return traffic
    
