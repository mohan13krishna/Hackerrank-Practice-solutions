
struct document get_document(char* text) {
     struct document doc;

    int pcount = 0;
    for(int i = 0; i < strlen(text) ; i ++) {
        if(text[i] == '\n') pcount ++;
    }
    pcount ++;

    doc.paragraph_count = pcount;
    doc.data = malloc(pcount * sizeof(struct paragraph));

    for(int n = 0, m = 0, l = 0, i = 0; i < pcount; i ++) {
        int scount = 0;
        while(text[n] != '\n' && n < strlen(text)) {
            if(text[n] == '.') scount ++;
            n ++;
        }
        n ++;

        doc.data[i].sentence_count = scount;
        doc.data[i].data = malloc(scount * sizeof(struct sentence));

        for(int j = 0; j < scount; j ++) {
            int wcount = 0;
            while(text[m] != '.' && m < n) {
                if(text[m] == ' ') wcount ++;
                m ++;
            }
            m ++;
            if(text[m] == '\n') m ++;
            wcount ++;

            doc.data[i].data[j].word_count = wcount;
            doc.data[i].data[j].data = malloc(wcount * sizeof(struct word));

            for(int k = 0; k < wcount; k ++) {
                int ccount = 0;
                while(text[l] != ' ' && text[l] != '.' && l < m) {
                    ccount ++;
                    l ++;
                }
                l ++;
                if(text[l] == '\n') l ++;

                ccount ++;
                doc.data[i].data[j].data[k].data = malloc(ccount * sizeof(char));
            }
        }
    }

    int r = 0;
    for(int i = 0; i < doc.paragraph_count; i ++) {
        for(int j = 0; j < doc.data[i].sentence_count; j ++) {
            for(int k = 0; k < doc.data[i].data[j].word_count; k ++) {
                int l = 0;
                while(text[r] != ' ' && text[r] != '.' && text[r] != '\n') {
                    doc.data[i].data[j].data[k].data[l] = text[r];
                    r++;
                    l++;
                }
                doc.data[i].data[j].data[k].data[l] = '\0';
                if(text[r] == '.') {
                    r++;
                    break;
                }
                r ++;
            }
            if(text[r] == '\n') {
                r ++;
                break;
            }
        }
    }

    return doc;
}

struct word kth_word_in_mth_sentence_of_nth_paragraph(struct document Doc, int k, int m, int n) {
    return Doc.data[n - 1].data[m - 1].data[k - 1];
}

struct sentence kth_sentence_in_mth_paragraph(struct document Doc, int k, int m) { 
    return Doc.data[m - 1].data[k - 1];
}

struct paragraph kth_paragraph(struct document Doc, int k) {
    return Doc.data[k - 1];
}




