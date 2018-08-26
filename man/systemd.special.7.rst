systemd.special(7)
====================

名称
--------

systemd.special - 特殊な systemd ユニット

書式
--------

basic.target, bluetooth.target, cryptsetup-pre.target, cryptsetup.target, ctrl-alt-del.target, default.target, emergency.target, exit.target, final.target, getty.target, getty-pre.target, graphical.target, halt.target, hibernate.target, hybrid-sleep.target, initrd-fs.target, initrd-root-device.target, initrd-root-fs.target, kbrequest.target, kexec.target, local-fs-pre.target, local-fs.target, machines.target multi-user.target, network-online.target, network-pre.target, network.target, nss-lookup.target, nss-user-lookup.target, paths.target, poweroff.target, printer.target, reboot.target, remote-cryptsetup.target, remote-fs-pre.target, remote-fs.target, rescue.target, rpcbind.target, runlevel2.target, runlevel3.target, runlevel4.target, runlevel5.target, shutdown.target, sigpwr.target, sleep.target, slices.target, smartcard.target, sockets.target, sound.target, suspend.target, swap.target, sysinit.target, system-update.target, time-sync.target, timers.target, umount.target, -.slice, system.slice, user.slice, machine.slice, -.mount, dbus.service, dbus.socket, display-manager.service, init.scope, syslog.socket, system-update-cleanup.service

説明
-----------

一部のユニットは systemd で特殊な扱いを受けます。そのようなユニットの多くは特殊な内部セマンティクスを持っており名前を変更することができません。他のユニットは名前には標準的な意味しかなくあらゆる環境に存在します。

特殊なシステムユニット
-----------------------

-.mount
   ルートマウントポイント。/ パスのマウントユニット。このマウントポイントは基本的なユーザー空間となるため、システムが立ち上がっている間、このユニットは無条件にアクティブになります。

basic.target
   基本的な起動を行うための特殊なターゲットユニット。

   systemd はこのターゲットユニットの *After=* タイプの依存を全てのサービスに自動的に追加します (*DefaultDependencies=no* と設定されたサービスは除く)。

   通常、このターゲットユニットは全てのローカルマウントポイントに加えて /var, /tmp, /var/tmp, スワップデバイス, ソケット, タイマー, パスユニットなど一般的なデーモンを使うのに必要な基本的な初期化を制御します。前述のマウントポイントはリモートで操作するための特殊なケースです。

   このターゲットは基本的にターゲット以外のユニットは直接引き込みません。他の起動初期ターゲットによって間接的に制御を行います。起動後期のサービスの同期ポイントとして作られています。関連するターゲットについて詳しくは :doc:`bootup.7` を参照。

ctrl-alt-del.target
   systemd はコンソール上で Control+Alt+Del が押されたときにこのターゲットを起動します。通常、このターゲットは reboot.target にエイリアス (シンボリックリンク) されます。

cryptsetup.target
   暗号ブロックデバイスの設定サービスを制御するターゲット。

dbus.service
   D-Bus バスデーモンの特殊なユニット。このサービスが完全に立ち上がるとすぐに systemd はバスに接続してサービスを登録します。

dbus.socket
   D-Bus システムバスソケットの特殊なユニット。*Type=dbus* のユニットは自動的にこのユニットに依存するようになります。

default.target
   システムの起動時に systemd が立ち上げるデフォルトユニット。通常、このユニットは multi-user.target あるいは graphical.target にエイリアス (シンボリックリンク) されます。

   *systemd.unit=* カーネルコマンドラインオプションを使うことで起動時に systemd が立ち上げるデフォルトユニットを上書きできます。

display-manager.service
   ディスプレイマネージャサービス。通常、このサービスは gdm.service などのディスプレイマネージャのサービスにエイリアス (シンボリックリンク) されます。

