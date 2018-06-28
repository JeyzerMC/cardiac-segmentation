import dicom, sys
import matplotlib.pyplot as plt

def read_contours(countour_path):
    with open(countour_path) as f:
        content = f.read().splitlines()
    return content

if __name__ == '__main__':
    path = sys.argv[1]
    ds = dicom.read_file(path)
    lines = read_contours(sys.argv[2])
    plt.imshow(ds.pixel_array)

    for line in lines:
        line = str(line).split()
        plt.plot(float(line[0]), float(line[1]), 'go--', markersize=1)

    plt.show()