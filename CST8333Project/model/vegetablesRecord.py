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
