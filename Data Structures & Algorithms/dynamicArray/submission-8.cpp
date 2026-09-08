class DynamicArray {
    int* arr;
    int size;
    int capacity;

public:

    DynamicArray(int capacity)
        : arr(new int[capacity])
        , size(0)
        , capacity(capacity) {}

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if(size == capacity) {
            resize();
        }
        arr[size++] = n;
    }

    int popback() {
        return arr[--size];
    }

    void resize() {
        capacity *= 2;
        int* newArr = new int[capacity];
        std::copy(arr, arr+size, newArr);
        delete[] arr;
        arr = newArr;
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return capacity;
    }
};
