
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
from dotenv import load_dotenv

load_dotenv()  # carica da .env se esiste

URL_BASE = os.getenv("URL_BASE", "http://localhost:8000")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="static"), name="static")

BLOG_POSTS=[
        {
  "pubblicazione": "2025-09-02T10:49:31.833+00:00",
  "titolo": "E' ancora possibile la vita?",
  "testo": "Potrebbe sembrare strano ma non tutti i negozianti sono degli imprenditori. A Trieste c’è una macelleria equina che anni fa frequentavo sempre. Il macellaio (il macellaio, non l’imprenditore o il proprietario, anche se sono la stessa persona) ha una settantina d’anni. Ha la sua clientela e non credo faccia più di 200€ al giorno. So quanta gente ci entrava e stava aperto solo la mattina. Il locale era suo e si portava a casa quello che gli serviva per vivere bene. Un economista capirebbe subito che dal punto di vista finanziario quell’attività stava perdendo soldi. Il locale era in centro e un negozio ‘moderno’ gli avrebbe pagato di affitto ben più di quanto lui potesse guadagnare nel suo mese migliore. \nDal punto di vista dell’economista il vecchio macellaio era un idiota perchè non sfruttava quello che aveva e si ostinava a lavorare. Non metteva a frutto il capitale.\n\n<br> \n\nLe aziende - e noi - siamo andati da tempo oltre. Non traiamo profitto solo dai capitali tradizionali. E’ del tutto normale mettere nei bilanci gli assett immateriali, quei “beni” che un’impresa possiede e l’aiutano a generare ricchezza pur essendo intangibili. Dai brevetti al know how, al logo di coca cola che gli consente di vendere le stesse molecole chimiche a prezzo più alto di tutte le fake cola. \n\n<br> \n\nAnche noi, forse meno consciamente, abbiamo capito che si possono capitalizzare gli assett immateriali. “Paghi la vista”, “E’ un’esperienza”, “Il sapore della tradizione” non suggeriscono forse la legittimazione di questo fatto?  \n\n<br> \n\nSono al porto di Volos. I ristoranti sono agghiaccianti ma quello in cui sono resiste e fa dei piatti semplici e sublimi. Il cuoco non ha capito la lezione - come il macellaio - perchè è un ristorante economico - ovvero non lo è ancora. (il prossimo articolo sarà su questo, sul doppio significato che la parola economico ha in italiano). Un giorno forse capirà che è bravo e quindi che può capitalizzare questa bravura.  Se sarà autenticamente moderno non inserirà nessuno ingrediente pregiato nel menù, basterà capitalizzare il suo know-how. Ovvero alzare i prezzi. Nessuno dubiterà che questo sia legittimo. Nessuno lo dubita.  Infatti l’aggettivo con cui io e i miei amici definiamo questo ristorante è assurdo. Non dovrebbe esistere così. I ristoranti che esistono ora sono come quello di cui ho visto in un vicolo di Marsiglia: pane e olio 4€. La semplicità si paga.\n\n<br> \n\nNon possiamo avere l’aspettativa che qualcuno con un buon ristorante che funziona, con un cuoco capace, possa rinunciare consapevolmente a guadagnare di più di quanto guadagna ora.\n\n<br> \n\nNon ce lo possiamo aspettare e siamo noi stessi sempre di più attenti a sfruttare le nostre possibilità di guadagno. A mettere a rendita non solo il nostro lavoro ma anche ciò che possediamo e ciò che siamo. La messa a rendita del nostro capitale più classico (i soldi in banca) è un esempio banale, anche se ubiquo - lo dimostra l’esplosione delle piattaforme di gestione di finanza personale per giovani nell’utimo periodo. \n\n<br> \n\nMa cosa stiamo facendo quando affittiamo la nostra stanza la settimana della moda? Quando traffichiamo i nostri vestiti su Vinted vantandoci con gli amici di averlo venduto il doppio di quanto lo abbiamo pagato? Economicizziamo pezzi della nostra vita.\n\n<br> \n\nFarlo significa solo non essere stupidi. D’altronde dopo che ci ha spennato il ristorante, il negozio di vestiti usato, il proprietario di casa 80enne, non saremo noi il buon samaritano. Noi con le nostre bollette, i nostri stipendi bassi, i nostri cocktail costosi. \n\n<br> \n\nContrastare questo meccanismo quando la scelta diventa il nostro quotidiano e non resta nei board di temibili multinazionali sembra impossibile perchè assomiglia in tutto e per tutto a una scelta irrazionale e don chisciottesca. Salvo che poi ci troviamo stritolati nel meccanismo.\n\n<br> \n\nFrancesco Ferrero, vincitore del primo Masterchef, su Instagram parla di cibo in una maniera che mi piace molto. Una volta ha scritto di una piccola città in Marocco dove mangiava in un ristorante delle verdure portate da lui. Diceva ‘*qui la vita è ancora possibile*’. \n\n<br> \n\nCiò che contribuisce a rendere impossibile la vita alle nostre latitudini (ma ormai sempre più giù) è che a tutto è già stato dato un prezzo e tutti cercano qualcosa su cui esporlo.\n\n<br> \n\nNella vecchia economia ciò che determinava questo prezzo era principalmente il lavoro e i costi di produzione di un bene. Ora è il valore percepito. Ogni cosa costa per quanto ne possiamo godere. \n\n<br> \n\nSono a Palermo, non ci torno da dieci anni. Vado al mercato del Capo, sperando che sia meglio della Vucciria, che so essere solo per turisti ormai. Neanche li c’è scampo. Chiedo numi a Silvia, mia amica di Palermo. Mi dice che ormai per comprare la frutta (i mercati ora sono ristoranti) c’è qualche piccolo mercato settimanale o i supermercati. Tutti i bancarellari l’hanno capito benissimo, che il loro capitale di bancarelle di ferro arrugginito non valeva niente ma la tradizione, quella potevano venderla a peso d’oro. E la gente ora deve comprare le pesche dure e insapori dei supermercati.\n\n<br> \n\nL’aria così si fa più rarefatta e la vita asfissiante perchè ciò che viene prezzato (e quindi reso più scarso) è esattamente la possibilità di godimento. E ogni possibile valore è già stato prezzato.\n\n<br> \n\nCerto, la vita non è solo godimento ma il meccanismo non si ferma qui.  \n\n<br> \n\nPrezzato il prezzabile, non resta che il residuo - ciò che non può essere subito fagocitato come si vorrebbe ( “il residuo è il mondo”  dice Simone Weil in Calasso - *Il cacciatore celeste* pag 132 - ma questa è un’altra storia). Il residuo va quindi eliminato o standardizzato per poter essere sfruttato.\n\n<br> \n\nNon sarà difficile.\n\n<br> \n\nA Piazza Morbegno a Milano il residuo a settembre 2025 è minimo: un negozio di musica impolverato e un ferramenta. Tutto il resto sono bar o - il peggio - vinai con cucina. So che il ferramenta ha venduto l’attività - a qualche coktail bar of course. Vendere l’attività significa: vendere il contratto di affitto. Paghi per prenderti il diritto di pagare l’affitto li. Può essere molto conveniente se l’affitto è basso. Quanto sarà servito per far ingoiare ai negozianti l’amore per il proprio lavoro?\nEccola qui, la vita che scompare ingurgitato il residuo. Dove andrei, se abitassi ancora li, a comprare bulloneria e farmi consigliare da un esperto? Probabilmente dovrei prendere la rossa, andare ancora più in periferia, forse in qualche OBI gigante e impersonale. \n\n<br> \n\nI ristoranti al porto sono già orribili - macchine da soldi per far mangiare prodotti surgelati a turisti senza forze. Ma fatturano e quindi, anche qui, pagano affitti più alti. Un giorno anche il proprietario delle mura del nostro ristorante deciderà di alzarlo. Il nostro amico cuoco potrà andare in perifieria o alzare i prezzi. Per fare ciò dovrà buttare le tovaglie di carta, i bicchieri spessi e il suo sarà un altro ristorante come tanti. Sul lungomare di Volos ogni metro quadro sarà sempre più conquistato da tavolini sempre meno acccoglienti. Anche chi non volesse per forza godere, ma magari mangiare un panino alla buona con gli amici, dovrà fuggire altrove, finchè non impareranno a sfruttare il capitale anche li.",
  "id": "68b6af9f001637a3ea55",
  "sequence": 4,
  "createdAt": "2025-09-02T08:49:35.761+00:00",
  "updatedAt": "2025-09-02T08:49:35.761+00:00",
  "permissions": [],
  "tags": [],
  "databaseId": "67b9b2060006cbdb292d",
  "tableId": "67b9b23a00059abb3c7d"
},
       {
  "pubblicazione": "2025-06-21T16:15:47.483+00:00",
  "titolo": "Autenticissimo",
  "testo": "Domenica scorsa si cercava un panino al lampredotto, esasperati dalla chisura di tutti i punti di fiducia, pur con una amica fiorentina ci siamo dovuti dirigere  al ‘’mercato’’ centrale. <br>\nLuogo orrido dove sai già cosa aspettarti. La ‘’’tradizione’’’ è tutta li. E’ un luogo a tutti gli effetti tipico, tipico però non di Firenze ma del nostro tempo. Accanto al lampredottaro non ci si vergogna certo a mettere della cucina asiatica, delle pizze, delle brioche col pistacchio. <br>\nSiamo però fortunati e non perchè il panino col lampredotto era meno infimo e caro di quanto pensassimo. No, la modesta sopresa è stata ampiamente controbilanciata dal dover affrontare una corsa insostenibile per trovare il posto. La fortuna sta nel trovarsi in un luogo talmente finto da non sembrare credibile, da non lasciare dubbi sulla natura dell’inganno. <br><br>\n\nCamminando per le strade di Firenze e guardando le boutique che vendono oggetti in pelle viene la tentazione di domandarsi se quella in cui ci stiamo fermando sia autentica o no. Incorriamo così in quella confusione, nella fatica di dover distinguere fra un vero e un falso. Questa confusione e l’ansia che l’accompagna è il sentimento più pervasivo del turista moderno. Confusione legittima ma del tutto inutile. \n<br><br>\nL’inganno più significativo, corrodente e profondo non sta infatti nel falso, ovvero nella plasticosa imitazione probabilmente prodotta in asia, ma nel vero, nell’oggetto effettivamente realizzato in cuoio da un artigiano italiano. L’inganno è, esattamente, pensare che stai comprando un oggetto di qualità, che durerà nel tempo, fatto con metodi tradizionali. Che sia effettivamente così dal punto di vista materiale conta veramente poco. Nella sostanza quello che compri è esattamente identico all’oggetto contraffatto perchè, come tutti dovremmo sapere, quello che stai comprando è semplicemente un’idea, l’emozione della tradizione, il cuore segreto di quel luogo. Domandarsi cosa sia questa tradizione è abbastanza inutile. In realtà sta li solo in quanto categoria di marketing, ovvero per espandere il numero di oggetti da vendere (ma anche e sempre di più ‘esperienze’, ovvero la vendita di sensazioni slegata dal fastidioso e vetero capitalistico bisogno tecnico della produzione di un oggetto sui cui appiccicarle). La ricerca spasmodica di parametri oggettivi per misurarla ( è vero cuoio, come sono le cuciture, me la sta vendendo un amabile vecchietto, è fatta a mano) serve solo a due cose. Innanzitutto a rendere il piacere dell’acquisto finale più intenso, ad amplificare l’esperienza acquisto con l’esperienza ricerca (predominante in altri settori, come la caccia alla chicca nei mercatini dell’usato). Secondariamente a creare una differenziazione di classe (ovvero: di fasce di marketing) fra chi può permettersi l’autentico più o meno contraffatto.\n<br><br>\n\nLa grande bellezza del mercato centrale di firenze è che consente di guardare il nostro vero stato. Li non ci dobbiamo più preoccupare se stiamo di fronte alla finzione della finzione o alla finzione semplice. Tutto è stato chiaramente costruito per noi. Forse li potremmo smettere di usare le virgolette per la parola tradizione perchè ormai il suo significato ha definitivamente oltrepassato quello precedente, non è più ambiguo. \n<br><br>\nQuesto certo ci genera una grande irritazione. L’irritazione di ritrovarsi consumare qualcosa espressamente fatto perchè noi lo potessimo consumare in quel luogo. L’irritazione di essere oggetti subenti il marketing e il capitalismo.\n<br>\nDa una parte questo non dovrebbe colpirci così tanto, è soltanto vedere il mondo in cui viviamo. D’altra parte ci viene voglia di combatterlo; ci sono alcune risposte a questa nostra condizione che sembrano interessanti ma rischiano di farci sprofondare nelle medesime ambiguità. Ne parlerò presto",
  "id": "6856be97003d7f23f1e1",
  "sequence": 3,
  "createdAt": "2025-06-21T14:15:52.475+00:00",
  "updatedAt": "2025-06-21T14:17:35.774+00:00",
  "permissions": [],
  "tags": [],
  "databaseId": "67b9b2060006cbdb292d",
  "tableId": "67b9b23a00059abb3c7d"
},
        {
  "pubblicazione": "2025-01-22T00:00:00.000+00:00",
  "titolo": "Un prodotto perfetto\n",
  "testo": "Nell'irresistibile 'Guida  perversa all'ideologia' Zizek racconta della geniale trovata di Starbucks: una piccola percentuale di ogni caffè viene data in beneficenza. Non so se ancora sia così ma l'idea è chiara. Non ti stai gustando un caffè ma stai facendo del bene. \nIl messaggio è: \"Yes our cappuccino is more expensive than others but we give one percent of all our income to some Guatemala children to keep them healthy. For the water supply for some Sahara farmers, or to save the forests, to enable organic growing coffee, etc.\"<br>\nE Zizek dice:<br>\n\"In the old days of pure simple consumerism, you bought a product and then you felt bad. \"My God, I'm just a consumerist while people are starving in Africa.\" So the idea was you had to do something to counteract your pure distractive consumerism.\"<br>\nDuoLingo ha raggiunto lo stesso miracolo mimetico.\n<br><br><br>\nLa realtà da nascondere non è più 'sono un consumista' ma 'sono un dipendente digitale'. Nel vecchio mondo - cinque anni fa - nessuno si sentiva davvero in colpa di usare il telefono così tanto. Nel nuovo si. La macchina addittificante ha raggiunto una potenza tale che la massa che se ne rende conto non è più trascurabile. E quindi bisogna inventare una soluzione interna al sistema per evitare che il sistema crolli.<br>\nNon basta più creare CandyCrush. Non basta più far scorrere infiniti reel. Non basta più creare telefoni dai colori tropicali, con suoneria accattivanti e notifiche infinite. SIAMO SOPRAFFATTI. <br>\nE quindi: le impostazioni per controllare il tempo di utilizzo. I telefono in bianco e nero. <br><br>\nE quindi: chiedete a chiunque perchè scorra instagram e vi dirà sempre che ha un feed di cose interessanti e che lo usa per informarsi. <br>\nChiedete a un artista e vi dirà che segue artisti. Chiedete a un appassionato di calcio e vi dirà che segue le notizie del calciomercato. Chiedete a un attivista e vi dirà che segue le pagine che dicono quello che succede veramente a Gaza. Ma interrompete qualcuno mentre scrolla o scrollate con lui/lei. Di tutti questi contenuti ci sarà traccia si ma stemperata in mezzo a milioni di inutilità. Gatti, macchine, modelle a dubai, piatti pieni di sushi. D'altronde non è davvero colpa nostra. Instagram potrebbe essere infinitamente più utile. Pensate a quanta fatica bisogna fare per trovare eventi in una città nuova. Devi cercare per nome, seguire, guardare fra i seguiti. Sarebbe così facile, fare una ricerca per tipologia e luogo. Ma sarebbe inutile, perchè vedremmo solo quello che ci interessa davvero. Potremmo dire che i contenuti interessanti servono soltanto a farci navigare nel letame. Ma sarebbe consolatorio, la realtà è molto più disturbante: servono a giustificarci mentre ci godiamo la nostra nuotata nel letame, di cui godiamo tantissimo finchè abbiamo qualcosa che ci distrae dal fatto che siamo coperti di merda.<br><br>\nE quindi: non gioco a CandyCrush non sono certo un boomer in metro ma i miei dieci minuti di oblio dopaminoso li voglio cazzo. Impara una nuova lingua. Non importa se la imparerai, se potresti studiare meglio e più velocemente con un po' di attenzione. Vieni qua, potrai guardare uno schermo con un uccellino che saltella, tutto colorato e cliccare alla rinfusa associazioni mai troppo difficili. Goditi tutto questo perchè stai migliorando la tua vita, stai scoprendo una nuova cultura, stai facendo continuous learning. Non stai usando il cellulare: stai studiando. E sei bravo: mille pietre azzurre in ricompensa.\n",
  "id": "67c5781a000f732fa9dc",
  "sequence": 2,
  "createdAt": "2025-03-03T09:36:26.381+00:00",
  "updatedAt": "2025-03-03T16:43:40.928+00:00",
  "permissions": [],
  "tags": [],
  "databaseId": "67b9b2060006cbdb292d",
  "tableId": "67b9b23a00059abb3c7d"
}
        ,
        {
  "pubblicazione": "2025-02-16T00:00:00.000+00:00",
  "titolo": "L'overtourism fra tiktok e classismo",
  "testo": "\nSi comincia a parlare sempre più di overtourism, ovvero di città piene di turisti in cui la qualità della vita residenti peggiora in continuazione. <br>\nVarie forme di protesta: i barcelloneti che sparano con pistole ad acqua contro ignari famiglie in vacanza, sticker più o meno minacciosi sui locker per le chiavi, manifestazioni di piazza. Le prime risposte: limitazione di airbnb in certe città (a Parigi da un po’), rimozione dei locker a Roma, ticket di ingresso a Venezia. <br>\n<br>\nCome sempre però protestare non ci esime dal capire; da dove viene tutto questo; che alternative realistiche ci sono. <br>\nUn esempio utile.<br>\nGli Unni di Roccaraso hanno cominciato la loro invasione dopo aver visto il video di una tiktoker napoletana. Subito cori sdegnati. Sporcano, inquinano e non spendono. Qui sono tre le cose importanti: gli Unni, tiktokt e la spesa.<br>\nLa prima e l’ultima sono la stessa. Volendo si può risalire fino al grand tour, inizio del passaggio da viaggio a turismo. Ci si sposta per guardare, non per fare altro e ci si sposta in luoghi conosciuti. I ricchi inglesi di buona cultura vanno a scoprire le bellezze europee. Saltando un po' possiamo guardare la seconda metà del ‘900. Nasce la villeggiatura al mare e con essa il turismo di massa. <br>\nI viaggi sono ancora interni, quelli all’estero non sono così semplici e sono cari. Non esistono le compagnie low cost, ci vuole il passaporto e sei quasi obbligato all’hotel. Comunque ci si comincia a muovere. Si spende tanto e si è relativamente pochi.<br>\nPoi Easyjet, Rynair, Airbnb e tutto esplode. Sono arrivati gli Unni. Quegli esseri spregevoli che non guadagnano abbastanza da poter andare in hotel e soggiornano in appartamenti arredati mondo convenienza (quando va bene Ikea). Le entrate per le città aumentano, le entrate per i privati aumentano. Tutti partecipano al gioco: le low cost si fanno pagare dagli aereoporti, gli aereoporti dalle città, i prezzi degli immobili salgono, i ristoranti fanno baldoria. C'è un ma: ci sono più soldi ma cala drasticamente la spesa media per turista. A un certo punto la macchina comincia ad incepparsi. Più persone significa anche più disagi, più infrastrutture da mantenere, vie più intasate, spazi pubblici dedicati esclusivamente ai visitatori. E se le persone aggiuntive portano sempre meno denaro ma gli stessi disagi, le persone aggiuntive piacciono sempre meno. Roccaraso è il caso perfetto. Si arriva con dei bus pagati a Napoli, si consuma se va bene una cioccolata calda, non si dorme li e la maggior parte delle persone non sa sciare e quindi non comprerà lo skipass. Gli Unni di Roccaraso diventano Unni, ovvero barbari da ricacciare indietro, magari armati dalle pistole ad acqua giunte da Barcellona. Dietro alle motivazioni di facciata (problemi logistici, problemi ambientali, etc.) c’è l’unica e vera: non spendono. Il problema è quello, il più grave. Il turista è ben accetto finché spende. Ci ritorniamo. <br>\nMa intanto, tiktok. Migliaia di persone solo per qualche video. Alle cinque terre questa estate mi si avvicina un americano e mi chiede 'ma dov’è il punto della foto?'. Avrei dovuto sapere quale foto, era evidente. Ricordo bene che non mi ha detto delle foto o della foto famosa. Stava pensando proprio a una. Riomaggiore era quella foto. Eravamo in un punto un po’ isolato - si ce ne sono anche lì - con solo ragazzetti del posto, il sole era alto e il mare stupendo. Ma non bastava, l’importante è cercare il punto della foto, ovvero riconettersi con l'idea che ci ha spinti fin là, non connettersi col posto.  <br>\nI luoghi diversi lontani non sono mai esisti in quanto tali ma sono sempre stati mediati dalla narrazione - ricordate il grand tour: non erano altro che intelletuali che avevano una fantasia guidata dai classici greci e latini che avevano letto. Ora però questa narrazione è pervasiva, monopolizzante e esplicita. Il che vuole dire, cominciando dal fondo: i luoghi ci sono presenti con immagini o reels e quindi perfettamente chiari, senza le sfumature che lasciavano i libri, le leggende o i racconti di amici. Queste immagini sono poi poche; anche quando ci vengono proposte da fonti diverse. Abbiamo sempre la stessa cascata presa dalla stessa inquadratura, lo stesso tuffo, lo stesso piatto di carbonara coi granelli di pistacchio. Si potrebbe quasi immaginare un'app per il telefono che scatti in automatico quando il gps riconosce che siamo arrivati nel punto instagrammabile (un'altra volta approfondiremo come i luoghi si trasformino per facilitare questo aspetto). Infine la narrazione è pervasiva, ovvero ne siamo martellati costringendoci a pensare sempre agli stessi luoghi e sempre nello stesso modo. TikTok e Instagram sono il veicolo di tutte le fantasie contemporanee (non c’è la pornografia ma ci sono infiniti corpi semi nudi quindi basta anche per quello). E i social -oggi molto più di ieri- non vivono di mille interazioni e mille post ma di un milione di interazioni sotto la foto divenuta casualmente virale. I luoghi da visitare non sono quindi mille, ma uno. E quel luogo straborderà di turisti. Quindi, l’overtourismo è la reazione perfettamente naturale al nostro modo di veicolare il desiderio. Pochi luoghi, constantemente proposti in maniera univoca e riduttiva. Da qualche parte ho letto che il 90% dei turisti visita il 10% delle ‘attrazioni’ (parola su cui già si potrebbe discutere). E ne avete prova immediata se a Venezia seguite il serpentone che si snoda dalla stazione a San Marco. Se, folli, osate distaccarvi per prendere una via laterale vi troverete in pochi metri da soli. <br>\n<br>\nAbbiamo il mix perfetto: siamo bombardati di contenuti che ci fanno vedere sempre gli stessi pochi luoghi meravigliosi a cui vogliamo arrivare solo per far una foto, viaggiare costa sempre meno e ci sono miliardi di persone pronte a poterselo permettere. Perchè siamo solo all'inizio, 300 milioni di americani non sono nulla di fronte all'uscita dalla povertà di 3 miliardi di cinesi e indiani.<br>\nCapito questo: aboliamo airbnb, facciamo tornare gli Unni ticktoccheggianti delle loro case di periferia e restiamo noi intenditori nei nostri hotel con la nostra guida Routard pronta all’uso. Finalmente. Ma chi ci da il diritto di fare ciò? Dopo che i ricchi occidentali hanno visitato il mondo siamo pronti a chiuderlo agli occidentali poveri, a non occidentali meno che ricchissimi? Faremo come con l’ambiente  che abbiamo inquinato a destra e manco per due secoli per poi pontificare negli ultimi vent'anni sugli indiani cattivi che riempiono di plastica l’oceano?<br>\nLa tentazione c’è, perchè è più facile trovare una soluzione esteticamente piacevole che dire che forse non una soluzione etica che tenga. Tutti vorranno visitare Roma e Venezia o quel nuovo spot che hanno visto online. <br>\nImpediamogli di arrivare, togliamo airbnb. Impediamogli di desiderare, togliamogli i social. Oppure facciamo dei centri di educazione di massa per costringere tutti a promuovere un turismo consapevole. Fate voi, se riuscite. Ma i termini del gioco sono questi e non ci sono soluzioni che non sappiano di un inguaribile snobismo.",
  "id": "67b9b376002a82708b45",
  "sequence": 1,
  "createdAt": "2025-02-22T11:22:30.798+00:00",
  "updatedAt": "2025-05-22T22:17:16.033+00:00",
  "permissions": [],
  "tags": [
  ],
  "databaseId": "67b9b2060006cbdb292d",
  "tableId": "67b9b23a00059abb3c7d"
}
        
    ]

