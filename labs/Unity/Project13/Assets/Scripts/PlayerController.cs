using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    Animator anim;
    public float speed = 100f;
    private Rigidbody2D rb;
    public Joystick joystick;
    void Start()
    {
        rb = GetComponent <Rigidbody2D>();
        anim = GetComponent <Animator>();

    }
    void Update()
    {
        
        if (joystick.Horizontal  == 0)
        {
            anim.SetInteger("State",1);

        }
        else
        {
            Flip(); 
            anim.SetInteger("State",3);
        }

        
    }

    void Flip()
    {
        if(joystick.Horizontal  > 0)
        {
            transform.localRotation = Quaternion.Euler(0,0,0);
        }

        if(joystick.Horizontal  < 0)
        {
            transform.localRotation = Quaternion.Euler(0,180,0);
        }
    }
    
   public void Jump()
    {
        
        anim.SetInteger("State",2);
        rb.AddForce(transform.up * 1000f, ForceMode2D.Impulse);
    
    }
    void OnTriggerEnter2D(Collider2D carrots)
    {
        Debug.Log(carrots.gameObject.tag);
        if (carrots.gameObject.tag == "Player")
        {
            Destroy(carrots.gameObject);
            //ExecuteAfterTime(5f, carrots);

        }

    }
    IEnumerator ExecuteAfterTime(float timeInSec, Collider2D carrots)
    {
        yield return new WaitForSeconds(timeInSec);
        Destroy(carrots.gameObject);
    }

    void FixedUpdate()
    {
      rb.velocity = new Vector2(joystick.Horizontal * 420f,rb.velocity.y);
    }
}
