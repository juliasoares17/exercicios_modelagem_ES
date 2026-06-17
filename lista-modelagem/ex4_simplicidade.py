class Pedido:
    _FLUXO_PERMITIDO = ["PENDENTE", "PROCESSANDO", "ENVIADO", "ENTREGUE"]

    def __init__(self, id_pedido: int):
        self.id_pedido = id_pedido
        self._status = self._FLUXO_PERMITIDO[0]

    @property
    def status(self) -> str:
        return self._status

    def atualizar_status(self, novo_status: str):
        if novo_status not in self._FLUXO_PERMITIDO:
            raise ValueError(f"Estado de andamento inválido: {novo_status}")
        
        indice_atual = self._FLUXO_PERMITIDO.index(self._status)
        indice_novo = self._FLUXO_PERMITIDO.index(novo_status)
        
        if indice_novo <= indice_atual:
            raise ValueError("Violação estrutural: O fluxo do pedido não pode retroceder.")
            
        self._status = novo_status
