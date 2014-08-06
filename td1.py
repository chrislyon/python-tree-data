## ==================
## TREE DATA PYTHON
## ==================

import os
import cmd
import h5py
import numpy as np

DEFAULT_FILE = None

PARAMS = {}

## parametre
DIR_FILE='DIR_FILE'
ROOT_DIR='ROOT_DIR'

## Pour l'instant
PARAMS[ROOT_DIR] = os.getcwd()
PARAMS[DIR_FILE] = '/data'


class TreeData(cmd.Cmd):

    """Simple command processor."""

    ## Fonction vide
    def not_yet(self, line):
        self.pr_msg( "Not yet implemented : %s " % line )

    def help_not_done(self):
        self.pr_msg( "No help ... sorry " )

    ### TODO
    # create / new
    # delete OBJET (recurse)
    # search (recurse)
    # set OBJET attribut = ""
    # show OBJET [attribut]
    # STORE FICHIER DATASET
    # GET DATASET FICHIER

    def pr_msg(self, msg):
        print "%s" % msg

    def pr_error(self, msg):
        print "Erreur : %s " % msg

    ## Fonction
    def do_ex(self, line):
        self.not_yet(line)

    def help_ex(self):
        self.help_not_done()

    ## Fonction
    def do_create(self, line):
        global DEFAULT_FILE
        try:
            modele, name = line.split()
        except:
            self.help_create()
        modele = modele.upper()
        if modele == "FILE":
            self.pr_msg( "CREATE FILE %s " % name)
            dirname = '/'.join((PARAMS[ROOT_DIR], PARAMS[DIR_FILE]))
            fname = os.path.abspath( '/'.join((dirname, ("%s.hdf5" % name) )))
            f = h5py.File(fname, "w")
            if DEFAULT_FILE is None:
                DEFAULT_FILE = f
            self.pr_msg( "File %s CREATED" % fname)
        elif modele == "GROUP":
            self.pr_msg( "CREATE GROUP %s " % name )
            if DEFAULT_FILE:
                DEFAULT_FILE.create_group(name)
                self.pr_msg( "GROUP %s CREATED" % name )
            else:
                self.pr_error( "NO FILE" )
        elif modele == "DATA":
            self.pr_msg( "CREATE DATA %s" % name )
        else:
            self.pr_error( "Modele inconnu ...")

    def help_create(self):
        self.pr_msg( "Create MODELE NAME" )

    ## Fonction Liste
    def print_list_name(self, name):
        print "- %s " % name

    def do_ls(self,line):
        self.do_list(line)

    def do_list(self, line):
        if not DEFAULT_FILE:
            self.pr_error( "NO File" )
        else:
            DEFAULT_FILE.visit(self.print_list_name)

    def help_list(self):
        self.pr_msg( "list / ls : liste le contenu du dossier" )

    def do_EOF(self, line):
        if DEFAULT_FILE is not None:
            DEFAULT_FILE.flush()
            DEFAULT_FILE.close()
        return True

if __name__ == '__main__':
    TreeData().cmdloop()
