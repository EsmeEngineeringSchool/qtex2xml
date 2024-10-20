"""
    les différentes entrées qui peuvent être lues dans un fichier tex_
        key        : la clé d'entrée #key
        long       : l'entrée commence par #key et #END key 
        translation : l'entrée est traduite ou pas
        multiple   : si elle peut être répété dans le fichier
"""

entrees={'CAT'                   :{'long':False,'translation':True ,'multiple':False},
         'TYPE'                  :{'long':False,'translation':False,'multiple':False},
         'NAME'                  :{'long':False,'translation':False,'multiple':False},
         'QLONG'                 :{'long':True ,'translation':True ,'multiple':False},
         'Q'                     :{'long':False,'translation':True ,'multiple':False},
         'GFBACK'                :{'long':False,'translation':True ,'multiple':False},
         'CFBACK'                :{'long':False,'translation':True ,'multiple':False},
         'PFBACK'                :{'long':False,'translation':True ,'multiple':False},
         'IFBACK'                :{'long':False,'translation':True ,'multiple':False},
         'ANSW_GRAD'             :{'long':False,'translation':False,'multiple':True},
         'ANSW_TEXT'             :{'long':False,'translation':True ,'multiple':True},
         'ANSW_FBACK'            :{'long':False,'translation':True,'multiple':True},
         'TAGS'                  :{'long':False,'translation':False,'multiple':False},
         'CR_PRELOAD'            :{'long':True ,'translation':False,'multiple':False},
         'CR_ANSWER'             :{'long':True ,'translation':False,'multiple':False},
         'CR_CASE_MARK'          :{'long':False,'translation':False,'multiple':True},
         'CR_CASE_CODE'          :{'long':True ,'translation':False,'multiple':True},
         'CR_CASE_ASEXAMPLE'     :{'long':False,'translation':False,'multiple':True},
         'CR_CASE_EXPECTED'      :{'long':False,'translation':False,'multiple':True},
         'CR_CASE_EXPECTED_LONG' :{'long':True ,'translation':False,'multiple':True}
} 
