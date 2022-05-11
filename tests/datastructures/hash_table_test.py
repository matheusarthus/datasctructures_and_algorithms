from datastructures.hash_table import HashTable


def test_put_and_get():
    hash_table = HashTable()

    hash_table.put("John Smith", "521-1234")
    hash_table.put("Lisa Smith", "521-8976")
    hash_table.put("Sam Doe", "521-5030")
    hash_table.put("Sandra Dee", "521-9655")
    hash_table.put("Ted Baker", "418-4165")

    assert hash_table.get("John Smith") == "521-1234"
    assert hash_table.get("Lisa Smith") == "521-8976"
    assert hash_table.get("Sam Doe")    == "521-5030"
    assert hash_table.get("Sandra Dee") == "521-9655"
    assert hash_table.get("Ted Baker")  == "418-4165"
    assert not hash_table.get("Tim Lee")

def test_empty():
    hash_table = HashTable()

    assert not hash_table.get("Ted Baker")
    assert not hash_table.get("Tim Lee")

def test_collision():
    hash_table = HashTable()

    hash_table.put("John Smith", "521-1234")
    hash_table.put("Sandra Dee", "521-9655")

    assert hash_table.get("John Smith") == "521-1234"
    assert hash_table.get("Sandra Dee") == "521-9655"
    assert not hash_table.get("Tim Lee")
