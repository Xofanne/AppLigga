import customtkinter as ctk
import locale
from os import mkdir
from datetime import datetime
from pathlib import Path
from brazilcep import get_address_from_cep, exceptions
import MontaForm as mf
import webbrowser as wb
from time import sleep
from random import choice
import json
from playsound import playsound

class Dados():
    def __init__(self, master) -> None:
        
        self.Operador = DadosOperador()
        self.Opcionais = DadosOpcionais()
        self.Cliente = DadosCliente()
        self.CPF = DadosCPF()
        self.CNPJ = DadosCNPJ()

class DadosOperador():
    def __init__(self) -> None:
        super().__init__()

        self.Matricula = ctk.StringVar(name="Matricula")
        self.Entrada = ctk.StringVar(name="Entrada")

class DadosOpcionais():
    def __init__(self) -> None:
        super().__init__()

        self.IDL = ctk.StringVar(name="IDL")
        self.OBS = ctk.StringVar(name="OBS")

class DadosCliente():
    def __init__(self) -> None:
        super().__init__()

        self.ISCPF = True

        self.CEP = ctk.StringVar(name="CEP")
        self.Rua = ctk.StringVar(name="Rua")
        self.Numero = ctk.StringVar(name="Número")
        self.Complemento = ctk.StringVar(name="Complemento")
        self.Cidade = ctk.StringVar(name="Cidade")

        self.Nome = ctk.StringVar(name="Nome")
        self.Telefone = ctk.StringVar(name="Telefone")
        self.Email = ctk.StringVar(name="Email")

        self.Empresa = ctk.StringVar(name="Empresa")
        self.Velocidade = ctk.StringVar(name="Velocidade")
        self.Pagamento = ctk.StringVar(name="Pagamento")
        self.Vencimento = ctk.StringVar(name="Vencimento")
        self.Adicionais : list = []

        self.DiaInstalacao = ctk.StringVar(name="Dia de Instalação")
        self.MesInstalacao = ctk.StringVar(name="Mes de Instalacao")
        self.AnoInstalacao = ctk.StringVar(name="Ano de Instalacao")
        self.DataInstalacao = ctk.StringVar(name="Data de Instalacao")
        self.Periodo = ctk.StringVar(name="Periodo")

class DadosCPF():
    def __init__(self) -> None:
        
        super().__init__()

        self.CPF = ctk.StringVar(name="CPF")
        self.DataDeNascimento = ctk.StringVar(name="Data de Nascimento")
        self.NomeDaMae = ctk.StringVar(name="Nome da Mãe")

class DadosCNPJ():
    def __init__(self) -> None:
        super().__init__()

        self.CNPJ = ctk.StringVar(name="CNPJ")

        self.NomeFantasia = ctk.StringVar(name="Nome Fantasia")
        self.RazaoSocial = ctk.StringVar(name="Razão Social")
        self.FinanceiroNome = ctk.StringVar(name="Nome Financeiro")
        self.FinanceiroTelefone = ctk.StringVar(name="Telefone Financeiro")
        self.FinanceiroEmail = ctk.StringVar(name="Email Financeiro")