emergency.target
   メインコンソールに緊急シェルを起動する特殊なターゲットユニット。このターゲットはサービスやマウントを制御しません。インタラクティブシェルを立ち上げるために必要な最小限の環境を起動します。実行されるプロセスはシステムマネージャ (PID 1) とシェルプロセスだけになります。このユニットはカーネルコマンドラインオプション *systemd.unit=* で使用します。また、必要なファイルシステムのチェックが失敗した場合や起動が続行できない場合にも使用されます。同じような用途の rescue.target もありますが、こちらは基本的なサービスの起動とファイルシステムのマウントも行われます。

   このモードで起動するには "systemd.unit=emergency.target" カーネルコマンドラインオプションを使ってください。このカーネルコマンドラインの短縮形として "emergency" が存在し、SysV と互換性があります。

   emergency.target で起動することはカーネルコマンドラインに "init=/bin/sh" と指定して起動するのとほとんど同じ効果を持ちますが、緊急モードでは完全なシステム・サービスマネージャを提供するため、個別のユニットを起動してブートプロセスを段階を追って続行することができます。

exit.target
   システムやユーザーサービスマネージャをシャットダウンするための特殊なサービスユニット。非コンテナ環境における poweroff.target と同じで、コンテナでも動作します。

   systemd はユーザーサービスデーモンの実行中に **SIGTERM** または **SIGINT** シグナルを受け取ると、このユニットを起動します。

   通常、このターゲット (非間接的に) は shutdown.target を引き寄せ、サービスマネージャが終了するときにシャットダウンするようにスケジューリングされたユニットと衝突します。

final.target
   シャットダウン時に使われる特殊なターゲットユニットで、全ての通常サービスが終了して全てのマウントがアンマウントされた後に後のサービスを制御するのに使われます。

getty.target
   静的に設定されたローカル TTY getty インスタンスを制御する特殊なターゲットユニット。

graphical.target
   グラフィカルなログイン画面をセットアップするための特殊なターゲットユニット。multi-user.target を引き寄せます。

   グラフィカルログインに必要なユニットにはこのユニット (あるいは multi-user.target) の Wants= 依存をインストール時に追加する必要があります。ユニットの "[Install]" セクションで *WantedBy=graphical.target* と設定するのが一番良いでしょう。

hibernate.target
   システムをハイバネートするための特殊なユニット。sleep.target を引き寄せます。

hybrid-sleep.target
   システムを同時にハイバネート・サスペンドするための特殊なユニット。sleep.target を引き寄せます。

halt.target
   システムをシャットダウン・停止するための特殊なターゲットユニット。このターゲットとは poweroff.target とは違ってシステムの停止だけを行い電源は切りません。

   システムを停止したいアプリケーションからこのユニットを直接起動してはいけません。代わりに **systemctl halt** を実行 (任意で --no-block オプションを付ける) するか :doc:`systemd.1` の **org.freedesktop.systemd1.Manager.Halt** D-Bus メソッドを直接呼び出してください。

init.scope
   このスコープユニットはシステム・サービスマネージャ (PID 1) が存在する場所になります。システムが立ち上がっている間はアクティブになります。

initrd-fs.target
   :doc:`systemd-fstab-generator.3` は自動的に sysroot-usr.mount と、**x-initrd.mount** が設定され **noauto** マウントオプションが設定されていない /etc/fstab の全てのマウントポイントに *Before=* タイプの依存を追加します。

initrd-root-device.target
   ルートファイルシステムデバイスが利用可能になったときに、マウントされる前に実行される特殊な initrd ターゲットユニット。:doc:`systemd-fstab-generator.3` と :doc:`systemd-gpt-auto-generator.3` によって自動的に適切な依存関係がセットアップされます。

initrd-root-fs.target
   :doc:`systemd-fstab-generator.3` によってカーネルコマンドラインから生成される sysroot.mount ユニットに *Before=* タイプの依存が追加されます。

kbrequest.target
   コンソールで Alt+ArrowUp が押されたときに systemd はこのターゲットを起動します。マシンに物理的にアクセスできるユーザーなら誰でも使うことができるため (認証は必要ありません)、注意して使うようにしてください。

