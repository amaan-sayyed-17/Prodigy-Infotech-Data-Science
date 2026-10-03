import glob
import os
from collections import Counter

import pandas as pd


CHUNK_SIZE = 100_000
OUTPUT_DIR = "task05_outputs"


def find_dataset():
    candidates = glob.glob("/kaggle/input/**/US_Accidents_March23.csv", recursive=True)
    if candidates:
        return candidates[0]
    local = "US_Accidents_March23.csv"
    if os.path.exists(local):
        return local
    raise FileNotFoundError(
        "US_Accidents_March23.csv not found. Add the Kaggle US Accidents (2016-2023) dataset."
    )


def main():
    dataset_path = find_dataset()
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    severity = Counter()
    hours = Counter()
    weekdays = Counter()
    months = Counter()
    states = Counter()
    cities = Counter()
    weather = Counter()
    road_features = Counter()
    hotspots = Counter()

    total_rows = 0
    missing_start_time = 0
    missing_weather = 0
    distance_sum = 0.0
    distance_count = 0
    state_values = set()
    city_values = set()
    weather_values = set()

    feature_cols = [
        "Traffic_Signal", "Junction", "Crossing", "Stop", "Give_Way",
        "Railway", "Roundabout", "No_Exit", "Bump"
    ]

    for chunk in pd.read_csv(dataset_path, chunksize=CHUNK_SIZE, low_memory=False):
        total_rows += len(chunk)

        start = pd.to_datetime(chunk["Start_Time"], errors="coerce")
        missing_start_time += int(start.isna().sum())
        valid_start = start.notna()
        hours.update(start[valid_start].dt.hour.astype(int).tolist())
        weekdays.update(start[valid_start].dt.day_name().tolist())
        months.update(start[valid_start].dt.month_name().tolist())

        if "Severity" in chunk:
            severity.update(chunk["Severity"].dropna().astype(int).tolist())

        if "State" in chunk:
            vals = chunk["State"].dropna().astype(str)
            states.update(vals.tolist())
            state_values.update(vals.unique())

        if "City" in chunk:
            vals = chunk["City"].dropna().astype(str)
            cities.update(vals.tolist())
            city_values.update(vals.unique())

        if "Weather_Condition" in chunk:
            wc = chunk["Weather_Condition"]
            missing_weather += int(wc.isna().sum())
            vals = wc.dropna().astype(str)
            weather.update(vals.tolist())
            weather_values.update(vals.unique())

        if "Distance(mi)" in chunk:
            d = pd.to_numeric(chunk["Distance(mi)"], errors="coerce")
            distance_sum += float(d.sum())
            distance_count += int(d.notna().sum())

        for col in feature_cols:
            if col in chunk:
                values = chunk[col]
                if values.dtype == bool:
                    mask = values.fillna(False)
                else:
                    mask = values.fillna(False).astype(str).str.strip().str.lower().isin(
                        ["true", "1", "yes", "y"]
                    )
                road_features[col] += int(mask.sum())

        if {"Start_Lat", "Start_Lng"}.issubset(chunk.columns):
            lat = pd.to_numeric(chunk["Start_Lat"], errors="coerce").round(2)
            lng = pd.to_numeric(chunk["Start_Lng"], errors="coerce").round(2)
            valid = lat.notna() & lng.notna()
            hotspots.update(zip(lat[valid], lng[valid]))

    def write_counter(counter, name, key_name, value_name, sort=False):
        rows = counter.most_common() if sort else sorted(counter.items(), key=lambda x: x[0])
        pd.DataFrame(rows, columns=[key_name, value_name]).to_csv(
            os.path.join(OUTPUT_DIR, name), index=False
        )

    write_counter(hours, "accidents_by_hour.csv", "Hour", "Accident_Count")
    write_counter(weekdays, "accidents_by_weekday.csv", "Day", "Accident_Count")
    write_counter(months, "accidents_by_month.csv", "Month", "Accident_Count")
    write_counter(severity, "severity_distribution.csv", "Severity", "Accident_Count")
    write_counter(states, "top_states.csv", "State", "Accident_Count", sort=True)
    write_counter(cities, "top_cities.csv", "City", "Accident_Count", sort=True)
    write_counter(
        weather, "top_weather_conditions.csv", "Weather_Condition", "Accident_Count", sort=True
    )
    write_counter(road_features, "road_features.csv", "Road_Feature", "Accident_Count", sort=True)

    hotspot_rows = [
        (lat, lng, count) for (lat, lng), count in hotspots.most_common(50)
    ]
    pd.DataFrame(
        hotspot_rows,
        columns=["Latitude", "Longitude", "Accident_Count"]
    ).to_csv(
        os.path.join(OUTPUT_DIR, "top_accident_hotspots.csv"),
        index=False
    )

    summary = pd.DataFrame(
        [
            ["Total records processed", total_rows],
            ["Missing Start_Time", missing_start_time],
            ["Missing Weather_Condition", missing_weather],
            ["Unique States", len(state_values)],
            ["Unique Cities", len(city_values)],
            ["Unique Weather Conditions", len(weather_values)],
            [
                "Average Accident Distance (miles)",
                round(distance_sum / distance_count, 3) if distance_count else None,
            ],
        ],
        columns=["Metric", "Value"],
    )
    summary.to_csv(os.path.join(OUTPUT_DIR, "eda_summary.csv"), index=False)

    print("Processing complete")
    print(summary.to_string(index=False))

    print("\nTop states:")
    print(
        pd.DataFrame(
            states.most_common(10),
            columns=["State", "Accident_Count"]
        ).to_string(index=False)
    )

    print("\nTop weather conditions:")
    print(
        pd.DataFrame(
            weather.most_common(10),
            columns=["Weather_Condition", "Accident_Count"]
        ).to_string(index=False)
    )


if __name__ == "__main__":
    main()
