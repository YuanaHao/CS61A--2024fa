(define (if-program condition if-true if-false)
  (if condition
      if-true
      if-false))

(define (square n) (* n n))

(define (pow-expr base exp)
  (if (= exp 0)
      1
      (if (= exp 1)
          base
          (* base (pow-expr base (- exp 1))))))

(define-macro (repeat n expr)
  `(repeated-call ,n ___))

; Call zero-argument procedure f n times and return the final result.
(define (repeated-call n f)
  (if (= n 1)
      ___
      (begin ___ ___)))
