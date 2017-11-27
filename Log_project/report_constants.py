#!/usr/bin/python3

fileName = 'log_report_file.txt'

mappingList = [{'path': '/article/media-obsessed-with-bears',
                'title': 'Media obsessed with bears'},
               {'path': '/article/so-many-bears',
                'title': 'There are a lot of bears'},
               {'path': '/article/balloon-goons-doomed',
                'title': 'Balloon goons doomed'},
               {'path': '/article/trouble-for-troubled',
                'title': 'Trouble for troubled troublemakers'},
               {'path': '/article/goats-eat-googles',
                'title': "Goats eat Google''s lawn"},
               {'path': '/article/bad-things-gone',
                'title': 'Bad things gone, say good people'},
               {'path': '/article/bears-love-berries',
                'title': 'Bears love berries, alleges bear'},
               {'path': '/article/candidate-is-jerk',
                'title': 'Candidate is jerk, alleges rival'}, ]

queryAndQuestions = [{'question': '\nWhat are the most popular three articles of all time?\n',
                      'query': '''select * from ( select title, count(*) as views, row_number()over(partition by Null order by count(*) desc) as rank from allNewsDataDN
                                        where title not in ('/')
                                        and status in ('200 OK') 
                                        group by 1) data
                                where rank <=3;
                            ''',
                      'formattedString':'''\t{2}: "{0}" with a total view count of {1}.\n'''},
                     {'question': '\nWho are the most popular authors of all time?\n',
                      'query': '''select name, count(*) as views from allNewsDataDN
                                    where title not in ('/')
                                                and status in ('200 OK') 
                                    group by 1 
                                    order by 2 desc;
                                    ''',
                      'formattedString':'''\t{0} with a total view count of {1}.\n'''},
                     {'question': '\nOn which days did more than 1% of the requests lead to an error?\n',
                      'query': '''select date, sum(case when status not in ('200 OK') then 1 else 0 end)*100.00/count(*) as percentError from allNewsDataDN 
                                    group by 1 
                                    having sum(case when status not in ('200 OK') then 1 else 0 end)*100.00/count(*) >1;
                                ''',
                      'formattedString':'''\t{0} had a error connection rate of {1:0.2f}%.\n'''}]
