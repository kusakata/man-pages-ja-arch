systemctl(1)
==================

名称
--------

systemctl - systemd システム・サービスマネージャを制御する

書式
--------

**systemctl** [OPTIONS...] COMMAND [UNIT...]

説明
-----------

**systemctl** を使うことで "systemd" システム・サービスマネージャの状態を調査・制御することができます。基本的な概念やこのツールで管理される機能については :doc:`systemd.1` を参照してください。

オプション
----------

以下のオプションを使うことができます:

.. option:: -t, --type=

   引数は **service** や **socket** などのユニットタイプをカンマで区切ったリストである必要があります。

   引数のどれかがユニットタイプの場合、指定したユニットタイプだけが表示されます。そうでない場合、全てのタイプのユニットが表示されます。

   特殊なケースとして、引数のどれかが **help** の場合、利用可能な値のリストが表示されてプログラムは終了します。

.. option:: --state=

   引数はユニットの状態の LOAD, SUB, ACTIVE をカンマで区切ったリストである必要があります。ユニットを一覧表示するときに、指定した状態のユニットだけが表示されるようになります。起動に失敗したユニットだけを表示したいときは **--state=failed** を使ってください。

   特殊なケースとして、引数のどれかが **help** の場合、利用可能な値のリストが表示されてプログラムは終了します。

.. option:: -p, --property=

   **show** コマンドでユニット・ジョブ・マネージャのプロパティを表示するときに、引数に指定したプロパティだけに表示を制限します。引数は "MainPID" などプロパティ名をカンマで区切ったリストである必要があります。指定しなかった場合、全ての既知のプロパティが表示されます。複数のプロパティを指定した場合、指定した名前の全てのプロパティが表示されます。プロパティ名はシェル補完が効きます。

   マネージャ自体については、:command:`systemctl show` で利用可能なプロパティが全て表示されます。プロパティについては :doc:`systemd-system.conf.5` で説明しています。

   ユニットのプロパティはユニットタイプによって変わるため、(存在しないユニットも含め) あらゆるユニットを表示してこのタイプに関するプロパティを一覧表示します。同じように、全てのジョブを表示することでジョブに関するプロパティが一覧表示されます。ユニットのプロパティについては :doc:`systemd.unit.5` で、あるいは :doc:`systemd.service.5` や :doc:`systemd.socket.5` など個別のユニットタイプのページで説明しています。

.. option:: -a, --all

   **list-units** でユニットを表示するときに、非活性なユニットと他のユニットに追従するユニットも表示します。ユニット・ジョブ・マネージャのプロパティを表示するときは、設定されているかどうかを問わずに全てのプロパティを表示します。

   ファイルシステムにインストールされているユニットを全て一覧したいときは、**list-unit-files** コマンドを使ってください。

   **list-dependencies** でユニットを一覧表示したときは、依存するユニットの全ての依存関係が表示されます (デフォルトでは指定したユニットの依存関係だけが表示されます)。

.. option:: -r, --recursive

   ユニットを一覧表示するときに、ローカルコンテナのユニットも表示します。ローカルコンテナのユニットにはコンテナの名前とコロン文字 (":") が前に付きます。

.. option:: --reverse

   **list-dependencies** でユニットの逆依存関係が表示されます。*Wants=* などではなく *WantedBy=*, *RequiredBy=*, *PartOf=*, *BoundBy=* タイプの依存を追従します。

.. option:: --after

   **list-dependencies** で指定したユニットより順番が前に来るユニットを表示します。つまり、*After=* の依存に従って再帰的にユニットを一覧表示します。

   *After=* の依存関係は自動的に複製されて *Before=* の依存が作成されるので注意してください。一時的な依存関係を明示的に指定することもできますが、*WantedBy=* ターゲットのユニットは依存関係が黙示的に作成されたり (:doc:`systemd.target.5` を参照)、他のディレクティブによって作成されることがあります (例: *RequiresMountsFor=*)。明示的・黙示的に定義された依存関係はどちらも **list-dependencies** で表示されます。

   **list-jobs** コマンドに指定した場合、各ジョブを待機するジョブが表示されます。**--before** と組み合わせることで各ジョブを待機するジョブだけでなく各ジョブが待機する全てのジョブも表示することが可能です。

.. option:: --before

   **list-dependencies** で指定したユニットよりも順番が後のユニットを表示します。つまり、*Before=* の依存に従って再帰的にユニットを一覧表示します。

   **list-jobs** コマンドに指定した場合、各ジョブから待機される他のジョブが表示されます。**--after** と組み合わせることで各ジョブから待機される他のジョブだけでなく各ジョブを待機するジョブも表示することが可能です。

.. option:: -l, --full

   ユニットの名前やプロセスツリーのエントリ、ジャーナルの出力を省略表示しません。さらに **status**, **list-units**, **list-jobs**, **list-timers** の出力におけるユニットの説明が切り詰められなくなります。

   また、**is-enabled** の出力でインストールターゲットが表示されます。

.. option:: --value

   **show** でプロパティを出力するときに、値だけを出力して、プロパティの名前や "=" を省きます。

.. option:: --show-types

   ソケットを表示するときに、ソケットのタイプを表示します。

.. option:: --job-mode=

   新しいジョブをキューに追加したときに、このオプションは既にキューに入っているジョブをどのように扱うのかを制御します。"fail", "replace", "replace-irreversibly", "isolate", "ignore-dependencies", "ignore-requirements", "flush" のどれかひとつを指定します。デフォルトは "replace" ですが、例外的に **isolate** コマンドを使う時だけは黙示的に "isolate" ジョブモードがデフォルトになります。

   "fail" が指定されると保留ジョブとリクエストした操作が競合する場合 (既に保留中の開始ジョブが停止ジョブになる、あるいはその逆)、操作は失敗するようになります。

   "replace" (デフォルト) が指定された場合、競合する保留ジョブは必要に応じて置き換えられます。

   "replace-irreversibly" が指定された場合、"replace" のように操作が行われますが、新しいジョブは不可逆になります。これによって今後は競合する操作によってジョブが置き換えられなくなります (あるいは不可逆のジョブが保留中の際はキューに入れられます)。不可逆ジョブは **cancel** コマンドを使って取り消すことができます。このジョブモードは shutdown.target を引き寄せる操作で使ってください。

   "isolate" は起動操作でのみ指定することができ、指定されたユニットが実行されたとき他のユニットは全て停止します。**isolate** コマンドを使用するときは常にこのモードが使われます。

   "flush" は新しいジョブがキューに入ったときにキューに入っている全てのジョブを取り消します。

   "ignore-dependencies" が指定された場合、新しいジョブではユニットの依存関係が全て無視され、操作は即座に実行されます。無視されたユニットから必要とされているユニットも無視され、順序の依存関係も考慮されません。このモードは管理者がデバッグや緊急ツールとして使うためのものであり、アプリケーションが使用するべきではありません。

   "ignore-requirements" は "ignore-dependencies" と似ていますが、必要の依存関係だけ無視され、順序の依存関係は遵守されます。

