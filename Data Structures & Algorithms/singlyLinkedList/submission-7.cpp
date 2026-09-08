struct ListNode {
    int val;
    ListNode* next;
    ListNode(int val) : val(val), next(nullptr) {}
};

class LinkedList {
    ListNode* head;
    ListNode* tail;
    
public:
    LinkedList() : head(new ListNode(-1)), tail(head) {}

    ~LinkedList() {
        while(head) {
            ListNode* next = head->next;
            delete head;
            head = next;
        }
    }

    int get(int index) {
        ListNode* ptr = head->next;
        for(int i = 0; ptr; ++i, ptr = ptr-> next) {
            if(i == index) {
                return ptr->val;
            }
        }
        return -1;
    }

    void insertHead(int val) {
        ListNode* newNode = new ListNode(val);
        newNode->next = head->next;
        head->next = newNode;
        if(tail == head) {
            tail = newNode;
        }
    }
    
    void insertTail(int val) {
        ListNode* newNode = new ListNode(val);
        tail->next = newNode;
        tail = newNode;
    }

    bool remove(int index) {
        ListNode* prev = head;
        for(int i = 0; i < index && prev->next; ++i) {
            prev = prev->next;
        }

        ListNode* target = prev->next;
        if(!target) {
            return false;
        }
        if(target == tail) {
            tail = prev;
        }

        prev->next = target->next;
        delete target;
        return true;
    }

    vector<int> getValues() {
        vector<int> result;
        for(ListNode* curr = head->next; curr; curr = curr->next) {
            result.push_back(curr->val);
        }
        return result;
    }
};
