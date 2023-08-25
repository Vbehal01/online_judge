def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    token_payload = decode_token(token)
    email = token_payload["email"]
    role = token_payload["role"]
    if role == "Admin":
        user = crud.get_admin_by_email(db, email)
        if user:
            return user
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    elif role == "Setter":
        user = crud.get_setter_by_email(db, email)
        if user:
            return user
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    elif role == "Solver":
        user = crud.get_solver_by_email(db, email)
        if user:
            return user
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    else:
        raise HTTPException(status_code=400, detail="role must be admin, setter, solver")