kexec.target
   kexec でシステムをシャットダウン・再起動するための特殊なターゲットユニット。

   システムを再起動したいアプリケーションがこのユニットを直接使ってはいけません。代わりに **systemctl kexec** を実行するか (**--no-block** オプションを付けることができます)、:doc:`systemd.1` の **org.freedesktop.systemd1.Manager.KExec** D-Bus メソッドを直接呼び出してください。

local-fs.target
   :doc:`systemd-fstab-generator.3` は自動的にローカルマウントポイントを参照する全てのマウントユニットにこのターゲットユニットの *Before=* タイプの依存を追加します。さらに、/etc/fstab に記述されているマウントに **auto** マウントオプションが設定されている場合、このターゲットユニットに *Wants=* タイプの依存が追加されます。

machines.target
   全てのコンテナと仮想マシンを起動するための標準ターゲットユニット。例は systemd-nspawn@.service を参照。

multi-user.target
   マルチユーザーシステム (非グラフィカル) をセットアップするための特殊なターゲットユニット。graphical.target によって使われます。

   マルチユーザーシステムに必要なユニットはインストール時にこのユニットに *Wants=* 依存を追加します。ユニットの "[Install]" セクションで *WantedBy=multi-user.target* と設定するのが最適です。

network-online.target
   ネットワーク接続を必要とするユニットは (*Wants=* タイプの依存で) network-online.target を必要とすることでネットワークが設定されてから起動するようになります。このターゲットユニットはネットワークが正しく立ち上がるまでサービスの実行を遅らせるために存在しています。ネットワーク管理サービスの実装に依存します。

   このユニットと network.target は違いがあるので注意してください。このユニットは能動的なユニットであり (したがって機能の提供者ではなく使用者によって使われます)、サービスを引き込むことで実行までの時間を伸ばします。逆に、network.target は受動的なユニットであり (機能の提供者によって使われます)、実行時間が伸びることはありません。通常、network.target はほとんどの環境で使われますが、network-online.target はどれかユニットが必要としないかぎり使用しません。詳しくは **Running Services After the Network is up** [1]_ も参照してください。

   リモートのネットワークファイルシステムのマウントユニットは自動的にこのユニットに依存して、後で起動するようになります。他のホストに機能を提供するネットワークデーモンはこのユニットに依存する必要はありません。

   systemd は "$network" ファシリティを参照する LSB ヘッダーが付与された SysV init スクリプトサービスユニットについて自動的に Wants= と After= タイプのこのターゲットユニットの依存を追加します。

   このユニットは最初のシステム起動ロジックでおいてのみ有用です。システムの起動が完了した後、システムのオンライン状態は追跡されません。そのため、ネットワーク接続を監視するためにこのユニットを用いることはできず、あくまでシステムの起動時一回きりでしか使用できません。

paths.target
   起動後にアクティブにする全てのパスユニットをセットアップする特殊なターゲットユニット (詳しくは :doc:`systemd.path.5` を参照)。

   アプリケーションによってインストールされたパスユニットはこのユニットから *Wants=* 依存を使って依存させることが推奨されます。パスユニットの "[Install]" セクションで *WantedBy=paths.target* と設定するのが最適です。

poweroff.target
   システムをシャットダウン・電源オフするときの特殊なターゲットユニット。

   システムの電源を切りたいアプリケーションがこのユニットを直接使ってはいけません。代わりに **systemctl poweroff** を (任意で --no-block オプションを付けて) 実行するか :doc:`systemd-logind.8` の **org.freedesktop.login1.Manager.PowerOff** D-Bus メソッドを直接呼び出してください。

   runlevel0.target は SysV との互換性を保つため、このターゲットユニットのエイリアスとなっています。

reboot.target
   システムをシャットダウン・再起動するための特殊なターゲットユニット。

   システムを再起動したいアプリケーションがこのユニットを直接使ってはいけません。代わりに **systemctl reboot** を (任意で --no-block オプションを付けて) 実行するか :doc:`systemd-logind.8` の **org.freedesktop.login1.Manager.Reboot** D-Bus メソッドを直接呼び出してください。

   runlevel6.target は SysV との互換性を保つため、このターゲットユニットのエイリアスとなっています。

