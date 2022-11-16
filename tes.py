import streamlit as st

translate = {
    'saya': 'beta', 'kamu': 'lu',
    'kalian': 'basong', 'bagaimana': 'karmana',
    'gimana': 'karmana', 'mereka': 'dong',
    'uang': 'doi', 'bersih': 'barisi',
    'kotor': 'dadolek', 'buat': 'bikin',
    'bapak': 'baptua', 'pacar': 'baitua',
    'mama': 'mamtua', 'pacar': 'maitua',
    'perempuan': 'nona', 'laki-laki': 'nyong',
    'pergi': 'pi', 'dengan': 'deng',
    'sudah': 'su', 'punya': 'pung',
    'siapa': 'sapa', 'mau': 'mo',
    'jangan': 'jang', 'coba': 'co',
    'lagi': 'lai', 'angkat': 'angka',
    'ikut': 'iko', 'malas': 'pamokol',
    'jalan-jalan': "tapale'uk", 'keren': 'kembo',
    'pelit': "kake'ek", 'bodoh': 'ngali',
    'lebai': 'lebe', 'tidak peduli': 'tasibu',
    'berbunyi': 'babunyi', 'mensucikan': 'kas barisi',
    'bersaudara': 'basodara', 'bercerita': 'bacarita',
    'seperti': "ba'iko"
}

bahasa = st.radio('Asal Bahasa :', ('Kupang', 'Indonesia'))
l_kata = []

text = st.text_input(f'Bahasa {bahasa} : ', '').lower().split()

if bahasa == 'Indonesia':
    for i in text:
        if i in translate.keys():
            l_kata.append(translate[i])
        else:
            l_kata.append(i)

    # print(' '.join(l_kata))
    st.write('Hasil translate ke Bahasa Kupang :')
    st.write(' '.join(l_kata))

elif bahasa == 'Kupang':
    key_list = list(translate.keys())
    value_list = list(translate.values())

    for i in text:
        if i in value_list:
            l_kata.append(key_list[value_list.index(i)])
        else:
            l_kata.append(i)

    st.write('Hasil translate ke Bahasa Indonesia :')
    st.write(' '.join(l_kata))
