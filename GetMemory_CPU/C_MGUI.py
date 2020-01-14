import subprocess
import matplotlib.pyplot as plt
import openpyxl
import time
import re

adb = 'adb'
wb = openpyxl.Workbook()
exceltime = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
reslist = [30, ]


def get_cpu():
    try:
        cputext = subprocess.Popen(adb + ' shell dumpsys cpuinfo | grep video.like', shell=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE).stdout.readline().decode().split()[2][:-1]
        # print(cputext)
        if cputext != '0':
            return cputext
    except IndexError:
        pass


def get_memory():
    name1 = ['Native', 'Heap']
    name2 = ['Dalvik', 'Heap']
    name3 = ['TOTAL:']
    name4 = ['Graphics:']

    def cmd(i):
        try:
            melist = list(filter(None, cputext[i].decode().strip().split(' ')))
            return melist
        except IndexError:
            pass
    memlist = []
    cputext = subprocess.Popen(adb + ' shell dumpsys meminfo video.like | grep -e Graphics -e Native -e Dalvik -e TOTAL',
                               shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE).stdout.readlines()

    for i in range(len(cputext)):
        # print(cmd(i))
        try:
            if set(name1) < set(cmd(i)):
                memlist.append(cmd(0)[2])  # Native
            if set(name2) < set(cmd(i)):
                memlist.append(cmd(1)[2])  # Dalvik
            if set(name3) < set(cmd(i)):
                memlist.append(cmd(5)[1])  # Total
            if set(name4) < set(cmd(i)):
                memlist.append(cmd(3)[1])  # Graphics

        except IndexError:
            pass
    print(memlist)
    return memlist


def get_battery():
    batterytext = subprocess.Popen(adb + ' shell dumpsys battery', shell=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE).stdout.readlines()[10].decode()[8:]
    print(batterytext)


def get_fps():
    '''
    纯粹app帧率，录制帧率另算
    :return:

    batterytext = subprocess.Popen(adb + ' shell dumpsys gfxinfo video.like', shell=True, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE).stdout.read().decode('utf-8')
    mat = re.findall(r'visibility=0(.*)View hierarchy', batterytext, re.S|re.M|re.I)
    frame_origin = mat[0].replace('\n', '').split('\t')[5:]
    try:
        frame = list(map(float, frame_origin))
        # print(batterytext)
        print(frame)
        global frame_count
        frame_count = len(frame) / 4
        # print(frame_count)
        global overtime
        overtime = 0
        n = 4
        framelist = [frame[i:i + n] for i in range(0, len(frame), n)]
        for bn in framelist:
            if sum(bn) > 16.67:
                overtime += int(sum(bn) / 16.67) - 1
            else:
                overtime += int(sum(bn) / 16.67)
    except ValueError:
        pass

    try:
        result = int(frame_count * 60 / (frame_count + overtime))
        print(result)
        return result
    except ZeroDivisionError:
        print(0)
        return 0
    '''
    mfocus = subprocess.Popen('adb shell dumpsys SurfaceFlinger | grep video.like',
                              shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE).stdout.readlines()[-1].decode(
        'utf-8')
    text_mfocus = re.findall('video.like/(.*)', mfocus, re.S | re.M | re.I)[0].replace('\n', '')
    print(text_mfocus)
    text = subprocess.Popen('adb shell dumpsys SurfaceFlinger --latency video.like/' + text_mfocus,
                            shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE).stdout.read().decode(
        'utf-8').split()
    # print(text)
    try:
        res = round((126 * 1e9) / (int(text[-2]) - int(text[2])))
        if res != 0:
            print(res)
            reslist.append(res)
            return res
        else:
            return reslist[-1]
    except IndexError:
        pass


