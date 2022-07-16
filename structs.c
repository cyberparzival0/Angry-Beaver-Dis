struct Books{
    int   id;
    char  author[50];
    char  title[50];
};

typedef struct Books Book;

struct Library {
	int id;
	char *p;
} __attribute__((packed)) lib;

struct Library2 {
	int id;
	char *p;
} lib2;
