class VegetablesRecord:
    """
    A data transfer object for the dataset 32100260
    """
    last_id = 0

    def __init__(self, ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor,
                 scalar_id, vector, coordinate, value, status, symbol, terminated, decimals):
        """
        Initialize the object with the provided attribute values
        """
        self.veg_id = self.generate_id()
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

    def generate_id(self):
        """
        Generates an incremental id each time it's called
        :return: incremental id integer
        """
        self.last_id += 1
        return self.last_id

    def to_list(self):
        """
        Converts the object attributes to a list
        :return: List of attributes
        """
        return [
            self.ref_date, self.geo, self.dguid, self.type_of_product, self.type_of_storage,
            self.uom, self.uom_id, self.scalar_factor, self.scalar_id, self.vector,
            self.coordinate, self.value, self.status, self.symbol, self.terminated, self.decimals
        ]

    def __str__(self):
        """
        A string representative of the object
        :return: A string of attributes comma separated
        """
        return f"Record(ref_date={self.ref_date}, geo={self.geo}, dguid={self.dguid}, " \
               f"type_of_product={self.type_of_product}, type_of_storage={self.type_of_storage}, " \
               f"uom={self.uom}, uom_id={self.uom_id}, scalar_factor={self.scalar_factor}, " \
               f"scalar_id={self.scalar_id}, vector={self.vector}, coordinate={self.coordinate}, " \
               f"value={self.value}, status={self.status}, symbol={self.symbol}, " \
               f"terminated={self.terminated}, decimals={self.decimals})"
