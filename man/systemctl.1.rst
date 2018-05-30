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

   指定したユニットがサポートしている場合、動作中のユニットのプロパティを設定します。動作を止めることなくリソース制御などの設定パラメータを変更することができます。全てのプロパティが動作中に変更できるわけではありませんが、リソース制御の設定の多くは変更可能です (主として :doc:`systemd.resource-control.5` の設定)。変更は即座に適用され、**--runtime** が指定されないかぎりディスクに変更が保存されて今後も変更が適用されます。指定した場合は次の起動時には変更は元に戻ります。プロパティの指定方法はユニットファイル内での設定の指定方法と似ています。

   例: **systemctl set-property foobar.service CPUShares=777**

   指定したユニットが動作していなかった場合、変更はディスクに保存されてユニットの起動時に変更が適用されます。

   このコマンドでは同時に複数のプロパティを変更できます。別々に設定するよりも同時に設定することが推奨されます。ユニットファイルの設定と同じように、空のリストを指定するとプロパティがリセットされます。

.. object:: help PATTERN...|PID...

   ひとつまたは複数のユニットのマニュアルページを表示します。PID を指定した場合、プロセスが属しているユニットのマニュアルページが表示されます。

.. object:: reset-failed [PATTERN...]

   指定したユニットの "failed" 状態をリセットします。ユニット名を指定しなかった場合、全てのユニットの状態がリセットされます。ユニットが何らかの理由で失敗した場合 (プロセスがゼロ以外のエラーコードで終了した、あるいは異常終了・タイムアウトしたなど)、ユニットは自動的に "failed" 状態になり、サービスが停止・再起動されたりこのコマンドでリセットされるまで、管理者が調査できるように終了コードと状態が記録されます。

.. object:: list-dependencies [UNIT]

   指定したユニットが依存しているユニットを表示します。*Requires=*, *Requisite=*, *ConsistsOf=*, *Wants=*, *BindsTo=* 依存を追って再帰的にユニットが表示されます。ユニットを指定しなかった場合、default.target の依存が表示されます。

   デフォルトでは、再帰的に依存関係が表示されるのはターゲットユニットだけです。**--all** を指定することで、他のユニットも再帰的に依存関係を表示するようになります。

   **--reverse**, **--after**, **--before** を使うことでどのタイプの依存を表示するのか変更できます。

ユニットファイルコマンド
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. object:: list-unit-files [PATTERN...]

   システムにインストールされているユニットファイルと (**is-enabled** で確認できる) 有効化状態を列挙します。ひとつまたは複数の *PATTERN* を指定した場合、パターンに名前がマッチするユニットファイルだけが表示されます (ユニットファイルのファイルシステムパスにパターンをマッチさせることはできません)。

.. object:: enable UNIT..., enable PATH...

   ひとつまたは複数のユニット、あるいはユニットインスタンスを有効化します。有効化すると指定したユニットファイルの "[Install]" セクションの記述に従って、シンボリックリンクが作成されます。シンボリックリンクを作成した後、変更を即座に適用するためにシステムマネージャの設定がリロードされます (**daemon-reload** と同じ)。ただし有効化されたユニットがすぐに起動するというわけではないので注意してください。ユニットを有効化してから起動したい場合、**--now** スイッチを付けて実行するか、あるいは後から **start** コマンドを実行してください。ユニットインスタンス (foo@bar.service という形式のユニット) を有効化した場合、インスタンスと同じ名前のシンボリックリンクがユニットの設定ディレクトリに作成されます。リンク先はインスタンス化する元のテンプレートユニットファイルになります。

   このコマンドでは適当なユニットの名前を指定するか (その場合は指定した名前で様々なユニットファイルのディレクトリが自動で検索されます)、あるいはユニットファイルの絶対パスを指定します (その場合は直接そのファイルが読み込まれます)。指定したユニットファイルが通常のユニットファイルのディレクトリにない場合、追加のシンボリックリンクが作成され、ユニットの設定パスにリンクが張られて、**start** などのコマンドで認識するようになります。リンク先のユニットファイルが存在するファイルシステムは systemd が起動したときにアクセスできるパスでないといけません (例: /home や /var 下のディレクトリはルートファイルシステム上にないかぎり使用できません)。

   このコマンドは実行されるファイルシステム操作を出力します。**--quiet** を指定することで出力は消すことができます。

   この操作ではユニットファイルの "[Install]" セクションに書かれているようにシンボリックリンクを作成することだけが行われます。ユニットの設定ディレクトリを操作するときはこのコマンドを使うことが推奨されますが、管理者はディレクトリに手動でシンボリックリンクを作成・削除することでも設定を変更できます。特にデフォルトのインストール環境から派生した設定を作成したい場合に有用です。その場合、管理者は必要に応じて **daemon-reload** を手動で実行して、変更を適用するようにしてください。

   ユニットの有効化はユニットの起動 (アクティベート) とは異なります。起動は **start** コマンドを使います。ユニットの有効化と起動は基本的に独立した操作です: ユニットは起動せずに有効化したり、逆に有効化せずに起動することができます。有効化では単にユニットが適当な場所にフックされます (例えば、ユニットがブート時に自動的に起動したり、特定のハードウェアを接続したときに起動するようになります)。起動では実際にデーモンプロセスが生成されたり (サービスユニットの場合)、ソケットがバインドされたり (ソケットユニットの場合) します。

   **--system**, **--user**, **--runtime**, **--global** を指定することで、ユニットをシステム全体で有効化したり、呼び出したユーザー限定で有効化したり、次回のブート限定で有効化したり、全てのユーザーの今後のログイン全てで有効化することができます。最後の場合、systemd のデーモン設定はリロードされません。

   マスク化されたユニットを **enable** することはできずエラーが返ります。

