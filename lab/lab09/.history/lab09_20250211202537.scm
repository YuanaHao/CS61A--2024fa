(define (over-or-under num1 num2)
  (cond 
    ((> num1 num2) 1)
    ((< num1 num2) -1)
    (else 0))
)

(define (make-adder num) 
  (lambda (x) (+ x num))
)

(define (composed f g)
  (lambda (x) (f (g x)))
)

(define (repeat f n)
  (if (= n 0)
      (lambda (x) x)
      (composed f (repeat f (- n 1)))
  )
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
  if (and ((> a b) (not((zero? (modulo a b))))))
    (gcd b (modulo a b))
)
