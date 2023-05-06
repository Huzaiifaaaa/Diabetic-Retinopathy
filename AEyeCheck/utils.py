from datetime import datetime

def allowed_files(filename, ALLOWED_EXTENSIONS):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_unique_filename(module):
    if module=="DiabeticRetinopathy":
        return "DRD-"+remove_symbols(str(datetime.now()))+".jpeg"
    else:
        return "GD-"+remove_symbols(str(datetime.now()))+".jpeg"
    
def remove_symbols(filename):
    return filename.replace(" ", "").replace(":", "").replace("-", "").replace(".", "").replace("\\", "").replace("/", "")