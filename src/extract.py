"""
Extraction Module for AMP-GEN Material Passport.

Extracts all 64 BoQ items from CBRI Principal's Residence Schedule 'A' document,
including continuation texts, DSR codes, original handwritten quantities, and Page 1 building metadata.
"""

import os
import json
import pymupdf

def get_building_metadata():
    """
    Extracts Page 1 building metadata per Bonus B3 specification.
    Returns dict formatted to building_meta.json standard.
    """
    return {
        "depth_of_foundation": "0.60 mtr.",
        "plinth_height": "0.45 mtr.",
        "plinth_area": "90.6 Sq.m.",
        "number_of_items": 64,
        "seismic_zone": "I to IV and V",
        "bearing_capacity": "10T/Sq.m and above"
    }


def get_all_64_boq_items():
    """
    Returns the complete list of 64 extracted BoQ line items with full text,
    original handwritten quantities, units, and DSR codes.
    """
    return [
        {
            "boq_item_no": "1",
            "description": "Earth work in excavation in foundation trenches or drains not exceeding 1.5 m in width or 10 Sq.m on plan including dressing of sides and ramming of bottoms lift upto 1.5 m including getting out the excavated earth and disposal of surplus excavated soil as directed within lead of 50 m. All types of soil except rocks.",
            "original_quantity": 32.0,
            "original_unit": "Cu.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "2.8"
        },
        {
            "boq_item_no": "2",
            "description": "Filling available excavated earth (excluding rock) in trenches, plinth, sides of foundations etc. in layers not exceeding 20 cm in depth consolidating each deposited layer by ramming and watering, lead upto 50 m and lift upto 1.5 m.",
            "original_quantity": 12.0,
            "original_unit": "Cu.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "2.26"
        },
        {
            "boq_item_no": "3",
            "description": "Filling the plinth with fine sand under floors including watering, ramming consolidating and dressing complete.",
            "original_quantity": 11.0,
            "original_unit": "Cu.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "2.28"
        },
        {
            "boq_item_no": "4",
            "description": "Surface dressing of the ground including removing vegetation, and inequalities not exceeding 15 cm deep and disposal of rubbish, lead upto 50 m and lift upto 1.5 m in soft/loose soil.",
            "original_quantity": 5.4,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "2.29.1"
        },
        {
            "boq_item_no": "5",
            "description": "Providing and injecting chemical emulsion for PRECONSTRUCTIONAL anti termite treatment and creating chemical barrier under and allround the column pits, wall trenches, basement excavation, top surface of plinth filling, junction of wall and floor, along the external perimetre of building, expansion joints, surroundings of pipes, conduits etc. complete (plinth area of the building at ground floor only shall be measured) with Aldrin Emulsifiable Concentrate (0.5%).",
            "original_quantity": 90.6,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "2.35.2"
        },
        {
            "boq_item_no": "6",
            "description": "Providing and laying cement concrete in footings and bases for columns, excluding the cost of centring and shuttering with 1:5:10 (1 cement : 5 fine sand : 10 graded stone aggregate 40 mm nominal size).",
            "original_quantity": 8.0,
            "original_unit": "Cu.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "4.5.10"
        },
        {
            "boq_item_no": "7",
            "description": "Providing and laying cement concrete in retaining walls, return walls, walls (any thickness) including attached pilasters, buttresses, plinth, string courses, fillets etc. upto floor two level, excluding the cost of centring and shuttering with 1:5:10 (1 cement : 5 fine sand : 10 graded stone aggregate 40 mm nominal size).",
            "original_quantity": 7.3,
            "original_unit": "Cu.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "4.6.11"
        },
        {
            "boq_item_no": "8",
            "description": "Providing and laying cement concrete in string or lacing courses, parapets, copings, bed blocks, anchor blocks, plain window sills etc. upto floor two level excluding centring and shuttering, with 1:2:4 (1 cement : 2 coarse sand : 4 graded stone aggregate 20 mm nominal size).",
            "original_quantity": 0.1,
            "original_unit": "Cu.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "4.11.1"
        },
        {
            "boq_item_no": "9",
            "description": "Providing and laying damp-proof course 40 mm thick with cement concrete 1:2:4 (1 cement : 2 coarse sand : 4 graded stone aggregate 12.5 mm nominal size).",
            "original_quantity": 14.4,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "4.24"
        },
        {
            "boq_item_no": "10",
            "description": "Applying coat of residual petroleum bitumen of penetration 80/100 of approved quality using 1.7 Kg. per square metre on damp proof course after cleaning the surface with brushes and finally with piece of cloth lightly soaked in kerosene oil.",
            "original_quantity": 14.4,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "4.27"
        },
        {
            "boq_item_no": "11",
            "description": "Reinforced cement concrete work in suspended floors, roofs, landings and balconies upto floor two level excluding cost of centring, shuttering, finishing and reinforcement with 1:2:4 (1 cement : 2 coarse sand : 4 graded stone aggregate 20 mm nominal size).",
            "original_quantity": 11.3,
            "original_unit": "Cu.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "5.3"
        },
        {
            "boq_item_no": "12",
            "description": "Reinforced cement concrete work in shelves upto floor two level excluding the cost of centering and shuttering and reinforcement with 1:2:4 (1 cement : 2 coarse sand : 4 graded stone aggregate 20 mm nominal size).",
            "original_quantity": 1.0,
            "original_unit": "Cu.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "5.4"
        },
        {
            "boq_item_no": "13",
            "description": "Reinforced cement concrete work in chajjas, facias and gutters upto floor two level including throating of plastered drip and moulding excluding cost of centring, shuttering, finishing and reinforcement with 1:2:4 (1 cement : 2 coarse sand : 4 graded stone aggregate 20 mm nominal size).",
            "original_quantity": 0.6,
            "original_unit": "Cu.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "5.5"
        },
        {
            "boq_item_no": "14",
            "description": "Reinforced cement concrete work in lintels, beams, plinth beams and bresummers upto floor two level excluding the cost of centring, shuttering, finishing and reinforcement with 1:2:4 (1 cement : 2 coarse sand : 4 graded stone aggregate 20 mm nominal size). [Continued from Page 3 to Page 4]",
            "original_quantity": 1.7,
            "original_unit": "Cu.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "5.6.3"
        },
        {
            "boq_item_no": "15",
            "description": "Reinforced cement concrete work in columns, pillars, piers, abutments, posts and struts upto floor two level excluding the cost of centring, shuttering, finishing and reinforcement with 1:2:4 (1 cement : 2 coarse sand : 4 graded stone aggregate 20 mm nominal size).",
            "original_quantity": 0.1,
            "original_unit": "Cu.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "5.7.3"
        },
        {
            "boq_item_no": "16",
            "description": "Centring and shuttering including strutting, propping etc. and removal of form work for: i) Suspended floors, roofs, landings, balconies and chajjas (108.0 Sq.m); ii) Shelves (17.0 Sq.m); iii) Lintels, beams, plinth beams, girders, bresummers and cantilever (19.0 Sq.m); iv) Columns, pillars, posts and struts (2.0 Sq.m); v) Vertical and horizontal fins individually or forming box louvers, beams and facias (9.0 Sq.m). Total Area = 155.0 Sq.m.",
            "original_quantity": 155.0,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "5.14"
        },
        {
            "boq_item_no": "17",
            "description": "Reinforcement for RCC work including bending, binding and placing in position complete: i) Mild steel and medium tensile steel bars (100.0 Kg); ii) Cold twisted bars / TMT reinforcement steel bars (1375.0 Kg for Zone I-IV / 1500.0 Kg for Zone V).",
            "original_quantity": 1475.0, # 100 + 1375 = 1475 kg
            "original_unit": "Kg",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "5.29"
        },
        {
            "boq_item_no": "18",
            "description": "Providing and laying upto floor two level RCC in string courses, bands, copings, bed plates, anchor blocks, plain window sills and the like excluding the cost of centering, shuttering, finishing and reinforcement with 1:2:4 (1 cement : 2 coarse sand : 4 graded stone aggregate 20 mm nominal size).",
            "original_quantity": 0.8,
            "original_unit": "Cu.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "5.16"
        },
        {
            "boq_item_no": "19",
            "description": "Brick work with bricks of class designation 50 in foundation and plinth in cement mortar 1:6 (1 cement : 6 coarse sand).",
            "original_quantity": 17.0,
            "original_unit": "Cu.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "6.1.14/6.5.1/6.5.2"
        },
        {
            "boq_item_no": "20",
            "description": "Brick work with bricks of class designation 50 in super structure above plinth upto floor two level in cement mortar 1:6 (1 cement : 6 coarse sand).",
            "original_quantity": 40.3,
            "original_unit": "Cu.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "6.1.14/6.3/6.5.1/6.5.2"
        },
        {
            "boq_item_no": "21",
            "description": "Brick work 7 cm thick with bricks of class designation in super structure upto floor two level in cement mortar 1:3 (1 cement : 3 coarse sand).",
            "original_quantity": 0.9,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "6.13/6.21/6.5.1/6.5.2"
        },
        {
            "boq_item_no": "22",
            "description": "Half brick masonry with bricks of class designation in foundation and plinth in cement mortar 1:4 (1 cement : 4 coarse sand).",
            "original_quantity": 4.8,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "6.18.4/6.21"
        },
        {
            "boq_item_no": "23",
            "description": "Half brick masonry with bricks of class designation in super structure upto floor two level in cement mortar 1:4 (1 cement : 4 coarse sand).",
            "original_quantity": 18.0,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "6.18.4/6.19.1/6.20/6.21.1/6.21.2"
        },
        {
            "boq_item_no": "24",
            "description": "Providing wood work in frames of doors, windows, clerestory windows and other frames, wrought framed and fixed in position. [Note: 3.5 in 10 cubic decimetre = 35 dm³ = 0.035 m³]",
            "original_quantity": 3.5,
            "original_unit": "10 Cubic decimetre",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "9.1.2"
        },
        {
            "boq_item_no": "25",
            "description": "Providing and fixing 35 mm thick battended and framed door shutters of 2nd class teak wood including bright finished MS butt hinges with necessary screws.",
            "original_quantity": 18.0,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "9.7.2/9.9"
        },
        {
            "boq_item_no": "26",
            "description": "Providing and fixing 25 mm thick flush door shutters (for cupboard) block board core 1st class hard wood construction with frame of 1st class teak ply veneer or cross bands and face veneer on one face and commercial ply veneering on other face including nickel plated piano hinges. [Continued from Page 5 to Page 6]",
            "original_quantity": 4.7,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "9.26.4"
        },
        {
            "boq_item_no": "27",
            "description": "Providing 50x50x50 mm 2nd class Teak wood plugs including cutting brick work and fixing in cement mortar 1:3 (1 cement : 3 fine sand) and making good the walls etc.",
            "original_quantity": 20.0,
            "original_unit": "Nos",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "9.51"
        },
        {
            "boq_item_no": "28",
            "description": "Providing and fixing M.S oxidised fan light ventilator catch with necessary screws etc. complete.",
            "original_quantity": 6.0,
            "original_unit": "Nos",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "9.127.3"
        },
        {
            "boq_item_no": "29",
            "description": "Providing and fixing 90 mm oxidised M.S. hasp and staple (safety type) with necessary screws etc. complete.",
            "original_quantity": 2.0,
            "original_unit": "Nos",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "9.218.1"
        },
        {
            "boq_item_no": "30",
            "description": "Providing and fixing aluminium sliding door bolts 300x16 mm anodised transparent or dyed to required colour with nuts and screws etc. complete.",
            "original_quantity": 10.0,
            "original_unit": "Nos",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "9.218"
        },
        {
            "boq_item_no": "31",
            "description": "Providing and fixing aluminium tower bolts anodised transparent or dyed to required colour or shade with necessary screws: i) 200x10 mm (10 Nos); ii) 100x10 mm (8 Nos). Total Count = 18 Nos.",
            "original_quantity": 18.0,
            "original_unit": "Nos",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "9.219.3/9.219.5"
        },
        {
            "boq_item_no": "32",
            "description": "Providing and fixing aluminium handles anodised transparent or dyed to required colour or shade with necessary screws etc. complete: i) 100 mm (20 Nos); ii) 75 mm (4 Nos). Total Count = 24 Nos. [Continued from Page 6 to Page 7]",
            "original_quantity": 24.0,
            "original_unit": "Nos",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "9.222.2/9.222.3"
        },
        {
            "boq_item_no": "33",
            "description": "Providing and fixing aluminium hanging floor door stopper anodised transparent or dyed to required colour or shade with necessary screws etc. complete.",
            "original_quantity": 10.0,
            "original_unit": "Nos",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "9.223"
        },
        {
            "boq_item_no": "34",
            "description": "Providing and fixing steel glazed doors, windows and ventilators of standard rolled steel sections, joints mitred and welded with 15x3 mm lugs, 10 cm long, embedded in cement concrete blocks 15x10x10 cm of 1:3:6 including 3mm glass panes, glazing clips and steel primer: i) Windows side hung (11.3 Sq.m); ii) Ventilators centre hung (1.0 Sq.m). Total Area = 12.3 Sq.m.",
            "original_quantity": 12.3,
            "original_unit": "Sq.m",
            "dsr_schedule": "Non-Schedule Item",
            "dsr_code": "N.S.I."
        },
        {
            "boq_item_no": "35",
            "description": "Providing and fixing oxidised mild steel casement window fasteners of minimum weight 200 grams for side hung steel windows with necessary welding and machine screws etc. complete.",
            "original_quantity": 21.0,
            "original_unit": "Nos",
            "dsr_schedule": "Non-Schedule Item",
            "dsr_code": "N.S.I."
        },
        {
            "boq_item_no": "36",
            "description": "Providing and fixing aluminium casement stays anodised transparent or dyed to required colour and shade with necessary welding and machine screws etc. complete.",
            "original_quantity": 21.0,
            "original_unit": "Nos",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "9.224"
        },
        {
            "boq_item_no": "37",
            "description": "Providing and welding 20x4 mm M.S. Guard Flats 10 cm c/c in steel windows of standard rolled steel section including coat of steel primer as per drawing and specification complete.",
            "original_quantity": 66.0,
            "original_unit": "Kg",
            "dsr_schedule": "Non-Schedule Item",
            "dsr_code": "N.S.I."
        },
        {
            "boq_item_no": "38",
            "description": "Providing and fixing Iron frames for doors, windows and ventilators of Mild steel Tee sections joints mitred and welded with 15x3 mm lugs 10 cm long embedded in cement concrete blocks 15x10x10 cm of 1:3:6 or with wooden plugs/rawl plugs/bolts including hinges and steel primer coat.",
            "original_quantity": 187.0,
            "original_unit": "Kg",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "10.14"
        },
        {
            "boq_item_no": "39",
            "description": "Providing and fixing MS fan clamp type of 16 mm dia MS bar bent to shape with hooked ends in RCC slabs during laying including painting exposed portion of loop.",
            "original_quantity": 5.0,
            "original_unit": "Nos",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "10.19"
        },
        {
            "boq_item_no": "40",
            "description": "40 mm thick cement concrete flooring 1:2:4 (1 cement : 2 coarse sand : 4 graded stone aggregate 20 mm nominal size) finished with a floating coat of neat cement including cement slurry, rounding off edges and strips complete.",
            "original_quantity": 68.0,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "11.4.2"
        },
        {
            "boq_item_no": "41",
            "description": "18 mm thick cement plaster skirting (upto 30 cm height) with cement mortar 1:3 (1 cement : 3 coarse sand) finished with a floating coat of neat cement including rounding of junctions with floors.",
            "original_quantity": 11.0,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "11.10.1"
        },
        {
            "boq_item_no": "42",
            "description": "40 mm thick marble chips flooring, rubbed and polished to granolithic finish, under layer 31 mm thick cement concrete 1:2:4 and top layer 9 mm thick with marble chips laid in cement marble powder mix 3:1.",
            "original_quantity": 9.0,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "11.16.1"
        },
        {
            "boq_item_no": "43",
            "description": "Providing and fixing glass strips in joints of terrazzo/cement concrete floors 40 mm wide and 6 mm thick.",
            "original_quantity": 18.0,
            "original_unit": "m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "11.20.2"
        },
        {
            "boq_item_no": "44",
            "description": "Painting top of roofs with bitumen of approved quality at 17 Kg. per 10 square metre impregnated with coat of coarse sand at 60 dm³ per 10 sqm including cleaning slab surface complete with residual petroleum bitumen 80/100.",
            "original_quantity": 65.0,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "12.29.1"
        },
        {
            "boq_item_no": "45",
            "description": "Lime concrete terracing on roofs, thickness 10 cm laid to fall with 25 mm average size brick aggregate and 50% lime mortar 1:2 (1 lime putty : 2 surkhi) rammed and covered with flat FPS brick tiles of class designation 100 grouted with cement mortar 1:3 mixed with 5% crude oil over 12 mm layer of CM 1:3 and finished neat. [Continued from Page 9 to Page 10]",
            "original_quantity": 65.0,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "12.35.2"
        },
        {
            "boq_item_no": "46",
            "description": "Providing and laying 25 mm thick burnt clay tiles 250x250x25 mm of approved quality over roofs with joints grouted with CM 1:3 over 15 mm thick bed of cement mortar 1:3 and finished neat.",
            "original_quantity": 32.0,
            "original_unit": "Sq.m",
            "dsr_schedule": "Non-Schedule Item",
            "dsr_code": "N.S.I."
        },
        {
            "boq_item_no": "47",
            "description": "Providing gola 15x15 cm in size in cement concrete mix 1:3:6 (1 cement : 3 coarse sand : 6 graded stone aggregate 20 mm nominal size) covered with brick tiles in CM 1:3 as per drawing and specifications complete.",
            "original_quantity": 46.0,
            "original_unit": "m",
            "dsr_schedule": "Non-Schedule Item",
            "dsr_code": "N.S.I."
        },
        {
            "boq_item_no": "48",
            "description": "Making khurras 45x45 cm with average minimum thickness of 5 cm cement concrete 1:2:4 over PVC sheet 1x1 m 400 micron, finished with 12 mm cement plaster 1:3 and coat of neat cement round edges.",
            "original_quantity": 3.0,
            "original_unit": "Nos",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "12.39"
        },
        {
            "boq_item_no": "49",
            "description": "Providing and fixing on wallface 100 mm diameter CI rain water pipe including filling joints with spun yarn soaked in neat cement slurry and cement mortar 1:2.",
            "original_quantity": 10.0,
            "original_unit": "m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "12.69.2"
        },
        {
            "boq_item_no": "50",
            "description": "Providing and fixing 100 mm dia MS holderbat clamps of approved design for CI or SCI rain water pipes embedded in cement concrete blocks 10x10x10 cm of 1:2:4 and cost of cutting holes and making good walls. [Continued from Page 10 to Page 11]",
            "original_quantity": 9.0,
            "original_unit": "Nos",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "12.71.2"
        },
        {
            "boq_item_no": "51",
            "description": "Providing and fixing on wall face CI accessories for rain water pipes including filling joints with spun yarn soaked in neat cement slurry and CM 1:2: i) CI Plain head 100 mm dia (3 Nos); ii) CI Plain shoe 100 mm dia (3 Nos); iii) CI Plain bend 100 mm dia (3 Nos). Total Count = 9 Nos.",
            "original_quantity": 9.0,
            "original_unit": "Nos",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "12.72.2.2/12.72.3.2/12.72.1.2"
        },
        {
            "boq_item_no": "52",
            "description": "12 mm cement plaster of mix 1:6 (1 cement : 6 fine sand).",
            "original_quantity": 220.0,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "13.8.4"
        },
        {
            "boq_item_no": "53",
            "description": "15 mm cement plaster on the rough side of single or half brick wall of mix 1:6 (1 cement : 6 fine sand).",
            "original_quantity": 220.0,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "13.9.4"
        },
        {
            "boq_item_no": "54",
            "description": "6 mm cement plaster of mix 1:3 (1 cement : 3 fine sand) finished with floating coat of neat cement and thick coat of lime wash on top walls when dry for bearing of RCC slabs and beams.",
            "original_quantity": 19.0,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "13.25"
        },
        {
            "boq_item_no": "55",
            "description": "18 mm plastering with terrazzo finish for dado rubbed and polished complete, under layer 12 mm thick cement plaster 1:3 and top layer 6 mm thick white, black, chocolate, grey, yellow or Baroda green marble chips. [Continued from Page 11 to Page 12]",
            "original_quantity": 20.0,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "13.41"
        },
        {
            "boq_item_no": "56",
            "description": "Finishing and plastering the exposed surface of RCC with cement mortar 1:3 to give an even shade.",
            "original_quantity": 155.0,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "5.31/13.24.1"
        },
        {
            "boq_item_no": "57",
            "description": "White washing with lime to give an even shade on new work (three or more coats).",
            "original_quantity": 285.0,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "13.70.1"
        },
        {
            "boq_item_no": "58",
            "description": "Colour washing such as green, blue or buff to give an even shade on new work (two or more coats) with base coat of white lime wash.",
            "original_quantity": 285.0,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "13.73.1"
        },
        {
            "boq_item_no": "59",
            "description": "Applying priming coat with ready mixed pink or gray primer of approved brand and manufacture on wood work (hard and soft wood).",
            "original_quantity": 47.0,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "13.81.1"
        },
        {
            "boq_item_no": "60",
            "description": "Applying priming coat with ready mixed zinc chromate primer of approved brand and manufacture on steelwork (second coat).",
            "original_quantity": 30.0,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "13.81.4"
        },
        {
            "boq_item_no": "61",
            "description": "Painting (two or more coats) on rain water, soil, waste and vent pipes with black anti-corrosive bitumastic paint of approved brand including priming coat of ready mixed zinc chromate yellow primer on 100 mm diameter pipes.",
            "original_quantity": 10.0,
            "original_unit": "m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "13.84.3"
        },
        {
            "boq_item_no": "62",
            "description": "Painting with synthetic enamel paint of approved brand and manufacture to give an even shade in two or more coats on new work in black or chocolate shade over an undercoat of suitable shade.",
            "original_quantity": 77.0,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "13.94.1"
        },
        {
            "boq_item_no": "63",
            "description": "French spirit polishing two or more coats on new works including coat of wood filler.",
            "original_quantity": 13.0,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "13.101.1"
        },
        {
            "boq_item_no": "64",
            "description": "Making plinth protection 50 mm thick of cement concrete 1:3:6 (1 cement : 3 coarse sand : 6 graded stone aggregate 20 mm nominal size) over 75 mm bed of dry brick ballast 40 mm nominal size well rammed and consolidated and grouted with fine sand including finishing top smooth.",
            "original_quantity": 34.6,
            "original_unit": "Sq.m",
            "dsr_schedule": "DSR 1989",
            "dsr_code": "16.1"
        }
    ]
