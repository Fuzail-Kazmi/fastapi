from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.responses import HTMLResponse
from contextlib import asynccontextmanager
from app.util.init_db import create_tables
from app.db.models import users, products
from app.db.services import user_services, product_services
from app.db.schemas import user_schema, product_schema
from app.core.database import get_db, engine
from sqlalchemy.orm import Session
from typing import Optional


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Created")
    create_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"Hello": "pong"}


# @app.get("/html", response_class=HTMLResponse)
# def get_html():
#     return """
#     <html>
#         <head>
#             <title>My First HTML API</title>
#         </head>
#         <body>
#             <h1>Hello, Fuzail!</h1>
#             <p>This HTML was returned by FastAPI.</p>
#         </body>
#     </html>
#     """


@app.get("/html/", response_class=HTMLResponse)
async def get_html():
    return """
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">

#         <title>FastAPI | HTML Response</title>

#         <style>
#             * {
#                 margin: 0;
#                 padding: 0;
#                 box-sizing: border-box;
#             }

#             body {
#                 min-height: 100vh;
#                 display: flex;
#                 justify-content: center;
#                 align-items: center;
#                 padding: 30px 20px;
#                 font-family: Arial, Helvetica, sans-serif;
#                 color: #f8fafc;
#                 background:
#                     radial-gradient(
#                         circle at top right,
#                         #172b50,
#                         transparent 40%
#                     ),
#                     linear-gradient(135deg, #071426, #0b1830);
#             }

#             .container {
#                 width: 100%;
#                 max-width: 1050px;
#                 overflow: hidden;
#                 border: 1px solid #263956;
#                 border-radius: 18px;
#                 background: rgba(10, 25, 48, 0.92);
#                 box-shadow: 0 25px 80px rgba(0, 0, 0, 0.3);
#             }

#             header {
#                 display: flex;
#                 justify-content: space-between;
#                 align-items: center;
#                 gap: 20px;
#                 padding: 22px 30px;
#                 border-bottom: 1px solid #263956;
#                 background: rgba(5, 17, 35, 0.7);
#             }

#             .brand {
#                 display: flex;
#                 align-items: center;
#                 gap: 12px;
#                 font-size: 23px;
#                 font-weight: 700;
#             }

#             .brand-icon {
#                 width: 42px;
#                 height: 42px;
#                 display: grid;
#                 place-items: center;
#                 border-radius: 50%;
#                 color: white;
#                 background: linear-gradient(135deg, #14b8a6, #2563eb);
#             }

#             .status {
#                 display: flex;
#                 align-items: center;
#                 gap: 9px;
#                 padding: 10px 15px;
#                 border: 1px solid #155e52;
#                 border-radius: 30px;
#                 color: #5eead4;
#                 background: #0c302f;
#                 font-size: 13px;
#             }

#             .status-dot {
#                 width: 8px;
#                 height: 8px;
#                 border-radius: 50%;
#                 background: #2dd4bf;
#                 box-shadow: 0 0 10px #2dd4bf;
#             }

#             main {
#                 padding: 75px 35px 65px;
#                 text-align: center;
#             }

#             .eyebrow {
#                 display: inline-block;
#                 padding: 8px 14px;
#                 border: 1px solid #263d69;
#                 border-radius: 30px;
#                 color: #93c5fd;
#                 background: #122648;
#                 font-size: 12px;
#                 font-weight: 700;
#                 letter-spacing: 1.5px;
#             }

#             h1 {
#                 margin-top: 28px;
#                 font-size: clamp(38px, 6vw, 65px);
#                 letter-spacing: -2px;
#                 line-height: 1.1;
#             }

#             h1 span {
#                 color: #60a5fa;
#             }

#             .description {
#                 max-width: 600px;
#                 margin: 22px auto 0;
#                 color: #a9bad2;
#                 font-size: 17px;
#                 line-height: 1.8;
#             }

#             .divider {
#                 width: 65px;
#                 height: 4px;
#                 margin: 30px auto 0;
#                 border-radius: 10px;
#                 background: linear-gradient(90deg, #3b82f6, #2dd4bf);
#             }

#             .features {
#                 display: grid;
#                 grid-template-columns: repeat(4, minmax(0, 1fr));
#                 gap: 16px;
#                 margin-top: 55px;
#             }

#             .feature-card {
#                 padding: 28px 16px;
#                 border: 1px solid #293d5c;
#                 border-radius: 14px;
#                 background: linear-gradient(
#                     145deg,
#                     #10213d,
#                     #0b1930
#                 );
#                 transition:
#                     transform 0.2s ease,
#                     border-color 0.2s ease;
#             }

#             .feature-card:hover {
#                 transform: translateY(-5px);
#                 border-color: #3b82f6;
#             }

#             .feature-icon {
#                 margin-bottom: 16px;
#                 color: #60a5fa;
#                 font-size: 28px;
#             }

#             .feature-card h2 {
#                 margin-bottom: 10px;
#                 font-size: 16px;
#             }

#             .feature-card p {
#                 color: #9aadc7;
#                 font-size: 13px;
#                 line-height: 1.7;
#             }

#             .endpoint {
#                 margin-top: 45px;
#                 padding: 22px;
#                 border: 1px solid #293d5c;
#                 border-radius: 14px;
#                 background: #081529;
#                 text-align: left;
#             }

#             .endpoint h2 {
#                 margin-bottom: 15px;
#                 font-size: 15px;
#             }

#             .endpoint-row {
#                 display: flex;
#                 align-items: center;
#                 gap: 14px;
#                 flex-wrap: wrap;
#                 padding: 15px;
#                 border: 1px solid #293d5c;
#                 border-radius: 9px;
#                 background: #10213a;
#             }

#             .method {
#                 padding: 7px 11px;
#                 border-radius: 6px;
#                 color: #6ee7b7;
#                 background: #123d36;
#                 font-size: 12px;
#                 font-weight: 700;
#             }

#             .endpoint code {
#                 overflow-wrap: anywhere;
#                 color: #dbeafe;
#                 font-size: 14px;
#             }

#             footer {
#                 display: flex;
#                 justify-content: space-between;
#                 gap: 15px;
#                 flex-wrap: wrap;
#                 padding: 22px 30px;
#                 border-top: 1px solid #263956;
#                 color: #8fa3bf;
#                 font-size: 12px;
#             }

#             @media (max-width: 750px) {
#                 main {
#                     padding: 55px 22px;
#                 }

#                 .features {
#                     grid-template-columns: repeat(2, minmax(0, 1fr));
#                 }

#                 header {
#                     padding: 18px;
#                 }

#                 .brand {
#                     font-size: 19px;
#                 }
#             }

#             @media (max-width: 450px) {
#                 .features {
#                     grid-template-columns: 1fr;
#                 }

#                 .status {
#                     padding: 8px;
#                     font-size: 11px;
#                 }

#                 h1 {
#                     letter-spacing: -1px;
#                 }

#                 .description {
#                     font-size: 15px;
#                 }

#                 footer {
#                     padding: 20px;
#                 }
#             }
#         </style>
#     </head>

#     <body>
#         <div class="container">

#             <header>
#                 <div class="brand">
#                     <div class="brand-icon">&#9889;</div>
#                     <span>FastAPI</span>
#                 </div>

#                 <div class="status">
#                     <span class="status-dot"></span>
#                     API Working
#                 </div>
#             </header>

#             <main>
#                 <div class="eyebrow">
#                     HTML RESPONSE EXAMPLE
#                 </div>

#                 <h1>
#                     Hello, <span>Fuzail!</span>
#                 </h1>

#                 <p class="description">
#                     This HTML page is returned directly from a FastAPI
#                     endpoint using HTMLResponse. A simple example of
#                     serving a complete HTML document from Python.
#                 </p>

#                 <div class="divider"></div>

#                 <section class="features">

#                     <article class="feature-card">
#                         <div class="feature-icon">&#9889;</div>
#                         <h2>Fast Response</h2>
#                         <p>
#                             Built with FastAPI for efficient
#                             HTTP request handling.
#                         </p>
#                     </article>

#                     <article class="feature-card">
#                         <div class="feature-icon">&lt;/&gt;</div>
#                         <h2>HTML Response</h2>
#                         <p>
#                             Returns a complete HTML document
#                             to the browser.
#                         </p>
#                     </article>

#                     <article class="feature-card">
#                         <div class="feature-icon">&#9673;</div>
#                         <h2>Modern Stack</h2>
#                         <p>
#                             Python, FastAPI and standard
#                             web technologies.
#                         </p>
#                     </article>

#                     <article class="feature-card">
#                         <div class="feature-icon">&#9825;</div>
#                         <h2>Simple &amp; Clean</h2>
#                         <p>
#                             Easy to understand, customize
#                             and extend.
#                         </p>
#                     </article>

#                 </section>

#                 <section class="endpoint">
#                     <h2>API Endpoint</h2>

#                     <div class="endpoint-row">
#                         <span class="method">GET</span>
#                         <code>/html</code>
#                     </div>
#                 </section>
#             </main>

#             <footer>
#                 <span>FastAPI &bull; HTML Response Example</span>
#                 <span>Built with Python and HTML/CSS</span>
#             </footer>

#         </div>
#     </body>
#     </html>
#     """