class TabViewDados(ctk.CTkTabview):
    def __init__(self, mainapp, Dados):
        super().__init__(mainapp)
        self.configure(command=lambda: self.valida(Dados))

        self.TabCPF = "CPF"
        self.TabCNPJ = "CNPJ"

        self.add(self.TabCPF)
        self.add(self.TabCNPJ)
        self.set(self.TabCPF)

        self.tab(self.TabCPF).grid_columnconfigure((0), weight=1)
        self.tab(self.TabCPF).grid_columnconfigure((1), weight=1)
        self.tab(self.TabCPF).grid_columnconfigure((3), weight=1)
        self.tab(self.TabCPF).grid_columnconfigure((4), weight=8)

        self.tab(self.TabCNPJ).grid_columnconfigure((0), weight=1)
        self.tab(self.TabCNPJ).grid_columnconfigure((1), weight=4)
        self.tab(self.TabCNPJ).grid_columnconfigure((3), weight=1)
        self.tab(self.TabCNPJ).grid_columnconfigure((4), weight=1)
        self.tab(self.TabCNPJ).grid_columnconfigure((5), weight=1)
        self.tab(self.TabCNPJ).grid_columnconfigure((6), weight=10)

        ### TAB CPF ###

        ### Linha 1 / CPF e Nome
        self.label_CPF_CPF = ctk.CTkLabel(self.tab(self.TabCPF), text="CPF")
        self.label_CPF_CPF.grid(row=0, column=0, sticky='e', pady=(20, 1), padx=2)

        self.entry_CPF_CPF = ctk.CTkEntry(self.tab(self.TabCPF), textvariable=Dados.CPF.CPF, justify="center", corner_radius=10, height=28, width=100)
        self.entry_CPF_CPF.grid(row=0, column=1, sticky='ew', pady=(20, 1), padx=2)

        self.label_CPF_Nome = ctk.CTkLabel(self.tab(self.TabCPF), text="Nome")
        self.label_CPF_Nome.grid(row=0, column=3, sticky='e', pady=(20, 1), padx=2)

        self.entry_CPF_Nome = ctk.CTkEntry(self.tab(self.TabCPF), textvariable=Dados.Cliente.Nome, justify="center", corner_radius=10, height=28)
        self.entry_CPF_Nome.grid(row=0, column=4, sticky='ew', pady=(20, 1), padx=2)
        ### -------- ###

        ### Linha 2 / Nascimento e nome da mãe
        self.label_CPF_Nasc = ctk.CTkLabel(self.tab(self.TabCPF), text="Data de\nnasc", anchor="e")
        self.label_CPF_Nasc.grid(row=1, column=0, sticky='e', pady=1, padx=2)

        self.entry_CPF_Nasc = ctk.CTkEntry(self.tab(self.TabCPF), textvariable=Dados.CPF.DataDeNascimento, justify="center", corner_radius=10, height=28, width=100)
        self.entry_CPF_Nasc.grid(row=1, column=1, sticky='ew', pady=1, padx=2)

        self.label_CPF_Mae = ctk.CTkLabel(self.tab(self.TabCPF), text="Nome da\nmãe", anchor='e')
        self.label_CPF_Mae.grid(row=1, column=3, sticky='e', pady=1, padx=2)

        self.entry_CPF_Mae = ctk.CTkEntry(self.tab(self.TabCPF), textvariable=Dados.CPF.NomeDaMae, justify="center", corner_radius=10, height=28)
        self.entry_CPF_Mae.grid(row=1, column=4, sticky='ew', pady=1, padx=2)
        ### -------- ###

        ### Linha 3 / Telefone e email
        self.label_CPF_Telefone = ctk.CTkLabel(self.tab(self.TabCPF), text="Tel")
        self.label_CPF_Telefone.grid(row=2, column=0, sticky='e', pady=1, padx=2)

        self.entry_CPF_Telefone = ctk.CTkEntry(self.tab(self.TabCPF), textvariable=Dados.Cliente.Telefone, justify="center", corner_radius=10, height=28, width=100)
        self.entry_CPF_Telefone.grid(row=2, column=1, sticky='ew', pady=1, padx=2)

        self.label_CPF_Email = ctk.CTkLabel(self.tab(self.TabCPF), text="Email")
        self.label_CPF_Email.grid(row=2, column=3, sticky='e', pady=1, padx=2)

        self.entry_CPF_Email = ctk.CTkEntry(self.tab(self.TabCPF), textvariable=Dados.Cliente.Email, justify="center", corner_radius=10, height=28)
        self.entry_CPF_Email.grid(row=2, column=4, sticky='ew', pady=1, padx=2)
        ### -------- ###

        ### FIM TAB CPF ###

        ### TAB CNPJ ###

        ### Linha 1 / CNPJ e Nome fantasia
        self.label_CNPJ_CNPJ = ctk.CTkLabel(self.tab(self.TabCNPJ), text=self.TabCNPJ)
        self.label_CNPJ_CNPJ.grid(row=0, column=0, sticky='e', pady=1, padx=2)

        self.entry_CNPJ_CNPJ = ctk.CTkEntry(self.tab(self.TabCNPJ), textvariable=Dados.CNPJ.CNPJ, justify="center", corner_radius=10, height=28, width=100)
        self.entry_CNPJ_CNPJ.grid(row=0, column=1, columnspan=3, sticky='ew', pady=1, padx=2)

        self.label_CNPJ_NomeFantasia = ctk.CTkLabel(self.tab(self.TabCNPJ), text="Nome\nfantasia", anchor="e")
        self.label_CNPJ_NomeFantasia.grid(row=0, column=4, sticky='e', pady=1, padx=2)

        self.entry_CNPJ_NomeFantasia = ctk.CTkEntry(self.tab(self.TabCNPJ), textvariable=Dados.CNPJ.NomeFantasia, justify="center", corner_radius=10, height=28)
        self.entry_CNPJ_NomeFantasia.grid(row=0, column=5, sticky='ew', pady=1, padx=2, columnspan=2)
        ### -------- ###

        ### Linha 2 / Razão social
        self.label_CNPJ_RazaoSocial = ctk.CTkLabel(self.tab(self.TabCNPJ), text="Razão\nsocial", anchor='e')
        self.label_CNPJ_RazaoSocial.grid(row=1, column=0, sticky='e', pady=(1, 9), padx=2)

        self.entry_CNPJ_RazaoSocial = ctk.CTkEntry(self.tab(self.TabCNPJ), textvariable=Dados.CNPJ.RazaoSocial, justify="center", corner_radius=10, height=28, width=100)
        self.entry_CNPJ_RazaoSocial.grid(row=1, column=1, sticky='ew', pady=(1, 9), padx=2, columnspan=6)
        ### -------- ###

        ### Linha 3 / Contato principal
        # self.label_CNPJ_Contato = ctk.CTkLabel(self.tab(self.TabCNPJ), text='Contato')
        # self.label_CNPJ_Contato.grid(row=2, column=0, sticky='sw', pady=1, padx=4, columnspan=2)

        self.label_CNPJ_Nome = ctk.CTkLabel(self.tab(self.TabCNPJ), text="Nome")
        self.label_CNPJ_Nome.grid(row=2, column=0, sticky='e', pady=1, padx=2)

        self.entry_CNPJ_Nome = ctk.CTkEntry(self.tab(self.TabCNPJ), textvariable=Dados.Cliente.Nome, justify="center", corner_radius=10, height=28, width=100)
        self.entry_CNPJ_Nome.grid(row=2, column=1, sticky='ew', pady=1, padx=2)

        self.label_CNPJ_Telefone = ctk.CTkLabel(self.tab(self.TabCNPJ), text="Tel")
        self.label_CNPJ_Telefone.grid(row=2, column=3, sticky='e', pady=1, padx=2)

        self.entry_CNPJ_Telefone = ctk.CTkEntry(self.tab(self.TabCNPJ), textvariable=Dados.Cliente.Telefone, justify="center", corner_radius=10, height=28, width=100)
        self.entry_CNPJ_Telefone.grid(row=2, column=4, sticky='ew', pady=1, padx=2)

        self.label_CNPJ_Email = ctk.CTkLabel(self.tab(self.TabCNPJ), text="Email")
        self.label_CNPJ_Email.grid(row=2, column=5, sticky='e', pady=1, padx=2)

        self.entry_CNPJ_Email = ctk.CTkEntry(self.tab(self.TabCNPJ), textvariable=Dados.Cliente.Email, justify="center", corner_radius=10, height=28)
        self.entry_CNPJ_Email.grid(row=2, column=6, sticky='ew', pady=1, padx=2)
        ### -------- ###

        ### Linha 3 / Contato financeiro
        self.label_CNPJ_Financeiro = ctk.CTkLabel(self.tab(self.TabCNPJ), text='Contato financeiro')
        self.label_CNPJ_Financeiro.grid(row=4, column=0, sticky='sw', pady=1, padx=4, columnspan=2)

        self.button_CNPJ_Copia = ctk.CTkButton(self.tab(self.TabCNPJ), text='Copiar dados do contato', command=lambda: self.CopiaDados(Dados))
        self.button_CNPJ_Copia.grid(row=4, column=6, sticky='ew', pady=1, padx=4)

        self.label_CNPJ_Nome_Financeiro = ctk.CTkLabel(self.tab(self.TabCNPJ), text="Nome")
        self.label_CNPJ_Nome_Financeiro.grid(row=5, column=0, sticky='e', pady=1, padx=2)

        self.entry_CNPJ_Nome_Financeiro = ctk.CTkEntry(self.tab(self.TabCNPJ), textvariable=Dados.CNPJ.FinanceiroNome, justify="center", corner_radius=10, height=28, width=100)
        self.entry_CNPJ_Nome_Financeiro.grid(row=5, column=1, sticky='ew', pady=1, padx=2)

        self.label_CNPJ_Telefone_Financeiro = ctk.CTkLabel(self.tab(self.TabCNPJ), text="Tel")
        self.label_CNPJ_Telefone_Financeiro.grid(row=5, column=3, sticky='e', pady=1, padx=2)

        self.entry_CNPJ_Telefone_Financeiro = ctk.CTkEntry(self.tab(self.TabCNPJ),textvariable=Dados.CNPJ.FinanceiroTelefone, justify="center", corner_radius=10, height=28, width=100)
        self.entry_CNPJ_Telefone_Financeiro.grid(row=5, column=4, sticky='ew', pady=1, padx=2)

        self.label_CNPJ_Email_Financeiro = ctk.CTkLabel(self.tab(self.TabCNPJ), text="Email")
        self.label_CNPJ_Email_Financeiro.grid(row=5, column=5, sticky='e', pady=1, padx=2)

        self.entry_CNPJ_Email_Financeiro = ctk.CTkEntry(self.tab(self.TabCNPJ), textvariable=Dados.CNPJ.FinanceiroEmail, justify="center", corner_radius=10, height=28)
        self.entry_CNPJ_Email_Financeiro.grid(row=5, column=6, sticky='ew', pady=1, padx=2)
        ### -------- ###
        
        self.valida(Dados)
        
    def valida(self, Dados):
        Dados.CPF.CPF.set("")
        Dados.CPF.DataDeNascimento.set("")
        Dados.CPF.NomeDaMae.set("")
        Dados.CNPJ.CNPJ.set("")
        Dados.CNPJ.RazaoSocial.set("")
        Dados.CNPJ.NomeFantasia.set("")
        Dados.CNPJ.FinanceiroNome.set("")
        Dados.CNPJ.FinanceiroTelefone.set("")
        Dados.CNPJ.FinanceiroEmail.set("")

    def CopiaDados(self, Dados):
        Dados.CNPJ.FinanceiroNome.set(Dados.Cliente.Nome.get())
        Dados.CNPJ.FinanceiroTelefone.set(Dados.Cliente.Telefone.get())
        Dados.CNPJ.FinanceiroEmail.set(Dados.Cliente.Email.get())