remote-cryptsetup.target
   cryptsetup.target と似ていますが、ネットワークを介してアクセスする暗号化デバイスで使います。**_netdev** が付いた :doc:`crypttab.8` エントリで使用。

remote-fs.target
   local-fs.target と似ていますが、リモートのマウントポイントで使います。

   systemd は LSB ヘッダーで "$remote_fs" ファシリティを参照している SysV init スクリプトサービスユニットに自動的に *After=* タイプの依存を追加します。

rescue.target
   (システムマウントを含む) ベースシステムを呼び出して緊急シェルを生成する特殊なターゲットユニット。全てのファイルシステムがマウントされサービスが動作していないシングルユーザーモードでシステムを管理したい場合にこのターゲットを使用します。emergency.target は rescue.target よりも限定的なターゲットとなっておりファイルシステムや基本的なサービスも提供しません。multi-user.target と比べた場合、このターゲットは single-user.target と考えられます。

   SysV との互換性を保つために、runlevel1.target はこのターゲットユニットのエイリアスとなっています。

   このモードで起動するには "systemd.unit=rescue.target" カーネルコマンドラインオプションを使用します。SysV と互換性をとるためにカーネルコマンドラインオプションの省略形として "1" が使えます。

runlevel2.target, runlevel3.target, runlevel4.target, runlevel5.target
   これらのターゲットは SysV の互換コードがランレベル 2, 3, 4, 5 を要求したときに呼び出されます。graphical.target (ランレベル 5 の場合) あるいは multi-user.target (その他のランレベル) のエイリアス (シンボリックリンク) にすると良いでしょう。

shutdown.target
   システムのシャットダウン時にサービスを終了する特殊なターゲットユニット。

   Services that shall be terminated on system shutdown shall add Conflicts= and Before= dependencies to this unit for their service unit, which is implicitly done when DefaultDependencies=yes is set (the default).

sigpwr.target
   A special target that is started when systemd receives the SIGPWR process signal, which is normally sent by the kernel or UPS daemons when power fails.

sleep.target
   A special target unit that is pulled in by suspend.target, hibernate.target and hybrid-sleep.target and may be used to hook units into the sleep state logic.

slices.target
   A special target unit that sets up all slice units (see systemd.slice(5) for details) that shall be active after boot. By default the generic system.slice slice unit, as well as the root slice unit -.slice, is pulled in and ordered before this unit (see below).

   It's a good idea to add WantedBy=slices.target lines to the "[Install]" section of all slices units that may be installed dynamically.

sockets.target
   A special target unit that sets up all socket units (see systemd.socket(5) for details) that shall be active after boot.

   Services that can be socket-activated shall add Wants= dependencies to this unit for their socket unit during installation. This is best configured via a WantedBy=sockets.target in the socket unit's "[Install]" section.

suspend.target
   A special target unit for suspending the system. This pulls in sleep.target.

swap.target
   Similar to local-fs.target, but for swap partitions and swap files.

sysinit.target
   systemd automatically adds dependencies of the types Requires= and After= for this target unit to all services (except for those with DefaultDependencies=no).

   This target pulls in the services required for system initialization. System services pulled in by this target should declare DefaultDependencies=no and specify all their dependencies manually, including access to anything more than a read only root filesystem. For details on the dependencies of this target, refer to bootup(7).

syslog.socket
   The socket unit syslog implementations should listen on. All userspace log messages will be made available on this socket. For more information about syslog integration, please consult the Syslog Interface [2]_ document.

system-update.target, system-update-cleanup.service
   A special target unit that is used for offline system updates. systemd-system-update-generator(8) will redirect the boot process to this target if /system-update exists. For more information see systemd.offline-updates(7).

   Updates should happen before the system-update.target is reached, and the services which implement them should cause the machine to reboot. As a safety measure, if this does not happen, and /system-update still exists after system-update.target is reached, system-update-cleanup.service will remove this symlink and reboot the machine.

