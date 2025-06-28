# Indian Premier League (IPL) Relational Database Project

A comprehensive relational database project modeled on the Indian Premier League (IPL), developed to demonstrate advanced ER modeling, relational schema design, and normalization practices.

## 📘 Description

This project implements a normalized relational database system for IPL. Starting from an ER diagram, we applied a step-by-step ER-to-Relational conversion methodology, covering all major relationship types, normalization forms (1NF, 2NF, 3NF), and including complex entity mapping scenarios like weak entities, multivalued attributes, and n-ary relationships.

## 🛠️ Key Features

- **ER to Relational Model Mapping**:
  - Regular Entities: `Broadcasters`, `Season`, `Match`, `Team`, `Sponsors`, `Venue`, `Umpire`, `Player`
  - Weak Entities: `Toss`, `Staff`, `Batsman Stats`, `Bowler Stats`
  - Binary Relationships: Included using Foreign Key Approach
  - N-ary Relationships: Implemented as separate relations (e.g., `Brought To You By`, `Hosted At`)
  - Multivalued Attributes: Extracted into separate relations (`Titles`, etc.)

- **Normalization**:
  - Converted to **1NF** by removing multivalued attributes
  - Confirmed **2NF** by ensuring full functional dependency on primary keys
  - Confirmed **3NF** by eliminating transitive dependencies

- **Special Attributes Handling**:
  - Composite keys used appropriately
  - Foreign keys included for proper relationship mapping
  - Attributes like `Bid Amount` added to related entities

## 🧠 Concepts Demonstrated

- ER to Relational Mapping
- Handling weak and strong entity sets
- 1:1, 1:N, and N-ary relationship conversion
- Multivalued attribute handling
- Normalization to 1NF, 2NF, and 3NF
- Schema refinement and dependency management

## 📊 Entity Highlights

- **Match**: Central to multiple relationships, connected to `Toss`, `Venue`, `Teams`, `Umpires`
- **Player**: Linked with `Team`, and appears in both batting and bowling stats
- **Brought To You By**: N-ary relation between `Broadcasters`, `Sponsors`, and `Players`
- **Hosted At**: Many-to-many between `Match` and `Venue`

## 📂 Deliverables

- ER Diagram
- Relational Model (Step-by-step)
- Final normalized relational schema (3NF)
- Justification and explanation for all steps

---

## 🏁 Final Notes

This project is a complete demonstration of end-to-end relational database design starting from conceptual modeling to fully normalized schemas. All conversion steps follow textbook principles and have been justified clearly.

