

# from fastapi import FastAPI, Depends, HTTPException, File, UploadFile
# from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session, relationship
# from pydantic import BaseModel
# import bcrypt
# import os
# from typing import List

# # SQLite 数据库连接
# DATABASE_URL = "sqlite:///./test.db"
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# # 创建用户数据库模型
# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     posts = relationship("Post", back_populates="user")

# # 创建帖子数据库模型
# class Post(Base):
#     __tablename__ = "posts"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     content = Column(String)
#     user_id = Column(Integer, ForeignKey("users.id"))

#     user = relationship("User", back_populates="posts")

# # 创建题目数据库模型
# class Question(Base):
#     __tablename__ = "questions"
#     id = Column(Integer, primary_key=True, index=True)
#     content = Column(String, nullable=False)
#     answer = Column(String, nullable=False)
#     difficulty = Column(Integer, nullable=False)
#     type = Column(String, nullable=False)
#     user_id = Column(Integer, ForeignKey("users.id"))

#     user = relationship("User")

# Base.metadata.create_all(bind=engine)

# # FastAPI 实例
# app = FastAPI()

# # Pydantic 模型
# class UserCreate(BaseModel):
#     username: str
#     password: str

# class UserLogin(BaseModel):
#     username: str
#     password: str

# class UserLogout(BaseModel):
#     username: str

# class PostCreate(BaseModel):
#     title: str
#     content: str
#     user_id: int

# class PostResponse(BaseModel):
#     id: int
#     title: str
#     content: str
#     user_id: int

# class QuestionCreate(BaseModel):
#     content: str
#     answer: str
#     difficulty: int
#     type: str
#     user_id: int

# class QuestionResponse(BaseModel):
#     id: int
#     content: str
#     answer: str
#     difficulty: int
#     type: str
#     user_id: int

#     class Config:
#         orm_mode = True

# # 依赖项：获取数据库会话
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # 注册用户
# @app.post("/register")
# async def register(user: UserCreate, db: Session = Depends(get_db)):
#     existing_user = db.query(User).filter(User.username == user.username).first()
#     if existing_user:
#         raise HTTPException(status_code=400, detail="Username already taken")
    
#     hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
#     new_user = User(username=user.username, hashed_password=hashed_password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return {"message": "User registered successfully"}

# # 用户登录
# @app.post("/login")
# async def login(user: UserLogin, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.username == user.username).first()
#     if not db_user:
#         raise HTTPException(status_code=400, detail="Invalid username or password")

#     if not bcrypt.checkpw(user.password.encode('utf-8'), db_user.hashed_password):
#         raise HTTPException(status_code=400, detail="Invalid username or password")

#     return {"message": "Login successful!", "user_id": db_user.id}

# # 创建帖子
# @app.post("/create_post")
# async def create_post(post: PostCreate, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.id == post.user_id).first()
#     if not db_user:
#         raise HTTPException(status_code=401, detail="User not found or not logged in")

#     new_post = Post(title=post.title, content=post.content, user_id=post.user_id)
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)

#     return {"message": "Post created successfully", "post_id": new_post.id, "user_id": post.user_id}

# # 获取所有帖子
# @app.get("/posts", response_model=List[PostResponse])
# async def get_posts(db: Session = Depends(get_db)):
#     posts = db.query(Post).all()
#     return posts

# # 批量添加题目
# @app.post("/questions/bulk_add")
# async def add_questions_bulk(questions: List[QuestionCreate], db: Session = Depends(get_db)):
#     for question_data in questions:
#         db_user = db.query(User).filter(User.id == question_data.user_id).first()
#         if not db_user:
#             raise HTTPException(status_code=404, detail=f"User ID {question_data.user_id} not found")

#         new_question = Question(
#             content=question_data.content,
#             answer=question_data.answer,
#             difficulty=question_data.difficulty,
#             type=question_data.type,
#             user_id=question_data.user_id
#         )
#         db.add(new_question)
#     db.commit()
#     return {"message": "Questions added successfully"}

# # 获取所有题目
# @app.get("/questions", response_model=List[QuestionResponse])
# async def get_all_questions(db: Session = Depends(get_db)):
#     questions = db.query(Question).all()
#     return questions

# # 用户登出
# @app.post("/logout")
# async def logout(user: UserLogout):
#     return {"message": f"User {user.username} logged out successfully"}

