# -*- coding: utf-8 -*-


def build_schema_rules(schema):
    # Constroi e retorna um dicionario para cada chave atributo com seu valor
    # Um atributo só pode possuir uma regra
    ret = {}
    for [att, card, qnt] in schema:
        if qnt == 'one' or qnt == 'many':
            if card == 'cardinality':
                ret[att] = qnt
    return ret


def apply_schema_rules(facts, rules):
    # Constroi e retorna uma lista de tuplas dos fatos validos
    facts.reverse()
    result = list(facts)
    removed = []  # Lista com atributos que ja foram removidos pela regra 'one'

    for [e, a, v, added] in facts:  # entidade (E), atributo (A), valor (V) e added

        if a not in rules:  # Se atributo 'a' não possui uma regra, remove fato
            result.remove((e, a, v, added))

        elif not added:  # Se added é false, fato não entra e remove se ouver algum outro igual
            for [ve, va, vv, vadded] in result:
                if ve == e and va == a:
                    result.remove((ve, va, vv, vadded))

        elif rules[a] == 'one':  # Se para o atributo 'a' a regra é one, remove todos os outros
            if (e, a) in removed:
                continue
            for [ve, va, vv, vadded] in result:
                if ve == e and va == a and vv != v:
                    result.remove((ve, va, vv, vadded))
                    removed.append((e, a))

    result.reverse()
    return result


def current_facts(facts, schema):
    # A função recebe `facts` (todos fatos conhecidos) e `schema` como argumentos.
    # Facts são compostos por entidade (E), atributo (A), valor (V) e added? no formato (E, A, V, added?)
    # Schema dita as regras de cardinalidade dos atributos, podendo ser 'one' ou 'many'

    # Se facts vazio, retornar lista vazia
    if facts is None or facts == []:
        return []

    # Construir regras
    rules = build_schema_rules(schema)

    # Aplicar regras
    ret = apply_schema_rules(facts, rules)
    return ret