.. option:: --fail

   **--job-mode=fail** の省略形。

   **kill** コマンドと組み合わせて使用した場合、どのユニットも終了しなかったときは操作はエラーになります。

.. option:: -i, --ignore-inhibitors

   システムのシャットダウンやスリープが要求されたときに、阻害ロックを無視します。特定の重要な操作 (CD 書き込みなど) がシステムのシャットダウンやスリープによって割り込まれないようにアプリケーションは阻害ロックを作成することができます。ロックは全てのユーザーが作成することができ、特権ユーザーはロックを上書きすることができます。ロックが取得されると、シャットダウンやスリープの要求は通常 (特権であるかどうかを問わず) 失敗して、アクティブなロックの一覧が表示されます。しかしながら、**--ignore-inhibitors** を指定した場合、ロックは無視され表示もされず、シャットダウン・スリープ操作が試行されます。場合によっては特権が必要になります。

.. option:: --dry-run

   実行されることを出力だけして実際の実行は行いません。現在のところ **halt**, **poweroff**, **reboot**, **kexec**, **suspend**, **hibernate**, **hybrid-sleep**, **default**, **rescue**, **emergency**, **exit** コマンドで使うことができます。

.. option:: -q, --quiet

   様々なコマンドの結果を出力しないようにして切り詰められたログ行のヒントも無くなります。(**show** など) 出力だけが実行結果であるコマンドの出力は消えません。エラーは常に出力されます。

.. option:: --no-block

   要求された操作が完了するまで同期的に待機しません。このオプションを指定しなかった場合、ジョブは検証されてキューに入ってから、ユニットの起動が完了するまで **systemctl** は待機します。この引数を指定した場合、検証とキューに入れるだけで終わります。このオプションは **--wait** と組み合わせることができません。

.. option:: --wait

   起動したユニットが終了するまで同期的に待機します。このオプションは **--no-block** と一緒に使うことができません。ユニットがいつまでも終了しないと (ユニット自身が終了したり操作によって停止されないかぎり) 永遠に待機することになるので注意してください。特に "RemainAfterExit=yes" を使用するユニットには注意してください。

.. option:: --user

   システムのサービスマネージャではなく、呼び出したユーザーのサービスマネージャを操作します。

.. option:: --system

   システムのサービスマネージャを操作します。特に指定がない場合のデフォルトです。

.. option:: --failed

   失敗状態のユニットを一覧表示します。**--state=failed** と同じです。

.. option:: --no-wall

   システムの停止・電源オフ・再起動の前に wall メッセージを送信しません。

.. option:: --global

   **enable** や **disable** でグローバルなユーザー設定ディレクトリを使用して、全てのユーザーのあらゆるログインについてグローバルなユニットファイルを有効化・無効化します。

.. option:: --no-reload

   **enable** や **disable** で変更を実行した後に黙示的にデーモンの設定をリロードしません。

.. option:: --no-ask-password

   **start** や関連するコマンドで使用したときに、パスワードを要求しないようにします。バックグラウンドサービスはシステムのハードディスクや暗号証明書を解錠するためにパスワードやパスフレーズ文字列の入力を求める場合があります。このオプションを指定しないでコマンドをターミナルから実行すると、**systemctl** はターミナル上でユーザーにパスワードの入力を要求します。このオプションを使うことでパスワードの要求をオフにすることができます。その場合、パスワードは何か別の方法で指定する必要があります (例えばグラフィカルなパスワードエージェント)。パスワードを指定しないとサービスは失敗します。また、このオプションを使用すると特権操作におけるユーザー認証も無効になります。

.. option:: --kill-who=

   **kill** で使用した場合、どのプロセスにシグナルを送信するか選択します。**main**, **control**, **all** のどれかを指定することでメインプロセスやコントロールプロセスだけを終了するのか、あるいはユニットの全てのプロセスを終了するのか選択してください。ユニットのメインプロセスは活動時間が定義されているプロセスです。ユニットのコントロールプロセスはマネージャによって呼び出されて状態を変化させるプロセスです。例えばサービスユニットの *ExecStartPre=*, *ExecStop=*, *ExecReload=* 設定によって起動したプロセスは全てコントロールプロセスです。状態変化は一度にひとつしか実行されないため、ユニットごとにコントロールプロセスはひとつしか存在しません。*Type=forking* タイプのサービスの場合、マネージャによって最初に *ExecStart=* で起動するプロセスがコントロールプロセスです。一方でフォークされたプロセスは最終的にユニットのメインプロセスになります (メインプロセスが定まる場合)。他のタイプのサービスユニットではこれと異なり、マネージャによって *ExecStart=* でフォークされたプロセスが常にメインプロセスになります。サービスユニットはゼロあるいはひとつのメインプロセスと、ゼロあるいはひとつのコントロールプロセス、そして任意の数の追加プロセスからなります。ただし全てのユニットタイプがこれらのタイプのプロセスを管理するわけではありません。例として、マウントユニットの場合、コントロールプロセスは定義されますが (/usr/bin/mount と /usr/bin/umount の実行)、メインプロセスは定義されません。省略した場合、デフォルトでは **all** になります。

.. option:: -s, --signal=

   **kill** と一緒に使用した場合、選択したプロセスにどのシグナルを送信するのか選択します。**SIGTERM**, **SIGINT**, **SIGSTOP** など既知のシグナルのどれかを指定する必要があります。省略した場合のデフォルトは **SIGTERM** です。

.. option:: -f, --force

   **enable** で使用した場合、競合する既存のシンボリックリンクを上書きします。

   **edit** で使用した場合、指定したユニットが存在しない場合はユニットを作成します。

   **halt**, **poweroff**, **reboot**, **kexec** で使用した場合は全てのユニットをシャットダウンせずに選択した操作を実行します。ただし、全てのプロセスを強制的に終了してファイルシステムは全てアンマウントされ読み取り専用で再マウントされます。劇薬ではありますが即座に再起動したいときは比較的安全なオプションです。これらの操作で **--force** を二回指定すると (**kexec** は除く)、プロセスの終了とファイルシステムのアンマウントも行わずに即座に操作が実行されます。

   .. warning::

      上記の操作で **--force** を二回指定したときはデータが破損する可能性があります。

   **--force** を二回指定したときは選択した操作は **systemctl** 自身によって実行され、システムマネージャを介しません。たとえシステムマネージャがクラッシュしていてもコマンドは通ります。

