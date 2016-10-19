import markdown

infile = open('index.md')
outfile = open('index.html', 'w')

md = markdown.Markdown(extensions=['markdown.extensions.toc'])

text = infile.read()
html = md.convert(text)

outfile.write(html)

