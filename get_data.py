import  argparse
import graphs


def load_data():
    parser = argparse.ArgumentParser(description='Graph skeletons representations')

    parser.add_argument('--data_name', type=str, help='dataset : SBU, NTU_xview_values, NTU_xsub_values ', default='SBU')

    parser.add_argument('--split', type=int, default=1, help='SBU : 1,2,3, 4, 5')


    args = parser.parse_args()



    dataset = graphs.Data()

    if args.data_name == 'SBU':
        dataset = dataset.get_SBU(args)
        N_nodes = dataset[-1].shape[0]
        n_classes = 8

    if args.data_name == 'NTU_xview_values':
        dataset = dataset.get_NTU_xview_values()
        N_nodes = dataset[-1].shape[0]
        n_classes = 60

    if args.data_name == 'NTU_xsub_values':
        dataset = dataset.get_NTU_xview_values(view='xsub')
        N_nodes = dataset[-1].shape[0]
        n_classes = 60


    labels_train, features_train, labels_test, features_test, _ = dataset


if __name__ == '__main__':
    load_data()

