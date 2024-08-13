import pandas as pd

import glide_data_grid as gdg

df = pd.DataFrame(
    [
        {
            "firstName": "John",
            "lastName": "Doe",
            "number": 100,
        },
        {
            "firstName": "Maria",
            "lastName": "Garcia",
            "number": 200,
        },
        {
            "firstName": "Nancy",
            "lastName": "Jones",
            "number": 300,
        },
        {
            "firstName": "James",
            "lastName": "Smith",
            "number": 400,
        },
    ]
)

column_config = [
    gdg.column_config.TextColumn("firstName", width=100),
    gdg.column_config.TextColumn("lastName", width=100),
    gdg.column_config.NumberColumn("number", width=100),
]

data = gdg.glide_data_grid(df=df, column_config=column_config, key="foo")
