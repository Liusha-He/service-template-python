import json
import logging
from typing import Optional, List

from src.config import EN_ENTITIES_DIR, N_OF_WORKERS, WORD_COUNT_DIR
from src.lib import extract_en
from src.handler import clean_text

_logger = logging.getLogger(__name__)


def entity_extraction_service_en(text: str) -> Optional[List[str]]:
    """a arapper of all stages from input to output"""
    with open(EN_ENTITIES_DIR, "r", encoding="utf-8") as file:
        entity_map = json.load(file)

    cleaned_text_pair = clean_text(text, WORD_COUNT_DIR)

    entities = extract_en(
        text_pair=cleaned_text_pair,
        entity_map=entity_map,
    )
    entities = list(entities)

    if len(entities) > 0:
        return list(entities)
    else:
        _logger.info(f"cannot find any phrase in {text}")
