try:
    import math
    math.exp(1000)
except OverflowError as e:
    print("Terjadi OverflowError:", e)
except ArithmeticError as e:
    print("Terjadi ArithmeticError:", e)
except Exception as e:
    print("Terjadi Exception umum:", e)

try:
    import os
    os.mkdir("test_folder")
    os.mkdir("test_folder")
except FileExistsError as e:
    print("Terjadi FileExistsError:", e)
except OSError as e:
    print("Terjadi OSError:", e)
except Exception as e:
    print("Terjadi Exception umum:", e)

try:
    import zipimport
    importer = zipimport.zipimporter("tidak_ada.zip")
except zipimport.ZipImportError as e:
    print("Terjadi ZipImportError:", e)
except ImportError as e:
    print("Terjadi ImportError:", e)
except Exception as e:
    print("Terjadi Exception umum:", e) 