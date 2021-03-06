# A file which contains all the functions to create an html result file

import variables


def link_maker(url, display):
    """
    :param url: string; a link to follow
    :param display: string; a text to show instead of the url
    :return: string; html tagged link
    """
    return '<a href="' + url + '">' + display + "</a>"


def add_head(doc, title, css_file="None"):
    """
    :param doc: list(); a list to write in
    :param title: string; a text to be written in the head
    :param css_file: string; a file which contains style parameters for a page
    :return: void
        Adds head, title and (optionally) link to css file tags
    """
    doc.append("<head>")
    doc.append("<title>" + title + "</title>")
    if css_file != "None":
        doc.append('<link rel="stylesheet" type="text/css" href="' + css_file + '" />')
    doc.append("</head>")


def insert_row(doc, cnt, content):
    """
    :param doc: list(); a list to write in
    :param cnt: int; number of cells in the raw
    :param content: list(); a list of cells of the current row
    :return: void
        Adds a row to the table from the new line of the list.
    """
    doc.append("<tr>")
    for i in range(cnt):
        doc.append("<td>" + str(content[i]) + "</td>")
    doc.append("</tr>")


def insert_table(doc, rows, cols, titles, content, align="center",
                 border="1", caption=""):
    """
    :param doc: list(); a list to write in
    :param rows: int; number of rows in the table
    :param cols: int; number of columns in the table
    :param titles: list(); a list of titles
    :param content: list(lambda); a list of lambdas, which will fill the table
    :param align: string; (optional) left/right/center; center is a default value
    :param border: string; (optional) number of pixels on the border of the table; '1' is a default value
    :param caption: string; (optional) a title for a table; No title by default
    :return: void
        Adds a table to a doc list from the new line.
    """
    doc.append("<table" + ' align="' + align + '" border="' + border + '" >')  # opening table tag with attributes
    if caption != "":
        doc.append("<caption><h1>" + caption + "</h1></caption>")
    insert_row(doc, cols, [elem for elem in titles])  # inserting titles row
    for i in range(rows):
        insert_row(doc, cols, [elem(i) for elem in content])  # inserting content rows
    doc.append("</table>")


def output(max_length, column_titles, column_content):
    """
    :param max_length: int; a length which can be provided by the lambda's list
    :param column_titles: list(); a list of titles for the table
    :param column_content: list(); a list of lambdas which will fill the table
    :return: void
        Creates an html file which contains a description text and a results table
    """
    file = open("results.html", 'w')

    filecontent = []
    if len(column_titles) != len(column_content):
        print("The numbers of titles and contents are not equal")
        return
    num_of_col = len(column_titles)
    num_of_row = min(max_length, variables.rows_to_show)

    # filling the html file
    filecontent.append("<html>")
    add_head(filecontent, 'Result table', "style.css")
    filecontent.append("<body>")
    filecontent.append('<h4><p align="center" >' + variables.text + "</p></h4>")
    insert_table(filecontent, num_of_row, num_of_col, column_titles, column_content,
                 caption="Result table")
    filecontent.append("<body>")
    filecontent.append("</html>")

    file.writelines([s + '\n' for s in filecontent])
    file.close()
