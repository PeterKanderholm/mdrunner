# model-runner

A framework for running user-defined calculations (here called models)

## 1. Installation
```
pip install model-runner
```

## 2. Get started
Sample code on how to define, register and run user-defined models.

### 2.1 User-defined model types
Each type of model shall be defined in ```ModelType``` 
```Python
from enum import Enum, auto

class ModelType(Enum):
    In = auto()
    A = auto()
    B = auto()
```

### 2.2 User-defined model classes
Each model shall be defined in a separate class that inherits from the ```Model()``` base class

For each model class declare
1. the model type ```ModelType```
2. the dependencies to other models in ```init()```
3. the calculations to execute in ```run()```

```Python
from mdrunner import Model

class In2(Model):
    model_type = ModelType.In
    def init(self):
        """expecting external input from runner.add({'str':any})
           for example with {'p1': 2.0, 'p2': 3.0} will be available as In.p1 and In.p2 """
        pass
    def run(self):
        pass

class A1(Model):
    model_type = ModelType.A
    def init(self):
        self.get(ModelType.In)
    def run(self):
        self.add(name='x', val=self.In.p1 * self.In.p2)
        
class B1(Model):
    model_type = ModelType.B
    def init(self):
        self.get(ModelType.In)
        self.get(ModelType.A)
        pass
    def run(self):
        self.add(name='x', val=self.A.x * self.In.p3)
```

### 2.3 Model parameters
Model input and output values are passed between models as ('name', 'value') pairs.
The 'name' must be a ```str``` and the 'value' can be ```any``` object like e.g.
```Python
{'p1': 2, 'p2': 3.12e5, 's32': 'my text', 'x': numpy.array([1, 2, 3]), 'df22': pandas.DataFrame, 'y': MyCustomClass, ...}
```

### 2.4 Model library
Put the models in a separate directory and include a ```__init__.py``` to make it an importable python module
```Python
/models/__init__.py
        models.py
```


### 2.4 Register and run the models

1. import the user-defined models
2. select the models to run
3. supply any model with input values
4. run the models
5. collect the results

The framework figures out the right order of execution. The result of the calculations are accessed through the Runner instance.

```Python
import importlib
from mdrunner import Runner
from models import ModelType

# Register models
all_models = importlib.import_module('models')
selected_models = ['A1', 'In2', 'B1']
runner = Runner(all_models, selected_models)

# feed models with external inputs
values = {'p1': 2.0, 'p2': 3.0, 'p3': 4.0}
runner.add(values, ModelType.In)

# run models
runner.run_models()

# check model results 
assert runner.params == \
    {'A.x': 6.0,
     'B.x': 24.0,
     'In.p1': 2.0,
     'In.p2': 3.0,
     'In.p3': 4.0}

assert runner.B.x == 24.0
```

## 3. Further reading
For more usage examples see the ```docs``` and ```tests``` folders



