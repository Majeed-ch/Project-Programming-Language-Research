import sys

sys.path.insert(0, '../model/')

from model.vegetablesRecord import VegetablesRecord
from model.vegetablesServices import VegetablesServices


# By Abdul Mazed
def test_add_vegetable():
    """
       Test case for the add_vegetable() method in the VegetablesServices class.

       This test verifies that the add_vegetable() method correctly adds a vegetable record to the records list.
       Assertions are made to ensure that the actual length is greater than the expected length, indicating that the
       record was successfully added. Additionally, it checks that the last element in the records list is an instance
       of the VegetablesRecord class and that its ref_date attribute matches the expected value.

       Returns:
           None
   """
    # Create a sample record and instantiate the vegetablesServices class
    record = ['2023-06-01', 'USA', '123456', 'Tomato', 'Cold Storage', 'kg', '123', '1.0', '456', 'VECTOR',
              'COORDINATE', '10.0', 'STATUS', 'SYMBOL', 'TERMINATED', '2']
    service = VegetablesServices("test_file.txt")

    expected_length = len(service.records)

    service.add_vegetable(record)
    actual_length = len(service.records)

    assert actual_length > expected_length
    assert isinstance(service.records[-1], VegetablesRecord)
    assert service.records[-1].ref_date == "2023-06-01"
