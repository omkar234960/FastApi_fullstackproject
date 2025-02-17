from fastapi import FastAPI,HTTPException,Depends
from .database import Base, engine, SessionLocal
from sqlalchemy.orm import Session  
from . import models
from . import schema


Base.metadata.create_all(bind=engine)
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/productadd/',response_model=schema.Product)
def CreateProduct(products:schema.ProductAdd,db:Session=Depends(get_db)):
    new_Product=models.Product(
        name=products.name,add=products.add,Quantity=products.Quantity,price=products.price,date_added=products.date_added
        )
    db.add(new_Product)
    db.commit()
    db.refresh(new_Product)
    return new_Product

@app.get('/products/', response_model=list[schema.Product])
def GetProducts (db:Session=Depends(get_db)):
    products=db.query(models.Product).all()
    return products

@app.put('/product/{product_id}',response_model=schema.Product)
def updateproduct(product_id:int,product:schema.ProductAdd,db:Session=Depends(get_db)):
    update_product=db.query(models.Product).filter(models.Product.id==product_id).first()
    if not update_product:
        raise HTTPException(status_code=404,detail='Product not found')
    update_product.name=product.name
    update_product.add=product.add
    update_product.Quantity=product.Quantity
    update_product.price=product.price
    db.commit()
    db.refresh(update_product)
    return update_product

@app.delete('/product/{product_id}')
def delete(product_id:int,db:Session=Depends(get_db)):
    product=db.query(models.Product).filter(models.Product.id==product_id).first()
    if not product:
        raise HTTPException(status_code=404,detail='Product not found')
    db.delete(product)
    db.commit()
    return {'detail':'Product deleted'}