# # FastAPI 删除题目接口
# @app.delete("/questions/{question_id}")
# async def delete_question(question_id: int, db: Session = Depends(get_db)):
#     question = db.query(Question).filter(Question.id == question_id).first()
#     if not question:
#         raise HTTPException(status_code=404, detail="Question not found")
    
#     db.delete(question)
#     db.commit()
#     return {"message": "Question deleted successfully"}

# @app.delete("/posts/{post_id}")
# async def delete_post(post_id: int, db: Session = Depends(get_db)):
#     # 查找帖子
#     post = db.query(Post).filter(Post.id == post_id).first()
#     if not post:
#         raise HTTPException(status_code=404, detail="Post not found")

#     # 删除帖子
#     db.delete(post)
#     db.commit()
#     return {"message": "Post deleted successfully"}

# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session, relationship
# from pydantic import BaseModel
# import bcrypt
# from typing import List

# # SQLite 数据库连接
# DATABASE_URL = "sqlite:///./test.db"
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# # 创建用户数据库模型
# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     posts = relationship("Post", back_populates="user")

# # 创建帖子数据库模型
# class Post(Base):
#     __tablename__ = "posts"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     content = Column(String)
#     subject = Column(String, nullable=False)  # 新增学科标签字段
#     user_id = Column(Integer, ForeignKey("users.id"))

#     user = relationship("User", back_populates="posts")

# # 创建题目数据库模型
# class Question(Base):
#     __tablename__ = "questions"
#     id = Column(Integer, primary_key=True, index=True)
#     content = Column(String, nullable=False)
#     answer = Column(String, nullable=False)
#     difficulty = Column(Integer, nullable=False)
#     type = Column(String, nullable=False)
#     user_id = Column(Integer, ForeignKey("users.id"))

#     user = relationship("User")

# Base.metadata.create_all(bind=engine)

# # FastAPI 实例
# app = FastAPI()

# # Pydantic 模型
# class UserCreate(BaseModel):
#     username: str
#     password: str

# class UserLogin(BaseModel):
#     username: str
#     password: str

# class UserLogout(BaseModel):
#     username: str

# class PostCreate(BaseModel):
#     title: str
#     content: str
#     subject: str  # 新增学科标签字段
#     user_id: int

# class PostResponse(BaseModel):
#     id: int
#     title: str
#     content: str
#     subject: str  # 新增学科标签字段
#     user_id: int

#     class Config:
#         orm_mode = True

# class QuestionCreate(BaseModel):
#     content: str
#     answer: str
#     difficulty: int
#     type: str
#     user_id: int

# class QuestionResponse(BaseModel):
#     id: int
#     content: str
#     answer: str
#     difficulty: int
#     type: str
#     user_id: int

#     class Config:
#         orm_mode = True

# # 依赖项：获取数据库会话
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # 注册用户
# @app.post("/register")
# async def register(user: UserCreate, db: Session = Depends(get_db)):
#     existing_user = db.query(User).filter(User.username == user.username).first()
#     if existing_user:
#         raise HTTPException(status_code=400, detail="Username already taken")
    
#     hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
#     new_user = User(username=user.username, hashed_password=hashed_password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return {"message": "User registered successfully"}

# # 用户登录
# @app.post("/login")
# async def login(user: UserLogin, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.username == user.username).first()
#     if not db_user:
#         raise HTTPException(status_code=400, detail="Invalid username or password")

#     if not bcrypt.checkpw(user.password.encode('utf-8'), db_user.hashed_password):
#         raise HTTPException(status_code=400, detail="Invalid username or password")

#     return {"message": "Login successful!", "user_id": db_user.id}

# # 创建帖子
# @app.post("/create_post", response_model=PostResponse)
# async def create_post(post: PostCreate, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.id == post.user_id).first()
#     if not db_user:
#         raise HTTPException(status_code=401, detail="User not found or not logged in")

#     new_post = Post(
#         title=post.title,
#         content=post.content,
#         subject=post.subject,  # 存储学科标签
#         user_id=post.user_id
#     )
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)

#     return new_post

# # 获取所有帖子
# @app.get("/posts", response_model=List[PostResponse])
# async def get_posts(db: Session = Depends(get_db)):
#     posts = db.query(Post).all()
#     return posts

# # 删除帖子
# @app.delete("/posts/{post_id}")
# async def delete_post(post_id: int, db: Session = Depends(get_db)):
#     post = db.query(Post).filter(Post.id == post_id).first()
#     if not post:
#         raise HTTPException(status_code=404, detail="Post not found")

