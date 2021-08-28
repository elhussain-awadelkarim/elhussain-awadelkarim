export GTK_IM_MODULE='fcitx'
export QT_IM_MODULE='fcitx'
export SDL_IM_MODILE='fcitx'
export XMODIFIERS='@im=fcitx'

fcitx -d &
xsetroot -name "$(date)" &
picom --config=/home/elhussain/picom.conf &
nitrogen --restore &
dwm
