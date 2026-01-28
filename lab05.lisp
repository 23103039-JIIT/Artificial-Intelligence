(defparameter *traffic-density* nil)
(defparameter *accident-status* nil)

(defun traffic-high-p ()
  (eq *traffic-density* 'high))

(defun no-accident-p ()
  (eq *accident-status* 'no))

(defun signal-color ()
  (if (and (traffic-high-p) (no-accident-p))
      'green
      'red))

(defun get-road-conditions ()
  (format t "Enter traffic density (high/low): ")
  (setf *traffic-density* (read))

  (format t "Is there an accident? (yes/no): ")
  (setf *accident-status* (read)))

(defun smart-traffic-system ()
  (get-road-conditions)
  (format t "~%Traffic Signal Decision:~%")
  (format t "→ Signal color is: ~a~%" (signal-color)))

(smart-traffic-system)
