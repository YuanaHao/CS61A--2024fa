(define (square n) (* n n))

(define (pow base exp) 
  (if (modulo exp 2) 
    (* (square (pow base (/ exp 2))) base)
    ((square (pow base (/ exp 2)))))
)

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let (__n_______________)
        (* y y y))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) 'YOUR-CODE-HERE)

(define (caddr s) 'YOUR-CODE-HERE)