@app.get("/blog")
def get_blog():
    return BLOG_POSTS

@app.get("/blog/{post_id}")
def get_blog_post(post_id: str):
    for post in BLOG_POSTS:
        if post["id"] == post_id:
            return post
    return {"error": "Articolo non trovato"}  # Niente eccezione

PRODOTTI=[
        {
  "url": f"{URL_BASE}/static/prodotti_impossibili/image-2",
  "Descrizione": "Anche nelle nostre società 'libere' milioni di telecamere ci osservano ogni giorno<br>\nCon l'AI è possibile facilmente analizzare volti e risalire a tutti i tuoi dati. <br>\nVari ricercatori hanno immaginato vestiti che confondono l'algoritmo con pattern particolari. Potete trovarne  un esempio <a href=\"https://antiai.biz\" target=\"_blank\">qui</a> o <a href=\" https://makerfairerome.eu/it/cap-able-abiti-anti-sorveglianza-contro-il-riconoscimento-facciale/\" target=\"_blank\">qui</a>.<br>  Noi abbiamo provato a immaginarne un po' meno tripping, anche se probabilmente non funzionante.",
  "id": "6841960a00107c2365c1",
  "sequence": 3,
  "createdAt": "2025-06-05T13:05:14.349+00:00",
  "updatedAt": "2025-06-05T13:19:38.429+00:00",
  "permissions": [],
  "databaseId": "6841614a001d274615f5",
  "tableId": "68416150002c1447e069"
}, 
         {
  "url": f"{URL_BASE}/static/prodotti_impossibili/image-3",
  "Descrizione": "Il nostro collare per proteste ti permette di riprendere costantemente quello che sta accadendo, proteggendo te e le persone che ti circondano da comportamenti eccessivi delle forze dell'ordine. <br>\nIl collare è dotato di memoria e funzionalità di trasmissione real time delle immagini a multipli ricevitori via wifi e connessione dati. Fino a 10h di ripresa ininterrotta. <br>\nIl collare è rimovibile solo con una chiave specifica ed è interamente realizzato in carbonio per garantire resistenza e un'indossabilità ottimale.",
  "id": "6841723500324900e357",
  "sequence": 2,
  "createdAt": "2025-06-05T10:32:21.953+00:00",
  "updatedAt": "2025-06-05T10:33:47.445+00:00",
  "permissions": [],
  "databaseId": "6841614a001d274615f5",
  "tableId": "68416150002c1447e069"
},
        {
  "url": f"{URL_BASE}/static/prodotti_impossibili/image-4",
  "Descrizione": "Con la nostra nuova zanzariera di Faraday* potrete evitare zanzare e notifiche con grande semplicità, creando uno spazio e un tempo di qualità assieme al vostro partner.\n<br>\n*Una gabbia di Faraday è una rete metallica che non permettere alle onde elettromagnetiche di passare, impedendo qualsiasi connessione di rete.",
  "id": "6841633600289652fb23",
  "sequence": 1,
  "createdAt": "2025-06-05T09:28:22.749+00:00",
  "updatedAt": "2025-06-05T10:00:39.531+00:00",
  "permissions": [],
  "databaseId": "6841614a001d274615f5",
  "tableId": "68416150002c1447e069"
}

        
    ]