.. object:: disable UNIT...

   ひとつまたは複数のユニットを無効化します。ユニットの設定ディレクトから指定したユニットに関連するユニットファイルのシンボリックリンクが削除され、**enable** や **link** による変更が元に戻されます。ユニットファイルにマッチする全てのシンボリックリンクが削除されるので注意してください。手動で作成したシンボリックリンクなど **enable** や **link** では作成していないシンボリックリンクも削除されます。**disable** は **enable** による効果を元に戻しますが、2つのコマンドは決して対称ではなく、**enable** によって作成されたシンボリックリンクよりも **disable** によって削除されるシンボリックリンクのほうが多いこともあります。

   このコマンドは適当なユニットの名前だけしか指定できません。ユニットファイルのパスは指定できません。

   引数として指定されたユニットだけでなく、対象のユニットファイルの "[Install]" セクションに記述されている *Also=* 設定に列挙されているユニットも無効化されます。

   このコマンドは操作が完了した後に黙示的にシステムマネージャの設定をリロードします。このコマンドで無効化されたユニットは黙示的に停止されないので注意してください。ユニットを止めたいときは、このコマンドに **--now** スイッチを組み合わせるか、あるいは後で **stop** コマンドを実行してください。

   このコマンドは実行されるファイルシステムの操作 (シンボリックリンクの削除) についての情報を出力します。**--quiet** を指定することで出力は消すことができます。

   このコマンドでは **enable** と同じように **--system**, **--user**, **--runtime**, **--global** を認識します。

.. object:: reenable UNIT...

   コマンドラインで指定した、ひとつまたは複数のユニットを再有効化します。再有効化は **disable** と **enable** の組み合わせで、有効化したユニットファイルのシンボリックリンクを "[Install]" セクションに設定されたデフォルトにリセットしたい場合に有用です。このコマンドはユニットの名前だけしか指定できません。ユニットファイルのパスは指定できません。

