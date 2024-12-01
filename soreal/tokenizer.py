import os
from logging import getLogger
from typing import List, Literal
from sentencepiece import SentencePieceProcessor

logger = getLogger(__name__)


class Tokenizer:
    def __init__(self, model_path: str) -> None:
        """
        Args:
            model_path: str; The path to the SentencePiece model file.
        """
        assert os.path.isfile(path=model_path), model_path

        self.sentencepiece_processor = SentencePieceProcessor(model_path=model_path)
        logger.info(f"Reloaded SentencePiece model from {model_path}")
