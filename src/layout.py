''' Arquivo com o layout dos arquivos txt
'''


class Layout:

    def __init__(self):
        # arquivo: {
        #   (id_coluna, tipo, primeira coluna, ultima coluna, formatador, é data?)
        # }
        self.specs = {
            'empenho': [
                ('orgao', 'int', 1, 2, '', False),
                ('uniorcam', 'int', 3, 4, '', False),
                ('funcao', 'int', 5, 6, '', False),
                ('subfuncao', 'int', 7, 9, '', False),
                ('programa', 'int', 10, 13, '', False),
                ('projativop', 'int', 17, 21, '', False),
                ('ndo', 'str', 22, 36, '', False),
                ('rv', 'int', 37, 40, '', False),
                ('contrapartida', 'int', 41, 44, '', False),
                ('nr_empenho', 'str', 45, 57, '', False),
                ('data_empenho', 'str', 58, 65, '', True),
                ('valor_empenho', 'int', 66, 78, '', False),
                ('sinal_valor', 'str', 79, 79, '', False),
                ('credor', 'int', 80, 89, '', False),
                ('cp', 'int', 255, 257, '', False),
                ('reg_preco', 'str', 260, 260, '', False),
                ('nr_licit', 'int', 281, 300, '', False),
                ('ano_licit', 'int', 301, 304, '', False),
                ('historico', 'str', 305, 704, '', False),
                ('modal_contrat', 'str', 705, 707, '', False),
                ('base_legal', 'str', 708, 709, '', False),
                ('identificador_folha', 'str', 710, 710, '', False)
            ]
        }

    def date_cols(self, file):
        date_cols = []
        for row in self.specs[file]:
            name, _, _, _, _, isdate = row
            if isdate:
                date_cols.append(name)

        # print(date_cols)
        return date_cols

    def colspecs(self, file):
        colspecs = []
        for row in self.specs[file]:
            _, _, first, last, _, _ = row
            # last += 1
            first -= 1
            colspecs.append((first, last))
        # print(colspecs)
        return colspecs

    def dtypes(self, file):
        dtypes = {}
        for row in self.specs[file]:
            name, dtype, _, _, _, _ = row
            dtypes[name] = dtype

        return dtypes

    def names(self, file):
        names = []
        for row in self.specs[file]:
            name, _, _, _, _, _ = row
            names.append(name)
        return names

    def has_layout(self, layout):
        if layout in self.specs:
            return True
        else:
            return False
