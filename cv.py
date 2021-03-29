import PyPDF2

keyword = 'PYTHON, C++ , Java.'

class Keyword:
    def txt_filter(self, dt):
        '''
        keyword to lower case
        maketrans for special symbols
        '''
        dt = dt.lower().translate(str.maketrans(',.', '  '))
        dt_list = []
        for i in dt.split():
            dt_list.append(i)
        return dt_list


class File:
    def parse_doc(self, file):
        '''
        parse a .pdf file
        :return: doc text
        '''
        try:
            doc_txt = ''
            # open the file, with read/binary priviledges
            f = open(file, 'rb')
            pdf = PyPDF2.PdfFileReader(f)
            for page in pdf.pages:
                doc_txt += page.extractText()
            f.close()
            doc_txt = Keyword().txt_filter(doc_txt)
            print(doc_txt)
            return doc_txt

        except:
            return None


class Ranker:
    def set_rank(self, keywords, doc_text):
        '''
        count occurance of keyword in text string
        :param keywords: str object of keyword
        :param doc_text: str object of file text
        :return: dict object
        '''
        keyword_count = {}
        for keyword in keywords:
            count = 0
            for text in doc_text:
                if text == keyword:
                    count += 1
            keyword_count.update({keyword: count})
        return keyword_count


keywords = Keyword().txt_filter(keyword)
doc_text = File().parse_doc('RESUME.pdf')

res = Ranker().set_rank(keywords, doc_text)
print(res)
