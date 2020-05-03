
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys
from botocore.vendored import requests


def main(params):
  return lambda_handler(None, {body: params})
    # text = getrequest()
    # return text


def getrequest():
    r = requests.get("https://www.example.com")
    return {"content": r.text}
    

import json
import time
import urllib
from datetime import date
from datetime import datetime
import random


TELE_TOKEN='CENSORED'
TELE_TOKEN2='CENSORED' #logchat
TELE_TOKEN3="CENSORED" #logchat2
URL = "https://api.telegram.org/bot{}/".format(TELE_TOKEN)
DICTKEY = 'CENSORED'
adminchatid = "CENSORED"
app_id = 'CENSORED'
app_key = 'CENSORED'
language = 'en-gb'
word_id = 'CENSORED'
fields = 'definitions'
strictMatch = 'false'

cursewords = ['2 girls 1 cup','2g1c','4r5e','5h1t','5hit','a$$','a$$hole','a_s_s','a2m','a54','a55','a55hole','acrotomophilia','aeolus','ahole','alabama hot pocket','alaskan pipeline','anal','anal impaler','anal leakage','analprobe','anilingus','anus','apeshit','ar5e','areola','areole','arian','arrse','arse','arsehole','aryan','ass','ass fuck','ass fuck','ass hole','assbag','assbandit','assbang','assbanged','assbanger','assbangs','assbite','assclown','asscock','asscracker','asses','assface','assfaces','assfuck','assfucker','ass-fucker','assfukka','assgoblin','assh0le','asshat','ass-hat','asshead','assho1e','asshole','assholes','asshopper','ass-jabber','assjacker','asslick','asslicker','assmaster','assmonkey','assmucus','assmucus','assmunch','assmuncher','assnigger','asspirate','ass-pirate','assshit','assshole','asssucker','asswad','asswhole','asswipe','asswipes','auto erotic','autoerotic','axwound','azazel','azz','b!tch','b00bs','b17ch','b1tch','babeland','baby batter','baby juice','ball gag','ball gravy','ball kicking','ball licking','ball sack','ball sucking','ballbag','balls','ballsack','bampot','bang (one\'s) box','bangbros','bareback','barely legal','barenaked','barf','bastard','bastardo','bastards','bastinado','batty boy','bawdy','bbw','bdsm','beaner','beaners','beardedclam','beastial','beastiality','beatch','beaver','beaver cleaver','beaver lips','beef curtain','beef curtain','beef curtains','beeyotch','bellend','bender','beotch','bescumber','bestial','bestiality','bi+ch','biatch','big black','big breasts','big knockers','big tits','bigtits','bimbo','bimbos','bint','birdlock','bitch','bitch tit','bitch tit','bitchass','bitched','bitcher','bitchers','bitches','bitchin','bitching','bitchtits','bitchy','black cock',
'blonde action','blonde on blonde action','bloodclaat','bloody','bloody hell','blow job','blow me','blow mud','blow your load','blowjob','blowjobs','blue waffle','blue waffle','blumpkin','blumpkin','bod','bodily','boink','boiolas','bollock','bollocks','bollok','bollox','bondage','boned','boner','boners','bong','boob','boobies','boobs','booby','booger','bookie','boong','booobs','boooobs','booooobs','booooooobs','bootee','bootie','booty','booty call','booze','boozer','boozy','bosom','bosomy','breasts','Breeder','brotherfucker','brown showers','brunette action','buceta','bugger','bukkake','bull shit','bulldyke','bullet vibe','bullshit','bullshits','bullshitted','bullturds','bum','bum boy','bumblefuck','bumclat','bummer','buncombe','bung','bung hole','bunghole','bunny fucker','bust a load','bust a load','busty','butt','butt fuck','butt fuck','butt plug','buttcheeks','buttfuck','buttfucka','buttfucker','butthole','buttmuch','buttmunch','butt-pirate','buttplug','c.0.c.k','c.o.c.k.','c.u.n.t','c0ck','c-0-c-k','c0cksucker','caca','cacafuego','cahone','camel toe','cameltoe','camgirl','camslut','camwhore','carpet muncher','carpetmuncher','cawk','cervix','chesticle','chi-chi man','chick with a dick','child-fucker','chinc','chincs','chink','chinky','choad','choade','choade','choc ice','chocolate rosebuds','chode','chodes','chota bags','chota bags','cipa','circlejerk','cl1t','cleveland steamer','climax','clit','clit licker','clit licker','clitface','clitfuck','clitoris','clitorus','clits','clitty','clitty litter','clitty litter','clover clamps','clunge','clusterfuck','cnut','cocain','cocaine','coccydynia','cock','c-o-c-k','cock pocket','cock pocket','cock snot','cock snot','cock sucker','cockass','cockbite','cockblock','cockburger','cockeye','cockface','cockfucker'
,'cockhead','cockholster','cockjockey','cockknocker','cockknoker','Cocklump','cockmaster','cockmongler','cockmongruel','cockmonkey','cockmunch','cockmuncher','cocknose','cocknugget','cocks','cockshit','cocksmith','cocksmoke','cocksmoker','cocksniffer','cocksuck','cocksuck','cocksucked','cocksucked','cocksucker','cock-sucker','cocksuckers','cocksucking','cocksucks','cocksucks','cocksuka','cocksukka','cockwaffle','coffin dodger','coital','cok','cokmuncher','coksucka','commie','condom','coochie','coochy','coon','coonnass','coons','cooter','cop some wood','cop some wood','coprolagnia','coprophilia','corksucker','cornhole','cornhole','corp whore','corp whore','corpulent','cox','crabs','crack','cracker','crackwhore','crap','crappy','creampie','cretin','crikey','cripple','crotte','cum','cum chugger','cum chugger','cum dumpster','cum dumpster','cum freak','cum freak','cum guzzler','cum guzzler','cumbubble','cumdump','cumdump','cumdumpster','cumguzzler','cumjockey','cummer','cummin','cumming','cums','cumshot','cumshots','cumslut','cumstain','cumtart','cunilingus','cunillingus','cunnie','cunnilingus','cunny','cunt','c-u-n-t','cunt hair','cunt hair','cuntass','cuntbag','cuntbag','cuntface','cunthole','cunthunter','cuntlick','cuntlick','cuntlicker','cuntlicker','cuntlicking','cuntlicking','cuntrag','cunts','cuntsicle','cuntsicle','cuntslut','cunt-struck','cunt-struck','cus','cut rope','cut rope','cyalis','cyberfuc','cyberfuck','cyberfuck','cyberfucked','cyberfucked','cyberfucker','cyberfuckers','cyberfucking','cyberfucking','d0ng','d0uch3','d0uche','d1ck','d1ld0','d1ldo','dago','dagos','dammit','damn','damned','damnit','darkie','darn','date rape','daterape','dawgie-style','deep throat','deepthroat','deggo','dendrophilia','dick','dick head','dick hole','dick hole','dick shy','dick shy','dickbag','dickbeaters','dickdipper','dickface','dickflipper','dickfuck','dickfucker','dickhead','dickheads','dickhole','dickish','dick-ish','dickjuice','dickmilk','dickmonger','dickripper','dicks','dicksipper','dickslap','dick-sneeze','dicksucker','dicksucking','dicktickler','dickwad','dickweasel','dickweed','dickwhipper','dickwod','dickzipper','diddle','dike','dildo','dildos','diligaf','dillweed','dimwit','dingle','dingleberries','dingleberry','dink','dinks','dipship','dipshit','dirsa','dirty','dirty pillows','dirty sanchez','dirty Sanchez','div','dlck','dog style','dog-fucker','doggie style','doggiestyle','doggie-style','doggin','dogging','doggy style','doggystyle','doggy-style','dolcett','domination','dominatrix','dommes','dong','donkey punch','donkeypunch','donkeyribber','doochbag','doofus','dookie','doosh','dopey','double dong','double penetration','Doublelift','douch3','douche','douchebag','douchebags','douche-fag','douchewaffle','douchey','dp action','drunk','dry hump','duche','dumass','dumb ass','dumbass','dumbasses','Dumbcunt','dumbfuck','dumbshit','dummy','dumshit','dvda','dyke','dykes','eat a dick','eat a dick','eat hair pie','eat hair pie','eat my ass','ecchi','ejaculate','ejaculated','ejaculates','ejaculates','ejaculating','ejaculating','ejaculatings','ejaculation','ejakulate','erect','erection','erotic','erotism','escort','essohbee','eunuch','extacy','extasy','f u c k','f u c k e r','f.u.c.k','f_u_c_k','f4nny','facial','fack','fag','fagbag','fagfucker','fagg','fagged','fagging','faggit','faggitt','faggot','faggotcock','faggots','faggs','fagot','fagots','fags','fagtard','faig','faigt','fanny','fannybandit','fannyflaps','fannyfucker','fanyy','fart','fartknocker','fatass','fcuk','fcuker','fcuking','fecal','feck','fecker','feist','felch','felcher','felching','fellate','fellatio','feltch','feltcher','female squirting','femdom','fenian','fice','figging','fingerbang','fingerfuck','fingerfuck','fingerfucked','fingerfucked','fingerfucker','fingerfucker','fingerfuckers','fingerfucking','fingerfucking','fingerfucks','fingerfucks','fingering','fist fuck','fist fuck','fisted','fistfuck','fistfucked','fistfucked','fistfucker','fistfucker','fistfuckers','fistfuckers','fistfucking','fistfucking','fistfuckings','fistfuckings','fistfucks','fistfucks','fisting','fisty','flamer','flange','flaps','fleshflute','flog the log','flog the log','floozy','foad','foah','fondle','foobar','fook','fooker','foot fetish','footjob','foreskin','freex','frenchify','frigg','frigga','frotting','fubar','fuc','fuck','fuck','f-u-c-k','fuck buttons','fuck hole','fuck hole','Fuck off','fuck puppet'
,'fuck puppet','fuck trophy','fuck trophy','fuck yo mama','fuck yo mama','fuck you','fucka','fuckass','fuck-ass','fuck-ass','fuckbag','fuck-bitch','fuck-bitch','fuckboy','fuckbrain','fuckbutt','fuckbutter','fucked','fuckedup','fucker','fuckers','fuckersucker','fuckface','fuckhead','fuckheads','fuckhole','fuckin','fucking','fuckings','fuckingshitmotherfucker','fuckme','fuckme','fuckmeat','fuckmeat','fucknugget','fucknut','fucknutt','fuckoff','fucks','fuckstick','fucktard','fuck-tard','fucktards','fucktart','fucktoy','fucktoy','fucktwat','fuckup','fuckwad','fuckwhit','fuckwit','fuckwitt','fudge packer','fudgepacker','fudge-packer','fuk','fuker','fukker','fukkers','fukkin','fuks','fukwhit','fukwit','fuq','futanari','fux','fux0r','fvck','fxck','gae','gai','gang bang','gangbang','gang-bang','gang-bang','gangbanged','gangbangs','ganja','gash','gassy ass','gassy ass','gay','gay sex','gayass','gaybob','gaydo','gayfuck','gayfuckist','gaylord','gays','gaysex','gaytard','gaywad','gender bender','genitals','gey','gfy','ghay','ghey','giant cock','gigolo','ginger','gippo','girl on','girl on top','girls gone wild','git','glans','goatcx','goatse','god','god damn','godamn','godamnit','goddam','god-dam','goddammit','goddamn','goddamned','god-damned','goddamnit','godsdamn','gokkun','golden shower','goldenshower','golliwog','gonad','gonads','goo girl','gooch','goodpoop','gook','gooks','goregasm','gringo','grope','group sex','gspot','g-spot','gtfo','guido','guro','h0m0','h0mo','ham flap','ham flap','hand job','handjob','hard core','hard on','hardcore','hardcoresex','he11','hebe','heeb','hell','hemp','hentai','heroin','herp','herpes','herpy','heshe','he-she','hircismus','hitler','hiv','ho','hoar','hoare','hobag','hoe','hoer','holy shit','hom0','homey','homo','homodumbshit','homoerotic','homoey','honkey','honky','hooch','hookah','hooker','hoor','hootch','hooter','hooters','hore','horniest','horny','hot carl','hot chick','hotsex','how to kill','how to murdep','how to murder','huge fat','hump','humped','humping','hun','hussy','hymen','iap','iberian slap','inbred','incest','injun','intercourse','jack off','jackass','jackasses','jackhole','jackoff','jack-off','jaggi','jagoff','jail bait','jailbait','jap','japs','jelly donut','jerk','jerk off','jerk0ff','jerkass','jerked','jerkoff','jerk-off','jigaboo','jiggaboo','jiggerboo','jism','jiz','jiz','jizm','jizm','jizz','jizzed','jock','juggs','jungle bunny','junglebunny','junkie','junky','kafir','kawk','kike','kikes','kill','kinbaku','kinkster','kinky','klan','knob','knob end','knobbing','knobead','knobed','knobend','knobhead','knobjocky','knobjokey','kock','kondum','kondums','kooch','kooches','kootch','kraut','kum','kummer','kumming','kums','kunilingus','kunja','kunt','kwif','kwif','kyke','l3i+ch','l3itch','labia','lameass','lardass','leather restraint','leather straight jacket','lech','lemon party','LEN','leper','lesbian','lesbians','lesbo','lesbos','lez','lezza/lesbo','lezzie','lmao','lmfao','loin','loins','lolita','looney','lovemaking','lube','lust','lusting','lusty','m0f0','m0fo','m45terbate','ma5terb8','ma5terbate','mafugly','mafugly','make me come','male squirting','mams','masochist','massa','masterb8','masterbat*','masterbat3','masterbate','master-bate','master-bate','masterbating','masterbation','masterbations','masturbate','masturbating','masturbation','maxi','mcfagget','menage a trois','menses','menstruate','menstruation','meth','m-fucking','mick','microphallus','middle finger','midget','milf','minge','minger','missionary position','mof0','mofo','mo-fo','molest','mong','moo moo foo foo','moolie','moron','mothafuck','mothafucka','mothafuckas','mothafuckaz','mothafucked','mothafucked','mothafucker','mothafuckers','mothafuckin','mothafucking','mothafucking','mothafuckings','mothafucks','mother fucker','mother fucker','motherfuck','motherfucka','motherfucked','motherfucker','motherfuckers','motherfuckin','motherfucking','motherfuckings','motherfuckka','motherfucks','mound of venus','mr hands','muff','muff diver','muff puff','muff puff','muffdiver','muffdiving','munging','munter','murder','mutha','muthafecker','muthafuckker','muther','mutherfucker','n1gga','n1gger','naked','nambla','napalm','nappy','nawashi','nazi','nazism','need the dick','need the dick','negro','neonazi','nig nog','nigaboo','nigg3r','nigg4h','nigga','niggah','niggas','niggaz','nigger','niggers','niggle','niglet','nig-nog','nimphomania','nimrod','ninny','ninnyhammer'
,'nipple','nipples','nob','nob jokey','nobhead','nobjocky','nobjokey','nonce','nsfw images','nude','nudity','numbnuts','nut butter','nut butter','nut sack','nutsack','nutter','nympho','nymphomania','octopussy','old bag','omg','omorashi','one cup two girls','one guy one jar','opiate','opium','orally','organ','orgasim','orgasims','orgasm','orgasmic','orgasms','orgies','orgy','ovary','ovum','ovums','p.u.s.s.y.','p0rn','paedophile','paki','panooch','pansy','pantie','panties','panty','pawn','pcp','pecker','peckerhead','pedo','pedobear','pedophile','pedophilia','pedophiliac','pee','peepee','pegging','penetrate','penetration','penial','penile','penis','penisbanger','penisfucker','penispuffer','perversion','phallic','phone sex','phonesex','phuck','phuk','phuked','phuking','phukked','phukking','phuks','phuq','piece of shit','pigfucker','pikey','pillowbiter','pimp','pimpis','pinko','piss','piss off','piss pig','pissed','pissed off','pisser','pissers','pisses','pisses','pissflaps','pissin','pissin','pissing','pissoff','pissoff','piss-off','pisspig','playboy','pleasure chest','pms','polack','pole smoker','polesmoker','pollock','ponyplay','poof','poon','poonani','poonany','poontang','poop','poop chute','poopchute','Poopuncher','porch monkey','porchmonkey','porn','porno','pornography','pornos','pot','potty','prick','pricks','prickteaser','prig','prince albert piercing','prod','pron','prostitute','prude','psycho','pthc','pube','pubes','pubic','pubis','punani','punanny','punany','punkass','punky','punta','puss','pusse','pussi','pussies','pussy','pussy fart','pussy fart','pussy palace','pussy palace','pussylicking','pussypounder','pussys','pust','puto','queaf','queaf','queef','queer','queerbait','queerhole','queero','queers','quicky','quim','racy','raghead','raging boner','rape','raped','raper','rapey','raping','rapist','raunch','rectal','rectum','rectus','reefer','reetard','reich','renob','retard','retarded','reverse cowgirl','revue','rimjaw','rimjob','rimming','ritard','rosy palm','rosy palm and her 5 sisters','rtard','r-tard','rubbish','rum','rump','rumprammer','ruski','rusty trombone','s hit','s&m','s.h.i.t.','s.o.b.','s_h_i_t','s0b','sadism','sadist','sambo','sand nigger','sandbar','sandbar','Sandler','sandnigger','sanger','santorum','sausage queen','sausage queen','scag','scantily','scat','schizo','schlong','scissoring','screw','screwed','screwing','scroat','scrog','scrot','scrote','scrotum','scrud','scum','seaman','seamen','seduce','seks','semen','sex','sexo','sexual','sexy','sh!+','sh!t','sh1t','s-h-1-t','shag','shagger','shaggin','shagging','shamedame','shaved beaver','shaved pussy','shemale','shi+','shibari','shirt lifter','shit','s-h-i-t','shit ass','shit fucker','shit fucker','shitass','shitbag','shitbagger','shitblimp','shitbrains','shitbreath','shitcanned','shitcunt','shitdick','shite','shiteater','shited','shitey','shitface','shitfaced','shitfuck','shitfull','shithead','shitheads','shithole','shithouse','shiting','shitings','shits','shitspitter','shitstain','shitt','shitted','shitter','shitters','shitters','shittier','shittiest','shitting','shittings','shitty','shiz','shiznit','shota','shrimping','sissy','skag','skank','skeet','skullfuck','slag','slanteye','slave','sleaze','sleazy','slope','slope','slut','slut bucket','slut bucket','slutbag','slutdumper','slutkiss','sluts','smartass','smartasses','smeg','smegma','smut','smutty','snatch','sniper','snowballing','snuff','s-o-b','sod off','sodom','sodomize','sodomy','son of a bitch','son of a motherless goat','son of a whore','son-of-a-bitch','souse','soused','spac','spade','sperm','spic','spick','spik','spiks','splooge','splooge moose','spooge','spook','spread legs','spunk','stfu','stiffy','stoned','strap on','strapon','strappado','strip','strip club','stroke','stupid','style doggy','suck','suckass','sucked','sucking','sucks','suicide girls','sultry women','sumofabiatch','swastika','swinger','t1t','t1tt1e5','t1tties','taff','taig','tainted love','taking the piss','tampon','tard','tart','taste my','tawdry','tea bagging','teabagging','teat','teets','teez','teste','testee','testes','testical','testicle','testis','threesome','throating','thrust','thug','thundercunt','tied up','tight white','tinkle','tit','tit wank','tit wank','titfuck','titi','tities','tits','titt','tittie5','tittiefucker','titties','titty','tittyfuck','tittyfucker','tittywank','titwank','toke','tongue in a','toots','topless','tosser','towelhead','tramp','tranny','transsexual','trashy','tribadism','trumped','tub girl','tubgirl','turd','tush','tushy','tw4t','twat','twathead','twatlips','twats','twatty','twatwaffle','twink','twinkie','two fingers','two fingers with tongue','two girls one cup','twunt','twunter','ugly','unclefucker','undies','undressing','unwed','upskirt','urethra play','urinal','urine','urophilia','uterus','uzi','v14gra','v1gra','vag','vagina','vajayjay','va-j-j','valium','venus mound','veqtable','viagra','vibrator','violet wand','virgin','vixen','vjayjay','vodka','vomit','vorarephilia'
,'voyeur','vulgar','vulva','w00se','wad','wang','wank','wanker','wankjob','wanky','wazoo','wedgie','weed','weenie','weewee','weiner','weirdo','wench','wet dream','wetback','wh0re','wh0reface','white power','whiz','whoar','whoralicious','whore','whorealicious','whorebag','whored','whoreface','whorehopper','whorehouse','whores','whoring','wigger','willies','willy','window licker','wiseass','wiseasses','wog','womb','wop','wrapping men','wrinkled starfish','wtf','xrated','x-rated','xx','xxx','yaoi','yeasty','yellow showers','yid','yiffy','yobbo','zibbi','zoophilia','zubb','lanjiao','ccb']

