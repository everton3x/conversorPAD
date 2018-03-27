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
                ('uniorcam', self.TYPE_INT, 3, 4, None),
                ('funcao', self.TYPE_INT, 5, 6, None),
                ('subfuncao', self.TYPE_INT, 7, 9, None),
                ('programa', self.TYPE_INT, 10, 13, None),
                ('projativop', self.TYPE_INT, 17, 21, None),
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
