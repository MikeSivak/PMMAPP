using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ChangeLocation : MonoBehaviour
{
    Camera camera;

    private void OnMouseDown(){
        camera = Camera.main;
        camera.transform.position = new Vector3(1,0,-2);
    }
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
