<a href="https://kich.dev.br"><img src="assets/header-pt.svg" width="100%" alt="Otávio Kich Mata. Uma sala em pixel art onde uma capivara e um quero-quero ficam ao lado de uma TV antiga que vive trocando de canal"></a>

<p align="center"><a href="https://github.com/tavmata">English</a> · <b>Português</b></p>

Estudo Relações Internacionais na Universidade Federal de Santa Catarina (UFSC), em Florianópolis, e pesquiso migração e direito internacional. Também construo jogos, painéis de dados e fluxos de trabalho com IA. Não venho da computação: quase tudo o que está aqui eu fiz coordenando agentes de código.

<p align="center">
<a href="https://mmorpg.kich.dev.br"><b>Jogar Kapi Online</b></a> ·
<a href="https://tavmata.github.io/painel-sul-sul-sismigra/">Painel de migração</a> ·
<a href="https://kich.dev.br">kich.dev.br</a> ·
<a href="https://otaviokmkm.itch.io">itch.io</a> ·
<a href="https://www.linkedin.com/in/ot%C3%A1vio-kich-mata-70b78b212/">LinkedIn</a> ·
<a href="https://lattes.cnpq.br/4797477996223695">Lattes</a>
</p>

## Ao vivo

<img src="https://raw.githubusercontent.com/tavmata/tavmata/output/capybara-pt.svg" width="100%" alt="Minhas contribuições no GitHub dos últimos 12 meses desenhadas como um campo de pinhões, com a capivara da sala atravessando e comendo, mais o total e as minhas sequências atual e recorde">

<sub>Uma GitHub Action redesenha isto toda manhã a partir do meu calendário público de contribuições.</sub>

## Programação de hoje

