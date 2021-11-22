using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Shooting : MonoBehaviour
{
    public int score = 0;
    public GameObject text;

    void Start()
    {
        text.SetActive(false);
    }

    void Update()
    {
        if (Input.GetMouseButtonDown(0))
        {
            Ray ray = Camera.main.ScreenPointToRay(new Vector2(Input.mousePosition.x, Input.mousePosition.y));
            RaycastHit _hit;
            if (Physics.Raycast(ray, out _hit))
            {
                if (_hit.collider.tag == "ShootingCube")
                {
                    Destroy(_hit.collider.gameObject);
                    score++;
                    text.SetActive(true);
                    text.GetComponent<Text>().text = "Score: " + score.ToString();


                    Debug.Log("Попадание в куб");



                }
                Debug.DrawRay(transform.position, transform.forward, Color.red, 1.0f, false);
            }
        }
    }

}
