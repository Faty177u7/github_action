import pytest
import app 

array_l = [5,3,4,2,1]
diccionario = [{"nombre":"Wendy","edad":23},{"nombre":"Gustavo","edad":15},{"nombre":"Anna","edad":43}]

def test_ordenar():
    assert app.ordenar(array_l) == [1,2,3,4,5]

def test_cont_mayores():
    assert app.cont_mayores(diccionario) == 2