Abstract
--------
This repository implements and evaluates algorithms for computing shortest and Pareto-optimal paths in weighted graphs, with an emphasis on reproducibility and modularity. The codebase provides canonical implementations of single-source and all-pairs shortest path algorithms, utilities for constructing and exporting graph data, and tools to evaluate trade-offs among multiple path metrics using Pareto-front analysis.

This project is used in this case for network and routing problems, but the algorithms and utilities are general-purpose and can be applied to any other type of graph or domain. This repository was developed as a "mini-projet de R.O (Recherche Operationelle)".
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
	- `pareto_front.py` — Pareto-front generation and multi-criteria selection.
- `helpers/` — Utilities for generating graphs, converting formats, selecting and evaluating paths:
	- `graph_2_constructor.py`, `graph_2_to_csv.py`, `csv_helpers/` — data preparation and IO helpers.
	- `get_dijkstra_path.py`, `get_floyd_path.py` — convenience wrappers for algorithm outputs.
	- `select_pareto_path.py`, `Weight_calculator.py`, `path_stats.py` — multi-criteria selection and evaluation helpers.
- `models/` — Data model definitions for graphs and nodes.
- `data/` and `sample_data/` — Example datasets used by demonstration scripts.
- `demo.py` / `main.py` — Example drivers and entry points for running experiments and demonstrations.

Dependencies and Environment
----------------------------
- Python 3.8+ is recommended. The project uses only the Python standard library and lightweight dependencies.
- To create an isolated environment (recommended):

```bash
python -m venv .venv
.venv\\Scripts\\activate 
pip install --upgrade pip
pip install -r requirements.txt
```

Usage and Examples
------------------
- To run the demonstration script (example):

```bash
python demo.py
```

- To use the library programmatically, import the algorithms and helper functions. Example (conceptual):

```python
from algorithms.dijkstra import dijkstra
from helpers.graph_2_constructor import build_graph

G = build_graph('data/demo.csv')
dist, prev = dijkstra(G, source=0)
```

Reproducibility and Experiments
-------------------------------
- Example data sets are stored under `data/` and `sample_data/` to allow experiments to be reproduced.
- Use the helper scripts in `helpers/` to generate variants of graphs, export them to CSV, and compute path statistics via `path_stats.py`.
- For multi-criteria evaluation, run the Pareto-front utilities in `algorithms/pareto_front.py` and inspect selected trade-offs using `select_pareto_path.py`.

Evaluation Metrics
------------------
- The repository provides utilities to compute standard metrics for paths (length, cumulative weight, and any user-defined attributes). These can be found in `helpers/path_stats.py` and `helpers/Weight_calculator.py`.

Extending the Codebase
----------------------
- To add a new algorithm, place a new module under `algorithms/` exposing a clear API (inputs: graph representation, parameters; outputs: distances and predecessor information or path lists).
- To add new datasets, place CSV files under `data/` and include a brief description in `sample_data/`.

