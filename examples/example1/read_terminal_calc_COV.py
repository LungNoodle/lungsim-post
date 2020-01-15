#!/usr/bin/env python
import numpy as np
import lungsimpost as lsp


field_to_average = 4 #indexing starts at zero, but first field will always be node number

model_results = lsp.import_exnode_tree('../example_inputs/solution_terminal.exnode')

print(model_results['total_nodes'])


field = model_results['nodes'][:,field_to_average]


print(np.mean(field))
print(np.std(field))
print(np.std(field)/np.mean(field)*100.)