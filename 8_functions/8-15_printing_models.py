#8.15 Printing Models

unprinted_designs = ['dodecahedron', 'mathsphere', 'catenary']
completed_designs = []

import printing_models as pm
pm.print_models(unprinted_designs, completed_designs)
pm.show_completed_models(completed_designs)
