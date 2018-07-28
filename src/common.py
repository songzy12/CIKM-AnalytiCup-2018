english_train_path = '../input/cikm_english_train_20180516.txt'
spanish_train_path = '../input/cikm_spanish_train_20180516.txt'
unlabel_spanish_train_path = '../input/cikm_unlabel_spanish_train_20180516.txt'
test_path = '../input/cikm_test_a_20180516.txt'

en_vec_path = '../input/wiki.en.vec'
es_vec_path = '../input/wiki.es.vec'

embed_size = 300
max_features = 5500
max_features = 4300  # this is for only es dataset
maxlen = 54

es_token_list = ['set_ratio', 'sort_ratio', 'set_ratio', 'no', 'sort_ratio', 'ha', 'con', 'el', 'la', 'ti', 'o', 'te', 'para', '?', 'mi', 'lo', 'hay',
                 'como', 'esta', 'una', 'otra', 'es', 'mis', 'los', 'tengo', 'este', 'estoy', 'me', 'eran', 'qué', 'entre', 'cuando', 'en', 'de', '.', 'esto', 'que', '¿']

es_5w1h_list = ['cuándo', 'por qué', 'qué', 'como', 'puedo']
