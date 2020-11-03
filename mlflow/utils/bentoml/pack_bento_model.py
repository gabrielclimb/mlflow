import os
import joblib
from bento_service import ModelPredictionService


def pack_model(model: str, path_to_save):
    model_booster = model.booster_

    bento_service = ModelPredictionService()

    bento_service.pack('model', model_booster)

    saved_path = bento_service.save(path=path_to_save)

    return saved_path
