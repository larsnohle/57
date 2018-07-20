import java.io.*;
import java.util.*;

public class FortySevenChallengeThree {
  
  private void displayResults(Map<Integer, List<String>> frequencyToWordsMap) {
    List<Integer> frequencies = new ArrayList<Integer>(frequencyToWordsMap.keySet());
    Collections.sort(frequencies, (x, y) -> y - x);

    for (Integer frequency : frequencies) {
      for (String word : frequencyToWordsMap.get(frequency)) {
        System.out.print(word + " : "); 
        printStars(frequency);
        System.out.println("");
      }
    }
  }

  private void printStars(int numberOfStars) {
    for (int i = 0; i < numberOfStars; i++) {
      System.out.print("*");
    }
  }
  
  private void addToFrequencyToWordMap(Map<Integer, List<String>> frequencyToWordsMap, String word, int newFrequency) {
    if (newFrequency > 1) {
      frequencyToWordsMap.get(newFrequency - 1).remove(word);
    }

    List<String> listToAddWordTo;
    if (frequencyToWordsMap.containsKey(newFrequency)) {
      listToAddWordTo = frequencyToWordsMap.get(newFrequency);
    } else {
      listToAddWordTo = new ArrayList<String>();
      frequencyToWordsMap.put(newFrequency, listToAddWordTo);
    }

    listToAddWordTo.add(word);
  }
         
  
  private Map<Integer, List<String>> openAndProcessFile(String filename) {
    Map<Integer, List<String>> frequencyToWordsMap = new HashMap<>();
    Map<String, Integer> wordFrequencyMap = new HashMap<>();

    try (FileReader fr = new FileReader(filename); BufferedReader br = new BufferedReader(fr)) {
      String line;
      while ((line = br.readLine()) != null) {
        StringTokenizer toke = new StringTokenizer(line.trim());
        while (toke.hasMoreTokens()) {
          String word = toke.nextToken();
          int newFrequency;
          if (wordFrequencyMap.containsKey(word)) {
            newFrequency = wordFrequencyMap.get(word) + 1;
          } else {
            newFrequency = 1;
          }
          
          wordFrequencyMap.put(word, newFrequency);
          addToFrequencyToWordMap(frequencyToWordsMap, word, newFrequency);
        }
      }      
    } catch (IOException ioe) {
      ioe.printStackTrace();
    }
        
    return frequencyToWordsMap;
  }
  
  public static void main(String[] args) {
    if (args.length < 1) {
      System.out.println("Usage: fortySixChallengeThree filename");
      System.exit(0);
    }
    long startTime = System.currentTimeMillis();
    FortySevenChallengeThree instance = new FortySevenChallengeThree();
    Map<Integer, List<String>> frequencyToWordsMap = instance.openAndProcessFile(args[0]);
    instance.displayResults(frequencyToWordsMap);
    long endTime = System.currentTimeMillis();
    System.out.println("Duration: " + (endTime - startTime) + " ms"); 
  } 
}
