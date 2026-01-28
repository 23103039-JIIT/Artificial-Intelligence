; Fault Diagnosis using Resolution

(defparameter *clauses*
  '(
    (not power machine-fault)
    (power)
    (not machine-fault)   ; negated goal
   ))

(defun empty-clause-p (clause)
  (null clause))

(defun resolve (c1 c2)
  (dolist (lit c1)
    (let ((neg-lit (if (eq (first (list lit)) 'not)
                       (second (list lit))
                       (list 'not lit))))
      (when (member neg-lit c2 :test #'equal)
        (return
         (remove-duplicates
          (append (remove lit c1 :test #'equal)
                  (remove neg-lit c2 :test #'equal))
          :test #'equal))))))

(defun resolution-refutation ()
  (format t "Applying Resolution...~%")
  (let ((new-clauses '()))
    (dolist (c1 *clauses*)
      (dolist (c2 *clauses*)
        (let ((res (resolve c1 c2)))
          (when res
            (format t "Resolved ~a and ~a -> ~a~%" c1 c2 res)
            (when (empty-clause-p res)
              (format t "~%Empty clause found! Machine fault detected.~%")
              (return-from resolution-refutation t))
            (push res new-clauses)))))
    (format t "~%No contradiction found.~%")
    nil))

(resolution-refutation)