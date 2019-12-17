import os
import re
import inspect
import importlib
import importlib.util
import types

from lib.tools.public.information import Information

content = """
    <html>
        <head>
            <title>parser.py doc</title>
            <style>
                html,body{
                    margin:0;
                    padding:0;
                    font-family: sans-serif, Arial;
                }
                .container{
                    background-color:lightskyblue;
                    margin-bottom:20px;
                }
                .container>span{
                    background-color:inherit;
                    font:16px arial;
                    color:magenta;
                }
                .container:hover{
                    background-color:deepskyblue;
                }
                span{
                    display:block;
                    margin:0;
                    padding:0;
                }
                span i{
                    padding-left:30px;
                    color:white;
                }
                .cls_signature{
                    padding:10px;
                    cursor:pointer;
                    background-color:#f0f8ff;
                }
                ul{
                    list-style:none;
                    display: none;
                    margin-top:0;
                    margin-left:40px;
                    padding:0;
                }
                li{
                    list-style:none;
                    padding:10px 0;
                    background-color:#ffffe0;
                }
                li:nth-child(2n+1){
                    background-color:khaki;
                }
                li:hover{
                    background-color:yellow;
                }
                .method_signature{
                    cursor:pointer;
                }
                li div{
                    background-color:bisque;
                    margin-left:30px;
                    display: none;
                }
                .desc_header{
                    font:italic bold 14px/20px arial;
                }
                .info{
                    padding-left:40px;
                }
            </style>
            
            <script>
                window.onload = function(){
                    cls = document.getElementsByClassName('cls_signature');
                    methods = document.getElementsByClassName('method_signature');
                    for(var i=0;i<cls.length;i++){
                        cls[i].addEventListener('click', toggle, false);
                    }
                    for(var i=0;i<methods.length;i++){
                        methods[i].addEventListener('click', toggle, false);
                    }
                }
                function toggle(event){
                    var target = event.target;
                    if(target.localName=="span")
                        target = target.nextElementSibling;
                    else
                        target = target.parentElement.nextElementSibling;
                    if (target.style.display=="" || target.style.display=="none")
                        target.style.display="block";
                    else
                        target.style.display="none";
                }
            </script>
        </head>
        <body>
"""

doc_path = Information.get_framework_local_path()+os.sep+'doc'+os.sep


def _parse_func_doc(doc: str):
    txt = '<span class="desc_header">Description:</span>'
    if not doc:
        return txt
    pattn = re.compile(r'([a-zA-Z]+:)(.*)')
    doc = doc.split('\n')
    txt_desc = ''
    for line in doc:
        m = pattn.match(line.strip())
        if not m:
            txt_desc += line.strip() + '<br/>'
        else:
            txt += f"""<span class="info"><code>{txt_desc}</code></span>"""
            txt_desc = ''
            kw = m.groups()
            if isinstance(kw, tuple):
                if kw[0] == 'IsInterface:' and kw[1].strip() == 'False':
                    return None
                txt += f'<span class="desc_header">{kw[0]}</span>'
                if kw[1].strip():
                    txt += f"""<span class="info"><code>{kw[1]}</code></span>"""
            else:
                txt += f'<span class="desc_header">{kw[0]}</span>'
    return txt


def _parse_class_doc(obj):
    name = obj.__name__
    methods = {}
    members = inspect.getmembers(obj)
    for m in members:
        if m[0].startswith('_') or not isinstance(m[1], types.FunctionType):
            continue
        t = str(m[1])
        if re.search(f'{name}', t):
            doc = inspect.getdoc(m[1])
            if not doc:
                continue
            method_doc = _parse_func_doc(doc)
            if not method_doc:
                continue
            signature = inspect.signature(m[1])
            method_def = f'def {m[0]}{signature}:'
            methods.update({method_def: method_doc})

    return methods


def html_doc(module: str):
    """
    call this function to generate api documents
    :param module:
    :return:
    """
    if not os.path.exists(doc_path):
        os.mkdir(doc_path)
    if os.path.isdir(module):
        for root, dirs, files in os.walk(module):
            py_files = filter(lambda f: f.endswith('.py'), files)
            for f in py_files:
                if f.startswith('_'):
                    continue
                file = os.path.abspath(os.path.join(root, f))
                _parser_file(f[:-3], file)

    elif os.path.isfile(module):
        if module.endswith('.py') and not module.startswith('_'):
            _parser_file(module[:-3], module)
    else:
        raise FileExistsError(f'{module} is not a valid file or path.')


def _parser_file(module_name: str, file: str):
    spec = importlib.util.spec_from_file_location(module_name, file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    with open(file, mode='r', encoding='utf-8') as f:
        classes = {}
        functions = {}

        line = f.readline()
        while True:
            if not line:
                break
            m = re.match(r'(class)|(def)', line)
            if m:  # if matched keywords
                name = re.search(r'\w\s+(\w+)', line.strip()).group(1)
                cls_func = getattr(module, name)
                if m.group() == 'class':
                    cls_signature = line.strip()
                    cls_doc = inspect.getdoc(cls_func)
                    methods = _parse_class_doc(cls_func)
                    if methods:
                        classes.update({cls_signature: [cls_doc, methods]})
                else:
                    functions.update({name: cls_func})
            line = f.readline()

        desc = ""
        for cls, info in classes.items():
            desc += f"""<div class="container">
                            <span class="cls_signature"><strong>{cls}</strong><br/><i>{info[0]}</i></span>
                     """
            if info[1]:
                desc += "<ul>"
                for func_def, func_desc in info[1].items():
                    desc += f"""<li>
                                    <span class="method_signature"><strong>{func_def}</strong></span>
                                    <div>{func_desc}
                                    </div></li>"""
                desc += "</ul>"
            desc += "</div>"
        if desc:
            desc = content + desc + """</body></html>"""
            with open(doc_path+module_name+'.html', 'w') as f:
                f.write(desc)


if __name__ == '__main__':
    html_doc('../')
