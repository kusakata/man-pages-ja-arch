systemd(1)
==================

名称
--------

systemd, init - systemd システム・サービスマネージャ

書式
--------

| **/usr/lib/systemd/systemd** [OPTIONS...]
| **init** [OPTIONS...] {COMMAND}

説明
-----------

systemd は Linux オペレーティングシステム用のシステム・サービスマネージャです。起動したときの最初のプロセス (PID 1) として実行することで、ユーザー空間のサービスを立ち上げたり管理する init システムとして機能します。

SysV との互換性を保つため、systemd を **init** として呼び出したときに PID が 1 ではない場合、**telinit** を実行して全てのコマンドライン引数をそのまま渡します。通常のログインセッションから呼び出したときは **init** も **telinit** もほとんど同じとなります。詳しくは :doc:`telinit.8` を参照。

システムインスタンスとして実行した場合、systemd は system.conf 設定ファイルと system.conf.d ディレクトリのファイルを読み込みます。ユーザーインスタンスとして実行した場合、systemd は user.conf 設定ファイルと user.conf.d ディレクトリのファイルを読み込みます。詳しくは :doc:`systemd-system.conf.5` を参照してください。

オプション
----------

以下のオプションを使うことができます:

.. option:: --test

   起動シーケンスを確認して、ダンプして終了します。デバッグのときに役立つオプションです。

.. option:: --dump-configuration-items

   使用できるユニット設定アイテムをダンプします。ユニット定義アイテムで使える設定アイテムの簡潔ながら網羅的なリストを出力します。

.. option:: --unit=

   起動時にアクティベートするデフォルトユニットを設定します。指定しなかった場合、デフォルトで default.target が使われます。

.. option:: --system, --user

   **--system** を指定した場合、プロセス ID が 1 ではない (systemd を init プロセスとして実行しない) 場合でも systemd はシステムインスタンスを実行します。**--user** は逆に、プロセス ID が 1 の場合でもユーザーインスタンスを実行します。通常はこれらのオプションを指定する必要はなく、systemd は自動的に起動するべきモードを認識します。デバッグ以外では使う可能性がほとんどないオプションとなります。PID が 1 ではないのに **--system** モードで systemd を動作させシステムを起動・管理することはサポートされないので注意してください。基本的に :option:`--test` と組み合わせる場合以外で **--system** を明示的に指定する意味はありません。

.. option:: --dump-core

   クラッシュ時のコアダンプを有効にします。ユーザーインスタンスとして実行する場合、このスイッチは効果を持ちません。この設定は起動時にカーネルコマンドラインで *systemd.dump_core=* オプションを使って有効にすることもできます。下を参照。

.. option:: --crash-vt=VT

   クラッシュ時に特定の仮想端末 (VT) に切り替えます。1-63 の範囲の正数値か論理値で指定します。正数を指定した場合、指定した VT に切り替わります。**yes** を指定した場合、カーネルメッセージが書き込まれる VT が選択されます。**no** の場合、VT の切り替えは行われません。ユーザーインスタンスとして実行している場合はこのスイッチは効果を持ちません。カーネルコマンドラインで *systemd.crash_vt=* オプションを使うことで起動時に設定を有効にすることもできます。下を参照。

.. option:: --crash-shell

   クラッシュ時にシェルを起動します。ユーザーインスタンスとして実行している場合はこのスイッチは効果を持ちません。カーネルコマンドラインで *systemd.crash_shell=* オプションを使うことで起動時に設定を有効にすることもできます。下を参照。

.. option:: --crash-reboot

   クラッシュ時にシステムを自動的に再起動します。ユーザーインスタンスとして実行している場合はこのスイッチは効果を持ちません。カーネルコマンドラインで *systemd.crash_reboot=* オプションを使うことで起動時に設定を有効にすることもできます。下を参照。

.. option:: --confirm-spawn

   プロセスを生成するときに確認を要求します。ユーザーインスタンスとして実行している場合はこのスイッチは効果を持ちません。

