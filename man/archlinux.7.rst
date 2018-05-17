archlinux(7)
==================

名称
--------

archlinux - 基本設定

書式
--------

Arch Linux の基本設定の概要。

説明
-----------

Arch Linux はユーザーから複雑なシステムを隠すようなことはしません。この man ページでは Arch Linux のインストール時に設定する必要がある設定ファイルについて簡単に説明しています。

システムサービス
-----------------

ブート時に起動したいシステムサービスは *systemctl enable <name>* で有効化することができます。利用可能なサービスを表示したい場合は *systemctl list-unit-files* を使ってください。

ホストネーム
--------------

マシンのホストネームは *hostnamectl set-hostname <hostname>* を使って設定できます。設定すると /etc/hostname に書き込まれます。

ロケール
---------

ロケールは /etc/locale.gen で有効化して *locale-gen* で生成することで設定できます。システム全体で使用するロケールは /etc/locale.conf で設定できます。これらの設定は $HOME/.config/locale.conf でユーザー個別に locale.conf を作成することで上書きできます。ユーザー個別のファイルはシステム全体のファイルよりも優先されます。

仮想端末
---------

仮想端末は /etc/vconsole.conf で設定します。フォントやキーボードレイアウトを設定できます。設定はあくまでコンソールのみに適用され X を使用するときは適用されないので注意してください。

時刻
---------

ローカルのタイムゾーンは *timedatectl set-timezone <Region/City>* を実行して設定します。/etc/localtime から相対的なシンボリックリンクが */usr/share/zoneinfo/* の適当な zoneinfo ファイルに作成されます。例:

   /etc/localtime -> ../usr/share/zoneinfo/Europe/Paris

コンピュータの電源がオフになっているときはリアルタイムクロックが時刻を保持します。*timedatectl set-local-rtc <false|true>* を実行することで UTC とローカルタイムのどちらを使用するか設定できます。デフォルトは UTC です。

ファイルシステム
------------------

ファイルシステムは /etc/fstab で設定し、暗号化マッピングは /etc/crypttab で設定します。

INITRAMFS
-----------

initramfs は *mkinitcpio -p <preset>* で生成します。デフォルトのプリセットは "linux" です。initramfs は /etc/mkinitcpio.conf で設定することができ、設定を変更したら再生成する必要があります。

パッケージマネージャ
----------------------

pacman パッケージマネージャは /etc/pacman.conf で設定します。

ブートローダー
----------------

GRUB の設定は /etc/default/grub から *grub-mkconfig -o /boot/grub/grub.cfg* を実行することで生成されます。Syslinux は /boot/syslinux/syslinux.cfg で設定します。

モジュール
-----------

ほとんどのモジュールは必要になったときにロードされます。起動時に常にロードしたいモジュールは /etc/modules-load.d/ で指定できます。自動的にロードしないようにしたいモジュールは /etc/modprobe.d/ で設定できます。

注意事項
--------

ファイルトリガーは予期しない形で動作してしまう状況というものが存在します。フックはインストール・アップグレード・削除されるパッケージのファイルリストを使って実行されます。*.pacnew* 拡張子で展開されたファイルをインストール・アップグレードするとき、フックを実行するときはオリジナルのファイル名が使われます。パッケージを削除するとき、ファイルシステムにファイルが存在しているかどうかに関係なくパッケージに含まれている全てのファイルによってフックは実行されます。

PostTransaction フックはトランザクションが何らかの理由で完了しなかった場合は実行されません。

pacman とその関連ツールの最新情報は pacman のウェブサイト https://www.archlinux.org/pacman/ を見てください。

関連項目
----------

:doc:`systemctl.1`,
:doc:`hostnamectl.1`,
:doc:`hostname.5`,
:doc:`locale.conf.5`,
:doc:`vconsole.conf.5`,
:doc:`timedatectl.1`,
:doc:`timezone.3`,
:doc:`hwclock.8`,
:doc:`fstab.5`,
:doc:`crypttab.5`,
:doc:`mkinitcpio.8`,
:doc:`pacman.8`,
:doc:`pacman.conf.5`,
:doc:`grub-mkconfig.8`,
:doc:`syslinux.1`,
:doc:`modules-load.d.5`,
:doc:`modprobe.d.5`,
:doc:`systemd.1`

著者
----------

このマニュアルページは Tom Gundersen によって書かれました。
