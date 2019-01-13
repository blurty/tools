#!/usr/bin/env python
import xml.etree.ElementTree as ET
import argparse
import os

# Instantiate the parser
parser = argparse.ArgumentParser(description='Optional app description')

def get_output_file(cfg, file):
    '''
    returns the out file corresponding to file
    :param cfg: Config
    :param file: in file with abstract path
    :return: out file with abstract path
    '''
    name = os.path.basename(file)
    return os.path.join(cfg.out_dir, name)


def patch_transfer_file(cfg):
    '''
    :param cfg: Config
    :return: [(in_file,out_file),...]
    '''
    patch_files = []
    if cfg.in_file is not None:
        patch_files.append((cfg.in_file, get_output_file(cfg, cfg.in_file)))
    elif cfg.in_dir is not None:
        files = os.listdir(cfg.in_dir)
        for file in files:
            abspath_file = os.path.abspath(os.path.join(cfg.in_dir, file))
            if not os.path.isfile(abspath_file):
                print("not file")
                continue
            if file.startswith("."):
                print("hide file")
                continue
            patch_files.append((abspath_file, get_output_file(cfg, abspath_file)))
    return patch_files

def convert(in_file, out_file):
    with open(in_file) as in_fp:
        data = in_fp.read()
    # convert
    root = ET.fromstring(data)
    with open(out_file, 'w') as out_fp:
        print("writing to "+out_file+"...")
        for text in root.itertext():
            out_fp.write(text+"\n")
        print("write over")

def start_transfer(cfg):
    # create output directory
    try:
        os.makedirs(cfg.out_dir, mode=0o755)
    except OSError:
        print("directory already exists, the transfer file will overwrite the same existed file")
    patch_files = patch_transfer_file(cfg)
    for in_file, out_file in patch_files:
        convert(in_file, out_file)

class Config(object):
    in_file = None
    out_file = None
    in_dir = None
    out_dir = None
    default_out_dir_suffix = "evernote_export_tmp"
    def parse_args(self, args):
        if args.f is not None:
            self.in_file = args.f
            self.out_dir = os.path.join(os.path.dirname(args.f), self.default_out_dir_suffix)
        elif args.dir is not None:
            self.in_dir = args.dir
            self.out_dir = os.path.join(args.dir, self.default_out_dir_suffix)
        else:
            raise RuntimeError('input file or directory not found')
        if args.output_dir is not None:
            self.out_dir = args.output_dir

if __name__ == "__main__":
    parser.add_argument('-f', type=str,
        help='file to transfer format')
    parser.add_argument('--dir', type=str,
        help='directory to transfer format')
    parser.add_argument('--output-dir', type=str,
        help='output directory name')
    args = parser.parse_args()
    cfg = Config()
    cfg.parse_args(args)
    start_transfer(cfg)