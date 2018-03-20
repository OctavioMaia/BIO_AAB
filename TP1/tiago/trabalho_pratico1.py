from metabolic_network import *
#import numpy as np
#import matplotlib.pyplot as plt


#VER COMO FAZER REGIONS EM PYTHON
#NAO CONSIGO IMPORTAR DE FORA


class MyGraph:

    def __init__(self, g={}):
        self.g = g

if __name__ == "__main__":





    ################################ PERGUNTA 1 ############################ 1.	Cria um grafo com base na rede metabólica presente nos 3 ficheiros. 
    #print("############################### PERGUNTA 1 ########################### Cria um grafo com base na rede metabólica presente nos 3 ficheiros")

    mrn = MetabolicNetwork("metabolite-reaction", {})
    mrn.load_from_files("C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-reac.txt", "C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-metab.txt", "C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-mat.txt")
    print ("--------------------METABOLITE - REACTION NETWORK--------------------")
    print("O tamanho é de:")
    print(mrn.size())
    mrn.print_graph()
    
    #mrn2 = MetabolicNetwork("metabolite", {})
    #mrn2.load_from_files("C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-reac.txt", "C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-metab.txt", "C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-mat.txt")
    #print ("-------------------- METABOLITE --------------------")
    #print("O tamanho é de:")
    #print(mrn2.size())
    #mrn2.print_graph()

    #mrn3 = MetabolicNetwork("reaction", {})
    #mrn3.load_from_files("C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-reac.txt", "C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-metab.txt", "C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-mat.txt")
    #print ("-------------------- REACTION --------------------")
    #print("O tKamanho é de:")
    #print(mrn3.size())
    #mrn3.print_graph()






    # ############################### PERGUNTA 2 ############################ 2.	Qual o número de reações e metabolitos.  
    print("\n \n \n \n ############################### PERGUNTA 2 ########################### Qual o número de reações e metabolitos")
    arq_reacao = 'C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-reac.txt'
    #f_reacao = open('C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-reac.txt')
    with open(arq_reacao, 'r') as f_reacao:
            numero_reacoes = len(f_reacao.readlines())
            f_reacao.close()
    print("O Numero de Reações é de:")
    print(numero_reacoes)


    arq_metabolito = 'C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-metab.txt'
    #f_metabolito = open('C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-metab.txt')
    with open(arq_metabolito, 'r') as f_metabolito:
            numero_metabolito = len(f_metabolito.readlines())
            f_metabolito.close()
    print("O Numero de Metabolitos é de:")
    print(numero_metabolito)





    ################################ PERGUNTA 3 ############################ 3.	Identifica os 10 metabolitos que participam num maior número de reações.
    print("\n \n \n \n ################################ PERGUNTA 3 ################################ Identifica os 10 metabolitos que participam num maior número de reações. \n ")
    
        
    print("ORDEM DECRESCENTE DOS 10 METABOLITOS QUE PARTICIPAM NUM MAIOR NUMERO DE REAÇÕES")
    print("M_h_c  -->  ['R_PGSA_EC', 'R_LCAD', 'R_GLUDy', 'R_TYRt2r', 'R_DXPRIi', 'R_HCINNMt2r', 'R_MTHFD', 'R_SERASr', 'R_GALUi', 'R_OXGDC2', 'R_DHPPDA2', 'R_CYTDt2r', 'R_D_LACt2', 'R_ILEt2r', 'R_TRSAR', 'R_PPPNDO', 'R_SHK3Dr', 'R_IGPS', 'R_GLYCLTDy', 'R_GLYCLTDx', 'R_PTPATi', 'R_GLCNt2r', 'R_IDOND2', 'R_GLXCL', 'R_GMPR', 'R_GLUTRR', 'R_2DGLCNRx', 'R_2DGLCNRy', 'R_ETOHt2r', 'R_G6PDH2r', 'R_C120SN', 'R_SERt2r', 'R_P5CR', 'R_MAN1PT2', 'R_SUCCt2b', 'R_GLUDC', 'R_DSERt2r', 'R_APRAUR', 'R_BSORx', 'R_BSORy', 'R_UAGDP', 'R_NO3R1', 'R_NO3R2', 'R_GLYCLTt2r', 'R_PPNDH', 'R_NNAT', 'R_2DGULRy', 'R_2DGULRx', 'R_PEPT_EC', 'R_OPHBDC', 'R_GALCTt2r', 'R_5DGLCNR', 'R_ADA', 'R_ADD', 'R_PIt2r', 'R_HISt2r', 'R_IDONt2r', 'R_DHORTS', 'R_C161SN', 'R_CPPPGO', 'R_DCYTD', 'R_XTSNt2r', 'R_ADNt2r', 'R_DXPS', 'R_FUCt', 'R_INDOLEt2r', 'R_TMKr', 'R_MEPCT', 'R_GLYBt2r', 'R_M1PD', 'R_TMPPP', 'R_ADHEr', 'R_GALCTNt2r', 'R_PPCDC', 'R_PYK', 'R_ASAD', 'R_C181SN', 'R_DHDPRy', 'R_GMHEPAT', 'R_GLTPD', 'R_ORNDC', 'R_DBTSr', 'R_DASYN_EC', 'R_GAPD', 'R_NO2t2r', 'R_ASNt2r', 'R_Kt2r', 'R_ASP1DC', 'R_PSSA_EC', 'R_LDH_D', 'R_BUTt2r', 'R_GLCRt2r', 'R_DMPPS', 'R_GALKr', 'R_UPPDC1', 'R_FHL', 'R_DOGULNR', 'R_ARGDC', 'R_CYTBD', 'R_DHFR', 'R_KARA1i', 'R_G3PD2', 'R_ADMDCr', 'R_PERD', 'R_C141SN', 'R_KARA2i', 'R_E4PD', 'R_GLUt2r', 'R_TMAOR1', 'R_TMAOR2', 'R_L_LACt2r', 'R_MECDPDH', 'R_PPPNt2r', 'R_CHLt2r', 'R_OCBT', 'R_AGPR', 'R_G5SD', 'R_THRt2r', 'R_DHBD', 'R_NMNAT', 'R_ACACt2', 'R_LYSDC', 'R_SBTPD', 'R_LCARS', 'R_UGLYCH', 'R_GTHOr', 'R_UAPGR', 'R_CYNTAH', 'R_PTRCt2r', 'R_HCO3E', 'R_PYRt2r', 'R_PRASCS', 'R_MANAO', 'R_ACBIPGT', 'R_ATPS4r', 'R_FDH2', 'R_FDH3', 'R_LEUt2r', 'R_DDGLCNt2r', 'R_THMDt2r', 'R_SPODM', 'R_FMNAT', 'R_SADH', 'R_IDOND', 'R_G1PTT', 'R_GLGC', 'R_ADEt2r', 'R_KG6PDC', 'R_CSND', 'R_HYD2', 'R_HYD3', 'R_GLYt2r', 'R_DPR', 'R_HYD1', 'R_HSDy', 'R_TAGURr', 'R_LYSt2r', 'R_C160SN', 'R_ACLS', 'R_NNDPR', 'R_DKGLCNR2y', 'R_DKGLCNR2x', 'R_GLUSy', 'R_ALLTNt2r', 'R_ARBt2r', 'R_CINNDO', 'R_TRDR', 'R_DALAt2r', 'R_URIt2r', 'R_VALt2r', 'R_MACPD', 'R_AOXSr', 'R_GARFT', 'R_GALU', 'R_PHEt2r', 'R_ACHBS', 'R_NTRIR2x', 'R_PSD_EC', 'R_C140SN', 'R_NAt3_1', 'R_DCTPD', 'R_NADH6', 'R_NADH7', 'R_NADH5', 'R_NADH8', 'R_NADH9', 'R_HPPPNt2r', 'R_3HCINNMH', 'R_HPYRRy', 'R_HPYRRx', 'R_CYTD', 'R_GUAD', 'R_SULR', 'R_GLCURt2r', 'R_ALAALAr', 'R_NADH10', 'R_MMCD', 'R_URAt2r', 'R_OMPDC', 'R_GOFUCR', 'R_ACt2r', 'R_ALAt2r', 'R_INSt2r', 'R_PRPPS', 'R_DAPDC', 'R_LCTSt', 'R_KAS14', 'R_KAS16', 'R_KAS15', 'R_MDH', 'R_AKGt2r', 'R_TRPt2r', 'R_3HPPPNH', 'R_CYTBO3', 'R_TDPDRR', 'R_BTS2', 'R_MTHFR2', 'R_OMCDC', 'R_ACCOACr', 'R_IPDPS', 'R_PRAGSr', 'R_ALCD19', 'R_PROt2r', 'R_DADA', 'R_GALURt2r', 'R_DKGLCNR1'] \n \n") 
    print("M_h2o_c  -->  ['R_IMPC', 'R_IMPD', 'R_LCAD', 'R_GLUDy', 'R_ARBabc', 'R_HKNTDH', 'R_MTHFC', 'R_PEAMNO', 'R_DHPPDA2', 'R_ALLTAH', 'R_HKNDDH', 'R_AHCYSNS', 'R_CYSabc', 'R_DNTPPA', 'R_MCITS', 'R_ATPM', 'R_H2Ot', 'R_CBL1abc', 'R_GLUPRT', 'R_DDPA', 'R_GALS3', 'R_PTRCabc', 'R_P5CD', 'R_MALTTRabc', 'R_SPMDabc', 'R_FBP', 'R_PYDXPP', 'R_NNAM', 'R_DKMPPD2', 'R_GPDDA1', 'R_GPDDA2', 'R_GPDDA5', 'R_GPDDA3', 'R_GPDDA4', 'R_AHC', 'R_LPLIPA2', 'R_LPLIPA1', 'R_GTPCII2', 'R_LPLIPA3', 'R_UACMAMO', 'R_METabc', 'R_BiomassEcoli', 'R_MALTPTabc', 'R_ADA', 'R_ADD', 'R_USHD', 'R_GSPMDA', 'R_CMPN', 'R_DHORTS', 'R_MALTabc', 'R_NACODA', 'R_DKMPPD', 'R_DCYTD', 'R_GLNabc', 'R_METAT', 'R_GLYC3Pabc', 'R_PRFGS', 'R_ILEabc', 'R_IPPS', 'R_G1PP', 'R_GMPS2', 'R_PRAMPC', 'R_FUM', 'R_FAO4', 'R_FAO3', 'R_FAO2', 'R_FAO1', 'R_SSALx', 'R_SSALy', 'R_ALLTN', 'R_MALTHXabc', 'R_CBLAT_DELETE', 'R_AGDC', 'R_KDOPS', 'R_KDOPP', 'R_NADPPPS', 'R_CBPS', 'R_DNMPPA', 'R_ASNabc', 'R_NMNt7', 'R_DHQD', 'R_G6PDA', 'R_HYPOE', 'R_SDPDS', 'R_THMabc', 'R_GALabc', 'R_PPC', 'R_PPA', 'R_PGPP_EC', 'R_POX', 'R_VALabc', 'R_FTHFD', 'R_PPS', 'R_MICITD', 'R_PLIPA3', 'R_PLIPA2', 'R_PLIPA1', 'R_SUCCabc', 'R_PRATPP', 'R_DUTPDP', 'R_LEUabc', 'R_MI1PP', 'R_E4PD', 'R_PYAM5PO', 'R_UDPGD', 'R_PGL', 'R_AGMT', 'R_PSP_L', 'R_NMNDA', 'R_TRPAS2', 'R_ALDD19x', 'R_ALAabc', 'R_HEMEOS', 'R_AP4AH', 'R_BETALDHx', 'R_BETALDHy', 'R_MALTTTRabc', 'R_FE2abc', 'R_HISabc', 'R_MTAN', 'R_DAPabc', 'R_UGLYCH', 'R_GMHEPPA', 'R_CRNCDH', 'R_SGDS', 'R_NTPTP2', 'R_NTPTP1', 'R_AMPN', 'R_ASNN', 'R_MOHMT', 'R_HCO3E', 'R_SELNPS', 'R_GP4GH', 'R_PAPA_EC', 'R_CDAPPA_EC', 'R_GCALDD', 'R_THRabc', 'R_ASNS1', 'R_TRE6PH', 'R_PDXPP', 'R_TRE6PP', 'R_ATPS4r', 'R_ACODA', 'R_RZ5PP', 'R_RIBabc', 'R_UHGADA', 'R_THRS', 'R_MLTG1', 'R_MLTG2', 'R_MLTG3', 'R_MLTG4', 'R_MLTG5', 'R_HMBS', 'R_CYSTL', 'R_SADH', 'R_PGLYCP', 'R_IPPMIb', 'R_IPPMIa', 'R_UDCPDP', 'R_CSND', 'R_TSULabc', 'R_PMDPHT', 'R_ORNabc', 'R_NTD10', 'R_NTD11', 'R_SGSAD', 'R_CBIAT_DELETE', 'R_LCADi', 'R_4HTHRS', 'R_AB6PGH', 'R_ALDD2x', 'R_TREH', 'R_SULabc', 'R_ARGabc', 'R_SADT2', 'R_NAMNPP', 'R_NTD9', 'R_NTD7', 'R_NTD8', 'R_NTD5', 'R_NTD6', 'R_NTD3', 'R_NTD4', 'R_NTD1', 'R_NTD2', 'R_AMPMS', 'R_ENO', 'R_MALS', 'R_OP4ENH', 'R_NADDP', 'R_AP5AH', 'R_CHLabc', 'R_HISTP', 'R_CTPS2', 'R_FFSD', 'R_GTPCI', 'R_PIabc', 'R_GLUabc', 'R_DCTPD', 'R_HISTD', 'R_CYTD', 'R_GUAD', 'R_SULR', 'R_NTPP7', 'R_NTPP8', 'R_NTPP3', 'R_NTPP4', 'R_NTPP5', 'R_NTPP6', 'R_PROabc', 'R_LACZ', 'R_ABUTD', 'R_DAAD', 'R_GLYBabc', 'R_THDPS', 'R_ICHORT', 'R_CS', 'R_BPNT', 'R_NMNN', 'R_LYSabc', 'R_METDabc', 'R_GLYOX', 'R_CYSDS', 'R_GLUN', 'R_Kabc', 'R_XYLabc', 'R_DADA', 'R_NTPP1', 'R_NTPP2', 'R_ASPabc', 'R_TAURabc'] \n \n")
    print("M_atp_c  -->  ['R_PANTS', 'R_ARBabc', 'R_DTMPK', 'R_UAMAS', 'R_PACCOAL', 'R_SERASr', 'R_CDPMEK', 'R_CYTK1', 'R_CYTK2', 'R_AACPS1', 'R_AACPS2', 'R_AACPS3', 'R_AACPS4', 'R_AACPS5', 'R_PTPATi', 'R_ADK1', 'R_ADNK1', 'R_CYSabc', 'R_GLUTRS', 'R_ATPM', 'R_CBL1abc', 'R_PTRCabc', 'R_MALTTRabc', 'R_SPMDabc', 'R_MTRK', 'R_NADS1', 'R_HPPK2', 'R_HETZK', 'R_NNAT', 'R_ADSK', 'R_TDSK', 'R_SUCBZL', 'R_GSPMDS', 'R_METabc', 'R_BiomassEcoli', 'R_PPCK', 'R_MALTPTabc', 'R_SUCOAS', 'R_PYDXNK', 'R_GTHS', 'R_TMDK1', 'R_ACS', 'R_MALTabc', 'R_DDGALK', 'R_RMK', 'R_GLU5K', 'R_GLNabc', 'R_TMKr', 'R_METAT', 'R_GLYC3Pabc', 'R_PRFGS', 'R_ILEabc', 'R_FCLK', 'R_GMPS2', 'R_CBMK', 'R_GMHEPAT', 'R_FAO3', 'R_FAO2', 'R_FAO1', 'R_MALTHXabc', 'R_CBLAT_DELETE', 'R_NADK', 'R_DBTSr', 'R_AIRC2', 'R_GART', 'R_FRUK', 'R_HSK', 'R_DAGK_EC', 'R_ADNCYC', 'R_CBPS', 'R_PYDXK', 'R_ASNabc', 'R_UAAGDS', 'R_THMabc', 'R_PRAIS', 'R_GALKr', 'R_GALabc', 'R_VALabc', 'R_SHKK', 'R_DPCOAK', 'R_PPS', 'R_PYDAMK', 'R_DHFS', 'R_SUCCabc', 'R_PMPK', 'R_TMPKr', 'R_RNTR1', 'R_LEUabc', 'R_ADOCBIK', 'R_GLYCK', 'R_UAMAGS', 'R_PGK', 'R_UGMDDS', 'R_ALAabc', 'R_PFK', 'R_GSNK', 'R_MALTTTRabc', 'R_NMNAT', 'R_FE2abc', 'R_HISabc', 'R_PPAKr', 'R_PFK_2', 'R_DAPabc', 'R_ASPK', 'R_HMPK1', 'R_THZPSN', 'R_NDPK8', 'R_NDPK7', 'R_NDPK6', 'R_NDPK5', 'R_NDPK4', 'R_NDPK3', 'R_NDPK2', 'R_NDPK1', 'R_DDGLK', 'R_GLNS', 'R_RBK', 'R_SELNPS', 'R_GLUCYS', 'R_THRabc', 'R_UMPK', 'R_ASNS2', 'R_PRASCS', 'R_ASNS1', 'R_ATPS4r', 'R_DHBSr', 'R_ARGSS', 'R_ACGK', 'R_URIDK2r', 'R_ATPPRT', 'R_RIBabc', 'R_FMNAT', 'R_GLGC', 'R_ACCOAL', 'R_TSULabc', 'R_AMANK', 'R_ORNabc', 'R_RBK_L1', 'R_ACKr', 'R_CBIAT_DELETE', 'R_DXYLK', 'R_SULabc', 'R_RBFK', 'R_ARGabc', 'R_SADT2', 'R_NAMNPP', 'R_XYLK', 'R_CHLabc', 'R_CTPS2', 'R_PIabc', 'R_GLUabc', 'R_GMHEPK', 'R_NTPP6', 'R_PROabc', 'R_ALAALAr', 'R_INSK', 'R_DGK1', 'R_PNTK', 'R_GLYBabc', 'R_PRPPS', 'R_GLYK', 'R_GNK', 'R_HEX1', 'R_LYSabc', 'R_ACCOACr', 'R_METDabc', 'R_PRAGSr', 'R_Kabc', 'R_GK1', 'R_XYLabc', 'R_ASPabc', 'R_TAURabc', 'R_DURIK1', 'R_DADK'] \n \n")
    print("M_h_e  -->  ['R_TYRt2r', 'R_HCINNMt2r', 'R_CYTDt2r', 'R_D_LACt2', 'R_ILEt2r', 'R_GLCNt2r', 'R_NAt3_15', 'R_ACNAMt2', 'R_ETOHt2r', 'R_SERt2r', 'R_DSERt2r', 'R_GLYCLTt2r', 'R_CADVt', 'R_DCYTt2', 'R_GALCTt2r', 'R_XANt2', 'R_PIt2r', 'R_HISt2r', 'R_IDONt2r', 'R_XTSNt2r', 'R_ADNt2r', 'R_FUCt', 'R_TMAOR2e', 'R_INDOLEt2r', 'R_DURIt2', 'R_GLYBt2r', 'R_GALCTNt2r', 'R_CYTDt2', 'R_GSNt2', 'R_NO2t2r', 'R_ASNt2r', 'R_TMAOR1e', 'R_Kt2r', 'R_BUTt2r', 'R_DINSt2', 'R_GLCRt2r', 'R_INSt2', 'R_DADNt2', 'R_SUCCt2_3', 'R_SUCCt2_2', 'R_GLCt2', 'R_GLUt2r', 'R_URIt2', 'R_L_LACt2r', 'R_GALt2', 'R_PPPNt2r', 'R_CHLt2r', 'R_ADNt2', 'R_THRt2r', 'R_ACACt2', 'R_HDCAt2', 'R_MALt2_2', 'R_MALt2_3', 'R_PTRCt2r', 'R_TTDCAt2', 'R_PYRt2r', 'R_THMDt2', 'R_ASPt2_2', 'R_ASPt2_3', 'R_DGSNt2', 'R_ATPS4r', 'R_LEUt2r', 'R_DDGLCNt2r', 'R_THMDt2r', 'R_GUAt2', 'R_URAt2', 'R_ADEt2r', 'R_GLYt2r', 'R_LYSt2r', 'R_ALLTNt2r', 'R_ARBt2r', 'R_DALAt2r', 'R_CSNt2', 'R_URIt2r', 'R_VALt2r', 'R_CYNTt2', 'R_PHEt2r', 'R_XYLt2', 'R_ABUTt2', 'R_NAt3_2', 'R_NAt3_1', 'R_HPPPNt2r', 'R_RMNt', 'R_GLCURt2r', 'R_MELIBt2', 'R_OCDCAt2', 'R_ASPt2', 'R_URAt2r', 'R_FUMt2_3', 'R_FUMt2_2', 'R_ACt2r', 'R_ALAt2r', 'R_INSt2r', 'R_LCTSt', 'R_THD2', 'R_AKGt2r', 'R_TRPt2r', 'R_PROt2r', 'R_GALURt2r'] \n \n")
    print("M_nad_c  -->  ['R_IMPD', 'R_LCAD', 'R_PPND', 'R_DHCIND', 'R_SHCHD2', 'R_AKGDH', 'R_P5CD', 'R_UACMAMO', 'R_PGCD', 'R_BiomassEcoli', 'R_M1PD', 'R_ADHEr', 'R_FAO4', 'R_FAO3', 'R_FAO2', 'R_FAO1', 'R_SSALx', 'R_GLTPD', 'R_NADK', 'R_GAPD', 'R_ACALDi', 'R_LDH_D', 'R_IPMD', 'R_PERD', 'R_E4PD', 'R_UDPGD', 'R_GLYCL', 'R_ALDD19x', 'R_BETALDHx', 'R_DHBD', 'R_PDX5PS', 'R_PDH', 'R_SBTPD', 'R_LCARS', 'R_GCALDD', 'R_MANAO', 'R_GLYCDx', 'R_THRD', 'R_IDOND', 'R_DHPPD', 'R_TAGURr', 'R_SGSAD', 'R_LCADi', 'R_ALDD2x', 'R_NADTRHD', 'R_NADDP', 'R_HISTD', 'R_ABUTD', 'R_ME1', 'R_MDH', 'R_ALCD19'] \n \n")
    print("M_nadph_c  -->  ['R_GLUDy', 'R_DXPRIi', 'R_MTHFD', 'R_SHK3Dr', 'R_GLYCLTDy', 'R_IDOND2', 'R_GMPR', 'R_GLUTRR', 'R_2DGLCNRy', 'R_G6PDH2r', 'R_C120SN', 'R_P5CR', 'R_APRAUR', 'R_BSORy', 'R_2DGULRy', 'R_BiomassEcoli', 'R_5DGLCNR', 'R_C161SN', 'R_ASAD', 'R_C181SN', 'R_DHDPRy', 'R_DHFR', 'R_KARA1i', 'R_G3PD2', 'R_C141SN', 'R_KARA2i', 'R_AGPR', 'R_G5SD', 'R_GTHOr', 'R_UAPGR', 'R_ICDHyr', 'R_DPR', 'R_HSDy', 'R_C160SN', 'R_DKGLCNR2y', 'R_GLUSy', 'R_TRDR', 'R_NADTRHD', 'R_C140SN', 'R_HPYRRy', 'R_SULR', 'R_GOFUCR', 'R_KAS16', 'R_TDPDRR', 'R_DKGLCNR1'] \n \n")
    print("M_nadh_c  -->  ['R_LCAD', 'R_TRSAR', 'R_PPPNDO', 'R_GLYCLTDx', 'R_2DGLCNRx', 'R_BSORx', 'R_2DGULRx', 'R_BiomassEcoli', 'R_M1PD', 'R_ADHEr', 'R_GLTPD', 'R_GAPD', 'R_LDH_D', 'R_DMPPS', 'R_DOGULNR', 'R_PERD', 'R_E4PD', 'R_DHBD', 'R_SBTPD', 'R_LCARS', 'R_MANAO', 'R_IDOND', 'R_TAGURr', 'R_DKGLCNR2x', 'R_CINNDO', 'R_NTRIR2x', 'R_NADH6', 'R_NADH7', 'R_NADH5', 'R_NADH8', 'R_NADH9', 'R_3HCINNMH', 'R_HPYRRx', 'R_NADH10', 'R_MDH', 'R_THD2', 'R_3HPPPNH', 'R_MTHFR2', 'R_IPDPS', 'R_ALCD19'] \n \n")
    print("M_pi_c  -->  ['R_GLYC3Pt6', 'R_PUNP3', 'R_PUNP2', 'R_PUNP1', 'R_PUNP4', 'R_PUNP5', 'R_PUNP6', 'R_PUNP7', 'R_TMDPP', 'R_SUCOAS', 'R_PIt2r', 'R_G6Pt6_2', 'R_PTA2', 'R_ASAD', 'R_CBLAT_DELETE', 'R_DBTSr', 'R_GAPD', 'R_GLCP', 'R_PTAr', 'R_MAN6Pt6_2', 'R_OCBT', 'R_AGPR', 'R_FUCPt6_2', 'R_MLTP1', 'R_MLTP3', 'R_MLTP2', 'R_PRASCS', 'R_ATPS4r', 'R_CBIAT_DELETE', 'R_PSCVT', 'R_DURIPP', 'R_ALAALAr', 'R_PYNP2r', 'R_ACCOACr', 'R_PRAGSr'] \n \n")
    print("M_adp_c  -->  ['R_DTMPK', 'R_CYTK1', 'R_CYTK2', 'R_ADK1', 'R_ADK4', 'R_ADK3', 'R_RNDR1', 'R_SUCOAS', 'R_TMKr', 'R_PYK', 'R_DBTSr', 'R_GALKr', 'R_TMPKr', 'R_PGK', 'R_PPAKr', 'R_ASPK', 'R_NDPK8', 'R_NDPK7', 'R_NDPK6', 'R_NDPK5', 'R_NDPK4', 'R_NDPK3', 'R_NDPK2', 'R_NDPK1', 'R_UMPK', 'R_PRASCS', 'R_ATPS4r', 'R_URIDK2r', 'R_ACKr', 'R_ALAALAr', 'R_DGK1', 'R_ACCOACr', 'R_PRAGSr', 'R_GK1', 'R_DADK'] \n \n")
    print("M_glu_DASH_L_c  -->  ['R_GLUDy', 'R_GLUTRS', 'R_GLUDC', 'R_BiomassEcoli', 'R_ALATA_L', 'R_ASPTA', 'R_GLU5K', 'R_VALTA', 'R_TYRTA', 'R_UNK3', 'R_LEUTAi', 'R_GLUABUTt7', 'R_ACOTA', 'R_DHFS', 'R_GLUt2r', 'R_ILETA', 'R_GLNS', 'R_GLUCYS', 'R_SDPTA', 'R_ACGS', 'R_TDPAGTA', 'R_PHETA1', 'R_HSTPT', 'R_GLUR', 'R_PSERT', 'R_OHPBAT'] \n \n")



    


    ################################ PERGUNTA 4 ############################ 4.	Cria um gráfico com a distribuição do número de reações por cada um dos possíveis graus do tipo “inout”.

    print("\n \n \n \n ################################ PERGUNTA 4 ################################ Cria um gráfico com a distribuição do número de reações por cada um dos possíveis graus do tipo “inout” \n ")
    print(mrn.all_degrees(deg_type="inout"))   






    ################################ PERGUNTA 5 ############################ 5.	Identifica os metabolitos que são dead ends, isto é, metabolitos que são produzidos e não há reações que os consumam. 


    arq_matri = 'C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-mat.txt'
    ref_arquivo = open(arq_matri,"r") 

    arq_metabolito = 'C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-metab.txt'
    ref_arquivo_metabolito = open(arq_metabolito,"r") 
   
    linha = ref_arquivo.readline()    
    count__find=0

    count = 0
    for linha in ref_arquivo:
        count = count + 1
        caracter = "-1.0"
        if linha.count(caracter) == 1:
            texto = ref_arquivo_metabolito.readline(count)

            print("O ID da linha do ficheiro MATRIX que contem os metabolitos que são produzidos e não há reações que os consumam: ID = ", count, "Metabolito = ", texto)

    # !!!! FALTA PROCURAR PELO ID NO TXT


    ################################ PERGUNTA 6 ############################ 6.	Considerando uma lista de metabolitos como uptake dado pelo utilizador, implementa uma função que retorna quais os produtos excretados pelo modelo. 


    





    ################################ PERGUNTA 7 ############################ 7.	Cria uma função que dado um metabolito dado pelo utilizador devolve a lista de reações que produzem esse metabolito.

    mrn = MetabolicNetwork("metabolite-reaction", {})
    mrn.load_from_files("C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-reac.txt", "C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-metab.txt", "C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/exemplo-mat.txt")
    print ("--------------------METABOLITE - REACTION NETWORK--------------------")
    #print("O tamanho é de:")
    #print(mrn.size())
    #mrn.print_graph()

    
    with open("C:/Users/TiagoAzevedo/Desktop/1 - Algoritmos Avançados de BioInformatica/TrabalhoPrático/reacoes_que_geraram_metabolitos.txt", "r") as arq:
        for f in arq.readlines():
            #!!!??VER PQ QUANDO FAÇO O INPUT DO METABOLITO NA CONSOLA NAO ENCONTRA AS REAÇÕES QUE O GERARAM MAS SE INTRODUZIR NO CODIGO JÁ FUNCIONA
            #input_pesquisaMetabolito = input ("Introduza o metabolico na qual pretende saber quais as reacoes que o geraram \n")
            if(f.find("M_gln_DASH_L_c")>-1):
                print (f)
    





    ################################ PERGUNTA 8 ############################ 8.	Valida que no modelo não existem reações que contenham o mesmo metabolito como reagente e produto, se existir devolve uma lista contendo essas reações, caso contrário devolve None.






    ################################ PERGUNTA 9 ############################ 9.	Implementa uma função que dado o metabolito origem e metabolito destino retorne todos os caminhos possíveis entre estes dois nós, onde o caminho é composto pela sequência de nós que permite da origem chegar ao destino.






    ################################ PERGUNTA 10 ############################ 10.	Implementa uma função que retorne a lista de ciclos existentes na rede. Clico: é a sequência de nodos que dado um ponto inicial consegue voltar ao mesmo ponto.  