Esta página segue [o meu site](https://kich.dev.br): cada seção é um canal de TV desenhado num estilo diferente. Abra um para sintonizar.

<details open>
<summary><code>CH 01</code> Sala · role os dados do War contra a capivara</summary>
<br>

<a href="https://github.com/tavmata/tavmata/issues/new?title=war%7Croll&body=Clique%20em%20Create%20para%20rolar%20o%20dado%20vermelho%20contra%20a%20capivara.%20O%20resultado%20aparece%20em%20github.com%2Ftavmata%20em%20cerca%20de%20um%20minuto."><img src="assets/dice-pt.svg?v=1" width="100%" alt="Dados de War: o seu dado vermelho contra o dado amarelo da capivara, com o placar até agora"></a>

<!-- dice:start -->
Visitantes 0, capivara 1, depois de 1 rolagem. As últimas:

| Jogador | Ataque | Defesa | Resultado |
| :-- | :-: | :-: | :-- |
| [tavmata](https://github.com/tavmata) | 2 | 4 | a defesa segura |
<!-- dice:end -->

[Role o dado vermelho](https://github.com/tavmata/tavmata/issues/new?title=war%7Croll&body=Clique%20em%20Create%20para%20rolar%20o%20dado%20vermelho%20contra%20a%20capivara.%20O%20resultado%20aparece%20em%20github.com%2Ftavmata%20em%20cerca%20de%20um%20minuto.). Você ataca, a capivara defende com o dado amarelo, e empate fica com a defesa, como no War. O link abre uma issue neste repositório, e uma GitHub Action rola os dois dados, coloca o resultado aqui e fecha a issue, em geral em menos de um minuto. Precisa de uma conta no GitHub, e cada jogador rola uma vez a cada 10 minutos.

<sub><a href="https://kich.dev.br/#sala">CH 01 no kich.dev.br</a>, onde os dados rolam com um clique e sem conta</sub>
</details>

<details open>
<summary><code>CH 02</code> Kapi Online · o MMORPG que faço com agentes de código</summary>
<br>

<a href="https://mmorpg.kich.dev.br"><img src="assets/kapi-cover.jpg" width="100%" alt="Capa do Kapi Online: um grupo de heróis enfrenta um dragão vermelho numa caverna, embaixo do logo de pedra do jogo"></a>

<table>
<tr>
<td width="33%"><a href="https://mmorpg.kich.dev.br"><img src="assets/kapi-raid.gif" width="100%" alt="Uma raid: uns doze jogadores lutando juntos numa passarela de madeira à beira da água"></a></td>
<td width="33%"><a href="https://mmorpg.kich.dev.br"><img src="assets/kapi-void.gif" width="100%" alt="Luta contra um chefe, um olho roxo gigante com tentáculos, na Dimensão do Vazio"></a></td>
<td width="33%"><a href="https://mmorpg.kich.dev.br"><img src="assets/kapi-bard.gif" width="100%" alt="Um bardo toca o Acorde Final numa estrada da floresta"></a></td>
</tr>
<tr>
<td align="center"><sub>Raid</sub></td>
<td align="center"><sub>Dimensão do Vazio</sub></td>
<td align="center"><sub>O Acorde Final do bardo</sub></td>
</tr>
</table>

O Kapi Online é um MMORPG em 2D feito para jogar em grupo: cinco classes, masmorras com chefes, guildas e um mercado entre jogadores. Uma estátua transforma tempo real de estudo em progresso no jogo, e uma IA lê o que você estudou e devolve uma dica e um próximo passo, como um professor faria. A arte é desenhada em código.

- Um servidor em Node.js decide cada ação, 30 vezes por segundo, e foi feito para aguentar 1.000 jogadores.
- O cliente 2D roda no computador e no celular. Também existe uma versão 3D jogável no Godot.
- O repositório recebeu 2.630 commits entre 28 de julho e 25 de novembro de 2026: 922 meus, 865 de agentes de IA e 843 automáticos do GitHub Actions.

Abre no navegador, sem instalar nada: [mmorpg.kich.dev.br](https://mmorpg.kich.dev.br)

<sub><a href="https://kich.dev.br/#kapi">CH 02 no kich.dev.br</a></sub>
</details>

<details>
<summary><code>CH 03</code> Relógio · quem escreve o Kapi Online, hora a hora</summary>
<br>

<img src="assets/clock-pt.svg" width="100%" alt="Um relógio art déco de 24 horas. Cada hora tem uma torre cor de cobre com os meus commits e uma azul com os dos agentes de IA. Meu pico é à meia-noite, com 70 commits, e o dos agentes às 5h, com 149">

As torres azuis são o Jules e os outros agentes de código.

<sub><a href="https://kich.dev.br/#relogio">CH 03 no kich.dev.br</a></sub>
</details>

<details>
<summary><code>CH 04</code> Pesquisa · migração, direitos humanos e direito internacional</summary>
<br>

Pesquiso direito internacional público, políticas migratórias, direitos humanos e constitucionalismo latino-americano.

Meu projeto atual estuda a imigração da Ásia e da África para o Brasil nos microdados do SISMIGRA: quem chega do Sul Global, com qual amparo legal e como entra no mercado de trabalho. O mapa mostra de onde vêm os dez maiores grupos de cada região. Dá para arrastar e dar zoom.

<!-- map:start -->
```geojson
{"type":"FeatureCollection","features":[{"type":"Feature","geometry":{"type":"LineString","coordinates":[[116.4,39.9],[-47.88,-15.79]]},"properties":{"de":"China","registros":"64.990"}},{"type":"Feature","geometry":{"type":"LineString","coordinates":[[120.98,14.6],[-47.88,-15.79]]},"properties":{"de":"Filipinas","registros":"26.271"}},{"type":"Feature","geometry":{"type":"LineString","coordinates":[[77.21,28.61],[-47.88,-15.79]]},"properties":{"de":"Índia","registros":"22.670"}},{"type":"Feature","geometry":{"type":"LineString","coordinates":[[126.98,37.57],[-47.88,-15.79]]},"properties":{"de":"Coreia do Sul","registros":"17.300"}},{"type":"Feature","geometry":{"type":"LineString","coordinates":[[36.29,33.51],[-47.88,-15.79]]},"properties":{"de":"Síria","registros":"8.984"}},{"type":"Feature","geometry":{"type":"LineString","coordinates":[[90.41,23.81],[-47.88,-15.79]]},"properties":{"de":"Bangladesh","registros":"7.797"}},{"type":"Feature","geometry":{"type":"LineString","coordinates":[[69.21,34.56],[-47.88,-15.79]]},"properties":{"de":"Afeganistão","registros":"7.627"}},{"type":"Feature","geometry":{"type":"LineString","coordinates":[[35.5,33.89],[-47.88,-15.79]]},"properties":{"de":"Líbano","registros":"6.973"}},{"type":"Feature","geometry":{"type":"LineString","coordinates":[[106.85,-6.21],[-47.88,-15.79]]},"properties":{"de":"Indonésia","registros":"6.476"}},{"type":"Feature","geometry":{"type":"LineString","coordinates":[[32.86,39.93],[-47.88,-15.79]]},"properties":{"de":"Turquia","registros":"3.385"}},{"type":"Feature","geometry":{"type":"LineString","coordinates":[[13.23,-8.84],[-47.88,-15.79]]},"properties":{"de":"Angola","registros":"33.029"}},{"type":"Feature","geometry":{"type":"LineString","coordinates":[[-17.47,14.72],[-47.88,-15.79]]},"properties":{"de":"Senegal","registros":"10.967"}},{"type":"Feature","geometry":{"type":"LineString","coordinates":[[7.4,9.08],[-47.88,-15.79]]},"properties":{"de":"Nigéria","registros":"8.264"}},{"type":"Feature","geometry":{"type":"LineString","coordinates":[[-15.6,11.86],[-47.88,-15.79]]},"properties":{"de":"Guiné-Bissau","registros":"7.379"}},{"type":"Feature","geometry":{"type":"LineString","coordinates":[[32.57,-25.97],[-47.88,-15.79]]},"properties":{"de":"Moçambique","registros":"6.025"}},{"type":"Feature","geometry":{"type":"LineString","coordinates":[[-6.83,34.02],[-47.88,-15.79]]},"properties":{"de":"Marrocos","registros":"4.821"}},{"type":"Feature","geometry":{"type":"LineString","coordinates":[[-0.19,5.6],[-47.88,-15.79]]},"properties":{"de":"Gana","registros":"4.140"}},{"type":"Feature","geometry":{"type":"LineString","coordinates":[[31.24,30.04],[-47.88,-15.79]]},"properties":{"de":"Egito","registros":"3.474"}},{"type":"Feature","geometry":{"type":"LineString","coordinates":[[-23.51,14.93],[-47.88,-15.79]]},"properties":{"de":"Cabo Verde","registros":"3.143"}},{"type":"Feature","geometry":{"type":"LineString","coordinates":[[15.27,-4.44],[-47.88,-15.79]]},"properties":{"de":"RD Congo","registros":"2.780"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[116.4,39.9]},"properties":{"país":"China","região":"Ásia","registros":"64.990","amparo de trabalho ou investimentos":"42,9%","acolhida humanitária ou refúgio":"4,7%"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[120.98,14.6]},"properties":{"país":"Filipinas","região":"Ásia","registros":"26.271","amparo de trabalho ou investimentos":"93,6%","acolhida humanitária ou refúgio":"1,5%"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[77.21,28.61]},"properties":{"país":"Índia","região":"Ásia","registros":"22.670","amparo de trabalho ou investimentos":"81,9%","acolhida humanitária ou refúgio":"2,2%"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[126.98,37.57]},"properties":{"país":"Coreia do Sul","região":"Ásia","registros":"17.300","amparo de trabalho ou investimentos":"58,9%","acolhida humanitária ou refúgio":"1,0%"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[36.29,33.51]},"properties":{"país":"Síria","região":"Ásia","registros":"8.984","amparo de trabalho ou investimentos":"0,7%","acolhida humanitária ou refúgio":"49,1%"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[90.41,23.81]},"properties":{"país":"Bangladesh","região":"Ásia","registros":"7.797","amparo de trabalho ou investimentos":"23,9%","acolhida humanitária ou refúgio":"19,2%"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[69.21,34.56]},"properties":{"país":"Afeganistão","região":"Ásia","registros":"7.627","amparo de trabalho ou investimentos":"0,2%","acolhida humanitária ou refúgio":"97,8%"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[35.5,33.89]},"properties":{"país":"Líbano","região":"Ásia","registros":"6.973","amparo de trabalho ou investimentos":"3,3%","acolhida humanitária ou refúgio":"25,2%"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[106.85,-6.21]},"properties":{"país":"Indonésia","região":"Ásia","registros":"6.476","amparo de trabalho ou investimentos":"92,6%","acolhida humanitária ou refúgio":"0,3%"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[32.86,39.93]},"properties":{"país":"Turquia","região":"Ásia","registros":"3.385","amparo de trabalho ou investimentos":"32,9%","acolhida humanitária ou refúgio":"7,1%"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[13.23,-8.84]},"properties":{"país":"Angola","região":"África","registros":"33.029","amparo de trabalho ou investimentos":"1,6%","acolhida humanitária ou refúgio":"49,4%"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[-17.47,14.72]},"properties":{"país":"Senegal","região":"África","registros":"10.967","amparo de trabalho ou investimentos":"8,4%","acolhida humanitária ou refúgio":"5,5%"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[7.4,9.08]},"properties":{"país":"Nigéria","região":"África","registros":"8.264","amparo de trabalho ou investimentos":"5,1%","acolhida humanitária ou refúgio":"21,2%"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[-15.6,11.86]},"properties":{"país":"Guiné-Bissau","região":"África","registros":"7.379","amparo de trabalho ou investimentos":"2,3%","acolhida humanitária ou refúgio":"13,7%"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[32.57,-25.97]},"properties":{"país":"Moçambique","região":"África","registros":"6.025","amparo de trabalho ou investimentos":"9,5%","acolhida humanitária ou refúgio":"6,7%"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[-6.83,34.02]},"properties":{"país":"Marrocos","região":"África","registros":"4.821","amparo de trabalho ou investimentos":"4,0%","acolhida humanitária ou refúgio":"54,3%"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[-0.19,5.6]},"properties":{"país":"Gana","região":"África","registros":"4.140","amparo de trabalho ou investimentos":"5,1%","acolhida humanitária ou refúgio":"40,0%"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[31.24,30.04]},"properties":{"país":"Egito","região":"África","registros":"3.474","amparo de trabalho ou investimentos":"13,3%","acolhida humanitária ou refúgio":"15,6%"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[-23.51,14.93]},"properties":{"país":"Cabo Verde","região":"África","registros":"3.143","amparo de trabalho ou investimentos":"2,6%","acolhida humanitária ou refúgio":"4,4%"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[15.27,-4.44]},"properties":{"país":"RD Congo","região":"África","registros":"2.780","amparo de trabalho ou investimentos":"1,5%","acolhida humanitária ou refúgio":"54,2%"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[-47.88,-15.79]},"properties":{"name":"Brasil"}}]}
```
<!-- map:end -->

<details>
<summary>Os números por trás do mapa</summary>
<br>

<!-- table:start -->
| País | Região | Registros | Trabalho ou investimentos | Acolhida humanitária ou refúgio |
| :-- | :-- | --: | --: | --: |
| China | Ásia | 64.990 | 42,9% | 4,7% |
| Angola | África | 33.029 | 1,6% | 49,4% |
| Filipinas | Ásia | 26.271 | 93,6% | 1,5% |
| Índia | Ásia | 22.670 | 81,9% | 2,2% |
| Coreia do Sul | Ásia | 17.300 | 58,9% | 1,0% |
| Senegal | África | 10.967 | 8,4% | 5,5% |
| Síria | Ásia | 8.984 | 0,7% | 49,1% |
| Nigéria | África | 8.264 | 5,1% | 21,2% |
| Bangladesh | Ásia | 7.797 | 23,9% | 19,2% |
| Afeganistão | Ásia | 7.627 | 0,2% | 97,8% |
| Guiné-Bissau | África | 7.379 | 2,3% | 13,7% |
| Líbano | Ásia | 6.973 | 3,3% | 25,2% |
| Indonésia | Ásia | 6.476 | 92,6% | 0,3% |
| Moçambique | África | 6.025 | 9,5% | 6,7% |
| Marrocos | África | 4.821 | 4,0% | 54,3% |
| Gana | África | 4.140 | 5,1% | 40,0% |
| Egito | África | 3.474 | 13,3% | 15,6% |
| Turquia | Ásia | 3.385 | 32,9% | 7,1% |
| Cabo Verde | África | 3.143 | 2,6% | 4,4% |
| RD Congo | África | 2.780 | 1,5% | 54,2% |
<!-- table:end -->

</details>

<sub>Os números contam registros de 2010 a abril de 2026, não pessoas únicas. Sul Global pelo critério da ONU/DESA.</sub>

- Dois artigos publicados (Qualis B3+) sobre educação financeira e tomada de decisão, e um submetido. Também sou coautor de livros, entre eles *Diálogos Impertinentes na Pandemia* (2022).
- Três iniciações científicas (PIBIC e EIRENÈ) sobre constitucionalismo latino-americano e direito internacional, com trabalhos apresentados no ADM 2024, no BELS 2024 e no V SEPERI.
- Tive uma proposta de projeto aprovada para pré-incubação no Sapiens Parque, em Florianópolis.

Mais no meu [Currículo Lattes](https://lattes.cnpq.br/4797477996223695).

<sub><a href="https://kich.dev.br/#pesquisa">CH 04 no kich.dev.br</a></sub>
</details>

<details>
<summary><code>CH 05</code> Passaporte · migrantes, refugiados e a ONU</summary>
<br>

<img src="assets/passport-pt.svg" width="100%" alt="Uma página de passaporte com carimbos: Núcleo de Migração da DPU, Voluntários da ONU no UNRISD, ENAP, UFSCMUN, AUGM e BSAFE">

- Defensoria Pública da União (DPU), Núcleo de Migração, em Florianópolis, de dezembro de 2024 a setembro de 2025. Atendi migrantes, refugiados e solicitantes de refúgio em inglês, espanhol e francês. Redigi peças, requerimentos administrativos e relatórios de regularização migratória, e acompanhei processos com órgãos federais, consulados e serviços de acolhimento.
- Voluntários das Nações Unidas (UNV), no UNRISD, de junho a dezembro de 2024, de forma remota. Pesquisa e engajamento comunitário ligados aos Objetivos de Desenvolvimento Sustentável, com análise de políticas regionais para o Instituto de Pesquisa das Nações Unidas para o Desenvolvimento Social.
- UFSCMUN VII e VIII. Organizei duas edições da simulação da ONU da UFSC e escrevi os guias de estudo e as regras.
- Certificados de segurança em campo BSAFE (UNDSS), da Escola de Inverno AUGM sobre democracia latino-americana (UFABC) e de Direitos dos Imigrantes (ENAP).

Falo português, inglês (C2), espanhol, francês (B2) e o básico de alemão e mandarim.

<sub><a href="https://kich.dev.br/#passaporte">CH 05 no kich.dev.br</a></sub>
</details>

<details>
<summary><code>CH 06</code> Painel · migração Sul-Sul no Brasil, em Power BI</summary>
<br>

<table>
<tr>
<td width="50%"><a href="https://tavmata.github.io/painel-sul-sul-sismigra/"><img src="assets/painel-01-visao-geral.png" width="100%" alt="Página de visão geral do painel: totais, série anual de registros do Sul e do Norte, regiões e principais países"></a></td>
<td width="50%"><a href="https://tavmata.github.io/painel-sul-sul-sismigra/"><img src="assets/painel-06-asia-africa.png" width="100%" alt="Página Ásia e África do painel: indicadores e grupos ocupacionais por sub-região"></a></td>
</tr>
<tr>
<td align="center"><sub>Visão geral</sub></td>
<td align="center"><sub>Ásia e África</sub></td>
</tr>
</table>

Registros de imigrantes do Sul Global no Brasil, de 2010 a abril de 2026, com foco em Ásia e África. Um seletor troca o critério de Sul Global (ONU/DESA ou UNCTAD) em todas as medidas. Dos 2,43 milhões de registros de imigrantes no período, 2.057.430 vêm do Sul Global, e só a Venezuela responde por 39% deles.

Um script em Python gera o arquivo inteiro do Power BI, com tabelas, relações, medidas DAX e páginas. Quando chega dado novo, refaço o painel com um comando.

[Abrir a versão web](https://tavmata.github.io/painel-sul-sul-sismigra/), com as mesmas páginas e filtros · [Código e dados](https://github.com/tavmata/painel-sul-sul-sismigra)

<sub><a href="https://kich.dev.br/#painel">CH 06 no kich.dev.br</a></sub>
</details>

<details>
<summary><code>CH 07</code> Agentes · como trabalho com IA</summary>
<br>

<img src="assets/blueprint-pt.svg" width="100%" alt="Planta do meu fluxo de trabalho: 01 escrevo as regras do projeto, 02 divido o trabalho em tarefas pequenas, 03 os agentes escrevem o código, 04 reviso o que volta, 05 testo antes de publicar, e volta para o 02 na próxima tarefa">

Várias sessões de agentes trabalham ao mesmo tempo no mesmo repositório, cada uma na sua tarefa. Na pesquisa uso o mesmo esquema para tratar microdados, montar painéis por código e transformar leituras em baralhos do Anki.

<sub><a href="https://kich.dev.br/#agentes">CH 07 no kich.dev.br</a></sub>
</details>

<details>
<summary><code>CH 08</code> Fliperama · mais dois jogos, grátis no itch.io</summary>
<br>

<table>
<tr>
<td width="38%" valign="top"><a href="https://otaviokmkm.itch.io/pinball-heroes"><img src="assets/pinball.gif" width="100%" alt="Pinball Heroes: fichas de heróis quicando entre bumpers e portais numa mesa escura de neon"></a></td>
<td width="62%" valign="top"><a href="https://otaviokmkm.itch.io/clair-tactics"><img src="assets/tactics.gif" width="100%" alt="Clair Tactics: uma luta por turnos num tabuleiro 3D na floresta, que termina numa explosão de gelo"></a>
<br><br>
<b><a href="https://otaviokmkm.itch.io/pinball-heroes">Pinball Heroes</a></b><br>
Pinball com RPG. Você lança cada herói na mesa, e bumpers, portais e impulsos mudam a velocidade e o dano. A campanha tem 30 fases.
<br><br>
<b><a href="https://otaviokmkm.itch.io/clair-tactics">Clair Tactics</a></b><br>
RPG tático por turnos num tabuleiro 3D. Você invoca heróis, posiciona o time e acerta o tempo dos golpes e das defesas.
<br><br>
Os dois rodam no navegador e salvam o progresso no seu aparelho.
</td>
</tr>
</table>

<sub><a href="https://kich.dev.br/#fliperama">CH 08 no kich.dev.br</a></sub>
</details>

<details>
<summary><code>CH 09</code> Ficha · o currículo como menu de RPG</summary>
<br>

<a href="https://kich.dev.br/#curriculo"><img src="assets/sheet-pt.svg" width="100%" alt="Uma tela de status de RPG. IAA 9,07, seis idiomas, 922 commits, dois artigos, duas ONUs simuladas, duas menções na OBMEP. Missões concluídas: Núcleo de Migração da DPU, voluntário online da ONU, monitoria e pesquisa no IFSC. Em curso: RI na UFSC, pesquisa Sul-Sul, Kapi Online"></a>

<img src="assets/items-pt.svg" width="100%" alt="A página de itens do menu de RPG, com as minhas ferramentas: Node.js no servidor do jogo, Canvas 2D e WebGL2 na arte, Godot 4 no cliente 3D, MongoDB nos dados dos jogadores, ElevenLabs nas vozes dos NPCs, Python, Power BI com DAX, Playwright, Claude Code e Gemini CLI">


As menções honrosas na OBMEP são de 2017 e 2019, e me formo em dezembro de 2027. O currículo para imprimir está no [kich.dev.br](https://kich.dev.br/#curriculo).

<sub><a href="https://kich.dev.br/#curriculo">CH 09 no kich.dev.br</a></sub>
</details>

<details>
<summary><code>CH 10</code> Cordel · o canal que saiu do ar</summary>
<br>

<table>
<tr>
<td width="40%" valign="top"><img src="assets/cordel.svg" width="100%" alt="Xilogravura de cordel: uma figura sorridente ergue um celular embaixo de um sol grande, com uma multidão de cabeças embaixo"></td>
<td valign="top">
Tive um canal no TikTok sobre educação política que chegou a 5.000 seguidores. Depois apaguei o canal. O site guarda uma nota de rodapé sobre isso, em versos:
<br><br>
<i>Peço licença ao leitor<br>
pra contar minha passagem<br>
por um canal no TikTok<br>
explicando a engrenagem<br>
do governo e da política,<br>
sem enfeite e sem bobagem.</i>
<br><br>
<i>Hoje eu sigo pesquisando,<br>
faço jogo pra rodar,<br>
mas do canal eu guardei<br>
o costume de explicar.<br>
Quem quiser mais um capítulo,<br>
é só descer e chamar.</i>
</td>
</tr>
</table>

<sub><a href="https://kich.dev.br/#cordel">O cordel inteiro no kich.dev.br</a></sub>
</details>

<details>
<summary><code>CH 11</code> Contato · pesquisa, estágio ou os jogos</summary>
<br>

<a href="https://kich.dev.br/#contato"><img src="assets/end-pt.svg" width="100%" alt="Barras de cor do padrão de teste com as palavras Fim de transmissão. A cada poucos segundos o tubo se apaga e liga de novo"></a>

<p align="center">
<a href="https://www.linkedin.com/in/ot%C3%A1vio-kich-mata-70b78b212/">LinkedIn</a> ·
<a href="https://lattes.cnpq.br/4797477996223695">Lattes</a> ·
<a href="https://otaviokmkm.itch.io">itch.io</a> ·
<a href="https://kich.dev.br/#contato">kich.dev.br</a>
</p>
</details>

<br>

<sub>Os cartões desta página são desenhados em código, como o site: o <a href="https://github.com/tavmata/tavmata/blob/main/tools/build.py">tools/build.py</a> faz a sala em pixel, os dados, o relógio, o passaporte, a planta, os menus de RPG e o padrão de teste. Duas GitHub Actions mantêm a página andando: uma redesenha o cartão de contribuições toda manhã (<a href="https://github.com/tavmata/tavmata/blob/main/tools/graph.py">tools/graph.py</a>) e a outra rola os dados (<a href="https://github.com/tavmata/tavmata/blob/main/tools/war_dice.py">tools/war_dice.py</a>). E tem um pinhão escondido na sala lá em cima. Ele aparece por três segundos a cada volta da TV.</sub>
