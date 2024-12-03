from Crypto.Util.number import bytes_to_long,inverse,getPrime,long_to_bytes
from Crypto.PublicKey import RSA    #常用于导入公钥
from gmpy2 import gcd,gcdext   #欧几里得算法和欧几里得扩展算法，分别用于求解最大公因数和求解s

### 导入公钥例程 ###
# with open("pubkey1.pem","rb") as f:
#     pk1_bit= f.read()
# with open("pubkey2.pem","rb") as f:
#     pk2_bit =f.read();
#
# pk1 = RSA.importKey(pk1_bit)
# pk2 = RSA.importKey(pk2_bit)
#
# n1 = pk1.n
# e1 = pk1.e
# n2 = pk2.n
# e2 = pk2.e
###


### RSA常规解密算法 ###

# n1=23220619839642624127208804329329079289273497927351564011985292026254914394833691542552890810511751239656361686073628273309390314881604580204429708461587512500636158161303419916259271078173864800267063540526943181173708108324471815782985626723198144643256432774984884880698594364583949485749575467318173034467846143380574145455195152793742611717169602237969286580028662721065495380192815175057945420182742366791661416822623915523868590710387635935179876275147056396018527260488459333051132720558953142984038635223793992651637708150494964785475065404568844039983381403909341302098773533325080910057845573898984314246089
# p1=138376604533530412400239558340424700312412702699022481119357799054715877829291635290832719835033140580690053865677079316241919169166375123691917675235979462772103681398725285808551041924624882840901583892858174270714471366531758975241868470938138238307005782651296179579961869801841395682782645916848523771439
# q1=167807411649676462546661119644113081915542378755778327057156191284453150887662343414908916953154897183613548083558919410359642450001343644814021159828724844730881111955050992398535063409828169462180970629537792676998647880110463527555034040871485964361418080481113059959410616446772218038141157051007091689351
# e1=65537
# c1=9700614748413503291260966231863562117502096284616216707445276355274869086619796527618473213422509996843430296526594113572675840559345077344419098900818709577642324900405582499683604786981144099878021784567540654040833912063141709913653416394888766281465200682852378794478801329251224801006820925858507273130504236563822120838520746270280731121442839412258397191963036040553539697846535038841541209050503061001070909725806574230090246041891486506980939294245537252610944799573920844235221096956391095716111629998594075762507345430945523492775915790828078000453705320783486744734994213028476446922815870053311973844961
#
# n2=22642739016943309717184794898017950186520467348317322177556419830195164079827782890660385734113396507640392461790899249329899658620250506845740531699023854206947331021605746078358967885852989786535093914459120629747240179425838485974008209140597947135295304382318570454491064938082423309363452665886141604328435366646426917928023608108470382196753292656828513681562077468846105122812084765257799070754405638149508107463233633350462138751758913036373169668828888213323429656344812014480962916088695910177763839393954730732312224100718431146133548897031060554005592930347226526561939922660855047026581292571487960929911
# p2=138376604533530412400239558340424700312412702699022481119357799054715877829291635290832719835033140580690053865677079316241919169166375123691917675235979462772103681398725285808551041924624882840901583892858174270714471366531758975241868470938138238307005782651296179579961869801841395682782645916848523771439
# q2=163631266233712837481823088378337134151021871060275887871338250274359922218053543333532579728777813509956261662615493179160669715503833949420308311581736674332268131534602581626817039237393599222688271607325131529790640375765697832746614700483681658911753936520482383592478743093233261371451718844275762094649
# e2=65537
# c2=20513108670823938405207629835395350087127287494963553421797351726233221750526355985253069487753150978011340115173042210284965521215128799369083065796356395285905154260709263197195828765397189267866348946188652752076472172155755940282615212228370367042435203584159326078238921502151083768908742480756781277358357734545694917591921150127540286087770229112383605858821811640935475859936319249757754722093551370392083736485637225052738864742947137890363135709796410008845576985297696922681043649916650599349320818901512835007050425460872675857974069927846620905981374869166202896905600343223640296138423898703137236463508
#
# phi_1 = (p1-1)*(q1-1)
# phi_2 = (p2-1)*(q2-1)
#
# d1 = inverse(e1,phi_1)
# d2 = inverse(e2,phi_2)
#
# m1 =pow(c1,d1,n1)
# m2 =pow(c2,d2,n2)
#
# print(long_to_bytes(m1)+long_to_bytes(m2))
###

