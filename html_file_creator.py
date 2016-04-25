import variables


def link_maker(url, display):
    return '<a href="' + url + '">' + display + "</a>"


def add_head(doc, title, css_file="None"):
    doc.append("<head>")
    doc.append("<title>" + title + "</title>")
    if css_file != "None":
        doc.append('<link rel="stylesheet" type="text/css" href="' + css_file + '" />')
    doc.append("</head>")


def insert_row(doc, cnt, content):
    doc.append("<tr>")
    for i in range(cnt):
        doc.append("<td>" + str(content[i]) + "</td>")
    doc.append("</tr>")


def insert_table(doc, rows, cols, titles, content, align = "center",
                 border = "1", caption=""):
    doc.append("<table" + ' align="' + align + '" border="' + border + '" >')
    if caption != "":
        doc.append("<caption><h2>" + caption + "</h2></caption>")
    insert_row(doc, cols, [elem for elem in titles])
    for i in range(rows):
        insert_row(doc, cols, [elem(i) for elem in content])
    doc.append("</table>")


def output(max_length, column_titles, column_content):
    file = open("results.html", 'w')
    filecontent = []
    if len(column_titles) != len(column_content):
        print("There are different counts of titles and contents")
        return
    num_of_col = len(column_titles)
    num_of_row = min(max_length, variables.rows_to_show)

    filecontent.append("<html>")
    add_head(filecontent, 'Result table')  # , 'table_style.css')
    filecontent.append("<body>")

    filecontent.append("<p>" + variables.text + "</p>")
    insert_table(filecontent, num_of_row, num_of_col, column_titles, column_content,
                 caption="Result table")
    filecontent.append("<body>")
    filecontent.append("</html>")
    file.writelines([s + '\n' for s in filecontent])