curseresponse = ['Wow! This is where I learnt your language!🤓 https://www.youtube.com/watch?v=bawmxQE_Fj0','Can you stop fucking swearing 😤',"it's time for you to expand your vocabulary! 😘","why are you so mean 😢", "Sorry, not found in GPRIJC dictionary 🤷️","Sorry, still learning 🧠, try 'commands' for more options!"]
vocablist = ["presribe","Recidivism","Exculpate","Exonerate","hotchpotch","quaint"," unremittingly"," lineage"," mushroomed","austere"," facade"," harness"," hustle and bustle"," illustrious"," feat"," painstaking"," laudable vs culpable"," empirical","cognitive","indigenous","cardinal","oblong","spatial","causality","notion"
,"encode","profound","disposition","placid","transgressor","restitute","eschew","excavate","since time immemorial","rudimentary","uncharted territories","kitty","well-heeled","maiden","audacious","reside","vicinity","artisanal","snotty","relegate","seditious","stigma","prevalent","tunnel vision","camadarie","ecstacy","cement",
"emulate","stellar achievement","underpin","nexus","culpable vs laudable","precipitate","full-fledged","unequivocal vs ambiguous","novel","ambiguous","stifle","inicimal","fervently","groteque","adage","dire","dysfunctional","transmorgrify","channel","go-getter","horde","covenant","scuffle","dole out","obsolescence","strenuous"
,"eulogy","ludicrous","demise","rank and file","prevail","epitomise","knack","aplomb","unscathed","precept","self-effacing","relish","winsome","metamorphosis","peevish","sinuous","mantle","callous","preponderance","ramification","glisten","cryptic","nihilistic","chasm","finesse","resolute","fervour","teeming with","totem","emanate"
,"point-blank","unnerving","inaugural","sandblasted","careen","emblematic","anachronistic","antiquated","inconsequential","apt","omniprescence vs ubiquitous","promulgate","steel","emaciate","condemn","forsaken","deftly","adroit","adept","miasma","stump","stump","diminutive","tantamount to","delirious","ominous","derelict","circumstantial"
,"lauel (to rest on one's laurel)","suffuse","Recursive","implicitly","proponents","indelible","foraging","tranquil","rustic","idyllic","sanctuary","undulating","meander","congregate","pristine","exodus","permeate","straddle","kaleidoscope","bequeathe","luxuriant","sentinel","estuarine","galvanise","wafted through","diplomacy","asymmetric","anemone","amenable","efficacy","aftermath","detestable","abominable","overarching","collude","adverse","probable","exacting","egregious","pragmatic","onerous","boisterous","prejudice","susceptible","regurgitate","probity","parity","idiocy","idiosyncrasy","eccentric","prima donna","impede","unemcumbered","pelt","gruelling","esprit de corps","echelon","fraught with","meager","arbitrary","repatriate","astronomical","exorbitant","transient","assuage","proffer","vis-a-vis","purview","protracted","inequitable vs parity","in pursuant to"," imperative","tendril","awning","miniscule vs diminutive","emanate","hapless","rogue","rendevouz","serenity vs tranquility","conflagration","flail","cognizant","mounting","indulge","subsume","shoestring budget","belligerent","toll","outpace","stark","oncologist","geriatric care","cartel","postulate","allude to","deplore","disparage","exonerate","to cast aspersions","countervailing","retort","predominant","intravenously","entail","decimate","laurel","regress","lull","aforementioned","frivolous","stringent","exemplary","avid","rehabilitate","latter","endeavour","shrewed","crafty","bestial","treacherous","implicate","banister","instinctively","foiled","porous","potent","surreptitious vs clandestine vs collude","underscore","clandestine","unanimously","disconcerting","shrill","brute","contraption","tenets","shackles","sanguine","alleviate","insurmountable","amalgamation","pundit","intriguing","delactable","lingua franca","inadvertently","exuberant","antics","erroneous","bricks and mortar","advent","trajectory","mundane","automaton","endorse","indiscriminately","creme de la creme","ubiquitous","equity","perpetrate","tributaries","statuesque","rev","relentless","commodity","intrepid","remnant","burgeon","keep sth at bay","stave off","persona non grata","pedigree","unilaterally","menace","exacerbate","petrified","prowess","gaberdine","cordovan","swaggered","impertinent","incapcitated","beak","euthanasia","rapine","awash","wiry","impotent","anaemic","elicit","taut","wispy","ringlets","wade","prim","stricture","trapezoid","gaunt","cirrus","cumulus","meringues","sleek","distended","prominent","champing","intricate","variegated","devoid","outlandish","belching","deep pockets","haggle over","solitude","intertwine","compelled","contemptible","malice","contemn","veritable","pilgrimage","roughshod","contemporary","eloquence","archaic","coddled and cossetted","mogul","reprieve","alluring","incessant","grow accustom to","distant pipe dream","salient","appropriation","whiling away the time","add insult to injury","ram the point home","correlation","counter-intuitively","predispose","inclination","doting","disparate","girth","fortified","homespun","incongruous","enervate","sidle","inscription","menace","traverse","belligerent","garret","studious","endow","technocrat","conspicuous","incur the wrath of","lolly","punting","in lieu of","largesse","plutocracy","coerce","chivalrous","bawl out","deluge","succumb","deft","proffer","construe","exhort","iniquities","compel","prevalent","opine","toil","guzzles","voluminous","versatile","tout","panacea","upending","palpable","guise","existential","academia","entity","fret","paranoia","advocate","cite","potemkin","pedagogy","nonplussed","permeate","fallacy","per se","exemplify","analogous to","bestowed","plethora","realm","blinkered view","supersede","egalitarian","elitist","in tandem","resonance","impoverish","tenor","stasis","unwitting","perpetuate","expedite","noble","engender","remedial","entrenched","conjure","archetypal","quintessential","circumspect","omnipresent","outset","feral","guffaw","slither","stasis","indelible","riven","flatline","incessant","punitive","ascribed","stratospheric","pivotal","untennable","inexorably","seminal","multitudinous","irrespective","impartial","austerity measures","pious","tinkering around the edges","draconian","demurrals","luminary","into the fray","impotent","hubristic","punitive","ascribed","attrition","ethos","accolades","stratify","gain traction","in retrospect","proliferate","instill","consesnsus","confer","perch","gingerly","hitch","scourge","carrot-and-stick","rejoinder: clever witty reply"," riposte: quick"," witty response"," countervail: to use equal force again","reciprocate: to give/act in turn following the lead of another","refute: to produce evidence or proof that an arg is wrong"," retort: to reply in a sharp"," retaliatory way","inquisitive: Having the nature of an investigator","frenetic: frantic and frenzied"
,"angst: a feeling of anxiety"," dread or anguish","irascible: easily irritated/annoyed; prone to losing temper","niggling: petty","annnoying","officious: asserting authority in an overbearing manner","vexation: frustration/annoyance resulting from some action/statement","social affirmation","conformity","trodden","pervasive","amorphous","truncated","condoning","credence","leveraging","herd","vying","synonymous","batter","stoic","trivial","composed by/of","minute","nebulous","reel in","cusp","utilitarian","proclivities","permutations","glean","trance","blear","debauchery","douse","primeval","jarr","assuage","unencumbered","rites","plein","call at","call away","call by","call down upon","call in","dexterity"," sprawling"," reckon"," indisputable"," enthrall"," meticulous","immaculate"," fastidious","discharge","forays","due diligence","touted","parochial","vouch","sentiment","rife","concur","posit","ensconcing","masquerade","presenteeism","scaffold","sacrosanct"," foppish"," cathartic"," milieu"," genial"," in the throes"," sheepish"," gale"," acclimatised to"," inkling"," yesteryear"," intrinsically"," indomitable"," at the forefront","revamp","drudgery","succession","overhaul","bolting","vernacular","periodically","forthcoming","inpart"," pro bono","demography","yogic","accrue","caricature","anarchic","adulterate","arboreal","plod ahead/through/on","abate","impediment","steel","bard","run of the mill","be in a rut","pilot-programmes","siphon off","afoot","oligarch","proverbially","replete with","folly","zealot","pandered","rabble-rousing","populous","presided over","dud","illict","glitzy","perversely","quagmire","propitious","upperhouse","sap","chauvinist","hamstring","preaching the virtues of","edgeways","bedivilling","inroads","decry","intricate","ordain","prudent","zoonotic","pertain","avian","gain a foothold","drawn on","veracity","envisage","blundering","concerted","morbidity","profanity","brain drain","prudish","emancipation","constrictions","ensue","onerous","fall away"," incalculable","social mores","vex","gateway to/ for something","kiki"," do you love me"," en masse","bureaucrats","wallah","ploy","exodus","construe","moped","bigot","wahhabism","apprehension","perilous","contempt","callous","unorthodox","persona-non-grata","anachronistic","squalid","dinghy","wanton","virulently","fervour","precarious","parable","reproachfully","precocious","sultry","aficionado","faddish","trawling","arcana","unnerve","bestride","neophyte","caveat","erudite","curator","corroborate","sacrosanct","monoliths","precarious","fervour","ascetic","inoculation","resignedly","morbidity rate","promulgate","arbitrate"," impetus","disrepute","secular","espuse","indictment","hitherto","apex","subsist","staunchly","syndicate","ignominious","genuflection","show deference to","ruminate","ignominious","indubitably","incontrovertibly","ironclad","vindicate","intrinsic","inherent","maxim","transphobic","staunch","gender dysphoria","upend","profess","whiff","infidelity","bereft","disquiet","ineffable","contrive","debilitating","extenuating","clarion call","propensity","scant","metastasize","decidely","empanel","disparate","allusive","homoeroticism","paraphernalia","promulgate","arbitrate","impetus","disrepute","secular","espouse","indictment","hitherto","apex","subsist","syndicate","emancipate","afflict","concerted efforts","unbridled","unfettered ","disuse","the apple never falls far from the tree","a barking dog never bites","a bird in the hands is worth two in the bush","subordinating","injunction","promulgate","presage","besmirch","spur","impetus","ephemeral","mischaracterising","bigotry","alimony","misogynistic","incarcerate","gerrymandering","vilify","demagogue","exculpoate","exonerate","despot","true blue","internment","pretence","subvert","mere lip service","masquerading","America is addicted to oil","anthropogenic","desecrated","morally reprehensible","sui generis","eminently","unimpeachable dedication","instituting","dismal","pecuniary","ad nauseam","triple bottom line","fiasco","dimetrically ","foolhardy","renege","prescribe value","recividism","anathema","epiphany","scourge","disquiet","subjugation","guerilla","insurrectionary","connivance","infanticide","micro financing","androgynous","pervade","heterodox","innumerable","ebullient","pneumatic","morose","reticent","absolve","exculpate","Prescribe value","Recidivism","Exculpate","Anathema","Epiphany","Scourge","Disquiet","Subjugation","Guerilla ","Insurrectionary","Connivance","Infanticide","Microcredit","Androgynous","Pervade","Heterodox","Innumerable","Ebullient","Pneumatic","Morose","Reticent","A beacon of hope","Heinous crime","Annex","Absolve","Misdemeanour ","Felony","Mens rea","Actus reus","Unbidden","Irascible","methamphetamine","Touted","Moratorium","Disgruntle","Fickle","Roe v wade","Enticement","Wayward","Decadence","Pander","Innocuous","Ill conceived","Acrimony","Social strife","Placate","Nascent separatism","Anthropogenic","Desecrated","Morally reprehensible"
,"Sui-generis","Eminently","Unimpeachable dedication","Instituting","Dismal","Pecuniary","Ad nauseam","Triple bottom line","Fiasco","Diametrically","Foolhardy","Renege","Crude"]
def send_message(text, chat_id):
    economistlist = getarticle()
    
    counter = 1
    firsttext = ("Here are the top 5 articles for " + str(date.today()))
    url = URL + "sendMessage?text={}&chat_id={}".format(firsttext, chat_id)
    requests.get(url)
    for article in economistlist:
        tosend = article.strip('[')
        tosend = tosend.strip(']')
        titletext = tosend
        url = URL + "sendMessage?text={}&chat_id={}".format(titletext, chat_id)
        requests.get(url)
        counter += 1
    sglist = getsgarticle()
    for article in sglist:
        tosend = article.strip('[')
        tosend = tosend.strip(']')
        titletext = tosend
        url = URL + "sendMessage?text={}&chat_id={}".format(titletext, chat_id)
        requests.get(url)
        counter += 1

