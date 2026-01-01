# multi-objective-network-routing

**Implementation of multi-objective shortest path methods, including scalar aggregation and Pareto-optimal approaches for network routing.**

A research-driven framework for experimenting with and comparing different multi-objective path-finding techniques on graph-based network models. Includes modular models, algorithmic approaches, and demonstration scripts.

The project was developed in the context of routing traffic in a network where nodes represent devices and edges represent links characterized with (latency, risk), however the models and algorithms implemented here work with any graph with double weighted edges.

Key Contributions
-----------------
- Implementations of core graph algorithms used for shortest-path computation and multi-criteria path selection.
- A set of utilities to construct, serialize, and analyze graph instances and computed paths.
- A reproducible example dataset and demonstration scripts allowing experiment replication.

Repository Structure
--------------------
- `algorithms/` — Implementations of the core algorithms:
	- `dijkstra.py` — Single-source shortest-path (Dijkstra).
	- `floyd_warshall.py` — All-pairs shortest paths (Floyd–Warshall).
	- `pareto_front.py` — Single source all non dominated paths (Pareto-front).
- `helpers/` — Utilities for generating graphs, converting formats, selecting and evaluating paths:
	- `graph_2_constructor.py`, `graph_2_to_csv.py`, `csv_helpers/` — data preparation and IO helpers.
	- `get_dijkstra_path.py`, `get_floyd_path.py`, `select_pareto_path.py` — convenience wrappers for algorithm outputs.
	- `path_stats.py` — path evaluation helper.
- `models/` — Data model definitions for graphs and nodes.
- `data/demo.csv` — Example dataset used by demonstration scripts.
- `demo.py` / `main.py` — Example drivers and entry points for running experiments and demonstrations.

Environment and Dependencies
----------------------------
Python 3.8+ is recommended.
- To create an isolated environment (recommended):

```bash
# Windows:
python -m venv .venv
.venv\\Scripts\\activate 
```

```bash
# Linux:
python3 -m venv env
source evn/bin/activate
```

- To install Dependencies:

```bash
pip install --updrade pip
pip install -r requirements.txt
```

Unit Tests
----------
- the `demo.py` can count as unit test for all the implemented algorithms

Usage and Examples
------------------
- Windows:
```bash
# To run the demonstration script (example):
python demo.py
# To run the main script (interactive):
python main.py
```

- Linux:
```bash
# To run the demonstration script (example):
python3 demo.py
# To run the main script (interactive):
python3 main.py
```

- To use the library programmatically, import the algorithms and helper functions. Example (conceptual):

```python
from models import Graph
from algorithms import dijkstra
from helpers import comb_gen, get_dijkstra_path, path_stats

g = Graph('data/demo.csv') # creates the graph
table = dijkstra(g, comb_gen(1, 10)) # runs dijkstra with weight aggregation function : w = 1*latency + 10*risk
path = get_dijkstra_path(g, table, dest='dest') # gets path to destination from dijkstra's table
path_stats(g, path) # show path, cumulative risk and latency
```

- graph `.csv` files must respect the following format:
1. 0 or 1 (0 for oriented, 1 for symmetric)
2. source_node_id
3. destination_node_id
4. node_1_id,node_2_id,latency,risk (repeat for as many edges as needed)

Reproducibility and Experiments
-------------------------------
- Example data set is stored under `data/demo.csv` to allow experiments to be reproduced.
- Use the helper scripts in `helpers/` to generate variants of graphs, export them to CSV, and see path statistics via `path_stats.py`.
- For multi-criteria evaluation, run the Pareto-front utilities in `algorithms/pareto_front.py` and inspect selected trade-offs using `select_pareto_path.py`.

Evaluation Metrics
------------------
- The repository provides utilities to compute standard metrics for paths (length, cumulative weight, and any user-defined attributes). These can be found in `helpers/path_stats.py`.

Extending the Codebase
----------------------
- To add a new algorithm, place a new module under `algorithms/` exposing a clear API (inputs: graph representation, parameters; outputs: distances and predecessor information or path lists).
- To add new datasets, place CSV files under `data/` and include a brief description in `sample_data/`.
