import re
def movie_type_check_All(movie_type,medium,resolving_power,title):
    def movie_type_check():
        if movie_type=='Movie':
            return True
        if movie_type == 'Movies WEB-DL' and medium == 'WEB-DL':
            return True
        if medium == 'WEB-DL' and movie_type != 'Movies WEB-DL':
            return False
        if movie_type == 'Movies 1080p' and resolving_power == '2K/1080p':
            return True
        if movie_type == 'Movies 720p' and resolving_power == '720p/i':
            return True
        if movie_type == 'Movies Blu-ray' and medium == 'Blu-ray':
            return True
        if movie_type == 'Movies 1080p REMUX' and medium == 'Remux':
            return True
        if movie_type=='Movies 2160p REMUX' and medium=='Remux' and resolving_power=='4K/2160p':
            return True
        if movie_type == 'Movies UHD-4K' and medium == 'UHD Blu-ray':
            return True
        if movie_type == 'Movies iPad':
            check_move_type = re.search('iPad', title, re.I)
            check_move_type2 = re.search('Pad', title, re.I)
            if medium == 'Encode' and (check_move_type or check_move_type2):
                return True
        if movie_type == 'Movies 2160p' and resolving_power == '4K/2160p':
            return True
        if movie_type=='Movies HDTV' and medium=='HDTV':
            return True
        if movie_type=='Movies 1080p REMUX' and resolving_power=='2K/1080p' and medium=='Remux':
            return True
    def movie_type_answer():
        if movie_type_check() is True:
            return '类型' + movie_type + '正确'
        if movie_type == 'Documentaries(纪录片)':
            return '类型' + movie_type
        if movie_type=='TV Series(电视剧)':
            return '类型' + movie_type
        else:
            return '类型' + movie_type + '错误'

    return movie_type_answer()