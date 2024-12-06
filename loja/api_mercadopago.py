import mercadopago
from .chaves import public_key, token


def criar_pagamento(itens_pedido, link):
    sdk = mercadopago.SDK(token)

    # itens da compra no formato de dicionário
    itens = []
    for item in itens_pedido:
        quantidade = int(item.quantidade)
        nome_produto = item.item_estoque.produto.nome
        preco_unitario = float(item.item_estoque.produto.preco)
        itens.append({
            'title': nome_produto,
            'quantity': quantidade,
            'unit_price': preco_unitario,
        })

    preference_data = {
        'items': itens,
        'auto-return': 'all',
        'back_urls': {
            'success': link,
            'pending': link,
            'failure': link,
        }
    }

    resposta = sdk.preference().create(preference_data)
    link_pagamento = resposta['response']['init_point']
    id_pagamento = resposta['response']['id']
    return link_pagamento, id_pagamento
