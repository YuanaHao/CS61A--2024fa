(define (square n) (* n n))

(define (pow base exp) 
  (cond (
    (modulo exp 2) (* (square (pow base (/ exp 2))) base))
    else ((square (pow base (/ exp 2)))))
    (if  
    
    )
)

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let (__n_______________)
        (* y y y))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) 'YOUR-CODE-HERE)

(define (caddr s) 'YOUR-CODE-HERE)
