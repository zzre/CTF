F = GF(2^32)

v = ' '.join([f"v{i}" for i in range(52, 99)])

for i in range(52, 99):
    exec(f'variables = var("{v}")')

equations = []

v3 = 487 * v82+ 188 * v81+ 145 * v80+ 365 * v79+ 132 * v78+ 635 * v77+ 278 * v76+ 931 * v75+ 871 * v74+ 954 * v73+ 260 * v72+ 246 * v71+ 71 * v70+ 845 * v69+ 357 * v68+ 669 * v67+ 567 * v66+ 659 * v65+ 610 * v62+ 996 * v61+ 411 * v60+ 888 * v59+ 515 * v58+ 826 * v57+ 584 * v56+ 812 * v55+ 426 * v54+ 290 * v53+ 660 * v52+ 139 * v63+ 21 * v64+ 524 * v83;
equations.append( ( 740 * v97+ 338 * v96+ 317 * v95+ 626 * v94+ 680 * v93+ 335 * v92+ 575 * v91+ 448 * v90+ 621 * v89+ 330 * v88+ 151 * v87+ 951 * v86+ 525 * v85+ v3+ 160 * v84+ 813 * v98 == 0x24E6C5 ))
v4 = 506 * v92+ 882 * v91+ 880 * v90+ 877 * v89+ 298 * v88+ 195 * v87+ 984 * v86+ 706 * v85+ 422 * v84+ 125 * v83+ 641 * v82+ 651 * v81+ 859 * v80+ 629 * v79+ 220 * v78+ 925 * v77+ 62 * v76+ 212 * v75+ 323 * v74+ 725 * v73+ 660 * v72+ 853 * v71+ 477 * v70+ 374 * v69+ 899 * v68+ 953 * v67+ 462 * v66+ 195 * v65+ 472 * v64+ 909 * v63+ 162 * v62+ 222 * v61+ 281 * v60+ 799 * v59+ 1018 * v58+ 738 * v57+ 205 * v56+ 444 * v55+ 886 * v54+ 573 * v53+ 9 * v52+ 677 * v93+ 13 * v94;
equations.append( ( 35 * v96 + 267 * v95 + v4 + 917 * v97 + 576 * v98 == 2519130 ))
v5 = 335 * v82+ 54 * v81+ 262 * v80+ 867 * v79+ 51 * v78+ 430 * v77+ 490 * v76+ 69 * v75+ 494 * v74+ 245 * v73+ 103 * v72+ 540 * v71+ 956 * v70+ 475 * v69+ 687 * v68+ 658 * v67+ 521 * v66+ 205 * v65+ 112 * v64+ 808 * v63+ 79 * v62+ 731 * v61+ 713 * v60+ 996 * v59+ 50 * v58+ 523 * v57+ 393 * v56+ 59 * v55+ 988 * v54+ 479 * v53+ 425 * v52+ 315 * v83;
equations.append( ( 891 * v97+ 621 * v96+ 563 * v95+ 811 * v94+ 896 * v93+ 807 * v92+ 631 * v91+ 682 * v90+ 996 * v89+ 861 * v88+ 207 * v87+ 667 * v86+ 392 * v85+ v5+ 576 * v84+ 529 * v98 == 2410525 ))
v6 = 160 * v60 + 790 * v58 + 941 * v57 + 1001 * v56 + 498 * v55 + 786 * v54 + 588 * v53 + (v52 *(1 << 6)) + 429 * v59;
equations.append( ( 148 * v97+ 115 * v96+ 452 * v95+ 816 * v94+ 872 * v93+ 682 * v92+ 498 * v91+ 629 * v90+ 415 * v89+ 744 * v88+ 557 * v87+ 946 * v86+ 987 * v85+ 178 * v84+ 238 * v83+ 333 * v82+ 627 * v81+ 678 * v80+ 1019 * v79+ 916 * v78+ 372 * v77+ 293 * v76+ 899 * v75+ 263 * v74+ 472 * v73+ 832 * v72+ 123 * v71+ 742 * v70+ 4 * v69+ 486 * v68+ 569 * v67+ 505 * v66+ 903 * v65+ 333 * v64+ 848 * v63+ 925 * v62+ v6+ 15 * v61+ 340 * v98 == 2636936 ))
v7 = 5 * v60+ 514 * v58+ 823 * v57+ 67 * v56+ 609 * v55+ 383 * v54+ 874 * v53+ 666 * v52+ 605 * v59+ 21 * v61+ 314 * v62;
equations.append( ( 610 * v97+ 658 * v96+ 936 * v95+ (v94 *(1<< 9))+ 880 * v93+ 378 * v92+ 204 * v91+ 228 * v90+ 91 * v89+ 189 * v88+ 98 * v87+ 313 * v86+ 238 * v85+ 700 * v84+ 559 * v83+ 56 * v82+ 892 * v81+ 342 * v80+ 973 * v79+ 381 * v78+ 138 * v77+ 517 * v76+ 507 * v75+ 324 * v74+ 193 * v73+ 309 * v72+ 547 * v71+ 996 * v70+ 274 * v69+ 230 * v68+ 43 * v67+ 651 * v66+ 296 * v65+ 645 * v64+ v7+ 127 * v63+ 188 * v98 == 2001991 ))
v8 = 111 * v94+ 692 * v93+ 279 * v92+ 456 * v91+ 926 * v90+ 716 * v89+ 535 * v88+ 389 * v87+ 565 * v86+ 331 * v85+ 171 * v84+ 782 * v83+ 764 * v82+ 1001 * v81+ 633 * v80+ 847 * v79+ 861 * v78+ 296 * v77+ 317 * v76+ 901 * v75+ 597 * v74+ 175 * v73+ 335 * v72+ 441 * v71+ 411 * v70+ 741 * v69+ 114 * v68+ 632 * v67+ 273 * v66+ 976 * v65+ 222 * v64+ 982 * v63+ 105 * v62+ 301 * v61+ 142 * v60+ 420 * v59+ 795 * v58+ 978 * v57+ 204 * v56+ 751 * v55+ 645 * v54+ 67 * v53+ 509 * v52;
equations.append( ( 760 * v97 + 457 * v96 + 1020 * v95 + v8 + 985 * v98 == 2616456 ))
v9 = 542 * v90+ 401 * v89+ 811 * v88+ 271 * v87+ 111 * v86+ 208 * v85+ 753 * v84+ 637 * v83+ 151 * v82+ 504 * v81+ 886 * v80+ 707 * v79+ 480 * v78+ 639 * v77+ 183 * v76+ 1011 * v75+ 746 * v74+ 107 * v73+ 45 * v72+ 330 * v71+ 583 * v70+ 541 * v69+ 905 * v68+ 925 * v67+ 596 * v66+ 601 * v65+ 174 * v64+ 153 * v61+ 750 * v60+ 204 * v59+ 738 * v58+ 402 * v57+ 391 * v56+ 153 * v55+ 862 * v54+ 862 * v52+ 5 * v53+ 88 * v62+ 5 * v63+ 873 * v91;
equations.append( ( 176 * v97 + 421 * v96 + 399 * v95 + 83 * v94 + 966 * v93 + v9 + 37 * v92 + 409 * v98 == 2226206 ))
v10 = 942 * v78+ 52 * v77+ 468 * v76+ 298 * v75+ 438 * v74+ 301 * v73+ 549 * v72+ 607 * v71+ 699 * v70+ 313 * v69+ 932 * v68+ 628 * v67+ 209 * v66+ 972 * v65+ 398 * v64+ 506 * v63+ 940 * v62+ 377 * v61+ 450 * v60+ 245 * v59+ 560 * v58+ 880 * v57+ 236 * v56+ 382 * v55+ 59 * v54+ 54 * v53+ 237 * v52+ 606 * v79;
equations.append( ( 647 * v97+ 759 * v96+ 585 * v95+ 904 * v94+ 791 * v93+ 690 * v92+ 438 * v91+ 463 * v90+ 981 * v89+ 577 * v88+ 314 * v87+ 238 * v86+ 796 * v85+ 918 * v84+ 385 * v83+ 743 * v82+ 444 * v81+ v10+ 36 * v80+ 446 * v98 == 2438804 ))
v11 = 295 * v81+ 535 * v80+ 250 * v79+ 152 * v78+ 108 * v77+ 498 * v76+ 430 * v75+ 484 * v74+ 628 * v73+ 961 * v72+ 540 * v71+ 579 * v70+ 61 * v69+ 468 * v68+ 612 * v67+ 124 * v66+ 1004 * v65+ 964 * v64+ 311 * v63+ 34 * v62+ 948 * v61+ 720 * v60+ 616 * v59+ 534 * v58+ 773 * v57+ 376 * v56+ 431 * v55+ 575 * v54+ 503 * v53+ 601 * v52+ 302 * v82;
equations.append( ( 270 * v97+ 459 * v96+ 331 * v95+ 248 * v94+ 177 * v93+ 470 * v92+ 14 * v91+ 110 * v90+ 724 * v89+ (v88 *(1<< 9))+ 402 * v87+ 522 * v86+ 29 * v85+ 524 * v84+ v11+ 37 * v83+ 364 * v98 == 2107275 ))        
v12 = 221 * v94+ 289 * v91+ 14 * v90+ 595 * v89+ 397 * v88+ 374 * v87+ 555 * v86+ 730 * v85+ 723 * v84+ 445 * v81+ 209 * v80+ 957 * v79+ 116 * v78+ 261 * v77+ 786 * v76+ 699 * v75+ 189 * v74+ (v73 *(1 << 6))+ 590 * v72+ 162 * v71+ 191 * v70+ 854 * v69+ 880 * v68+ 329 * v67+ 582 * v66+ 170 * v65+ 745 * v64+ 260 * v63+ 152 * v62+ 628 * v61+ 54 * v60+ 549 * v59+ 683 * v58+ 861 * v57+ 430 * v56+ 948 * v55+ 909 * v54+ 602 * v53+ 144 * v52+ 947 * v82+ 21 * v83+ 975 * v92+ 3 * v93;
equations.append( ( 332 * v97 + v12 + 868 * v95 + 63 * v96 + 123 * v98 == 2187656 ))
v13 = 96 * v52 + 774 * v53;v14 = 748 * v95+ 766 * v94+ 721 * v93+ 345 * v92+ 887 * v91+ 776 * v90+ 493 * v89+ 603 * v88+ 22 * v87+ 463 * v86+ 591 * v85+ 1020 * v84+ 494 * v83+ 834 * v82+ 995 * v81+ 703 * v80+ 739 * v79+ 870 * v78+ 738 * v77+ 863 * v76+ 967 * v75+ 750 * v74+ 927 * v73+ 401 * v72+ 194 * v71+ 798 * v70+ 662 * v69+ 1021 * v68+ 2 * v67+ 224 * v66+ 177 * v65+ 377 * v64+ 677 * v63+ 805 * v62+ 987 * v61+ 903 * v60+ 998 * v59+ (v58 *(1 << 7))+ 969 * v57+ 528 * v56+ 645 * v55+ v13+ 1023 * v54;
equations.append( ( 467 * v97 + 821 * v96 + v14 + 125 * v98 == 3060182 ))
v15 = 117 * v88+ 525 * v87+ 56 * v86+ 432 * v85+ 287 * v82+ 504 * v81+ 239 * v80+ 855 * v79+ 92 * v78+ 698 * v77+ 665 * v76+ 160 * v74+ 179 * v70+ 420 * v69+ 200 * v68+ 471 * v67+ 189 * v66+ 541 * v65+ 83 * v64+ 358 * v63+ 981 * v62+ 359 * v61+ 763 * v60+ 885 * v59+ 462 * v58+ 526 * v57+ 1016 * v56+ 748 * v55+ 319 * v54+ 174 * v53+ 548 * v52+ 654 * v71+ 27 * v72+ 395 * v73+ 31 * v75+ 475 * v83+ 576 * v84+ 244 * v89;
equations.append( ( 134 * v97+ 725 * v96+ 715 * v95+ 274 * v94+ 962 * v93+ 725 * v92+ 559 * v91+ v15+ 513 * v90+ 437 * v98 == 2106171 ))
v16 = 122 * v77+ 357 * v76+ 544 * v75+ 75 * v74+ 738 * v73+ 649 * v70+ 893 * v67+ 714 * v66+ 89 * v65+ 762 * v64+ 228 * v63+ 561 * v62+ 115 * v61+ 14 * v60+ 972 * v59+ 937 * v58+ 315 * v57+ 737 * v54+ 817 * v53+ 82 * v52+ 410 * v55+ 3 * v56+ 580 * v68+ 127 * v69+ 231 * v71+ 73 * v72+ 759 * v78;
equations.append( ( 208 * v97+ 173 * v96+ 209 * v95+ 582 * v94+ 47 * v93+ 798 * v92+ 856 * v91+ 188 * v90+ 543 * v89+ 1015 * v88+ 108 * v87+ 314 * v86+ 848 * v85+ 506 * v84+ 435 * v83+ 259 * v82+ 16 * v81+ 93 * v80+ v16+ 255 * v79+ 691 * v98 == 1969653 ))
v17 = 271 * v84+ 700 * v83+ 508 * v82+ 825 * v81+ 139 * v80+ 385 * v79+ 242 * v78+ 404 * v77+ 812 * v76+ 204 * v75+ 367 * v74+ 50 * v73+ 145 * v72+ 567 * v71+ 846 * v70+ 537 * v69+ 927 * v68+ 667 * v67+ 429 * v66+ 739 * v65+ 518 * v64+ 910 * v63+ 277 * v62+ 864 * v61+ 999 * v58+ 359 * v57+ 182 * v56+ 707 * v55+ 265 * v54+ 766 * v53+ 469 * v52+ 540 * v59+ 18 * v60+ 338 * v85;
equations.append( ( 807 * v97+ 654 * v96+ 528 * v95+ 460 * v94+ 613 * v93+ 449 * v92+ 110 * v91+ 43 * v90+ 305 * v89+ 268 * v88+ 485 * v87+ v17+ 5 * v86+ 339 * v98 == 2176941 ))
v18 = 474 * v94+ 844 * v93+ 516 * v92+ 496 * v91+ 157 * v90+ 629 * v89+ 574 * v88+ 901 * v87+ 726 * v86+ 225 * v85+ 317 * v84+ 171 * v83+ 495 * v82+ 254 * v81+ 772 * v80+ 967 * v79+ 191 * v78+ 276 * v77+ 329 * v76+ 87 * v75+ 877 * v74+ 848 * v73+ 888 * v72+ 411 * v71+ 648 * v70+ 531 * v69+ 1004 * v68+ 903 * v67+ 358 * v66+ 122 * v65+ 619 * v64+ 487 * v63+ 955 * v62+ 816 * v61+ 994 * v60+ 466 * v59+ 636 * v58+ 370 * v57+ 864 * v56+ 338 * v55+ 1013 * v54+ 609 * v53+ 87 * v52;
equations.append( ( 263 * v97 + 907 * v96 + 563 * v95 + v18 + 507 * v98 == 2658391 ))
v19 = 872 * v78+ 829 * v77+ 114 * v76+ 92 * v75+ 771 * v74+ 88 * v73+ 520 * v70+ 88 * v69+ 349 * v68+ 4 * v67+ 960 * v66+ 754 * v65+ 47 * v64+ 180 * v63+ 1011 * v62+ 693 * v61+ 274 * v60+ 996 * v59+ 236 * v58+ 771 * v57+ 501 * v56+ 1000 * v55+ 457 * v54+ 844 * v53+ 278 * v52+ 518 * v71+ 15 * v72+ 56 * v79;
equations.append( ( 610 * v97+ 44 * v96+ 142 * v95+ 70 * v94+ 699 * v93+ 773 * v92+ 606 * v91+ 839 * v90+ 14 * v89+ 312 * v88+ 698 * v87+ 281 * v86+ 482 * v85+ 596 * v84+ 962 * v83+ 664 * v82+ 873 * v81+ v19+ 257 * v80+ 315 * v98 == 2188027 ))
v20 = 832 * v95+ 781 * v94+ 833 * v93+ 983 * v92+ 97 * v91+ 97 * v90+ 197 * v89+ 623 * v88+ 998 * v87+ 326 * v86+ 364 * v85+ 308 * v84+ 983 * v83+ 477 * v82+ 229 * v81+ 659 * v80+ 1013 * v79+ 866 * v78+ 728 * v77+ 675 * v76+ 969 * v75+ 546 * v74+ 911 * v73+ 69 * v72+ 236 * v71+ 184 * v70+ 742 * v69+ 385 * v68+ 407 * v67+ 142 * v66+ 375 * v65+ 798 * v64+ 876 * v63+ 914 * v62+ 898 * v60+ 645 * v59+ 822 * v58+ 279 * v57+ 204 * v56+ 188 * v55+ 173 * v54+ 272 * v53+ 558 * v52;
equations.append( ( 701 * v97 + 724 * v96 + v20 + 385 * v98 == 2510283 ))
v21 = 699 * v94+ 940 * v93+ 226 * v92+ 898 * v91+ 531 * v90+ 169 * v89+ 439 * v88+ 834 * v87+ 173 * v86+ 202 * v83+ 1020 * v82+ 930 * v81+ 716 * v80+ 437 * v79+ 222 * v78+ 803 * v77+ v76+ 352 * v75+ 322 * v74+ 568 * v73+ 623 * v72+ 298 * v71+ 508 * v68+ 490 * v67+ 899 * v66+ 268 * v65+ 233 * v64+ 691 * v63+ 306 * v62+ 122 * v61+ 986 * v60+ 198 * v59+ 552 * v56+ 214 * v55+ 631 * v54+ 618 * v52+ 513 * v53+ 466 * v57+ 288 * v58+ 480 * v69+ 27 * v70+ 379 * v84+ 10 * v85;
equations.append( ( 692 * v95 + v21 + 264 * v96 + 576 * v97 + 301 * v98 == 2220943 ))
v22 = 657 * v75+ 530 * v74+ 304 * v71+ 612 * v70+ 816 * v69+ 242 * v68+ 92 * v67+ 464 * v66+ 505 * v65+ 914 * v64+ 894 * v63+ 814 * v62+ 203 * v61+ 955 * v60+ 182 * v59+ 879 * v58+ 829 * v57+ 865 * v56+ 706 * v55+ 248 * v54+ 530 * v53+ 786 * v52+ 262 * v72+ 127 * v73+ 478 * v76;
equations.append( ( 173 * v97+ 173 * v96+ 458 * v95+ 448 * v94+ 553 * v93+ 251 * v92+ 329 * v91+ 348 * v90+ 314 * v89+ 756 * v88+ 780 * v87+ 837 * v86+ 641 * v85+ 476 * v84+ 780 * v83+ 121 * v82+ 571 * v81+ 367 * v80+ 28 * v79+ 2 * v78+ v22+ 73 * v77+ 421 * v98 == 2322631 ))
v23 = 679 * v77+ 289 * v76+ 838 * v75+ 844 * v74+ 746 * v73+ 670 * v72+ 399 * v71+ 434 * v70+ 720 * v69+ 584 * v68+ 509 * v67+ 619 * v66+ 236 * v65+ 509 * v64+ 321 * v63+ 887 * v62+ 867 * v61+ 706 * v60+ 853 * v59+ 874 * v58+ 810 * v57+ 937 * v56+ 982 * v55+ 1011 * v54+ 772 * v52+ (v53 *(1 << 7))+ 898 * v78;
equations.append( ( 818 * v97+ 261 * v96+ 820 * v95+ 981 * v94+ 920 * v93+ 717 * v92+ 441 * v91+ 863 * v90+ 692 * v89+ 960 * v88+ 809 * v87+ 43 * v86+ 508 * v85+ 797 * v84+ 874 * v83+ 721 * v82+ 269 * v81+ 618 * v80+ v23+ 160 * v79+ 894 * v98 == 3160127 ))
v24 = 313 * v88+ 501 * v87+ 343 * v86+ 372 * v85+ 585 * v82+ 477 * v81+ 418 * v80+ 713 * v79+ 517 * v78+ 730 * v77+ 647 * v76+ 325 * v75+ 174 * v74+ 284 * v73+ 805 * v72+ 974 * v69+ 872 * v68+ 78 * v67+ 186 * v66+ 61 * v63+ 583 * v62+ 617 * v61+ 119 * v60+ 93 * v59+ 587 * v58+ 803 * v57+ 158 * v56+ 523 * v55+ 630 * v54+ 278 * v52+ 8 * v53+ 407 * v64+ 5 * v65+ 1007 * v70+ 63 * v71+ 862 * v83+ 9 * v84+ 577 * v89;
equations.append( ( 323 * v97+ 621 * v96+ 964 * v95+ 356 * v94+ 839 * v93+ 53 * v92+ 852 * v91+ v24+ 31 * v90+ 957 * v98 == 2180863 ))
v25 = 16 * v91+ 581 * v90+ 56 * v89+ 416 * v88+ 855 * v87+ 922 * v86+ 809 * v85+ 239 * v84+ 541 * v83+ 206 * v82+ 234 * v81+ 382 * v80+ 389 * v79+ 483 * v78+ 457 * v77+ 793 * v76+ 879 * v75+ 416 * v74+ 42 * v73+ 985 * v72+ 1018 * v71+ 950 * v70+ 289 * v69+ 1009 * v68+ 57 * v67+ 301 * v66+ 82 * v65+ 444 * v64+ 563 * v63+ 787 * v62+ 776 * v61+ 518 * v60+ 543 * v59+ 870 * v58+ 658 * v57+ 153 * v56+ 224 * v55+ (v54 *(1 << 6))+ 484 * v53+ 266 * v52+ 649 * v92;
equations.append( ( 781 * v97+ 535 * v96+ 937 * v95+ 926 * v94+ v25+ 129 * v93+ 924 * v98 == 2447720 ))
v26 = 679 * v88+ 854 * v87+ 732 * v86+ 724 * v85+ 197 * v84+ 466 * v83+ 411 * v82+ 163 * v79+ 61 * v78+ 950 * v77+ 904 * v76+ 354 * v75+ 735 * v74+ 956 * v73+ 476 * v72+ 261 * v71+ 894 * v70+ 996 * v69+ 994 * v68+ 331 * v67+ 725 * v66+ 211 * v65+ 50 * v64+ 102 * v63+ 123 * v62+ 660 * v61+ 834 * v60+ 745 * v59+ 567 * v58+ 541 * v57+ 743 * v56+ 1011 * v55+ 677 * v54+ 801 * v53+ 778 * v52+ 495 * v80+ 320 * v81+ 811 * v89;
equations.append( ( 299 * v97+ 755 * v96+ 248 * v95+ 914 * v94+ 173 * v93+ 673 * v92+ 964 * v91+ v26+ 41 * v90+ 504 * v98 == 2649697 ))
v27 = 849 * v81+ 448 * v80+ 600 * v79+ 76 * v78+ 147 * v77+ 472 * v76+ 711 * v75+ 361 * v74+ 961 * v73+ 772 * v72+ 882 * v69+ 120 * v68+ 964 * v67+ 161 * v66+ 142 * v65+ 587 * v64+ 899 * v63+ 629 * v62+ 399 * v61+ 100 * v60+ 334 * v59+ 853 * v58+ 760 * v57+ 937 * v56+ 810 * v55+ 464 * v54+ 277 * v53+ 357 * v52+ 244 * v70+ 15 * v71+ 494 * v82;
equations.append( ( 781 * v97+ 189 * v96+ 922 * v95+ 942 * v94+ 813 * v93+ 756 * v92+ 590 * v91+ 211 * v90+ 306 * v89+ 685 * v88+ 630 * v87+ 669 * v86+ 445 * v85+ 962 * v84+ v27+ 25 * v83+ 416 * v98 == 2531775 ))       
v28 = 299 * v92+ 794 * v91+ 649 * v88+ 435 * v85+ 518 * v84+ 423 * v83+ 244 * v82+ 34 * v81+ 459 * v80+ 186 * v77+ 167 * v76+ 159 * v75+ 787 * v74+ 314 * v73+ 426 * v72+ 562 * v71+ 482 * v70+ 778 * v69+ 769 * v68+ 644 * v67+ 723 * v66+ 231 * v65+ 32 * v62+ 718 * v61+ 731 * v60+ 833 * v59+ 701 * v58+ 872 * v55+ 279 * v54+ 54 * v53+ 336 * v52+ 135 * v56+ 40 * v57+ 89 * v63+ 19 * v64+ 363 * v78+ 73 * v79+ 958 * v86+ 24 * v87+ 1000 * v89+ 36 * v90+ 77 * v93+ 80 * v94;
equations.append( ( 148 * v97 + v28 + 956 * v95 + 12 * v96 + 770 * v98 == 1994440 ))
v29 = 366 * v71+ 408 * v70+ 431 * v69+ 541 * v68+ 460 * v67+ 162 * v66+ 862 * v65+ 302 * v64+ 336 * v63+ 349 * v62+ 801 * v61+ 799 * v60+ 802 * v59+ 631 * v58+ 270 * v57+ 119 * v56+ 396 * v55+ 486 * v54+ 120 * v53+ 598 * v52+ 236 * v72;
equations.append( ( 411 * v97+ 838 * v96+ 997 * v95+ 134 * v94+ 131 * v93+ 188 * v92+ 999 * v91+ 397 * v90+ 233 * v89+ 340 * v88+ 196 * v87+ 766 * v86+ 582 * v85+ 202 * v84+ 356 * v83+ 752 * v82+ 395 * v81+ 349 * v80+ 44 * v79+ 1022 * v78+ 641 * v77+ 859 * v76+ 125 * v75+ 876 * v74+ v29+ 96 * v73+ 612 * v98 == 2184786 ))
v30 = 905 * v63+ 931 * v62+ 622 * v61+ 83 * v58+ 972 * v57+ 284 * v52+ 106 * v53+ 19 * v54+ 140 * v55+ 48 * v56+ 989 * v59+ 80 * v60+ 699 * v64;
equations.append( ( 762 * v97+ 774 * v96+ 149 * v95+ 345 * v94+ 698 * v93+ 38 * v92+ 611 * v91+ 169 * v90+ 672 * v89+ 523 * v88+ 824 * v87+ 250 * v86+ 501 * v85+ 620 * v84+ 401 * v83+ 457 * v82+ 887 * v81+ 561 * v80+ 476 * v79+ 919 * v78+ 478 * v77+ 1002 * v76+ 419 * v75+ 389 * v74+ 177 * v73+ 913 * v72+ 249 * v71+ 562 * v70+ 329 * v69+ 899 * v68+ 547 * v67+ 983 * v66+ v30+ 36 * v65+ 570 * v98 == 2380571 ))
v31 = 903 * v87+ 521 * v86+ 278 * v85+ 940 * v84+ 1018 * v83+ 197 * v82+ 109 * v79+ 679 * v78+ 133 * v77+ 848 * v74+ 263 * v73+ 579 * v72+ 44 * v71+ 592 * v68+ 306 * v67+ 682 * v66+ 316 * v65+ 264 * v64+ 803 * v63+ 750 * v62+ 436 * v61+ 482 * v60+ 808 * v59+ 630 * v58+ 508 * v57+ 639 * v56+ 517 * v55+ 828 * v54+ 743 * v53+ 84 * v52+ 325 * v69+ 40 * v70+ 939 * v75+ 37 * v76+ 202 * v80+ 19 * v81+ 570 * v88;
equations.append( ( 526 * v97+ 433 * v96+ 496 * v95+ 82 * v94+ 972 * v93+ 370 * v92+ 539 * v91+ 651 * v90+ v31+ 12 * v89+ 456 * v98 == 2230704 ))
v32 = 485 * v91+ 643 * v90+ 144 * v88+ 36 * v87+ 295 * v85+ 720 * v84+ 439 * v83+ 432 * v82+ 896 * v81+ 710 * v80+ 628 * v79+ 186 * v78+ 890 * v77+ 678 * v76+ 216 * v75+ 457 * v74+ 719 * v73+ (v72 *(1 << 7))+ 282 * v71+ 922 * v70+ 594 * v69+ 236 * v66+ 466 * v65+ 421 * v64+ 157 * v63+ 504 * v62+ 588 * v61+ 929 * v60+ 964 * v59+ 812 * v58+ 598 * v57+ 368 * v56+ 106 * v55+ 301 * v54+ 202 * v53+ 284 * v52+ 111 * v67+ 96 * v68+ 430 * v86+ 25 * v89+ 723 * v92;
equations.append( ( 338 * v97+ 459 * v96+ 772 * v95+ 260 * v94+ v32+ 511 * v93+ 153 * v98 == 2126732 ))
v33 = 916 * v94+ 419 * v93+ 955 * v92+ 107 * v91+ 302 * v90+ 1015 * v89+ 420 * v88+ 959 * v87+ 554 * v86+ 574 * v85+ 252 * v84+ 544 * v83+ 245 * v82+ 421 * v81+ 68 * v80+ 563 * v79+ 103 * v78+ 904 * v77+ 921 * v76+ 275 * v75+ 51 * v74+ 338 * v73+ 188 * v72+ 592 * v71+ 910 * v70+ 918 * v69+ 865 * v68+ 297 * v67+ 541 * v66+ 109 * v65+ 443 * v64+ 775 * v63+ 802 * v62+ 272 * v61+ 326 * v60+ 827 * v59+ 745 * v58+ 696 * v57+ 981 * v56+ 1019 * v55+ 622 * v54+ 692 * v53+ 222 * v52;
equations.append( ( 428 * v97 + 654 * v96 + 314 * v95 + v33 + 303 * v98 == 2538169 ))
v34 = 735 * v90+ 553 * v89+ 532 * v88+ 795 * v87+ 887 * v86+ 898 * v85+ 960 * v84+ 94 * v83+ 332 * v82+ 343 * v81+ 475 * v80+ 1013 * v79+ 165 * v78+ 32 * v77+ 352 * v76+ 70 * v75+ 516 * v74+ 494 * v73+ 112 * v72+ 940 * v71+ 581 * v70+ 943 * v69+ 139 * v68+ 608 * v67+ 508 * v66+ 709 * v65+ 524 * v64+ 684 * v63+ 228 * v60+ 845 * v59+ 895 * v58+ 923 * v57+ 666 * v56+ 39 * v55+ 181 * v54+ 940 * v53+ 385 * v52+ 713 * v61+ 9 * v62+ 526 * v91;
equations.append( ( 240 * v97+ 279 * v96+ 501 * v95+ 671 * v94+ 350 * v93+ v34+ 1023 * v92+ 919 * v98 == 2516019 ))
v35 = 603 * v94+ 698 * v93+ 914 * v92+ 939 * v91+ 914 * v90+ 695 * v89+ 163 * v88+ 238 * v87+ 121 * v86+ 43 * v85+ 309 * v84+ 832 * v83+ 299 * v82+ 989 * v81+ 874 * v80+ 400 * v79+ 318 * v78+ 107 * v77+ 287 * v76+ 825 * v75+ 462 * v74+ 70 * v73+ 146 * v72+ 290 * v71+ 970 * v70+ 239 * v69+ 852 * v68+ 534 * v67+ 637 * v66+ 882 * v65+ 880 * v64+ 607 * v63+ 606 * v62+ 546 * v61+ 730 * v60+ 680 * v59+ 26 * v58+ 917 * v57+ 284 * v56+ 531 * v55+ 993 * v54+ 738 * v53+ 830 * v52;
equations.append( ( 136 * v97 + 298 * v96 + 793 * v95 + v35 + 616 * v98 == 2619695 ))
v36 = 756 * v90+ 935 * v89+ 598 * v88+ 335 * v87+ 59 * v86+ 815 * v85+ 578 * v84+ 383 * v83+ 932 * v82+ 78 * v81+ 795 * v80+ v79+ 815 * v78+ 277 * v77+ 725 * v76+ 957 * v75+ 861 * v74+ 105 * v73+ 543 * v72+ 95 * v71+ 880 * v70+ 493 * v69+ 445 * v68+ 479 * v67+ 741 * v66+ 53 * v65+ 804 * v64+ 83 * v63+ 86 * v60+ 1011 * v59+ 185 * v58+ 179 * v57+ 767 * v56+ 364 * v55+ 534 * v54+ 438 * v53+ 719 * v52+ 295 * v61+ 48 * v62+ 510 * v91;     
equations.append( ( 379 * v97+ 421 * v96+ 131 * v95+ 343 * v94+ 719 * v93+ v36+ 511 * v92+ 695 * v98 == 2297196 ))
v37 = 598 * v85+ 595 * v84+ 988 * v83+ 103 * v82+ 857 * v81+ 952 * v80+ 487 * v79+ 703 * v78+ 1018 * v77+ 345 * v76+ 639 * v75+ 406 * v74+ 111 * v73+ 93 * v72+ 104 * v71+ 869 * v70+ 822 * v69+ 44 * v68+ 847 * v67+ 2 * v66+ 684 * v65+ 823 * v64+ 905 * v63+ 524 * v62+ 493 * v61+ 661 * v58+ 238 * v57+ 635 * v56+ 952 * v55+ 784 * v54+ 983 * v53+ 373 * v52+ 783 * v59+ 3 * v60+ 579 * v86;
equations.append( ( 533 * v97+ 996 * v96+ 977 * v95+ 286 * v94+ 701 * v93+ 972 * v92+ 854 * v91+ 335 * v90+ 162 * v89+ 437 * v88+ v37+ 12 * v87+ 878 * v98 == 2669838 ))
v38 = 411 * v93+ 935 * v92+ 770 * v91+ 518 * v90+ 919 * v89+ 760 * v88+ 681 * v87+ 191 * v86+ 486 * v85+ 623 * v84+ 444 * v83+ 415 * v82+ 498 * v81+ 14 * v80+ 244 * v79+ 779 * v78+ 705 * v75+ 133 * v74+ 245 * v73+ 883 * v72+ 304 * v71+ 514 * v70+ 739 * v69+ 731 * v68+ 542 * v67+ 650 * v66+ 985 * v65+ 1000 * v64+ 414 * v63+ 527 * v62+ 874 * v61+ 739 * v60+ 679 * v59+ 657 * v58+ 893 * v57+ 932 * v56+ (v55 *(1 << 9))+ 114 * v54+ 727 * v53+ 528 * v52+ 440 * v76+ 640 * v77+ 8 * v94;
equations.append( ( 718 * v97+ 355 * v96+ v38+ 21 * v95+ 382 * v98 == 2579438 ))
v39 = 874 * v73+ 264 * v72+ 741 * v71+ 450 * v70+ 756 * v69+ 529 * v68+ 399 * v67+ 328 * v66+ 959 * v61+ 272 * v60+ 989 * v59+ 803 * v58+ 245 * v57+ 383 * v56+ 931 * v55+ 396 * v54+ 60 * v53+ 971 * v52+ 903 * v62+ 160 * v63+ 53 * v64+ 72 * v65+ 404 * v74;
equations.append( ( 135 * v97+ 394 * v96+ 324 * v95+ 586 * v94+ 755 * v93+ 615 * v92+ 499 * v91+ 807 * v90+ 922 * v89+ 216 * v88+ 181 * v86+ 136 * v85+ 660 * v84+ 637 * v83+ 639 * v82+ 94 * v81+ 715 * v80+ 428 * v79+ 339 * v78+ 83 * v77+ 720 * v76+ v39+ 20 * v75+ 462 * v98 == 2285803 ))
v40 = 901 * v94+ 356 * v93+ 286 * v92+ 722 * v91+ 974 * v90+ 389 * v89+ 988 * v88+ 385 * v87+ 658 * v86+ 374 * v85+ 969 * v84+ 876 * v83+ 212 * v82+ 923 * v81+ 702 * v80+ 559 * v79+ 219 * v78+ 236 * v77+ 527 * v76+ 1001 * v75+ 619 * v74+ 225 * v73+ 994 * v72+ 712 * v71+ 70 * v70+ 929 * v69+ 977 * v68+ 212 * v67+ 740 * v66+ 617 * v65+ 706 * v64+ 1017 * v63+ 112 * v62+ 569 * v61+ 516 * v60+ 602 * v59+ 517 * v58+ 196 * v57+ 428 * v56+ 723 * v55+ 552 * v54+ 920 * v53+ 560 * v52;
equations.append( ( 918 * v97+ 787 * v96+ 759 * v95+ v40+ 762 * v98 == 2920377 ))
v41 = 837 * v58+ 1022 * v55+ 949 * v52+ 961 * v53+ 27 * v54+ 556 * v56+ 17 * v57+ 111 * v59;
equations.append( ( 856 * v97+ 771 * v96+ 743 * v95+ 545 * v94+ 376 * v93+ 840 * v92+ 174 * v91+ 426 * v90+ 341 * v89+ 329 * v88+ 57 * v87+ 298 * v86+ 148 * v85+ 266 * v84+ 682 * v83+ 763 * v82+ 615 * v81+ 948 * v80+ 282 * v79+ 122 * v78+ 681 * v77+ 996 * v76+ 463 * v75+ 757 * v74+ 60 * v73+ 565 * v72+ 699 * v71+ 726 * v70+ 673 * v69+ 522 * v68+ 310 * v67+ 271 * v66+ 728 * v65+ 671 * v64+ 767 * v63+ 711 * v62+ 889 * v61+ v41+ 81 * v60+ 143 * v98 == 2471657 ))
v42 = 566 * v94+ 887 * v93+ 662 * v92+ 636 * v91+ 687 * v90+ 843 * v89+ 102 * v88+ 182 * v87+ 305 * v86+ 486 * v85+ 603 * v84+ 194 * v83+ 519 * v82+ 705 * v81+ 540 * v80+ 290 * v79+ 853 * v78+ 948 * v77+ 561 * v76+ 441 * v75+ 118 * v74+ 647 * v73+ 381 * v72+ 1013 * v71+ 147 * v70+ 699 * v69+ 1019 * v68+ 319 * v67+ 133 * v66+ 920 * v65+ 183 * v64+ 930 * v63+ 1007 * v62+ 633 * v61+ 271 * v60+ 186 * v59+ 405 * v58+ 341 * v57+ 297 * v56+ 734 * v55+ 769 * v54+ 400 * v53+ 438 * v52;
equations.append( ( 773 * v95+ v42+ 485 * v96+ 11 * v97+ 311 * v98 == 2512964 ))
v43 = 877 * v91+ 262 * v90+ 326 * v89+ 865 * v88+ 821 * v87+ 721 * v86+ 929 * v85+ 263 * v84+ 67 * v83+ 629 * v82+ 43 * v81+ 714 * v80+ 711 * v79+ 968 * v78+ 877 * v77+ 996 * v76+ 594 * v75+ 125 * v74+ 762 * v73+ 903 * v72+ 377 * v71+ 757 * v70+ 813 * v69+ 323 * v66+ 549 * v65+ 497 * v64+ 89 * v63+ 1023 * v61+ 571 * v59+ 78 * v58+ 85 * v57+ 421 * v56+ 518 * v55+ 688 * v54+ 246 * v53+ 779 * v52+ 281 * v60+ 127 * v62+ 173 * v67+ 81 * v68+ 370 * v92;
equations.append( ( 138 * v97+ 695 * v96+ 969 * v95+ 143 * v94+ v43+ 288 * v93+ 495 * v98 == 2351755 ))
v44 = 68 * v93+ 82 * v92+ 569 * v91+ 67 * v90+ 179 * v89+ 368 * v88+ 729 * v87+ 377 * v86+ 47 * v83+ 724 * v82+ 411 * v81+ 240 * v80+ 718 * v79+ 157 * v78+ 110 * v77+ 212 * v76+ 791 * v75+ 218 * v74+ 594 * v73+ 615 * v72+ 263 * v71+ 518 * v70+ 986 * v69+ 370 * v68+ 62 * v67+ 786 * v66+ 794 * v65+ 746 * v64+ 82 * v63+ 155 * v62+ 153 * v61+ 838 * v60+ 341 * v59+ 875 * v58+ 633 * v57+ 52 * v54+ 483 * v53+ 274 * v52+ 163 * v55+ 33 * v56+ 253 * v84+ 33 * v85+ 808 * v94;
equations.append( ( 29 * v97+ 998 * v96+ v44+ 511 * v95+ 545 * v98 == 1909222 ))
v45 = 431 * v73+ 434 * v70+ 568 * v69+ 874 * v68+ 650 * v67+ 198 * v66+ 789 * v65+ 546 * v64+ 381 * v63+ 947 * v62+ 824 * v61+ 233 * v60+ 920 * v59+ 928 * v58+ 485 * v57+ 824 * v56+ 557 * v55+ 45 * v54+ 140 * v53+ 718 * v52+ 771 * v71+ 384 * v72+ 350 * v74;
equations.append( ( 383 * v97+ 373 * v96+ 712 * v95+ 233 * v94+ 865 * v93+ 228 * v92+ 520 * v91+ 114 * v90+ 1016 * v89+ 845 * v88+ 540 * v87+ 679 * v86+ 345 * v85+ 910 * v84+ 224 * v83+ 506 * v82+ 773 * v81+ 437 * v80+ 29 * v79+ 653 * v78+ (v77 *(1 << 6))+ 915 * v76+ v45+ 9 * v75+ 607 * v98 == 2557994 ))
v46 = 470 * v62+ 458 * v61+ 326 * v60+ 929 * v59+ 295 * v58+ 126 * v57+ 218 * v56+ 775 * v53+ 308 * v52+ 649 * v54+ 320 * v55+ 795 * v63;
equations.append( ( 737 * v97+ 348 * v96+ 407 * v95+ 989 * v94+ 326 * v93+ 641 * v92+ 677 * v91+ 29 * v90+ 957 * v89+ 775 * v88+ 368 * v87+ 953 * v86+ 624 * v85+ 90 * v84+ 143 * v83+ 887 * v82+ 942 * v81+ 903 * v80+ 441 * v79+ 535 * v78+ 369 * v77+ 179 * v76+ 496 * v75+ 742 * v74+ 815 * v73+ 989 * v72+ 1009 * v71+ 929 * v70+ 996 * v69+ 727 * v68+ 218 * v67+ 397 * v66+ 94 * v65+ v46+ 129 * v64+ 199 * v98 == 2584886 ))
v47 = 32 * v61+ 324 * v60+ 247 * v59+ 196 * v58+ 376 * v57+ 178 * v56+ 811 * v55+ 313 * v54+ 911 * v53+ 228 * v52+ 246 * v62;
equations.append( ( 894 * v97+ 198 * v96+ 584 * v95+ 477 * v94+ 215 * v93+ 915 * v92+ 117 * v91+ 502 * v90+ 243 * v89+ 403 * v88+ 960 * v87+ 246 * v86+ 655 * v85+ 577 * v84+ 507 * v83+ 550 * v82+ 950 * v81+ 424 * v80+ 284 * v79+ 623 * v78+ 578 * v77+ 401 * v76+ 732 * v75+ 803 * v74+ 401 * v73+ 236 * v72+ 912 * v71+ 268 * v70+ 389 * v69+ 382 * v68+ 69 * v67+ 949 * v66+ 705 * v65+ 971 * v64+ v47+ 33 * v63+ 114 * v98 == 2134976 ))       
v48 = 280 * v69+ 625 * v68+ 789 * v67+ 152 * v66+ 759 * v65+ 93 * v64+ 429 * v63+ 786 * v62+ 910 * v61+ 427 * v60+ 666 * v59+ (v58 *(1 << 7))+ 604 * v57+ 981 * v56+ 579 * v55+ 572 * v54+ 851 * v53+ 817 * v52+ 863 * v70; 
equations.append( ( 300 * v97+ 102 * v96+ 872 * v95+ 887 * v94+ 964 * v93+ 209 * v92+ 521 * v91+ 989 * v90+ 103 * v89+ 594 * v88+ 381 * v87+ 8 * v86+ 55 * v85+ 899 * v84+ 205 * v83+ 198 * v82+ 594 * v81+ 340 * v80+ 652 * v79+ 865 * v78+ 520 * v77+ 934 * v76+ 172 * v75+ 88 * v74+ 828 * v73+ 296 * v72+ v48+ 129 * v71+ 265 * v98 == 2504301 ))
v49 = 581 * v93+ 579 * v92+ 766 * v91+ 900 * v90+ 400 * v89+ 165 * v88+ 145 * v87+ 983 * v86+ 577 * v85+ 401 * v84+ 530 * v83+ 1006 * v82+ 8 * v80+ 507 * v79+ 346 * v78+ 151 * v77+ 343 * v76+ 943 * v75+ 438 * v74+ 205 * v73+ 546 * v72+ 112 * v71+ 593 * v70+ 130 * v69+ 942 * v68+ 418 * v67+ 536 * v66+ 525 * v65+ 365 * v64+ 69 * v63+ 456 * v62+ 212 * v61+ 718 * v60+ 431 * v59+ 596 * v58+ 811 * v57+ 324 * v56+ 392 * v55+ 402 * v54+ 880 * v53+ 662 * v52+ 1022 * v94;
equations.append( ( 314 * v97+ 230 * v96+ v49+ 11 * v95+ 448 * v98 == 2234809 ))
v50 = 2 * v72 + 14 * v71 + 45 * v70 + 238 * v69 + 186 * v68 + 741 * v67 + 499 * v66 + 1013 * v65 + 294 * v64 + 889 * v63 + 325 * v62 + 110 * v61 + 1022 * v60 + 241 * v59 + 271 * v58 + 922 * v57 + 252 * v56 + 970 * v55 + 375 * v54 + 1021 * v53 + 281 * v52 + 14 * v73;
equations.append( ( 919 * v97+ 895 * v96+ 328 * v95+ 803 * v94+ 821 * v93+ 210 * v92+ 191 * v91+ 224 * v90+ 334 * v89+ 820 * v88+ 713 * v87+ 426 * v86+ 162 * v85+ 564 * v84+ 754 * v83+ 933 * v82+ 865 * v81+ 828 * v80+ 464 * v79+ 577 * v78+ 245 * v77+ 591 * v76+ 883 * v75+ v50+ 33 * v74+ 263 * v98 == 2374375 ))

solution = solve(equations, variables, domain=F)[0]
flag = [chr(x.rhs()) for x in solution]
print(''.join(flag))
