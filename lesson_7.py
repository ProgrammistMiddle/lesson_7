'''with open('data.py','w') as f:
    f.writelines(
        'file = {}\n'
        "file['house'] = 'Fasade decor for a private house'\n"
        "file['design_project'] = '30.000 '\n"
        "file['production'] = '638.000 '\n"
        "file['mounting'] = '350.000 '\n"
         )'''


from doc import file
about=list(file.items())

import datetime
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm


def get_context(house,*args):
    return {'view_house': house}


def from_template(dict_file,template, signature):
    template = DocxTemplate(template)
    context = get_context(dict_file)

    img_size = Cm(15)
    photo = InlineImage(template,signature, img_size)
    context['foto'] = photo
    context['cost_design_project'] = about[1][1]
    context['cost_production'] = about[2][1]
    context['cost_mounting'] = about[3][1]
    template.render(context)
    template.save('fasad' + '_' + str(datetime.datetime.now().date()) + 'report.docx')

def generate_report(dict_file):
    template = 'report.docx'
    signature = 'foto.png'
    from_template(dict_file, template, signature)
    return 'Документ составлен'
print(generate_report(about[0][1]))






