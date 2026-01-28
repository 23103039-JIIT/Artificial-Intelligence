(defparameter *facts* '())          ; Working memory
(defparameter *diagnosis* '())      ; Diagnosed diseases

(defparameter *rules*
  '(
    ((fever headache chills) malaria 3)
    ((fever cough) flu 2)
    ((cough sore-throat) cold 1)
   ))

(defun conditions-met-p (conditions facts)
  (every (lambda (c) (member c facts)) conditions))

(defun applicable-rules ()
  (remove-if-not
   (lambda (rule)
     (conditions-met-p (first rule) *facts*))
   *rules*))

(defun select-rule (rules)
  (car (sort rules #'> :key #'third)))

(defun forward-chain ()
  (loop
    (let ((conflicts (applicable-rules)))
      (if (null conflicts)
          (return)
          (let* ((rule (select-rule conflicts))
                 (disease (second rule)))
            (unless (member disease *diagnosis*)
              (format t "Rule fired: IF ~a THEN ~a (Priority ~a)~%"
                      (first rule) disease (third rule))
              (push disease *diagnosis*))
            ;; Remove fired rule to avoid repetition
            (setf *rules* (remove rule *rules*)))))))

(defun get-symptoms ()
  (format t "Enter symptoms one by one (type done to finish):~%")
  (loop
    (let ((symptom (read)))
      (if (eq symptom 'done)
          (return)
          (push symptom *facts*)))))

(defun show-diagnosis ()
  (format t "~%Diagnosis Result:~%")
  (if *diagnosis*
      (dolist (d *diagnosis*)
        (format t "→ Disease detected: ~a~%" d))
      (format t "→ No disease diagnosed.~%")))

(defun medical-expert-system ()
  (setf *facts* '())
  (setf *diagnosis* '())
  (get-symptoms)
  (format t "~%Forward Chaining Inference Started~%~%")
  (forward-chain)
  (show-diagnosis))

(medical-expert-system)