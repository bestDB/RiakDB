# Importujemy modu�
import riak

# ��czymy si� z baz�, port 10018 jest standardowym 
# portem dev1 kt�ry zosta� utworzony w 
# krokach zwi�zanych z konfiguracj�
client = riak.RiakClient('127.0.0.1',10018)

# ��czymy si� z bucketem Customers
customerBucket = client.bucket('Customers')

# Tworzymy w buckecie nowy klucz 
zeus = customerBucket.new('007')

# Ustawiamy jemu wartosci
zeus.set_data({ 'CompanyName'  : 'Zeus', \ 
				'ContactName'  : '' , \
				'ContactTitle' : 'God' , \
				'Address' : 'Olimp' , \
				'City' : 'Athens' , \
				'Region' : 'GodMountain' , \
				'Phone' : '' , \
				'Fax' : '' })

# Wstawiamy do bazy
zeus.store()

# W momencie kiedy mamy obiekt odpowiedniego
# bucketu pobranie wartosci jest w miare proste...
olimpGod = customerBucket.get('007')

# Usuwanie jest rownie proste,z bucketu
# pobieramy wartosc, po czym na obiekcie
# wywolujemy funkcje delete i to wszystko
godToDelete = customerBucket.get('007')
godToDelete.delete()







