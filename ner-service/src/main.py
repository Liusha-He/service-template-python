import logging

from fastapi import FastAPI
import uvicorn

from src.lib.models import APIRequest, APIResponse
from src.service import entity_extraction_service_en

app = FastAPI()
_logger = logging.getLogger(__name__)


@app.get("/extract/en", response_model=APIResponse)
async def match_query_string(query: APIRequest):
    input_text = query.query_string

    res_list = entity_extraction_service_en(input_text)

    _logger.info(f"get {res_list} from '{input_text}'")

    if res_list is not None:
        return {"entities": res_list}

    return {"entities": []}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
