# Graph skeletons

# SBU skeletons

python get_data.py --data_name SBU --split 1

# NTU skeletons : NTU_xview_values or NTU_xsub_values

First download the skeleton representations from

https://drive.google.com/file/d/1EhpKFlOAw_UqA2YMtETK6B0Eq9UYIQTO/view?usp=sharing

Then put the data in /graph_skeletons/data/ as for SBU

python get_data.py --data_name NTU_xview_values



# Reference

@inproceedings{MLGCN,
  author    = {Ahmed Mazari and Hichem Sahbi},
  title     = {MLGCN: Multi-Laplacian Graph Convolutional Networks for Human Action Recognition},
  booktitle = {30th British Machine Vision Conference 2019, {BMVC} 2019, Cardiff, UK, September 9-12, 2019},
  pages     = {281},
  publisher = {{BMVA} Press},
  year      = {2019},
  url       = {https://bmvc2019.org/wp-content/uploads/papers/1103-paper.pdf}
}


