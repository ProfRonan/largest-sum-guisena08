"""Module with functions."""


def largest_sum(numbers: list[int]) -> tuple[int, int]:
     if len (numbers) <2:
          return None
     maior_numero = max(numbers)
     numbers.remove(maior_numero)
     segundo_maior = max(numbers)
     primeiro = min(maior_numero, segundo_maior)
     segundo = max(maior_numero, segundo_maior)
     return primeiro, segundo 



   


