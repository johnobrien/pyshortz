'''
Created on Jun 30, 2015

I'm thinking evenutally we'll start reusing our lists,
and the functions we're using to create lists of things.

So, I figure, let's start sticking them all in a "lists" module.

@author: Leiran Biton, John O'Brien
'''

from solver.word import strip_accents
import requests
import re


def get_companies():
    page = requests.get('https://www.sec.gov/rules/other/4-460list.htm')
    content = strip_accents(str(page.text))
    companies = re.findall(r'<TD>(.*?)\n</TD>', content)
    for company in companies:
        yield company.lower()


def get_musicians():
    urls = ['https://en.wikipedia.org/wiki/Category:American_pop_singers',
            'https://en.wikipedia.org/w/index.php?title=Category:American_pop_singers&pagefrom=Edner%2C+Bobby%0ABobby+Edner#mw-pages',
            'https://en.wikipedia.org/w/index.php?title=Category:American_pop_singers&pagefrom=Lamond%2C+George%0AGeorge+Lamond#mw-pages',
            'https://en.wikipedia.org/w/index.php?title=Category:American_pop_singers&pagefrom=Ponce+Sisters%2C+The%0AThe+Ponce+Sisters#mw-pages',
            'https://en.wikipedia.org/w/index.php?title=Category:American_pop_singers&pagefrom=Wallace%2C+Chris%0AChris+Wallace+%28musician%29#mw-pages']

    for url in urls:
        page = requests.get(url)
        content = strip_accents(str(page.text))
        musicians = re.findall(r'">(.*?)</a>', content)
        for musician in musicians:
            yield musician.lower()


