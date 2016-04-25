import variables


def link_maker(url, display):
    return '<a href="' + url + '">' + display + "</a>"


def add_head(doc, title, css_file="None"):
    doc.append("<head>")
    doc.append("<title>" + title + "</title>")
    if css_file != "None":
        doc.append('<link rel="stylesheet" type="text/css" href="' + css_file + '" />')
    doc.append("</head>")


def output(max_length, column_titles, column_content):
    file = open('results.html', 'w')
    filecontent = []
    if len(column_titles) != len(column_content):
        print('There are different counts of titles and contents')
        return
    num_of_col = len(column_titles)
    num_of_row = min(max_length, variables.rows_to_show)

    filecontent.append('<html>')
    add_head(filecontent, 'Result table') #, 'table_style.css')

    filecontent.append('</html>')
    file.writelines(filecontent)