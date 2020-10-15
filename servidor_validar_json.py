def validar_json(dados):
    # Verificar se os campos obrigatórios do JSON constam e são válidos.

    # Verificar se a chave 'medida' consta no JSON.
    if "medida" not in dados:
        # Em caso contrário, retornar 400.
        resposta = {"Erro": "Campo 'medida' inexistente."}
        return resposta, 400
    else:
        # 'medida' existe, agora é preciso verificar se é string.
        if type(dados["medida"]) is not str:
            # Em caso contrário, retornar 400.
            resposta = {"Erro": "Campo 'medida' deve ser string."}
            return resposta, 400

    # Verificar se a chave 'valores' consta no JSON.
    if "valores" not in dados:
        # Em caso contrário, retornar 400.
        resposta = {"Erro": "Campo 'valores' inexistente."}
        return resposta, 400
    else:
        # 'valores' existe, agora é preciso verificar se existe pelo menos
        # 1 par chave-valor.
        if type(dados["valores"]) is not list or len(dados["valores"]) < 1:
            # Em caso contrário, retornar 400.
            resposta = {
                "Erro": "Campo 'valores' deve ser uma lista não vazia."}
            return resposta, 400
if "marcadores" not in dados:
        resposta = {"Erro": "Campo 'marcadores' inexistente."}
        return resposta,400
    else:
        for item in dados["marcadores"]:
            for chave, valor in item.itens():
                if chave.lower() == "url":
                    url_de_teste = valor
                    
        if url_de_teste:
            req = get(url_de_teste)
            if req.status_code >= 200 and req.status_code <= 399:
                resposta = {"Sucesso": "URL válida"}
                return resposta, 200
    # Se todas as verificações foram feitas, retornar 200.
    resposta = {"Sucesso": "JSON válido."}
    return resposta, 200
