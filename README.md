# Repositório de Projetos em Python com OpenCV

Esse é o meu primeiro repositório de projetos em Python utilizando o OpenCV! Este repositório contém quatro diferentes projetos que exploram as funcionalidades básicas do OpenCV para processamento de imagens e visão computacional.

## Projetos

### Projeto 1: Detecção de Movimento de Carros

Neste projeto, utilizando contornos e ferramentas mais simples e primitivas do OpenCV, é feita uma detecção do movimento dos carros em vídeos de tráfego. O objetivo principal é identificar os carros que estão em movimento nas cenas capturadas pelas câmeras de vigilância e rastreá-los ao longo do tempo.

### Projeto 2: Detecção de Rosto Frontal

Este projeto utiliza um arquivo XML de modelo pré-treinado chamado `haarcascade_frontalface_default.xml` fornecido pelo OpenCV para realizar a detecção simples de rostos de frente em imagens e vídeos. O objetivo é identificar e delimitar rostos de pessoas voltados para a câmera.

### Projeto 3: Desfoque de Rostos Detectados

Neste projeto, é utilizado o modelo `haarcascade_frontalface_default.xml` para detectar rostos em imagens e aplicar um efeito de desfoque (blurr) na região do rosto detectado. O objetivo é preservar a privacidade das pessoas ao desfocar suas faces em fotos e vídeos.

### Projeto 4: Detecção de Rostos Específicos

No Projeto 4, é utilizado o modelo `haarcascade_frontalface_default.xml` em conjunto com um método simples de treinamento para realizar a detecção do rosto específico da cantora Avril Lavigne em imagens e vídeos. O objetivo é identificar e delimitar o rosto da cantora nas cenas em que ela aparece.

## Utilizando os Projetos

Para utilizar cada projeto, siga as instruções presentes em suas respectivas pastas, contidas neste repositório. Certifique-se de ter o Python e o OpenCV instalados em seu ambiente antes de executar os projetos.

**Nota importante:** Todos os projetos são projetados para fechar a janela de exibição das imagens ou vídeos ao pressionar a tecla "q". Portanto, para encerrar a execução de qualquer projeto, basta pressionar a tecla "q" enquanto a janela estiver em foco.
