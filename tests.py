# -*- coding: utf-8 -*-
from challenge import current_facts
from challenge import build_schema_rules
from challenge import apply_schema_rules


def test1():
    res = current_facts([], [])
    if res:
        return "Fail: teste 1"
    else:
        return "Success: teste 1"


def test2():
    # Teste 2 - fornecido pelo desafio
    facts = [
      ('gabriel', 'endereço', 'av rio branco, 109', True),
      ('joão', 'endereço', 'rua alice, 10', True),
      ('joão', 'endereço', 'rua bob, 88', True),
      ('joão', 'telefone', '234-5678', True),
      ('joão', 'telefone', '91234-5555', True),
      ('joão', 'telefone', '234-5678', False),
      ('gabriel', 'telefone', '98888-1111', True),
      ('gabriel', 'telefone', '56789-1010', True),
    ]

    schema = [
        ('endereço', 'cardinality', 'one'),
        ('telefone', 'cardinality', 'many')
    ]

    expected = [
      ('gabriel', 'endereço', 'av rio branco, 109', True),
      ('joão', 'endereço', 'rua bob, 88', True),
      ('joão', 'telefone', '91234-5555', True),
      ('gabriel', 'telefone', '98888-1111', True),
      ('gabriel', 'telefone', '56789-1010', True)
    ]

    res = current_facts(facts, schema)
    if res != expected:
        return "Fail: teste 2"
    else:
        return "Success: teste 2"


def test3():
    # Teste 3 - Testando a funcao build_schema_rules
    schema = [
        ('endereço', 'cardinality', 'one'),
        ('telefone', 'cardinality', 'many'),
        ('telefone', 'cardinality', 'one'),
        ('teste_card', 'error', 'many'),
        ('teste_quant', 'cardinality', 'error')
    ]

    res = build_schema_rules(schema)
    if res != {'endereço': 'one', 'telefone': 'one'}:
        return "Fail: teste 3"
    else:
        return "Success: teste 3"


def test4():
    # Teste 4 - atributo que nao pertence a lista nao deve entrar na resposta
    facts = [
      ('gabriel', 'endereço', 'rua alice, 10', True),
      ('gabriel', 'endereço', 'av rio branco, 109', True),
      ('joão', 'endereço', 'rua alice, 10', True),
      ('joão', 'endereço', 'rua bob, 88', True),
      ('joão', 'telefone', '234-5678', True),
      ('gabriel', 'telefone', '98888-1111', True),
      ('gabriel', 'telefone', '56789-1010', True)
    ]

    schema = [
        ('endereço', 'cardinality', 'one'),
    ]

    expected = [
      ('gabriel', 'endereço', 'av rio branco, 109', True),
      ('joão', 'endereço', 'rua bob, 88', True),
    ]

    res = current_facts(facts, schema)
    if res != expected:
        return "Fail: teste 4"
    else:
        return "Success: teste 4"


def test5():
    # Teste 5 - Testando false
    facts = [
      ('joão', 'telefone', '234-5678', False),
      ('joão', 'telefone', '234-5678', False),
      ('gabriel', 'telefone', '98888-1111', False),
      ('gabriel', 'telefone', '56789-1010', False),
    ]

    schema = [
        ('telefone', 'cardinality', 'many')
    ]

    res = current_facts(facts, schema)
    if res:
        return "Fail: teste 5"
    else:
        return "Success: teste 5"


def test6():
    # Teste 6 - Testando a funcao apply_schema_rules separadamente
    facts = [
      ('gabriel', 'endereço', 'av rio branco, 109', True),
      ('joão', 'endereço', 'rua alice, 10', True),
      ('joão', 'endereço', 'rua bob, 88', True),
      ('joão', 'telefone', '234-5678', True),
      ('joão', 'telefone', '91234-5555', True),
      ('joão', 'telefone', '234-5678', False),
      ('gabriel', 'telefone', '98888-1111', True),
      ('gabriel', 'telefone', '56789-1010', True),
    ]

    rules = {'endereço': 'one', 'telefone': 'many'}

    expected = [
      ('gabriel', 'endereço', 'av rio branco, 109', True),
      ('joão', 'endereço', 'rua bob, 88', True),
      ('joão', 'telefone', '91234-5555', True),
      ('gabriel', 'telefone', '98888-1111', True),
      ('gabriel', 'telefone', '56789-1010', True)
    ]

    res = apply_schema_rules(facts, rules)
    if res != expected:
        return "Fail: teste 6"
    else:
        return "Success: teste 6"


# Run all tests
for test in [test1, test2, test3, test4, test5, test6]:
    res = test()
    print(res)
