# python-datetime-now #
# 2018 07 12 # 2018 06 22
# _datetime_now_.py

import datetime, time

#
def _now_yWw_( dat = None ):
    if dat == None: dat = datetime.datetime.now()
    y = dat.strftime( '%y' )
    W = dat.strftime( '%W' )
    w = dat.strftime( '%w' )
    yWw = ( "%02d%02d%1d" % (int(y), int(W), int(w)) )
    return ( dat, yWw, y, W, w )

#
def _now_yj_( dat = None ):
    if dat == None: dat = datetime.datetime.now()
    y = dat.strftime( '%y' )
    j = dat.strftime( '%j' )
    yj = ( "%02d%3d" % (int(y), int(j) ) )
    return ( dat, yj, y, j )

#
def _now_HMS_( dat = None ):
    if dat == None: dat = datetime.datetime.now()
    H = dat.strftime( '%H' )
    M = dat.strftime( '%M' )
    S = dat.strftime( '%S' )
    HMS = ( "%05d" % (int(H)*60*60+int(M)*60+int(S)) )
    return ( dat, HMS, H, M, S )

#
'''
--- test 1 ---
(datetime.datetime(2018, 7, 12, 11, 57, 34, 629868), '18284', '18', '28', '4')
(datetime.datetime(2018, 7, 12, 11, 57, 34, 634472), '18193', '18', '193')
(datetime.datetime(2018, 7, 12, 11, 57, 34, 638394), '43054', '11', '57', '34')
--- test 2 ---
(datetime.datetime(2018, 7, 12, 11, 57, 34, 647645), '18284', '18', '28', '4')
(datetime.datetime(2018, 7, 12, 11, 57, 34, 647645), '18193', '18', '193')
(datetime.datetime(2018, 7, 12, 11, 57, 34, 647645), '43054', '11', '57', '34')
'''

#
if __name__ == "__main__":
    
    ### test 1 ###
    print( '--- test 1 ---' )
    print( _now_yWw_() )
    print( _now_yj_() )
    print( _now_HMS_() )

    ### test 2 ###
    print( '--- test 2 ---' )
    dat = datetime.datetime.now()
    print( _now_yWw_(dat) )
    print( _now_yj_(dat) )
    print( _now_HMS_(dat) )


#