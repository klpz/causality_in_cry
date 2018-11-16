import matplotlib.pyplot as plt

def refactor_series(data, name):
    diff = []
    for index in data.index.tolist():
        if index == 0:
            diff.append(0)
            continue
        diff.append(data[name].loc[index] - data[name].loc[index - 1])
    data['diff'] = diff

    diff = []
    for index in data.index.tolist():
        if index == 0:
            diff.append(0)
            continue
        diff.append(data['diff'].loc[index]*100/data[name].loc[index - 1])
    data['change_percent'] = diff

    return data

def plot2ax(bigdata, first_name, second_name):
    fig = plt.figure()
    ax = fig.add_subplot(111, label="1")
    ax2 = fig.add_subplot(111, label="2", frame_on=False)
    ax.plot(bigdata[[first_name]].values[360:], color="C3")
    ax.set_xlabel('x_'+first_name, color="C3")
    ax.set_ylabel('y_'+first_name, color="C3")
    ax2.plot(bigdata[[second_name]].values[360:], color="C0")
    ax2.xaxis.tick_top()
    ax2.yaxis.tick_right()
    ax2.set_xlabel('x_'+second_name, color="C0")
    ax2.set_ylabel('y_'+second_name, color="C0")
    ax2.xaxis.set_label_position('top')
    ax2.yaxis.set_label_position('right')
    plt.show()
