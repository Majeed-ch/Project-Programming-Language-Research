class DatasetS23:
    """A data transfer object for the dataset 32100260"""
    def __init__(self, ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor,
                 scalar_id, vector, coordinate, value, status, symbol, terminated, decimals):
        """Initialize the object with the provided attribute values"""
        self.ref_date = ref_date
        self.geo = geo
        self.dguid = dguid
        self.type_of_product = type_of_product
        self.type_of_storage = type_of_storage
        self.uom = uom
        self.uom_id = uom_id
        self.scalar_factor = scalar_factor
        self.scalar_id = scalar_id
        self.vector = vector
        self.coordinate = coordinate
        self.value = value
        self.status = status
        self.symbol = symbol
        self.terminated = terminated
        self.decimals = decimals

    def to_list(self):
        """Convert the object attributes to a list"""
        return [
            self.ref_date, self.geo, self.dguid, self.type_of_product, self.type_of_storage,
            self.uom, self.uom_id, self.scalar_factor, self.scalar_id, self.vector,
            self.coordinate, self.value, self.status, self.symbol, self.terminated, self.decimals
        ]
