(define (if-program condition if-true if-false)
  (if condition
      if-true
      if-false))

(define (square n) (* n n))

(define (pow-expr base exp)
  (define (helper exp)
    (cond ((= exp 0) 1)
          ((= exp 1) `(* ,base 1))
          ((even? exp) `(square ,(helper (/ exp 2))))
          (else `(* ,base ,(helper (- exp 1))))))
  (helper exp))

(define-macro (repeat n expr)
  `(repeated-call ,n (lambda () ,expr)))

; Call zero-argument procedure f n times and return the final result.
(define (repeated-call n f)
  (if (= n 1)
      (f)
      (begin (f) (repeated-call (- n 1) f))))
