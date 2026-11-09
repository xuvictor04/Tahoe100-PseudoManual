---
module: 131
type: "module"
n_genes: 36
n_plus: 36
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "Eukaryotic Translation Termination"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 131

*Eukaryotic Translation Termination · 36 genes (single-armed) · [[Module 131.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **Eukaryotic Translation Termination** (reactome, q 2e-32; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Eukaryotic Translation Termination | reactome | 20/36 | 92.0 | 2e-32 |
| + | Eukaryotic Translation Termination | reactome | 20/36 | 92.0 | 2e-32 |
| + | Peptide chain elongation | reactome | 19/36 | 91.5 | 2e-30 |
| all | Peptide chain elongation | reactome | 19/36 | 91.5 | 2e-30 |
| all | PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA | reactome | 19/36 | 90.4 | 3e-30 |
| + | PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA | reactome | 19/36 | 90.4 | 3e-30 |
| + | Viral mRNA Translation | reactome | 19/36 | 88.4 | 4e-30 |
| all | Viral mRNA Translation | reactome | 19/36 | 88.4 | 4e-30 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 130), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 0.5 µM (+4.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+4.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+3.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (+3.6, ⚠ transcription drop; cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+3.3, ⚠ toxic; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+3.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (+2.5); [[Niclosamide (olamine) (drug)]] 5 µM (+2.3, ⚠ toxic; cell-cycle shift); [[Bendamustine (drug)]] 5 µM (+2.2); [[Arbutin (drug)]] 5 µM (+2.2); [[9-ING-41 (drug)]] 0.5 µM (+2.1); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+2.1); [[Azithromycin (hydrate) (drug)]] 5 µM (+2.0); [[Sulfatinib (drug)]] 5 µM (+2.0); [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM (+2.0); [[XRK3F2 (drug)]] 0.5 µM (+1.9); [[Methylprednisolone succinate (drug)]] 0.5 µM (+1.9) (115 in all, 25 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-4.3, ⚠ cell-cycle shift); [[Folic acid (drug)]] 5 µM (-2.1); [[Diphenhydramine (drug)]] 0.05 µM (-2.0); [[Sapanisertib (drug)]] 5 µM (-2.0); [[Ralimetinib dimesylate (drug)]] 0.05 µM (-1.9, ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 0.5 µM (-1.9, ⚠ cell-cycle shift); [[Demeclocycline (drug)]] 5 µM (-1.9); [[Anethole trithione (drug)]] 0.5 µM (-1.9); [[Encorafenib (drug)]] 5 µM (-1.9); [[Budesonide (drug)]] 5 µM (-1.9); [[Fenofibrate (drug)]] 0.05 µM (-1.9); [[Tirabrutinib (drug)]] 0.05 µM (-1.9); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM (-1.8) (116 in all, 15 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[SW480 (line)]], [[HT-29 (line)]], [[LS 180 (line)]], [[SW 900 (line)]], [[PANC-1 (line)]], [[HOP62 (line)]], [[LoVo (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 34 candidates, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert.*

| # | Gene | Set | Mean cos | Alert |
|---|---|---|---|---|
| 1 | [[RPS10]] | Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide | +0.93 |  |
| 2 | [[RPS25]] | Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide | +0.93 |  |
| 3 | [[RPS13]] ⚠ | Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide | +0.93 | ⚠ in the vector space only through drug-doses that carry an alert |
| 4 | [[RPL32]] | SARS-CoV-1 modulates host translation machinery | +0.92 |  |
| 5 | [[RPS21]] | Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide | +0.91 |  |
| 6 | [[RPS29]] | Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide | +0.91 |  |
| 7 | [[RPL28]] | SARS-CoV-1 modulates host translation machinery | +0.91 |  |
| 8 | [[RPS16]] ⚠ | Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide | +0.91 | ⚠ in the vector space only through drug-doses that carry an alert |
| 9 | [[RPS11]] | Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide | +0.91 |  |
| 10 | [[RPS23]] | Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide | +0.91 |  |
| 11 | [[RPLP2]] | SARS-CoV-1 modulates host translation machinery | +0.91 |  |
| 12 | [[RPL36A]] | SARS-CoV-1 modulates host translation machinery | +0.91 |  |
| 13 | [[RPL38]] | SARS-CoV-1 modulates host translation machinery | +0.90 |  |
| 14 | [[RPL8]] ⚠ | SARS-CoV-1 modulates host translation machinery | +0.89 | ⚠ in the vector space only through drug-doses that carry an alert |
| 15 | [[RPL7A]] | SARS-CoV-1 modulates host translation machinery | +0.89 |  |
| 16 | [[RPL15]] | SARS-CoV-1 modulates host translation machinery | +0.88 |  |
| 18 | [[RPS24]] | Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide | +0.86 |  |
| 19 | [[FAU]] | Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide | +0.84 |  |

*⚠ 5 of its 36 genes are in the vector space only through drug-doses that carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what those drug-doses did to the cells. They are marked in the tables of this note.*

## + arm (36)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[RPS21]] | 0.969 | ribosomal protein S21 |  |
| [[RPL36A]] | 0.962 | ribosomal protein L36a |  |
| [[RPS29]] | 0.961 | ribosomal protein S29 |  |
| [[RPS10]] | 0.961 | ribosomal protein S10 |  |
| [[RPLP2]] | 0.961 | ribosomal protein lateral stalk subunit P2 |  |
| [[RPS25]] | 0.960 | ribosomal protein S25 |  |
| [[RPS13]] | 0.959 | ribosomal protein S13 | ⚠ only flagged evidence |
| [[RPL28]] | 0.953 | ribosomal protein L28 |  |
| [[RPL32]] | 0.952 | ribosomal protein L32 |  |
| [[RPS11]] | 0.951 | ribosomal protein S11 |  |
| [[RPL38]] | 0.947 | ribosomal protein L38 |  |
| [[RPS23]] | 0.947 | ribosomal protein S23 |  |
| [[RPL7A]] | 0.933 | ribosomal protein L7a |  |
| [[RPS15]] | 0.925 | ribosomal protein S15 | ⚠ only flagged evidence |
| [[RPL8]] | 0.922 | ribosomal protein L8 | ⚠ only flagged evidence |
| [[RPS16]] | 0.917 | ribosomal protein S16 | ⚠ only flagged evidence |
| [[RPL15]] | 0.914 | ribosomal protein L15 |  |
| [[SNHG25]] | 0.903 | small nucleolar RNA host gene 25 |  |
| [[FAU]] | 0.898 | FAU ubiquitin like and ribosomal protein S30 fusion |  |
| [[RPS24]] | 0.885 | ribosomal protein S24 |  |
| [[TPT1]] | 0.871 | tumor protein, translationally-controlled 1 |  |
| [[ASTN2]] | 0.801 | astrotactin 2 |  |
| [[SNRPD2]] | 0.777 | small nuclear ribonucleoprotein D2 polypeptide |  |
| [[CHCHD2]] | 0.773 | coiled-coil-helix-coiled-coil-helix domain containing 2 |  |
| [[GAS5]] | 0.750 | growth arrest specific 5 |  |
| [[ATP5MG]] | 0.748 | ATP synthase membrane subunit g |  |
| [[MZT2B]] | 0.746 | mitotic spindle organizing protein 2B |  |
| [[TRMT112]] | 0.732 | tRNA methyltransferase activator subunit 11-2 |  |
| [[FKBP2]] | 0.651 | FKBP prolyl isomerase 2 | ⚠ only flagged evidence |
| [[ABHD18]] | 0.651 | abhydrolase domain containing 18 |  |
| [[TRPC4AP]] | 0.640 | transient receptor potential cation channel subfamily C member 4 associated protein |  |
| [[MZT2A]] | 0.637 | mitotic spindle organizing protein 2A |  |
| [[HINT1]] | 0.635 | histidine triad nucleotide binding protein 1 |  |
| [[PI4KAP1-1]] | 0.609 | — |  |
| [[LUC7L]] | 0.515 | LUC7 like |  |
| [[LINC01425]] | 0.451 | long independently transcribed non-coding RNA 1425 |  |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 131; `graph/modules.parquet` — module == 131; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [130] (drug-dose × line)
