import bentoml
from bentoml.adapters import DataframeInput
from bentoml.artifact import LightGBMModelArtifact

@bentoml.artifacts([
    LightGBMModelArtifact('model'),
])
@bentoml.env(pip_dependencies=['lightgbm'])
class PricingPredictionService(bentoml.BentoService):

    @bentoml.api(input=DataframeInput(orient='records'))
    def predict(self, df):

        df[objetc_columns] = df[objetc_columns].astype("category")

        data = df[[
            'composition_truck', 'composition_axles',
            'region_origin', 'region_destination',
            'cargox_route_distance'
        ]]

        return self.artifacts.model.predict(data)