@app.get("/users/", response_model=list[user_schema.User])
async def get_users(db: Session = Depends(get_db)):
    return user_services.get_users(db)


@app.get("/user/{id}", response_model=user_schema.User)
async def get_user(id: int, db: Session = Depends(get_db)):
    user_queryset = user_services.get_user(db, id)
    if user_queryset:
        return user_queryset
    raise HTTPException(status_code=404, detail="Invalid User Id Provide")


@app.post("/user/", response_model=user_schema.User)
async def create_new_user(user: user_schema.CreateUser, db: Session = Depends(get_db)):
    return user_services.create_user(db, user)


@app.put("/user/{id}/", response_model=user_schema.User)
async def update_user(
    user: user_schema.CreateUser, id: int, db: Session = Depends(get_db)
):
    db_update = user_services.update_user(db, user, id)
    if db_update:
        return db_update
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/user/{id}/", response_model=user_schema.User)
async def delete_user(id: int, db: Session = Depends(get_db)):
    delete_entry = user_services.delete_user(db, id)
    if delete_entry:
        return delete_entry
    raise HTTPException(status_code=404, detail="User not found")


@app.get("/products/", response_model=list[product_schema.Product])
async def get_products(db: Session = Depends(get_db)):
    return product_services.get_products(db)


@app.post("/product/", response_model=product_schema.Product)
async def create_new_product(
    product: product_schema.CreateProduct, db: Session = Depends(get_db)
):
    return product_services.create_product(db, product)


@app.get("/product/{product_id}", response_model=product_schema.Product)
async def get_product(product_id: int, db: Session = Depends(get_db)):
    product_queryset = product_services.get_product(db, product_id)
    if product_queryset:
        return product_queryset
    raise HTTPException(status_code=404, detail="Invalid Product Id Provide")


@app.put("/product/{product_id}", response_model=product_schema.Product)
async def update_product(
    product: product_schema.CreateProduct,
    product_id: int,
    db: Session = Depends(get_db),
):
    db_update = product_services.update_product(db, product, product_id)
    if db_update:
        return db_update
    raise HTTPException(404, "Product Not Found")


@app.delete("/product/{product_id}", response_model=product_schema.Product)
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    delete_query = product_services.delete_product(db, product_id)
    if delete_query:
        return delete_query
    raise HTTPException(404, "Product not Found")

