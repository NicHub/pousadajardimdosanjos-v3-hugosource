#!/usr/bin/env python
# -*- coding: utf-8 -*-


import glob
import os
import string


def executeSystemCmd( cmd ):
    u"""
    executeSystemCmd
    """

    cmd = " ".join( cmd )

    if os.name in [ 'posix' ]:
        cmd = "TIMEFORMAT='time : %3R s'; time( " + cmd + " )"
    elif os.name in [ 'nt' ]:
        pass

    print "\n%s\n" % cmd
    os.system( cmd )


def main():

    TIFFiles = glob.glob( "./*/*.tif" )
    TIFFiles.extend( glob.glob( "./*/*/*.tif" ) )
    i = 0
    # GMcmd = 'gm convert -quality 50 -resize 50% -level 20%,1,85%'
    GMcmd = 'gm convert -quality 70 -resize 50%'
    basePath = [ '/Users/nico/Sites/pontsdelumiere/2015-12-30_images_jpg/' ]

    for TIFFile in TIFFiles:
        i += 1
        print '%d %s' % ( i, TIFFile )
        JPGFile = './chambres-deluxes-I/chambre-101-s-474.jpg'
        JPGFile = string.split( TIFFile, ".tif" )
        JPGFile = string.split( JPGFile[ 0 ], "/" )
        JPGFile[ -1 ] += ".jpg"
        JPGFile = "/".join( JPGFile )
        print JPGFile

        cmd = [ '%s %s %s' % ( GMcmd, TIFFile, JPGFile ) ]
        executeSystemCmd( cmd )

        # break


def test():

    from pgmagick import Image, FilterTypes
    im = Image( './chambres-deluxes-I/chambre-101-s-474.tif' )
    im.quality( 100 )
    im.filterType( FilterTypes.SincFilter )
    im.scale( '100x100' )
    im.sharpen( 1.0 )
    im.write( 'output.jpg' )


if __name__ == '__main__':

    main()

