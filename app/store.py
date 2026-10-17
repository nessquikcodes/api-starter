"""In-memory item store. Replaced by a real database in a later part."""

from app.schemas import ItemCreate, ItemResponse

_items: dict[int, ItemResponse] = {}
_next_id: int = 1


def create_item(data: ItemCreate) -> ItemResponse:
    """Store a new item and return it with its assigned id."""
    global _next_id
    item = ItemResponse(id=_next_id, name=data.name)
    _items[item.id] = item
    _next_id += 1
    return item


def list_items() -> list[ItemResponse]:
    """Return all stored items in insertion order."""
    return list(_items.values())


def get_item(item_id: int) -> ItemResponse | None:
    """Return the item with the given id, or None if it does not exist."""
    return _items.get(item_id)


def delete_item(item_id: int) -> bool:
    """Delete the item with the given id. Return True if it existed."""
    return _items.pop(item_id, None) is not None


def reset() -> None:
    """Clear the store and reset the id counter. Used by tests."""
    global _next_id
    _items.clear()
    _next_id = 1
