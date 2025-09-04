import json
import pandas as pd
import mysql.connector

from sentence_transformers import SentenceTransformer

# cretea instance for embbeding model
embbedder = SentenceTransformer('BAAI/bge-m3')

db = mysql.connector.connect(
  host = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
  port = 4000,
  user = "38UoY8RWEAyV3Pi.root",
  password = "3mz9K3klHbILQFPv",
  database = "RAG",
  ssl_ca = "./ca.pem",
  ssl_verify_cert = True,
  ssl_verify_identity = True
)

curr = db.cursor()

# read data from csv
df = pd.read_csv('data_knowledge.csv')

for index, row in df.iterrows():
    text = str(row['question']) + " " + str(row['answer'])
    
    try:
        embbedding_list = embbedder.encode([text])[0].tolist()
        embbedding_str = json.dumps(embbedding_list)

        sql_query = """
            INSERT INTO documents (text, embedding) VALUES (%s, %s)
        """
        curr.execute(sql_query, (text, embbedding_str))
        print(f"Inserted row {index} into the database.")
    except Exception as e:
        print(f"Error processing row {index}: {e}")


db.commit()
curr.close()
print("success insert all data")