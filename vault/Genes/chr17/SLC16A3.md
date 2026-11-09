---
symbol: "SLC16A3"
type: "gene"
col: 6537
ensembl_id: "ENSG00000141526"
name: "solute carrier family 16 member 3"
location: "17q25.3"
module: 113
arm: "+"
pooled_cpm: 136.96
n_lines_expressing: 43
n_dd_up: 4
n_dd_down: 34
n_dd_up_clean: 3
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 5
direction_downstream: 8
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# SLC16A3

*solute carrier family 16 member 3* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.23× (z +4.5, q 0.003, up in 21 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.447× (z -17.3, q 0e+00, down in 36 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIDN]] (+0.59, fdr 1e-05), [[SKI]] (+0.59, fdr 1e-05), [[EGLN3]] (+0.59, fdr 1e-05); moves opposite to [[VPS36]] (-0.52, fdr 6e-05), [[ZNF326]] (-0.50, fdr 2e-05), [[FAM204A]] (-0.49, fdr 5e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SERPINA1]] → it (grade B ⚠); 8 go from it, the strongest it → [[SLCO4A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6537.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.5 | 0.003 | 21/41 (A498, Hs 766T, …) | rises with dose |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.29×** | +3.9 | 0.029 | 27/41 (J82, HOP62, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.27×** | +3.7 | 0.039 | 23/41 (SNU-423, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.039 | 25/42 (HT-29, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Filgotinib (drug)]] 0.05 µM |  | 1.22× | +3.1 | 0.17 | 19/41 (J82, HOP62, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.17 | 17/41 (SW48, MIA PaCa-2, …) | two highest doses | low cells (technical?) |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 1.22× | +3.1 | 0.17 | 18/41 (Panc 03.27, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6537.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.447×** | -17.3 | 0e+00 | 36/41 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.376×** | -14.3 | 4e-44 | 39/41 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.406×** | -13.2 | 1e-37 | 37/41 (HT-29, KATO III, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.506×** | -10.4 | 5e-23 | 31/41 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.534×** | -9.5 | 2e-19 | 37/41 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.576×** | -8.4 | 5e-15 | 32/42 (SW 900, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.587×** | -7.7 | 1e-12 | 35/41 (SK-MEL-2, A498, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.607×** | -7.6 | 2e-12 | 36/41 (NCI-H23, HOP62, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.599×** | -7.5 | 4e-12 | 27/37 (CHP-212, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.627×** | -7.1 | 8e-11 | 34/41 (SK-MEL-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.637×** | -6.9 | 4e-10 | 32/41 (KATO III, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.643×** | -6.7 | 9e-10 | 29/41 (KATO III, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.645×** | -6.7 | 1e-09 | 33/41 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.646×** | -6.6 | 1e-09 | 34/41 (HT-29, BT-474, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.447×** | -6.4 | 6e-09 | 35/38 (NCI-H1573, HOP62, …) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.662×** | -6.3 | 1e-08 | 32/41 (NCI-H23, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.464×** | -6.1 | 3e-08 | 36/42 (KATO III, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.665×** | -5.9 | 8e-08 | 33/42 (HepG2/C3A, hTERT-HPNE, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.485×** | -5.8 | 2e-07 | 29/41 (KATO III, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.687×** | -5.7 | 3e-07 | 33/41 (SK-MEL-2, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6537. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 170 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -27.0) |
| [[SK-MEL-2 (line)]] | alt | 91.4 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -18.1) |
| [[KATO III (line)]] | alt | 176 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -19.6) |
| [[NCI-H23 (line)]] | alt | 88.8 | 1 (1 ⚠) | 12 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +9.2) ⚠ cell-cycle shift, explains ~50% of this change | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -27.1) |
| [[BT-474 (line)]] | alt | 89.1 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -17.7) |
| [[HT-29 (line)]] | alt | 150 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -22.4) |
| [[NCI-H1573 (line)]] | alt | 260 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -23.7) |
| [[Hs 766T (line)]] | wt | 112 | 0 | 6 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.268× (z -12.8) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.361× (z -9.9) |
| [[SW 900 (line)]] | alt | 160 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.273× (z -12.9) |
| [[HepG2_C3A (line)]] | wt | 288 | 0 | 5 (3 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.286× (z -12.8) |
| [[PANC-1 (line)]] | alt | 234 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -22.5) |
| [[A498 (line)]] | wt | 142 | 0 | 4 | — | [[Ixazomib citrate (drug)]] 5 µM 0.376× (z -10.2) |
| [[A549 (line)]] | wt | 81.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -22.0) |
| [[CHP-212 (line)]] | wt | 269 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -17.9) |
| [[H4 (line)]] | wt | 173 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.190× (z -14.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.361× (z -13.2) |
| [[HOP62 (line)]] | alt | 310 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.390× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 63.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -13.7) |
| [[LS 180 (line)]] | wt | 98.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -12.6) |
| [[SW480 (line)]] | alt | 160 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.306× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 141 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -23.8) |
| [[MIA PaCa-2 (line)]] | alt | 147 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 185 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -15.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 64.0 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.173× (z -14.7) |
| [[SW48 (line)]] | wt | 126 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -11.8) |
| [[A-172 (line)]] | wt | 109 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -14.4) |
| [[CFPAC-1 (line)]] | alt | 252 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -10.6) |
| [[HCT15 (line)]] | alt | 154 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -15.9) |
| [[hTERT-HPNE (line)]] | wt | 272 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.362× (z -10.2) ⚠ toxic · without an alert: [[Verteporfin (drug)]] 5 µM 0.405× (z -9.0) |
| [[J82 (line)]] | alt | 192 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 140 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 86.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +9.7) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[C-33 A (line)]] | alt | 40.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -9.9) |
| [[COLO 205 (line)]] | alt | 187 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.193× (z -10.8) ⚠ toxic |
| [[LoVo (line)]] | wt | 42.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +10.1) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H1792 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.303× (z -10.2) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 36.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.405× (z -8.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 25.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 23.5 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 23.8 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 28.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 13.2 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.0 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 50.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6537), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIDN]] | +0.59 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[SKI]] | +0.59 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[EGLN3]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[ZSWIM6]] | +0.57 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[ANGPTL4]] | +0.57 | +0.59 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[POLG]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 | same gene group |
| [[EIF4A3]] | +0.56 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[RCOR1]] | +0.55 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[ERRFI1]] | +0.55 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ARHGAP45]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[MAFB]] | +0.53 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[TUBB4B]] | +0.52 | +0.42 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS36]] | -0.52 | -0.39 / -0.57 | both halves | 6e-05 |  |
| [[ZNF326]] | -0.50 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[FAM204A]] | -0.49 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[CIZ1]] | -0.49 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[DRAM2]] | -0.49 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[SCP2]] | -0.48 | -0.36 / -0.51 | both halves | 9e-05 | same gene group |
| [[MRPL16]] | -0.48 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[NNT]] | -0.47 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[IQCK]] | -0.47 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[VTI1B]] | -0.46 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[SCRN3]] | -0.46 | -0.32 / -0.56 | both halves | 2e-04 |  |
| [[LMO3]] | -0.46 | -0.47 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINA1]] | B | SERPINA1 activity raises SLC16A3's level | lines that do not express SERPINA1 (34) vs lines expressing it (16) | 1.98× lower at baseline in the lines without SERPINA1 | 0.036 | ⚠ within organs, on part of the lines; also absent: SERPINA5, CST6, SERPINA3 |
| [[MYO1E]] | B | MYO1E activity raises SLC16A3's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 3.31× lower at baseline in the lines without MYO1E | 0.044 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[SLCO4A1]] | B | SLCO4A1 activity raises SLC16A3's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 2.55× lower at baseline in the lines without SLCO4A1 | 0.047 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[NIBAN2]] | B | NIBAN2 activity raises SLC16A3's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 4.43× lower at baseline in the lines without NIBAN2 | 0.089 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[SDC4]] | C | SDC4 activity raises SLC16A3's level | lines that do not express SDC4 (5) vs lines expressing it (45) | 5.54× lower at baseline in the lines without SDC4 | 0.060 | ⚠ within organs, on part of the lines; also absent: LAMB1, TGFBR2, PHLDA2; co-absent with the target; its own permutation p |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLCO4A1]] | B | SLC16A3 activity raises SLCO4A1's level | lines that do not express SLC16A3 (7) vs lines expressing it (43) | 3.31× lower at baseline in the lines without SLC16A3 | 0.032 | ⚠ within organs, on part of the lines; also absent: IL4R, SDC4, ARHGAP27; maybe low, not absent |
| [[PLIN3]] | B | SLC16A3 activity raises PLIN3's level | lines that do not express SLC16A3 (7) vs lines expressing it (43) | 1.60× lower at baseline in the lines without SLC16A3 | 0.047 | ⚠ within organs, on part of the lines; also absent: IL4R, SDC4, ARHGAP27; maybe low, not absent |
| [[PDIK1L]] | B | SLC16A3 activity lowers PDIK1L's level | lines that do not express SLC16A3 (7) vs lines expressing it (43) | 1.26× higher at baseline in the lines without SLC16A3 | 0.060 | ⚠ within organs, on part of the lines; also absent: IL4R, SDC4, ARHGAP27; maybe low, not absent |
| [[S100A11]] | B | SLC16A3 activity raises S100A11's level | lines that do not express SLC16A3 (7) vs lines expressing it (43) | 1.63× lower at baseline in the lines without SLC16A3 | 0.068 | ⚠ within organs, on part of the lines; also absent: IL4R, SDC4, ARHGAP27; maybe low, not absent |
| [[NIBAN2]] | B | SLC16A3 activity raises NIBAN2's level | lines that do not express SLC16A3 (7) vs lines expressing it (43) | 2.29× lower at baseline in the lines without SLC16A3 | 0.069 | ⚠ within organs, on part of the lines; also absent: IL4R, SDC4, ARHGAP27; maybe low, not absent |
| [[PFKFB3]] | B | SLC16A3 activity raises PFKFB3's level | lines that do not express SLC16A3 (7) vs lines expressing it (43) | 1.73× lower at baseline in the lines without SLC16A3 | 0.072 | ⚠ within organs, on part of the lines; also absent: IL4R, SDC4, ARHGAP27; maybe low, not absent |
| [[AGPAT2]] | B | SLC16A3 activity raises AGPAT2's level | lines that do not express SLC16A3 (7) vs lines expressing it (43) | 2.16× lower at baseline in the lines without SLC16A3 | 0.084 | ⚠ within organs, on part of the lines; also absent: IL4R, SDC4, ARHGAP27; maybe low, not absent |
| [[SDC4]] | C | SLC16A3 activity raises SDC4's level | lines that do not express SLC16A3 (7) vs lines expressing it (43) | 3.17× lower at baseline in the lines without SLC16A3 | 0.042 | ⚠ within organs, on part of the lines; also absent: IL4R, SDC4, ARHGAP27; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.599). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.4, -16.2); signed map (-20.9, 41.8). **Vector** length 120, 40.9% of its response variance represented; |z| ≥ 3 in 1,341 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +4.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.0 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +1.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | -0.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.2 | +1.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.7 | +2.7 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.6 | -8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.1 | -7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.8 | -6.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.5 | -6.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.9 | -13.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.7 | -3.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.3 | -5.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.7 | -3.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 16 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,217,934-82,261,129 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MCT3, MCT4 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Solute carrier family 16 |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 7 pathways, smallest: Proton-coupled monocarboxylate transport; Basigin interactions; SLC-mediated transport of organic anions |
| Matched by | ensembl_id |

