import unittest
import sqlite3
from model.vegetablesServices import VegetablesServices


# By Abdul Mazed
class TestVegetablesServices(unittest.TestCase):
    def setUp(self):
        """Create a test database and table before running each test"""
        self.db = sqlite3.connect("test_database.db")
        self.db.execute("DROP TABLE IF EXISTS vegetable;")
        self.db.execute("""
            CREATE TABLE vegetable (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ref_date TEXT,
                geo TEXT,
                dguid TEXT,
                type_of_product TEXT,
                type_of_storage TEXT,
                uom TEXT,
                uom_id TEXT,
                scalar_factor TEXT,
                scalar_id TEXT,
                vector TEXT,
                coordinate TEXT,
                value TEXT,
                status TEXT,
                symbol TEXT,
                terminated TEXT,
                decimals TEXT
            );
        """)
        self.db.execute("""
            INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, 
                                    scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
            VALUES ('1970-01', 'Canada', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 
                    'v722342', '1.1.1', '1041', '', '', '', '0');
        """)
        self.db.commit()

    # By Abdul Mazed
    def tearDown(self):
        """Close the database connection after running each test"""
        self.db.close()

    def test_get_veg_by_id(self):
        """Test that get_veg_by_id retrieves the correct record"""
        self.service = VegetablesServices("test_database.db")
        expected_record = [1, '1970-01', 'Canada', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ',
                           '0', 'v722342', '1.1.1', '1041', '', '', '', '0']
        actual_record = self.service.get_veg_by_id(1)
        self.assertEqual(actual_record, expected_record)


if __name__ == '__main__':
    unittest.main()
