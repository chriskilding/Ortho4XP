#!/usr/bin/env python3
import sys
import os

import src.O4_File_Names as FNAMES
import src.O4_Imagery_Utils as IMG
import src.O4_Vector_Map as VMAP
import src.O4_Mesh_Utils as MESH
import src.O4_Mask_Utils as MASK
import src.O4_Tile_Utils as TILE
import src.O4_GUI_Utils as GUI
import src.O4_Config_Utils as CFG  # CFG imported last because it can modify other modules variables

cmd_line="USAGE: Ortho4XP_v130.py lat lon imagery zl (won't read a tile config)\n   OR:  Ortho4XP_v130.py lat lon (with existing tile config file)"


def main():
    if not os.path.isdir(FNAMES.Utils_dir):
        raise SystemExit("Missing " + FNAMES.Utils_dir + " directory, check your install. Exiting.")
    for directory in (FNAMES.Preview_dir, FNAMES.Provider_dir, FNAMES.Extent_dir, FNAMES.Filter_dir, FNAMES.OSM_dir,
                      FNAMES.Mask_dir,FNAMES.Imagery_dir,FNAMES.Elevation_dir,FNAMES.Geotiff_dir,FNAMES.Patch_dir,
                      FNAMES.Tile_dir,FNAMES.Tmp_dir):
        if not os.path.isdir(directory):
            try:
                os.makedirs(directory)
                print("Creating missing directory",directory)
            except:
                raise SystemExit("Could not create required directory " + directory + ". Exit.")
    IMG.initialize_extents_dict()
    IMG.initialize_color_filters_dict()
    IMG.initialize_providers_dict()
    IMG.initialize_combined_providers_dict()
    if len(sys.argv)==1: # switch to the graphical interface
        Ortho4XP = GUI.Ortho4XP_GUI()

        Ortho4XP.mainloop()
        print("Bon vol!")
    else: # sequel is only concerned with command line
        if len(sys.argv)<3:
            raise SystemExit(cmd_line)
        try:
            lat=int(sys.argv[1])
            lon=int(sys.argv[2])
        except:
            raise SystemExit(cmd_line)
        if len(sys.argv)==3:
            try:
                tile=CFG.Tile(lat,lon,'')
            except Exception as e:
                print(e)
                raise SystemExit("ERROR: could not read tile config file.")
        else:
            try:
                provider_code=sys.argv[3]
                zoomlevel=int(sys.argv[4])
                tile=CFG.Tile(lat,lon,'')
                tile.default_website=provider_code
                tile.default_zl=zoomlevel
            except:
                raise SystemExit(cmd_line)
        try:
            VMAP.build_poly_file(tile)
            MESH.build_mesh(tile)
            MASK.build_masks(tile)
            TILE.build_tile(tile)
            print("Bon vol!")
        except:
            raise SystemExit("Crash!")


if __name__ == '__main__':
    main()