timers.target
   A special target unit that sets up all timer units (see systemd.timer(5) for details) that shall be active after boot.

   It is recommended that timer units installed by applications get pulled in via Wants= dependencies from this unit. This is best configured via WantedBy=timers.target in the timer unit's "[Install]" section.

umount.target
   A special target unit that unmounts all mount and automount points on system shutdown.

   Mounts that shall be unmounted on system shutdown shall add Conflicts dependencies to this unit for their mount unit, which is implicitly done when DefaultDependencies=yes is set (the default).

デバイスの特殊なシステムユニット
---------------------------------

Some target units are automatically pulled in as devices of certain kinds show up in the system. These may be used to automatically activate various services based on the specific type of the available hardware.

bluetooth.target
   This target is started automatically as soon as a Bluetooth controller is plugged in or becomes available at boot.

   This may be used to pull in Bluetooth management daemons dynamically when Bluetooth hardware is found.

printer.target
   This target is started automatically as soon as a printer is plugged in or becomes available at boot.

   This may be used to pull in printer management daemons dynamically when printer hardware is found.

smartcard.target
   This target is started automatically as soon as a smartcard controller is plugged in or becomes available at boot.

   This may be used to pull in smartcard management daemons dynamically when smartcard hardware is found.

sound.target
   This target is started automatically as soon as a sound card is plugged in or becomes available at boot.

   This may be used to pull in audio management daemons dynamically when audio hardware is found.

特殊なパッシブシステムユニット
---------------------------------

A number of special system targets are defined that can be used to properly order boot-up of optional services. These targets are generally not part of the initial boot transaction, unless they are explicitly pulled in by one of the implementing services. Note specifically that these passive target units are generally not pulled in by the consumer of a service, but by the provider of the service. This means: a consuming service should order itself after these targets (as appropriate), but not pull it in. A providing service should order itself before these targets (as appropriate) and pull it in (via a Wants= type dependency).

Note that these passive units cannot be started manually, i.e. "systemctl start time-sync.target" will fail with an error. They can only be pulled in by dependency. This is enforced since they exist for ordering purposes only and thus are not useful as only unit within a transaction.

cryptsetup-pre.target
   This passive target unit may be pulled in by services that want to run before any encrypted block device is set up. All encrypted block devices are set up after this target has been reached. Since the shutdown order is implicitly the reverse start-up order between units, this target is particularly useful to ensure that a service is shut down only after all encrypted block devices are fully stopped.

getty-pre.target
   A special passive target unit. Users of this target are expected to pull it in the boot transaction via a dependency (e.g. Wants=). Order your unit before this unit if you want to make use of the console just before getty is started.

local-fs-pre.target
   This target unit is automatically ordered before all local mount points marked with auto (see above). It can be used to execute certain units before all local mounts.

network.target
   This unit is supposed to indicate when network functionality is available, but it is only very weakly defined what that is supposed to mean, with one exception: at shutdown, a unit that is ordered after network.target will be stopped before the network — to whatever level it might be set up then — is shut down. It is hence useful when writing service files that require network access on shutdown, which should order themselves after this target, but not pull it in. Also see Running Services After the Network is up [1]_ for more information. Also see network-online.target described above.

network-pre.target
   This passive target unit may be pulled in by services that want to run before any network is set up, for example for the purpose of setting up a firewall. All network management software orders itself after this target, but does not pull it in.

nss-lookup.target
   A target that should be used as synchronization point for all host/network name service lookups. Note that this is independent of UNIX user/group name lookups for which nss-user-lookup.target should be used. All services for which the availability of full host/network name resolution is essential should be ordered after this target, but not pull it in. systemd automatically adds dependencies of type After= for this target unit to all SysV init script service units with an LSB header referring to the "$named" facility.

nss-user-lookup.target
   A target that should be used as synchronization point for all regular UNIX user/group name service lookups. Note that this is independent of host/network name lookups for which nss-lookup.target should be used. All services for which the availability of the full user/group database is essential should be ordered after this target, but not pull it in. All services which provide parts of the user/group database should be ordered before this target, and pull it in. Note that this unit is only relevant for regular users and groups — system users and groups are required to be resolvable during earliest boot already, and hence do not need any special ordering against this target.

