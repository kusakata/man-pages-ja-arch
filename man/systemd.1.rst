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

systemd が生成したプロセスはプレイベートな systemd 階層にあるプロセスが属するユニットの名前が付いた個別の Linux コントロールグループに配置されます (コントロールグループ "cgroups" について詳しくは **cgroups.txt** [1]_ を参照してください)。systemd はコントロールグループを使って効率的にプロセスを追跡します。コントロールグループの情報はカーネル内で管理され、ファイルシステム階層 (/sys/fs/cgroup/systemd/) からアクセスできます。また、:doc:`systemd-cgls.1` や :doc:`ps.1` などのツールを使う方法もあります (**ps xawf -eo pid,user,cgroup,args** で全てのプロセスとプロセスが属する systemd ユニットを一覧表示することができます)。

systemd は SysV init システムと大部分で互換性を保っています: SysV init スクリプトはサポートされており、もうひとつの設定ファイルフォーマットとして読み込まれます (ただし制限があります)。SysV の /dev/initctl インターフェイスも提供され、様々な SysV クライアントツールの互換実装が存在します。加えて、/etc/fstab や utmp データベースなどの既存の Unix 機能に対応しています。

systemd はミニマルなトランザクションシステムを備えています: ユニットの起動やシャットダウンが要求されると、ユニットとその依存ユニットは一時的なトランザクションに追加されます。そして、トランザクションの整合性 (全てのユニットの順序が循環していないかどうか) が確認されます。循環が見つかった場合、systemd は解決を試みて、ループを抜けるために不必要なジョブをトランザクションから削除します。また、systemd は実行中のサービスを停止するようなトランザクションの重要でないジョブを抑圧できないか試行します。最後にトランザクションのジョブが既にキューに入っているジョブと相反しないかチェックされ、任意でトランザクションが停止されます。全てのチェックが問題なく通過してトランザクションの整合性が保たれ影響を最小限に抑えることができてから、既存のジョブとマージされて実行キューに追加されます。要求された操作を実行する前に、systemd は操作が正しいか確認して、可能であれば修正を行って、上手く行かない場合にのみ失敗します。

systemd はブートプロセスの一部として実行する必要がある様々なタスクをネイティブで実装しています。例えば、systemd はホストネームを設定したりループバックネットワークデバイスの設定を行います。/sys や /proc など様々な API ファイルシステムの設定とマウントも行います。

systemd の背景にある概念や構想について詳しくはオリジナルの設計ドキュメント [2]_ を参照してください。

また、systemd によって提供されているインターフェイスの一部は Interface Stability Promise [3]_ に記載されています。

ユニットは起動時やシステムマネージャのリロード時に動的に生成されることがあります。例えば他の設定ファイルやカーネルコマンドラインに渡されたパラメータによって生成される場合があります。詳しくは :doc:`systemd.generator.7` を参照。

コンテナや initrd 環境で systemd を呼び出すシステムは Container Interface [4]_ あるいは initrd Interface [5]_ 仕様を実装する必要があります。

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
   このシグナルを受信すると systemd システムマネージャは状態をシリアライズして、自分自身を再実行してから保存した状態をデシリアライズします。**systemctl daemon-reexec** とほとんど同じです。

   systemd ユーザーマネージャはこのシグナルを受信すると exit.target ユニットを起動します。**systemctl --user start exit.target --job-mode=replace-irreversible** とほとんど同じです。

SIGINT
   このシグナルを受信すると systemd システムマネージャは ctrl-alt-del.target ユニットを起動します。**systemctl start ctrl-alt-del.target --job-mode=replace-irreversible** とほとんど同じです。このシグナルを2秒間に7回以上受け取った場合、即座に再起動が行われます。コンソールで Ctrl-Alt-Del を押すとこのシグナルが発火します。したがって、再起動中にフリーズした場合、Ctrl-Alt-Del を2秒間に7回以上押すことで比較的安全に強制再起動ができます。

   systemd ユーザーマネージャはこのシグナルを SIGTERM と同じように扱います。

