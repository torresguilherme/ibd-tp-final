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
        ("Mint", "LTS", "apt", "Mint Team", "Debian Unstable"),
        ("elementary OS", "Common", "apt", "elementary OS Team", "Ubuntu LTS"),
        ("MX Linux", "Common", "apt", "community", "Debian Stable"),
        ("Ubuntu LTS", "LTS", "apt", "Canonical", "Debian Stable"),
        ("Ubuntu", "Common", "apt", "Canonical", "Debian Stable"),
        ("Debian Stable", "LTS", "apt", "community", None),
        ("Debian Testing", "Rolling", "apt", "community", None),
        ("Debian Unstable", "Rolling", "apt", "community", None),
        ("Fedora", "Rolling", "dnf", "Red Hat", None),
        ("openSUSE Leap", "LTS", "zypper", "SUSE", None),
        ("openSUSE Tumbleweed", "Rolling", "zypper", "SUSE", None),
        ("Solus", "Rolling", "eopkg", "Solus devs", None),
        ("Arch", "Rolling", "pacman", "community", None),
        ("CentOS", "LTS", "yum", "Red Hat", "Red Hat Enterprise Linux"),
        ("Red Hat Enterprise Linux", "LTS", "yum", "Red Hat", None)
]

distro_arch = [
    ("Manjaro", "x86_64"),
    ("Mint", "i386"), ("Mint", "x86_64"),
    ("elementary OS", "x86_64"),
    ("MX Linux", "i686"), ("MX Linux", "x86_64"),
    ("Ubuntu LTS", "armhf"), ("Ubuntu LTS", "i686"), ("Ubuntu LTS", "powerpc"), ("Ubuntu LTS", "ppc64el"), ("Ubuntu LTS", "s390x"), ("Ubuntu LTS", "x86_64"),
    ("Ubuntu", "armhf"), ("Ubuntu", "i686"), ("Ubuntu", "powerpc"), ("Ubuntu", "ppc64el"), ("Ubuntu", "s390x"), ("Ubuntu", "x86_64"),
    ("Debian Stable", "arm64"), ("Debian Stable", "armel"), ("Debian Stable", "armhf"), ("Debian Stable", "i686"), ("Debian Stable", "mips"), ("Debian Stable", "mipsel"), ("Debian Stable", "ppc64el"), ("Debian Stable", "s390x"), ("Debian Stable", "x86_64"),
    ("Debian Testing", "arm64"), ("Debian Testing", "armel"), ("Debian Testing", "armhf"), ("Debian Testing", "i686"), ("Debian Testing", "mips"), ("Debian Testing", "mipsel"), ("Debian Testing", "ppc64el"), ("Debian Testing", "s390x"), ("Debian Testing", "x86_64"),
    ("Debian Unstable", "arm64"), ("Debian Unstable", "armel"), ("Debian Unstable", "armhf"), ("Debian Unstable", "i686"), ("Debian Unstable", "mips"), ("Debian Unstable", "mipsel"), ("Debian Unstable", "ppc64el"), ("Debian Unstable", "s390x"), ("Debian Unstable", "x86_64"),
    ("Fedora", "aarch64"), ("Fedora", "armhfp"), ("Fedora", "i686"), ("Fedora", "x86_64"),
    ("openSUSE Leap", "arm64"), ("openSUSE Leap", "armhf"), ("openSUSE Leap", "i686"), ("openSUSE Leap", "ppc64"), ("openSUSE Leap", "ppc64el"), ("openSUSE Leap", "s390x"), ("openSUSE Leap", "x86_64"),
    ("openSUSE Tumbleweed", "arm64"), ("openSUSE Tumbleweed", "armhf"), ("openSUSE Tumbleweed", "i686"), ("openSUSE Tumbleweed", "ppc64"), ("openSUSE Tumbleweed", "ppc64el"), ("openSUSE Tumbleweed", "s390x"), ("openSUSE Tumbleweed", "x86_64"),
    ("Solus", "x86_64"),
    ("Arch", "arm"), ("Arch", "x86_64"),
    ("CentOS", "i386"), ("CentOS", "x86_64"),
    ("Red Hat Enterprise Linux", "arm64"), ("Red Hat Enterprise Linux", "i386"), ("Red Hat Enterprise Linux", "ia64"), ("Red Hat Enterprise Linux", "IBM Z"), ("Red Hat Enterprise Linux", "ppc"), ("Red Hat Enterprise Linux", "ppc64el"), ("Red Hat Enterprise Linux", "s390"), ("Red Hat Enterprise Linux", "s390x"), ("Red Hat Enterprise Linux", "x86_64")   
]