class FrameCEP(ctk.CTkFrame):
    def __init__(self, master, Dados):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=5)

        self.label_CEP = ctk.CTkLabel(self, text='CEP')
        self.label_CEP.grid(row=0, column=0, sticky='e', padx=(20, 2), pady=(5, 1))

        self.entry_CEP = ctk.CTkEntry(self, textvariable=Dados.Cliente.CEP, justify="center", corner_radius=10, height=28, width=100)
        self.entry_CEP.grid(row=0, column=1, padx=(5, 200), pady=(5, 1), sticky='ew')

        self.label_Rua = ctk.CTkLabel(self, text='Rua')
        self.label_Rua.grid(row=1, column=0, sticky='e', padx=(20, 2), pady=1)

        self.entry_Rua = ctk.CTkEntry(self, textvariable=Dados.Cliente.Rua, justify="center", corner_radius=10, height=28, width=100)
        self.entry_Rua.grid(row=1, column=1, padx=5, pady=1, sticky='ew')

        self.label_Numero = ctk.CTkLabel(self, text='Número')
        self.label_Numero.grid(row=2, column=0, sticky='e', padx=(20, 2), pady=1)

        self.entry_Numero = ctk.CTkEntry(self, textvariable=Dados.Cliente.Numero, justify="center", corner_radius=10, height=28, width=100)
        self.entry_Numero.grid(row=2, column=1, padx=(5, 100), pady=1, sticky='ew')

        self.label_Complemento = ctk.CTkLabel(self, text='Comp')
        self.label_Complemento.grid(row=3, column=0, sticky='e', padx=(20, 2), pady=1)

        self.entry_Complemento = ctk.CTkEntry(self, textvariable=Dados.Cliente.Complemento, justify="center", corner_radius=10, height=28, width=100)
        self.entry_Complemento.grid(row=3, column=1, padx=(5, 100), pady=1, sticky='ew')

        self.label_Cidade = ctk.CTkLabel(self, text='Cidade')
        self.label_Cidade.grid(row=4, column=0, sticky='e', padx=(20, 2), pady=1)

        self.entry_Cidade = ctk.CTkEntry(self, textvariable=Dados.Cliente.Cidade, justify="center", corner_radius=10, height=28, width=100)
        self.entry_Cidade.grid(row=4, column=1, padx=(5, 100), pady=1, sticky='ew')

        self.button_Busca = ctk.CTkButton(self, text="Buscar CEP", command=lambda: self.PesquisarCep(Dados))
        self.button_Busca.grid(row=5, column=0, columnspan=2, sticky='new', pady=(5, 1), padx=10)

    def PesquisarCep(self, Dados):
        try:
            address = get_address_from_cep(Dados.Cliente.CEP.get())
            Dados.Cliente.Rua.set(value=f"{address['street']}")
            Dados.Cliente.Cidade.set(value=f"{address['city']} / {address['uf']}")
            # {'district': 'Bairro', 'cep': 'xxxxx-xxx', 'city': 'Cidade', 'street': 'Rua', 'uf': 'Estado', 'complement': '?'}
        except ValueError as ve:
            Dados.Cliente.Rua.set(value=f"CEP não pode estar vazio")

        # when provide CEP is invalid. Wrong size or with chars that dont be numbers.
        except exceptions.InvalidCEP as eic:
            Dados.Cliente.Rua.set(value=f"CEP inválido")

        # CEP is fine but not exist ou not found in request API's database
        except exceptions.CEPNotFound as ecnf:
            Dados.Cliente.Rua.set(value=f"CEP não encontrado")

        # many request exception
        except exceptions.BlockedByFlood as ebbf:
            Dados.Cliente.Rua.set(value=f"ERRO: Muitas tentativas seguidas")

        # general exceptions
        except exceptions.BrazilCEPException as e:
            print(e)

