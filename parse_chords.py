with open('chords.tsv','r') as fi:
    with open('chords.ttl','w') as fo:
        for k,line in enumerate(fi):
            if not (line.startswith('#') or line.startswith('\n')):
                # Parse
                ls = line.strip().split('\t')
                uri  = 'mid-chord:' + '-'.join(ls[0].lower().split())
                lab = ls[0][0].upper() + ls[0][1:] + ' chord'
                qty = ls[1][0].upper() + ls[1][1:]
                npc = len(ls)-1
                itv = ls[2:]
        
                # Print
                fo.write('%s a mid:Chord ;\n' % uri)
                fo.write('\trdfs:label "%s" ;\n' % lab)
                fo.write('\tmid:quality "%s" ;\n' % qty)
                fo.write('\tmid:npc %i ;\n' % npc)
                for i in itv[:-1]:
                    fo.write('\tmid:interval %s ;\n' % i)
                fo.write('\tmid:interval %s .\n' % itv[-1])
                fo.write('\n')