distro_desktop = [
    ("Manjaro", "Cinnamon"), ("Manjaro", "GNOME"), ("Manjaro", "KDE"), ("Manjaro", "MATE"), ("Manjaro", "LXQt"), ("Manjaro", "Xfce"),
    ("Mint", "Cinnamon"), ("Mint", "MATE"), ("Mint", "Xfce"),
    ("elementary OS", "Pantheon"),
    ("MX Linux", "Xfce"),
    ("Ubuntu LTS", "GNOME"),
    ("Ubuntu", "GNOME"),
    ("Debian Stable", "Cinnamon"), ("Debian Stable", "GNOME"), ("Debian Stable", "KDE"), ("Debian Stable", "MATE"), ("Debian Stable", "LXQt"), ("Debian Stable", "Xfce"),
    ("Debian Testing", "Cinnamon"), ("Debian Testing", "GNOME"), ("Debian Testing", "KDE"), ("Debian Testing", "MATE"), ("Debian Testing", "LXQt"), ("Debian Testing", "Xfce"),
    ("Debian Unstable", "Cinnamon"), ("Debian Unstable", "GNOME"), ("Debian Unstable", "KDE"), ("Debian Unstable", "MATE"), ("Debian Unstable", "LXQt"), ("Debian Unstable", "Xfce"),
    ("Fedora", "Cinnamon"), ("Fedora", "GNOME"), ("Fedora", "KDE"), ("Fedora", "MATE"), ("Fedora", "LXQt"), ("Fedora", "Xfce"),
    ("openSUSE Leap", "Cinnamon"), ("openSUSE Leap", "GNOME"), ("openSUSE Leap", "KDE"), ("openSUSE Leap", "MATE"), ("openSUSE Leap", "LXQt"), ("openSUSE Leap", "Xfce"),
    ("openSUSE Tumbleweed", "Cinnamon"), ("openSUSE Tumbleweed", "GNOME"), ("openSUSE Tumbleweed", "KDE"), ("openSUSE Tumbleweed", "MATE"), ("openSUSE Tumbleweed", "LXQt"), ("openSUSE Tumbleweed", "Xfce"),
    ("Solus", "GNOME"), ("Solus", "MATE"),
    ("Arch", "Cinnamon"), ("Arch", "GNOME"), ("Arch", "KDE"), ("Arch", "MATE"), ("Arch", "Xfce"),
    ("CentOS", "GNOME"), ("CentOS", "KDE"), 
    ("Red Hat Enterprise Linux", "GNOME"), ("Red Hat Enterprise Linux", "KDE")
]

desktops = [
        ("Cinnamon", "Nemo", "Xreader", "Xviewer", None),
        ("GNOME", "Nautilus", "Evince", "Eye of GNOME", "GNOME Terminal"),
        ("KDE", "Dolphin", "Okular", "Gwenview", "Konsole"),
        ("MATE", "Caja", "Atril", "eom", "mate-terminal"),
        ("LXQt", "PCManFM", None, "lximage-qt", "qterminal"),
        ("Pantheon", "Pantheon Files", "Pantheon Reader", "Pantheon Photos", "Pantheon Terminal"),
        ("Xfce", "Thunar", None, "Ristretto", "Xfce Terminal")
]

maintainters = [
        ("community", "non-profit", "international", None),
        ("Manjaro Team", "non-profit", "international", None),
        ("Mint Team", "non-profit", "Ireland", None),
        ("elementary OS Team", "non-profit", "USA", None),
        ("Solus devs", "non-profit", "Ireland", None),
        ("Canonical", "company", "Isle of Man", 125970000),
        ("Red Hat", "company", "USA", 2900000000),
        ("SUSE", "company", "Germany", 303400000)
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
#sql_insert_query = """ INSERT INTO usuarios (id, nome, sobrenome, genero, idade, pais, usoProfissional) 
#                       VALUES (%s,%s,%s,%s) """

# USUARIO
id = 0
ages_normal = get_truncated_normal(mean=35, sd=20, low=MIN_AGE, upp=MAX_AGE)
countries = list(dict(countries_for_language('en')).values())
for num_insertions in range(TOTAL_INSERT_AMOUNT):
    names = generate_names(INSERT_BUFFER_SIZE)
    ages = ages_normal.rvs(INSERT_BUFFER_SIZE)
    insert_params = []
    
    
    for buffer in range(INSERT_BUFFER_SIZE):
        line_tuple = (id,
                      names[buffer].split(' ')[0],
                      names[buffer].split(' ')[1],
                      generos[random.randint(0,len(generos) - 1)],
                      int(ages[buffer]),
                      countries[random.randint(0,len(countries) - 1)],
                      random.choice([True, False]))
        insert_params.append(line_tuple)
        id += 1
    print(insert_params)

# DISTRO
for it in distros:
    print(it)

# USUARIO-DISTRO
for num_insertions in range(TOTAL_INSERT_AMOUNT):
    insert_params = []
    for buffer in range(INSERT_BUFFER_SIZE):
        line_tuple = (random.randint(0, id), random.choice(distros)[0])
        insert_params.append(line_tuple)
    print(insert_params)

# DESKTOP
for it in desktops:
    print(it)

# MAINTAINER
for it in maintainters:
    print(it)

# DISTRO-ARCH

for it in distro_arch:
    print(it)

# DISTRO-DESKTOP
for it in distro_desktop:
    print(it)