### RSA共模攻击例程 ###
# with open("cipher1.txt","rb") as f:
#     c1= f.read()
# with open("cipher2.txt","rb") as f:
#     c2= f.read()
#
# c1= bytes_to_long(c1)
# c2= bytes_to_long(c2)
#
# s= gcdext(e1,e2)
# # print(s)
#
# m = (pow(c1,s[1],n1)*pow(c2,s[2],n2) ) % n1
# m = long_to_bytes(m)
# print(m)
###

### 低指数广播攻击 ###
# from gmpy2 import *
# from functools import reduce
# elems=[{"c": 7366067574741171461722065133242916080495505913663250330082747465383676893970411476550748394841437418105312353971095003424322679616940371123028982189502042, "e": 10, "n": 25162507052339714421839688873734596177751124036723831003300959761137811490715205742941738406548150240861779301784133652165908227917415483137585388986274803},
# {"c": 21962825323300469151795920289886886562790942771546858500842179806566435767103803978885148772139305484319688249368999503784441507383476095946258011317951461, "e": 10, "n": 23976859589904419798320812097681858652325473791891232710431997202897819580634937070900625213218095330766877190212418023297341732808839488308551126409983193},
# {"c": 6569689420274066957835983390583585286570087619048110141187700584193792695235405077811544355169290382357149374107076406086154103351897890793598997687053983, "e": 10, "n": 18503782836858540043974558035601654610948915505645219820150251062305120148745545906567548650191832090823482852604346478335353784501076761922605361848703623},
# {"c": 4508246168044513518452493882713536390636741541551805821790338973797615971271867248584379813114125478195284692695928668946553625483179633266057122967547052, "e": 10, "n": 23383087478545512218713157932934746110721706819077423418060220083657713428503582801909807142802647367994289775015595100541168367083097506193809451365010723},
# {"c": 22966105670291282335588843018244161552764486373117942865966904076191122337435542553276743938817686729554714315494818922753880198945897222422137268427611672, "e": 10, "n": 31775649089861428671057909076144152870796722528112580479442073365053916012507273433028451755436987054722496057749731758475958301164082755003195632005308493},
# {"c": 17963313063405045742968136916219838352135561785389534381262979264585397896844470879023686508540355160998533122970239261072020689217153126649390825646712087, "e": 10, "n": 22246342022943432820696190444155665289928378653841172632283227888174495402248633061010615572642126584591103750338919213945646074833823905521643025879053949},
# {"c": 1652417534709029450380570653973705320986117679597563873022683140800507482560482948310131540948227797045505390333146191586749269249548168247316404074014639, "e": 10, "n": 25395461142670631268156106136028325744393358436617528677967249347353524924655001151849544022201772500033280822372661344352607434738696051779095736547813043},
# {"c": 15585771734488351039456631394040497759568679429510619219766191780807675361741859290490732451112648776648126779759368428205194684721516497026290981786239352, "e": 10, "n": 32056508892744184901289413287728039891303832311548608141088227876326753674154124775132776928481935378184756756785107540781632570295330486738268173167809047},
# {"c": 8965123421637694050044216844523379163347478029124815032832813225050732558524239660648746284884140746788823681886010577342254841014594570067467905682359797, "e": 10, "n": 52849766269541827474228189428820648574162539595985395992261649809907435742263020551050064268890333392877173572811691599841253150460219986817964461970736553},
# {"c": 13560945756543023008529388108446940847137853038437095244573035888531288577370829065666320069397898394848484847030321018915638381833935580958342719988978247, "e": 10, "n": 30415984800307578932946399987559088968355638354344823359397204419191241802721772499486615661699080998502439901585573950889047918537906687840725005496238621}]
#
# cips =[]
# keys =[]
#
# for elem in elems:
#     cips.append(elem["c"])
#     keys.append(elem["n"])
#
#
# def crt(remainders, moduli):
#     """
#     中国剩余定理实现
#     :param remainders: 余数列表 [r1, r2, ...]
#     :param moduli: 模数列表 [m1, m2, ...]
#     :return: 满足所有条件的最小非负整数解 x
#     """
#     # 确保余数和模数数量一致
#     if len(remainders) != len(moduli):
#         raise ValueError("Remainders and moduli must have the same length.")
#     # 计算模数的乘积
#     M = reduce(lambda x, y: x * y, moduli)
#     # 计算解
#     x = 0
#     for r, m in zip(remainders, moduli):
#         Mi = M // m
#         # 求 Mi 关于模 m 的逆元
#         Mi_inv = pow(Mi, -1, m)  # 使用 Python 3.8+ 的内置模逆函数
#         x += r * Mi * Mi_inv
#
#     return x % M
# sol = crt(cips,keys)
# msg,flag = iroot(mpz(str(sol)),mpz(str(10)))
# print(long_to_bytes(msg))

###