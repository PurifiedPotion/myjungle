#include "rbtree.h"

#include <stdlib.h>

rbtree *new_rbtree(void) {
  rbtree *p = (rbtree *)calloc(1, sizeof(rbtree));
  // TODO: initialize struct if needed
  node_t *first_nil = calloc(1, sizeof(node_t));
  p->nil = first_nil;
  p->root = first_nil;
  p->nil->color = RBTREE_BLACK;  // sentinel node is always blackW
  p->nil->parent = p->nil;
  return p;
}

void delete_rbtree(rbtree *t) {
  // TODO: reclaim the tree nodes's memory
  delete_node(t, t->root);
  free(t->nil); // free the sentinel node
  free(t);
}

void delete_node(rbtree *t, node_t *node)
{
  if (node == t->nil) return;
  delete_node(t, node->left);
  delete_node(t, node->right);
  free(node);
}

node_t *rbtree_insert(rbtree *t, const key_t key) 
{
  // TODO: implement insert
  node_t *new_node = (node_t *)calloc(1, sizeof(node_t));
  new_node->key = key;

  node_t *x = t->root;
  node_t *y = t->nil;

  while (x != t->nil) 
  {
    y = x;
    if (key < x->key) 
    {
      x = x->left;
    } 
    else 
    {
      x = x->right;
    }
  }
  new_node->parent = y;

  if (y == t->nil)
    t->root = new_node;  // Tree was empty
  else if (key < y->key)
    y->left = new_node;
  else
    y->right = new_node;

  new_node->left = t->nil;
  new_node->right = t->nil;
  new_node->color = RBTREE_RED;

  rb_insert_fixup(t, new_node);

  return new_node; // Return the newly inserted node
}

node_t *rbtree_find(const rbtree *t, const key_t key) {
  // TODO: implement find
  node_t *current = t->root;

  while (current != t->nil)
  {
    if (key == current->key)
      return current;
    else if (key < current->key)
      current = current->left;
    else
      current = current->right;
  }

  return NULL; // Not found
}

node_t *rbtree_min(const rbtree *t) {
  // TODO: implement find
  node_t *current = t->root;
  while (current->left != t->nil)
  {
    current = current->left;
  }
  return current;
}

node_t *rbtree_min_node(const rbtree *t, node_t *subroot) 
{
  node_t *current = subroot;
  while (current->left != t->nil)
  {
    current = current->left;
  }
  return current;
}

node_t *rbtree_max(const rbtree *t) {
  // TODO: implement find
  node_t *current = t->root;
  while (current->right != t->nil)
  {
    current = current->right;
  }
  return current;
}

int rbtree_erase(rbtree *t, node_t *p) {
  // TODO: implement erase
  node_t *y = p;
  node_t *x;
  color_t y_original_color = y->color;
  if (p->left == t->nil)
  {
    x = p->right;
    rb_transplant(t, p, p->right);
  }
  else if (p->right == t->nil)
  {
    x = p->left;
    rb_transplant(t, p, p->left);
  }
  else
  {
    y = rbtree_min_node(t, p->right);
    y_original_color = y->color;
    x = y->right;
    if (y != p->right)
    {
      rb_transplant(t, y, y->right);
      y->right = p->right;
      y->right->parent = y;
    }
    else x->parent = y;
    rb_transplant(t, p, y);
    y->left = p->left;
    y->left->parent = y;
    y->color = p->color;
  }

  if (y_original_color == RBTREE_BLACK) rb_delete_fixup(t, x); // x는 대체된 노드
  return 0;
}

int rbtree_to_array(const rbtree *t, key_t *arr, const size_t n) {
  // TODO: implement to_array
  node_t *stack[100];  // 충분한 크기 가정
  int top = -1;
  node_t *current = t->root;
  int count = 0;

  while (top != -1 || current != t->nil) {
      while (current != t->nil) {
          stack[++top] = current;
          current = current->left;
      }

      current = stack[top--];

      if (count < n) {
          arr[count++] = current->key;
      } else {
          break;
      }

      current = current->right;
  }

  return count;
}

void left_rotate(rbtree *t, node_t *x)
{
  node_t *y = x->right;
  x->right = y->left;
  if (y->left != t->nil)
  {
    y->left->parent = x;
  }
  y->parent = x->parent;
  if (x->parent == t->nil)
  {
    t->root = y;
  }
  else if (x == x->parent->left)
  {
    x->parent->left = y;
  }
  else
  {
    x->parent->right = y;
  }
  y->left = x;
  x->parent = y;
}

