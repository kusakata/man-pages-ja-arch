btrfs(8)
==================

名称
--------

btrfs - btrfs ファイルシステムを管理するツールボックス

書式
--------

**btrfs** <*command*> [<*args*>]

説明
-----------

**btrfs** ユーティリティは btrfs ファイルシステムを管理するためのツールボックスです。サブボリュームやデバイス、あるいはファイルシステム全体を操作するためのコマンドグループが存在します。**コマンド** セクションを見てください。

**btrfs-convert** や **btrfstune** など特定の作業のためのスタンドアロンツールも存在します。これらのツールは歴史的に分割されていたり、あるいはメインユーティリティにまだ統合されていません。詳しくは **スタンドアロンツール** セクションを見てください。

他のトピック (マウントオプションなど) については別のマニュアルページ :doc:`btrfs.5` を見てください。

コマンド構文
---------------

コマンドは全て省略形に縮めることができますが、スクリプトの中では完全なコマンド名を使うことを指定します。全てのコマンドグループにはそれぞれ **btrfs-** <*group*> という名前のマニュアルページが存在します。

例えば: :command:`btrfs subvolume snapshot` の代わりに :command:`btrfs sub snaps` として実行することができます。ただし、**btrfs file s** は実行できません。**file s** は **filesystem show** と **filesystem sync** のどちらとも解釈できるからです。

コマンド名が曖昧な場合、候補となるオプションのリストが出力されます。

特定のコマンドの概要を確認したい場合、*btrfs command --help* または *btrfs [command...] --help --full* で利用可能なオプションを確認できます。

コマンド
------------

:command:`balance`
   ひとつ、または複数のデバイス間にまたがる btrfs ファイルシステムのチャンクを再配置します。

   詳しくは :doc:`btrfs-balance.8` を参照してください。

:command:`check`
   btrfs ファイルシステムのオフラインチェックを実行します。

   詳しくは :doc:`btrfs-check.8` を参照してください。

:command:`device`
   btrfs によって管理するデバイスを管理・追加・削除・スキャンします。

   詳しくは :doc:`btrfs-device.8` を参照してください。

:command:`filesystem`
   ラベルの設定や同期など btrfs ファイルシステムを管理します。

   詳しくは :doc:`btrfs-filesystem.8` を参照してください。

:command:`inspect-internal`
   開発者・ハッカー用のデバッグツール。

   詳しくは :doc:`btrfs-inspect-internal.8` を参照してください。

:command:`property`
   btrfs オブジェクトのプロパティを取得・設定。

   詳しくは :doc:`btrfs-property.8` を参照してください。

:command:`qgroup`
   btrfs ファイルシステムのクォータグループ (qgroup) を管理。

   詳しくは :doc:`btrfs-qgroup.8` を参照してください。

:command:`quota`
   btrfs ファイルシステムのクォータを管理。クォータの有効化や再スキャンなど。

   詳しくは :doc:`btrfs-quota.8` を参照してください。

:command:`receive`
   標準入力やファイルからサブボリュームデータを受信して復元など。

   詳しくは :doc:`btrfs-receive.8` を参照してください。

:command:`replace`
   btrfs デバイスの置換。

   詳しくは :doc:`btrfs-replace.8` を参照してください。

:command:`rescue`
   破損した btrfs ファイルシステムの救出を試みる。

   詳しくは :doc:`btrfs-rescue.8` を参照してください。

:command:`restore`
   破損した btrfs ファイルシステムからファイルの復元を試みる。

   詳しくは :doc:`btrfs-restore.8` を参照してください。

:command:`scrub`
   btrfs ファイルシステムのチェック。

   詳しくは :doc:`btrfs-scrub.8` を参照してください。

:command:`send`
   バックアップ用などにサブボリュームデータを標準出力やファイルに送信。

   詳しくは :doc:`btrfs-send.8` を参照してください。

:command:`subvolume`
   btrfs サブボリュームを作成・削除・確認・管理。

   詳しくは :doc:`btrfs-subvolume.8` を参照してください。

スタンドアロンツール
----------------------

新しい機能はスタンドアロンツールを使うことで利用できます。機能が有益であると認められたら、スタンドアロンツールは非推奨となってメインツールに機能がコピーされます。非推奨となってからしばらく時間がたつと (数年)、ツールは削除されます。

**btrfs** にまだ機能が移されていないツール:

btrfs-convert
   ext2/3/4 ファイルシステムを btrfs に変換

btrfstune
   アンマウントされているファイルシステムのファイルシステムプロパティを設定

btrfs-select-super
   スペアコピーからプライマリスーパーブロックを上書きするレスキューツール

btrfs-find-root
   ファイルシステムのツリールートを検索するレスキューヘルパー

非推奨・廃止されたツール:

btrfs-debug-tree
   **btrfs inspect-internal dump-tree** に移されました

btrfs-show-super
   **btrfs inspect-internal dump-super** に移されました

btrfs-zero-log
   **btrfs rescue zero-log** に移されました

終了ステータス
-----------------

**btrfs** は問題なく動いたときは終了ステータスとしてゼロを返します。問題が発生したときはゼロ以外が返ります。

使用方法
-----------

**btrfs** は btrfs-progs に含まれています。詳しくは btrfs wiki http://btrfs.wiki.kernel.org を参照してください。

関連項目
--------

:doc:`btrfs-balance.8`,
:doc:`btrfs-check.8`,
:doc:`btrfs-convert.8`,
:doc:`btrfs-device.8`,
:doc:`btrfs-filesystem.8`,
:doc:`btrfs-inspect-internal.8`,
:doc:`btrfs-property.8`,
:doc:`btrfs-qgroup.8`,
:doc:`btrfs-quota.8`,
:doc:`btrfs-receive.8`,
:doc:`btrfs-replace.8`,
:doc:`btrfs-rescue.8`,
:doc:`btrfs-restore.8`,
:doc:`btrfs-scrub.8`,
:doc:`btrfs-send.8`,
:doc:`btrfs-subvolume.8`,
:doc:`btrfstune.8`,
:doc:`mkfs.btrfs.8`
