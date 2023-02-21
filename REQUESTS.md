# Contexto geral da Pizzaria para a modelagem geral (DER)  do banco de dados relacional

Para a atividade individual vamos considerar a pizzaria completa, conforme o contexto discutido em sala.

Para o trabalho final, com a implementação do pequeno programa em equipes, ficaremos apenas com o cadastro do cliente e encomenda de um pedido (pizzas + bebidas).

Lembrando dos detalhes do contexto alinhado:

Tamanhos:

- Pequena, 1 sabor
- Média, até 2 sabores
- Grande, até 3 sabores

Sabores:

- Tradicionais
- Especiais
- Possuem preços diferentes conforme o sabor e o tamanho, o banco armazena um pequena descrição de cada sabor.

Bordas:

- sem borda
- borda requeijão
- borda de chocolate

As bordas adicionam um taxa extra em cada pizza (pode ser fixa ou variável por tamanho)

Bebidas, apenas:

- refrigerantes
- cervejas

Considerar as informações do entregador (quem é o colaborador que está levando o pedido) e o custo de entrega (pode ser fixo).

Quanto ao cliente, os dados pessoais básicos e seu endereço de entrega (o ideal é considerar que pode ter vários endereços de entrega). Neste sentido cada pedido poderia se entregue em um lugar diferente, mesmo sendo proveniente do mesmo cliente.

Outras situações podem ser adicionadas pela equipe, sem problemas se considerar um cenário mais complexo e/ou com outros requisitos.

Várias ferramentas podem ser usar (ver postagem mais acima), o importante é procurar criar seu modelo, usando os conceitos de integridade referencial já vistos (trabalho individual), e depois alinhar com a dupla como fica o BD que será usado para o trabalho (prático feito em duplas).

No trabalho final a maioria dos dados podem ser inserido no BD manualmente, o programa apenas terá as funções de cadastrar cliente e fazer pedidos (ou seja, a maioria das tabelas serão apenas consultadas).