class TabViewAdicionais(ctk.CTkTabview):
    def __init__(self, master, Dados):
        super().__init__(master)

        self.grid_columnconfigure((0, 1), weight=1)

        self.TabLigga_C = "Venda - Ligga"
        self.TabNova_C = "Venda - Nova"
        self.TabRN_C = "Rede Neutra"

        self.TabLigga = "L"
        self.TabNova = "N"
        self.TabRN = "RN"

        self.configure(state='disabled', segmented_button_unselected_color = '#636363', text_color_disabled	= '#bfbbba', segmented_button_selected_color = '#543729', anchor='w')

        self.add(self.TabLigga)
        self.add(self.TabNova)
        self.add(self.TabRN)

        ### TAB LIGGA ###
        self.checkbox_Ligga_HBO = ctk.CTkCheckBox(self.tab(self.TabLigga), text="HBO", onvalue="1", offvalue="0", command=lambda: self.AdicionaRemove(Dados, self.checkbox_Ligga_HBO))
        self.checkbox_Ligga_HBO.grid(row=0, column=0, columnspan=2, pady=1, padx=5, sticky='w')

        self.checkbox_Ligga_Paramount = ctk.CTkCheckBox(self.tab(self.TabLigga), text="Paramout", onvalue="1", offvalue="0", command=lambda: self.AdicionaRemove(Dados, self.checkbox_Ligga_Paramount))
        self.checkbox_Ligga_Paramount.grid(row=1, column=0, columnspan=2, pady=1, padx=5, sticky='w')

        self.checkbox_Ligga_Mesh = ctk.CTkCheckBox(self.tab(self.TabLigga), text="Mesh", onvalue="1", offvalue="0", command=lambda: self.AdicionaRemove(Dados, self.checkbox_Ligga_Mesh))
        self.checkbox_Ligga_Mesh.grid(row=2, column=0, columnspan=2, pady=1, padx=5, sticky='w')

        self.checkbox_Ligga_Seguro = ctk.CTkCheckBox(self.tab(self.TabLigga), text="Seguro Residencial", onvalue="1", offvalue="0", command=lambda: self.AdicionaRemove(Dados, self.checkbox_Ligga_Seguro))
        self.checkbox_Ligga_Seguro.grid(row=3, column=0, columnspan=2, pady=1, padx=5, sticky='w')
        ### FIM TAB LIGGA ###

        ### TAB NOVA ###
        self.checkbox_Nova_Seguro = ctk.CTkCheckBox(self.tab(self.TabNova), text="Seguro Residencial", onvalue="1", offvalue="0", command=lambda: self.AdicionaRemove(Dados, self.checkbox_Nova_Seguro))
        self.checkbox_Nova_Seguro.grid(row=0, column=0, columnspan=2, pady=1, padx=5, sticky='w')

        self.checkbox_Nova_Rastreamento = ctk.CTkCheckBox(self.tab(self.TabNova), text="Rastreamento de veiculo", onvalue="1", offvalue="0", command=lambda: self.AdicionaRemove(Dados, self.checkbox_Nova_Rastreamento))
        self.checkbox_Nova_Rastreamento.grid(row=1, column=0, columnspan=2, pady=1, padx=5, sticky='w')

        self.checkbox_Nova_Monitoramento = ctk.CTkCheckBox(self.tab(self.TabNova), text="Monitoramento residencial", onvalue="1", offvalue="0", command=lambda: self.AdicionaRemove(Dados, self.checkbox_Nova_Monitoramento))
        self.checkbox_Nova_Monitoramento.grid(row=2, column=0, columnspan=2, pady=1, padx=5, sticky='w')
        ### FIM TAB NOVA ###

        ### TAB RN ###
        self.checkbox_RN_HBO = ctk.CTkCheckBox(self.tab(self.TabRN), text="HBO", onvalue="1", offvalue="0", command=lambda: self.AdicionaRemove(Dados, self.checkbox_RN_HBO))
        self.checkbox_RN_HBO.grid(row=0, column=0, columnspan=2, pady=1, padx=5, sticky='w')
        
        self.checkbox_RN_Paramount = ctk.CTkCheckBox(self.tab(self.TabRN), text="Paramout", onvalue="1", offvalue="0", command=lambda: self.AdicionaRemove(Dados, self.checkbox_RN_Paramount))
        self.checkbox_RN_Paramount.grid(row=1, column=0, columnspan=2, pady=1, padx=5, sticky='w')
        
        self.checkbox_RN_Seguro = ctk.CTkCheckBox(self.tab(self.TabRN), text="Seguro Residencial", onvalue="1", offvalue="0", command=lambda: self.AdicionaRemove(Dados, self.checkbox_RN_Seguro))
        self.checkbox_RN_Seguro.grid(row=2, column=0, columnspan=2, pady=1, padx=5, sticky='w')

    def AdicionaRemove(self, Dados, Adicional):
        if Adicional.get() == "1":
            Dados.Cliente.Adicionais.append(Adicional.cget("text"))
            return
        Dados.Cliente.Adicionais.remove(Adicional.cget("text"))