SIGWINCH
   このシグナルを受信すると systemd システムマネージャは kbrequest.target ユニットを起動します。**systemctl start kbrequest.target** とほとんど同じです。

   systemd ユーザーマネージャはこのシグナルを無視します。

SIGPWR
   このシグナルを受信すると systemd システムマネージャは sigpwr.target ユニットを起動します。**systemctl start sigpwr.target** とほとんど同じです。

SIGUSR1
   このシグナルを受信すると systemd システムマネージャは D-Bus バスに再接続を試行します。

SIGUSR2
   このシグナルを受信すると systemd システムマネージャは人間が読める形式で全ての状態をログに出力します。ログに保存されるデータは **systemd-analyze dump** と同じになります。

SIGHUP
   デーモンの設定を完全にリロードします。**systemctl daemon-reload** とほとんど同じです。

SIGRTMIN+0
   デフォルトモードに入って、default.target ユニットを起動します。**systemctl isolate default.target** とほとんど同じです。

SIGRTMIN+1
   レスキューモードに入って、rescue.targe ユニットを起動します。**systemctl isolate rescue.target** とほとんど同じです。

SIGRTMIN+2
   緊急モードに入って、emergency.service ユニットを起動します。**systemctl isolate emergency.service** とほとんど同じです。

SIGRTMIN+3
   マシンを停止して、halt.target ユニットを起動します。**systemctl start halt.target --job-mode=replace-irreversible** とほとんど同じです。

SIGRTMIN+4
   マシンの電源を切って、poweroff.target ユニットを起動します。**systemctl start poweroff.target --job-mode=replace-irreversible** とほとんど同じです。

SIGRTMIN+5
   マシンを再起動して、reboot.target ユニットを起動します。**systemctl start reboot.target --job-mode=replace-irreversible** とほとんど同じです。

SIGRTMIN+6
   kexec でマシンを再起動して kexec.target ユニットを起動します。**systemctl start kexec.target --job-mode=replace-irreversible** とほとんど同じです。

SIGRTMIN+13
   即座にマシンを停止します。

SIGRTMIN+14
   即座にマシンの電源を切ります。

SIGRTMIN+15
   即座にマシンを再起動します。

SIGRTMIN+16
   即座に kexec でマシンを再起動します。

SIGRTMIN+20
   コンソールの状態メッセージの表示を有効にします。カーネルコマンドラインの *systemd.show_status=1* でも同じように制御されます。

SIGRTMIN+21
   コンソールの状態メッセージの表示を無効化します。カーネルコマンドラインの *systemd.show_status=0* でも同じように制御されます。

SIGRTMIN+22, SIGRTMIN+23
   ログレベルを "debug" (あるいは **SIGRTMIN+23** の場合は "info") に設定します。カーネルコマンドラインの *systemd.log_level=debug* (あるいは **SIGRTMIN+23** の場合は *systemd.log_level=info*) でも同じように制御されます。

SIGRTMIN+24
   即座にマネージャを終了します (--user インスタンスのみで使用可能)。

SIGRTMIN+26, SIGRTMIN+27, SIGRTMIN+28
   ログターゲットを "journal-or-kmsg" (**SIGRTMIN+27** の場合は "console"、**SIGRTMIN+28** の場合は "kmsg") に設定します。カーネルコマンドラインの *systemd.log_target=journal-or-kmsg* でも同じように制御されます (あるいは **SIGRTMIN+27** の場合は *systemd.log_target=console* または **SIGRTMIN+28** の場合は *systemd.log_target=kmsg*)。

環境変数
----------

.. envvar:: $SYSTEMD_LOG_LEVEL

   systemd はこの環境変数からログレベルを読み込みます。**--log-level=** で上書き可能です。

.. envvar:: $SYSTEMD_LOG_TARGET

   systemd はこの環境変数からログターゲットを読み込みます。**--log-target=** で上書き可能です。

.. envvar:: $SYSTEMD_LOG_COLOR

   重要なログメッセージをハイライトするかどうか制御します。**--log-color=** で上書き可能です。

