def traverse(node):
    if len(node) == 0:
        return 0
    else:
        return 1 + max([traverse(child) for child in node])

xml = ''.join(input() for _ in range(int(input())))
import xml.etree.ElementTree as etree
tree = etree.ElementTree(etree.fromstring(xml))


print(traverse(tree.getroot()))