**Function**, from UniProt [O15427](https://www.uniprot.org/uniprotkb/O15427) (Monocarboxylate transporter 4):

> Proton-dependent transporter of monocarboxylates such as L-lactate and pyruvate. Plays a predominant role in L-lactate efflux from highly glycolytic cells (By similarity).

**Summary**, from NCBI Gene [9123](https://www.ncbi.nlm.nih.gov/gene/9123):

> Lactic acid and pyruvate transport across plasma membranes is catalyzed by members of the proton-linked monocarboxylate transporter (MCT) family, which has been designated solute carrier family-16. Each MCT appears to have slightly different substrate and inhibitor specificities and transport kinetics, which are related to the metabolic requirements of the tissues in which it is found. The MCTs, which include MCT1 (SLC16A1; MIM 600682) and MCT2 (SLC16A7; MIM 603654), are characterized by 12 …

**Accessions** — [HGNC:10924](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10924) · Entrez [9123](https://www.ncbi.nlm.nih.gov/gene/9123) · UniProt [O15427](https://www.uniprot.org/uniprotkb/O15427) · Ensembl [ENSG00000141526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141526)

## Data

Gene col 6537: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6537); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6537, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6537]; `tensor/DDL_lfc|DDL_z.npy` [6537]; `embed/gene_vectors.npy` [6537]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6537 or target_col == 6537). Every well: [[SLC16A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC16A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