.. envvar:: $SYSTEMD_LOG_LOCATION

   ログメッセージにコードの位置を出力するかどうか制御します。**--log-location=** で上書き可能です。

.. envvar:: $XDG_CONFIG_HOME, $XDG_CONFIG_DIRS, $XDG_DATA_HOME, $XDG_DATA_DIRS

   systemd ユーザーマネージャはこの変数を使って **XDG Base Directory specification** [6]_ に従って設定を検索します。

.. envvar:: $SYSTEMD_UNIT_PATH

   systemd がユニットファイルを検索するパスを制御します。

.. envvar:: $SYSTEMD_SYSVINIT_PATH

   systemd が SysV init スクリプトを検索するパスを制御します。

.. envvar:: $SYSTEMD_SYSVRCND_PATH

   systemd が SysV init スクリプトランレベルリンクファームを検索するパスを制御します。

.. envvar:: $SYSTEMD_COLORS

   値は論理値である必要があります。カラー出力を生成するかどうか制御します。**systemd** は *$TERM* 変数と接続されているコンソールを元にカラー出力するかどうか決定しますが、この変数を指定することで上書きすることができます。

.. envvar:: $LISTEN_PID, $LISTEN_FDS, $LISTEN_FDNAMES

   ソケットベースのアクティベーションで systemd によって設定される監視プロセス。詳しくは :doc:`sd_listen_fds.3` を参照。

.. envvar:: $NOTIFY_SOCKET

   状態・起動補完通知で systemd によって設定される監視プロセス。詳しくは :doc:`sd_notify.3` を参照。

カーネルコマンドライン
-----------------------

システムインスタンスとして実行する場合、systemd は様々なカーネルコマンドライン引数を読み込みます [7]_:

systemd.unit=, rd.systemd.unit=
   起動時にアクティベートするユニットを上書きします。デフォルトは default.target です。別の起動ユニットで一時的に起動するのに使うことができます。例えば rescue.target や emergency.service など。これらのユニットについて詳しくは :doc:`systemd.special.7` を参照してください。"rd." が前に付くオプションは初期 RAM ディスク (initrd) でのみ反映され、プリフィックスが付かないオプションはメイン環境でのみ反映されます。

systemd.dump_core
   論理値で指定するか、何も引数を指定しない場合はオプションが有効になります。有効にすると、systemd マネージャ (PID 1) がクラッシュしたときにコアダンプが生成されます。無効の場合はコアダンプは作成されません。デフォルトは有効です。

systemd.crash_chvt
   正の整数、あるいは論理値を指定します。引数を指定しなかった場合、真の論理値と同じ意味になります。正の整数 (1-63 の範囲) を指定した場合、システムマネージャ (PID 1) はクラッシュしたときに指定した仮想端末 (VT) をアクティベートします。デフォルトでは無効となっており、仮想端末の切り替えは行われません。enabled に設定した場合、カーネルメッセージの書き込み先となっている VT が選択されます。

systemd.crash_shell
   論理値で引数を指定します。何も引数を指定しなかった場合、オプションは有効になります。有効にすると、システムマネージャ (PID 1) はクラッシュしたときに10秒待機してからシェルを生成します。無効の場合、シェルは生成されません。シェルがパスワードで保護されないというセキュリティ上の理由から、デフォルトでは無効になっています。

systemd.crash_reboot
   論理値で引数を指定します。何も引数を指定しなかった場合、オプションは有効になります。有効にすると、システムマネージャ (PID 1) はクラッシュしたときに10秒待機してからマシンを自動的に再起動します。無効の場合、システムは永遠にフリーズします。再起動ループに陥らないようにするため、デフォルトでは無効となっています。*systemd.crash_shell* と組み合わせた場合、シェルを終了した後にシステムが再起動します。

systemd.confirm_spawn
   論理値または確認メッセージを出力する仮想端末のパスを指定します。引数を指定しない場合、真の論理値と同じ意味になります。有効の場合、システムマネージャ (PID 1) は **/dev/console** を使ってプロセスを生成するときに確認を要求します。パスまたはコンソール名 ("ttyS0" など) を指定したときは、パスまたは名前によって指定された仮想端末が使われます。デフォルトは無効です。