void right_rotate(rbtree *t, node_t *x)
{
  node_t *y = x->left;
  x->left = y->right;
  if (y->right != t->nil)
  {
    y->right->parent = x;
  }
  y->parent = x->parent;
  if (x->parent == t->nil)
  {
    t->root = y;
  }
  else if (x == x->parent->right)
  {
    x->parent->right = y;
  }
  else
  {
    x->parent->left = y;
  }
  y->right = x;
  x->parent = y;
}

void rb_insert_fixup(rbtree *t, node_t *z)
{
  while (z->parent->color == RBTREE_RED)
  {
    if (z->parent == z->parent->parent->left)
    {
      node_t *y = z->parent->parent->right;
      if (y->color == RBTREE_RED) // Case 1
      {
        z->parent->color = RBTREE_BLACK;
        y->color = RBTREE_BLACK;
        z->parent->parent->color = RBTREE_RED;
        z = z->parent->parent;
      }
      else
      {
        if (z == z->parent->right) // Case 2
        {
          z = z->parent;
          left_rotate(t, z);
        }
        // Case 3
        z->parent->color = RBTREE_BLACK;
        z->parent->parent->color = RBTREE_RED;
        right_rotate(t, z->parent->parent);
      }
    }
    else
    {
      node_t *y = z->parent->parent->left;
      if (y->color == RBTREE_RED) // Case 1
      {
        z->parent->color = RBTREE_BLACK;
        y->color = RBTREE_BLACK;
        z->parent->parent->color = RBTREE_RED;
        z = z->parent->parent;
      }
      else
      {
        if (z == z->parent->left) // Case 2
        {
          z = z->parent;
          right_rotate(t, z);
        }
        // Case 3
        z->parent->color = RBTREE_BLACK;
        z->parent->parent->color = RBTREE_RED;
        left_rotate(t, z->parent->parent);
      }
    }
  }
  t->root->color = RBTREE_BLACK; // Ensure the root is always black
}

void rb_transplant(rbtree *t, node_t *u, node_t *v)
{
  if (u->parent == t->nil)
    t->root = v;
  else if (u == u->parent->left)
    u->parent->left = v;
  else
    u->parent->right = v;
  v->parent = u->parent;
}

void rb_delete_fixup(rbtree *t, node_t *x)
{
  while (x != t->root && x->color == RBTREE_BLACK)
  {
    if (x == x->parent->left)
    {
      node_t *w = x->parent->right;
      if (w->color == RBTREE_RED) // Case 1
      {
         w->color = RBTREE_BLACK;
         x->parent->color = RBTREE_RED;
         left_rotate(t, x->parent);
         w = x->parent->right; // 형제 변환
      }

      if (w->left->color == RBTREE_BLACK && w->right->color == RBTREE_BLACK) // Case 2
      {
        w->color = RBTREE_RED;
        x = x->parent; // 부모로 Double Black 전가
      }
      else
      {
        if (w->right->color == RBTREE_BLACK) // Case 3
        {
          w->left->color = RBTREE_BLACK;
          w->color = RBTREE_RED;
          right_rotate(t, w);
          w = x->parent->right; // 형제 변환
        }
        // Case 4
        w->color = x->parent->color;
        x->parent->color = RBTREE_BLACK;
        w->right->color = RBTREE_BLACK;
        left_rotate(t, x->parent);
        x = t->root;
      }
    }
    else
    {
      node_t *w = x->parent->left;
      if (w->color == RBTREE_RED) // Case 1
      {
        w->color = RBTREE_BLACK;
        x->parent->color = RBTREE_RED;
        right_rotate(t, x->parent);
        w = x->parent->left;
      }

      if (w->right->color == RBTREE_BLACK && w->left->color == RBTREE_BLACK) // Case 2
      {
        w->color = RBTREE_RED;
        x = x->parent;
      }
      else
      {
        if (w->left->color == RBTREE_BLACK) // Case 3
        {
          w->right->color = RBTREE_BLACK;
          w->color = RBTREE_RED;
          left_rotate(t, w);
          w = x->parent->left;
        }
        // Case 4
        w->color = x->parent->color;
        x->parent->color = RBTREE_BLACK;
        w->left->color = RBTREE_BLACK;
        right_rotate(t, x->parent);
        x = t->root;
      }
    }
  }
  x->color = RBTREE_BLACK; // Ensure the root is always black
}