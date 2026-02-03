(defun loanApproval (income creditScore)
  (if 
    (or 
      (if (<= income 30000) (progn (print "Low Income") NIL) T)
      (if (<= creditScore 650) (progn (print "Low credit score") NIL) T) 
      "Loan Rejected" 
      "Loan Approved"
    )
  )
)

(loanApproval 30000 650)
