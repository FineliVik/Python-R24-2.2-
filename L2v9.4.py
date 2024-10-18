import xml.dom.minidom as minidom

# №4 Распарсить файл и извлечь данные, согласно варианту. Выполнить приведения типов по необходимости.
# (Два отдельных списка NumCode и CharCode)

xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

currency_dict_NumCode = []
currency_dict_CharCode = []

dom = minidom.parseString(xml_data)
elements = dom.getElementsByTagName('Valute')

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'NumCode':
                if child.firstChild.nodeType == 3:
                    currency_dict_NumCode.append(child.firstChild.data)
            if child.tagName == 'CharCode':
                if child.firstChild.nodeType == 3: # проверка текстовая ли информация
                    currency_dict_CharCode.append(child.firstChild.data)

print(f'Элементы списка currency_dict_NumCode: {currency_dict_NumCode}')
print(f'Элементы списка currency_dict_CharCode: {currency_dict_CharCode}')
xml_file.close()
