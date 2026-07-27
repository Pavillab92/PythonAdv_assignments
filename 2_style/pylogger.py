"""
content = assignment
course  = Python Advanced
 
date    = 14.11.2025
email   = contact@alexanderrichtertd.com
"""

# original: logging.init.py

def findCaller(self):
    """
    Find the stack frame of the caller so that we can note the source
    file name, line number and function name.
    """
    f = currentframe()
    #On some versions of IronPython, currentframe() returns None if
    #IronPython isn't run with -X:Frames.
    if f is not None:
        f = f.f_back
    rv = "(unknown file)", 0, "(unknown function)"
    while hasattr(f, "f_code"):
        co = f.f_code
        filename = os.path.normcase(co.co_filename)
        if filename == _srcfile:
            f = f.f_back
            continue
        rv = (co.co_filename, f.f_lineno, co.co_name)
        break
    return rv

# How can we make this code better?

# *****************************************************************************
# PEP8 rules applied to script
# *****************************************************************************

"""
content = assignment
course  = Python Advanced

date    = 14.11.2025
email   = contact@alexanderrichtertd.com
"""

# original: logging.init.py


def find_caller(self):
    """
    Find the stack frame of the caller so that we can note the source
    file name, line number and function name.
    """
    frame= currentframe()
    # On some versions of IronPython, currentframe() returns None if
    # IronPython isn't run with -X:Frames.
    if frame is not None:
        frame = frame.f_back


    result = "(unknown file)", 0, "(unknown function)"
    while hasattr(frame, "f_code"):
        code = frame.f_code
        filename = os.path.normcase(code.co_filename)
        if filename == _srcfile:
            frame = frame.f_back
            continue
        result = (code.co_filename, frame.f_lineno, code.co_name)
        break


    return result