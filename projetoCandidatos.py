import random

class Candidato:
    def __init__(self, nome, partido, voto):
        self.nome = nome
        self.partido = partido
        self.voto = voto

    def __str__(self):
        return f'Nome: {self.nome}, Partido: {self.partido}, Votos: {self.voto}'


class Candidatos:

    @staticmethod
    def Dados():
        nomes = ["Betão Nelo", "Marta RossLinda", "BolsaNoah", "Çula", "Eu Diego"]
        partidos = ["Vai dar PT", "PLA", "UNI", "PUC", "BZ"]
        Ar1 = random.randint(1, 100)
        NomesCand = []

        for i in range(Ar1):
            nome = random.choice(nomes)
            partido_cand = random.choice(partidos)
            voto = random.randint(0, 1000)
            NomesCand.append(Candidato(nome, partido_cand, voto))
        return NomesCand

    @staticmethod
    def PrintaCandidato(NomesCand):
        for candidato in NomesCand:
            print(candidato)

    @staticmethod
    def OrdenaçãoNome(NomesCand):
        # Ordenação por nome, com critérios de desempate por voto e partido
        for cont in range(1, len(NomesCand)):
            TempCand = NomesCand[cont]
            contComp = cont - 1
            while contComp >= 0 and (NomesCand[contComp].nome > TempCand.nome or
                                     (NomesCand[contComp].nome == TempCand.nome and NomesCand[contComp].voto > TempCand.voto) or
                                     (NomesCand[contComp].nome == TempCand.nome and NomesCand[contComp].voto == TempCand.voto and NomesCand[contComp].partido > TempCand.partido)):
                NomesCand[contComp + 1] = NomesCand[contComp]
                contComp -= 1
            NomesCand[contComp + 1] = TempCand

    @staticmethod
    def OrdenaçãoPartido(NomesCand):
        # Ordenação por partido, com critérios de desempate por voto e nome
        for cont in range(len(NomesCand)):
            MenorCont = cont
            for j in range(cont + 1, len(NomesCand)):
                if (NomesCand[j].partido < NomesCand[MenorCont].partido or
                   (NomesCand[j].partido == NomesCand[MenorCont].partido and NomesCand[j].voto > NomesCand[MenorCont].voto) or
                   (NomesCand[j].partido == NomesCand[MenorCont].partido and NomesCand[j].voto == NomesCand[MenorCont].voto and NomesCand[j].nome < NomesCand[MenorCont].nome)):
                    MenorCont = j
            NomesCand[cont], NomesCand[MenorCont] = NomesCand[MenorCont], NomesCand[cont]

    @staticmethod
    def OrdenaçãoVoto(NomesCand):
        # Ordenação por votos, com critérios de desempate por nome e partido
        for cont in range(len(NomesCand)):
            MenorCont = cont
            for j in range(cont + 1, len(NomesCand)):
                if (NomesCand[j].voto < NomesCand[MenorCont].voto or
                   (NomesCand[j].voto == NomesCand[MenorCont].voto and NomesCand[j].nome < NomesCand[MenorCont].nome) or
                   (NomesCand[j].voto == NomesCand[MenorCont].voto and NomesCand[j].nome == NomesCand[MenorCont].nome and NomesCand[j].partido < NomesCand[MenorCont].partido)):
                    MenorCont = j
            NomesCand[cont], NomesCand[MenorCont] = NomesCand[MenorCont], NomesCand[cont]

    @staticmethod
    def PBCand(NomesCand, CandProcurado):
        esquerda, direita = 0, len(NomesCand) - 1

        while esquerda <= direita:
            centro = (esquerda + direita) // 2
            if NomesCand[centro].nome == CandProcurado:
                return centro
            elif NomesCand[centro].nome < CandProcurado:
                esquerda = centro + 1
            else:
                direita = centro - 1
        return -1


if __name__ == "__main__":
    NomesCand = Candidatos.Dados()

    print("Candidatos Concorridos:")
    Candidatos.PrintaCandidato(NomesCand)

    print("\nCandidatos em Ordem Alfabética (Nome):")
    Candidatos.OrdenaçãoNome(NomesCand)
    Candidatos.PrintaCandidato(NomesCand)

    print("\nCandidatos em Ordem por Votos:")
    Candidatos.OrdenaçãoVoto(NomesCand)
    Candidatos.PrintaCandidato(NomesCand)

    print("\nCandidatos em Ordem por Partido:")
    Candidatos.OrdenaçãoPartido(NomesCand)
    Candidatos.PrintaCandidato(NomesCand)

    # Pesquisa Binária
    CandProcurado = input("\nPesquise um Candidato (Nome) --> ")
    Candidatos.OrdenaçãoNome(NomesCand)  # Certificar-se que está ordenado por nome antes da pesquisa binária
    Result = Candidatos.PBCand(NomesCand, CandProcurado)

    if Result != -1:
        print("\nSegue o Candidato Procurado -->")
        print(NomesCand[Result])
    else:
        print("\nHmmm, Não Achei o que procura")
