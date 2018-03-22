''' Arquivo com o layout dos arquivos txt
'''

class Layout:

    def __init__(self):
        # arquivo: {
        #   (id_coluna, tipo, primeira coluna, ultima coluna, formatador)
        # }
        self.specs = {
            'empenho': [
                ('orgao', 'int', 1, 2, ''),
                ('uniorcam', 'int', 3, 4, ''),
                ('funcao', 'int', 5, 6, ''),
                ('subfuncao', 'int', 7, 9, ''),
                ('programa', 'int', 10, 13, ''),
                ('projativop', 'int', 17, 21, ''),
                ('ndo', 'int64', 22, 36, ''),
                ('rv', 'int', 37, 40, ''),
                ('contrapartida', 'int', 41, 44, ''),
                ('nr_empenho', 'int64', 45, 57, ''),
                ('data_empenho', 'datetime64[ns]', 58, 65, ''),
                ('valor_empenho', None, 66, 78, Converters.valor),
                ('sinal_valor', 'str', 79, 79, ''),
                ('credor', 'int', 80, 89, ''),
                ('cp', 'int', 255, 257, ''),
                ('reg_preco', 'str', 260, 260, ''),
                ('nr_licit', 'int', 281, 300, ''),
                ('ano_licit', 'int', 301, 304, ''),
                ('historico', 'str', 305, 704, ''),
                ('modal_contrat', 'str', 705, 707, ''),
                ('base_legal', 'str', 708, 709, ''),
                ('identificador_folha', 'str', 710, 710, '')
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
            if conv != '':
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
