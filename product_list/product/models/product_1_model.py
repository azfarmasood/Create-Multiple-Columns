from sqlmodel import Field, SQLModel, Column, JSON


class Images(SQLModel):
    main_image: str
    image_1: str
    image_2: str
    image_3: str
    image_4: str
    
class ListItmes(SQLModel):
    name: str
    description: str
    price: float

class ProductBase(SQLModel):
    product_id: int | None = Field(None, primary_key = True)
    
    
class Product(ProductBase, table= True):
    image: str
    name: str
    description: str
    price: float
    images: Images = Field(sa_column = Column(JSON))
    multiple_lists_products: list[ListItmes] = Field(sa_column = Column(JSON))
    
    
class RequProductModel(SQLModel):
    image: str
    name: str
    description: str
    price: float
    images: Images
    multiple_lists_products: list[ListItmes]