systemd.service_watchdogs=
   論理値を指定します。無効の場合、全てのサービス実行時ウォッチドッグ (**WatchdogSec=**) と緊急アクション (例: **OnFailure=** または **StartLimitAction=**) はシステムマネージャ (PID 1) によって無視されます。:doc:`systemd.service.5` を見てください。デフォルトでは有効になっており、ウォッチドッグと失敗時のアクションは通常通りに処理されます。このオプションはハードウェアウォッチドッグに影響を与えません。

systemd.show_status
   論理値あるいは定数 **auto** を指定します。引数を付けずに指定することもでき、正の論理値と同じ効果を持ちます。有効の場合、systemd マネージャ (PID 1) は起動時にサービスの状態更新を簡潔にコンソールに表示します。**auto** はユニットが失敗するまで、あるいは起動に異常に時間がかかっている場合を除いて **false** と同じように振る舞います。デフォルトでは有効ですが、カーネルコマンドラインに **quiet** を指定した場合は、デフォルトで **auto** となります。カーネルコマンドラインで指定することでシステムマネージャの設定ファイルのオプション **ShowStatus=** が上書きされます。:doc:`systemd-system.conf.5` を参照してください。ただし、プロセスのコマンドラインオプション **--show-status=** はカーネルコマンドラインのオプションと設定ファイルのオプションどちらよりも優先されます。

systemd.log_target=, systemd.log_level=, systemd.log_location=, systemd.log_color
   ログの出力を制御します。上述の :envvar:`$SYSTEMD_LOG_TARGET`, :envvar:`$SYSTEMD_LOG_LEVEL`, :envvar:`$SYSTEMD_LOG_LOCATION`, :envvar:`$SYSTEMD_LOG_COLOR` 環境変数と同じ効果を持ちます。*systemd.log_color* は引数を付けずに指定でき、その場合は正の論理値と同じ効果を持ちます。

systemd.default_standard_output=, systemd.default_standard_error=
   サービスのデフォルトの標準出力とエラー出力を制御します。上述のコマンドライン引数 **--default-standard-output=** と **--default-standard-error=** と同じ効果を持ちます。

systemd.setenv=
   VARIABLE=VALUE という形式で引数を指定します。フォークされた子プロセスに追加するデフォルトの環境変数を設定できます。複数回使用して複数の変数を設定できます。

systemd.machine_id=
   machine-id を設定するときに使用する32文字の16進数の値を指定します。毎回同じ machine-id を使いたいネットワークブートなどで使用します。

systemd.unified_cgroup_hierarchy
   引数を付けずに指定した場合や true 引数が指定された場合、統合的 cgroup 階層 [8]_ (別名 cgroups-v2) の使用が有効になります。false 引数を指定した場合、ハイブリッドあるいはレガシーな cgroup 階層にフォールバックします。

   このオプションを指定しなかった場合、デフォルトの挙動はコンパイル時の設定によって決まります (**--with-default-hierarchy=** オプション)。カーネルが統合 cgroup 階層をサポートしていない場合、このオプションを指定していてもレガシー階層が使われます。

systemd.legacy_systemd_cgroup_controller
   完全な統合 cgroup 階層が使われない場合にのみ効果を持ちます (前のオプションを参照)。引数を付けずに指定した場合や true 引数を付けた場合、(systemd では cgroups-v2 ツリーを使用して他のコントローラではレガシーな cgroup 階層である cgroups-v1 [9]_ を使用する) ハイブリッドの cgroup 階層の使用が無効になり、強制的に完全なレガシーモードになります。false 引数を指定した場合は、ハイブリッド階層の使用が有効になります。

   このオプションを指定しなかった場合、デフォルトの挙動はコンパイルの設定によって決まります (**--with-default-hierarchy=** オプション)。カーネルが統合 cgroup 階層をサポートしていなかった場合、このオプションを使用していてもレガシー階層が使われます。

