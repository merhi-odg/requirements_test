import aif360

# modelop.init
def begin():
    
    global version
    version = aif360.__version__
    
    print("version: ", version, flush=True)
    pass

# modelop.score
def action(x):
    yield x
