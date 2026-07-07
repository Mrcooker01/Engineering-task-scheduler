# Engineering Task & Sprint Scheduler

A robust, terminal-based project management tool developed in Python to simulate core Agile/Scrum functionalities. This application focuses on dynamic memory allocation, state management, and algorithmic filtering, utilizing nested data structures to handle complex programming logic without external software dependencies.

## Key Features
- **Dynamic Sprint Management:** Utilizes nested dictionary-list architectures to manage tasks dynamically across predefined states (`Todo`, `Doing`, `Done`).
- **Data Integrity Constraints:** Employs explicit boundary validation for priority inputs, preventing state corruption.
- **Relational Object Mapping:** Uniquely tracks tasks using self-incrementing, deterministic IDs mapped across independent data collections.
- **Cross-Collection State Mutators:** Implements safe multi-dimensional loop traversal to dynamically search, pop, and re-allocate task objects between logic queues.
- **Context-Aware Analytics:** Extracts high-priority assets using logical flag-tracking algorithms across volatile memory structures.

## Core Concepts Applied
- Multi-dimensional Dictionary Iteration (`for-each` nesting)
- Complex Data Scope Control & Logical Flag Handling (`bool` state tracking)
- Strict Sequence Range Operations (`range` boundary checks)
- Clean Code Documentation via PEP 257-compliant Docstrings

## Technical Architecture
The system stores data efficiently using an in-memory database layout:
```python
project_board = {
    "Todo": [ {"id": 1, "title": "Setup DB", "priority": 1}, ... ],
    "Doing": [ ... ],
    "Done": [ ... ]
}
