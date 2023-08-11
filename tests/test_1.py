import importlib
from src.mdrunner import Runner
from tests.models import ModelType


class Test_1:

    def test_models(self):
        ''' Register and run models '''

        # configure models to run
        all_models = importlib.import_module('tests.models')
        selected_models = ['S1']
        runner = Runner(all_models, selected_models)

        # feed models with external inputs
        values = {'p1': 2.0, 'p2': 3.0}
        runner.add_input_to_model(values, ModelType.S)

        # run models
        runner.run_models()

        # check result

        assert runner.input == {
            'S.input.p1': 2.0,
            'S.input.p2': 3.0
        }

        assert runner.output == {
            'S.output.x': 6.0
        }

        # get individual values
        assert runner.S.input.p1 == 2.0
        assert runner.S.input.p2 == 3.0
        assert runner.S.output.x == 6.0
