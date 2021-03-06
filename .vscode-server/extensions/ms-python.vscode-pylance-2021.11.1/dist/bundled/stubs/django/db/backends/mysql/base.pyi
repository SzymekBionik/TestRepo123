from typing import Any, Optional

from django.db.backends.base.base import BaseDatabaseWrapper as BaseDatabaseWrapper

version: Any
django_conversions: Any
server_version_re: Any

class CursorWrapper:
    codes_for_integrityerror: Any = ...
    cursor: Any = ...
    def __init__(self, cursor: Any) -> None: ...
    def execute(self, query: Any, args: Optional[Any] = ...): ...
    def executemany(self, query: Any, args: Any): ...
    def __getattr__(self, attr: Any): ...
    def __iter__(self) -> Any: ...

class DatabaseWrapper(BaseDatabaseWrapper):
    vendor: str = ...
    data_types: Any = ...
    operators: Any = ...
    pattern_esc: str = ...
    pattern_ops: Any = ...
    isolation_levels: Any = ...
    Database: Any = ...
    SchemaEditorClass: Any = ...
    client_class: Any = ...
    creation_class: Any = ...
    features_class: Any = ...
    introspection_class: Any = ...
    ops_class: Any = ...
    validation_class: Any = ...
    isolation_level: Any = ...
    def get_connection_params(self): ...
    def get_new_connection(self, conn_params: Any): ...
    def init_connection_state(self) -> None: ...
    def create_cursor(self, name: Optional[Any] = ...): ...
    def disable_constraint_checking(self): ...
    needs_rollback: Any = ...
    def enable_constraint_checking(self) -> None: ...
    def check_constraints(self, table_names: Optional[Any] = ...) -> None: ...
    def is_usable(self): ...
    def display_name(self): ...
    def data_type_check_constraints(self): ...
    def mysql_server_info(self): ...
    def mysql_version(self): ...
    def mysql_is_mariadb(self): ...
    def sql_mode(self): ...
