bats(7)
==================

名称
--------

**bats** - Bats テストファイルフォーマット

説明
-----------

Bats テストファイルは特殊な構文でテストケースを定義した Bash スクリプトです。内部的には、各テストケースは説明が書かれたただの関数です。

.. code-block:: bash

   #!/usr/bin/env bats

   @test "addition using bc" {
     result="$(echo 2+2 | bc)"
     [ "$result" -eq 4 ]
   }

   @test "addition using dc" {
     result="$(echo 2 2+p | dc)"
     [ "$result" -eq 4 ]
   }

各 Bats テストファイルは n+1 回評価されます。n はファイル内のテストケースの数です。最初の実行時にテストケースの数がカウントされ、それから繰り返し別々のプロセスでテストケースが実行されます。

RUN ヘルパー
--------------

Bats テストの多くはコマンドの実行と終了ステータスと出力のアサーションが必要です。Bats にはコマンドとして引数を実行して、終了ステータスと出力を特殊なグローバル変数に保存し、ステータスコード **0** を返してテストケースのアサーションに続行することができる **run** ヘルパーが存在します。

例えば、**foo** コマンドをテストするとして、存在しないファイル名を指定したときに、ステータスコード **1** が返されてエラーメッセージが出力されることを確認するには:

.. code-block:: bash

   @test "invoking foo with a nonexistent file prints an error" {
     run foo nonexistent_filename
     [ "$status" -eq 1 ]
     [ "$output" = "foo: no such file ´nonexistent_filename´" ]
   }

**$status** 変数にはコマンドのステータスコードが入り、**$output** 変数にはコマンドの標準出力と標準エラーストリームが結合された文字列が入ります。

さらに、出力の各行に簡単にアクセスできるように特殊な変数 **$lines** 配列が用意されています。例えば何も引数を付けずに **foo** を実行したときに1行目に使用方法が出力されることをテストしたい場合:

.. code-block:: bash

   @test "invoking foo without arguments prints usage" {
     run foo
     [ "$status" -eq 1 ]
     [ "${lines[0]}" = "usage: foo <filename>" ]
   }

LOAD コマンド
--------------

複数のテストファイルで共通のコードを共有したいと思うかもしれません。Bats には現在のテストファイルから相対パスで Bash ソースファイルを読み込める便利な **load** コマンドが存在します。例えば、**test/foo.bats** に Bats テストがある場合、以下のコマンドでテストファイルに **test/test_helper.bash** スクリプトが読み込まれます:

.. code-block:: bash

   load test_helper

環境を設定したりフィクスチャをロードする関数を共有したい場合に有用です。

SKIP コマンド
--------------

テストのスキップしたい箇所で **skip** コマンドを使うことでテストをスキップできます。

.. code-block:: bash

   @test "A test I don´t want to execute for now" {
     skip
     run foo
     [ "$status" -eq 0 ]
   }

任意で、スキップの理由を記入することができます:

.. code-block:: bash

   @test "A test I don´t want to execute for now" {
     skip "This command will return zero soon, but not now"
     run foo
     [ "$status" -eq 0 ]
   }

条件付きでスキップすることもできます:

.. code-block:: bash

   @test "A test which should run" {
     if [ foo != bar ]; then
       skip "foo isn´t bar"
     fi

     run foo
     [ "$status" -eq 0 ]
   }

SETUP と TEARDOWN 関数
------------------------

特別な **setup** と **teardown** 関数を定義することで、テストケースの前と後に実行させることができます。これらの関数を使ってフィクスチャをロードしたり、環境を設定したり、テスト後のゴミを掃除することができます。

テストケースの外側のコード
----------------------------

テストファイルの **@test** 関数の外側にコードを記述することができます。例えば、依存関係をチェックして、満たされていない場合に即座にテストを失敗させたい場合などに有用です。ただし、**@test** の外側のコードの出力を行うときは、**setup** と **teardown** 関数を **stderr** (**>&2**) にリダイレクトさせる必要があります。そうしないと、出力によって標準出力の TAP ストリームが汚染されて Bats の実行が失敗してしまうおそれがあります。

特殊な変数
------------

Bats のテストを確認するためのグローバル変数が複数存在します:

* **$BATS_TEST_FILENAME** は Bats テストファイルの完全なパスになります。
* **$BATS_TEST_DIRNAME** は Bats テストファイルが配置されたディレクトリになります。
* **$BATS_TEST_NAMES** は各テストケースの関数名の配列になります。
* **$BATS_TEST_NAME** は現在のテストケースが含まれている関数の名前になります。
* **$BATS_TEST_DESCRIPTION** は現在のテストケースの説明文になります。
* **$BATS_TEST_NUMBER** はテストファイルにおける現在のテストケースの (1始まりの) インデックスになります。
* **$BATS_TMPDIR** は一時ファイルを保存するのに使用するディレクトリのパスになります。

関連項目
--------

:doc:`bash.1`,
:doc:`bats.1`