class FrameEmpresa(ctk.CTkFrame):
    def __init__(self, master, Dados):
        super().__init__(master)

        self.grid_columnconfigure((0), weight=1)
        self.grid_columnconfigure(2, weight=10)

        self.options_empresa = ctk.CTkOptionMenu(self, values=["Venda - Ligga", "Venda - Nova", "Rede Neutra"], variable=Dados.Cliente.Empresa, command=lambda x: self.SetAdicionais(self.tabviewAdicionais, Dados), anchor='center')
        self.options_empresa.set('Empresa')
        self.options_empresa.configure(width=130)
        self.options_empresa.grid(row=0, column=0, pady=(10, 1), padx=5)

        self.options_velocidade = ctk.CTkOptionMenu(self, values=[], anchor='center', command=lambda x: Dados.Cliente.Velocidade.set(self.options_velocidade.get()))
        self.options_velocidade.set('Velocidade')
        self.options_velocidade.grid(row=1, column=0, pady=1, padx=5)

        self.options_Pagamento = ctk.CTkOptionMenu(self, values=["Boleto", "Débito"], anchor='center', command=lambda x: Dados.Cliente.Pagamento.set(self.options_Pagamento.get()))
        self.options_Pagamento.set('Pagamento')
        self.options_Pagamento.grid(row=2, column=0, pady=1, padx=5)

        self.options_Vencimento = ctk.CTkOptionMenu(self, values=['1', '5', '10', '15', '20', '25'], anchor='center', command=lambda x: Dados.Cliente.Vencimento.set(self.options_Vencimento.get()))
        self.options_Vencimento.set('Vencimento')
        self.options_Vencimento.grid(row=3, column=0, pady=1, padx=5)

        self.tabviewAdicionais = TabViewAdicionais(self, Dados)
        self.tabviewAdicionais.configure(height=160, width=230)
        self.tabviewAdicionais.grid(row=0, rowspan=6, column=2, pady=1, padx=(5, 0), sticky='ew')

    def SetAdicionais(self, adicionaisTab, Dados):
        self.ClearAdicionais(adicionaisTab, Dados)

        if self.options_empresa.get() == self.tabviewAdicionais.TabLigga_C:
            Dados.Cliente.Empresa.set(self.options_empresa.get())
            self.options_velocidade.configure(values=['100 MB', '200 MB', '400 MB', '500 MB', '600 MB', '700 MB'])
            self.options_velocidade.set('Velocidade')
            adicionaisTab.set(adicionaisTab.TabLigga)
        elif self.options_empresa.get() == self.tabviewAdicionais.TabNova_C:
            Dados.Cliente.Empresa.set(self.options_empresa.get())
            self.options_velocidade.configure(values=['100 MB', '200 MB', '400 MB', '600 MB', '700 MB'])
            self.options_velocidade.set('Velocidade')
            adicionaisTab.set(adicionaisTab.TabNova)
        elif self.options_empresa.get() == self.tabviewAdicionais.TabRN_C:
            Dados.Cliente.Empresa.set(self.options_empresa.get())  
            self.options_velocidade.configure(values=['200 MB', '400 MB', '600 MB', '700 MB', '1 GB'])
            self.options_velocidade.set('Velocidade')  
            adicionaisTab.set(adicionaisTab.TabRN)

    def ClearAdicionais(self, adicionaisTab, Dados):
        adicionaisTab.checkbox_Ligga_HBO.deselect()
        adicionaisTab.checkbox_Ligga_Paramount.deselect()
        adicionaisTab.checkbox_Ligga_Seguro.deselect()
        adicionaisTab.checkbox_Ligga_Mesh.deselect()
        adicionaisTab.checkbox_Nova_Seguro.deselect()
        adicionaisTab.checkbox_Nova_Rastreamento.deselect()
        adicionaisTab.checkbox_Nova_Monitoramento.deselect()
        adicionaisTab.checkbox_RN_HBO.deselect()
        adicionaisTab.checkbox_RN_Paramount.deselect()
        adicionaisTab.checkbox_RN_Seguro.deselect()
        Dados.Cliente.Adicionais.clear()


class FrameData(ctk.CTkFrame):
    def __init__(self, master, Dados):
        super().__init__(master)

        self.meses28 = ['02']
        self.meses30 = ['04', '06', '09', '11']
        self.QTDEDIAS = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
        self.QTDEDIAS31 = [str(x) for x in range(10, 32)]
        self.QTDEDIAS30 = [str(x) for x in range(10, 31)]
        self.QTDEDIAS28 = [str(x) for x in range(10, 29)]
        self.QTDEMES = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        self.ANO = [str(x) for x in range(2024, 2026)]

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0,1,2,3), weight=1)

        self.label_instalacao = ctk.CTkLabel(self, text="Data de instalação", font=('helvetica', 14, 'bold'))
        self.label_instalacao.grid(row=0, column=0, columnspan=3, pady=2, padx=1, sticky='new')

        self.option_Mes = ctk.CTkOptionMenu(self, variable=Dados.Cliente.MesInstalacao, values=self.QTDEMES, anchor="center", command=lambda x: self.SetDias(self.option_Mes.get()))
        self.option_Mes.set('Mes')
        self.option_Mes.configure(width=70)
        self.option_Mes.grid(row=1, column=0, pady=(0, 5), padx= 2, sticky="se")

        self.option_Dia = ctk.CTkOptionMenu(self, variable=Dados.Cliente.DiaInstalacao, values=[], anchor="center")
        self.option_Dia.set('Dia')
        self.option_Dia.configure(width=70)
        self.option_Dia.grid(row=1, column=1, pady=(0, 5), padx= 2, sticky="sw")

        self.option_Ano = ctk.CTkOptionMenu(self, variable=Dados.Cliente.AnoInstalacao, values=self.ANO, anchor="center")
        self.option_Ano.set('2024')
        self.option_Ano.configure(width=70)
        self.option_Ano.grid(row=2, column=0, columnspan=2, pady=(0, 5), padx= 2, sticky="n")

        self.option_Periodo = ctk.CTkOptionMenu(self, variable=Dados.Cliente.Periodo, values=["Manhã", "Tarde"], anchor="center")
        self.option_Periodo.set('Período')
        self.option_Periodo.configure(width=140)
        self.option_Periodo.grid(row=3, column=0, columnspan=2, pady=(1, 10), sticky='n')


    def SetDias(self, x):
        if x in self.meses28:
            self.QTDEDIAS = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
            self.QTDEDIAS.extend(self.QTDEDIAS28)
            self.option_Dia.configure(values=self.QTDEDIAS)
            return
        elif x in self.meses30:
            self.QTDEDIAS = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
            self.QTDEDIAS.extend(self.QTDEDIAS30)
            self.option_Dia.configure(values=self.QTDEDIAS)
            return
        else:
            self.QTDEDIAS = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
            self.QTDEDIAS.extend(self.QTDEDIAS31)
            self.option_Dia.configure(values=self.QTDEDIAS)

