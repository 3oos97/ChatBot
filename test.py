import io
import json

import snips_nlu_en
from snips_nlu import SnipsNLUEngine, load_resources
from snips_nlu.default_configs import CONFIG_EN


#default_engine = SnipsNLUEngine()

load_resources('snips_nlu_en')


engine = SnipsNLUEngine(config=CONFIG_EN)

with io.open("dataset.json") as f:
    dataset = json.load(f)

engine.fit(dataset)

parsing = engine.parse(u" give me my gpa")
result = json.loads(json.dumps(parsing, indent=2))
print(result)