#     db.delete(post)
#     db.commit()
#     return {"message": "Post deleted successfully"}

# # 批量添加题目
# @app.post("/questions/bulk_add")
# async def add_questions_bulk(questions: List[QuestionCreate], db: Session = Depends(get_db)):
#     for question_data in questions:
#         db_user = db.query(User).filter(User.id == question_data.user_id).first()
#         if not db_user:
#             raise HTTPException(status_code=404, detail=f"User ID {question_data.user_id} not found")

#         new_question = Question(
#             content=question_data.content,
#             answer=question_data.answer,
#             difficulty=question_data.difficulty,
#             type=question_data.type,
#             user_id=question_data.user_id
#         )
#         db.add(new_question)
#     db.commit()
#     return {"message": "Questions added successfully"}

# # 获取所有题目
# @app.get("/questions", response_model=List[QuestionResponse])
# async def get_all_questions(db: Session = Depends(get_db)):
#     questions = db.query(Question).all()
#     return questions

# # 删除题目
# @app.delete("/questions/{question_id}")
# async def delete_question(question_id: int, db: Session = Depends(get_db)):
#     question = db.query(Question).filter(Question.id == question_id).first()
#     if not question:
#         raise HTTPException(status_code=404, detail="Question not found")
    
#     db.delete(question)
#     db.commit()
#     return {"message": "Question deleted successfully"}

# # 用户登出
# @app.post("/logout")
# async def logout(user: UserLogout):
#     return {"message": f"User {user.username} logged out successfully"}













# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session, relationship
# from pydantic import BaseModel
# import bcrypt
# from typing import List

# # SQLite 数据库连接
# DATABASE_URL = "sqlite:///./test.db"
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# # 创建用户数据库模型
# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     posts = relationship("Post", back_populates="user")
#     replies = relationship("Reply", back_populates="user")

# # 创建帖子数据库模型
# class Post(Base):
#     __tablename__ = "posts"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     content = Column(String)
#     subject = Column(String, nullable=False)
#     user_id = Column(Integer, ForeignKey("users.id"))

#     user = relationship("User", back_populates="posts")
#     replies = relationship("Reply", back_populates="post")

# # 创建回复数据库模型
# class Reply(Base):
#     __tablename__ = "replies"
#     id = Column(Integer, primary_key=True, index=True)
#     content = Column(String, nullable=False)
#     post_id = Column(Integer, ForeignKey("posts.id"))
#     user_id = Column(Integer, ForeignKey("users.id"))

#     post = relationship("Post", back_populates="replies")
#     user = relationship("User", back_populates="replies")

# # 创建题目数据库模型
# class Question(Base):
#     __tablename__ = "questions"
#     id = Column(Integer, primary_key=True, index=True)
#     content = Column(String, nullable=False)
#     answer = Column(String, nullable=False)
#     difficulty = Column(Integer, nullable=False)
#     type = Column(String, nullable=False)

#     subject = Column(String, nullable=False)
#     user_id = Column(Integer, ForeignKey("users.id"))

#     user = relationship("User")

# Base.metadata.create_all(bind=engine)

# # FastAPI 实例
# app = FastAPI()

# # Pydantic 模型
# class UserCreate(BaseModel):
#     username: str
#     password: str

# class UserLogin(BaseModel):
#     username: str
#     password: str

# class UserLogout(BaseModel):
#     username: str

# class PostCreate(BaseModel):
#     title: str
#     content: str
#     subject: str
#     user_id: int

# class PostResponse(BaseModel):
#     id: int
#     title: str
#     content: str
#     subject: str
#     user_id: int

#     class Config:
#         orm_mode = True

# class ReplyCreate(BaseModel):
#     content: str
#     post_id: int
#     user_id: int

# class ReplyResponse(BaseModel):
#     id: int
#     content: str
#     post_id: int
#     user_id: int

#     class Config:
#         orm_mode = True

# class QuestionCreate(BaseModel):
#     content: str
#     answer: str
#     difficulty: int
#     type: str
#     subject:str
#     user_id: int

# class QuestionResponse(BaseModel):
#     id: int
#     content: str
#     answer: str
#     difficulty: int
#     type: str
#     subject:str
#     user_id: int

#     class Config:
#         orm_mode = True

# # 依赖项：获取数据库会话
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # 注册用户
# @app.post("/register")
# async def register(user: UserCreate, db: Session = Depends(get_db)):
#     existing_user = db.query(User).filter(User.username == user.username).first()
#     if existing_user:
#         raise HTTPException(status_code=400, detail="Username already taken")
    