def get_network_traffic():
    liutext = subprocess.Popen('adb shell dumpsys package video.like | grep userId',
                               shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    # print(liutext)
    userid = re.findall('userId=(.*)', liutext, re.M|re.I)[0]
    # print(userid)
    rsorigin = subprocess.Popen('adb shell cat /proc/net/xt_qtaguid/stats | grep ' + userid,
                                shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE).stdout.read().decode('utf-8').split('\n')
    rslist = []
    # print(rsorigin)
    for n in rsorigin:
        rslist.append(n.split())
    # # print(rslist)
    rcv = []
    snd = []
    try:
        for i in rslist:
            # print(i)
            # print(i[5])
            rcv.append(i[5])
            snd.append(i[7])
    except IndexError:
        pass
    rcv_result = sum(map(int, rcv))
    snd_result = sum(map(int, snd))
    print(rcv_result)
    print(snd_result)
    return rcv_result, snd_result


sheet1 = wb.active
sheet1['B1'] = 'native'
sheet1['C1'] = 'dalvik'
sheet1['D1'] = 'total'
sheet1['E1'] = 'graphics'


def matplo():
    ax = []
    ax2 = []
    ax3 = []
    ax4 = []
    ay = []
    ay2 = []
    ay3 = []
    ay4 = []
    bx = []
    by = []
    cx = []
    cy = []
    num = 0
    a = 2
    # 交互模式开启
    plt.ion()
    # 调整子图间距
    plt.subplots_adjust(wspace=0.9, hspace=2.0)
    while True:
        plt.clf()
        native = int(get_memory()[0])
        dalvik = int(get_memory()[1])
        total = int(get_memory()[2])
        graphics = int(get_memory()[3])
        ax.append(num)
        ax2.append(num)
        ax3.append(num)
        ax4.append(num)
        ay.append(native)
        ay2.append(dalvik)
        ay3.append(total)
        ay4.append(graphics)
        agraphic = plt.subplot(3, 2, 1)
        agraphic.set_title('native')
        agraphic.set_xlabel('second', fontsize=10)
        agraphic.set_ylabel('memory', fontsize=10)
        plt.plot(ax, ay, 'g-')
        agraphic2 = plt.subplot(3, 2, 2)
        agraphic2.set_title('dalvik')
        agraphic2.set_xlabel('second', fontsize=10)
        agraphic2.set_ylabel('memory', fontsize=10)
        plt.plot(ax2, ay2, 'g-')
        agraphic3 = plt.subplot(3, 2, 3)
        agraphic3.set_title('total')
        agraphic3.set_xlabel('second', fontsize=10)
        agraphic3.set_ylabel('memory', fontsize=10)
        plt.plot(ax3, ay3, 'g-')
        agraphic4 = plt.subplot(3, 2, 4)
        agraphic4.set_title('graphics')
        agraphic4.set_xlabel('second', fontsize=10)
        agraphic4.set_ylabel('memory', fontsize=10)
        plt.plot(ax4, ay4, 'g-')
        g2 = get_cpu()
        bx.append(num)
        by.append(g2)
        bgraphic = plt.subplot(3, 2, 5)
        bgraphic.set_title('cpu')
        bgraphic.set_xlabel('second', fontsize=10)
        bgraphic.set_ylabel('cpu', fontsize=10)
        plt.plot(bx, by, 'y-')
        fps = int(get_fps())
        cx.append(num)
        cy.append(fps)
        cgraphic = plt.subplot(3, 2, 6)
        cgraphic.set_title('fps')
        cgraphic.set_xlabel('second', fontsize=10)
        cgraphic.set_ylabel('fps', fontsize=10)
        plt.plot(cx, cy, 'r-')
        net = get_network_traffic()
        plt.pause(0.5)
        sheet1['B1'] = 'native'
        sheet1['C1'] = 'dalvik'
        sheet1['D1'] = 'total'
        sheet1['E1'] = 'graphics'
        sheet1['F1'] = 'fps'
        sheet1['G1'] = 'rcv'
        sheet1['H1'] = 'snd'
        sheet1['A' + str(a)] = time.ctime()
        sheet1['B' + str(a)] = native
        sheet1['C' + str(a)] = dalvik
        sheet1['D' + str(a)] = total
        sheet1['E' + str(a)] = graphics
        sheet1['F' + str(a)] = fps
        sheet1['G' + str(a)] = net[0]
        sheet1['H' + str(a)] = net[1]
        wb.save('{}.xlsx'.format(exceltime))
        num += 1
        a += 1
    # 预防动态图直接完了
    plt.ioff()
    plt.show()


matplo()