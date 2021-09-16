import sims4.commands
import sims4.reload as r
import os.path

@sims4.commands.Command('monareload', command_type=sims4.commands.CommandType.Live)
def myfirstscript(module:str, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    try:
        output('リロードしています3')
        openfolder = 'D:/SIMS4MAKEMOD/Script/Decompiler/SimsThings-master/Sims 4 Python Script Workspace/My Script Mods/Example Mod/Scripts'
        output('openfolder設定しました')
        output('ファイルは' + openfolder + module)
        if os.path.exists(openfolder + module == True):
            output('ファイルは見つかりませんでした')
        else:
            output('ファイルを見つけました  ')
        
        r.reload_file(openfolder + "done!")
        output('完了しました！')
    except Exception as e:
        print('エラーが発生しましたpythonでのエラー' + e)