def lambda_handler(event, context):
    message = json.loads(event['body'])
    try:
        chat_id = message['message']['chat']['id']
    except:
        chat_id = adminchatid
    try:
        first_name = message['message']['chat']['first_name']
    except:
        first_name = "failed firstname"
    try:
        username = message['message']['chat']['username']
    except:
        username = "failed username"
    try:
        msg_id = message['message']['message_id']
    except:
        msg_id = 5
    #time stamp
    #try:
      #  
    #except:
       # 
    try:
        date = message['message']['date']
        # date = str(date.today())
        timestamp = datetime.fromtimestamp(date)
    except:
        timestamp = str(adminchatid)
    try:
        fullreply = int(fullreply)
        reply = str(fullreply)
    except:
        try:
            fullreply = message['message']['text']
            reply = fullreply.lower() 
        except:
            fullreply = "no"
            reply = fullreply.lower()
    logurl = "https://api.telegram.org/bot{}/".format(TELE_TOKEN2)
    infolog = ("text: " + str(fullreply) + ", name: " + str(first_name) + ", username: " + str(username) +  ", user_id: " + str(chat_id) + ", msg_id: " + str(msg_id) + ", timestamp: " + str(timestamp))
    logurl = logurl + "sendMessage?text={}&chat_id={}".format(infolog, adminchatid)
    logurl2 = "https://api.telegram.org/bot{}/".format(TELE_TOKEN3)
    logurl2 = logurl2 + "sendMessage?text={}&chat_id={}".format(infolog, adminchatid)
    
    f = open("/tmp/namefile.txt","w+")
    with open('/tmp/namefile.txt') as f:
        if username in f.read():
            print("have")
        else:
            xie = open("/tmp/namefile.txt","a+")
            xie.write("\n "+ username)
            nameinfolog = ("New user! " + str(username))
            requests.get("https://api.telegram.org/bot{}/".format(TELE_TOKEN2) + "sendMessage?text={}&chat_id={}".format(nameinfolog, adminchatid))
    
    
    if reply == "mf26":
        firsttext = ("Here is your MF26! :)")
        sendmyshit(firsttext, chat_id)
        titletext = "https://www.seab.gov.sg/content/syllabus/alevel/2018Syllabus/ListMF26.pdf"
        sendmyshit(titletext, chat_id)
    elif reply == "about":
        responselist = ["This bot is built by the GPRIJC team and will be maintained as long as they are alive. So keep them alive. Thnks.","also if u would like to thank the people behind the entire ecosystem, pls free to buy us a cup of coffee as a word of thanks!😋😋 https://www.patreon.com/user?u=26290351"]
        for response in responselist:
            sendmyshit(response, chat_id)
    elif reply == "wordlist":
        sendmyshit("How many words would you like? (1 to 20)", chat_id)
    elif integer(reply):
        for i in range(0,int(reply)):
                word = random.choice(vocablist).lower()
                meaning = str(definition(word)).strip('"').strip("]").strip("[")
                sendmyshit(str(i+1) + ". " + word + " -- " + str(meaning).strip('"'), chat_id)
    elif reply == "linklist":
        linklist = ["SGExam RESOURCES - exams.sg","QUICK STUDY RESOURCE - tick.ninja","ECONS ESSAY PLANNER - http://www.thateconsplanner.com","KS BULL 2018 ISSUE 1 - https://ivy.ri.edu.sg/courses/1232/files/98436/download?download_frd=1","KS BULL 2018 ISSUE 2 -https://ivy.ri.edu.sg/courses/1232/files/91528/download?download_frd=1", "JC Papers from other JCs - https://drive.google.com/drive/mobile/folders/15GrqdzOpdQQ3W2QTytIJ1vAUKFs3ISH_", "Physics and Maths Tutor - https://www.physicsandmathstutor.com/past-papers/a-level-physics/"]
        for word in linklist:
            sendmyshit(word, chat_id)
    elif reply == "essays":
        linklist = ["RJC Model Essays Issue 1 - https://cdn-03.anonfile.com/L7Xeq291na/a40e9cba-1572180897/2019KSBull.pdf", "RJC Model Essays Issue 2 - https://cdn-25.anonfile.com/OaX6q09an3/96b33c37-1572180994/2019KSBull2.pdf"]
        for word in linklist:
            sendmyshit(word, chat_id)
    elif reply == "chem":
        urllink = ["DATABOOKLET - https://www.alevelh2chemistry.com/wp-content/uploads/2019/05/9729-Data-Booklet-for-JC-A-Level-H1-H2-H3-Chemistry-Syllabuses-Original.pdf","ENERGETICS DEFINITIONS - https://www.alevelh2chemistry.com/chemical-energetics-definitions-of-standard-enthalpy-changes-of-reactions/","PERIODIC TABLE - https://ptable.com/print/periodic-table.pdf"]
        for link in urllink:
            sendmyshit(link, chat_id)
    elif reply == "phy":
        urllink = ["DATABOOKLET - https://filestore.aqa.org.uk/resources/physics/AQA-7408-SDB.PDF","DEFINITIONS - https://cdn-17.anonfile.com/U2y2x29dnd/fc3bc1c7-1572320097/PHYSICSDEFINITIONS.pdf\n or \nhttps://drive.google.com/open?id=1ODL8qihVIBLkbX2IKykrVff3mSuAKoIo\n or \nhttps://anonymousfiles.io/f/PHYSICSDEFINITIONS_2.pdf"]
        for link in urllink:
            sendmyshit(link, chat_id)
    elif reply == "bio":
        urllink = ["NOTES - https://drive.google.com/drive/folders/1xWfBNF0FsNhM4ezYtLpjK73ffPrccVCJ?usp=sharing"]
        for link in urllink:
            sendmyshit(link,chat_id)
    elif reply == "econs":
        urllinks = ["ECONS DEFINITIONS - https://cdn-04.anonfile.com/6eFeqc91n7/952b311e-1572173701/Definitions.pdf \n or \nhttps://drive.google.com/open?id=1GaLDXS1Nw1snRw--rxsMkizRFRD1ip8J","2008-2018 A level Answers -- https://drive.google.com/drive/folders/10b1j1I0jLyGQ_ZfxcF7-QFq0s_hRjqp8",
        "NOTES - https://drive.google.com/drive/folders/1bIVWIvmx8vzmujHD-xPyprse0IQDveDE?usp=sharing","2014-2019 ECONOMICS PRELIM PAPERS - https://drive.google.com/drive/folders/1f07WNMUHA7CJ6vHzCiWDHncJkh269Tkt?usp=sharing",]
        for url in urllinks:
            sendmyshit(url, chat_id)
    elif reply == "quotes":
        urllinks = ["GP Quotes 1 - https://drive.google.com/open?id=1sWDPeaR5hAkxlToz-mD2Of37VISjAjRg"]
        for url in urllinks:
            sendmyshit(url, chat_id)
    elif reply == ("podcast" or "podcasts"):
        urllink = ["IntelligenceSquaredUS Debates - https://open.spotify.com/show/5g5YrVw4ednbJpN7tuyb2k?si=GTC_w2j6QW2YTm84dkAVeg",
        "WIRED -- https://open.spotify.com/show/0SH5lhsW8vV6OgmrXRQXAD?si=9IVvtnmiQMGsmMdz6QnURw", 
        "IntelligenceSquared Discuss - https://open.spotify.com/show/7gnNY9Fy8QSRbjXZ00A9jW?si=rsjeJqf8TXuCmSHE5_Ughw",
        "BBC Global News - https://open.spotify.com/show/3wBfqov60qDZbEVjPHo0a8?si=B3CXjhKrTqmqOjZ9q4sVHg",
        "Vox Today Explained - https://open.spotify.com/show/3pXx5SXzXwJxnf4A5pWN2A?si=XYhLPHxfR--kSafQtFMqBA"]
        for link in urllink:
            sendmyshit(link, chat_id)
    elif reply == "others":
        urllinks = ["ADULTING IN SG - http://www.howtoadult.sg", "MONEYSMART - https://www.moneysmart.sg", "pls dm @gp.rijc on instagram to suggest additional features!","Feel free to contribute notes/files @ https://drive.google.com/drive/folders/1FF6WZk9_7OwPPhCTlX4OQVBhYmw9v1vC?usp=sharing"]
        for urllink in urllinks:
            sendmyshit(urllink, chat_id)
    elif reply == "commands":
        sendmyshit("Enter any of these commands:", chat_id)
        commandlist = ["news -- 5 Daily News Articles","essays -- General Paper Model Essays", 'papers -- Prelim Papers for As', "mf26 -- MF26","econs - Economics Stuff", "chem -- Chemistry Stuff", "bio -- Biology Stuff", "phy -- Physics Data Booklet","def *word* -- Returns Definition of Word", "wordlist -- List of Vocabulary/Phrases","quotes -- List of GP Quotes", "linklist -- List of Useful Resource Links", "about -- About my dear creator", "others -- List of other useful links",
        'podcast -- List of Constructive, Comprehensive Podcasts']
        for command in commandlist:
            sendmyshit(command, chat_id)
    elif reply == "news":
        send_message(reply, chat_id)
    elif reply == 'papers':
        commandlist = ["2008-2018 ALEVEL SCHOOL PAPERS - https://drive.google.com/folderview?id=1LRcmzHDzVTTv1TnxhdVZPjLJT_G-OnqG", '2019 ALEVEL PRELIM PAPERS -- https://drive.google.com/drive/u/1/folders/1m6T-AzajfmCJ83Z8dhivsSTNMqf8e-uF']
        for command in commandlist:
            sendmyshit(command, chat_id)
    elif reply == 'secret':
        commandlist = ["AI NOTES - https://cdn-18.anonfile.com/H6vdr695ne/eab2c5de-1572187870/AINotes.pdf","ECONOMICS DEFINITIONS -- https://drive.google.com/open?id=1XzsTJG4jSEaaywQlVO0t6e8z-Qj6pQVL",
        "PHYSICS DEFINITIONS - https://drive.google.com/file/d/1-sWC97iYQl1dHERdfvGju-1z4OTxqvkG/view",
        "ACEYOURECONS - aceyourecons.talentlms.com"]
        for command in commandlist:
            sendmyshit(command, chat_id)
    elif reply[:3] == "def":
        word = reply[4:].lower()
        try:
            meaning = definition(word)
            counter = 1
            meaningstring = ""
            for lexicon in meaning:
                meaningstring += ("\n " + str(counter) + ". " + str(lexicon) + "\n ")
                counter += 1
            if str(meaning) != "":
                sendmyshit(word + " -- " + str(meaningstring), chat_id)
            else:
                sendmyshit(word + " -- " + "no definition found :(", chat_id)
        except:
            sendmyshit(word + " -- " + "no definition found :(", chat_id)
    elif reply[:3] == "rep":
        try:
            if reply[12] != " ": #if it is 9 characters long
                chatid = int(reply[4:13])
                text = reply[14:]
                sendmyshit(str(text), chatid)
                sendmyshit("done, sent: " + str(text) + ", to: " + str(chatid) , adminchatid)
            else: #if it is 8 char long
                chatid = reply[4:12] #grab 8 digits
                text = reply[13:]
                sendmyshit(str(text), chatid)
                sendmyshit("done, sent: " + str(text) + ", to: " + str(chatid), adminchatid)
        except:
            sendmyshit("failed", adminchatid)
    elif (reply in cursewords):
        choice = random.choice(curseresponse)
        if choice == "it's time for you to expand your vocabulary! 😘":
            sendmyshit(choice, chat_id)
            for i in range(0,5):
                word = random.choice(vocablist)
                sendmyshit(word, chat_id)
        else:
            sendmyshit(choice, chat_id)
    else:
        responze1 = "Unrecognized command. Say what? Try 'commands'!"
        sendmyshit(responze1, chat_id)
    
    requests.get(logurl)
    requests.get(logurl2)

    return {
        'statusCode': 200
    }
    
    