quiet
   起動時の状態出力をオフになります。ほとんど *systemd.show_status=false* と同じです。このオプションはカーネルによっても読み込まれるためカーネルのログ出力も無効になります。このオプションを指定することでシステムマネージャとカーネルの両方からの通常出力がオフになります。

debug
   デバッグ出力をオンにします。*systemd.log_level=debug* と同等の効果を持ちます。このオプションはカーネルによっても読み込まれるため、カーネルのデバッグ出力も有効になります。したがって、このオプションを指定するとシステムマネージャとカーネル両方のデバッグ出力が有効になります。

emergency, rd.emergency, -b
   緊急モードで起動します。*systemd.unit=emergency.target* あるいは *rd.systemd.unit=emergency.target* と同じ効果を持っており、互換性のために存在するオプションです。

rescue, rd.rescue, single, s, S, 1
   レスキューモードで起動します。*systemd.unit=rescue.target* あるいは *rd.systemd.unit=rescue.target* と同じ効果を持っており、互換性のために存在するオプションです。

2, 3, 4, 5
   指定した旧 SysV のランレベルで起動します。*systemd.unit=runlevel2.target*, *systemd.unit=runlevel3.target*, *systemd.unit=runlevel4.target*, *systemd.unit=runlevel5.target* と同等で互換性のために存在するオプションです。

locale.LANG=, locale.LANGUAGE=, locale.LC_CTYPE=, locale.LC_NUMERIC=, locale.LC_TIME=, locale.LC_COLLATE=, locale.LC_MONETARY=, locale.LC_MESSAGES=, locale.LC_PAPER=, locale.LC_NAME=, locale.LC_ADDRESS=, locale.LC_TELEPHONE=, locale.LC_MEASUREMENT=, locale.LC_IDENTIFICATION=
   使用するシステムロケールを設定します。このオプションは /etc/locale.conf の設定を上書きします。詳しくは :doc:`locale.conf.5` や :doc:`locale.7` を参照。

コア OS のコンポーネントによって認識される他のカーネルコマンドラインパラメータについては :doc:`kernel-command-line.7` を参照してください。

ソケットと FIFO
------------------

/run/systemd/notify
   デーモン状態通知ソケット。**AF_UNIX** データグラムソケットであり、:doc:`sd_notify.3` によって実装されているように重要なデーモン通知ロジックを実装するのに使われます。

/run/systemd/private
   :doc:`systemctl.1` と systemd プロセスが内部的に使用する通信チャンネル。**AF_UNIX** ストリームソケットです。このインターフェイスは systemd が内部的に使用するものであり外部プロジェクトでは使用できません。

/dev/initctl
   SysV クライアントインターフェイスの限定的な互換サポート。systemd-initctl.service ユニットによって実装。ファイルシステムの名前付きパイプです。このインターフェイスは非推奨であり新しいアプリケーションで使用してはいけません。

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
:doc:`systemd.special.7`,
:doc:`pkg-config.1`,
:doc:`kernel-command-line.7`,
:doc:`bootup.7`,
:doc:`systemd.directives.7`

注釈
-------

.. [1] https://www.kernel.org/doc/Documentation/cgroup-v1/cgroups.txt
.. [2] http://0pointer.de/blog/projects/systemd.html
.. [3] https://www.freedesktop.org/wiki/Software/systemd/InterfaceStabilityPromise
.. [4] https://www.freedesktop.org/wiki/Software/systemd/ContainerInterface
.. [5] https://www.freedesktop.org/wiki/Software/systemd/InitrdInterface
.. [6] http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html
.. [7] Linux コンテナの中で実行する場合、`オプション`_ セクションで説明しているコマンドラインオプションと一緒に、コマンドライン引数として systemd に渡すこともできます。Linux コンテナの外側で実行する場合、引数は /proc/cmdline から読み込まれます。
.. [8] https://www.kernel.org/doc/Documentation/cgroup-v2.txt
.. [9] https://www.kernel.org/doc/Documentation/cgroup-v1/
.. [10] https://www.freedesktop.org/wiki/Software/systemd/
