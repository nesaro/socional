import subprocess
from collections import defaultdict
from fastapi import FastAPI, HTTPException

app = FastAPI()

PATH = ''

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/doc/{item_id}")
async def read_item(item_id):
    try:
        print(f'{PATH}/{item_id}.md')
        with open(f'{PATH}/{item_id}.md') as f:
            return {"content": f.read()}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Item not found")

@app.get("/search/")
async def search(q: str = None):
    completed_process = subprocess.run(f'ag {q} {PATH}',
                                       capture_output=True,
                                       check=True,
                                       shell=True)
    content = completed_process.stdout.decode()
    entries = content.split('\n')
    results = defaultdict(list)
    for entry in entries:
        first_colon_index = entry.find(':')
        results[entry[:first_colon_index]].append(entry[first_colon_index+1:])
    return {"content": results}
