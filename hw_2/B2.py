import random, pylab



L = [[0.25, 0.25], [0.25, 0.75], [0.75, 0.25], [0.75, 0.75]]

N = 4
sigma = 0.1197
histo_data = []



delta = 0.1

n_steps = 2000000




for steps in range(n_steps):
    if steps % 10000 ==0:
        print steps
    a = random.choice(L)
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
    min_dist_sq = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a)
    box_cond_sq = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
    if not (box_cond_sq or min_dist_sq < 4.0 * sigma ** 2):
        a[:] = b
    pos = L
    for k in range(N):
        histo_data.append(pos[k][0])
        
pylab.hist(histo_data, bins=100, normed=True)
pylab.xlabel('x')
pylab.ylabel('frequency')
pylab.title('Markov sampling: x coordinate histogram (density eta=0.18)')
pylab.grid()
pylab.savefig('markov_disks_histo.png')
pylab.show()