import pandas as pd

import pandas_profiling

import streamlit as st

from streamlit_pandas_profiling import st_profile_report

from pandas_profiling import ProfileReport





df = pd.read_csv("crop_production.csv", na_values=['='])




profile = ProfileReport(df,

                        title="Agriculture Data",

        dataset={

        "description": "This profiling report was generated for Personal Studies",

        "copyright_holder": "Shivpal Wadkar",

        "copyright_year": "2023",

        "url": "https://www.gmail.com",

    },

    variables={

        "descriptions": {

            "State_Name": "Name of the state",

            "District_Name": "Name of district",

            "Crop_Year": "Year when it was seeded",

            "Season": "Crop year",

            "Crop": "Which crop was seeded?",

            "Area": "How much area was allocated to the crop?",

            "Production": "How much production?",


        }

    }

)


st.title("Pandas Profiling in Streamlit!")

st.write(df)

st_profile_report(profile)