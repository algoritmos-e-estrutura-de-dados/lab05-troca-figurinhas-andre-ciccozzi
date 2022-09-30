from main import torcadefigurinha

def tese01():
    maria = [1000]
    joao = [1000]

    assert torcadefigurinha(maria, joao) == 0


def teste02():
    maria = ['1', '3', '5']
    joao = ['2', '4', '6', '8']

    assert torcadefigurinha(maria, joao) == 3


def teste03():
    maria = ['1', '1', '2', '3', '5', '7', '8', '8', '9', '15']
    joao = ['2', '2', '2', '3', '4', '6', '10', '11', '11']

    assert torcadefigurinha(maria, joao) == 4
