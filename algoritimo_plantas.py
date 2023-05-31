from banco_de_dados import Banco
from comparador_plantas import ComparadorPlantas
import time
banco = Banco()
comp = ComparadorPlantas()


def verificar_status_planta(planta_dict):
    id_planta = planta_dict.get("id_planta")
    tipo_planta = planta_dict.get("tipo_planta")
    status = match_case_planta(tipo_planta, planta_dict)
    banco.update_plant_status(id_planta, status["status"])
    banco.update_plant_warnings(id_planta, status["warnings"])


def escanear_banco():
    plantas_dict = banco.get_lista_de_plantas()
    for i in range(len(plantas_dict)):
        planta_dict = plantas_dict.get(i)
        verificar_status_planta(planta_dict)


def match_case_planta(planta, planta_dict):
    match planta:
        case "tomato":
            print(planta_dict)
            comparacao_dict = {"temperatura": {"favoravel": (25, 30), "neutro": {"comp1": (20, 25), "comp2": None}},
                               "umidade": {"favoravel": (60, 70), "neutro": {"comp1": (40, 60), "comp2": None}},
                               "luz": {"favoravel": (8, 10), "neutro": {"comp1": (6, 8), "comp2": None}},
                               "ph": {"favoravel": (6, 6.8), "neutro": {"comp1": (5.5, 6), "comp2": (6.8, 8)}}}
            resposta = comp.comparar_universal(planta_dict, comparacao_dict)
            print(resposta, "\n")
            return resposta
        case "peper":
            print(planta_dict)
            comparacao_dict = {"temperatura": {"favoravel": (25, 30), "neutro": {"comp1": (20, 25), "comp2": None}},
                               "umidade": {"favoravel": (60, 70), "neutro": {"comp1": (40, 60), "comp2": None}},
                               "luz": {"favoravel": (8, 10), "neutro": {"comp1": (6, 8), "comp2": None}},
                               "ph": {"favoravel": (6, 6.8), "neutro": {"comp1": (5.5, 6), "comp2": (6.8, 8)}}}
            resposta = comp.comparar_universal(planta_dict, comparacao_dict)
            print(resposta, "\n")
            return resposta
        case "zucchini":
            print(planta_dict)
            comparacao_dict = {"temperatura": {"favoravel": (24, 30), "neutro": {"comp1": (18, 24), "comp2": None}},
                               "umidade": {"favoravel": (60, 70), "neutro": {"comp1": (40, 60), "comp2": None}},
                               "luz": {"favoravel": (8, 10), "neutro": {"comp1": (6, 8), "comp2": None}},
                               "ph": {"favoravel": (6, 6.8), "neutro": {"comp1": (5.5, 6), "comp2": (6.8, 8)}}}
            resposta = comp.comparar_universal(planta_dict, comparacao_dict)
            print(resposta, "\n")
            return resposta
        case "lettuce":
            print(planta_dict)
            comparacao_dict = {"temperatura": {"favoravel": (10, 15), "neutro": {"comp1": (15, 25), "comp2": None}},
                               "umidade": {"favoravel": (50, 70), "neutro": {"comp1": (40, 50), "comp2": (70, 80)}},
                               "luz": {"favoravel": (4, 6), "neutro": {"comp1": (6, 8), "comp2": None}},
                               "ph": {"favoravel": (6, 6.8), "neutro": {"comp1": (5.5, 6), "comp2": (6.8, 8)}}}
            resposta = comp.comparar_universal(planta_dict, comparacao_dict)
            print(resposta, "\n")
            return resposta
        case "arugula":
            print(planta_dict)
            comparacao_dict = {"temperatura": {"favoravel": (10, 15), "neutro": {"comp1": (15, 25), "comp2": None}},
                               "umidade": {"favoravel": (50, 70), "neutro": {"comp1": (40, 50), "comp2": (70, 80)}},
                               "luz": {"favoravel": (4, 6), "neutro": {"comp1": (6, 8), "comp2": None}},
                               "ph": {"favoravel": (6, 6.8), "neutro": {"comp1": (5.5, 6), "comp2": (6.8, 8)}}}
            resposta = comp.comparar_universal(planta_dict, comparacao_dict)
            print(resposta, "\n")
            return resposta
        case "spinach":
            print(planta_dict)
            comparacao_dict = {"temperatura": {"favoravel": (5, 15), "neutro": {"comp1": (15, 25), "comp2": None}},
                               "umidade": {"favoravel": (50, 70), "neutro": {"comp1": (40, 50), "comp2": (70, 80)}},
                               "luz": {"favoravel": (2, 4), "neutro": {"comp1": (4, 6), "comp2": None}},
                               "ph": {"favoravel": (6, 7), "neutro": {"comp1": (5.5, 6), "comp2": (7, 8)}}}
            resposta = comp.comparar_universal(planta_dict, comparacao_dict)
            print(resposta, "\n")
            return resposta
        case "bean":
            print(planta_dict)
            comparacao_dict = {"temperatura": {"favoravel": (25, 30), "neutro": {"comp1": (20, 25), "comp2": None}},
                               "umidade": {"favoravel": (50, 70), "neutro": {"comp1": (40, 50), "comp2": (70, 80)}},
                               "luz": {"favoravel": (6, 8), "neutro": {"comp1": (4, 6), "comp2": (8, 10)}},
                               "ph": {"favoravel": (6, 6.8), "neutro": {"comp1": (5.5, 6), "comp2": (6.8, 8)}}}
            resposta = comp.comparar_universal(planta_dict, comparacao_dict)
            print(resposta, "\n")
            return resposta
        case "pea":
            print(planta_dict)
            comparacao_dict = {"temperatura": {"favoravel": (10, 15), "neutro": {"comp1": (15, 25), "comp2": None}},
                               "umidade": {"favoravel": (50, 70), "neutro": {"comp1": (40, 50), "comp2": (70, 80)}},
                               "luz": {"favoravel": (4, 6), "neutro": {"comp1": (6, 8), "comp2": None}},
                               "ph": {"favoravel": (6, 7), "neutro": {"comp1": (5.5, 6), "comp2": (7, 8)}}}
            resposta = comp.comparar_universal(planta_dict, comparacao_dict)
            print(resposta, "\n")
            return resposta
        case "lentil":
            print(planta_dict)
            comparacao_dict = {"temperatura": {"favoravel": (10, 15), "neutro": {"comp1": (15, 25), "comp2": None}},
                               "umidade": {"favoravel": (50, 70), "neutro": {"comp1": (40, 50), "comp2": (70, 80)}},
                               "luz": {"favoravel": (4, 6), "neutro": {"comp1": (6, 8), "comp2": None}},
                               "ph": {"favoravel": (6, 7), "neutro": {"comp1": (5.5, 6), "comp2": (7, 8)}}}
            resposta = comp.comparar_universal(planta_dict, comparacao_dict)
            print(resposta, "\n")
            return resposta
        case "carroto":
            print(planta_dict)
            comparacao_dict = {"temperatura": {"favoravel": (10, 15), "neutro": {"comp1": (15, 25), "comp2": None}},
                               "umidade": {"favoravel": (50, 70), "neutro": {"comp1": (40, 50), "comp2": (70, 80)}},
                               "luz": {"favoravel": (4, 6), "neutro": {"comp1": (6, 8), "comp2": None}},
                               "ph": {"favoravel": (6, 7), "neutro": {"comp1": (5.5, 6), "comp2": (7, 8)}}}
            resposta = comp.comparar_universal(planta_dict, comparacao_dict)
            print(resposta, "\n")
            return resposta
        case "beet":
            print(planta_dict)
            comparacao_dict = {"temperatura": {"favoravel": (10, 15), "neutro": {"comp1": (15, 25), "comp2": None}},
                               "umidade": {"favoravel": (50, 70), "neutro": {"comp1": (40, 50), "comp2": (70, 80)}},
                               "luz": {"favoravel": (4, 6), "neutro": {"comp1": (6, 8), "comp2": None}},
                               "ph": {"favoravel": (6, 7), "neutro": {"comp1": (5.5, 6), "comp2": (7, 8)}}}
            resposta = comp.comparar_universal(planta_dict, comparacao_dict)
            print(resposta, "\n")
            return resposta
        case "radish":
            print(planta_dict)
            comparacao_dict = {"temperatura": {"favoravel": (10, 15), "neutro": {"comp1": (15, 25), "comp2": None}},
                               "umidade": {"favoravel": (50, 70), "neutro": {"comp1": (40, 50), "comp2": (70, 80)}},
                               "luz": {"favoravel": (4, 6), "neutro": {"comp1": (6, 8), "comp2": None}},
                               "ph": {"favoravel": (6, 7), "neutro": {"comp1": (5.5, 6), "comp2": (7, 8)}}}
            resposta = comp.comparar_universal(planta_dict, comparacao_dict)
            print(resposta, "\n")
            return resposta