class FrameConfirm(ctk.CTkFrame):
    def __init__(self, master, Dados, Empresa):
        super().__init__(master)

        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_rowconfigure(2, weight=2)

        self.MATRICULAS = ['29922', '33776', '32817', '20417', '32811', '28219', '33777', '33945', '34066', '34204', '20593', '34335']
        self.ENTRADA = ["Receptivo", 'Ativo', "Whatsapp"]

        self.label_IDL = ctk.CTkLabel(self, text="ID da \nligação")
        self.label_IDL.grid(row=0, column=0, pady=(5, 1), padx=(5, 1), sticky='nsew')

        self.entry_IDL = ctk.CTkEntry(self, textvariable=Dados.Opcionais.IDL, justify="center", corner_radius=10, height=28, width=200)
        self.entry_IDL.grid(row=0, column=1, columnspan=2, pady=(5, 1), padx=5, sticky='ew')

        self.label_Obs = ctk.CTkLabel(self, text="Obs")
        self.label_Obs.grid(row=1, column=0, pady=1, padx=1)

        self.entry_Obs = ctk.CTkEntry(self, textvariable=Dados.Opcionais.OBS, justify="center", corner_radius=10, width=200, height=28)
        self.entry_Obs.grid(row=1, column=1, columnspan=2, pady=1, padx=2, sticky='ew')

        self.button_config = ctk.CTkButton(self, text=f"Matrícula: {Dados.Operador.Matricula.get()}\nEntrada: {Dados.Operador.Entrada.get()}", fg_color="transparent", command=lambda: self.Configuracoes(master, Dados), height=40)
        self.button_config.grid(row=0, column=3, pady=(5, 1), padx=(1, 5), sticky='ew')

        self.button_TXT = ctk.CTkButton(self, text="Arquivo de\ntexto de hoje", fg_color="transparent", command=lambda: self.AbrirTxt(master))
        self.button_TXT.grid(row=1, column=3, pady=1, padx=(1, 5), sticky='new')

        self.button_TXT = ctk.CTkButton(self, text="Pasta de\narquivos txt", fg_color="transparent", command=lambda: self.AbrirPasta(master))
        self.button_TXT.grid(row=2, column=3, pady=(1, 5), padx=(1, 5), sticky='snew')

        self.button_Pausa = ctk.CTkButton(self, text="Pausa", fg_color="transparent", command=lambda: self. CriaTimer(master))
        self.button_Pausa.grid(row=2, column=2, pady=(1, 5), padx=5, sticky="nsew")

        self.button_enviar = ctk.CTkButton(self, text="Enviar", font=('helvetica', 20, 'bold'), command=lambda: master.Enviar(Empresa))
        self.button_enviar.grid(row=2, column=0, columnspan=2, pady=(1,5), padx=5, sticky='snew')

    def CriaTimer(self, master):
        timer = Timer(master)

    def AbrirTxt(self, master):
        wb.open(master.txtFile)

        ### abre a pasta onde ta o arquivo
    def AbrirPasta(self, master):
        try:
            '''Abre a pasta onde está o arquivo'''
            current_directory = Path(__file__).parent.parent.resolve()
            wb.open(str(current_directory)+"\TXTs") 
        except:
            current_directory = Path(__file__).parent.resolve()
            wb.open(current_directory)


    def Configuracoes(self, master, Dados):

        def Confirma():
            self.button_config.configure(text=f"Matrícula: {Dados.Operador.Matricula.get()}\nEntrada: {Dados.Operador.Entrada.get()}")
            try:
                with open('dadosOperador.json', 'r+', encoding="utf8") as file:
                    dados = json.load(file)
                    dados['Matricula'] = Dados.Operador.Matricula.get()
                    dados['Entrada'] = Dados.Operador.Entrada.get()
                    file.seek(0)
                    json.dump(dados, file)
                    file.truncate()
            except:
                with open('_internal/dadosOperador.json', 'r+', encoding="utf8") as file:
                    dados = json.load(file)
                    dados['Matricula'] = Dados.Operador.Matricula.get()
                    dados['Entrada'] = Dados.Operador.Entrada.get()
                    file.seek(0)
                    json.dump(dados, file)
                    file.truncate()
            self.toplevel_configs.destroy()

        self.toplevel_configs = ctk.CTkToplevel()
        self.toplevel_configs.title("Dados do Operador")
        self.toplevel_configs.geometry(f"+{master.winfo_x()+530}+{master.winfo_y()+200}")
        self.toplevel_configs.grab_set()

        self.label_Matricula = ctk.CTkLabel(self.toplevel_configs, text="Matrícula")
        self.label_Matricula.grid(row=0, column=0, pady=(10, 3), padx=(50, 8))
        
        self.option_matriculas = ctk.CTkOptionMenu(self.toplevel_configs, variable=Dados.Operador.Matricula, values=self.MATRICULAS, anchor="center")
        self.option_matriculas.grid(row=0, column=1, pady=(10, 3), padx=(8, 50))

        self.label_Entrada = ctk.CTkLabel(self.toplevel_configs, text="Entrada")
        self.label_Entrada.grid(row=1, column=0, pady=3, padx=(50, 8))
        
        self.option_Entrada = ctk.CTkOptionMenu(self.toplevel_configs, variable=Dados.Operador.Entrada, values=self.ENTRADA, anchor="center")
        self.option_Entrada.grid(row=1, column=1, pady=3, padx=(8, 50))

        self.button_confirma = ctk.CTkButton(self.toplevel_configs, text="Confirmar", command=lambda: Confirma())
        self.button_confirma.grid(row=2, column=0, columnspan=2, pady=(3, 10), padx=50)

class Timer(ctk.CTkToplevel):

    def __init__(self, master) -> None:
        super().__init__(master)

        self.title("Timer")
        self.minsize(300, 100)
        self.maxsize(300, 100)
        self.wm_attributes('-topmost', 1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)

        self.solve = ""
        self.tempo = 0

        self.attLabel(0, master)

        self.label_timer = ctk.CTkLabel(self, text="", anchor='center', font=("Roboto", 30, "bold"), fg_color="#cccccc", text_color="#000000")
        self.label_timer.grid(row=0, rowspan=4, column=1)

        self.button_5min = ctk.CTkButton(self, text="5 min", anchor="center", width=10, command=lambda: self.attLabel(300, master))
        self.button_5min.grid(row=0, column=0, sticky="ew")

        self.button_10min = ctk.CTkButton(self, text="10 min", anchor="center", width=10, command=lambda: self.attLabel(600, master))
        self.button_10min.grid(row=1, column=0, sticky="ew")

        self.button_20min = ctk.CTkButton(self, text="20 min", anchor="center", width=10, command=lambda: self.attLabel(1200, master))
        self.button_20min.grid(row=2, column=0, sticky="ew")

        self.button_start = ctk.CTkButton(self, text="Start", anchor="center", width=10, command=lambda: self.countdown(master))
        self.button_start.grid(row=3, column=0, sticky="ew")

    def attLabel(self, t, master):
        self.tempo = t
        mins, secs = divmod(self.tempo, 60)
        timerstr = '{:02d} : {:02d}'.format(mins, secs)
        self.label_timer = ctk.CTkLabel(self, text=f"{timerstr}", anchor="center", font=("Roboto", 40, "bold"), fg_color="#cccccc", text_color="#000000")
        self.label_timer.grid(row=0, rowspan=4, column=1, sticky='nsew')
        if self.solve != "":
            master.after_cancel(self.solve)
        return t

    def countdown(self, master, *x):
        if self.tempo > 0:
            if self.tempo == 61:
                try:
                    playsound("_internal/notf.wav", False)
                except: 
                    playsound("notf.wav", False)
            mins, secs = divmod(self.tempo, 60)
            timerstr = '{:02d} : {:02d}'.format(mins, secs)
            self.label_timer.configure(text=f"{timerstr}")
            if self.tempo >=120:
                self.solve = master.after(1000, lambda: self.countdown(self, master))
                self.tempo -= 1
            elif self.tempo < 120 and self.tempo > 60:
                self.solve = master.after(1000, lambda: self.countdown(self, master))
                self.label_timer.configure(fg_color="#5cd69d")
                self.tempo -= 1
            elif self.tempo <= 60 and self.tempo > 0:
                self.solve = master.after(1000, lambda: self.countdown(self, master))
                self.label_timer.configure(fg_color="#db1102")
                self.tempo -= 1