#     hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
#     new_user = User(username=user.username, hashed_password=hashed_password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return {"message": "User registered successfully"}

# # 用户登录
# @app.post("/login")
# async def login(user: UserLogin, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.username == user.username).first()
#     if not db_user:
#         raise HTTPException(status_code=400, detail="Invalid username or password")

#     if not bcrypt.checkpw(user.password.encode('utf-8'), db_user.hashed_password):
#         raise HTTPException(status_code=400, detail="Invalid username or password")

#     return {"message": "Login successful!", "user_id": db_user.id}

# # 创建帖子
# @app.post("/create_post", response_model=PostResponse)
# async def create_post(post: PostCreate, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.id == post.user_id).first()
#     if not db_user:
#         raise HTTPException(status_code=401, detail="User not found or not logged in")

#     new_post = Post(
#         title=post.title,
#         content=post.content,
#         subject=post.subject,
#         user_id=post.user_id
#     )
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)

#     return new_post

# # 获取所有帖子
# @app.get("/posts", response_model=List[PostResponse])
# async def get_posts(db: Session = Depends(get_db)):
#     posts = db.query(Post).all()
#     return posts

# # 添加回复
# @app.post("/posts/{post_id}/replies", response_model=ReplyResponse)
# async def add_reply(post_id: int, reply: ReplyCreate, db: Session = Depends(get_db)):
#     db_post = db.query(Post).filter(Post.id == post_id).first()
#     if not db_post:
#         raise HTTPException(status_code=404, detail="Post not found")
    
#     new_reply = Reply(content=reply.content, post_id=post_id, user_id=reply.user_id)
#     db.add(new_reply)
#     db.commit()
#     db.refresh(new_reply)
#     return new_reply

# # 获取指定帖子的所有回复
# @app.get("/posts/{post_id}/replies", response_model=List[ReplyResponse])
# async def get_replies(post_id: int, db: Session = Depends(get_db)):
#     replies = db.query(Reply).filter(Reply.post_id == post_id).all()
#     return replies

# # 删除帖子
# @app.delete("/posts/{post_id}")
# async def delete_post(post_id: int, db: Session = Depends(get_db)):
#     post = db.query(Post).filter(Post.id == post_id).first()
#     if not post:
#         raise HTTPException(status_code=404, detail="Post not found")

#     db.delete(post)
#     db.commit()
#     return {"message": "Post deleted successfully"}

# # 批量添加题目
# @app.post("/questions/bulk_add")
# async def add_questions_bulk(questions: List[QuestionCreate], db: Session = Depends(get_db)):
#     for question_data in questions:
#         db_user = db.query(User).filter(User.id == question_data.user_id).first()
#         if not db_user:
#             raise HTTPException(status_code=404, detail=f"User ID {question_data.user_id} not found")

#         new_question = Question(
#             content=question_data.content,
#             answer=question_data.answer,
#             difficulty=question_data.difficulty,
#             type=question_data.type,
#             subject=question_data.subejct,
#             user_id=question_data.user_id
#         )
#         db.add(new_question)
#     db.commit()
#     return {"message": "Questions added successfully"}

# # 获取所有题目
# @app.get("/questions", response_model=List[QuestionResponse])
# async def get_all_questions(db: Session = Depends(get_db)):
#     questions = db.query(Question).all()
#     return questions

# # 删除题目
# @app.delete("/questions/{question_id}")
# async def delete_question(question_id: int, db: Session = Depends(get_db)):
#     question = db.query(Question).filter(Question.id == question_id).first()
#     if not question:
#         raise HTTPException(status_code=404, detail="Question not found")
    
#     db.delete(question)
#     db.commit()
#     return {"message": "Question deleted successfully"}

# @app.post("/logout")
# async def logout(user: UserLogout):
#      return {"message": f"User {user.username} logged out successfully"}


from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from pydantic import BaseModel
import bcrypt
from typing import List

# SQLite 数据库连接
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 创建用户数据库模型
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    posts = relationship("Post", back_populates="user")
    replies = relationship("Reply", back_populates="user")

# 创建帖子数据库模型
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    subject = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="posts")
    replies = relationship("Reply", back_populates="post")

# 创建回复数据库模型
class Reply(Base):
    __tablename__ = "replies"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    post = relationship("Post", back_populates="replies")
    user = relationship("User", back_populates="replies")