def definition(text):
    definitionlist =[]
    url = "https://dictionaryapi.com/api/v3/references/sd4/json/" + str(text) + "?key=" + "e23a2515-5414-4fe1-9e40-9c286f74d326"
    r = requests.get(url)
    definitionlist = []
    instring = json.loads(r.text)
    for mean in instring[0]['shortdef']:
        definitionlist.append(str(mean).strip("'").strip("[").strip("]"))
    return definitionlist
    
def integer(text):
    try:
        text = int(text)
        if text <= 20:
            return True
        else:
            return False
    except:
        return False
        
def find(key, dictionary):
    for k, v in dictionary.items():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                for result in find(key, d):
                    yield result

def getarticle():
    response = requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=73756f6d2dc6451399fcb0b15ad9d8cc",verify=False) 
    nyt = requests.get("https://newsapi.org/v2/top-headlines?sources=the-new-york-times&apiKey=73756f6d2dc6451399fcb0b15ad9d8cc",verify=False)
    todos = json.loads(response.text)
    nyttodos = json.loads(nyt.text)
    articles = todos['articles']
    nytarticles = nyttodos['articles']
    # print(type((articles)))
    economistlist = []
    nytlist = []
    for i in range(0,2):
        article = nytarticles[i]
        title = article['title']
        desc = article['description']
        link = article['url']
        content = article['content']
        altogether = title + " " + link + " "
        economistlist.append(altogether)
    return economistlist
    
def getsgarticle():
    sgnews = requests.get("https://newsapi.org/v2/top-headlines?country=sg&apiKey=73756f6d2dc6451399fcb0b15ad9d8cc",verify=False)
    json_sgnews = json.loads(sgnews.text)
    sgarticles = json_sgnews['articles']
    sglist = []
    for i in range(0,3):
        article = sgarticles[i]
        title = article['title']
        link = article['url']
        content = article['content']
        altogether = title + " " + link + " "
        sglist.append(altogether)
    return sglist

def sendmyshit(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    requests.get(url)
    return {
        'statusCode': 200
    }

