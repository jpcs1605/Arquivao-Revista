import openpyxl
from openpyxl.styles import Border, Side

def num_p_letra(nova_coluna):
    if 1 <= nova_coluna <= 26:
        return chr(64 + nova_coluna)
    else:
        raise ValueError("O número deve estar entre 1 e 26.")

def construcao_planilha(aba_TabelaBasePreco,nova_coluna_L,celula_colunaCodVendas,cv_aplicados, planilha_TabelaBasePreco, produtos_baseDePor):
    ProdutosDePor=produtos_baseDePor.keys()
    thin_border = Side(border_style="thin", color="000000")



    for celula_CodVenda in aba_TabelaBasePreco[celula_colunaCodVendas]:
        linha_CodVenda=celula_CodVenda.row
        celulanova=aba_TabelaBasePreco[f'{nova_coluna_L}{linha_CodVenda}']
        celulanova.border = Border(top=thin_border, left=thin_border, right=thin_border, bottom=thin_border)
        if celula_CodVenda.value in cv_aplicados:
            chave_prodDePor=(produtos_baseDePor[celula_CodVenda.value])
            valor_De_DePor=(chave_prodDePor["Valor De"])


            aba_TabelaBasePreco[f'{nova_coluna_L}{linha_CodVenda}']=valor_De_DePor

            celulanova.border = Border(top=thin_border, left=thin_border, right=thin_border, bottom=thin_border)
            #print(aba_TabelaBasePreco[f'{nova_coluna_L}{linha_CodVenda}'].value)
    planilha_TabelaBasePreco.save("Arquivão_final.xlsx")


def busca_coluna_cv(aba_TabelaDePor,celula_colunaCV, cv_aplicados, celula_colunaValorPor, celula_colunaValorDe,produtos_baseDePor):
    sku_antes=[]


    #print(celula_colunaCV)
    for celula_cv in aba_TabelaDePor[celula_colunaCV]:
        linha_cv=celula_cv.row
        #print (celula_colunaValorPor)
        #print (celula_colunaValorDe)
        sku_antes.append(celula_cv.value)
        if celula_cv.value != None and celula_cv.value !="CV":
            #print(celula_cv.value)
            valorDe=(aba_TabelaDePor[f'{celula_colunaValorDe}{linha_cv}'])
            #print(valorDe)
            valorPor=(aba_TabelaDePor[f'{celula_colunaValorPor}{linha_cv}'])
            ''' produtos_baseDePor={
                    celula_cv.value:{
                        "cv":celula_cv.value,
                        "Valor De": valorDe.value,
                        "Valor Por": valorPor.value
                    }
            }'''
            produtos_baseDePor.update({celula_cv.value:{"cv":celula_cv.value, "Valor De": valorDe.value, "Valor Por": valorPor.value}})
            #print(produtos_baseDePor[celula_cv.value]["cv"])
            #print(produtos_baseDePor[celula_cv.value]["Valor De"])
            #print(produtos_baseDePor[celula_cv.value]["Valor De"])

    #print(produtos_baseDePor.keys())

    #print(sku_antes)
    #print(produtos_baseDePor)



    for produto in sku_antes:
        if produto != None and produto !="CV":

            cv_aplicados.append(produto)


    #if "De" in colunas_planilhaDePor:
    #    aba_TabelaDePor[f'A{linha1}']
    #print(cv_aplicados)


def busca_coluna_codVenda(aba_TabelaBasePreco,celula_colunaCodVendas, cv_base,produtos_basePreco,celula_colunaValorSV,celula_colunaValorSV2,nova_coluna, cv_aplicados, planilha_TabelaBasePreco,produtos_baseDePor):
    sku2_antes=[]
    nova_coluna=celula_colunaValorSV2+1
    nova_coluna_L= num_p_letra(nova_coluna)
    aba_TabelaBasePreco.insert_cols(nova_coluna)
    aba_TabelaBasePreco[f'{nova_coluna_L}{2}']="Valor De da Base DE/POR"
    for celula_CodVenda in aba_TabelaBasePreco[celula_colunaCodVendas]:
        linha_CodVenda=celula_CodVenda.row
        sku2_antes.append(celula_CodVenda.value)
        if celula_CodVenda.value != None and celula_CodVenda.value !="Código de Venda":
            valorSV=(aba_TabelaBasePreco[f'{celula_colunaValorSV}{linha_CodVenda}'])
            produtos_basePreco.update({celula_CodVenda.value:{"cv":celula_CodVenda.value, "Valor SV": valorSV.value}})

    for produto_base in sku2_antes:
        if produto_base != None and produto_base !="Código de Venda":
            cv_base.append(produto_base)

    construcao_planilha(aba_TabelaBasePreco,nova_coluna_L,celula_colunaCodVendas,cv_aplicados, planilha_TabelaBasePreco, produtos_baseDePor)


