import shlex

orig = """
CREATE MODELE model_name ( id int16, nom S20, no_poste int8 )
"""

for l in  shlex.shlex(orig):
    print l
