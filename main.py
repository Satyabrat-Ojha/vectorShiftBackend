from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import json

from is_dag import is_dag

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/pipelines/parse')
def parse_pipeline(pipeline: str = Form(...)):
    try:
        # Parse the JSON string into a Python dictionary
        pipeline_data = json.loads(pipeline)
        nodes = pipeline_data.get('nodes', [])
        edges = pipeline_data.get('edges', [])
        
        # Validate input types
        if not isinstance(nodes, list) or not isinstance(edges, list):
            return {"error": "Invalid input format. 'nodes' and 'edges' must be lists."}

        # Return the required information
        return {
            'num_nodes': len(nodes),
            'num_edges': len(edges),
            'is_dag': is_dag(nodes, edges)
        }
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format for pipeline."}
