from faker import Faker
import pandas as pd
import pyarrow

fake = Faker()
#doesn't repeat values
fake.unique;

# Generate a dataset
num_employees = 100
data = []
for _ in range(num_employees):
    #modify the following fields for the schema you want your fake dataset to have
    data.append({
        'employee_id': fake.random_int( min= 1, max= num_employees),
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'department_id': fake.random_int(1, 10),
        'salary': fake.random_int(min = 50000, max=350000),
        'hired_date': fake.date()
    })

df = pd.DataFrame(data)
#output as .csv
#df.to_csv('output.csv', index=False)

#parquet compression options: snappy, gzip
df.to_parquet('output.parquet',compression='snappy')