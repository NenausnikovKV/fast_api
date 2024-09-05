import json

from fastapi.encoders import jsonable_encoder

from app.routers.shop_products import schemas


#
# def create_shop(db: Session, shop: schemas.CreateShop):
#     """create user in database"""
#     db_shop = models.Shop(name=shop.name)
#     db.add(db_shop)
#     db.commit()
#     db.refresh(db_shop)
#     return db_shop
#
#
# def get_shop(db: Session, shop_id: int):
#     """get shop from db by id"""
#     return db.query(models.Shop).filter(models.Shop.id == shop_id).first()
#
#
# def get_shop_by_name(db: Session, shop_name: str):
#     """get shop from db by name"""
#     return db.query(models.Shop).filter(models.Shop.name == shop_name).first()
#
#
# def get_shops(db: Session, skip: int = 0, limit: int = 100):
#     """get users from db"""
#     return db.query(models.Shop).offset(skip).limit(limit).all()
#
#
# def create_shop_product(db: Session, product: schemas.ProductCreate, shop_id: int):
#     """create product from db dor given user id"""
#     db_product = models.Product(**product.model_dump(), shop_id=shop_id)
#     db.add(db_product)
#     db.commit()
#     db.refresh(db_product)
#     return db_product
#
#
# def get_products(db: Session, skip: int = 0, limit: int = 100):
#     """get products from db"""
#     products = db.query(models.Product).offset(skip).limit(limit).all()
#     return products
#
#
# def get_product(db: Session, product_id: int):
#     """get shop from db by id"""
#     return db.query(models.Product).filter(models.Product.id == product_id).first()
#
#
#
#





# def test_create_shop(test_client):
#     """ test create shop api"""
#     test_shop_name = "test_shop"
#     create_shop = schemas.CreateShop(name=test_shop_name)
#     request_body = jsonable_encoder(create_shop)
#     response = test_client.post("/products/shop/", json=request_body)
#     assert response.status_code == 200
#     response_shop_name = json.load(response.json()).name
#     assert response_shop_name == test_shop_name

#
#
# @router.get("/shops/", response_model=list[schemas.Shop])
# def get_shops(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     """get shops by limit"""
#     shops = crud.get_shops(db, skip=skip, limit=limit)
#     return shops
#
#
# @router.get("/shop/{shop_id}", response_model=schemas.Shop)
# def get_shop(shop_id: int, db: Session = Depends(get_db)):
#     """gt user pedantic model data"""
#     db_shop = crud.get_shop(db, shop_id=shop_id)
#     if db_shop is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_shop
#
#
# @router.post("/shop/{shop_id}/product/", response_model=schemas.Product)
# def create_product_for_shop(
#         shop_id: int,
#         product: schemas.ProductCreate,
#         db: Session = Depends(get_db)
# ):
#     """create item for given user"""
#     db_product = crud.create_shop_product(db=db, product=product, shop_id=shop_id)
#     return db_product
#
#
# @router.get("/products/", response_model=list[schemas.Product])
# def get_products(
#         skip: int = 0,
#         limit: int = 100,
#         db: Session = Depends(get_db)
# ):
#     """return all shop products"""
#     products = crud.get_products(db, skip, limit)
#     return products
#
#
# @router.get("/{product_id}/", response_model=schemas.Product)
# def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
#     """
#     return product for given id
#     otherwise raise exception
#     """
#     db_product = crud.get_product(db, product_id=product_id)
#     if db_product is None:
#         raise HTTPException(status_code=404, detail="Product not found")
#     return db_product
