text = 'In informatica, inteligenta artificiala (IA) este inteligenta masinilor, spre deosebire de inteligenta naturala de la oameni si animale. Informatica defineste cercetarea IA ca studiu al \"agentilor inteligenti?(d)\": orice dispozitiv care Isi percepe mediul si efectueaza actiuni care maximizeaza sansa de a-si atinge cu succes obiectivele. Mai exact, Kaplan si Haenlein definesc IA ca fiind \"capacitatea unui sistem de a interpreta corect datele externe, de a Invata din astfel de date si de a folosi ceea ce a Invatat pentru a-si atinge obiective si sarcini specifice printr-o adaptare flexibila\". Termenul \"inteligenta artificiala\" este utilizat colocvial pentru a descrie masinile care imita functiile cognitive pe care le asociaza oamenii cu alte minti umane, cum ar fi \"Invatarea\" si \"rezolvarea problemelor\". Inteligenta artificiala implica dezvoltarea de algoritmi si modele care permit masinilor sa-si perceapa mediul, sa Isi motiveze mediul si sa faca actiuni adecvate pentru a atinge obiective specifice. Acesti algoritmi folosesc volume mari de date si tehnici avansate, cum ar fi Invatarea automata, Invatarea profunda, procesarea limbajului natural si viziunea computerizata.'
length = len(text)
tx1 = ''
tx2 = ''

if length%2 == 0:
    tx1 = text[:length//2].upper().replace(' ', '')
    tx2 = text[length//2:][::-1]
    for ch in ['.', ',', '!', '?']:
        tx2 = tx2.replace(ch, '')
    tx2 = tx2[0].upper() + tx2[1:]
    print(tx1+tx2)
else:
    tx1 = text[:length//2+1].upper().replace(' ', '')
    tx2 = text[length//2+1:][::-1]
    tx2 = tx2[0].upper() + tx2[1:]
    for ch in ['.', ',', '!', '?']:
        tx2 = tx2.replace(ch, '')
    print(tx1+tx2)
