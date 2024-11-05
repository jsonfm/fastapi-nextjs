from fastapi import FastAPI, APIRouter


app = FastAPI(
    docs_url="/api/py/docs",
    openapi_url="/api/py/openapi.json",
    title="Fastapi API + Next.js",
    description="💚 some API endpoints",
)

router = APIRouter(tags=["Home"])


@router.get("/")
def hello():
    return {"message": "Hello world!"}


@router.get("/about")
def about():
    return {"message": "about"}


app.include_router(router)
