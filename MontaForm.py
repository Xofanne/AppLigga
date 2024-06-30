import requests

class EnviaForm:

    def FillForm(Dados):

        if Dados.CPF.CPF.get() == "":
            nome = Dados.CNPJ.RazaoSocial.get()
            doc = Dados.CNPJ.CNPJ.get()
        else:
            nome = Dados.Cliente.Nome.get()
            doc = Dados.CPF.CPF.get()

        value = {
    # Cep (required)
    #   Option: any text
    "entry.1690259070": Dados.Cliente.CEP.get(),
    # Endereço (required)
    #   Option: any text
    "entry.1064235413": Dados.Cliente.Rua.get(),
    # Complemento
    #   Option: any text
    "entry.1599573058": Dados.Cliente.Complemento.get(),
    # Número (required)
    #   Option: any text
    "entry.182259312": Dados.Cliente.Numero.get(),
    # Cidade (required)
    #   Option: any text
    "entry.1828596069": Dados.Cliente.Cidade.get(),
    # CPF / CNPJ (required)
    #   Option: any text
    "entry.1603772010": doc,
    # Nome do Cliente (required)
    #   Option: any text
    "entry.948186743": nome,
    # Telefone (required)
    #   Option: any text
    "entry.1098815865": Dados.Cliente.Telefone.get(),
    # E-mail (required)
    #   Option: any text
    "entry.1858565817": Dados.Cliente.Email.get(),
    # Plano Contratado (required)
    #   Options: ['100 MB', '200 MB', '400 MB', '500 MB', '600 MB', '700 MB', '1 Gb']
    "entry.1924736303": Dados.Cliente.Velocidade.get(),
    # Adicionais (required)
    #   Options: ['HBO', 'Paramount', 'Mesh', 'Seguro Residencial', 'Rastr. Veicular', 'Monit. Residencial']
    "entry.1274466521": Dados.Cliente.Adicionais,
    # Data de instalação
    #   Option: any text
    "entry.1652985137": Dados.Cliente.DataInstalacao.get(),
    # Período da Instalação (required)
    #   Options: ['Manhã', 'Tarde']
    "entry.1409046645": Dados.Cliente.Periodo.get(),
    # Observação
    #   Option: any text
    "entry.527229650": Dados.Opcionais.OBS.get(),
    # Entrada (required)
    #   Options: ['Receptivo', 'Ativo', 'Whatsapp']
    "entry.1927730902": Dados.Operador.Entrada.get(),
    # Categoria (required)
    #   Options: ['Ligga', 'Nova', 'Rede Neutra']
    "entry.968955457": Dados.Cliente.Empresa.get(),
    # Matrícula (required)
    #   Options: ['29922', '33776', '32817', '20417', '28219', '33777', '34066', '34204', '34335']
    "entry.131314365": Dados.Operador.Matricula.get(),
    # Page History
    #   Options: from 0 to (number of page - 1)
    "pageHistory": "0,1,2,3,4"
}
        {
    # Cep (required)
    #   Option: any text
    "entry.1690259070": "",
    # Endereço (required)
    #   Option: any text
    "entry.1064235413": "",
    # Complemento
    #   Option: any text
    "entry.1599573058": "",
    # Número (required)
    #   Option: any text
    "entry.182259312": "",
    # Cidade (required)
    #   Option: any text
    "entry.1828596069": "",
    # CPF / CNPJ (required)
    #   Option: any text
    "entry.1603772010": "",
    # Nome do Cliente (required)
    #   Option: any text
    "entry.948186743": "",
    # Telefone (required)
    #   Option: any text
    "entry.1098815865": "",
    # E-mail (required)
    #   Option: any text
    "entry.1858565817": "",
    # Plano Contratado (required)
    #   Options: ['100 MB', '200 MB', '400 MB', '500 MB', '600 MB', '700 MB', '1 Gb']
    "entry.1924736303": "",
    # Adicionais (required)
    #   Options: ['HBO', 'Paramount', 'Mesh', 'Seguro Residencial', 'Rastr. Veicular', 'Monit. Residencial']
    "entry.1274466521": "",
    # Data de instalação
    #   Option: any text
    "entry.1652985137": "",
    # Período da Instalação (required)
    #   Options: ['Manhã', 'Tarde']
    "entry.1409046645": "",
    # Observação
    #   Option: any text
    "entry.527229650": "",
    # Entrada (required)
    #   Options: ['Receptivo', 'Ativo', 'Whatsapp']
    "entry.1927730902": "",
    # Categoria (required)
    #   Options: ['Ligga', 'Nova', 'Rede Neutra']
    "entry.968955457": "",
    # Matrícula (required)
    #   Options: ['29922', '33776', '32817', '20417', '28219', '33777', '34066', '34204', '34335']
    "entry.131314365": "",
    # Page History
    #   Options: from 0 to (number of page - 1)
    "pageHistory": "0,1,2,3,4"
}
                        
        return value
            
    def Submit(data):
        try:
            requests.post('https://docs.google.com/forms/d/e/1FAIpQLSdJFAe1oJfRzzg49p1BP1YwXe6pb9OlCbhRVSE3iJCIOEXWng/formResponse', data = data)
            print("Submitted successfully!")
        except:
            print("Error!")