.. option:: --message=

   **halt**, **poweroff**, **reboot** で使用することで操作の理由を説明する短いメッセージを設定できます。メッセージはデフォルトのシャットダウンメッセージと一緒にログに保存されます。

.. option:: --now

   **enable** で使用した場合、ユニットの有効化だけでなく起動も行われます。**disable** や **mask** で使用した場合、ユニットは停止されます。有効化・無効化の操作が成功したときのみ起動・停止操作も行われます。

.. option:: --root=

   **enable/disable/is-enabled** (や関連するコマンド) で使用することで、ユニットファイルを検索するときに指定されたルートパスを使用します。このオプションが存在するとき、**systemctl** は **systemd** デーモンを通して変更を行うのではなくファイルシステムを直接操作します。

.. option:: --runtime

   **enable**, **disable**, **edit** (と関連するコマンド) で、変更を一時的に適用します。次回再起動時に変更は消失します。/etc のサブディレクトリではなく /run に変更を加えることで、同じ変更ながら再起動で変更が戻る一時的な変更になります。

   同じように **set-property** と組み合わせて使用したときも変更が一時的なものになり、再起動で元に戻るようになります。

.. option:: --preset-mode=

   "full" (デフォルト), "enable-only", "disable-only" のどれかひとつを指定します。**preset** あるいは **preset-all** コマンドで指定することで、プリセットルールにあわせてユニットを無効化・有効化するか、あるいは有効化・無効化のどちらかしか行わないかを制御します。

.. option:: -n, --lines=

   **status** で使用することで、最後の行から数えて、表示するジャーナルの行数を制御します。正の整数を引数として指定してください。デフォルトは 10 です。

.. option:: -o, --output=

   **status** でジャーナルのエントリを表示するフォーマットを制御します。利用可能なオプションについては :doc:`journalctl.1` を参照してください。デフォルトは "short" です。

.. option:: --firmware-setup

   **reboot** コマンドと組み合わせて使用したときに、システムのファームウェアをセットアップモードで起動します。サポートされているのは一部の EFI システムだけであり、システムを EFI モードで起動している場合にのみ使用できます。

.. option:: --plain

   **list-dependencies**, **list-units**, **list-machines** で出力がツリー状ではなくリストになり、黒丸が省略されます。

.. option:: -H, --host=

   操作をリモートで実行します。接続するホスト名、あるいはユーザー名とホスト名を "@" で区切って指定してください。ホスト名には任意で ":" とコンテナ名を後ろに付けることができ、指定したホストの指定されたコンテナに直接接続されます。リモートマシンのマネージャインスタンスに接続するのに SSH が使われます。コンテナ名は **machinectl -H** *HOST* で列挙することができます。

.. option:: -M, --machine=

   ローカルコンテナで操作を実行します。接続するコンテナの名前を指定してください。

.. option:: --no-pager

   ページャに出力をパイプで渡しません。

.. option:: --no-legend

   ヒントが記載されたカラムヘッダーやフッターなど凡例を出力しません。

.. option:: -h, --help

   短いヘルプテキストを表示して終了。

.. option:: --version

   短いバージョン文字列を表示して終了。

コマンド
-----------

以下のコマンドが使用できます:

ユニットコマンド
^^^^^^^^^^^^^^^^^

.. object:: list-units [PATTERN...]

   **systemd** がメモリ内で確保しているユニットを一覧表示します。直接参照されているユニットだけでなく、依存関係によって参照されているユニットや、アプリケーションによってプログラム的にピン止めされているユニット、過去にアクティブ状態だったユニットも含まれます。デフォルトではアクティブなユニットと保留ジョブが存在するユニット、起動に失敗したユニットだけが表示されます。**--all** オプションを使うことで全てのユニットを表示できます。ひとつあるいは複数の *PATTERN* を指定した場合、パターンにマッチするユニットだけが表示されます。**--type=** や **--state=** を使ってさらにユニットを絞り込むこともできます。

   これはデフォルトのコマンドです。

.. object:: list-sockets [PATTERN...]

   メモリ内のソケットユニットを listen しているアドレスの順番で一覧表示します。ひとつあるいは複数の *PATTERN* を指定した場合、パターンにマッチするユニットだけが表示されます。実際には以下のように出力されます::

      LISTEN           UNIT                        ACTIVATES
      /dev/initctl     systemd-initctl.socket      systemd-initctl.service
      ...
      [::]:22          sshd.socket                 sshd.service
      kobject-uevent 1 systemd-udevd-kernel.socket systemd-udevd.service

      5 sockets listed.

   .. note::

      アドレスには空白が含まれることがあるため、出力はプログラムで処理するのに適していません。

   **--show-types**, **--all**, **--state=** も参照してください。

.. object:: list-timers [PATTERN...]

   メモリ内のタイマーユニットを次回に実行される順番で一覧表示します。ひとつあるいは複数の *PATTERN* を指定した場合、パターンにマッチするユニットだけが表示されます。実際には以下のように出力されます::

      NEXT                         LEFT          LAST                         PASSED     UNIT                         ACTIVATES
      /a                          n/a           Thu 2017-02-23 13:40:29 EST  3 days ago ureadahead-stop.timer        ureadahead-stop.service
      Sun 2017-02-26 18:55:42 EST  1min 14s left Thu 2017-02-23 13:54:44 EST  3 days ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
      Sun 2017-02-26 20:37:16 EST  1h 42min left Sun 2017-02-26 11:56:36 EST  6h ago     apt-daily.timer              apt-daily.service
      Sun 2017-02-26 20:57:49 EST  2h 3min left  Sun 2017-02-26 11:56:36 EST  6h ago     snapd.refresh.timer          snapd.refresh.service

   *NEXT* はタイマーが次回に実行される時刻を表示します。

   *LEFT* は次回にタイマーが実行されるまでの残り時間を表示します。

   *LAST* は最後にタイマーが実行された時刻を表示します。

   *PASSED* は最後にタイマーが実行されてからの経過時間を表示します。

   *UNIT* はタイマーの名前を表示します。

   *ACTIVATES* はタイマーが実行されたときに有効になるサービスの名前を表示します。

   **--all** や **--state=** も参照してください。

.. object:: start PATTERN...

   コマンドラインで指定したひとつあるいは複数のユニットを起動します。

   glob パターンはメモリ内に存在するユニットのプライマリ名に適用されます。アクティブでないユニットや起動に失敗したユニットは基本的にメモリ内に存在しないため、パターンを指定してもマッチしません。さらに、インスタンス化されたユニットの場合、systemd はインスタンスが起動しないかぎりインスタンス名を認識しません。したがって、**start** で使える glob パターンは使いどころが限られます。また、ユニットのセカンダリエイリアス名は認識されません。

