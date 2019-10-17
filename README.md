# PYPILINE

## Instalação

        pip instal pypiline
        
## Utilização

### Encadeando tarefas

Com pypeline você consegue encadear tarefas. Cada tarefa retorna seu resultado para a próxima tarefa.


            +---------------------------------------------+
            | Pipeline                                    |
            |                                             |
            | +--------------+         +--------------+   |
            | |              |         |              |   |
            | |   Tarefa 1   +-------->+   Tarefa 2   |   |
            | |              |         |              |   |
            | +--------------+         +--------------+   |
            +---------------------------------------------+

Exemplo:

        pipeline = Pypeline().append(
            math.pow, 2, 2
        ).append(
            operator.add, 5
        )
        pipeline.do()  # output: 9 -> add(pow(2**2), 5)

### Encadear pipelines
Você também pode encadear pipelines (O resultado da pipeline não é repassado para outra pipeline):

            +---------------------------------------------+
            | Pipeline                                    |
            |                                             |
            | +--------------+         +--------------+   |
            | |              |         |              |   |
            | |   Tarefa 1   +-------->+   Tarefa 2   |   |
            | |              |         |              |   |
            | +--------------+         +--------------+   |
            +----------------------+----------------------+
                                   |
                                   |
                                   |
                                   |
                                   v
            +----------------------+----------------------+
            | Pipeline                                    |
            |                                             |
            | +--------------+         +--------------+   |
            | |              |         |              |   |
            | |   Tarefa 1   +-------->+   Tarefa 2   |   |
            | |              |         |              |   |
            | +--------------+         +--------------+   |
            +---------------------------------------------+

Exemplo:

            sub_pipeline = Pypeline().append(
                do_something, 'first', 'second', third='third'
            ).append(
                do_something, something_else=True
            )
            pipeline = Pypeline().append_context(
                sub_pipeline
            ).append_context(
                sub_pipeline
            )
            sub_pipeline.do()

