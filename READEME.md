项目的根目录应该为`./Scholarship`, 所以请在`./Scholarship`打开pycharm
在`./Scholarship`目录下用powershell运行下面的代码创建虚拟环境并运行代码(操作系统需要是windows)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py runserver
```