def busca_coluna_TabelaBasePreco(aba_TabelaBasePreco, cv_base, colunas_planilhaBasePreco,produtos_basePreco,nova_coluna, cv_aplicados, planilha_TabelaBasePreco,produtos_baseDePor):
    colunas_TabelaBasePreco=[]
    for colunas_BasePreco in aba_TabelaBasePreco['2']:
        colunas_BasePreco_Nome=colunas_BasePreco.value
        colunas_BasePreco_Letra=colunas_BasePreco.column_letter
        colunas_planilhaBasePreco[colunas_BasePreco_Nome] = colunas_BasePreco_Letra
        if colunas_BasePreco_Nome=="SV":
            celula_colunaValorSV2=colunas_BasePreco.column
    if "SV" in colunas_planilhaBasePreco:
        celula_colunaValorSV=colunas_planilhaBasePreco["SV"]

    if "Código de Venda" in colunas_planilhaBasePreco:
        celula_colunaCodVendas=colunas_planilhaBasePreco["Código de Venda"]
        #print(colunas_TabelaBasePreco)
        #print(celula_linha2_coluna)
        busca_coluna_codVenda(aba_TabelaBasePreco,celula_colunaCodVendas, cv_base,produtos_basePreco,celula_colunaValorSV,celula_colunaValorSV2,nova_coluna, cv_aplicados, planilha_TabelaBasePreco,produtos_baseDePor)

def  infos_planilha2(cv_base,colunas_planilhaBasePreco,produtos_basePreco, nova_coluna,aba_TabelaDePor, cv_aplicados, produtos_baseDePor):
    #TabelaBasePreco=input("Digite o nome do arquivo .xlsx, de TabelaBasePreco:")
    TabelaBasePreco="202318_Base de Preços"
    TabelaBasePreco=TabelaBasePreco+".xlsx"
    planilha_TabelaBasePreco=openpyxl.load_workbook(TabelaBasePreco)
    aba_TabelaBasePreco=planilha_TabelaBasePreco['Base de Preços BR VF']
    busca_coluna_TabelaBasePreco(aba_TabelaBasePreco, cv_base, colunas_planilhaBasePreco,produtos_basePreco,nova_coluna, cv_aplicados, planilha_TabelaBasePreco, produtos_baseDePor)

def comparador_cvs(cv_aplicados, cv_base):

    difference = [elem for elem in cv_aplicados if elem not in cv_base]
    print("Segue lista de CV's que não localizamos na base de Preços: ")
    print(difference)

def comparador_valores(aba_TabelaBasePreco,produtos_baseDePor,produtos_basePreco, cv_aplicados, cv_base,nova_coluna,  TabelaBasePreco):
    ProdutosDePor=produtos_baseDePor.keys()
    ProdutosBasePreco=produtos_basePreco.keys()
    for ProdDePor in cv_aplicados:
        if ProdDePor in ProdutosBasePreco:

            #chave_prod=produtos_baseDePor.get()
            chave_prodBasePreco=(produtos_basePreco[ProdDePor])
            #print(chave_prodBasePreco)
            valor_SV_BasePreco=(chave_prodBasePreco["Valor SV"])
            chave_prodDePor=(produtos_baseDePor[ProdDePor])
            valor_De_DePor=(chave_prodDePor["Valor De"])
            if valor_SV_BasePreco!=valor_De_DePor:
                print(f'Temos valores diferentes no CV: {ProdDePor}, \nNa Base de Preço temos o valor: {valor_SV_BasePreco} \nJá na De Por temos: {valor_De_DePor}')
                #print(type(valor_De_DePor))
            #print(chave_prodDePor)
            #print(valor_De_DePor)

    '''for ProdDePor in ProdutosDePor:
        for ProdBasePreco in ProdutosBasePreco:
            if ProdDePor == ProdBasePreco'''

def busca_coluna_TabelaDePor(aba_TabelaDePor ):
    produtos_baseDePor={}
    produtos_basePreco={}
    colunas_TabelaDePor=[]
    cv_aplicados=[]
    cv_base=[]
    nova_coluna=0
    aba_TabelaBasePreco="x"

    colunas_planilhaBasePreco={}

    colunas_planilhaDePor={}
    #print(celula_colunaCodVendas)

    for colunas_DePor in aba_TabelaDePor['4']:
        colunas_nome=colunas_DePor.value
        colunas_colunaL=colunas_DePor.column_letter
        colunas_planilhaDePor[colunas_nome] = colunas_colunaL
    #print(colunas_planilhaDePor.keys())
    if "De" in colunas_planilhaDePor:
        celula_colunaValorDe=colunas_planilhaDePor["De"]
    if "Por" in colunas_planilhaDePor:
        celula_colunaValorPor=colunas_planilhaDePor["Por"]
    if "CV" in colunas_planilhaDePor:
        celula_colunaCV=colunas_planilhaDePor["CV"]
        busca_coluna_cv(aba_TabelaDePor,celula_colunaCV, cv_aplicados, celula_colunaValorPor, celula_colunaValorDe,produtos_baseDePor)
        infos_planilha2(cv_base,colunas_planilhaBasePreco,produtos_basePreco, nova_coluna,aba_TabelaDePor, cv_aplicados, produtos_baseDePor)
    '''if "[Desconto (%)]" in colunas_planilhaDePor:
        celula_colunaValorDesconto=colunas_planilhaDePor["[Desconto (%)]"]
    if "Você Lucra" in colunas_planilhaDePor:
        celula_colunaVoceLucra=colunas_planilhaDePor["Você Lucra"]   '''


            #print(cv_aplicados) CVs de DePor
            #print(cv_base) CVs de base de preço
    comparador_cvs(cv_aplicados, cv_base)


TabelaDePor=input("Digite o nome do arquivo .xlsx, de TabelaDePor:")
#TabelaDePor="Tabela DePor_Teste (4)"
TabelaDePor=TabelaDePor+".xlsx"
planilha_TabelaDePor=openpyxl.load_workbook(TabelaDePor)
aba_TabelaDePor=planilha_TabelaDePor['Tabela DePor']
busca_coluna_TabelaDePor(aba_TabelaDePor )