.. object:: preset UNIT...

   コマンドラインで指定した、ひとつまたは複数のユニットファイルの有効化・無効化状態をリセットして、プリセットポリシーファイルに設定されたデフォルト状態に戻します。プリセットファイルにユニットが記述されているかどうかに応じて、**disable** あるいは **enable** と全く同じ操作が行われます。

   ユニットの有効化・無効化の両方を行う、あるいは有効化・無効化のどちらかしか行われないように制御したい場合、**--preset-mode=** を使ってください。

   ユニットにインストール情報が記載されていない場合、このコマンドは特にエラーを吐かずに終了します。*UNIT* はユニットの正確な名前である必要があり、エイリアス名は無視されます。

   プリセットポリシーのフォーマットについて詳しくは :doc:`systemd.preset.5` を見てください。プリセットの概念についての情報は **Preset** [#]_ ドキュメントを読んでください。

.. object:: preset-all

   インストールされている全てのユニットファイルをプリセットポリシーファイル (上を参照) で設定されているデフォルト状態にリセットします。

   ユニットの有効化・無効化の両方を行う、あるいは有効化・無効化のどちらかしか行われないように制御したい場合、**--preset-mode=** を使ってください。

.. object:: is-enabled UNIT...

   指定したユニットファイルが (**enable** によって) 有効化されているかどうか確認します。指定されたユニットの中で有効化されているユニットがない場合は終了コード 0 が返り、それ以外の場合は 0 以外の値が返ります。現在の有効化状態が出力されます (表を参照)。出力を消すには、**--quiet** を使ってください。インストールターゲットを表示したい場合は **--full** を使ってください。

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

   コマンドラインで指定したひとつまたは複数のユニットをマスクします。指定されたユニットファイルは /dev/null にリンクされ、ユニットを起動することができなくなります。これは **disable** よりも強力で、有効化や手動アクティベーションを含む、あらゆる種類のアクティベーションがユニットに効かなくなります。このオプションは注意して使ってください。**--runtime** オプションと組み合わせることで次回起動時まで一時的にマスクすることもできます。**--now** オプションを使用するとユニットの停止も行われます。このコマンドはユニットの名前しか認識せず、ユニットファイルのパスを指定することはできません。

.. object:: unmask UNIT...

   コマンドラインで指定したひとつまたは複数のユニットファイルのマスクを解除します。**mask** の効果が元に戻されます。このコマンドはユニットの名前しか認識せず、ユニットファイルのパスを指定することはできません。

.. object:: link PATH...

   ユニットファイルの検索パスに存在しないユニットファイルをユニットファイルの検索パスにリンクします。このコマンドではユニットファイルの絶対パスを指定してください。このコマンドによる操作は **disable** で元に戻すことができます。このコマンドを使うことでユニットの検索に直接インストールされていなくても、**start** などのコマンドでユニットファイルを使うことができるようになります。リンクを作成するユニットファイルが存在するファイルシステムは systemd が起動したときにアクセスできなくてはなりません (例: /home や /var 下のディレクトリはルートファイルシステム上にないかぎり使用できません)。

.. object:: revert UNIT...

   ひとつまたは複数のユニットファイルをディストリビューションが提供しているバージョンにリバートします。このコマンドは指定したユニットに変更を加えるドロップイン設定ファイルを削除し、ディストリビューションが提供するユニットファイルを上書きするようにユーザーが設定したユニットファイルも削除されます。例えば "foo.service" ユニットに対応する永続的・一時的な設定ディレクトリ (/etc/systemd/system と /run/systemd/system) の "foo.service.d/" ディレクトリに含まれているファイルは全て削除されます。ユニットファイルにディストリビューションが提供するバージョン (/usr 下のユニットファイル) が存在する場合、同名の永続的・一時的な上書きユニットファイルも削除されます。ユニットファイルにディストリビューション提供バージョンが存在しない場合 (/etc/systemd/system または /run/systemd/system でのみ定義されており /usr に同名のユニットファイルが保存されていない場合)、ユニットファイルは削除されません。また、ユニットがマスクされている場合、マスクが解除されます。

   事実上、このコマンドは **systemctl edit**, **systemctl set-property**, **systemctl mask** による変更を全て差し戻してオリジナルのユニットファイルに設定をリセットします。

.. object:: add-wants TARGET UNIT..., add-requires TARGET UNIT...

   ひとつまたは複数のユニットを指定した *TARGET* の "Wants=" または "Requires=" 依存に追加します。

   このコマンドは **enable** と同じように **--system**, **--user**, **--runtime**, **--global** を認識します。

.. object:: edit UNIT...

   指定したユニットを拡張・上書きするドロップインスニペットあるいは (**--full** を指定した場合は) 置換ファイルを編集します。

   **--system** (デフォルト), **--user**, **--global** のどれを指定したかによって、ユニットのドロップインファイルが作成される場所が変わり、それぞれシステム全体・コマンドを実行したユーザー・全てのユーザーの全てのログインに反映されます。そして一時ファイルでエディタ (下の `環境変数`_ セクションを参照) が起動して、エディタが正しく終了すると実際の場所にファイルが書き込まれます。

   **--full** を指定した場合、ドロップインファイルを作成するかわりにオリジナルのユニットがコピーされます。

   **--force** を指定して既存のユニットが存在しない場合、新しいユニットファイルが開かれます。

   **--runtime** を指定した場合、変更は /run に一時的に作成されるため次回起動時に変更は失われます。

   エディタの終了時に一時ファイルが空だった場合、ユニットの編集はキャンセルされます。

   ユニットを編集したら、systemd の設定がリロードされます (**daemon-reload** と同じ効果)。

   このコマンドではリモートでユニットを編集したり /etc に存在するユニットを一時的に編集することはできません。/run よりも優先して使われるためです。

.. object:: get-default

   デフォルトの起動ターゲットを返します。default.target にエイリアス (シンボリックリンク) されているターゲットのユニット名が返されます。

.. object:: set-default TARGET

   デフォルトの起動ターゲットを設定します。指定したターゲットユニットに default.target エイリアス (シンボリックリンク) が設定されます。

マシンコマンド
^^^^^^^^^^^^^^^^^

.. object:: list-machines [PATTERN...]

   ホストと実行中のローカルコンテナとコンテナの状態を列挙します。ひとつまたは複数の *PATTERN* が指定された場合、パターンにマッチするコンテナだけが表示されます。

ジョブコマンド
^^^^^^^^^^^^^^^^^

.. object:: list-jobs [PATTERN...]

   進行中のジョブを一覧表示します。ひとつまたは複数の *PATTERN* が指定された場合、パターンにマッチするユニットのジョブだけが表示されます。

   **--after** または **--before** と組み合わせることでジョブが待機する他のジョブ、あるいはどのジョブによって待機されるか情報が追加されます。上を参照。

.. object:: cancel JOB...

   コマンドラインから数字のジョブ ID で指定したひとつまたは複数のジョブを取り消します。ジョブ ID を指定しなかった場合、保留中の全てのジョブが取り消されます。

環境コマンド
^^^^^^^^^^^^^^^

.. object:: show-environment

   systemd マネージャの環境変数ブロックがダンプされます。マネージャが生成する全てのプロセスに渡されるものと同じ環境ブロックです。環境ブロックはシェルから読み込むことができる形式で出力されます。環境変数の値に特殊文字や空白が含まれていない場合、エスケープは行われず、"VARIABLE=value" という形式で吐き出されます。空白やシェルにとって特殊な文字が含まれている場合、ドル記号とシングルクォートによるエスケープが使われ、"VARIABLE=$'value'" という形式で吐き出されます。この形式は :doc:`bash.1`, :doc:`zsh.1`, :doc:`ksh.1`, :doc:`busybox.1` の :doc:`ash.1` でサポートされていますが、:doc:`dash.1` と :doc:`fish.1` ではサポートされていません。

.. object:: set-environment VARIABLE=VALUE...

   コマンドラインで指定したひとつまたは複数の systemd マネージャの環境変数を設定。

.. object:: unset-environment VARIABLE...

   ひとつまたは複数の systemd マネージャ環境変数の設定を解除。変数名だけ指定された場合、変数の値は関係なく変数が削除されます。変数と値が指定された場合、値が一致している場合にのみ変数が削除されます。

.. object:: import-environment [VARIABLE...]

   クライアントに設定されている全て、あるいはひとつ・複数の環境変数を systemd マネージャの環境変数ブロックにインポートします。引数を指定しなかった場合、環境変数ブロック全てがインポートされます。ひとつまたは複数の環境変数の名前を指定した場合、指定した環境変数のクライアントの値がマネージャの環境変数ブロックにインポートされます。

マネージャライフサイクルコマンド
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. object:: daemon-reload

   systemd マネージャの設定をリロードします。全てのジェネレータが実行され (:doc:`systemd.generator.7` を参照)、全てのユニットファイルがリロードされ、全ての依存関係ツリーが再生成されます。デーモンがリロード中のときでも、systemd が listen しているソケットには全てアクセス可能です。

   このコマンドは **reload** コマンドとは異なるので注意してください。

.. object:: daemon-reexec

   systemd マネージャを再実行します。マネージャの状態をシリアライズしてから、プロセスが再実行され、それから状態がデシリアライズされます。デバッグやパッケージアップグレード以外でこのコマンドを使うことはほぼありません。場合によっては強力な **daemon-reload** として使えることもあります。デーモンが再実行中のときでも、systemd が listen しているソケットには全てアクセス可能です。

システムコマンド
^^^^^^^^^^^^^^^^^^^

.. object:: is-system-running

   システムが動作可能な状態か確認します。システムが完全に立ち上がって動作しているときは成功 (終了コード 0) が返りますが、起動・シャットダウン中のときやメンテナンスモードの場合、あるいはサービスの起動が失敗したときは失敗 (ゼロ以外の終了コード) が返ります。さらに、現在の状態が以下の表のように標準出力に短く表示されます。出力を消したいときは **--quiet** を使ってください。

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

   デフォルトモードに入ります。**systemctl isolate default.target** と同等のコマンドです。この操作はデフォルトでブロッキングを行いますが、**--no-block** を使うことで非同期に行うことができます。

.. object:: rescue

   レスキューモードに入ります。**systemctl isolate rescue.target** と同等のコマンドです。この操作はデフォルトでブロッキングを行いますが、**--no-block** を使うことで非同期に行うことができます。

.. object:: emergency

   緊急モードに入ります。**systemctl isolate emergency.target** と同等のコマンドです。この操作はデフォルトでブロッキングを行いますが、**--no-block** を使うことで非同期に行うことができます。

.. object:: halt

   システムをシャットダウンして停止します。**systemctl start halt.target --job-mode=replace-irreversibly --no-block** とほぼ同等のコマンドですが、ウォールメッセージは全てのユーザーに出力されます。このコマンドは非同期です。停止コマンドがキューに入るとすぐに操作が返ります。完了するまで待機することはありません。この操作ではシャットダウン後に OS カーネルを停止することだけ行い、ハードウェアは電源が入ったままの状態になるので注意してください。システムの電源を切りたいときは **systemctl poweroff** を使ってください (下を参照)。

   **--force** と組み合わせた場合、実行中のサービスのシャットダウンがスキップされますが、プロセスは全て終了して全てのファイルシステムがアンマウントあるいは読み取り専用でマウントされ、その後すぐにシステムが停止します。**--force** を2回指定した場合、プロセスの終了やファイルシステムのアンマウントも省いて即座に操作が実行されます。この場合はデータが喪失する可能性があります。**--force** が2回指定されたとき停止操作は **systemctl** 自身によって実行され、システムマネージャには接続されません。このため、システムマネージャがクラッシュしていてもコマンドは通ります。

.. object:: poweroff

   システムをシャットダウンして電源オフにします。**systemctl start poweroff.target --job-mode=replace-irreversibly --no-block** とほぼ同等のコマンドですが、全てのユーザーにウォールメッセージが出力されます。このコマンドは非同期です。電源オフ操作がキューに入るとすぐに操作が返り、完了するまで待機することはありません。

   **--force** と組み合わせた場合、実行中のサービスのシャットダウンがスキップされますが、プロセスは全て終了して全てのファイルシステムがアンマウントあるいは読み取り専用でマウントされ、その後すぐにシステムの電源を切ります。**--force** を2回指定した場合、プロセスの終了やファイルシステムのアンマウントも省いて即座に操作が実行されます。この場合はデータが喪失する可能性があります。**--force** が2回指定されたとき停止操作は **systemctl** 自身によって実行され、システムマネージャには接続されません。このため、システムマネージャがクラッシュしていてもコマンドは通ります。

.. object:: reboot [arg]

   システムをシャットダウンして再起動します。**systemctl start reboot.target --job-mode=replace-irreversibly --no-block** とほぼ同等のコマンドですが、全てのユーザーにウォールメッセージが出力されます。このコマンドは非同期です。再起動操作がエンキューされるとすぐに操作が返り、完了するまで待機しません。

   **--force** と組み合わせた場合、実行中のサービスのシャットダウンがスキップされますが、プロセスは全て終了して全てのファイルシステムがアンマウントあるいは読み取り専用でマウントされ、その後すぐに再起動が実行されます。**--force** を2回指定した場合、プロセスの終了やファイルシステムのアンマウントも省いて即座に操作が実行されます。この場合はデータが喪失する可能性があります。**--force** が2回指定されたとき再起動操作は **systemctl** 自身によって実行され、システムマネージャには接続されません。そのため、システムマネージャがクラッシュしていてもコマンドは通ります。

   任意引数の *arg* を指定すると、:doc:`reboot.2` システムコールに任意引数として渡されます。値はアーキテクチャやファームウェアによって異なります。例えばシステムリカバリを実行するのに "recovery" と指定したり、“firmware over the air” (FOTA) アップデートを実行するのに "fota" と指定したりします。

.. object:: kexec

   **kexec** でシステムをシャットダウンして再起動します。**systemctl start kexec.target --job-mode=replace-irreversibly --no-block** と同等のコマンドです。このコマンドは非同期です。再起動操作がエンキューされるとすぐに操作が返り、完了するまで待機しません。

   **--force** と組み合わせた場合、実行中のサービスのシャットダウンがスキップされますが、プロセスは全て終了して全てのファイルシステムがアンマウントあるいは読み取り専用でマウントされ、その後すぐに再起動が実行されます。

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