remote-fs-pre.target
   This target unit is automatically ordered before all mount point units (see above) and cryptsetup devices marked with the _netdev. It can be used to run certain units before remote encrypted devices and mounts are established. Note that this unit is generally not part of the initial transaction, unless the unit that wants to be ordered before all remote mounts pulls it in via a Wants= type dependency. If the unit wants to be pulled in by the first remote mount showing up, it should use network-online.target (see above).

rpcbind.target
   The portmapper/rpcbind pulls in this target and orders itself before it, to indicate its availability. systemd automatically adds dependencies of type After= for this target unit to all SysV init script service units with an LSB header referring to the "$portmap" facility.

time-sync.target
   Services responsible for synchronizing the system clock from a remote source (such as NTP client implementations) should pull in this target and order themselves before it. All services where correct time is essential should be ordered after this unit, but not pull it in. systemd automatically adds dependencies of type After= for this target unit to all SysV init script service units with an LSB header referring to the "$time" facility.

特殊なユーザーユニット
-----------------------

When systemd runs as a user instance, the following special units are available, which have similar definitions as their system counterparts: exit.target, default.target, shutdown.target, sockets.target, timers.target, paths.target, bluetooth.target, printer.target, smartcard.target, sound.target.

特殊なパッシブユーザーユニット
--------------------------------

graphical-session.target
   This target is active whenever any graphical session is running. It is used to stop user services which only apply to a graphical (X, Wayland, etc.) session when the session is terminated. Such services should have "PartOf=graphical-session.target" in their "[Unit]" section. A target for a particular session (e. g. gnome-session.target) starts and stops "graphical-session.target" with "BindsTo=graphical-session.target".

   Which services are started by a session target is determined by the "Wants=" and "Requires=" dependencies. For services that can be enabled independently, symlinks in ".wants/" and ".requires/" should be used, see systemd.unit(5). Those symlinks should either be shipped in packages, or should be added dynamically after installation, for example using "systemctl add-wants", see systemctl(1).

   Example 1. Nautilus as part of a GNOME session "gnome-session.target" pulls in Nautilus as top-level service:

   .. code-block:: ini

      [Unit]
      Description=User systemd services for GNOME graphical session
      Wants=nautilus.service
      BindsTo=graphical-session.target

   "nautilus.service" gets stopped when the session stops:

   .. code-block:: ini

      [Unit]
      Description=Render the desktop icons with Nautilus
      PartOf=graphical-session.target

      [Service]
      ...

graphical-session-pre.target
   This target contains services which set up the environment or global configuration of a graphical session, such as SSH/GPG agents (which need to export an environment variable into all desktop processes) or migration of obsolete d-conf keys after an OS upgrade (which needs to happen before starting any process that might use them). This target must be started before starting a graphical session like gnome-session.target.

特殊なスライスユニット
------------------------

There are four ".slice" units which form the basis of the hierarchy for assignment of resources for services, users, and virtual machines or containers. See systemd.slice(7) for details about slice units.

-.slice
   The root slice is the root of the slice hierarchy. It usually does not contain units directly, but may be used to set defaults for the whole tree.

system.slice
   By default, all system services started by systemd are found in this slice.

user.slice
   By default, all user processes and services started on behalf of the user, including the per-user systemd instance are found in this slice. This is pulled in by systemd-logind.service

machine.slice
   By default, all virtual machines and containers registered with systemd-machined are found in this slice. This is pulled in by systemd-machined.service

関連項目
--------

:doc:`systemd.1`,
:doc:`systemd.unit.5`,
:doc:`systemd.service.5`,
:doc:`systemd.socket.5`,
:doc:`systemd.target.5`,
:doc:`systemd.slice.5`,
:doc:`bootup.7`,
:doc:`systemd-fstab-generator.8`

注釈
-------

.. [1] https://www.freedesktop.org/wiki/Software/systemd/NetworkTarget
.. [2] https://www.freedesktop.org/wiki/Software/systemd/syslog
