from jinja2 import Environment, FileSystemLoader

def gen_html(ft, fs, **infos):
    env = Environment(loader=FileSystemLoader('.'), trim_blocks=True)
    template = env.get_template(ft)
    html = template.render(infos)
    f = open(fs, 'w')
    f.write(html)
    f.close()

