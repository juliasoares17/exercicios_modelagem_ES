import unittest

class Aluno:
    def __init__(self, nome: str):
        self.nome = nome
        self._notas = []

    def adicionar_nota(self, nota: float):
        self._notas.append(nota)

    def media(self) -> float:
        if not self._notas:
            return 0.0
        return sum(self._notas) / len(self._notas)

class TestAluno(unittest.TestCase):
    def test_media_com_notas_validas(self):
        aluno = Aluno("Aluno da Silva")
        aluno.adicionar_nota(8.0)
        aluno.adicionar_nota(10.0)
        self.assertEqual(aluno.media(), 9.0)

    def test_media_sem_notas_evita_divisao_por_zero(self):
        aluno = Aluno("Aluno da Silva")
        self.assertEqual(aluno.media(), 0.0)
