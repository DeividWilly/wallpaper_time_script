# Wallpaper real time script #
![](example.png)
Este script muda o seu papel de parede de acordo com o horário, dividido em 4 partes do dia:
 - Madrugada (midnight).
 - Manhã (morning).
 - Tarde (afternoon).
 - Noite (night).

## Dependências: ##

 - [feh](https://wiki.archlinux.org/title/Feh) (3.9.1>)
 - [Python](https://www.python.org/) (3.10.9>) obs: não testado em versões abaixo disso

No [ArchLinux](https://wiki.archlinux.org/title/Pacman):
```
# pacman -S python feh
```

No [Debian]():
```
# apt-get update
# apt-get install feh
```
Para instalar o Python siga esta [instruções](https://linuxnightly.com/install-python-debian/).

--------------------------
## Como instalar ##

Você pode clonar este repositório com apenas o comando:
```
$ git clone https://github.com/DeividWilly/wallpaper_time_script.git
```
ou baixar manualmente o zip.

Copie o arquivo `wall.py` para a pasta de preferência:
```
$ mkdir ~/scripts
$ cp ~/wallpaper_time_script/wall.py ~/scripts/wall.py
```
------------------
## Configuração ##
Dentro de `wall.py`modifique as váriaveis de acordo com seu arquivos e imagens que deseja utilizar, por exemplo:

```py
################################################
#               Basic Config                   #

path_wallpaperFolder = "Pictures/wallpapers" # <-- Pasta que está as imagens
# it is not necessary to write since /home, only the normal path from ~ #

midnight = "midnight.jpg" # <-- Imagem em path_wallpaperFolder setada para ser a imagem de madrugada 
morning = "morning.jpg"
afternoon = "afternoon.jpg"
night = "night.jpg"
################################################
```
Por recomendação padronize seu diretório de scripts e papéis de parede para fácil manutenção e modificação.

ATENÇÃO: NÃO MODIFIQUE MAIS NADA ALÉM DISSO SE NÃO SOUBER O QUE ESTÁ FAZENDO !

-------------------
## Como usar ##

Se você usa algum TWM, como o BSPWM por exemplo, configure no arquivo certo o comando necessário para inicializar o script sempre ao entrar no ambiente, no BSPWM por exemplo, adicione ao arquivo `bspwmrc` a linha:
```
python ~/scripts/wall.py &
```
É necessário a caractere `&` para sinalizar que deve iniciar em segundo plano.

Para mais opções de inicialização, consulte a documentação de sua DE ou WM, a documentação do `xorg` ou outro. 
------------------

Caso o script não funcione, teste primeiro separadamente e veja oque retorne, abra um `PR` ou verifique o que está impedindo. 