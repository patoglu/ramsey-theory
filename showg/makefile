CXX = gcc
CXXFLAGS =
LDFLAGS = 
LBLIBS =  

SRC = showg.c
OBJ = $(SRC:.cc=.o)
EXEC = showg

all: $(EXEC)

$(EXEC): $(OBJ)
	$(CXX) $(CXXFLAGS) -o $@ $(OBJ) $(LBLIBS)

clean:
	rm showg
