from criptrografia import encryptThis


def test_encryptThis():
    assert encryptThis("Python") == '58stye'  # Teste cinco letras
    assert encryptThis("dog") == '280stt'  # Teste três letras
    assert encryptThis("good morning") == '107stte 340dllo'  # Teste múltiplas palavras
    assert encryptThis("") == ''  # Teste para string vazia

test_encryptThis()