def get_animals():
    wild = ['Aardwolf'
        ,'Admiral'
        ,'Adouri '
        ,'crake'
        ,'buffalo'
        ,'squirrel'
        ,'otter'
        ,'darter'
        ,'elephant'
        ,'fish eagle'
        ,'squirrel '
        ,'jacana'
        ,'lion'
        ,'lynx'
        ,'wagtail'
        ,'polecat'
        ,'porcupine'
        ,'bulbul'
        ,'skink'
        ,'snake '
        ,'wild cat'
        ,'wild dog'
        ,'lizard '
        ,'wallaby'
        ,'Agouti'
        ,'Albatross'
        ,'Alligator'
        ,'Alpaca'
        ,'parrot '
        ,'opossum'
        ,'alligator'
        ,'badger'
        ,'beaver'
        ,'bighorn sheep'
        ,'bison'
        ,' bear'
        ,'buffalo'
        ,'crow'
        ,'marten'
        ,'racer'
        ,'woodcock'
        ,'Anaconda '
        ,'goose'
        ,'Ant '
        ,'Anteater'
        ,'Antechinus'
        ,'Antelope'
        ,'spiny rat'
        ,'fox'
        ,'hare'
        ,'lemming'
        ,'tern'
        ,'Argalis'
        ,'Armadillo'
        ,'elephant'
        ,'vampire bat'
        ,'tortoise'
        ,'lion'
        ,'openbill'
        ,'red fox'
        ,'water buffalo'
        ,'water dragon'
        ,'jackal'
        ,'wild ass'
        ,'Ass'
        ,'turkey'
        ,'magpie'
        ,'masked owl'
        ,'pelican'
        ,'sea lion'
        ,'anteater'
        ,'Avocet'
        ,'Baboon'
        ,'Badger'
        ,'pintail'
        ,'Bald eagle'
        ,'Baleen whale'
        ,'mongoose'
        ,'Bandicoot'
        ,'deer'
        ,'Barbet'
        ,'bird'
        ,'gecko'
        ,'goldeneye'
        ,'Bat'
        ,'fox'
        ,'eagle'
        ,'Bear'
        ,'Beaver'
        ,'Bee-eater'
        ,'Bee-eater'
        ,'oryx'
        ,'Bengal vulture'
        ,'wallaby'
        ,'Bent-toed gecko'
        ,'Bettong'
        ,'Bird '
        ,'Bird'
        ,'Bison'
        ,'colobus'
        ,'bear'
        ,'curlew'
        ,'kite'
        ,'rhinoceros'
        ,'spider monkey'
        ,'swan'
        ,'vulture'
        ,'jackal'
        ,'magpie'
        ,'capuchin'
        ,'Black-capped chickadee'
        ,'waxbill'
        ,'barbet'
        ,'crane'
        ,'Black-crowned night heron'
        ,'Black-eyed bulbul'
        ,'Black-faced kangaroo'
        ,'Black-footed ferret'
        ,'Black-fronted bulbul'
        ,'Black-necked stork'
        ,'Black-tailed deer'
        ,'Black-tailed prairie dog'
        ,'Black-tailed tree creeper'
        ,'Black-throated butcher bird'
        ,'Black-throated cardinal'
        ,'Black-winged stilt'
        ,'Blackbird'
        ,'Blackbuck'
        ,'Blackish oystercatcher'
        ,'Blacksmith plover'
        ,'Bleeding heart monkey'
        ,'Blesbok'
        ,'Bleu'
        ,'Blue and gold macaw'
        ,'Blue and yellow macaw'
        ,'Blue catfish'
        ,'Blue crane'
        ,'Blue duck'
        ,'Blue fox'
        ,'Blue peacock'
        ,'Blue racer'
        ,'Blue shark'
        ,'Blue waxbill'
        ,'Blue wildebeest'
        ,'Blue-breasted cordon bleu'
        ,'Blue-faced booby'
        ,'Blue-footed booby'
        ,'Blue-tongued lizard'
        ,'Blue-tongued skink'
        ,'Boa'
        ,'Boar'
        ,'Boat-billed heron'
        ,'Bobcat'
        ,'Bohor reedbuck'
        ,'Bonnet macaque'
        ,'Bontebok'
        ,'Booby'
        ,'Bottle-nose dolphin'
        ,'Boubou'
        ,'Brazilian otter'
        ,'Brazilian tapir'
        ,'Brindled gnu'
        ,'Brocket'
        ,'Brolga crane'
        ,'marshbird'
        ,'antechinus'
        ,'brocket'
        ,'capuchin'
        ,'hyena'
        ,'lemur'
        ,'pelican'
        ,'Brush-tailed bettong'
        ,'Brush-tailed phascogale'
        ,'Brush-tailed rat kangaroo'
        ,'Buffalo'
        ,'Bulbul'
        ,'Bunting'
        ,'Burmese  mountain tortoise'
        ,'Burmese mountain tortoise'
        ,'Burrowing owl'
        ,'Bush dog'
        ,'Bushbaby'
        ,'Bushbuck'
        ,'Bushpig'
        ,'Bustard'
        ,'Butterfly '
        ,'Butterfly'
        ,'Buttermilk snake'
        ,'Caiman'
        ,'California sea lion'
        ,'Camel'
        ,'Campo flicker'
        ,'Canada goose'
        ,'Canadian river otter'
        ,'Canadian tiger swallowtail butterfly'
        ,'Cape Barren goose'
        ,'Cape clawless otter'
        ,'Cape cobra'
        ,'Cape fox'
        ,'Cape raven'
        ,'Cape starling'
        ,'Cape white-eye'
        ,'Cape wild cat'
        ,'Capuchin'
        ,'Capybara'
        ,'Caracal'
        ,'Caracara '
        ,'Caracara'
        ,'Cardinal'
        ,'Caribou'
        ,'Carmine bee-eater'
        ,'Carpet python'
        ,'Carpet snake'
        ,'Cat'
        ,'Catfish'
        ,'Cattle egret'
        ,'Cereopsis goose'
        ,'Chacma baboon'
        ,'Chameleon '
        ,'Cheetah'
        ,'Chestnut weaver'
        ,'Chickadee'
        ,'Chilean flamingo'
        ,'Chimpanzee'
        ,'Chipmunk'
        ,'Chital'
        ,'Chuckwalla'
        ,'Civet '
        ,'Civet cat'
        ,'Civet'
        ,'Cliffchat'
        ,'Coatimundi'
        ,'Cobra '
        ,'Cobra'
        ,'Cockatoo'
        ,'Collared lemming'
        ,'Collared lizard'
        ,'Collared peccary'
        ,'Colobus'
        ,'Columbian rainbow boa'
        ,'Comb duck'
        ,'Common boubou shrike'
        ,'Common brushtail possum'
        ,'Common dolphin'
        ,'Common duiker'
        ,'Common eland'
        ,'Common genet'
        ,'Common goldeneye'
        ,'Common green iguana'
        ,'Common grenadier'
        ,'Common langur'
        ,'Common long-nosed armadillo'
        ,'Common melba finch'
        ,'Common mynah'
        ,'Common nighthawk'
        ,'Common palm civet'
        ,'Common pheasant'
        ,'Common raccoon'
        ,'Common rhea'
        ,'Common ringtail'
        ,'Common seal'
        ,'Common shelduck'
        ,'Common turkey'
        ,'Common wallaroo'
        ,'Common waterbuck'
        ,'Common wolf'
        ,'Common wombat'
        ,'Common zebra'
        ,'Common zorro'
        ,'Constrictor'
        ,'Coot'
        ,'Coqui francolin'
        ,'Coqui partridge'
        ,'Corella'
        ,'Cormorant '
        ,'Cormorant'
        ,'Cottonmouth'
        ,'Cougar'
        ,'Cow'
        ,'Coyote'
        ,'Crab '
        ,'Crab'
        ,'Crab-eating fox'
        ,'Crab-eating raccoon'
        ,'Crake'
        ,'Crane'
        ,'Creeper'
        ,'Crested barbet'
        ,'Crested bunting'
        ,'Crested porcupine'
        ,'Crested screamer'
        ,'Crimson-breasted shrike'
        ,'Crocodile'
        ,'Crow'
        ,'Crown of thorns starfish'
        ,'Crowned eagle'
        ,'Crowned hawk-eagle'
        ,'Cuis'
        ,'Curlew'
        ,'Currasow '
        ,'Curve-billed thrasher'
        ,'Dabchick'
        ,'Dama wallaby'
        ,'Dark-winged trumpeter'
        ,'Darter'
        ,'Darwin ground finch '
        ,'Dassie'
        ,'Deer'
        ,'Defassa waterbuck'
        ,'Desert kangaroo rat'
        ,'Desert spiny lizard'
        ,'Desert tortoise'
        ,'Devil'
        ,'Dik'
        ,'Dingo'
        ,'Dog'
        ,'Dolphin'
        ,'Dove'
        ,'Downy woodpecker'
        ,'Dragon'
        ,'Dragonfly'
        ,'Dromedary camel'
        ,'Drongo'
        ,'Duck'
        ,'Duiker'
        ,'Dunnart'
        ,'Dusky gull'
        ,'Dusky rattlesnake'
        ,'Eagle owl '
        ,'Eagle'
        ,'boa constrictor'
        ,'box turtle'
        ,'cottontail rabbit'
        ,'diamondback rattlesnake'
        ,'dwarf mongoose'
        ,'fox squirrel'
        ,'grey kangaroo'
        ,'indigo snake'
        ,'quoll'
        ,'white pelican'
        ,'Echidna'
        ,'Egret'
        ,'Egyptian cobra'
        ,'Egyptian goose'
        ,'Egyptian viper'
        ,'Egyptian vulture'
        ,'Eland'
        ,'Elegant crested tinamou'
        ,'Elephant'
        ,'Eleven-banded armadillo '
        ,'Elk'
        ,'Emerald green tree boa'
        ,'Emerald-spotted wood dove'
        ,'Emu'
        ,'Eurasian badger'
        ,'Eurasian beaver'
        ,'Eurasian hoopoe'
        ,'Eurasian red squirrel'
        ,'Euro wallaby'
        ,'badger'
        ,'beaver'
        ,'red squirrel'
        ,'shelduck'
        ,'spoonbill'
        ,'stork'
        ,'wild cat'
        ,'Fairy penguin'
        ,'Falcon'
        ,'Fat-tailed dunnart'
        ,'Feathertail glider'
        ,'Feral rock pigeon'
        ,'Ferret'
        ,'Ferruginous hawk'
        ,'Field flicker'
        ,'Finch'
        ,'Fisher'
        ,'Flamingo'
        ,'Flicker'
        ,'Flightless cormorant'
        ,'Flycatcher'
        ,'Flying fox '
        ,'Fork-tailed drongo'
        ,'Four-horned antelope'
        ,'Four-spotted skimmer'
        ,'Four-striped grass mouse'
        ,'Fowl'
        ,'Fox'
        ,'Francolin'
        ,'Frilled dragon'
        ,'Frilled lizard'
        ,'Fringe-eared oryx'
        ,'Frog '
        ,'Frogmouth'
        ,'Galah'
        ,'Galapagos albatross'
        ,'Galapagos dove'
        ,'Galapagos hawk'
        ,'Galapagos mockingbird'
        ,'Galapagos penguin'
        ,'Galapagos sea lion'
        ,'Galapagos tortoise'
        ,'quail'
        ,'Gaur'
        ,'Gazelle'
        ,'Gazer'
        ,'Gecko '
        ,'Gecko'
        ,'Gelada baboon'
        ,'Gemsbok'
        ,'Genet'
        ,'Genoveva'
        ,'Gerbil '
        ,'Gerenuk'
        ,'Giant anteater'
        ,'Giant armadillo'
        ,'Giant girdled lizard'
        ,'Giant heron'
        ,'Giant otter'
        ,'Gila monster'
        ,'Giraffe'
        ,'Glider'
        ,'Glossy ibis'
        ,'Glossy starling '
        ,'Gnu'
        ,'Goanna lizard'
        ,'Goat'
        ,'Godwit'
        ,'Golden brush-tailed possum'
        ,'Golden eagle'
        ,'Golden jackal'
        ,'Golden-mantled ground squirrel'
        ,'Goldeneye'
        ,'Goliath heron'
        ,'Gonolek'
        ,'Goose'
        ,'Gorilla'
        ,'gazelle'
        ,'dugong'
        ,'Gray duiker'
        ,'Gray heron'
        ,'Gray langur'
        ,'Gray rhea'
        ,'Great cormorant'
        ,'Great egret'
        ,'Great horned owl'
        ,'Great kiskadee'
        ,'Great skua'
        ,'Great white pelican'
        ,'Greater adjutant stork'
        ,'Greater blue-eared starling'
        ,'Greater flamingo'
        ,'Greater kudu'
        ,'Greater rhea'
        ,'Greater roadrunner'
        ,'Greater sage grouse'
        ,'Grebe'
        ,'Green heron'
        ,'Green vine snake'
        ,'Green-backed heron'
        ,'Green-winged macaw'
        ,'Green-winged trumpeter'
        ,'Grenadier'
        ,'Grey fox'
        ,'Grey heron'
        ,'Grey lourie'
        ,'Grey mouse lemur'
        ,'Grey phalarope'
        ,'Grey-footed squirrel'
        ,'Greylag goose'
        ,'Griffon vulture'
        ,'Grison'
        ,'Grizzly bear'
        ,'Ground legaan'
        ,'Ground monitor '
        ,'Groundhog'
        ,'Grouse'
        ,'Guanaco'
        ,'Guerza'
        ,'Gull'
        ,'Gulls '
        ,'Hanuman langur'
        ,'Harbor seal'
        ,'Hare'
        ,'Hartebeest'
        ,'Hawk'
        ,'Hawk-eagle'
        ,'Hawk-headed parrot'
        ,'Hedgehog'
        ,'Helmeted guinea fowl'
        ,'Hen'
        ,'Heron'
        ,'Herring gull'
        ,'Hippopotamus'
        ,'Hoary marmot'
        ,'Honey badger'
        ,'Hoopoe'
        ,'Hornbill'
        ,'Horned lark'
        ,'Horned puffin'
        ,'Horned rattlesnake'
        ,'Hottentot teal'
        ,'House crow'
        ,'House sparrow'
        ,'Hudsonian godwit'
        ,'Hummingbird '
        ,'Huron'
        ,'Hyena'
        ,'Hyrax'
        ,'Ibex'
        ,'Ibis'
        ,'Iguana'
        ,'Impala'
        ,'Indian giant squirrel'
        ,'Indian jackal'
        ,'Indian leopard'
        ,'Indian mynah'
        ,'Indian peacock'
        ,'Indian porcupine'
        ,'Indian red admiral'
        ,'Indian star tortoise'
        ,'Indian tree pie'
        ,'Insect'
        ,'Jabiru stork'
        ,'Jacana'
        ,'Jackal'
        ,'Jackrabbit'
        ,'Jaeger'
        ,'Jaguar'
        ,'Jaguarundi'
        ,'Japanese macaque'
        ,'Javan gold-spotted mongoose'
        ,'Javanese cormorant'
        ,'Jungle cat'
        ,'Jungle kangaroo'
        ,'Kaffir cat'
        ,'Kafue flats lechwe'
        ,'Kalahari scrub robin'
        ,'Kangaroo'
        ,'Kelp gull'
        ,'Killer whale'
        ,'King cormorant'
        ,'King vulture'
        ,'Kingfisher'
        ,'Kinkajou'
        ,'Kiskadee'
        ,'Kite'
        ,'Klipspringer'
        ,'Knob-nosed goose'
        ,'Koala'
        ,'Komodo dragon'
        ,'Kongoni'
        ,'Kookaburra'
        ,'Kori bustard'
        ,'Kudu'
        ,'Land iguana'
        ,'Langur'
        ,'Lappet-faced vulture'
        ,'Lapwing '
        ,'Lapwing'
        ,'Large cormorant'
        ,'Large-eared bushbaby'
        ,'Lark'
        ,'Laughing dove'
        ,'Laughing kookaburra'
        ,'Lava gull'
        ,'Least chipmunk'
        ,'Lechwe'
        ,'Legaan'
        ,'Lemming'
        ,'Lemur'
        ,'Leopard'
        ,'Lesser double-collared sunbird'
        ,'Lesser flamingo'
        ,'Lesser masked weaver'
        ,'Lesser mouse lemur'
        ,'Lilac-breasted roller'
        ,'Lily trotter'
        ,'Lion'
        ,'Little blue penguin'
        ,'Little bat'
        ,'Little dove'
        ,'Little cormorant'
        ,'Little grebe'
        ,'Little heron'
        ,'Lizard '
        ,'Lizard'
        ,'Llama'
        ,'Long-billed cockatoo'
        ,'Long-billed corella'
        ,'Long-crested hawk eagle'
        ,'Long-finned pilot whale'
        ,'Long-necked turtle'
        ,'Long-nosed bandicoot'
        ,'Long-tailed jaeger'
        ,'Long-tailed skua'
        ,'Long-tailed spotted cat'
        ,'Lorikeet'
        ,'Loris'
        ,'Lory'
        ,'Lourie'
        ,'Lynx'
        ,'Macaque'
        ,'Macaw'
        ,'Madagascar fruit bat'
        ,'Madagascar hawk owl'
        ,'Magellanic penguin'
        ,'Magistrate  colobus'
        ,'Magnificent frigate bird'
        ,'Magpie'
        ,'Malabar squirrel'
        ,'Malachite kingfisher'
        ,'Malagasy ground boa'
        ,'Malay squirrel '
        ,'Mallard'
        ,'Malleefowl'
        ,'Manatee'
        ,'Mandras tree shrew'
        ,'Mara'
        ,'Marabou stork'
        ,'Margay'
        ,'Marine iguana'
        ,'Marmot'
        ,'Marshbird'
        ,'Marten'
        ,'Masked booby'
        ,'Meerkat'
        ,'Mexican beaded lizard'
        ,'Mexican boa'
        ,'Mexican wolf'
        ,'Mississippi alligator'
        ,'Moccasin'
        ,'Mocking cliffchat'
        ,'Mockingbird'
        ,'Mongoose'
        ,'Monitor lizard '
        ,'Monitor'
        ,'Monkey'
        ,'Monster'
        ,'Moorhen'
        ,'Moose'
        ,'Mouflon'
        ,'Mountain duck'
        ,'Mountain goat'
        ,'Mountain lion'
        ,'Mourning collared dove'
        ,'Mouse'
        ,'Mudskipper '
        ,'Mule deer'
        ,'Musk ox'
        ,'Mynah'
        ,'Native cat'
        ,'Nelson ground squirrel'
        ,'Neotropic cormorant'
        ,'Netted rock dragon'
        ,'Nighthawk'
        ,'Nile crocodile'
        ,'Nilgai'
        ,'Nine-banded armadillo'
        ,'beaver'
        ,'porcupine'
        ,'red fox'
        ,'river otter'
        ,'elephant seal'
        ,'fur seal'
        ,'phalarope'
        ,'Nubian bee-eater'
        ,'Numbat'
        ,'Nutcracker'
        ,'Nuthatch'
        ,'Nyala'
        ,'Ocelot'
        ,'Old world fruit bat '
        ,'Olive baboon'
        ,'Onager'
        ,'Openbill stork'
        ,'Openbill'
        ,'Opossum'
        ,'Orca'
        ,'Oribi'
        ,'Oriental short-clawed otter'
        ,'Oriental white-backed vulture'
        ,'Ornate rock dragon'
        ,'Oryx'
        ,'Osprey'
        ,'Ostrich'
        ,'Otter'
        ,'Ovenbird'
        ,'Owl'
        ,'Ox'
        ,'Oystercatcher'
        ,'Paca'
        ,'Pacific gull'
        ,'Paddy heron '
        ,'Pademelon'
        ,'Painted stork'
        ,'Pale white-eye'
        ,'Pale-throated three-toed sloth'
        ,'Palm squirrel'
        ,'Pampa gray fox'
        ,'Paradoxure'
        ,'Parakeet'
        ,'Parrot'
        ,'Partridge'
        ,'Peacock'
        ,'Peccary'
        ,'Pelican'
        ,'Penguin'
        ,'Peregrine falcon'
        ,'Phalarope'
        ,'Phascogale'
        ,'Pheasant'
        ,'Pie'
        ,'Pied avocet'
        ,'Pied butcher bird'
        ,'Pied cormorant'
        ,'Pied crow'
        ,'Pied kingfisher'
        ,'Pig-tailed macaque'
        ,'Pigeon'
        ,'Pine siskin'
        ,'Pine snake '
        ,'Pine squirrel'
        ,'Pintail'
        ,'Plains zebra'
        ,'Platypus'
        ,'Plover'
        ,'Pocket gopher '
        ,'Polar bear'
        ,'Polecat'
        ,'Porcupine'
        ,'Possum'
        ,'Potoroo'
        ,'Prairie falcon'
        ,'Praying mantis '
        ,'Prehensile-tailed porcupine'
        ,'Pronghorn'
        ,'Puffin'
        ,'Puku'
        ,'Puma'
        ,'Puna ibis'
        ,'Purple grenadier'
        ,'Purple moorhen'
        ,'Pygmy possum'
        ,'Python '
        ,'Python'
        ,'Quail'
        ,'Quoll'
        ,'Rabbit'
        ,'Raccoon dog'
        ,'Raccoon'
        ,'Racer snake'
        ,'Racer'
        ,'Radiated tortoise'
        ,'Rainbow lory'
        ,'Rat'
        ,'Rattlesnake'
        ,'Raven'
        ,'Red and blue macaw'
        ,'Red brocket'
        ,'Red deer'
        ,'Red hartebeest'
        ,'Red howler monkey'
        ,'Red kangaroo'
        ,'Red lava crab'
        ,'Red meerkat'
        ,'Red phalarope'
        ,'Red sheep'
        ,'Red squirrel'
        ,'Red-billed buffalo weaver'
        ,'Red-billed hornbill'
        ,'Red-billed toucan'
        ,'Red-billed tropic bird'
        ,'Red-breasted cockatoo'
        ,'Red-breasted nuthatch'
        ,'Red-capped cardinal'
        ,'Red-cheeked cordon bleu'
        ,'Red-headed woodpecker'
        ,'Red-knobbed coot'
        ,'Red-legged pademelon'
        ,'Red-necked phalarope'
        ,'Red-necked wallaby'
        ,'Red-shouldered glossy starling'
        ,'Red-tailed cockatoo'
        ,'Red-tailed hawk'
        ,'Red-tailed phascogale'
        ,'Red-tailed wambenger'
        ,'Red-winged blackbird'
        ,'Red-winged hawk '
        ,'Reedbuck'
        ,'Reindeer'
        ,'Rhea'
        ,'Rhesus macaque'
        ,'Rhesus monkey'
        ,'Rhinoceros'
        ,'Ring dove'
        ,'Ring-necked pheasant'
        ,'Ring-tailed coatimundi'
        ,'Ring-tailed gecko'
        ,'Ring-tailed lemur'
        ,'Ring-tailed possum'
        ,'Ringtail'
        ,'Ringtail cat'
        ,'River wallaby'
        ,'Roadrunner'
        ,'Roan antelope'
        ,'Robin'
        ,'Rock dove'
        ,'Roe deer'
        ,'Roller'
        ,'Rose-ringed parakeet'
        ,'Roseat flamingo'
        ,'Roseate cockatoo'
        ,'Royal tern'
        ,'Rufous tree pie'
        ,'Rufous-collared sparrow'
        ,'Russian dragonfly'
        ,'Sable antelope'
        ,'Sacred ibis'
        ,'Saddle-billed stork'
        ,'Sage grouse'
        ,'Sage hen'
        ,'Sally lightfoot crab'
        ,'Salmon pink bird eater tarantula'
        ,'Salmon'
        ,'Sambar'
        ,'Sandgrouse'
        ,'Sandhill crane'
        ,'Sandpiper'
        ,'Sarus crane'
        ,'Savanna baboon'
        ,'Savanna fox'
        ,'Savannah deer'
        ,'Savannah deer '
        ,'Scaly-breasted lorikeet'
        ,'Scarlet macaw'
        ,'Scottish highland cow'
        ,'Screamer'
        ,'Sea birds '
        ,'Seal'
        ,'Secretary bird'
        ,'Serval'
        ,'Seven-banded armadillo'
        ,'Shark'
        ,'Sheathbill'
        ,'Sheep'
        ,'Shelduck'
        ,'Short-beaked echidna'
        ,'Short-nosed bandicoot'
        ,'Shrew'
        ,'Shrike'
        ,'Sidewinder'
        ,'Sifaka'
        ,'Silver gull'
        ,'Silver-backed fox'
        ,'Silver-backed jackal'
        ,'Siskin'
        ,'Skimmer'
        ,'Skink'
        ,'Skua'
        ,'Skunk'
        ,'Slender loris'
        ,'Slender-billed cockatoo'
        ,'Sloth bear'
        ,'Sloth'
        ,'Small Indian mongoose'
        ,'Small-clawed otter'
        ,'Small-spotted genet'
        ,'Small-toothed palm civet'
        ,'Snake '
        ,'Snake'
        ,'Snake-necked turtle'
        ,'Snow goose'
        ,'Snowy egret'
        ,'Snowy owl'
        ,'Snowy sheathbill'
        ,'Sociable weaver'
        ,'Sockeye salmon'
        ,'hedgehog'
        ,'meadowlark '
        ,'puma'
        ,'sea lion'
        ,'gull'
        ,'boubou'
        ,'bandicoot'
        ,'elephant seal'
        ,'ground hornbill'
        ,'hairy-nosed wombat'
        ,'lapwing'
        ,'right whale'
        ,'screamer'
        ,'sea lion'
        ,'tamandua'
        ,'white-crowned shrike'
        ,'Sparrow'
        ,'Spectacled caiman'
        ,'Spider'
        ,'Spoonbill'
        ,'Sportive lemur'
        ,'Spotted deer'
        ,'Spotted hyena'
        ,'Spotted wood sandpiper'
        ,'Spotted-tailed quoll'
        ,'Springbok'
        ,'Springbuck'
        ,'Springhare'
        ,'Spur-winged goose'
        ,'Spurfowl'
        ,'Square-lipped rhinoceros'
        ,'Squirrel glider'
        ,'Squirrel'
        ,'Stanley bustard'
        ,'Stanley crane'
        ,'Starfish'
        ,'Starling'
        ,'Steenbok'
        ,'Steenbuck'
        ,'Steller sea lion'
        ,'sea lion'
        ,'Stick insect'
        ,'Stilt'
        ,'Stone sheep'
        ,'Stork'
        ,'Striated heron'
        ,'Striped dolphin'
        ,'Striped hyena'
        ,'Striped skunk'
        ,'Sugar glider'
        ,'Sulfur-crested cockatoo'
        ,'Sun gazer'
        ,'Sunbird'
        ,'Sungazer'
        ,'Superb starling'
        ,'Suricate'
        ,'Swallow '
        ,'Swallow-tail gull'
        ,'Swamp deer'
        ,'Swan'
        ,'Tailless tenrec'
        ,'Tamandua'
        ,'Tammar wallaby'
        ,'Tapir'
        ,'Tarantula'
        ,'Tasmanian devil'
        ,'Tawny eagle'
        ,'Tawny frogmouth'
        ,'Tayra'
        ,'Teal'
        ,'Tenrec'
        ,'Tern'
        ,'Thirteen-lined squirrel'
        ,'Thrasher'
        ,'Three-banded plover'
        ,'Tiger'
        ,'Tiger cat'
        ,'Tiger snake'
        ,'Timber wolf'
        ,'Tinamou'
        ,'Toddy cat'
        ,'Tokay gecko'
        ,'Topi'
        ,'Tortoise'
        ,'Toucan'
        ,'Tree porcupine'
        ,'Tropical buckeye butterfly'
        ,'Trotter'
        ,'Trumpeter swan'
        ,'Trumpeter'
        ,'Tsessebe'
        ,'Turaco'
        ,'Turkey vulture'
        ,'Turkey'
        ,'Turtle '
        ,'Turtle'
        ,'Two-banded monitor'
        ,'Two-toed sloth'
        ,'Two-toed tree sloth'
        ,'Tyrant flycatcher'
        ,'Uinta ground squirrel'
        ,'Urial'
        ,'Vervet monkey'
        ,'Vicuna'
        ,'Vine snake '
        ,'Violet-crested turaco'
        ,'Violet-eared waxbill'
        ,'Viper'
        ,'Vulture'
        ,'Wagtail'
        ,'Wallaby'
        ,'Wallaroo'
        ,'Wambenger'
        ,'Wapiti'
        ,'Warthog'
        ,'Water legaan'
        ,'Water moccasin'
        ,'Water monitor'
        ,'Waterbuck'
        ,'Wattled crane'
        ,'Waved albatross'
        ,'Waxbill'
        ,'Weaver'
        ,'Weeper capuchin'
        ,'bearded dragon'
        ,'grey kangaroo'
        ,'lowland gorilla'
        ,'palm tanager '
        ,'patch-nosed snake'
        ,'pygmy possum'
        ,'spotted skunk'
        ,'Whale'
        ,'Whip-tailed wallaby'
        ,'White rhinoceros'
        ,'White spoonbill'
        ,'White stork'
        ,'White-bellied sea eagle'
        ,'White-browed owl'
        ,'White-browed sparrow weaver'
        ,'White-cheeked pintail'
        ,'White-eye'
        ,'White-faced tree rat'
        ,'White-faced whistling duck'
        ,'White-fronted bee-eater'
        ,'White-fronted capuchin'
        ,'White-headed vulture'
        ,'White-lipped peccary'
        ,'White-mantled colobus'
        ,'White-necked raven'
        ,'White-necked stork'
        ,'White-nosed coatimundi'
        ,'White-rumped vulture'
        ,'White-tailed deer'
        ,'White-tailed jackrabbit'
        ,'White-throated kingfisher'
        ,'White-throated monitor'
        ,'White-throated robin'
        ,'White-throated toucan'
        ,'White-winged  tern'
        ,'White-winged dove'
        ,'White-winged tern'
        ,'Wild boar'
        ,'Wild turkey'
        ,'Wild water buffalo'
        ,'Wildebeest'
        ,'Wolf spider'
        ,'Wolf'
        ,'Wombat'
        ,'Wood pigeon'
        ,'Woodchuck'
        ,'Woodcock'
        ,'Woodpecker'
        ,'Woodrat '
        ,'Woolly-necked stork'
        ,'Worm snake '
        ,'Woylie'
        ,'Yak'
        ,'Yellow baboon'
        ,'Yellow mongoose'
        ,'Yellow-bellied marmot'
        ,'Yellow-billed hornbill'
        ,'Yellow-billed stork'
        ,'Yellow-sungazer'
        ,'Yellow-crowned night heron'
        ,'Yellow-headed caracara'
        ,'Yellow-necked spurfowl'
        ,'Yellow-rumped siskin'
        ,'Yellow-throated sandgrouse'
        ,'Zebra'
        ,'Zorilla'
        ,'Zorro'
       ]
    domestic = ['sheep'
               ,'horse'
               ,'Pony'
               ,'yak'
               ,'cow'
               ,'guinea pig'
               ,'dog'
               ,'mule'
               ,'pig'
               ,'ferret'
               ,'rabbit'
               ,'llama'
               ,'cattle'
               ,'alpaca'
               ,'cat'
               ,'mouse'
               ,'goat'
               ,'donkey'
               ,'rat'
               ]
    return wild + domestic