PUBBLICITA=[{
  "description": "La vera felicità",
  "url": f"{URL_BASE}/static/pubblicita/torte.jpeg",
  "id": "6899cddf00311ae54a04",
  "sequence": 13,
  "createdAt": "2025-08-11T11:02:56.031+00:00",
  "updatedAt": "2025-08-11T11:02:56.031+00:00",
  "permissions": [],
  "databaseId": "67ce05fd003b3c7b6b37",
  "tableId": "67ce12a90008bc9b3aaf"
}
,
{
  "description": "La vera magia ",
  "url": f"{URL_BASE}/static/prodotti_impossibili/coca.jpeg",
  "id": "6899cd9b00014ac531ee",
  "sequence": 12,
  "createdAt": "2025-08-11T11:01:47.301+00:00",
  "updatedAt": "2025-08-11T11:01:47.301+00:00",
  "permissions": [],
  "databaseId": "67ce05fd003b3c7b6b37",
  "tableId": "67ce12a90008bc9b3aaf"
},
{
  "description": "Schiscietta anticapitalistica...da comprare per sentirsi ribelli",
   "url": f"{URL_BASE}/static/prodotti_impossibili/Schiscetta.PNG",
    "id": "685c053d0024bf59d6de",
  "sequence": 11,
  "createdAt": "2025-06-25T14:18:37.688+00:00",
  "updatedAt": "2025-06-25T14:18:37.688+00:00",
  "permissions": [],
  "databaseId": "67ce05fd003b3c7b6b37",
  "tableId": "67ce12a90008bc9b3aaf"
},
{
  "description": "Rivelate il vostro potenziale",
    "url": f"{URL_BASE}/static/prodotti_impossibili/occhiali.png",
"id": "6839c3b60022cad14313",
  "sequence": 10,
  "createdAt": "2025-05-30T14:41:58.854+00:00",
  "updatedAt": "2025-05-30T14:41:58.854+00:00",
  "permissions": [],
  "databaseId": "67ce05fd003b3c7b6b37",
  "tableId": "67ce12a90008bc9b3aaf"
},
{
  "description": "Buy now!!!!!!!!!!!!!!!!!!!!",
    "url": f"{URL_BASE}/static/prodotti_impossibili/crocere.png",
"id": "683051da00325372d481",
  "sequence": 9,
  "createdAt": "2025-05-23T10:45:46.946+00:00",
  "updatedAt": "2025-05-23T10:45:46.946+00:00",
  "permissions": [],
  "databaseId": "67ce05fd003b3c7b6b37",
  "tableId": "67ce12a90008bc9b3aaf"
},
{
  "description": "Il vero motivo per cui viaggiare",
    "url": f"{URL_BASE}/static/prodotti_impossibili/selfie.png",
"id": "682f8a2f0038c1917855",
  "sequence": 8,
  "createdAt": "2025-05-22T20:33:52.000+00:00",
  "updatedAt": "2025-05-23T10:46:46.062+00:00",
  "permissions": [],
  "databaseId": "67ce05fd003b3c7b6b37",
  "tableId": "67ce12a90008bc9b3aaf"
},
{
  "description": "La vita è un'attrazione (a pagamento) indimenticabile",
   "url": f"{URL_BASE}/static/prodotti_impossibili/indimenticabile.png",
 "id": "682f89ca003716a1a1eb",
  "sequence": 7,
  "createdAt": "2025-05-22T20:32:10.993+00:00",
  "updatedAt": "2025-05-22T20:32:10.993+00:00",
  "permissions": [],
  "databaseId": "67ce05fd003b3c7b6b37",
  "tableId": "67ce12a90008bc9b3aaf"
},
,
{
  "description": "Be social",
    "url": f"{URL_BASE}/static/prodotti_impossibili/be_social.jpreg",
"id": "682b0bce003e0187214a",
  "sequence": 5,
  "createdAt": "2025-05-19T10:45:35.076+00:00",
  "updatedAt": "2025-05-19T10:45:35.076+00:00",
  "permissions": [],
  "databaseId": "67ce05fd003b3c7b6b37",
  "tableId": "67ce12a90008bc9b3aaf"
},
{
  "description": "Purezza",
    "url": f"{URL_BASE}/static/prodotti_impossibili/shell.jpeg",
"id": "682b0bc3000079cc540c",
  "sequence": 4,
  "createdAt": "2025-05-19T10:45:23.072+00:00",
  "updatedAt": "2025-05-19T10:45:23.072+00:00",
  "permissions": [],
  "databaseId": "67ce05fd003b3c7b6b37",
  "tableId": "67ce12a90008bc9b3aaf"
},
{
  "description": "Felicità in vendita",
    "url": f"{URL_BASE}/static/prodotti_impossibili/felicita_vestiti.jpeg",
"Created": null,
  "id": "682b0bab002f697393fc",
  "sequence": 3,
  "createdAt": "2025-05-19T10:44:59.831+00:00",
  "updatedAt": "2025-05-19T10:44:59.831+00:00",
  "permissions": [],
  "databaseId": "67ce05fd003b3c7b6b37",
  "tableId": "67ce12a90008bc9b3aaf"
},
{
  "description": "Felicità in vendita",
    "url": f"{URL_BASE}/static/prodotti_impossibili/pizza_felicita.jpeg",
"Created": null,
  "id": "682b0bab002f697393fc",
  "sequence": 3,
  "createdAt": "2025-05-19T10:44:59.831+00:00",
  "updatedAt": "2025-05-19T10:44:59.831+00:00",
  "permissions": [],
  "databaseId": "67ce05fd003b3c7b6b37",
  "tableId": "67ce12a90008bc9b3aaf"
},
{
  "description": "Perchè dovete mangiare",
    "url": f"{URL_BASE}/static/prodotti_impossibili/snack.jpeg",
"Created": null,
  "id": "682b0b9b0038c677658d",
  "sequence": 2,
  "createdAt": "2025-05-19T10:44:43.990+00:00",
  "updatedAt": "2025-05-19T10:44:43.990+00:00",
  "permissions": [],
  "databaseId": "67ce05fd003b3c7b6b37",
  "tableId": "67ce12a90008bc9b3aaf"
}

]

@app.get("/prodotti")
def get_prodotti():
    return PRODOTTI

@app.get("/pubblicita")
def get_prodotti():
    return PUBBLICITA
