# python-object_relational_mapping

Part of the ALU Higher Level Programming curriculum.

This project links Python to MySQL, first with raw SQL queries using
`MySQLdb`, then through an Object-Relational Mapper (ORM) using
`SQLAlchemy`. It covers connecting to a database, running `SELECT`,
`INSERT`, `UPDATE`, and `DELETE` operations, guarding against SQL
injection, and mapping Python classes to MySQL tables, including
one-to-many relationships between `State` and `City`.

## Requirements

- Ubuntu 20.04 LTS, python3 (3.8.5)
- MySQL 8.0
- MySQLdb 2.0.x (`mysqlclient`)
- SQLAlchemy 1.4.x

## Files

| File | Description |
| --- | --- |
| `0-select_states.py` | List all states (MySQLdb) |
| `1-filter_states.py` | List states starting with `N` |
| `2-my_filter_states.py` | Filter states by user input (not injection safe) |
| `3-my_safe_filter_states.py` | Filter states by user input (injection safe) |
| `4-cities_by_state.py` | List all cities with their state, one query |
| `5-filter_cities.py` | List cities of a given state, one query |
| `model_state.py` | `State` model (SQLAlchemy) |
| `7-model_state_fetch_all.py` | List all `State` objects |
| `8-model_state_fetch_first.py` | Print the first `State` object |
| `9-model_state_filter_a.py` | List `State` objects containing `a` |
| `10-model_state_my_get.py` | Get a `State` id by name |
| `11-model_state_insert.py` | Insert `Louisiana` as a new `State` |
| `12-model_state_update_id_2.py` | Rename the `State` with `id=2` |
| `13-model_state_delete_a.py` | Delete `State` objects containing `a` |
| `model_city.py` | `City` model (SQLAlchemy) |
| `14-model_city_fetch_by_state.py` | List all `City` objects with their state |
| `relationship_state.py` | `State` model with a `cities` relationship |
| `relationship_city.py` | `City` model with a `state` relationship |
| `100-relationship_states_cities.py` | Create `California` with `San Francisco` |
| `101-relationship_states_cities_list.py` | List states and their cities, one query |
| `102-relationship_cities_states_list.py` | List cities and their state, one query |

## Usage

```
$ ./0-select_states.py <mysql_user> <mysql_password> <database>
```

## Author

Rosette
