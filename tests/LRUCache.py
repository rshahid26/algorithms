from data_structures import LRUCache

def test_LRUCache():
    print("Testing LRUCache...")

    # Create a cache of size 2
    cache = LRUCache(2)

    # Add items to the cache
    cache.put(1, "One")
    cache.put(2, "Two")

    # Test retrieval
    assert cache.get(1) == "One", "Error in get method"
    assert cache.get(2) == "Two", "Error in get method"
    assert cache.get(3) == -1, "Error in get method for non-existent key"

    # Test update and LRU removal
    cache.put(3, "Three")  # This should remove key 1 (LRU)
    assert cache.get(1) == -1, "Error in LRU removal"
    assert cache.get(3) == "Three", "Error in put method"

    # Test setting a new size
    cache.set_size(1)  # This should keep only the most recent item (key 3)
    assert cache.get(2) == -1, "Error in resizing cache"

    print("All tests passed!")

if __name__ == "__main__":
    test_LRUCache()