.. option:: --show-status=

   論理引数あたいは特殊値 **auto** を指定します。on の場合、起動時・シャットダウン時にコンソールにユニットの状態情報が簡潔に表示されます。off の場合、状態情報は表示されません。**auto** に設定した場合の挙動は off と似ていますが、ユニットの実行が失敗したり起動に時間がかかっている場合などに自動的に on に切り替わります。ユーザーインスタンスとして実行している場合はこのスイッチは効果を持ちません。指定した場合、カーネルコマンドラインの systemd.show_status= 設定 (下を参照) と設定ファイルのオプション **ShowStatus=** が上書きされます。:doc:`systemd-system.conf.5` を参照。

.. option:: --log-target=

   ログターゲットを設定します。引数は **console**, **journal**, **kmsg**, **journal-or-kmsg**, **null** のどれかである必要があります。

.. option:: --log-level=

   ログレベルを設定します。数字のログレベルあるいは :doc:`syslog.3` のシンボル名 (小文字) を引数として指定できます: **emerg**, **alert**, **crit**, **err**, **warning**, **notice**, **info**, **debug**。

.. option:: --log-color=

   重要なログメッセージをハイライト表示します。引数は論理値です。引数を省略した場合、デフォルトでは **true** になります。

.. option:: --log-location=

   ログメッセージにコードの位置を含めます。主としてデバッグ用のオプションです。引数は論理値です。引数を省略した場合はデフォルトで **true** となります。

.. option:: --default-standard-output=, --default-standard-error=

   全てのサービスとソケットについてデフォルト出力・エラー出力を設定します。**StandardOutput=** と **StandardError=** のデフォルトを制御します (詳しくは :doc:`systemd.exec.5` を参照)。**inherit**, **null**, **tty**, **journal**, **journal+console**, **syslog**, **syslog+console**, **kmsg**, **kmsg+console** のどれかで指定します。引数を省略した場合は **--default-standard-output=** のデフォルトは **journal** に、**--default-standard-error=** のデフォルトは **inherit** になります。

.. option:: --machine-id=

   ハードドライブに設定された machine-id を上書きします。ネットワークブートやコンテナで役に立つオプションです。全てをゼロに設定することはできません。

.. option:: --service-watchdogs=

   全てのサービスのウォッチドッグタイムアウトと緊急アクションをグローバルに有効化・無効化します。この設定は起動時にカーネルコマンドラインで *systemd.service_watchdogs=* オプションを使って指定することも可能です。下を参照。デフォルトは enabled です。

.. option:: -h, --help

   短いヘルプテキストを出力して終了します。

.. option:: --version

   短いバージョン文字列を出力して終了します。

概念
-----------

systemd は11の異なるタイプの「ユニット」と呼ばれるエンティティ間の依存システムを提供します。ユニットではシステムの起動やメンテナンスに関連する様々なオブジェクトがカプセル化されています。ユニットの多くはユニット設定ファイルで設定を行います。設定構文や基本的なオプションについては :doc:`systemd.unit.5` で説明していますが、他の設定から自動的に作成されたり、システムの状態や実行時にプログラムに従って動的に生成されるユニットも存在します。ユニットには "active" 状態 (起動済み・バインド済み・接続済みなどユニットのタイプによって意味は変わります、下を参照) と "inactive" 状態 (停止済み・バインド解除・未接続...) があり、さらにそのふたつの状態に遷移する途中の中間状態が存在します ("activating" または "deactivating" と呼ばれます)。また、特殊な "failed" 状態も存在します。"failed" は "inactive" とよく似ており、何らかの理由でサービスの実行が失敗した場合 (プロセスがエラーコードで終了した、クラッシュした、操作がタイムアウトした、何度も再起動が発生している、など) に遷移します。この状態になったときは、後で確認できるように原因がログに保存されます。ユニットタイプによってはさらに他の状態が存在する場合があり、上記の一般的な5つのユニット状態にマッピングされます。