class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.deactivate_automatic_dpi_awareness()
        ctk.set_widget_scaling(0.9)
        ctk.set_appearance_mode('dark')
        try:
            ctk.set_default_color_theme("_internal/dark-blue.json")
        except:
            ctk.set_default_color_theme("dark-blue.json")

        locale.setlocale(locale.LC_NUMERIC, "C")
        
        self.caminhoArquivo = Path(__file__).parent.parent.resolve()

        try:
            with open('names.json', 'r', encoding="utf8") as names:
                names_dados = json.load(names)
                self.title(choice(names_dados.get('names')))
        except:
            with open('_internal/names.json', 'r', encoding="utf8") as names:
                names_dados = json.load(names)
                self.title(choice(names_dados.get('names')))

        print('''\n\n//        :::        ::::::::::: ::::::::   ::::::::      :::                       
//       :+:            :+:    :+:    :+: :+:    :+:   :+: :+:                      
//      +:+            +:+    +:+        +:+         +:+   +:+                      
//     +#+            +#+    :#:        :#:        +#++:++#++:                      
//    +#+            +#+    +#+   +#+# +#+   +#+# +#+     +#+                       
//   #+#            #+#    #+#    #+# #+#    #+# #+#     #+#                        
//  ########## ########### ########   ########  ###     ###''')            
        print('''//    ::::::::::: :::::::::: :::        :::::::::: ::::::::   ::::::::    :::   ::: 
//       :+:     :+:        :+:        :+:       :+:    :+: :+:    :+:  :+:+: :+:+: 
//      +:+     +:+        +:+        +:+       +:+        +:+    +:+ +:+ +:+:+ +:+ 
//     +#+     +#++:++#   +#+        +#++:++#  +#+        +#+    +:+ +#+  +:+  +#+  
//    +#+     +#+        +#+        +#+       +#+        +#+    +#+ +#+       +#+   
//   #+#     #+#        #+#        #+#       #+#    #+# #+#    #+# #+#       #+#    
//  ###     ########## ########## ########## ########   ########  ###       ###\n\n''')
        sleep(0.5)

        try:
            mkdir(f"{self.caminhoArquivo}\\TXTs")
            print(f"Pasta de textos criada em -> {self.caminhoArquivo}")
        except:
            print(f"Pasta de textos já existe em -> {self.caminhoArquivo}")

        month = datetime.today().strftime('%B-%Y')

        try:
            mkdir(f"{self.caminhoArquivo}\\TXTs\\{month}")
            print(f"Pasta de textos do Mês criado em -> {self.caminhoArquivo}\\TXTs")
        except:
            print(f"Pasta do Mês já existe em -> {self.caminhoArquivo}\\TXTs")


        try:
            self.txtFile = f"{self.caminhoArquivo}\\TXTs\\{month}\\{datetime.today().strftime('%d-%b')}.txt"
            open(self.txtFile, 'x+')
            print(f"Arquivo de texto criado em -> {self.caminhoArquivo}\\TXTs\\{month}")
        except:
            print(f"Arquivo de texto de hoje já existe em -> {self.caminhoArquivo}\\TXTs\\{month}")


        self.minsize(900, 330) ## com minsize e maxsize não precisa informar o tamanho da tela, se não vai bugar
        self.maxsize(1200, 330)
        self.grid_columnconfigure((0), weight=1)
        self.grid_columnconfigure((1), weight=1)
        self.grid_columnconfigure((2), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.CriaDados()

        self.confirmFrame = FrameConfirm(self, self.Dados, self.empresaFrame)   
        self.confirmFrame.grid(row=1, column=2, pady=(1, 0), padx=(1, 0), sticky="nsew")
    
    def CriaDados(self):

        self.Dados = Dados(self)

        try:
            with open('dadosOperador.json', 'r', encoding="utf8") as file:
                dados = json.load(file)
                self.Dados.Operador.Matricula.set(dados.get('Matricula'))
                self.Dados.Operador.Entrada.set(dados.get('Entrada'))
        except:
            with open('_internal/dadosOperador.json', 'r', encoding="utf8") as file:
                dados = json.load(file)
                self.Dados.Operador.Matricula.set(dados.get('Matricula'))
                self.Dados.Operador.Entrada.set(dados.get('Entrada'))

        self.newTab = TabViewDados(self, self.Dados)
        self.newTab.configure(width=575, height=210)
        self.newTab.grid(row=0, column=0, pady=(0, 1), padx=(0, 1), sticky='ew', columnspan=2)

        self.cepFrame = FrameCEP(self, self.Dados)
        self.cepFrame.grid(row=0, column=2, pady=(0, 1), padx=(1, 0), sticky='nsew', columnspan=2)

        self.empresaFrame = FrameEmpresa(self, self.Dados)
        self.empresaFrame.configure(width=380, height=140)
        self.empresaFrame.grid(row=1, column=0, pady=(1, 0), padx=(0, 1), sticky='nsew')

        self.dataFrame = FrameData(self, self.Dados)
        self.dataFrame.configure(width=100)
        self.dataFrame.grid(row=1, column=1, pady=(1, 0), padx=1, sticky='nsew')
    
    def TopLevelError(self, *args: str):

        self.topviewError = ctk.CTkToplevel(self)
        self.topviewError.title("Erro")
        self.topviewError.geometry(f"+{self.winfo_x()+560}+{self.winfo_y()+240}")
        self.labelerror = ctk.CTkLabel(self.topviewError, text=(f"{args[0]} em branco"), font=('helvetica', 20, 'bold'))
        self.labelerror.pack(anchor="center", expand=True, padx=40, pady=20)
        self.labelerror.grab_set()



    def validarpreenchimento(self):
        
        if self.Dados.CNPJ.CNPJ.get() == "" and self.Dados.CPF.CPF.get() == "":
            self.topviewError = ctk.CTkToplevel(self)
            self.topviewError.title("Erro")
            self.topviewError.geometry(f"+{self.winfo_x()+560}+{self.winfo_y()+240}")
            self.labelerror = ctk.CTkLabel(self.topviewError, text=(f"CPF ou CNPJ em branco"), font=('helvetica', 20, 'bold'))
            self.labelerror.pack(anchor="center", expand=True, padx=40, pady=20)
            self.labelerror.grab_set()
            return False

        
        if self.Dados.CNPJ.CNPJ.get() == "":

            required = [   
                self.Dados.Cliente.Nome,
                self.Dados.Cliente.Telefone,
                self.Dados.Cliente.Email,
                self.Dados.CPF.DataDeNascimento,
                self.Dados.CPF.NomeDaMae,
                self.Dados.Cliente.CEP,
                self.Dados.Cliente.Rua,
                self.Dados.Cliente.Numero,
                self.Dados.Cliente.Cidade,
                self.Dados.Cliente.Empresa,
                self.Dados.Cliente.Velocidade,
                self.Dados.Cliente.Pagamento,
                self.Dados.Cliente.Vencimento,
                self.Dados.Cliente.Periodo,
                self.Dados.Operador.Entrada,
                self.Dados.Operador.Matricula,
            ]
            for x in required:
                if x.get() =="":
                    self.TopLevelError(x)
                    return False
        else:
            required = [   
                    self.Dados.Cliente.Nome,
                    self.Dados.Cliente.Telefone,
                    self.Dados.Cliente.Email,
                    self.Dados.CNPJ.RazaoSocial,
                    self.Dados.CNPJ.FinanceiroNome,
                    self.Dados.CNPJ.FinanceiroTelefone,
                    self.Dados.CNPJ.FinanceiroEmail,
                    self.Dados.Cliente.CEP,
                    self.Dados.Cliente.Rua,
                    self.Dados.Cliente.Numero,
                    self.Dados.Cliente.Cidade,
                    self.Dados.Cliente.Empresa,
                    self.Dados.Cliente.Velocidade,
                    self.Dados.Cliente.Pagamento,
                    self.Dados.Cliente.Vencimento,
                    self.Dados.Cliente.Periodo,
                    self.Dados.Operador.Entrada,
                    self.Dados.Operador.Matricula,
                ]
            for x in required:
                if x.get() =="":
                    self.TopLevelError(x)
                    return False

        if self.Dados.Cliente.MesInstalacao.get() == "Mes":
            self.TopLevelError(self.Dados.Cliente.MesInstalacao)
            return False
        if self.Dados.Cliente.DiaInstalacao.get() == "Dia":
            self.TopLevelError(self.Dados.Cliente.DiaInstalacao)
            return False
        
        return True
        
    def Enviar(self, Empresa):

        if self.validarpreenchimento() == True:
            self.Dados.Cliente.DataInstalacao.set(value=f"{self.Dados.Cliente.AnoInstalacao.get()}-{self.Dados.Cliente.MesInstalacao.get()}-{self.Dados.Cliente.DiaInstalacao.get()}")

            self.InsertInTXT()

            Empresa.ClearAdicionais(self.empresaFrame.tabviewAdicionais, self.Dados)

            self.CriaDados()

    def InsertInTXT(self):

        if len(self.Dados.Cliente.Adicionais) == 0:
            self.Dados.Cliente.Adicionais.append("Nenhum")

        self.listaDeDados = [   
            self.Dados.Operador.Entrada, 
            self.Dados.CPF.CPF,
            self.Dados.CNPJ.CNPJ,
            self.Dados.CNPJ.NomeFantasia,
            self.Dados.CNPJ.RazaoSocial,
            self.Dados.Cliente.Nome,
            self.Dados.Cliente.Telefone,
            self.Dados.Cliente.Email,
            self.Dados.CPF.DataDeNascimento,
            self.Dados.CPF.NomeDaMae,
            self.Dados.CNPJ.FinanceiroNome,
            self.Dados.CNPJ.FinanceiroTelefone,
            self.Dados.CNPJ.FinanceiroEmail,
            self.Dados.Cliente.CEP,
            self.Dados.Cliente.Rua,
            self.Dados.Cliente.Numero,
            self.Dados.Cliente.Complemento,
            self.Dados.Cliente.Cidade,
            self.Dados.Cliente.Empresa,
            self.Dados.Cliente.Velocidade,
            self.Dados.Cliente.Pagamento,
            self.Dados.Cliente.Vencimento,
            self.Dados.Cliente.Adicionais,
            self.Dados.Cliente.DataInstalacao,
            self.Dados.Cliente.Periodo,
            self.Dados.Opcionais.IDL,
            self.Dados.Opcionais.OBS,
        ]

        with open(self.txtFile, 'a') as txt:
            txt.write("\n\n# # # # # # # # # # # # # # # # # # #\n # # # # # # # # # # # # # # # # # # #\n\n")
            txt.write(f"---VENDA--- {self.Dados.Cliente.Empresa.get()}\n\n")
            for x in self.listaDeDados:
                try:
                    if str(x.get()) != "":
                        txt.write(str(x))
                        txt.write(" : ")
                        txt.write(str(x.get()))
                        txt.write("\n")
                except:
                    txt.write("Adicionais : ")
                    txt.write(str(x))
                    txt.write("\n")

        mf.EnviaForm.Submit(mf.EnviaForm.FillForm(self.Dados))
        
        for x in self.listaDeDados:
            if x == self.Dados.Operador.Matricula or x == self.Dados.Operador.Entrada:
                pass
            else:
                try:
                    x.set("")
                except:
                    self.Dados.Cliente.Adicionais.clear()
        
        return

def main() -> None:

    Aplicativo = MainApp()
    Aplicativo.mainloop()

if __name__ == "__main__":
    main()
