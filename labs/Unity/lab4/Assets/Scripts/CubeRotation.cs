using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CubeRotation : MonoBehaviour
{
    float y;
    public GameObject target1;
    public GameObject target2;
    public float distanceX;
    public float distanceY;
    public float distanceZ;
    public float distanceTotal;
    public Transform other;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame

    void Update()
    {
        y += Time.deltaTime * 10;
        transform.rotation = Quaternion.Euler(0, y, 0);

        Vector3 delta = target2.transform.position - target1.transform.position;
        distanceX = delta.x;
        distanceY = delta.y;
        distanceZ = delta.z;
        distanceTotal = delta.magnitude;

        if (distanceTotal < 10)
        {
            transform.position = Vector3.MoveTowards(transform.position, target1.transform.position, Time.deltaTime);
        }

        if (other)
        {
            Vector3 forward = transform.TransformDirection(Vector3.forward);
            Vector3 toOther = other.position - transform.position;

            if (Vector3.Dot(forward, toOther) < 0)
            {
                transform.position = Vector3.MoveTowards(transform.position, target1.transform.position, Time.deltaTime);
            }
        }

    }
}
