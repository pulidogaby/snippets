from faker import Faker
import pandas as pd
import pyarrow

fake = Faker()
#use .unique to avoid duplicate values
#fake.unique;

# Generate a dataset of size max_num
max_num = 100
data = []
for _ in range(max_num):
    #modify the following fields for the schema you want your fake dataset to have
    data.append({
        'employee_id': fake.unique.random_int( min= 1, max= num_employees),
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