.. object:: stop PATTERN...

   コマンドラインで指定したひとつあるいは複数のユニットを停止します。

.. object:: reload PATTERN...

   コマンドラインで指定した全てのユニットの設定をリロードします。リロードされるのはサービスごとの設定であり、systemd のユニット設定ファイルはリロードされないので注意してください。systemd のユニットの設定ファイルをリロードしたいときは、**daemon-reload** コマンドを使ってください。例えば Apache の場合、reload コマンドでリロードされるのはウェブサーバーの Apache の httpd.conf であって、systemd ユニットファイルの apache.service ではありません。

   このコマンドと **daemon-reload** コマンドは混同しないようにしてください。

.. object:: restart PATTERN...

   コマンドラインで指定したひとつあるいは複数のユニットを停止してから起動します。ユニットが起動していなかった場合、起動だけが行われます。

   このコマンドでユニットを再起動しても、再起動前にユニットのリソースが全て開放されるとは必ずしも限らないので注意してください。例えば、サービスごとのファイル記述子ストレージファシリティ (:doc:`systemd.service.5` の *FileDescriptoreStoreMax=* を参照) はユニットに保留ジョブがあるかぎり残り続け、ユニットが完全に停止して保留ジョブがなくなったときに初めて消去されます。ファイル記述子ストアも消去したい場合、**systemctl stop** コマンドを明示的に実行してから **systemctl start** コマンドを実行するようにして再起動してください。

.. object:: try-restart PATTERN...

   ユニットが動作中の場合、コマンドラインで指定したひとつあるいは複数のユニットを停止してから起動します。ユニットが起動していなかった場合、何も行いません。

.. object:: reload-or-restart PATTERN...

   ユニットがリロードをサポートしている場合、指定したひとつあるいは複数のユニットをリロードします。サポートされていない場合、かわりにユニットを停止してから起動します。ユニットが起動していなかった場合、起動だけが行われます。

.. object:: try-reload-or-restart PATTERN...

   ユニットがリロードをサポートしている場合、指定したひとつあるいは複数のユニットをリロードします。サポートされていない場合、かわりにユニットを停止してから起動します。ユニットが起動していなかった場合、何も行いません。

.. object:: isolate UNIT

   コマンドラインで指定したユニットとその依存ユニットを起動して、**IgnoreOnIsolate=yes** が設定されていない他のユニットは全て停止します (:doc:`systemd.unit.5` を参照)。指定したユニット名に拡張子がない場合、拡張子は ".target" として認識されます。

   **isolate** は伝統的な init システムにおけるランレベルの変更と似ています。**isolate** コマンドは新しいユニットで有効になっていないプロセスを即座に停止します。使用中のグラフィカル環境やターミナルも含まれます。

   **isolate** コマンドが使えるのは **AllowIsolate=** が有効になっているユニットだけです。詳しくは :doc:`systemd.unit.5` を見てください。

.. object:: kill PATTERN...

   ひとつまたは複数のユニットのプロセスにシグナルを送信します。どのプロセスを終了するか選択するには **--kill-who=** を使います。送信するシグナルを選択するには **--signal=** を使います。

.. object:: is-active PATTERN...

   指定したユニットがアクティブ (動作中) かどうか確認します。指定したユニットのどれかひとつでもアクティブなら終了コード **0** が返り、そうでない場合はゼロ以外の値が返ります。**--quiet** が指定されていない場合、現在のユニットの状態が標準出力に出力されます。

.. object:: is-failed PATTERN...

   指定されたユニットのどれかが "failed" 状態でないか確認します。どれかひとつでもユニットが失敗していれば終了コード **0** が返り、そうでない場合はゼロ以外の値が返ります。**--quiet** が指定されていない場合、現在のユニットの状態が標準出力に出力されます。

.. object:: status [PATTERN...|PID...]

   ひとつまたは複数のユニットの動作状態情報を簡潔に表示して、ジャーナルから一番最近のログデータを表示します。ユニットを指定しなかった場合、システムの状態を表示します。**--all** と組み合わせたときは、全てのユニットの状態を表示します (ただし **-t** で制限を指定できます)。PID を指定した場合、プロセスが属しているユニットの情報が表示されます。

   この機能は人間が読みやすい出力を生成します。コンピュータでパースするための出力を求めている場合、代わりに **show** を使ってください。デフォルトでは、この機能は出力を10行だけ表示してターミナルウィンドウに行が収まるように切り詰めます。**--lines** と **--full** を使うことでこの挙動は変更できます (上を参照)。さらに、**journalctl --unit=NAME** や **journalctl --user-unit=NAME** はメッセージを同じようにフィルタリングします。

   systemd は必要に応じて黙示的にユニットをロードするため、**status** を実行するだけでもファイルがロードされます。何かがロードされているかどうか確認するためにこのコマンドを使うことはできません。操作が完了した後に特にメモリ内に残しておく理由がなければユニットはすぐにアンロードされる可能性があります。

   **例 1. systemctl status の出力例**

   .. code-block:: console

      $ systemctl status bluetooth
      ● bluetooth.service - Bluetooth service
         Loaded: loaded (/usr/lib/systemd/system/bluetooth.service; enabled; vendor preset: enabled)
         Active: active (running) since Wed 2017-01-04 13:54:04 EST; 1 weeks 0 days ago
           Docs: man:bluetoothd(8)
       Main PID: 930 (bluetoothd)
         Status: "Running"
          Tasks: 1
         Memory: 648.0K
            CPU: 435ms
         CGroup: /system.slice/bluetooth.service
                 └─930 /usr/lib/bluetooth/bluetoothd

      Jan 12 10:46:45 example.com bluetoothd[8900]: Not enough free handles to register service
      Jan 12 10:46:45 example.com bluetoothd[8900]: Current Time Service could not be registered
      Jan 12 10:46:45 example.com bluetoothd[8900]: gatt-time-server: Input/output error (5)

   黒丸 ("●") はカラーをサポートしているターミナルでは色を使ってユニットの状態がひと目でわかるようにします。白色は "inactive" または "deactivating" 状態を示します。赤色は "failed" または "error" 状態を、緑色は "active", "reloading", "activating" 状態のどれかを示します。

   "Loaded:" 行にはメモリ内にユニットがロードされているときは "loaded" と表示されます。他にも "Loaded:" には "error" (ロード時に問題が発生した場合) と表示されたり "not-found" や "masked" と表示されることがあります。ユニットファイルのパスと一緒に、ユニットの有効化状態も表示されます。有効化されたコマンドは起動時に実行されます。("masked" の定義を含む) 有効化状態を説明している完全な表が **is-enabled** コマンドのドキュメントに存在します。

   "Active:" 行はアクティブ状態を示します。通常の場合、値は "active" または "inactive" です。アクティブはユニットタイプに応じて起動済み・バインド済み・接続済みなどを意味します。状態が変化している途中のユニットは "activating" または "deactivating" と表示されます。サービスがクラッシュしたりエラーコードで終了したりタイムアウトしたりすると特殊な "failed" 状態になります。失敗状態になったときは後で参照できるように原因がログに保存されます。

