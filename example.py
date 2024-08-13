from glide_data_grid import glide_data_grid
import pandas as pd


df = pd.DataFrame(
    [
        {
            "firstName": "John",
            "lastName": "Doe"
        },
        {
            "firstName": "Maria",
            "lastName": "Garcia"
        },
        {
            "firstName": "Nancy",
            "lastName": "Jones"
        },
        {
            "firstName": "James",
            "lastName": "Smith"
        }
    ]
)

columns = [
  { "title": "firstName", "width": 300 },
  { "title": "firstName", "width": 200 }
]



data = glide_data_grid(df=df, columns=columns, key="foo")
