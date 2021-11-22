using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class CoinsCounter : MonoBehaviour
{

    public GameObject text;
    public GameObject endtext;
    private int score = 0;
    void Start()
    {
        text.SetActive(false);
        endtext.SetActive(false);

    }
    void OnTriggerEnter2D(Collider2D carrots)
    {
        if(carrots.gameObject.tag == "Carrot")
        {
           
           Destroy(carrots.gameObject);
           score++;
           text.SetActive(true);
           text.GetComponent<Text>().text = "Carrots: " + score.ToString() +"/30";

        }
        else if(carrots.gameObject.tag == "GoldCarrot")
        {
            Destroy(carrots.gameObject);
            score = score +5;
            text.SetActive(true);
            text.GetComponent<Text>().text = "Carrots: " + score.ToString() + "/30";
        }
        if (score == 30)
        {
            endtext.SetActive(true);
            score = 0;
            
            SceneManager.LoadScene("FinalScene");         
        }
    
    }

}
