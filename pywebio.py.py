
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
sorular = {
    1:{
        "soru":"türkiyenin başkenti hangisidir",
        "cevaplar":{"Ankara","istanbul","izmir","osmaniye"},
        "yanıt":"Ankara"
    
    },

    2:{
        "soru":"almanyanın başkenti hangisidir",
        "cevaplar":{"münih","berlin","izmir","osmaniye"},
        "yanıt":"berlin"
    },

    3: {
        "soru":"fransanın başkenti hangisidir",
        "cevaplar":{"berlin","maldova","paris","osmaniye"},
        "yanıt":"paris"
    
    }
}



def soru(soru_no):
    puan = 0
    soru_metni = sorular[soru_no]["soru"]
    with use_scope("soru_scope", clear = True):
        put_text(soru_metni)
    cevaplar = sorular[soru_no]["cevaplar"]
    cevap = radio("choose one", options=cevaplar)
    dogru_yanıt = sorular[soru_no]["yanıt"]
    if cevap == dogru_yanıt:
        popup("tebrikler doğru cevap")
        puan = 10
    else: 
        popup("üzgünüm yanlış cevap tekrar deneyin")

    return puan

def main():
    puanlar = 0
    for i in range(1,4):
        puanlar+=soru(i)
    with use_scope("soru_scope", clear = True):
        put_text("toplam puanınız = %r" % puanlar)



main()