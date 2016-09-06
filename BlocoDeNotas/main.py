# -*- coding: utf-8 -*-

from bloco_de_notas import BlocoDeNotas
from anotacoes import Anotacoes

a = Anotacoes(1, '1ª anotação mesmo')
b = Anotacoes(2, '2ª anotação mesmo')
c = Anotacoes(3, 'I never got into training to be an All-Ireland boxing champ or to win a belt. At the start, I just got into it to learn how to defend myself when I got into situations.')

notepad = BlocoDeNotas(a, b, c)

print(notepad.getPalavrasMaisFrequentes())