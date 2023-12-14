from _typeshed import Incomplete
from collections.abc import ItemsView

def ignore_ref_siblings(schema) -> list[tuple[str, Incomplete]] | ItemsView[str, Incomplete]: ...
def dependencies_draft3(validator, dependencies, instance, schema) -> None: ...
def dependencies_draft4_draft6_draft7(validator, dependencies, instance, schema) -> None: ...
def disallow_draft3(validator, disallow, instance, schema) -> None: ...
def extends_draft3(validator, extends, instance, schema) -> None: ...
def items_draft3_draft4(validator, items, instance, schema) -> None: ...
def additionalItems(validator, aI, instance, schema) -> None: ...
def items_draft6_draft7_draft201909(validator, items, instance, schema) -> None: ...
def minimum_draft3_draft4(validator, minimum, instance, schema) -> None: ...
def maximum_draft3_draft4(validator, maximum, instance, schema) -> None: ...
def properties_draft3(validator, properties, instance, schema) -> None: ...
def type_draft3(validator, types, instance, schema) -> None: ...
def contains_draft6_draft7(validator, contains, instance, schema) -> None: ...
def recursiveRef(validator, recursiveRef, instance, schema) -> None: ...