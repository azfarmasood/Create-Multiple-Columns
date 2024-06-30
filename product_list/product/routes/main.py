from fastapi import FastAPI
from product.models.product_1_model import Product, RequProductModel
from product.db.db import DB_SESSION, create_db_and_tables

app = FastAPI(lifespan = create_db_and_tables)


@app.post("/create_products/", response_model = Product)
def create_product(db: DB_SESSION, create_req_product: RequProductModel):
    
    list_products_details = []
    
    for i in create_req_product.multiple_lists_products:
        list_products = i.model_dump()
        list_products_details.append(list_products)
        
    
    dict_model = create_req_product.model_dump()
    
    
    dict_model["images"] = create_req_product.images.model_dump()
    
    new_product = Product(**dict_model)
    
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

