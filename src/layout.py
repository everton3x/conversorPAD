''' Arquivo com o layout dos arquivos txt
'''

class Layout:

    TYPE_INT = 'int64'
    TYPE_STR = 'str'
    TYPE_DATE = 'datetime64[ns]'

    def __init__(self):
        # arquivo: {
        #   (id_coluna, tipo, primeira coluna, ultima coluna, formatador)
        # }
        self.specs = {
            'empenho': [
                ('orgao', self.TYPE_INT, 1, 2, None),
                ('uniorcam', self.TYPE_INT, 1, 4, None),
                ('funcao', self.TYPE_INT, 5, 6, None),
                ('subfuncao', self.TYPE_INT, 7, 9, None),
                ('programa', self.TYPE_INT, 10, 13, None),
                ('projativ', self.TYPE_INT, 17, 21, None),
                ('ndo', self.TYPE_INT, 22, 36, None),
                ('rv', self.TYPE_INT, 37, 40, None),
                ('contrapartida', self.TYPE_INT, 41, 44, None),
                ('nr_empenho', self.TYPE_INT, 45, 57, None),
                ('data_empenho', self.TYPE_DATE, 58, 65, None),
                ('valor_empenho', None, 66, 78, Converters.valor),
                ('sinal_valor', self.TYPE_STR, 79, 79, None),
                ('credor', self.TYPE_INT, 80, 89, None),
                ('cp', self.TYPE_INT, 255, 257, None),
                ('reg_preco', self.TYPE_STR, 260, 260, None),
                ('nr_licit', self.TYPE_INT, 281, 300, None),
                ('ano_licit', self.TYPE_INT, 301, 304, None),
                ('historico_empenho', self.TYPE_STR, 305, 704, None),
                ('modal_contrat', self.TYPE_STR, 705, 707, None),
                ('base_legal', self.TYPE_STR, 708, 709, None),
                ('identificador_folha', self.TYPE_STR, 710, 710, None)
            ],
            'liquidac': [
                ('nr_empenho', self.TYPE_INT, 1, 13, None),
                ('nr_liquidacao', self.TYPE_INT, 14, 33, None),
                ('data_liquidacao', self.TYPE_DATE, 34, 41, None),
                ('valor_liquidacao', None, 42, 54, Converters.valor),
                ('sinal_valor', self.TYPE_STR, 55, 55, None),
                ('cod_operacao', self.TYPE_STR, 221, 250, None),
                ('historico_liquidacao', self.TYPE_STR, 251, 650, None),
                ('existe_contrato', self.TYPE_STR, 651, 651, None),
                ('nr_contrato_tce', self.TYPE_INT, 652, 671, None),
                ('nr_contrato', self.TYPE_STR, 672, 691, None),
                ('ano_contrato', self.TYPE_INT, 692,695 , None),
                ('existe_nf', self.TYPE_STR, 696, 696, None),
                ('nr_nf', self.TYPE_INT, 697, 705, None),
                ('serie_nf', self.TYPE_STR, 706, 708, None),
                ('tipo_contrato', self.TYPE_STR, 709, 709, None)
            ],
            'pagament': [
                ('nr_empenho', self.TYPE_INT, 1, 13, None),
                ('nr_pagamento', self.TYPE_INT, 14, 33, None),
                ('data_pagamento', self.TYPE_DATE, 34, 41, None),
                ('valor_pagamento', None, 42, 54, Converters.valor),
                ('sinal_valor', self.TYPE_STR, 55, 55, None),
                ('cod_operacao', self.TYPE_STR, 176, 205, None),
                ('conta_debito', None, 206, 225, Converters.conta),
                ('uniorcam_debito', self.TYPE_INT, 226, 229, None),
                ('conta_credito', None, 230, 249, Converters.conta),
                ('uniorcam_credito', self.TYPE_INT, 250, 253, None),
                ('historico_pagamento', self.TYPE_STR, 254, 653, None),
                ('nr_liquidacao', self.TYPE_INT, 654, 673, None),
            ],
            'bal_rec': [
                ('nro', self.TYPE_INT, 1, 20, None),
                ('uniorcam', self.TYPE_INT, 21, 24, None),
                ('receita_orcada', None, 25, 37, Converters.valor),
                ('receita_arrecadada', None, 38, 50, Converters.valor),
                ('rv', self.TYPE_INT, 51, 54, None),
                ('receita', self.TYPE_STR, 55, 224, None),
                ('tipo_nivel', self.TYPE_STR, 225, 225, None),
                ('nr_nivel', self.TYPE_INT, 226, 227, None),
                ('cp', self.TYPE_INT, 228, 230, None),
                ('previsao_atualizada', None, 231, 243, Converters.valor)
            ],
            'receita': [
                ('nro', self.TYPE_INT, 1, 20, None),
                ('uniorcam', self.TYPE_INT, 21, 24, None),
                ('arrec_janeiro', None, 25, 37, Converters.valor),
                ('arrec_fevereiro', None, 38, 50, Converters.valor),
                ('arrec_marco', None, 51, 63, Converters.valor),
                ('arrec_abril', None, 64, 76, Converters.valor),
                ('arrec_maio', None, 77, 89, Converters.valor),
                ('arrec_junho', None, 90, 102, Converters.valor),
                ('arrec_julho', None, 103, 115, Converters.valor),
                ('arrec_agosto', None, 116, 128, Converters.valor),
                ('arrec_setembro', None, 129, 141, Converters.valor),
                ('arrec_outubro', None, 142, 154, Converters.valor),
                ('arrec_novembro', None, 155, 167, Converters.valor),
                ('arrec_dezembro', None, 168, 180, Converters.valor),
                ('meta_1bim', None, 181, 192, Converters.valor),
                ('meta_2bim', None, 193, 204, Converters.valor),
                ('meta_3bim', None, 205, 216, Converters.valor),
                ('meta_4bim', None, 217, 228, Converters.valor),
                ('meta_5bim', None, 229, 240, Converters.valor),
                ('meta_6bim', None, 241, 252, Converters.valor),
                ('cp', self.TYPE_INT, 253, 255, None),
                ('rv', self.TYPE_INT, 256, 259, None)
            ],
            'bal_desp': [
                ('orgao', self.TYPE_INT, 1, 2, None),
                ('uniorcam', self.TYPE_INT, 1, 4, None),
                ('funcao', self.TYPE_INT, 5, 6, None),
                ('subfuncao', self.TYPE_INT, 7, 9, None),
                ('programa', self.TYPE_INT, 10, 13, None),
                ('projativ', self.TYPE_INT, 17, 21, None),
                ('elemento', self.TYPE_INT, 22, 27, None),
                ('rv', self.TYPE_INT, 28, 31, None),
                ('dotacao_inicial', None, 32, 44, Converters.valor),
                ('atualizacao', None, 45, 57, Converters.valor),
                ('suplementar', None, 58, 70, Converters.valor),
                ('especial', None, 71, 83, Converters.valor),
                ('extraordinario', None, 84, 96, Converters.valor),
                ('reducao', None, 97, 109, Converters.valor),
                ('suplementar_rv', None, 110, 122, Converters.valor),
                ('reducao_rv', None, 123, 135, Converters.valor),
                ('empenhado', None, 136, 148, Converters.valor),
                ('liquidado', None, 149, 161, Converters.valor),
                ('pago', None, 162, 174, Converters.valor),
                ('limitado', None, 175, 187, Converters.valor),
                ('recomposicao', None, 188, 200, Converters.valor),
                ('previsao_termino', None, 201, 213, Converters.valor)
            ],
            'bal_ver': [
                ('conta', None, 1, 20, Converters.conta),
                ('uniorcam', self.TYPE_INT, 21, 24, None),
                ('anterior_debito', None, 25, 37, Converters.valor),
                ('anterior_credito', None, 38, 50, Converters.valor),
                ('movimento_debito', None, 51, 63, Converters.valor),
                ('movimento_credito', None, 64, 76, Converters.valor),
                ('atual_debito', None, 77, 89, Converters.valor),
                ('atual_credito', None, 90, 102, Converters.valor),
                ('nome_conta', self.TYPE_STR, 103, 250, None),
                ('tipo_nivel', self.TYPE_STR, 251, 251, None),
                ('nr_nivel', self.TYPE_INT, 252, 253, None),
                ('escrituravel', self.TYPE_STR, 255, 255, None),
                ('natureza', self.TYPE_STR, 256, 256, None),
                ('superavit', self.TYPE_STR, 257, 257, None),
                ('rv', self.TYPE_INT, 258, 261, None),
            ],
            'bver_enc': [
                ('conta', None, 1, 20, Converters.conta),
                ('uniorcam', self.TYPE_INT, 21, 24, None),
                ('anterior_debito', None, 25, 37, Converters.valor),
                ('anterior_credito', None, 38, 50, Converters.valor),
                ('movimento_debito', None, 51, 63, Converters.valor),
                ('movimento_credito', None, 64, 76, Converters.valor),
                ('atual_debito', None, 77, 89, Converters.valor),
                ('atual_credito', None, 90, 102, Converters.valor),
                ('nome_conta', self.TYPE_STR, 103, 250, None),
                ('tipo_nivel', self.TYPE_STR, 251, 251, None),
                ('nr_nivel', self.TYPE_INT, 252, 253, None),
                ('escrituravel', self.TYPE_STR, 255, 255, None),
                ('natureza', self.TYPE_STR, 256, 256, None),
                ('superavit', self.TYPE_STR, 257, 257, None),
                ('rv', self.TYPE_INT, 258, 261, None),
            ],
            'rd_extra': [
                ('conta', None, 1, 20, Converters.conta),
                ('uniorcam', self.TYPE_INT, 21, 24, None),
                ('valor', None, 25, 37, Converters.valor),
                ('identificador', self.TYPE_STR, 38, 38, None),
                ('classificacao', self.TYPE_INT, 39, 48, None)
            ],
            'decreto': [
                ('nr_lei', self.TYPE_STR, 1, 20, None),
                ('data_lei', self.TYPE_DATE, 21, 28, None),
                ('nr_decreto', self.TYPE_STR, 29, 48, None),
                ('data_decreto', self.TYPE_DATE, 49, 56, None),
                ('adicional', None, 57, 69, Converters.valor),
                ('reducao', None, 70, 82, Converters.valor),
                ('tipo_credito', self.TYPE_INT, 83, 83, None),
                ('origem_recurso', self.TYPE_INT, 84, 84, None)
            ],
            'brec_ant': [
                ('nro', self.TYPE_INT, 1, 20, None),
                ('uniorcam', self.TYPE_INT, 21, 24, None),
                ('receita_orcada', None, 25, 37, Converters.valor),
                ('receita_arrecadada', None, 38, 50, Converters.valor),
                ('rv', self.TYPE_INT, 51, 54, None),
                ('receita', self.TYPE_STR, 55, 224, None),
                ('tipo_nivel', self.TYPE_STR, 225, 225, None),
                ('nr_nivel', self.TYPE_INT, 226, 227, None),
                ('cp', self.TYPE_INT, 228, 230, None)
            ],
            'rec_ant': [
                ('nro', self.TYPE_INT, 1, 20, None),
                ('uniorcam', self.TYPE_INT, 21, 24, None),
                ('arrec_janeiro', None, 25, 37, Converters.valor),
                ('arrec_fevereiro', None, 38, 50, Converters.valor),
                ('arrec_marco', None, 51, 63, Converters.valor),
                ('arrec_abril', None, 64, 76, Converters.valor),
                ('arrec_maio', None, 77, 89, Converters.valor),
                ('arrec_junho', None, 90, 102, Converters.valor),
                ('arrec_julho', None, 103, 115, Converters.valor),
                ('arrec_agosto', None, 116, 128, Converters.valor),
                ('arrec_setembro', None, 129, 141, Converters.valor),
                ('arrec_outubro', None, 142, 154, Converters.valor),
                ('arrec_novembro', None, 155, 167, Converters.valor),
                ('arrec_dezembro', None, 168, 180, Converters.valor),
                ('cp', self.TYPE_INT, 181, 183, None),
                ('rv', self.TYPE_INT, 184, 187, None)
            ],
            'brub_ant': [
                ('orgao', self.TYPE_INT, 1, 2, None),
                ('uniorcam', self.TYPE_INT, 1, 4, None),
                ('funcao', self.TYPE_INT, 5, 6, None),
                ('subfuncao', self.TYPE_INT, 7, 9, None),
                ('programa', self.TYPE_INT, 10, 13, None),
                ('projativ', self.TYPE_INT, 17, 21, None),
                ('elemento', self.TYPE_INT, 22, 36, None),
                ('rv', self.TYPE_INT, 37, 40, None),
                ('empenhado_1bim', None, 41, 51, Converters.valor),
                ('empenhado_2bim', None, 52, 62, Converters.valor),
                ('empenhado_3bim', None, 63, 73, Converters.valor),
                ('empenhado_4bim', None, 74, 84, Converters.valor),
                ('empenhado_5bim', None, 85, 95, Converters.valor),
                ('empenhado_6bim', None, 96, 106, Converters.valor),
                ('liquidado_1bim', None, 107, 117, Converters.valor),
                ('liquidado_2bim', None, 118, 128, Converters.valor),
                ('liquidado_3bim', None, 129, 139, Converters.valor),
                ('liquidado_4bim', None, 140, 150, Converters.valor),
                ('liquidado_5bim', None, 151, 161, Converters.valor),
                ('liquidado_6bim', None, 162, 172, Converters.valor),
                ('pago_1bim', None, 173, 172, Converters.valor),
                ('pago_2bim', None, 184, 194, Converters.valor),
                ('pago_3bim', None, 195, 205, Converters.valor),
                ('pago_4bim', None, 206, 216, Converters.valor),
                ('pago_5bim', None, 217, 227, Converters.valor),
                ('pago_6bim', None, 228, 238, Converters.valor)
            ],
            'bver_ant': [
                ('conta', None, 1, 20, Converters.conta),
                ('uniorcam', self.TYPE_INT, 21, 24, None),
                ('anterior_debito', None, 25, 37, Converters.valor),
                ('anterior_credito', None, 38, 50, Converters.valor),
                ('movimento_debito', None, 51, 63, Converters.valor),
                ('movimento_credito', None, 64, 76, Converters.valor),
                ('atual_debito', None, 77, 89, Converters.valor),
                ('atual_credito', None, 90, 102, Converters.valor),
                ('nome_conta', self.TYPE_STR, 103, 250, None),
                ('tipo_nivel', self.TYPE_STR, 251, 251, None),
                ('nr_nivel', self.TYPE_INT, 252, 253, None),
                ('escrituravel', self.TYPE_STR, 255, 255, None),
                ('natureza', self.TYPE_STR, 256, 256, None),
                ('superavit', self.TYPE_STR, 257, 257, None)
            ],
            'bvmovant': [
                ('conta', None, 1, 20, Converters.conta),
                ('uniorcam', self.TYPE_INT, 21, 24, None),
                ('debito_1bim', None, 25, 37, Converters.valor),
                ('credito_1bim', None, 38, 50, Converters.valor),
                ('debito_2bim', None, 51, 63, Converters.valor),
                ('credito_2bim', None, 64, 76, Converters.valor),
                ('debito_3bim', None, 77, 89, Converters.valor),
                ('credito_3bim', None, 90, 102, Converters.valor),
                ('debito_4bim', None, 103, 115, Converters.valor),
                ('credito_4bim', None, 116, 128, Converters.valor),
                ('debito_5bim', None, 129, 141, Converters.valor),
                ('credito_5bim', None, 142, 154, Converters.valor),
                ('debito_6bim', None, 155, 167, Converters.valor),
                ('credito_6bim', None, 168, 180, Converters.valor)
            ],
            'orgao': [
                ('exercicio', self.TYPE_INT, 1, 4, None),
                ('codigo', self.TYPE_INT, 5, 6, None),
                ('orgao', self.TYPE_STR, 7, 86, None)
            ],
            'uniorcam': [
                ('exercicio', self.TYPE_INT, 1, 4, None),
                ('orgao', self.TYPE_INT, 5, 6, None),
                ('codigo', self.TYPE_INT, 5, 8, None),
                ('uniorcam', self.TYPE_STR, 9, 88, None),
                ('identificador', self.TYPE_INT, 89, 90, None),
                ('cnpj', self.TYPE_INT, 91, 104, None)
            ],
            'funcao': [
                ('exercicio', self.TYPE_INT, 1, 4, None),
                ('codigo', self.TYPE_INT, 5, 6, None),
                ('funcao', self.TYPE_STR, 7, 86, None)
            ],
            'subfunc': [
                ('exercicio', self.TYPE_INT, 1, 4, None),
                ('codigo', self.TYPE_INT, 5, 7, None),
                ('subfuncao', self.TYPE_STR, 8, 87, None)
            ],
            'programa': [
                ('exercicio', self.TYPE_INT, 1, 4, None),
                ('codigo', self.TYPE_INT, 5, 8, None),
                ('subfuncao', self.TYPE_STR, 9, 88, None)
            ],
            'projativ': [
                ('exercicio', self.TYPE_INT, 1, 4, None),
                ('codigo', self.TYPE_INT, 5, 9, None),
                ('subfuncao', self.TYPE_STR, 10, 89, None),
                ('identificador', self.TYPE_INT, 90, 91, None)
            ],
            'rubrica': [
                ('exercicio', self.TYPE_INT, 1, 4, None),
                ('codigo', self.TYPE_INT, 5, 19, None),
                ('rubrica', self.TYPE_STR, 20, 129, None),
                ('tipo_nivel', self.TYPE_STR, 130, 130, None),
                ('nr_nivel', self.TYPE_INT, 131, 132, None),
            ],
            'recurso': [
                ('codigo', self.TYPE_INT, 1, 4, None),
                ('recurso', self.TYPE_STR, 5, 84, None),
                ('finalidade', self.TYPE_STR, 85, 244, None)
            ],
            'credor': [
                ('codigo', self.TYPE_INT, 1, 10, None),
                ('nome', self.TYPE_STR, 11, 70, None),
                ('cnpj_cpf', self.TYPE_INT, 71, 84, None),
                ('inscricao_estadual', self.TYPE_INT, 85, 99, None),
                ('inscricao_municipal', self.TYPE_INT, 100, 114, None),
                ('endereco', self.TYPE_STR, 115, 164, None),
                ('cidade', self.TYPE_STR, 165, 194, None),
                ('uf', self.TYPE_STR, 195, 196, None),
                ('cep', self.TYPE_INT, 197, 204, None),
                ('fone', self.TYPE_INT, 205, 219, None),
                ('fax', self.TYPE_INT, 220, 234, None),
                ('tipo_credor', self.TYPE_INT, 235, 236, None),
                ('tipo_pessoa', self.TYPE_INT, 237, 238, None)
            ],
            'cta_disp': [
                ('conta', None, 1, 20, Converters.conta),
                ('uniorcam', self.TYPE_INT, 21, 24, None),
                ('rv', self.TYPE_INT, 25, 28, None),
                ('banco', self.TYPE_INT, 29, 33, None),
                ('agencia', self.TYPE_STR, 34, 38, None),
                ('conta_corrente', self.TYPE_STR, 39, 58, None),
                ('tipo_conta', self.TYPE_INT, 59, 59, None),
                ('classificacao', self.TYPE_INT, 60, 60, None)
            ],
            'cta_oper': [
                ('codigo_operacao', self.TYPE_STR, 1, 30, None),
                ('data_operacao', self.TYPE_DATE, 31, 38, None),
                ('valor_operacao', None, 39, 51, Converters.valor),
                ('sinal_valor', self.TYPE_STR, 52, 52, None),
                ('rv', self.TYPE_INT, 53, 56, None),
                ('nro', self.TYPE_INT, 57, 76, None),
                ('uniorcam_receita', self.TYPE_INT, 77, 80, None),
                ('conta', None, 81, 100, Converters.conta),
                ('uniorcam_conta', self.TYPE_INT, 101, 104, None)
            ]
        }

    def date_cols(self, file):
        date_cols = []
        for row in self.specs[file]:
            name, dtype, _, _, _ = row
            if (dtype != None) and (dtype.startswith('date')):
                date_cols.append(name)

        # print(date_cols)
        return date_cols

    def converters(self, file):
        converters = {}
        for row in self.specs[file]:
            name, _, _, _, conv = row
            if conv is not None:
                converters[name] = conv

        return converters

    def colspecs(self, file):
        colspecs = []
        for row in self.specs[file]:
            _, _, first, last, _ = row
            # last += 1
            first -= 1
            colspecs.append((first, last))
        # print(colspecs)
        return colspecs

    def dtypes(self, file):
        dtypes = {}
        for row in self.specs[file]:
            name, dtype, _, _, _ = row
            dtypes[name] = dtype

        return dtypes

    def names(self, file):
        names = []
        for row in self.specs[file]:
            name, _, _, _, _ = row
            names.append(name)
        return names

    def has_layout(self, layout):
        if layout in self.specs:
            return True
        else:
            return False


class Converters:

    @staticmethod
    def valor(original):
        reais = int(original[0:len(original) - 2])
        centavos = original[len(original) - 2:]
        return float('{0}.{1}'.format(reais, centavos))

    @staticmethod
    def conta(original):
        return original.lstrip('0').ljust(20,'0')
