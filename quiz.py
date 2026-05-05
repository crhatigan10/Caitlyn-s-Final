from question import Question

if __name__ == '__main__':
    first = Question('what is the largest bird on earth?', ['hawk', 'flamingo', 'penguin'], 'ostrich')
    first.ask()

    second = Question('what is the capital of france', ['london', 'england', 'ireland'], 'france')
    second.ask()

    third = Question('what is the planet known as the red planet', ['Earth', 'Venus', 'Saturn'], 'mars')
    third. ask ()

    fourth = Question('what is the sixth month of the year', ['July', 'March', 'September',], 'june')
    fourth. ask ()