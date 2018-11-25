import random
import mysql.connector
from country_list import countries_for_language
from scipy.stats import truncnorm

#Peguei do https://stackoverflow.com/questions/36894191/how-to-get-a-normal-distribution-within-a-range-in-numpy
def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)
generos = [
        "Masculino",
        "Feminino",
        "Outro"
        ]
nomes = [
        "Socrusto",
        "Pimpernelo",
        "Witor",
        "Samille",
        "Kennya",   
        "Jilberto",
        "Giairo",
        "Creysson",
        "Hericlepton",
        "Waldisney",
        "Joleno",
        "Tsunderio",
        "Tormato",
        "Dorlange",
        "Gilderoi",
        "Miriadas",
        "Maralena",
        "Tobio",
        "Onyx",
        "Sabriel",
        "Descolado",
        "Anjelino",
        "Joender",
        "Jemerson",
        "Galerio",
        "Cavalheiro",
        "Kaylo",
        "Hendersel",
        "Kuderio",
        "Stanislau",
        "Gastoncio",
        "Deviloguia",
        "Maximo",
        "Yrlla",
        "Demetrius",
        "Kelia",
        "Sumireca",
        "Deuzivaldo",
        "Eraldonclobes",
        "Madeinusa",
        "Mijardina",
        "Jhaulismaflancyo",
        "Heubler",
        "Wonarllevyston",
        "Libertino",
        "Gosmoguete",
        "Wanslívia",
        "Hermengarda",
        "Mirella"
        ]

sobrenomes = [
        "de Andrade",
        "das Couves",
        "Spiderman",
        "Hanekawa",
        "Matador",
        "Demolidor",
        "Tobias",
        "Jacinto",
        "Bulbassauro",
        "Massimanilo",
        "Degeneris",
        "Lacroix",
        "Las Casas",
        "Brasileiro",
        "Africano",
        "Americano",
        "Alvarenga",
        "Torres",
        "Carlos",
        "Alien",
        "Flanckson",
        "Frickson",
        "Rhazyel",
        "Raimundo",
        "Misericordioso",
        "Kennemann",
        "Nemelgar",
        "Canudo",
        "Pedrosa",
        "Dratini",
        "Macharet",
        "Meira",
        "Gordo",
        "Fiorentino",
        "Castelo Branco",
        "Siqueira",
        "Gomide",
        "Zonatto",
        "Magalhaes",
        "Varella",
        "Bezerra",
        "Almirante",
        "Padeiro",
        "Glabber",
        "Globber",
        "Walquiria",
        "Quenia",   
        "Lorenzoni",
        "Pedersen",
        "Moro"
        ]

distros = [
        ("Manjaro", "Rolling", "pacman", "Manjaro Team", "Arch"),
        ("Mint", "Common", "apt", "Mint Team", "Debian"),
        ("elementary OS", "Common", "apt", "elementary Os Team", "Ubuntu"),
        ("MX Linux", "Common", "apt", "community", "Debian/anitX"),
        ("Ubuntu LTS", "LTS", "apt", "Canonical", "Debian"),
        ("Ubuntu", "Common", "apt", "Canonical", "Debian"),
        ("Debian Stable", "LTS", "apt", "community", "independent"),
        ("Debian Testing", "Rolling", "apt", "community", "independent"),
        ("Debian Unstable", "Rolling", "apt", "community", "independent"),
        ("Fedora", "Rolling", "dnf", "Red Hat", "independent"),
        ("openSUSE Leap", "LTS", "zypper", "SUSE", "independent"),
        ("openSUSE Tumbleweed", "Rolling", "zypper", "SUSE", "independent"),
        ("Solus", "Rolling", "eopkg", "Solus devs", "independent"),
        ("Arch", "Rolling", "pacman", "community", "independent"),
        ("CentOS", "LTS", "yum", "CentOS Project", "Red Hat Enterprise Linux"),
        ("Red Hat Enterprise Linux", "LTS", "yum", "Red Hat", "independent")
]

desktops = [
        ("AfterStep"),
        ("Awesome"),
        ("BlackBox"),
        ("Cinnamon"),
        ("GNOME"),
        ("IceWM"),
        ("KDE"),
        ("MATE"),
        ("LXQt"),
        ("Pantheon"),
        ("Xfce")
]

maintainters = [
        ("community", "non-profit", "international", None),
        ("Manjaro Team", "non-profit", "international", None)
]

CHANCE_SOBRENOME_ADICIONAL = 0.4
def generate_names(amount):
    nomes_completos = []
    nome_range = len(nomes) - 1
    sobrenome_range = len(sobrenomes) - 1
    for i in range(amount):
        nome_completo = ""
        nome_completo += nomes[random.randint(0,nome_range)]
        sobrenome_adicional_rand = 0
        while(sobrenome_adicional_rand <= CHANCE_SOBRENOME_ADICIONAL):
            nome_completo += " " + sobrenomes[random.randint(0,sobrenome_range)]
            sobrenome_adicional_rand = random.random()
        nomes_completos.append(nome_completo)
    
    return nomes_completos

MIN_AGE = 14
MAX_AGE = 95
TOTAL_INSERT_AMOUNT = 100
INSERT_BUFFER_SIZE = 10
HOST = "localhost"
USER = "root"
PASS = "123456"
DB_NAME = "ibd_final"
#mydb = mysql.connector.connect(
#  host=HOST,
#  database=DB_NAME,
#  user=USER,
#  passwd=PASS
#)
#
#
#cursor = mydb.cursor()
#sql_insert_query = """ INSERT INTO usuarios (nome, genero,idade, pais) 
#                       VALUES (%s,%s,%s,%s) """
id = 0
ages_normal = get_truncated_normal(mean=35, sd=20, low=MIN_AGE, upp=MAX_AGE)
countries = list(dict(countries_for_language('en')).values())
for num_insertions in range(TOTAL_INSERT_AMOUNT):
    names = generate_names(INSERT_BUFFER_SIZE)
    ages = ages_normal.rvs(INSERT_BUFFER_SIZE)
    insert_params = []
    
    
    for buffer in range(INSERT_BUFFER_SIZE):
        line_tuple = (id,
                      names[buffer],
                      generos[random.randint(0,len(generos) - 1)],
                      int(ages[buffer]),
                      countries[random.randint(0,len(countries) - 1)],
                      random.choice([True, False]))
        insert_params.append(line_tuple)
        id += 1
    print(insert_params)

for it in distros:
    print(it)

for num_insertions in range(TOTAL_INSERT_AMOUNT):
    insert_params = []
    for buffer in range(INSERT_BUFFER_SIZE):
        line_tuple = (random.randint(0, id), random.choice(distros)[0])
        insert_params.append(line_tuple)
    print(insert_params)
