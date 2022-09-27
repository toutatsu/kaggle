FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-runtime
# FROM python:3
# FROM kaggle/python


# 環境変数:language
ENV LANG en_US.utf8


### Advanced Package Tool(apt) ###
### Debian系のパッケージ管理ツール ###

# apt-get で利用するパッケージダウンロード元のリポジトリを日本のサーバに変更 日本ではネットワーク通信時間が減少
RUN sed --in-place=.backup 's@archive.ubuntu.com@ftp.jaist.ac.jp/pub/Linux@g' /etc/apt/sources.list

# パッケージリスト /etc/apt/sources.list に基づいて
# パッケージインデックスファイルを /var/lib/apt/lists に作る

# update list of available packages
RUN apt update

# upgrade the system by installing/upgrading packages
RUN apt upgrade --assume-yes

# upgrade the system by removing/installing/upgrading packages
# RUN apt upgrade full-upgrade

# list packages based on package names
RUN apt list

### zsh ####
# RUN apt install --assume-yes zsh

#RUN apt install --assume-yes vi
RUN apt install --assume-yes vim

RUN apt install --assume-yes curl

RUN apt install --assume-yes tmux

# RUN apt install --assume-yes git

################################################

WORKDIR /root/


RUN curl -OL https://raw.githubusercontent.com/toutatsu/Docker_templates/main/ubuntu/template.bashrc
RUN cp template.bashrc .bashrc

# RUN cp template.zshrc .zshrc


# RUN curl -OL https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash
# RUN echo ". ~/git-completion.bash" >> .bashrc

# RUN curl -OL https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh
# RUN echo ". ~/git-prompt.sh" >> .bashrc
# RUN export GIT_PS1_SHOWDIRTYSTATE=1
# RUN export PS1='$PS1(__git_ps1 " (%s)")\$ '

# localesのインストール
#RUN apt-get install --assume-yes locales

# ロケール環境の定義
#RUN localedef --inputfile=en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8


# パッケージインデックスファイルを消して容量削減
# RUN rm --recursive --force /var/lib/apt/lists/*




### python ###
RUN pip install --upgrade pip

# requirements
COPY requirements.txt /root
RUN pip install -r requirements.txt