ユニットタイプは以下が存在します:

   1. サービスユニット。サービスを構成するデーモンやプロセスを起動・制御します。詳しくは :doc:`systemd.service.5` を参照。

   2. ソケットユニット。システムのローカル IPC やネットワークソケットソケットをカプセル化して、ソケットベースのアクティベーションを可能にします。ソケットユニットについて詳しくは :doc:`systemd.socket.5` を参照してください。ソケットベースのアクティベーションなどアクティベーションについての詳しい情報は :doc:`daemon.7` を見てください。

   3. ターゲットユニット。ユニットをグループ化したり、起動時の同期ポイントを提供します。:doc:`systemd.target.5` を参照。

   4. デバイスユニット。カーネルデバイスを systemd から扱えるようにしてデバイスベースのアクティベーションを実装します。詳しくは :doc:`systemd.device.5` を参照。

   5. マウントユニット。ファイルシステムのマウントポイントを制御します。詳しくは :doc:`systemd.mount.5` を参照。

   6. 自動マウントユニット。ファイルシステムを必要に応じてマウントしたりブートを並列化するための自動マウント機能を提供します。:doc:`systemd.automount.5` を参照。

   7. タイマーユニット。タイマーに基づいて他のユニットをアクティベートします。詳細は :doc:`systemd.timer.5` に書かれています。

   8. スワップユニット。マウントユニットとよく似ており、オペレーティングシステムのメモリスワップパーティションやスワップファイルをカプセル化します。:doc:`systemd.swap.5` で解説しています。

   9. パスユニット。ファイルシステムオブジェクトが変更されたときに他のサービスをアクティベートするのに使います。:doc:`systemd.path.5` を見てください。

   10. スライスユニット。システムプロセスを管理するユニット (サービスユニットやスコープユニットなど) を階層ツリーでグループ化してリソース管理するために使用します。:doc:`systemd.slice.5` を見てください。

   11. スコープユニット。サービスユニットと似ていますが、プロセスを起動するのではなく外部プロセスを管理します。:doc:`systemd.scope.5` を見てください。

ユニットは設定ファイルとして名前を付けます。一部のユニットには特殊な命名規則があります。詳しくは :doc:`systemd.special.7` を参照。

systemd は様々な依存関係を扱うことができ、正負の必要依存関係 (*Requires=* と *Conflicts=*) や順序の依存関係 (*After=* と *Before=*) が設定できます。注意: 順序の依存関係と必要依存関係は直交します。2つのユニットの間に必要の依存関係だけが存在する場合で (例: foo.service が bar.service を必要とする)、順序の依存関係が存在しない場合 (例: foo.service は bar.service の後に来る)、両方同時に起動するよう設定した場合、ユニットは並列に起動します。一般的には必要・順序の依存関係は両方とも設定するパターンが基本です。また、ほとんどの依存関係は systemd によって黙示的に作成・管理されます。大抵の場合、依存関係を手動で宣言する必要はない場合が多いですが、手動で設定しようと思えば設定することも可能です。

アプリケーションプログラムと (依存関係の) ユニットはユニットの状態の変更をリクエストすることができます。systemd では、これらのリクエストは「ジョブ」としてカプセル化されてジョブキューで管理されます。ジョブは成功あるいは失敗し、スケジュールしたユニットの順序の依存関係に基づいて実行順序が決まります。

起動時に systemd は default.target ターゲットユニットをアクティベートしてジョブによって起動サービスがアクティベートされたり、依存関係によって他の起動ユニットがアクティベートされます。通常、ユニット名は graphical.target (UI を立ち上げるフル機能の起動) あるいは multi-user.target (組み込み・サーバー環境で使用するコンソールのみの起動、graphical.target のサブセット) のエイリアス (シンボリックリンク) となります。ただし、管理者の裁量で他のターゲットユニットのエイリアスとして設定することもできます。ターゲットユニットについて詳しくは :doc:`systemd.special.7` を参照してください。

