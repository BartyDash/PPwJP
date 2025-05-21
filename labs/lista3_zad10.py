text = """Trzeba być zawsze tylko sobą. Koń bez ułana jest
zawsze koniem. Ułan bez konia tylko człowiekiem."""

text = text.lower().replace('.', '').replace('\n', '')

words = text.split()

word_dict = {
    word: {'count': words.count(word), 'length': len(word)}
    for word in set(words)
}

filtered_dict = {
    word: info for word, info in word_dict.items()
    if not (info['count'] == 1 and info['length'] < 5)
}

sorted_dict = dict(
    sorted(filtered_dict.items(), key=lambda item: item[1]['length'], reverse=True)
)

for word, info in sorted_dict.items():
    print(f"{word}: {info}")
