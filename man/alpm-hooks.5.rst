alpm-hooks(5)
==================

名称
--------

alpm-hooks - alpm フックファイルフォーマット

書式
--------

| [Trigger] (Required, Repeatable)
| Operation = Install|Upgrade|Remove (Required, Repeatable)
| Type = File|Package (Required)
| Target = <Path|PkgName> (Required, Repeatable)

| [Action] (Required)
| Description = ... (Optional)
| When = PreTransaction|PostTransaction (Required)
| Exec = <Command> (Required)
| Depends = <PkgName> (Optional)
| AbortOnFail (Optional, PreTransaction only)
| NeedsTargets (Optional)

説明
-----------

libalpm はパッケージのトランザクションやファイルの変更の前後に指定されたフックを実行する機能を備えています。フックは実行するアクションを記述したひとつの *[Action]* セクションと、どのトランザクションで実行するべきかを記述したひとつあるいは複数の *[Trigger]* セクションからなります。フックファイルの名前には拡張子として ".hook" が必要です。フックはファイル名のアルファベット順で実行されます。

トリガー
------------

フックには最低でもひとつの *[Trigger]* セクションが必要で、フックを実行するトランザクションを記述します。複数のトリガーセクションを定義した場合、トリガーのどれかにトランザクションが一致すればフックは実行されます。

.. object:: Operation = Install|Upgrade|Remove

   操作のタイプを選択します。複数回指定することが可能です。パッケージやファイルがシステム上に既に存在する場合、新しいパッケージのバージョンが現在インストールされているバージョンよりも大きいかどうかとは関係なくインストールはアップグレードとして認識されます。File トリガーの場合、パッケージによってファイルの所有権が変化する場合も同じように認識されます。必須の項目です。

.. object:: Type = File|Package

   トランザクションの対象がパッケージあるいはファイルのどちらであるか選択します。File トリガーに関する下の注意事項を見てください。必須の項目です。

.. object:: Target = <path|package>

   トリガーを発動するファイルのパスあるいはパッケージの名前を指定します。ファイルのパスはパッケージアーカイブの中のファイルを参照するようにしてください。パスの中にインストールルートは含めてはいけません。シェル式の glob パターンを使うことができます。エクスクラメーションマークをファイルの前に付けることで除外するファイルを指定することもできます。複数回指定することが可能です。必須の項目です。

アクション
--------------------

.. object:: Description = ...

   フロントエンドの出力で使用されるアクションの任意の説明。

.. object:: Exec = <command>

   実行するコマンド。コマンド引数は空白で区切ってください。空白を含む値はクォートで囲ってください。必須の項目です。

.. object:: When = PreTransaction|PostTransaction

   いつフックを実行するか。必須の項目です。

.. object:: Depends = <package>

   フックを実行するのにインストールが必要なパッケージ。複数回指定できます。

.. object:: AbortOnFail

   フックがゼロ以外で終了したときにトランザクションを中止します。PreTransaction フックにのみ適用されます。

.. object:: NeedsTargets

   マッチしたトリガーターゲットのリストが実行するフックに標準入力で渡されます。

フックの上書き
---------------

優先度が高いフックディレクトリに同じ名前のファイルを配置することでフックは上書きすることができます。*/dev/null* へのシンボリックリンクを作成して上書きした場合はフックは無効化されます。

サンプル
---------------

.. code-block:: ini

   # Force disks to sync to reduce the risk of data corruption

   [Trigger]
   Operation = Install
   Operation = Upgrade
   Operation = Remove
   Type = Package
   Target = *

   [Action]
   Depends = coreutils
   When = PostTransaction
   Exec = /usr/bin/sync

注意事項
--------

ファイルトリガーは予期しない形で動作してしまう状況というものが存在します。フックはインストール・アップグレード・削除されるパッケージのファイルリストを使って実行されます。*.pacnew* 拡張子で展開されたファイルをインストール・アップグレードするとき、フックを実行するときはオリジナルのファイル名が使われます。パッケージを削除するとき、ファイルシステムにファイルが存在しているかどうかに関係なくパッケージに含まれている全てのファイルによってフックは実行されます。

PostTransaction フックはトランザクションが何らかの理由で完了しなかった場合は実行されません。

pacman とその関連ツールの最新情報は pacman のウェブサイト https://www.archlinux.org/pacman/ を見てください。

バグ
----------

このソフトウェアにバグは存在しません。バグを発見したら、できるかぎり詳しくバグの内容を記述して pacman-dev@archlinux.org にメールを送信してください。

著者
----------

現在のメンテナ:

   * Allan McRae <allan@archlinux.org>
   * Andrew Gregory <andrew.gregory.8@gmail.com>
   * Dan McGee <dan@archlinux.org>
   * Dave Reisner <dreisner@archlinux.org>

過去の主要貢献者:

   * Judd Vinet <jvinet@zeroflux.org>
   * Aurelien Foret <aurelien@archlinux.org>
   * Aaron Griffin <aaron@archlinux.org>
   * Xavier Chantry <shiningxc@gmail.com>
   * Nagy Gabor <ngaba@bibl.u-szeged.hu>

他の貢献者については pacman.git リポジトリで git shortlog -s を使って確認できます。
