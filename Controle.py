from Lista import Lista
from Trie import Trie
from Candidato import Candidato
from Bem import Bem
from time import perf_counter


class Controle:
    def __init__(self):
        self.__candidatos = Lista()
        self.__indiceCand = Trie()

    def carregarCandidatos(self, arquivo):
        with open(arquivo, encoding='latin1') as f:
            for linha in f:
                l = linha.strip().split(';')
#                 2 ANO_ELEICAO
#                 5 SIGLA_UF
#                 8 CODIGO_CARGO
#                 9 DESCRICAO_CARGO
#                 10 NOME_CANDIDATO
#                 11 SEQUENCIAL_CANDIDATO
#                 12 NUMERO_CANDIDATO
#                 13 CPF_CANDIDATO
#                 14 NOME_URNA_CANDIDATO
#                 16 DES_SITUACAO_CANDIDATURA
#                 17 NUMERO_PARTIDO
#                 18 SIGLA_PARTIDO
#                 19 NOME_PARTIDO
#                 24 CODIGO_OCUPACAO
#                 25 DESCRICAO_OCUPACAO
#                 26 DATA_NASCIMENTO
#                 30 DESCRICAO_SEXO
#                 32 DESCRICAO_GRAU_INSTRUCAO
#                 34 DESCRICAO_ESTADO_CIVIL
#                 39 SIGLA_UF_NASCIMENTO
#                 41 NOME_MUNICIPIO_NASCIMENTO
#                 44 DESC_SIT_TOT_TURNO
                cand = Candidato(eleicao=l[2].strip('"'),
                                 uf=l[5].strip('"'),
                                 cod_cargo=l[8].strip('"'),
                                 desc_cargo=l[9].strip('"'),
                                 nome=l[10].strip('"'),
                                 num_seq=l[11].strip('"'),
                                 num_urna=l[12].strip('"'),
                                 cpf=l[13].strip('"'),
                                 nome_urna=l[14].strip('"'),
                                 num_partido=l[17].strip('"'),
                                 nome_partido=l[19].strip('"'),
                                 sigla_partido=l[18].strip('"'),
                                 cod_profissao=l[24].strip('"'),
                                 profissao=l[25].strip('"'),
                                 data_nasc=l[26].strip('"'),
                                 sexo=l[30].strip('"'),
                                 instrucao=l[32].strip('"'),
                                 estado_civil=l[34].strip('"'),
                                 uf_nasc=l[39].strip('"'),
                                 nome_municipio=l[41].strip('"'),
                                 sit_pleito=l[44].strip('"'),
                                 sit_cand=l[16].strip('"'))
                # self.__candidatos.inserirOrdenado(cand)
                self.__candidatos.inserir(cand)
                self.__indiceCand[cand.num_seq] = cand

    def carregarBens(self, arquivo):
        with open(arquivo, encoding='latin1') as f:
            for linha in f:
                l = linha.strip().split(';')
# 5 SQ_CANDIDATO
# 6 CD_TIPO_BEM_CANDIDATO
# 7 DS_TIPO_BEM_CANDIDATO
# 8 DETALHE_BEM
# 9 VALOR_BEM
                bem = Bem(cod_tipo=int(l[6].strip('"')),
                          desc_tipo=l[7].strip('"'),
                          descricao=l[8].strip('"'),
                          valor=float(l[9].strip('"')))
                try:
                    # cand = self.__candidatos.pesquisa(l[5].strip('"'), key='num_seq')
                    cand = self.__indiceCand.buscar(l[5].strip('"'))
                    cand.inserirBem(bem)
                except ValueError:
                    pass
                except KeyError:
                    pass

    def candidatos(self):
        return self.__candidatos

    def candidatos2(self):
        return self.__indiceCand


class Cronometro:
    ''' Cronometra tempo gasto desde a criacao ate a chamada do metodo
        tempo_gasto
    '''

    def __init__(self):
        self.__criacao = perf_counter()

    def inicia(self):
        self.__inicio = perf_counter()

    def para(self):
        self.__fim = perf_counter()

    def tempo_gasto(self):
        return self.__fim - self.__inicio


if __name__ == '__main__':
    UFs = ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA",
           "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN",
           "RO", "RR", "RS", "SC", "SE", "SP", "TO"]
    arq_cand = "consulta_cand_2014/consulta_cand_2014_{}.txt"
    arq_bem = "bem_candidato_2014/bem_candidato_2014_{}.txt"
    ctrl = Controle()

    cron = Cronometro()
    cron.inicia()
    for uf in UFs:
        ctrl.carregarCandidatos(arq_cand.format(uf))
    cron.para()
    tempoCand = cron.tempo_gasto()

    cron.inicia()
    for uf in UFs:
        ctrl.carregarBens(arq_bem.format(uf))
    cron.para()
    tempoBem = cron.tempo_gasto()
    frase = "Tempo gasto no carregamento dos dados dos "
    frase_cand = "{}candidatos: {:.3f}s".format(frase, tempoCand)
    frase_bens = "{}bens dos candidatos: {:.3f}s\n".format(frase, tempoBem)
    arquivo = open("saida.txt", "a")
    arquivo.write(frase_cand+"\n")
    arquivo.write(frase_bens+"\n")
    print(frase_cand)
    print(frase_bens)

    i = 0
    for c in ctrl.candidatos():
        arquivo.write(str(c)+"\n")
        print(c)
        if i > 4:
            break
        i += 1
    arquivo.close()