.. object:: show [PATTERN...|JOB...]

   ひとつまたは複数のユニット・ジョブ・マネージャのプロパティを表示します。引数を指定しなかった場合、マネージャのプロパティが表示されます。ユニット名を指定した場合、ユニットのプロパティが表示され、ジョブ ID を指定した場合、ジョブのプロパティが表示されます。デフォルトでは、空のプロパティは表示されません。表示したいときは **--all** を使ってください。表示したいプロパティを選択するときは、**--property=** を使います。このコマンドはプログラムでパースできる出力が必要なときに使用してください。人間が読みやすい形式で出力を得たいときは **status** を使います。

   **systemctl show** によって表示される多数のプロパティはシステム・サービスマネージャ・ユニットファイルの設定に直接マッピングされています。このコマンドによって表示されるプロパティは基本的にオリジナルの設定をもっと低水準から統一された表現になり、設定に加えて実行状態も表示されます。例えば、サービスユニットで表示されるプロパティにはサービスの現在のメインプロセスの識別子が "MainPID" として表示され (実行状態)、たとえマッチする設定オプションが "...Sec" で終わっていたとしても、システム・サービスマネージャによって使用される統一の時刻単位はマイクロ秒であるため、時刻設定は常に "...USec" で終わるプロパティで表示されます。

.. object:: cat PATTERN...

   ひとつまたは複数のユニットのバッキングファイルを表示します。ユニットの "fragment" と "drop-ins" (ソースファイル) が出力されます。それぞれのファイルにはファイル名を含むコメントが前に付きます。このコマンドはディスク上のバッキングファイルの中身を表示するため、ディスク上のユニットファイルを修正してから **daemon-reload** コマンドをまだ実行していない場合、表示される内容がシステムマネージャが認識しているユニットの中身と一致していない可能性があります。

.. object:: set-property UNIT PROPERTY= VALUE...

   Set the specified unit properties at runtime where this is supported. This allows changing configuration parameter properties such as resource control settings at runtime. Not all properties may be changed at runtime, but many resource control settings (primarily those in systemd.resource-control(5)) may. The changes are applied immediately, and stored on disk for future boots, unless --runtime is passed, in which case the settings only apply until the next reboot. The syntax of the property assignment follows closely the syntax of assignments in unit files.

   例: **systemctl set-property foobar.service CPUShares=777**

   If the specified unit appears to be inactive, the changes will be only stored on disk as described previously hence they will be effective when the unit will be started.

   Note that this command allows changing multiple properties at the same time, which is preferable over setting them individually. Like with unit file configuration settings, assigning an empty list will reset the property.

.. object:: help PATTERN...|PID...

   Show manual pages for one or more units, if available. If a PID is given, the manual pages for the unit the process belongs to are shown.

.. object:: reset-failed [PATTERN...]

   Reset the "failed" state of the specified units, or if no unit name is passed, reset the state of all units. When a unit fails in some way (i.e. process exiting with non-zero error code, terminating abnormally or timing out), it will automatically enter the "failed" state and its exit code and status is recorded for introspection by the administrator until the service is stopped/re-started or reset with this command.

.. object:: list-dependencies [UNIT]

   Shows units required and wanted by the specified unit. This recursively lists units following the Requires=, Requisite=, ConsistsOf=, Wants=, BindsTo= dependencies. If no unit is specified, default.target is implied.

   By default, only target units are recursively expanded. When --all is passed, all other units are recursively expanded as well.

   Options --reverse, --after, --before may be used to change what types of dependencies are shown.

ユニットファイルコマンド
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. object:: list-unit-files [PATTERN...]

   List unit files installed on the system, in combination with their enablement state (as reported by is-enabled). If one or more PATTERNs are specified, only unit files whose name matches one of them are shown (patterns matching unit file system paths are not supported).

.. object:: enable UNIT..., enable PATH...

   Enable one or more units or unit instances. This will create a set of symlinks, as encoded in the "[Install]" sections of the indicated unit files. After the symlinks have been created, the system manager configuration is reloaded (in a way equivalent to daemon-reload), in order to ensure the changes are taken into account immediately. Note that this does not have the effect of also starting any of the units being enabled. If this is desired, combine this command with the --now switch, or invoke start with appropriate arguments later. Note that in case of unit instance enablement (i.e. enablement of units of the form foo@bar.service), symlinks named the same as instances are created in the unit configuration directory, however they point to the single template unit file they are instantiated from.

   This command expects either valid unit names (in which case various unit file directories are automatically searched for unit files with appropriate names), or absolute paths to unit files (in which case these files are read directly). If a specified unit file is located outside of the usual unit file directories, an additional symlink is created, linking it into the unit configuration path, thus ensuring it is found when requested by commands such as start. The file system where the linked unit files are located must be accessible when systemd is started (e.g. anything underneath /home or /var is not allowed, unless those directories are located on the root file system).

   This command will print the file system operations executed. This output may be suppressed by passing --quiet.

   Note that this operation creates only the symlinks suggested in the "[Install]" section of the unit files. While this command is the recommended way to manipulate the unit configuration directory, the administrator is free to make additional changes manually by placing or removing symlinks below this directory. This is particularly useful to create configurations that deviate from the suggested default installation. In this case, the administrator must make sure to invoke daemon-reload manually as necessary, in order to ensure the changes are taken into account.

   Enabling units should not be confused with starting (activating) units, as done by the start command. Enabling and starting units is orthogonal: units may be enabled without being started and started without being enabled. Enabling simply hooks the unit into various suggested places (for example, so that the unit is automatically started on boot or when a particular kind of hardware is plugged in). Starting actually spawns the daemon process (in case of service units), or binds the socket (in case of socket units), and so on.

   Depending on whether --system, --user, --runtime, or --global is specified, this enables the unit for the system, for the calling user only, for only this boot of the system, or for all future logins of all users. Note that in the last case, no systemd daemon configuration is reloaded.

   Using enable on masked units is not supported and results in an error.

