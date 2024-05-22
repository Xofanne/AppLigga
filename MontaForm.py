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
                    # Tipo registro (required)
                    #   Options: ['Receptivo', 'Ativo', 'Whatsapp']
                    "entry.1843810681": Dados.Operador.Entrada.get(),
                    # Categoria (required)
                    #   Options: ['Venda - Ligga', 'Venda - Nova', 'Rede Neutra']
                    "entry.1619545935": Dados.Cliente.Empresa.get(),
                    # Matricula (required)
                    #   Options: ['29922', '33776', '32817', '20417', '32811', '28219', '33777', '33945', '34066', '34204', '20593', '34335']
                    "entry.42020429": Dados.Operador.Matricula.get(),
                    #####################################################
                    ################ P�gina da LIGGA ####################
                    # CPF/CNPJ (required)
                    #   Option: any text
                    "entry.792467593": doc,
                    # Nome do Cliente (required)
                    #   Option: any text
                    "entry.1241182038": nome,
                    # Telefone (required)
                    #   Option: any text
                    "entry.474099969": Dados.Cliente.Telefone.get(),
                    # E-mail (required)
                    #   Option: any text
                    "entry.1050701897": Dados.Cliente.Email.get(),
                    # CEP (required)
                    #   Option: any text
                    "entry.1313923048": Dados.Cliente.CEP.get(),
                    # Endere�o (required)
                    #   Option: any text
                    "entry.895769876": str(Dados.Cliente.Rua.get() + " - " + Dados.Cliente.Numero.get() + " - " + Dados.Cliente.Complemento.get()),
                    # Cidade 
                    #   Option: any text
                    "entry.1660866954": Dados.Cliente.Cidade.get(),
                    # Plano Contratado (required)
                    #   Options: ['100 MB', '200 MB', '400 MB', '500 MB', '600 MB', '700 MB']
                    "entry.307780867": Dados.Cliente.Velocidade.get(),
                    # Adicionais (required)
                    #   Options: ['HBO', 'Paramout', 'Mesh', 'Seguro Residencial', 'Nenhum']
                    "entry.2119590350": Dados.Cliente.Adicionais,
                    # Data da instala��o (required)
                    #   Option: any text
                    "entry.1574179663": Dados.Cliente.DataInstalacao.get(),
                    # Per�odo da instala��o (required)
                    #   Options: ['Manh�', 'Tarde']
                    "entry.776654809": Dados.Cliente.Periodo.get(),
                    # Observa��o 
                    #   Option: any text
                    "entry.174562035": Dados.Opcionais.OBS.get(),
                    ################################################
                    ############### p�gina a NOVA ##################
                    # CPF/CNPJ (required)
                    #   Option: any text
                    "entry.110641306": doc,
                    # Nome do Cliente (required)
                    #   Option: any text
                    "entry.1067003665": nome,
                    # Telefone (required)
                    #   Option: any text
                    "entry.548025792": Dados.Cliente.Telefone.get(),
                    # E-mail (required)
                    #   Option: any text
                    "entry.359757353": Dados.Cliente.Email.get(),
                    # CEP (required)
                    #   Option: any text
                    "entry.1958693030": Dados.Cliente.CEP.get(),
                    # Endere�o (required)
                    #   Option: any text
                    "entry.1678444158": str(Dados.Cliente.Rua.get() + " - " + Dados.Cliente.Numero.get() + " - " + Dados.Cliente.Complemento.get()),
                    # Cidade (required)
                    #   Option: any text
                    "entry.1401799317": Dados.Cliente.Cidade.get(),
                    # Plano Contratado (required)
                    #   Options: ['100 MB', '200 MB', '400 MB', '600 MB', '700 MB']
                    "entry.746038169": Dados.Cliente.Velocidade.get(),
                    # Adicionais (required)
                    #   Options: ['Seguro Residencial', 'Rastreamento de veiculo', 'Monitoramento residencial', 'Nenhum']
                    "entry.611471044": Dados.Cliente.Adicionais,
                    # Data da instala��o (required)
                    #   Option: any text
                    "entry.1960475321": Dados.Cliente.DataInstalacao.get(),
                    # Per�odo da instala��o (required)
                    #   Options: ['Manh�', 'Tarde']
                    "entry.1568203101": Dados.Cliente.Periodo.get(),
                    # Observa��o 
                    #   Option: any text
                    "entry.2067361142": Dados.Opcionais.OBS.get(),
                    ###############################################
                    ################ P�gina RN ####################
                    # CPF/CNPJ (required)
                    #   Option: any text
                    "entry.1054269664": doc,
                    # Nome do Cliente (required)
                    #   Option: any text
                    "entry.520011651": nome,
                    # Telefone (required)
                    #   Option: any text
                    "entry.41142562": Dados.Cliente.Telefone.get(),
                    # E-mail (required)
                    #   Option: any text
                    "entry.1766378859": Dados.Cliente.Email.get(),
                    # CEP (required)
                    #   Option: any text
                    "entry.1551965158": Dados.Cliente.CEP.get(),
                    # Endere�o (required)
                    #   Option: any text
                    "entry.657876691": str(Dados.Cliente.Rua.get() + " - " + Dados.Cliente.Numero.get() + " - " + Dados.Cliente.Complemento.get()),
                    # Cidade (required)
                    #   Option: any text
                    "entry.1251799126": Dados.Cliente.Cidade.get(),
                    # Plano Contratado (required)
                    #   Options: ['200 MB', '400 MB', '600 MB', '700 MB', '1 GB']
                    "entry.787335658": Dados.Cliente.Velocidade.get(),
                    # Adicionais (required)
                    #   Options: ['HBO', 'Paramout', 'Seguro Residencial', 'Nenhum']
                    "entry.124990098": Dados.Cliente.Adicionais,
                    # Data da instala��o 
                    #   Option: any text
                    "entry.822942176": Dados.Cliente.DataInstalacao.get(),
                    # Per�odo da instala��o (required)
                    #   Options: ['Manh�', 'Tarde']
                    "entry.1343291811": Dados.Cliente.Periodo.get(),
                    # Observa��o 
                    #   Option: any text
                    "entry.409916028": Dados.Opcionais.OBS.get(),
                    # Page History 
                    #   Options: from 0 to (number of page - 1)
                    "pageHistory": "0,1,2,3,4,5,6,7,8,9,10,11,12",
                }
                        
        return value
            
    def Submit(data):
        try:
            requests.post('https://docs.google.com/forms/d/e/1FAIpQLSf4XlvIq7su-nWvsMVWOj_LSZTDFFocuSkKE09YLKgAFuEpYw/formResponse', data = data)
            print("Submitted successfully!")
        except:
            print("Error!")