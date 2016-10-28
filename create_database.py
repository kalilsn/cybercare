import sqlite3
import os

dbname = "cybercare.db"

if not os.path.isfile(dbname):
    db = sqlite3.connect(dbname)
    db.execute(
        """
        CREATE TABLE customers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            telephone INTEGER,
            street TEXT,
            city TEXT,
            state CHAR(2),
            zip TEXT
        );
        """
    )
    db.executescript(
        """
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Jared Gibbs','hin@bojol.gov',962435262,'1698 Feghu Trail','Lihnavref','LA','37100');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Alma Jensen','ep@wiwi.com',481190297,'314 Conu Manor','Ucimhug','UT','39067');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Danny Goodwin','kawub@zalubu.com',671681860,'1899 Surew Park','Konerpo','MI','06892');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Nancy Powell','kummod@ji.gov',399443529,'944 Ucguk Pike','Piacumu','IL','57983');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Mildred Underwood','paba@juohaig.com',094366396,'1629 Lilto Junction','Vubukaf','LA','91300');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Jeffrey Holt','ifru@reklokbi.edu',089780449,'270 Zubi River','Modigza','MI','80018');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Dylan Silva','ziec@gehwatir.edu',774025478,'1834 Jakib Park','Fevomjuf','GA','42325');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Eliza Stewart','fa@ji.net',346960023,'1904 Muzo Heights','Ewanecuk','DC','17422');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Corey Warner','dornechuv@led.com',316620262,'169 Zosu River','Osmohon','TN','41940');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Russell Castillo','supbiogo@nein.co.uk',907637673,'1882 Jacav Loop','Edlewwaj','OR','01767');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Claudia Castillo','be@jotfewa.com',819649717,'73 Urrik Court','Pevobfi','VA','59971');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Josie Davidson','ko@radagi.gov',848695280,'903 Bezfe Boulevard','Unokube','DE','42683');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Isaiah Gross','tomzozva@ponjirti.org',114322837,'1781 Tawrit Highway','Taztoav','NC','70958');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Leroy Morris','piwfob@kazih.edu',574862727,'1943 Joojo Turnpike','Pucviro','SD','04549');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('George Oliver','jaavecu@ihpus.org',018041767,'458 Vijjat Square','Cucdoob','WA','54658');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Howard Owen','kibi@uvmeuju.org',560095992,'1485 Zuwfa Grove','Elciwi','MA','87428');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Ruby Casey','asoke@jib.co.uk',781841402,'1866 Pipa Road','Owopokno','WV','44633');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Katie Hernandez','kiszaam@okaejnop.edu',967887379,'1628 Jalabu Extension','Zelofu','LA','41319');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Isabel Stevens','bo@zalezu.io',899500295,'970 Fecso Boulevard','Bivuguho','MS','54201');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Myrtle Steele','pego@kimtigo.net',055423490,'1509 Pobu Circle','Ografdu','SD','25230');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Wayne Garcia','pinuf@ipoesga.co.uk',921009390,'652 Ligu Boulevard','Puutepe','GA','84665');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Jeff Greer','os@goz.gov',773771782,'539 Wuhah Junction','Esdowub','OK','17048');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Emily Castillo','ofi@fo.co.uk',675141895,'1555 Eboroh Point','Joricjib','KS','23730');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Grace Goodman','ugnofipi@zeiji.io',849499360,'387 Gekso Lane','Liwenino','MI','85815');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Michael Nunez','nadmajzec@bilobu.edu',227598875,'150 Furo Pike','Arizepus','MI','89523');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Dylan Greer','tifuwu@lihajboh.gov',349547920,'1152 Wulca Road','Pifkerit','HI','89345');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Olive Norris','me@owahu.co.uk',591322592,'1851 Buvib Extension','Zocatu','VA','95292');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Amelia Mack','olfa@zazliwri.gov',884032948,'1815 Tehba Ridge','Opajipze','NC','24219');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Alta Patton','tem@imto.org',170095835,'1860 Duez Path','Hasuwpa','IN','68153');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Ada Joseph','lu@zurlefnuh.io',296807163,'526 Pisaf Highway','Zofluli','WV','17046');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Minerva Fleming','jinozi@jolitor.co.uk',939483072,'1306 Caom Square','Omolecus','KS','02205');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Josephine Owens','co@weda.com',074552967,'98 Nures Mill','Kozitwe','WA','28634');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Birdie Williamson','onuwasu@ge.org',630141131,'1538 Pagfak Avenue','Midsire','OK','33372');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Christian Stone','zurol@go.com',244439433,'934 Kasiv Drive','Ibubajzek','NM','60623');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Minerva Lambert','hig@ozoehitu.edu',525455137,'1223 Epdon Glen','Rofufus','IA','75307');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Nathan Alvarez','tir@vodoh.org',681315792,'1996 Mudo Terrace','Lemmolu','IL','84959');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Marie Franklin','kakujdu@be.gov',373067411,'783 Bobo Street','Duaruf','WA','92058');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Charlie Potter','uc@fewmop.net',225378164,'150 Ohme View','Adajjo','ID','63954');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Martha Cole','fuwjer@seowfi.net',837770701,'345 Fafuv Mill','Leteniped','NH','24507');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Mittie Gregory','darik@pa.net',864006142,'300 Foperu View','Vuawona','AK','17575');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Edwin Henry','ub@duhi.edu',489378493,'1753 Toze Circle','Lojawius','NV','39713');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Eric Lewis','ru@wav.com',612254737,'1992 Cione River','Lovkunu','IL','66036');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Bettie Padilla','ji@nuzer.co.uk',094778164,'1386 Melne Square','Rukdihuk','PA','60332');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Caroline Sparks','rupetba@cagwiv.org',062870710,'474 Tiapi Street','Nivawuw','MT','16897');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Devin Frank','dekcujjiv@tav.com',307240756,'1574 Mirob Pass','Lijucoc','CO','56095');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Rosalie Farmer','uguto@na.edu',973483441,'1440 Dagvi Plaza','Basipaj','LA','44382');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Max Vasquez','loos@lidok.gov',271808101,'1668 Forza Manor','Sovivob','UT','50444');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Maurice Stephens','wajga@ozooli.io',640214557,'1341 Oholaw Drive','Pacejer','MI','78554');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Allie Yates','vimamver@ra.co.uk',140826486,'1713 Nakos Highway','Oshakzi','PA','16616');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Katharine Glover','omsa@rieduug.co.uk',756542885,'1004 Ovapi Trail','Aciafpu','MT','40030');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Nicholas Pearson','iturooz@pup.org',041588703,'1994 Dicli Plaza','Ocuseduh','MT','13193');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Clayton Lawson','ladna@owo.com',508273871,'912 Okrok Key','Reozinim','IN','04502');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Gussie Warren','ohora@ka.co.uk',882531940,'183 Rucpal Glen','Carwezguf','DE','77577');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Anthony Roy','wildoz@kegheove.gov',307259216,'298 Kawib River','Vacsaddi','SD','74600');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Isaiah Hoffman','ucazag@suruka.co.uk',535228192,'1078 Kavaw Heights','Laezne','CO','20868');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Micheal Poole','nuwejoh@mewdem.com',460663965,'1086 Tiztuj Pike','Ulujacif','RI','87386');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Linnie Mullins','tafugen@eb.edu',568795680,'1030 Okilah Circle','Kizujsu','UT','43180');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Kathryn Harper','hilud@mim.net',618977694,'766 Fizdod Center','Jufufit','AL','98332');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Olivia Marshall','gu@kohlagis.org',046184597,'435 Noffaj Trail','Hegetubol','IA','40129');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Mason Harvey','wo@rubfecjew.io',374584951,'358 Hutaz Path','Fuozije','OR','54265');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Jackson Lee','efomilut@kimlinub.edu',453241904,'510 Agimu Ridge','Raleges','RI','89873');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Nathaniel Henry','esum@ve.edu',753813704,'824 Musko Key','Tenasseb','ID','13805');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Essie Potter','sad@fun.co.uk',615906451,'1371 Weruv Square','Hukpevnur','FL','94273');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Zachary Moss','isukuge@zasfonmas.com',975684811,'1929 Mipi Parkway','Tulbitcek','MO','95725');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Bryan Waters','pe@wepenet.edu',945574153,'1279 Mavab Parkway','Seadovub','OR','41866');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Edith Hunter','icowej@meal.edu',657059564,'1733 Vehed Terrace','Ofubisij','IA','38581');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Joel Warren','tahbeghat@et.org',674668755,'484 Nisawi View','Bozjarciz','OH','28986');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Alfred Chapman','cudih@didupu.gov',476380322,'422 Hotso Court','Mofhikrad','MO','13444');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Austin Flores','segdurlu@lit.edu',119521344,'227 Fugwa Boulevard','Fawrisoz','NH','18566');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Dorothy Black','ud@bepdev.org',390805604,'914 Canwor Glen','Piazara','VA','09143');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Ellen Fisher','wutela@keep.com',176208288,'593 Gejrec Park','Iggusmuz','MO','38494');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Lydia Keller','zesbeek@bepwo.org',622004270,'563 Ewrov Trail','Tikpomew','IL','76358');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Tyler Henderson','gu@ukoami.gov',691417177,'780 Zovo Trail','Edfegir','ND','67490');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Carrie Bowman','hurcuvepo@maof.edu',772141396,'1938 Liwba Trail','Cumiztoz','NY','81973');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Connor Patterson','lujihga@ijodubur.io',616674773,'1701 Wajtah Square','Epadede','GA','54813');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Mabel Fowler','ti@vumissom.io',997462726,'1501 Awid Grove','Wanlicav','NM','60251');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Raymond Craig','rup@mesaltes.gov',262968692,'1311 Lajis Circle','Dahmuku','MT','94127');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Aaron Nichols','daep@zikokli.co.uk',926000485,'891 Zuit View','Izakermu','AK','06081');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Troy Warner','epuze@inupve.com',546155909,'208 Soun Trail','Dumele','MA','43896');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Eddie Houston','idu@sat.co.uk',355819561,'1182 Pinem Junction','Bogikip','MD','40454');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Michael Harmon','nena@milpursaz.net',633755684,'706 Nunep Glen','Jowkaubo','OK','71685');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Christopher Patton','cirbovih@gijhavkuz.net',908894966,'113 Wicawa Turnpike','Inewabdu','AR','25599');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Marguerite Murray','liufeko@su.co.uk',814104759,'866 Sigla Square','Utijuhaw','AL','30301');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Adrian Moore','agjiewe@fud.io',686513883,'1151 Eszi Road','Gijgadab','NH','08251');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Danny Neal','ulra@na.net',605886436,'1214 Baop Heights','Agsisloj','AL','25394');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Rosa Page','zupi@sofojib.net',814982803,'1181 Ipote Highway','Romwuzle','MS','03441');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Frederick Gray','efokolce@wot.io',357988094,'431 Mimzo Key','Pomenrid','IA','93627');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('James Griffin','zamezlu@zitpi.edu',105771020,'1642 Sudepi Glen','Sasuaka','ID','24758');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Jonathan Hanson','zu@dudarno.io',432361979,'1590 Suki Way','Moemgej','MI','14625');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('George Hunter','ciko@zeggi.edu',835260115,'1088 Leplu Boulevard','Jedbapu','NC','75442');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Sue Parks','jusnucor@icu.gov',908140279,'1667 Vapop Key','Tabaczok','NM','01034');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Thomas Tucker','najsa@wizvobu.net',162306354,'1835 Akfif Ridge','Nufamve','CA','00007');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Jacob Ruiz','etkuhudu@elrip.org',523051727,'197 Fihruj Lane','Nikitzej','MI','96062');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Carlos Boone','zebebi@remija.com',320357215,'1520 Eran Grove','Japehmeh','AL','40532');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Delia Reed','iv@el.com',410879367,'1386 Fehu Boulevard','Hocuwvij','VT','66501');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Katie Gill','nicadi@luij.io',321693650,'15 Wofo Road','Anocpug','DC','55486');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Lloyd Welch','doojuza@fekgop.net',526229195,'906 Dosik Parkway','Golhutan','OH','91924');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Jeff Taylor','piktirse@fob.net',382956965,'1568 Degiba Mill','Ziindi','NE','52140');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Callie Sharp','da@leblodnu.gov',772296441,'1678 Gotfa Center','Udatatos','IN','28318');
        INSERT INTO customers(name,email,telephone,street,city,state,zip)
        VALUES ('Gilbert Curtis','azfofebe@ribuziz.net',341374444,'1544 Zuod Plaza','Vabwigi','MD','47960');
        """
    )
