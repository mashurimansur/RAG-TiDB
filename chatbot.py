import mysql.connector
import json
import ollama

from sentence_transformers import SentenceTransformer

OLLAMA_HOST = "http://localhost:11434"
OLLAMA_MODEL = "deepseek-llm:latest"

llm_agent = ollama.Client(host=OLLAMA_HOST)
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

def search_document(database, query, top_k=5):
    result = []

    embbedding_list = embbedder.encode(query).tolist()
    embbedding_str = json.dumps(embbedding_list)

    curr = db.cursor()

    sql_query = f"""
        SELECT text, vec_cosine_distance(embedding, %s) AS distance 
        FROM documents
        ORDER BY distance ASC
        LIMIT {top_k}
    """

    curr.execute(sql_query, (embbedding_str,))
    search_result = curr.fetchall()

    database.commit()
    curr.close()

    for result in search_result:
        text,distance = result
        result.append({
            'text': text,
            'distance': distance
        })
    
    return result

def response_query(database, query):
    retreived_docs = search_document(database, query)

    context = "\n".join([doc['text'] for doc in retreived_docs])
    prompt = f"Answer the question based on the context below.\n\nContext: {context}\n\nQuestion: {query}\n\nAnswer:"
    response = llm_agent.chat(model=OLLAMA_MODEL, messages=[{"role": "user", "content": prompt}])

    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    print("Chatbot is running...")
    while True:
        query_text = input("Prompt: ")

        if query_text.lower() in ['exit', 'quit', 'q']:
            print("Exiting chatbot.")
            break

        response = response_query(database=db, query=query_text)
        print("Response:", response)

print("Chatbot terminated.")