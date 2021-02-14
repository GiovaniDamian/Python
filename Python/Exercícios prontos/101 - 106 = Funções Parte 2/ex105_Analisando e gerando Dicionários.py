def notas(*n, sit=False):
    """
    ->Função para analisar notas e situação dos alunos
    :param n: uma ou mais notas do aluno
    :param sit:valor opcional, indicando se deve ou não adicionar a situação
    :return:dicionário com várias informações sobre a situação da turma
    """
    aluno = dict()
    aluno['Total'] = len(n)
    aluno['Maior'] = max(n)
    aluno['Menor'] = min(n)
    aluno['Média'] = sum(n)/len(n)
    if sit:
        if aluno['Média'] >= 7:
            aluno['Situação'] = 'BOA'
        elif aluno['Média'] >= 5:
            aluno['Situação'] = 'RAZOÁVEL'
        else:
            aluno['Situação'] = 'RUIM'
    return aluno


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
