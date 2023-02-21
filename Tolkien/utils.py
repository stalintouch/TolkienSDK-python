import os
import sys


# ================== Paths ==================

ROOT_DIR = os.path.abspath(os.curdir)
TESTS_DIR = os.path.join(ROOT_DIR, 'tests')
TEST_MOCK_DIR = os.path.join(TESTS_DIR, 'mock')


# Limits what the SDK exports and can be used by the client
def export(fn):
    '''
    This function decorator adds function and classes to __all__ which controls
    what packages are exportable
    '''
    mod = sys.modules[fn.__module__]
    if hasattr(mod, '__all__'):
        mod.__all__.append(fn.__name__)
    else:
        mod.__all__ = [fn.__name__]
    return fn
