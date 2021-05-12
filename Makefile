me_git := ${HOME}/src/me.git

IRC_HOST = angela.somas.is

NEWSBOAT := ${XDG_CONFIG_HOME}/newsboat/urls.pub ${XDG_CONFIG_HOME}/newsboat/urls.secret
DUNST := ${XDG_CONFIG_HOME}/dunst/dunstrc.pub ${XDG_CONFIG_HOME}/dunst/dunstrc.secret

all: FRC dunst newsboat

dunst: FRC ${XDG_CONFIG_HOME}/dunst/dunstrc

newsboat: FRC ${XDG_CONFIG_HOME}/newsboat/urls

${IRC_HOST}: FRC pounce-${IRC_HOST} litterbox-${IRC_HOST}

pounce-${IRC_HOST}: FRC
	rsync -ru --delete-after --exclude /home/pounce/.config/pounce/${IRC_HOST} ${XDG_CONFIG_HOME}/pounce/ pounce@${IRC_HOST}:~/.config/pounce
	ssh pounce@${IRC_HOST} mkdir -p '~/.cache/pounce'

litterbox-${IRC_HOST}: FRC
	rsync -ru --delete-after ${XDG_CONFIG_HOME}/litterbox/ pounce@${IRC_HOST}:~/.config/litterbox
	ssh pounce@${IRC_HOST} mkdir -p "~/.local/share/litterbox" "~/.cache/litterbox"

catgirl-${IRC_HOST}: FRC
	rsync -ru --delete-after ${XDG_CONFIG_HOME}/catgirl/ somasis@${IRC_HOST}:~/.config/catgirl
	ssh somasis@${IRC_HOST} mkdir -p "~/.local/share/catgirl" "~/.cache/catgirl"

${XDG_CONFIG_HOME}/%/:
	mkdir -p ${XDG_CONFIG_HOME}/$*

${XDG_CONFIG_HOME}/dunst/dunstrc: ${DUNST}
	cat ${DUNST} > $@

${XDG_CONFIG_HOME}/newsboat/urls: ${NEWSBOAT}
	sed '/^#/d' ${NEWSBOAT} | urls | xe -N0 -Fv urlck
	cat ${NEWSBOAT} > $@

FRC:
