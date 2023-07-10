class VegetablesRecord:
    """
    A data transfer object for the Vegetables dataset 32100260
    """

    _last_id = 0

    def __init__(
        self,
        veg_id,
        ref_date,
        geo,
        dguid,
        type_of_product,
        type_of_storage,
        uom,
        uom_id,
        scalar_factor,
        scalar_id,
        vector,
        coordinate,
        value,
        status,
        symbol,
        terminated,
        decimals
    ):
        """
        Initializes a new instance of the VegetablesRecord class.

        Args:

        Returns:
            None
        """
        self.veg_id = veg_id
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

    @classmethod
    def from_iterable(cls, iterable_data):
        """
        Alternate constructor that creates a new instance of VegetablesRecord from an iterable data type like a list.

        Args:
            cls: The class object.
            iterable_data: A iterable variable containing the attribute values for the record.
                The list should follow the order of the attributes:
                [ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id,
                scalar_factor, scalar_id, vector, coordinate, value, status, symbol,
                terminated, decimals]

        Returns:
            VegetablesRecord: A new instance of the VegetablesRecord class.
        """
        return cls(*iterable_data)

    @staticmethod
    def generate_id():
        """
        Generates an incremental id for a VegetableRecord instance

        This static method increments the `_last_id` class variable of the VegetablesRecord class by 1,
        and returns the updated value as the generated ID.

        Returns:
            int: The generated ID for a VegetablesRecord instance.
        """
        VegetablesRecord._last_id += 1
        return VegetablesRecord._last_id

    def to_list(self):
        """
        Converts a VegetablesRecord object to a list.

        Args:
            self: The current instance of the class.

        Returns:
            list: A list representation of the VegetablesRecord object.
        """
        return [
            self.veg_id,
            self.ref_date,
            self.geo,
            self.dguid,
            self.type_of_product,
            self.type_of_storage,
            self.uom,
            self.uom_id,
            self.scalar_factor,
            self.scalar_id,
            self.vector,
            self.coordinate,
            self.value,
            self.status,
            self.symbol,
            self.terminated,
            self.decimals,
        ]

    def __str__(self):
        """
        Returns a string representation of the VegetablesRecord object.

        Args:
            self: The current instance of the class.

        Returns:
            str: A string representation of the VegetablesRecord object.
        """
        return (
            f"Id: {self.veg_id}, ref_date: {self.ref_date}, geo: {self.geo}, dguid: {self.dguid}, "
            f"type_of_product: {self.type_of_product}, type_of_storage: {self.type_of_storage}, "
            f"uom: {self.uom}, uom_id: {self.uom_id}, scalar_factor: {self.scalar_factor}, "
            f"scalar_id: {self.scalar_id}, vector: {self.vector}, coordinate: {self.coordinate}, "
            f"value: {self.value}, status: {self.status}, symbol: {self.symbol}, "
            f"terminated: {self.terminated}, decimals: {self.decimals}"
        )