# 创建题目数据库模型
class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    difficulty = Column(Integer, nullable=False)
    type = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User")

Base.metadata.create_all(bind=engine)

# FastAPI 实例
app = FastAPI()

# Pydantic 模型
class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserLogout(BaseModel):
    username: str

class PostCreate(BaseModel):
    title: str
    content: str
    subject: str
    user_id: int

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    subject: str
    user_id: int
    username:str

    class Config:
        orm_mode = True

class ReplyCreate(BaseModel):
    content: str
    post_id: int
    user_id: int

class ReplyResponse(BaseModel):
    id: int
    content: str
    post_id: int
    user_id: int
    username:str

    class Config:
        orm_mode = True

class QuestionCreate(BaseModel):
    content: str
    answer: str
    difficulty: int
    type: str
    subject: str
    user_id: int

class QuestionResponse(BaseModel):
    id: int
    content: str
    answer: str
    difficulty: int
    type: str
    subject: str
    user_id: int

    class Config:
        orm_mode = True

# 依赖项：获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 注册用户
@app.post("/register")
async def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    new_user = User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}

# 用户登录
@app.post("/login")
async def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    if not bcrypt.checkpw(user.password.encode('utf-8'), db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    return {"message": "Login successful!", "user_id": db_user.id}

# 创建帖子
@app.post("/create_post", response_model=PostResponse)
async def create_post(post: PostCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == post.user_id).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="User not found or not logged in")

    new_post = Post(
        title=post.title,
        content=post.content,
        subject=post.subject,
        user_id=post.user_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    # 需要返回包含 username 字段的数据
    return PostResponse(
        id=new_post.id,
        title=new_post.title,
        content=new_post.content,
        subject=new_post.subject,
        user_id=new_post.user_id,
        username=db_user.username  # 加上用户名
    )

# 获取所有帖子
@app.get("/posts", response_model=List[PostResponse])
async def get_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    post_responses = []
    for post in posts:
        post_responses.append(PostResponse(
            id=post.id,
            title=post.title,
            content=post.content,
            subject=post.subject,
            user_id=post.user_id,
            username=post.user.username
        ))
    return post_responses

# 添加回复
@app.post("/posts/{post_id}/replies", response_model=ReplyResponse)
async def add_reply(post_id: int, reply: ReplyCreate, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    new_reply = Reply(content=reply.content, post_id=post_id, user_id=reply.user_id)
    db.add(new_reply)
    db.commit()
    db.refresh(new_reply)
    return ReplyResponse(
        id=new_reply.id,
        content=new_reply.content,
        post_id=new_reply.post_id,
        user_id=new_reply.user_id,
        username=new_reply.user.username
    )

# 获取指定帖子的所有回复
@app.get("/posts/{post_id}/replies", response_model=List[ReplyResponse])
async def get_replies(post_id: int, db: Session = Depends(get_db)):
    replies = db.query(Reply).filter(Reply.post_id == post_id).all()
    return [
        ReplyResponse(
            id=reply.id,
            content=reply.content,
            post_id=reply.post_id,
            user_id=reply.user_id,
            username=reply.user.username
        )
        for reply in replies
    ]

# 删除帖子
@app.delete("/posts/{post_id}")
async def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    db.delete(post)
    db.commit()
    return {"message": "Post deleted successfully"}

# 批量添加题目
@app.post("/questions/bulk_add")
async def add_questions_bulk(questions: List[QuestionCreate], db: Session = Depends(get_db)):
    for question_data in questions:
        db_user = db.query(User).filter(User.id == question_data.user_id).first()
        if not db_user:
            raise HTTPException(status_code=404, detail=f"User ID {question_data.user_id} not found")
    
        new_question = Question(
            content=question_data.content,
            answer=question_data.answer,
            difficulty=question_data.difficulty,
            type=question_data.type,
            subject=question_data.subject,
            user_id=question_data.user_id
        )
        db.add(new_question)
    db.commit()
    return {"message": "Questions added successfully"}

# 获取所有题目
@app.get("/questions", response_model=List[QuestionResponse])
async def get_all_questions(db: Session = Depends(get_db)):
    questions = db.query(Question).all()
    return questions

# 删除题目
@app.delete("/questions/{question_id}")
async def delete_question(question_id: int, db: Session = Depends(get_db)):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    db.delete(question)
    db.commit()
    return {"message": "Question deleted successfully"}

@app.post("/logout")
async def logout(user: UserLogout):
     return {"message": f"User {user.username} logged out successfully"}