.. object:: disable UNIT...

   Disables one or more units. This removes all symlinks to the unit files backing the specified units from the unit configuration directory, and hence undoes any changes made by enable or link. Note that this removes all symlinks to matching unit files, including manually created symlinks, and not just those actually created by enable or link. Note that while disable undoes the effect of enable, the two commands are otherwise not symmetric, as disable may remove more symlinks than a prior enable invocation of the same unit created.

   This command expects valid unit names only, it does not accept paths to unit files.

   In addition to the units specified as arguments, all units are disabled that are listed in the Also= setting contained in the "[Install]" section of any of the unit files being operated on.

   This command implicitly reloads the system manager configuration after completing the operation. Note that this command does not implicitly stop the units that are being disabled. If this is desired, either combine this command with the --now switch, or invoke the stop command with appropriate arguments later.

   This command will print information about the file system operations (symlink removals) executed. This output may be suppressed by passing --quiet.

   This command honors --system, --user, --runtime and --global in a similar way as enable.

.. object:: reenable UNIT...

   Reenable one or more units, as specified on the command line. This is a combination of disable and enable and is useful to reset the symlinks a unit file is enabled with to the defaults configured in its "[Install]" section. This command expects a unit name only, it does not accept paths to unit files.

.. object:: preset UNIT...

   Reset the enable/disable status one or more unit files, as specified on the command line, to the defaults configured in the preset policy files. This has the same effect as disable or enable, depending how the unit is listed in the preset files.

   Use --preset-mode= to control whether units shall be enabled and disabled, or only enabled, or only disabled.

   If the unit carries no install information, it will be silently ignored by this command. UNIT must be the real unit name, any alias names are ignored silently.

   For more information on the preset policy format, see systemd.preset(5). For more information on the concept of presets, please consult the Preset [#]_ document.

.. object:: preset-all

   Resets all installed unit files to the defaults configured in the preset policy file (see above).

   Use --preset-mode= to control whether units shall be enabled and disabled, or only enabled, or only disabled.

.. object:: is-enabled UNIT...

   Checks whether any of the specified unit files are enabled (as with enable). Returns an exit code of 0 if at least one is enabled, non-zero otherwise. Prints the current enable status (see table). To suppress this output, use --quiet. To show installation targets, use --full.

   .. list-table:: 表 1. is-enabled の出力
      :header-rows: 1
      :widths: 1, 8, 1

      * - 名前
        - 説明
        - 終了コード
      * - "enabled"
        - .wants/, .requires/, *Alias=* シンボリックリンク (/etc/systemd/system/ は永続的、/run/systemd/system/ は一時的) で有効化されている。
        - 0
      * - "enabled-runtime"
        -
        -
      * - "linked"
        - ユニットファイルがユニットファイルの検索パスの外にあるが、ひとつあるいは複数のユニットファイルのシンボリックリンクで有効になっている (/etc/systemd/system/ は永続的、/run/systemd/system/ は一時的)。
        - > 0
      * - "linked-runtime"
        -
        -
      * - "masked"
        - 完全に無効化されており、起動操作も失敗する (/etc/systemd/system/ は永続的、/run/systemd/system/ は一時的)。
        - > 0
      * - "masked-runtime"
        -
        -
      * - "static"
        - ユニットファイルは有効化されておらず、ユニットファイルの "[Install]" セクションに有効化するための記述がない。
        - 0
      * - "indirect"
        - ユニットファイル自体は有効になっていないが、ユニットファイルの "[Install]" セクションの *Also=* 設定が空ではなく、有効化されている他のユニットが含まれている、あるいは Also= で指定されていないシンボリックリンクによって別の名前のエイリアスが存在する。テンプレートユニットファイルの場合、*DefaultInstance=* で指定されているインスタンス以外のインスタンスが有効になっている。
        - 0
      * - "disabled"
        - ユニットファイルは有効化されていないが、インストール方法が書かれた "[Install]" セクションが存在する。
        - > 0
      * - "generated"
        - ジェネレータツールによって動的に生成されたユニットファイル。:doc:`systemd.generator.7` を参照。生成されたユニットは有効化することができず、ジェネレータによって黙示的に有効になります。
        - 0
      * - "transient"
        - ランタイム API によって動的に作成されたユニットファイル。一時ユニットは有効化できません。
        - 0
      * - "bad"
        - ユニットファイルが不正またはエラーが発生している。**is-enabled** はこの状態を返すのではなく、エラーメッセージを出力します。ただし **list-unit-files** で出力されたユニットファイルはこの状態を表示します。
        - > 0

.. object:: mask UNIT...

   Mask one or more units, as specified on the command line. This will link these unit files to /dev/null, making it impossible to start them. This is a stronger version of disable, since it prohibits all kinds of activation of the unit, including enablement and manual activation. Use this option with care. This honors the --runtime option to only mask temporarily until the next reboot of the system. The --now option may be used to ensure that the units are also stopped. This command expects valid unit names only, it does not accept unit file paths.

.. object:: unmask UNIT...

   Unmask one or more unit files, as specified on the command line. This will undo the effect of mask. This command expects valid unit names only, it does not accept unit file paths.

.. object:: link PATH...

   Link a unit file that is not in the unit file search paths into the unit file search path. This command expects an absolute path to a unit file. The effect of this may be undone with disable. The effect of this command is that a unit file is made available for commands such as start, even though it is not installed directly in the unit search path. The file system where the linked unit files are located must be accessible when systemd is started (e.g. anything underneath /home or /var is not allowed, unless those directories are located on the root file system).

.. object:: revert UNIT...

   Revert one or more unit files to their vendor versions. This command removes drop-in configuration files that modify the specified units, as well as any user-configured unit file that overrides a matching vendor supplied unit file. Specifically, for a unit "foo.service" the matching directories "foo.service.d/" with all their contained files are removed, both below the persistent and runtime configuration directories (i.e. below /etc/systemd/system and /run/systemd/system); if the unit file has a vendor-supplied version (i.e. a unit file located below /usr) any matching persistent or runtime unit file that overrides it is removed, too. Note that if a unit file has no vendor-supplied version (i.e. is only defined below /etc/systemd/system or /run/systemd/system, but not in a unit file stored below /usr), then it is not removed. Also, if a unit is masked, it is unmasked.

   Effectively, this command may be used to undo all changes made with systemctl edit, systemctl set-property and systemctl mask and puts the original unit file with its settings back in effect.

.. object:: add-wants TARGET UNIT..., add-requires TARGET UNIT...

   Adds "Wants=" or "Requires=" dependencies, respectively, to the specified TARGET for one or more units.

   This command honors --system, --user, --runtime and --global in a way similar to enable.

.. object:: edit UNIT...

   Edit a drop-in snippet or a whole replacement file if --full is specified, to extend or override the specified unit.

   Depending on whether --system (the default), --user, or --global is specified, this command creates a drop-in file for each unit either for the system, for the calling user, or for all futures logins of all users. Then, the editor (see the "Environment" section below) is invoked on temporary files which will be written to the real location if the editor exits successfully.

   If --full is specified, this will copy the original units instead of creating drop-in files.

   If --force is specified and any units do not already exist, new unit files will be opened for editing.

   If --runtime is specified, the changes will be made temporarily in /run and they will be lost on the next reboot.

   If the temporary file is empty upon exit, the modification of the related unit is canceled.

   After the units have been edited, systemd configuration is reloaded (in a way that is equivalent to daemon-reload).

   Note that this command cannot be used to remotely edit units and that you cannot temporarily edit units which are in /etc, since they take precedence over /run.

.. object:: get-default

   Return the default target to boot into. This returns the target unit name default.target is aliased (symlinked) to.

.. object:: set-default TARGET

   Set the default target to boot into. This sets (symlinks) the default.target alias to the given target unit.

マシンコマンド
^^^^^^^^^^^^^^^^^

.. object:: list-machines [PATTERN...]

   List the host and all running local containers with their state. If one or more PATTERNs are specified, only containers matching one of them are shown.

ジョブコマンド
^^^^^^^^^^^^^^^^^

.. object:: list-jobs [PATTERN...]

   List jobs that are in progress. If one or more PATTERNs are specified, only jobs for units matching one of them are shown.

   When combined with --after or --before the list is augmented with information on which other job each job is waiting for, and which other jobs are waiting for it, see above.

.. object:: cancel JOB...

   Cancel one or more jobs specified on the command line by their numeric job IDs. If no job ID is specified, cancel all pending jobs.

環境コマンド
^^^^^^^^^^^^^^^

.. object:: show-environment

   Dump the systemd manager environment block. This is the environment block that is passed to all processes the manager spawns. The environment block will be dumped in straight-forward form suitable for sourcing into most shells. If no special characters or whitespace is present in the variable values, no escaping is performed, and the assignments have the form "VARIABLE=value". If whitespace or characters which have special meaning to the shell are present, dollar-single-quote escaping is used, and assignments have the form "VARIABLE=$'value'". This syntax is known to be supported by bash(1), zsh(1), ksh(1), and busybox(1)'s ash(1), but not dash(1) or fish(1).

.. object:: set-environment VARIABLE=VALUE...

   Set one or more systemd manager environment variables, as specified on the command line.

.. object:: unset-environment VARIABLE...

   Unset one or more systemd manager environment variables. If only a variable name is specified, it will be removed regardless of its value. If a variable and a value are specified, the variable is only removed if it has the specified value.

.. object:: import-environment [VARIABLE...]

   Import all, one or more environment variables set on the client into the systemd manager environment block. If no arguments are passed, the entire environment block is imported. Otherwise, a list of one or more environment variable names should be passed, whose client-side values are then imported into the manager's environment block.

マネージャライフサイクルコマンド
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. object:: daemon-reload

   Reload the systemd manager configuration. This will rerun all generators (see systemd.generator(7)), reload all unit files, and recreate the entire dependency tree. While the daemon is being reloaded, all sockets systemd listens on behalf of user configuration will stay accessible.

   This command should not be confused with the reload command.

.. object:: daemon-reexec

   Reexecute the systemd manager. This will serialize the manager state, reexecute the process and deserialize the state again. This command is of little use except for debugging and package upgrades. Sometimes, it might be helpful as a heavy-weight daemon-reload. While the daemon is being reexecuted, all sockets systemd listening on behalf of user configuration will stay accessible.

システムコマンド
^^^^^^^^^^^^^^^^^^^

.. object:: is-system-running

   Checks whether the system is operational. This returns success (exit code 0) when the system is fully up and running, specifically not in startup, shutdown or maintenance mode, and with no failed services. Failure is returned otherwise (exit code non-zero). In addition, the current state is printed in a short string to standard output, see the table below. Use --quiet to suppress this output.

   .. list-table:: 表 2. is-system-running の出力
      :header-rows: 1
      :widths: 1, 7, 1

      * - 名前
        - 説明
        - 終了コード
      * - *initializing*
        - 起動初期段階、basic.target に達する前、あるいは *maintenance* ステートに入る前。
        - > 0
      * - *starting*
        - 起動後期段階、ジョブキューが最初に待機状態になる前、あるいはレスキューターゲットのどれかに達する前。
        - > 0
      * - *running*
        - システムが完全に機能している状態。
        - 0
      * - *degraded*
        - システムは機能しているがひとつあるいは複数のユニットの起動に失敗している。
        - > 0
      * - *maintenance*
        - レスキューあるいは緊急ターゲットがアクティブ。
        - > 0
      * - *stopping*
        - マネージャがシャットダウンされている。
        - > 0
      * - *offline*
        - マネージャが動作していない。システムマネージャ (PID 1) として互換性のないプログラムが動作している場合の状態。
        - > 0
      * - *unknown*
        - リソースが不足していたりエラーが発生しているために動作状態が確認できない。
        - > 0

.. object:: default

   Enter default mode. This is equivalent to systemctl isolate default.target. This operation is blocking by default, use --no-block to request asynchronous behavior.

.. object:: rescue

   Enter rescue mode. This is equivalent to systemctl isolate rescue.target. This operation is blocking by default, use --no-block to request asynchronous behavior.

.. object:: emergency

   Enter emergency mode. This is equivalent to systemctl isolate emergency.target. This operation is blocking by default, use --no-block to request asynchronous behavior.

.. object:: halt

   Shut down and halt the system. This is mostly equivalent to systemctl start halt.target --job-mode=replace-irreversibly --no-block, but also prints a wall message to all users. This command is asynchronous; it will return after the halt operation is enqueued, without waiting for it to complete. Note that this operation will simply halt the OS kernel after shutting down, leaving the hardware powered on. Use systemctl poweroff for powering off the system (see below).

   If combined with --force, shutdown of all running services is skipped, however all processes are killed and all file systems are unmounted or mounted read-only, immediately followed by the system halt. If --force is specified twice, the operation is immediately executed without terminating any processes or unmounting any file systems. This may result in data loss. Note that when --force is specified twice the halt operation is executed by systemctl itself, and the system manager is not contacted. This means the command should succeed even when the system manager has crashed.

.. object:: poweroff

   Shut down and power-off the system. This is mostly equivalent to systemctl start poweroff.target --job-mode=replace-irreversibly --no-block, but also prints a wall message to all users. This command is asynchronous; it will return after the power-off operation is enqueued, without waiting for it to complete.

   If combined with --force, shutdown of all running services is skipped, however all processes are killed and all file systems are unmounted or mounted read-only, immediately followed by the powering off. If --force is specified twice, the operation is immediately executed without terminating any processes or unmounting any file systems. This may result in data loss. Note that when --force is specified twice the power-off operation is executed by systemctl itself, and the system manager is not contacted. This means the command should succeed even when the system manager has crashed.

.. object:: reboot [arg]

   Shut down and reboot the system. This is mostly equivalent to systemctl start reboot.target --job-mode=replace-irreversibly --no-block, but also prints a wall message to all users. This command is asynchronous; it will return after the reboot operation is enqueued, without waiting for it to complete.

   If combined with --force, shutdown of all running services is skipped, however all processes are killed and all file systems are unmounted or mounted read-only, immediately followed by the reboot. If --force is specified twice, the operation is immediately executed without terminating any processes or unmounting any file systems. This may result in data loss. Note that when --force is specified twice the reboot operation is executed by systemctl itself, and the system manager is not contacted. This means the command should succeed even when the system manager has crashed.

   If the optional argument arg is given, it will be passed as the optional argument to the reboot(2) system call. The value is architecture and firmware specific. As an example, "recovery" might be used to trigger system recovery, and "fota" might be used to trigger a “firmware over the air” update.

.. object:: kexec

   Shut down and reboot the system via kexec. This is equivalent to systemctl start kexec.target --job-mode=replace-irreversibly --no-block. This command is asynchronous; it will return after the reboot operation is enqueued, without waiting for it to complete.

   If combined with --force, shutdown of all running services is skipped, however all processes are killed and all file systems are unmounted or mounted read-only, immediately followed by the reboot.

.. object:: exit [EXIT_CODE]

   Ask the service manager to quit. This is only supported for user service managers (i.e. in conjunction with the --user option) or in containers and is equivalent to poweroff otherwise. This command is asynchronous; it will return after the exit operation is enqueued, without waiting for it to complete.

   The service manager will exit with the specified exit code, if EXIT_CODE is passed.

.. object:: switch-root ROOT [INIT]

   Switches to a different root directory and executes a new system manager process below it. This is intended for usage in initial RAM disks ("initrd"), and will transition from the initrd's system manager process (a.k.a. "init" process) to the main system manager process which is loaded from the actual host volume. This call takes two arguments: the directory that is to become the new root directory, and the path to the new system manager binary below it to execute as PID 1. If the latter is omitted or the empty string, a systemd binary will automatically be searched for and used as init. If the system manager path is omitted, equal to the empty string or identical to the path to the systemd binary, the state of the initrd's system manager process is passed to the main system manager, which allows later introspection of the state of the services involved in the initrd boot phase.

.. object:: suspend

   Suspend the system. This will trigger activation of the special target unit suspend.target. This command is asynchronous, and will return after the suspend operation is successfully enqueued. It will not wait for the suspend/resume cycle to complete.

.. object:: hibernate

   Hibernate the system. This will trigger activation of the special target unit hibernate.target. This command is asynchronous, and will return after the hibernation operation is successfully enqueued. It will not wait for the hibernate/thaw cycle to complete.

.. object:: hybrid-sleep

   Hibernate and suspend the system. This will trigger activation of the special target unit hybrid-sleep.target. This command is asynchronous, and will return after the hybrid sleep operation is successfully enqueued. It will not wait for the sleep/wake-up cycle to complete.

パラメータ構文
^^^^^^^^^^^^^^^^

   Unit commands listed above take either a single unit name (designated as UNIT), or multiple unit specifications (designated as PATTERN...). In the first case, the unit name with or without a suffix must be given. If the suffix is not specified (unit name is "abbreviated"), systemctl will append a suitable suffix, ".service" by default, and a type-specific suffix in case of commands which operate only on specific unit types. For example,

   .. code-block:: console

      # systemctl start sshd

   and

   .. code-block:: console

      # systemctl start sshd.service

   are equivalent, as are

   .. code-block:: console

      # systemctl isolate default

   and

   .. code-block:: console

      # systemctl isolate default.target

   Note that (absolute) paths to device nodes are automatically converted to device unit names, and other (absolute) paths to mount unit names.

   .. code-block:: console

      # systemctl status /dev/sda
      # systemctl status /home

   are equivalent to:

   .. code-block:: console

      # systemctl status dev-sda.device
      # systemctl status home.mount

   In the second case, shell-style globs will be matched against the primary names of all units currently in memory; literal unit names, with or without a suffix, will be treated as in the first case. This means that literal unit names always refer to exactly one unit, but globs may match zero units and this is not considered an error.

   Glob patterns use fnmatch(3), so normal shell-style globbing rules are used, and "*", "?", "[]" may be used. See glob(7) for more details. The patterns are matched against the primary names of units currently in memory, and patterns which do not match anything are silently skipped. For example:

   .. code-block:: console

      # systemctl stop sshd@*.service

   will stop all sshd@.service instances. Note that alias names of units, and units that aren't in memory are not considered for glob expansion.

   For unit file commands, the specified UNIT should be the name of the unit file (possibly abbreviated, see above), or the absolute path to the unit file:

   .. code-block:: console

      # systemctl enable foo.service

   or

   .. code-block:: console

      # systemctl link /path/to/foo.service

終了ステータス
---------------

成功時は 0 が返り、失敗時はゼロ以外のコードが返ります。

環境変数
----------

.. envvar:: $SYSTEMD_EDITOR

   ユニットを編集するときに使用数するエディタを指定します。*$EDITOR* と *$VISUAL* を上書きします。*$SYSTEMD_EDITOR*, *$EDITOR*, *$VISUAL* のいずれもが設定されていない場合や空文字に設定されている場合、あるいはコマンドの実行に失敗した場合、systemctl は有名なエディタを次の順番で実行できないか試行します: :doc:`editor.1`, :doc:`nano.1`, :doc:`vim.1`, :doc:`vi.1`。

.. envvar:: $SYSTEMD_PAGER

   Pager to use when --no-pager is not given; overrides $PAGER. If neither $SYSTEMD_PAGER nor $PAGER are set, a set of well-known pager implementations are tried in turn, including less(1) and more(1), until one is found. If no pager implementation is discovered no pager is invoked. Setting this environment variable to an empty string or the value "cat" is equivalent to passing --no-pager.

.. envvar:: $SYSTEMD_LESS

   Override the options passed to less (by default "FRSXMK").

.. envvar:: $SYSTEMD_LESSCHARSET

   Override the charset passed to less (by default "utf-8", if the invoking terminal is determined to be UTF-8 compatible).

関連項目
--------

:doc:`systemd.1`,
:doc:`journalctl.1`,
:doc:`loginctl.1`,
:doc:`machinectl.1`,
:doc:`systemd.unit.5`,
:doc:`systemd.resource-control.5`,
:doc:`systemd.special.7`,
:doc:`wall.1`,
:doc:`systemd.preset.5`,
:doc:`systemd.generator.7`,
:doc:`glob.7`

注釈
-------

.. [#] https://www.freedesktop.org/wiki/Software/systemd/Preset