systemd が生成したプロセスはプレイベートな systemd 階層にあるプロセスが属するユニットの名前が付いた個別の Linux コントロールグループに配置されます (コントロールグループ "cgroups" について詳しくは **cgroups.txt** [#]_ を参照してください)。systemd はコントロールグループを使って効率的にプロセスを追跡します。コントロールグループの情報はカーネル内で管理され、ファイルシステム階層 (/sys/fs/cgroup/systemd/) からアクセスできます。また、:doc:`systemd-cgls.1` や :doc:`ps.1` などのツールを使う方法もあります (**ps xawf -eo pid,user,cgroup,args** で全てのプロセスとプロセスが属する systemd ユニットを一覧表示することができます)。

systemd は SysV init システムと大部分で互換性を保っています: SysV init スクリプトはサポートされており、もうひとつの設定ファイルフォーマットとして読み込まれます (ただし制限があります)。SysV の /dev/initctl インターフェイスも提供され、様々な SysV クライアントツールの互換実装が存在します。加えて、/etc/fstab や utmp データベースなどの既存の Unix 機能に対応しています。

systemd はミニマルなトランザクションシステムを備えています: ユニットの起動やシャットダウンが要求されると、ユニットとその依存ユニットは一時的なトランザクションに追加されます。そして、トランザクションの整合性 (全てのユニットの順序が循環していないかどうか) が確認されます。循環が見つかった場合、systemd は解決を試みて、ループを抜けるために不必要なジョブをトランザクションから削除します。また、systemd は実行中のサービスを停止するようなトランザクションの重要でないジョブを抑圧できないか試行します。最後にトランザクションのジョブが既にキューに入っているジョブと相反しないかチェックされ、任意でトランザクションが停止されます。全てのチェックが問題なく通過してトランザクションの整合性が保たれ影響を最小限に抑えることができてから、既存のジョブとマージされて実行キューに追加されます。要求された操作を実行する前に、systemd は操作が正しいか確認して、可能であれば修正を行って、上手く行かない場合にのみ失敗します。

systemd はブートプロセスの一部として実行する必要がある様々なタスクをネイティブで実装しています。例えば、systemd はホストネームを設定したりループバックネットワークデバイスの設定を行います。/sys や /proc など様々な API ファイルシステムの設定とマウントも行います。

systemd の背景にある概念や構想について詳しくはオリジナルの設計ドキュメント [#]_ を参照してください。

また、systemd によって提供されているインターフェイスの一部は Interface Stability Promise [#]_ に記載されています。

ユニットは起動時やシステムマネージャのリロード時に動的に生成されることがあります。例えば他の設定ファイルやカーネルコマンドラインに渡されたパラメータによって生成される場合があります。詳しくは :doc:`systemd.generator.7` を参照。

コンテナや initrd 環境で systemd を呼び出すシステムは Container Interface [#]_ あるいは initrd Interface [#]_ 仕様を実装する必要があります。

ディレクトリ
-------------

システムユニットディレクトリ
   systemd システムマネージャは様々なディレクトリからユニットの設定を読み込みます。ユニットファイルをインストールするパッケージは **pkg-config systemd --variable=systemdsystemunitdir** で返ってきたディレクトリにユニットファイルを配置してください。他にチェックされるディレクトリは /usr/local/lib/systemd/system と /usr/lib/systemd/system です。ユーザー設定は常に優先されます。**pkg-config systemd --variable=systemdsystemconfdir** でシステムの設定ディレクトリのパスが返ります。これらのディレクトリは :doc:`systemctl.1` ツールの **enable** と **disable** コマンド以外でパッケージが中身を変更しないようにしてください。ディレクトリの完全な一覧は :doc:`systemd.unit.5` で列挙しています。

ユーザーユニットディレクトリ
   同じルールはユーザーユニットのディレクトリにも適用されます。ただし、XDG Base Directory 仕様 [6]_ に従ってユニットが検索されます。アプリケーションは **pkg-config systemd --variable=systemduserunitdir** によって返されるディレクトリにユニットファイルを配置してください。グローバルな設定は **pkg-config systemd --variable=systemduserconfdir** で返されるディレクトリを使います。:doc:`systemctl.1` ツールの **enable** と **disable** コマンドはグローバル (全ユーザー共通) およびプライベート (特定のユーザーのみ) 両方のユニットの有効化と無効化を処理します。ディレクトリの完全なリストは :doc:`systemd.unit.5` を参照。

SysV init スクリプトディレクトリ
   SysV init スクリプトのディレクトリパスはディストリビューションによって変わります。systemd が要求されたサービスのネイティブユニットファイルを見つけられなかった場合、同じ名前の (.service 拡張子を取り除いた) SysV init スクリプトが検索されます。

SysV ランレベルリンクファームディレクトリ
   SysV ランレベルリンクファームディレクトリのパスはディストリビューションによって異なります。systemd はサービスを有効化するかどうか計算するときにリンクファームを考慮します。SysV ランレベルリンクファームを有効化した場合、ネイティブユニット設定ファイルがあるサービスユニットは起動できないので注意してください。

シグナル
----------

SIGTERM
   Upon receiving this signal the systemd system manager serializes its state, reexecutes itself and deserializes the saved state again. This is mostly equivalent to systemctl daemon-reexec.

   systemd user managers will start the exit.target unit when this signal is received. This is mostly equivalent to systemctl --user start exit.target --job-mode=replace-irreversible.

SIGINT
   Upon receiving this signal the systemd system manager will start the ctrl-alt-del.target unit. This is mostly equivalent to systemctl start ctrl-alt-del.target --job-mode=replace-irreversible. If this signal is received more than 7 times per 2s, an immediate reboot is triggered. Note that pressing Ctrl-Alt-Del on the console will trigger this signal. Hence, if a reboot is hanging, pressing Ctrl-Alt-Del more than 7 times in 2s is a relatively safe way to trigger an immediate reboot.

   systemd user managers treat this signal the same way as SIGTERM.

SIGWINCH
   When this signal is received the systemd system manager will start the kbrequest.target unit. This is mostly equivalent to systemctl start kbrequest.target.

   This signal is ignored by systemd user managers.

SIGPWR
   When this signal is received the systemd manager will start the sigpwr.target unit. This is mostly equivalent to systemctl start sigpwr.target.

SIGUSR1
   When this signal is received the systemd manager will try to reconnect to the D-Bus bus.

SIGUSR2
   When this signal is received the systemd manager will log its complete state in human-readable form. The data logged is the same as printed by systemd-analyze dump.

SIGHUP
   Reloads the complete daemon configuration. This is mostly equivalent to systemctl daemon-reload.

SIGRTMIN+0
   Enters default mode, starts the default.target unit. This is mostly equivalent to systemctl isolate default.target.

SIGRTMIN+1
   Enters rescue mode, starts the rescue.target unit. This is mostly equivalent to systemctl isolate rescue.target.

SIGRTMIN+2
   Enters emergency mode, starts the emergency.service unit. This is mostly equivalent to systemctl isolate emergency.service.

SIGRTMIN+3
   Halts the machine, starts the halt.target unit. This is mostly equivalent to systemctl start halt.target --job-mode=replace-irreversible.

SIGRTMIN+4
   Powers off the machine, starts the poweroff.target unit. This is mostly equivalent to systemctl start poweroff.target --job-mode=replace-irreversible.

SIGRTMIN+5
   Reboots the machine, starts the reboot.target unit. This is mostly equivalent to systemctl start reboot.target --job-mode=replace-irreversible.

SIGRTMIN+6
   Reboots the machine via kexec, starts the kexec.target unit. This is mostly equivalent to systemctl start kexec.target --job-mode=replace-irreversible.

SIGRTMIN+13
   Immediately halts the machine.

SIGRTMIN+14
   Immediately powers off the machine.

SIGRTMIN+15
   Immediately reboots the machine.

SIGRTMIN+16
   Immediately reboots the machine with kexec.

SIGRTMIN+20
   Enables display of status messages on the console, as controlled via systemd.show_status=1 on the kernel command line.

SIGRTMIN+21
   Disables display of status messages on the console, as controlled via systemd.show_status=0 on the kernel command line.

SIGRTMIN+22, SIGRTMIN+23
   Sets the log level to "debug" (or "info" on SIGRTMIN+23), as controlled via systemd.log_level=debug (or systemd.log_level=info on SIGRTMIN+23) on the kernel command line.

SIGRTMIN+24
   Immediately exits the manager (only available for --user instances).

SIGRTMIN+26, SIGRTMIN+27, SIGRTMIN+28
   Sets the log target to "journal-or-kmsg" (or "console" on SIGRTMIN+27, "kmsg" on SIGRTMIN+28), as controlled via systemd.log_target=journal-or-kmsg (or systemd.log_target=console on SIGRTMIN+27 or systemd.log_target=kmsg on SIGRTMIN+28) on the kernel command line.

環境変数
----------

.. envvar:: $SYSTEMD_LOG_LEVEL

   systemd reads the log level from this environment variable. This can be overridden with --log-level=.

.. envvar:: $SYSTEMD_LOG_TARGET

   systemd reads the log target from this environment variable. This can be overridden with --log-target=.

.. envvar:: $SYSTEMD_LOG_COLOR

   Controls whether systemd highlights important log messages. This can be overridden with --log-color=.

.. envvar:: $SYSTEMD_LOG_LOCATION

   Controls whether systemd prints the code location along with log messages. This can be overridden with --log-location=.

.. envvar:: $XDG_CONFIG_HOME, $XDG_CONFIG_DIRS, $XDG_DATA_HOME, $XDG_DATA_DIRS

   The systemd user manager uses these variables in accordance to the XDG Base Directory specification [6]_ to find its configuration.

.. envvar:: $SYSTEMD_UNIT_PATH

   Controls where systemd looks for unit files.

.. envvar:: $SYSTEMD_SYSVINIT_PATH

   Controls where systemd looks for SysV init scripts.

.. envvar:: $SYSTEMD_SYSVRCND_PATH

   Controls where systemd looks for SysV init script runlevel link farms.

.. envvar:: $SYSTEMD_COLORS

   The value must be a boolean. Controls whether colorized output should be generated. This can be specified to override the decision that systemd makes based on $TERM and what the console is connected to.

.. envvar:: $LISTEN_PID, $LISTEN_FDS, $LISTEN_FDNAMES

   Set by systemd for supervised processes during socket-based activation. See sd_listen_fds(3) for more information.

.. envvar:: $NOTIFY_SOCKET

   Set by systemd for supervised processes for status and start-up completion notification. See sd_notify(3) for more information.

カーネルコマンドライン
-----------------------

When run as system instance systemd parses a number of kernel command line arguments [7]_:

systemd.unit=, rd.systemd.unit=
   Overrides the unit to activate on boot. Defaults to default.target. This may be used to temporarily boot into a different boot unit, for example rescue.target or emergency.service. See systemd.special(7) for details about these units. The option prefixed with "rd." is honored only in the initial RAM disk (initrd), while the one that is not prefixed only in the main system.

systemd.dump_core
   Takes a boolean argument or enables the option if specified without an argument. If enabled, the systemd manager (PID 1) dumps core when it crashes. Otherwise, no core dump is created. Defaults to enabled.

systemd.crash_chvt
   Takes a positive integer, or a boolean argument. Can be also specified without an argument, with the same effect as a positive boolean. If a positive integer (in the range 1–63) is specified, the system manager (PID 1) will activate the specified virtual terminal (VT) when it crashes. Defaults to disabled, meaning that no such switch is attempted. If set to enabled, the VT the kernel messages are written to is selected.

systemd.crash_shell
   Takes a boolean argument or enables the option if specified without an argument. If enabled, the system manager (PID 1) spawns a shell when it crashes, after a 10s delay. Otherwise, no shell is spawned. Defaults to disabled, for security reasons, as the shell is not protected by password authentication.

systemd.crash_reboot
   Takes a boolean argument or enables the option if specified without an argument. If enabled, the system manager (PID 1) will reboot the machine automatically when it crashes, after a 10s delay. Otherwise, the system will hang indefinitely. Defaults to disabled, in order to avoid a reboot loop. If combined with systemd.crash_shell, the system is rebooted after the shell exits.

systemd.confirm_spawn
   Takes a boolean argument or a path to the virtual console where the confirmation messages should be emitted. Can be also specified without an argument, with the same effect as a positive boolean. If enabled, the system manager (PID 1) asks for confirmation when spawning processes using /dev/console. If a path or a console name (such as "ttyS0") is provided, the virtual console pointed to by this path or described by the give name will be used instead. Defaults to disabled.

systemd.service_watchdogs=
   Takes a boolean argument. If disabled, all service runtime watchdogs ( WatchdogSec=) and emergency actions (e.g. OnFailure= or StartLimitAction=) are ignored by the system manager (PID 1); see systemd.service(5). Defaults to enabled, i.e. watchdogs and failure actions are processed normally. The hardware watchdog is not affected by this option.

systemd.show_status
   Takes a boolean argument or the constant auto. Can be also specified without an argument, with the same effect as a positive boolean. If enabled, the systemd manager (PID 1) shows terse service status updates on the console during bootup. auto behaves like false until a unit fails or there is a significant delay in boot. Defaults to enabled, unless quiet is passed as kernel command line option, in which case it defaults to auto. If specified overrides the system manager configuration file option ShowStatus=, see systemd-system.conf(5). However, the process command line option --show-status= takes precedence over both this kernel command line option and the configuration file option.

systemd.log_target=, systemd.log_level=, systemd.log_location=, systemd.log_color
   Controls log output, with the same effect as the $SYSTEMD_LOG_TARGET, $SYSTEMD_LOG_LEVEL, $SYSTEMD_LOG_LOCATION, $SYSTEMD_LOG_COLOR environment variables described above. systemd.log_color can be specified without an argument, with the same effect as a positive boolean.

systemd.default_standard_output=, systemd.default_standard_error=
   Controls default standard output and error output for services, with the same effect as the --default-standard-output= and --default-standard-error= command line arguments described above, respectively.

systemd.setenv=
   Takes a string argument in the form VARIABLE=VALUE. May be used to set default environment variables to add to forked child processes. May be used more than once to set multiple variables.

systemd.machine_id=
   Takes a 32 character hex value to be used for setting the machine-id. Intended mostly for network booting where the same machine-id is desired for every boot.

systemd.unified_cgroup_hierarchy
   When specified without an argument or with a true argument, enables the usage of unified cgroup hierarchy [8]_ (a.k.a. cgroups-v2). When specified with a false argument, fall back to hybrid or full legacy cgroup hierarchy.

   If this option is not specified, the default behaviour is determined during compilation (the --with-default-hierarchy= option). If the kernel does not support unified cgroup hierarchy, the legacy hierarchy will be used even if this option is specified.

systemd.legacy_systemd_cgroup_controller
   Takes effect if the full unified cgroup hierarchy is not used (see previous option). When specified without an argument or with a true argument, disables the use of "hybrid" cgroup hierarchy (i.e. a cgroups-v2 tree used for systemd, and legacy cgroup hierarchy [9]_, a.k.a. cgroups-v1, for other controllers), and forces a full "legacy" mode. When specified with a false argument, enables the use of "hybrid" hierarchy.

   If this option is not specified, the default behaviour is determined during compilation (the --with-default-hierarchy= option). If the kernel does not support unified cgroup hierarchy, the legacy hierarchy will be used even if this option is specified.

quiet
   Turn off status output at boot, much like systemd.show_status=false would. Note that this option is also read by the kernel itself and disables kernel log output. Passing this option hence turns off the usual output from both the system manager and the kernel.

debug
   Turn on debugging output. This is equivalent to systemd.log_level=debug. Note that this option is also read by the kernel itself and enables kernel debug output. Passing this option hence turns on the debug output from both the system manager and the kernel.

emergency, rd.emergency, -b
   Boot into emergency mode. This is equivalent to systemd.unit=emergency.target or rd.systemd.unit=emergency.target, respectively, and provided for compatibility reasons and to be easier to type.

rescue, rd.rescue, single, s, S, 1
   Boot into rescue mode. This is equivalent to systemd.unit=rescue.target or rd.systemd.unit=rescue.target, respectively, and provided for compatibility reasons and to be easier to type.

2, 3, 4, 5
   Boot into the specified legacy SysV runlevel. These are equivalent to systemd.unit=runlevel2.target, systemd.unit=runlevel3.target, systemd.unit=runlevel4.target, and systemd.unit=runlevel5.target, respectively, and provided for compatibility reasons and to be easier to type.

locale.LANG=, locale.LANGUAGE=, locale.LC_CTYPE=, locale.LC_NUMERIC=, locale.LC_TIME=, locale.LC_COLLATE=, locale.LC_MONETARY=, locale.LC_MESSAGES=, locale.LC_PAPER=, locale.LC_NAME=, locale.LC_ADDRESS=, locale.LC_TELEPHONE=, locale.LC_MEASUREMENT=, locale.LC_IDENTIFICATION=
   Set the system locale to use. This overrides the settings in /etc/locale.conf. For more information, see locale.conf(5) and locale(7).

For other kernel command line parameters understood by components of the core OS, please refer to kernel-command-line(7).

ソケットと FIFO
------------------

/run/systemd/notify
   Daemon status notification socket. This is an AF_UNIX datagram socket and is used to implement the daemon notification logic as implemented by sd_notify(3).

/run/systemd/private
   Used internally as communication channel between systemctl(1) and the systemd process. This is an AF_UNIX stream socket. This interface is private to systemd and should not be used in external projects.

/dev/initctl
   Limited compatibility support for the SysV client interface, as implemented by the systemd-initctl.service unit. This is a named pipe in the file system. This interface is obsolete and should not be used in new applications.

関連項目
--------

**systemd ホームページ** [10]_,
:doc:`systemd-system.conf.5`,
:doc:`locale.conf.5`,
:doc:`systemctl.1`,
:doc:`journalctl.1`,
:doc:`systemd-notify.1`,
:doc:`daemon.7`,
:doc:`sd-daemon.3`,
:doc:`systemd.unit.5`,
:doc:`systemd.special.5`,
:doc:`pkg-config.1`,
:doc:`kernel-command-line.7`,
:doc:`bootup.7`,
:doc:`systemd.directives.7`

注釈
-------

.. [#] https://www.kernel.org/doc/Documentation/cgroup-v1/cgroups.txt
.. [#] http://0pointer.de/blog/projects/systemd.html
.. [#] https://www.freedesktop.org/wiki/Software/systemd/InterfaceStabilityPromise
.. [#] https://www.freedesktop.org/wiki/Software/systemd/ContainerInterface
.. [#] https://www.freedesktop.org/wiki/Software/systemd/InitrdInterface
.. [#] http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html
.. [#] If run inside a Linux container these arguments may be passed as command line arguments to systemd itself, next to any of the command line options listed in the Options section above. If run outside of Linux containers, these arguments are parsed from /proc/cmdline instead.
.. [#] https://www.kernel.org/doc/Documentation/cgroup-v2.txt
.. [#] https://www.kernel.org/doc/Documentation/cgroup-v1/
.. [#] https://www.freedesktop.org/wiki/Software/systemd/
