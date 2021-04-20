import aif360
import statsmodels

# modelop.init
def begin():
    
    global aif360_version
    global statsmodels_version

    aif360_version = aif360.__version__
    statsmodels_version = statsmodels.__version__
    
    print("aif360_version: ", vaif360ersion, flush=True)
    print("statsmodels_version: ", statsmodels_version, flush=True)

    pass

# modelop.score
def action(x):
    yield x
