
void sort_by_area(triangle* tr, int n) {
    float *area = malloc(n * sizeof(float));
    for (int i = 0; i < n; i++) {
        float p = (tr[i].a + tr[i].b + tr[i].c) / 2.0;
        area[i] = sqrt(p * (p - tr[i].a) * (p - tr[i].b) * (p - tr[i].c));
    }
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (area[j] > area[j + 1]) {
                float temp = area[j];
                area[j] = area[j + 1];
                area[j + 1] = temp;
                triangle temp_tr = tr[j];
                tr[j] = tr[j + 1];
                tr[j + 1] = temp_tr;
            }
        }
    }
    free(area);
}

