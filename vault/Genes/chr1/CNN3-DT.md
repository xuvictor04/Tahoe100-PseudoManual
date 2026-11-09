---
symbol: "CNN3-DT"
type: "gene"
col: 14022
ensembl_id: "ENSG00000235501"
name: "CNN3 divergent transcript"
location: "1p21.3"
module: 10
arm: "+"
pooled_cpm: 2.65
n_lines_expressing: 42
n_dd_up: 36
n_dd_down: 5
n_dd_up_clean: 28
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# CNN3-DT

*CNN3 divergent transcript* — 1p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.21× (z +20.1, q 0e+00, up in 27 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.551× (z -5.9, q 2e-06, down in 16 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TENM3-AS1]] (+0.62, fdr 1e-05), [[HDAC2-AS2]] (+0.62, fdr 2e-05), [[TMEM72-AS1]] (+0.61, fdr 1e-05); moves opposite to [[SFI1]] (-0.51, fdr 3e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[BEND6]] → it (grade B ⚠); 4 go from it, the strongest it → [[STARD4-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14022.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.21×** | +20.1 | 0e+00 | 27/29 (PANC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +9.0 | 7e-17 | 1/5 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.87×** | +8.7 | 7e-16 | 15/27 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.02×** | +6.9 | 7e-10 | 7/12 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.87×** | +6.2 | 7e-08 | 16/32 (A498, J82, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +5.9 | 3e-07 | 2/5 (NCI-H2347, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +5.3 | 7e-06 | 6/23 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +5.2 | 2e-05 | 15/35 (A-172, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.42×** | +4.8 | 7e-05 | 7/34 (A-427, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.42×** | +4.8 | 7e-05 | 2/34 (C-33 A, NCI-H2347) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.61×** | +4.7 | 1e-04 | 11/36 (NCI-H1792, A498, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.62×** | +4.5 | 3e-04 | 6/33 (NCI-H2030, HepG2/C3A, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **1.39×** | +4.5 | 3e-04 | 9/34 (SW480, A498, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.59×** | +4.4 | 5e-04 | 9/30 (SW480, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +4.4 | 5e-04 | 13/34 (J82, A498, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.3 | 7e-04 | 9/28 (A-427, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ferulic acid (drug)]] 0.5 µM |  | **1.54×** | +4.2 | 8e-04 | 3/33 (NCI-H1573, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.50×** | +3.8 | 0.005 | 6/33 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.005 | 8/36 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14022.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.551×** | -5.9 | 2e-06 | 16/35 (PANC-1, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.658×** | -4.2 | 0.009 | 12/34 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.667×** | -4.0 | 0.011 | 5/36 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.685×** | -3.8 | 0.023 | 10/32 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Malotilate (drug)]] 0.05 µM |  | **0.702×** | -3.5 | 0.048 | 5/31 (KATO III, RKO, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.728× | -3.0 | 0.22 | 2/34 (SW480, PANC-1) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14022. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.78 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +8.7) | [[Ixazomib citrate (drug)]] 0.5 µM 0.0564× (z -13.7) |
| [[SW480 (line)]] | alt | 3.40 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0599× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0827× (z -9.6) |
| [[HOP62 (line)]] | alt | 1.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 4.47 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[RKO (line)]] | wt | 4.57 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM 0.0620× (z -9.0) |
| [[A-172 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.253 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.636 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.868 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.435 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.337 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.780 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.930 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.569 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.692 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14022), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TENM3-AS1]] | +0.62 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[HDAC2-AS2]] | +0.62 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[TMEM72-AS1]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[BEND6]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[HSD11B1-AS1]] | +0.60 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[MYH7B]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[MRAS]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ZBED5-AS1]] | +0.58 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ATXN1-AS1]] | +0.58 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[CYP1B1-AS1]] | +0.57 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[GALNT7-DT]] | +0.57 | +0.62 / +0.32 | both halves | 2e-04 | same gene group |
| [[LRRC8C-DT]] | +0.57 | +0.60 / +0.44 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFI1]] | -0.51 | -0.56 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BEND6]] | B | BEND6 activity raises CNN3-DT's level | lines that do not express BEND6 (14) vs lines expressing it (36) | 1.87× lower at baseline in the lines without BEND6 | 0.037 | ⚠ within organs, on part of the lines; also absent: GNB4, MAP1B, MPDZ |
| [[COL28A1]] | C | COL28A1 activity lowers CNN3-DT's level | lines that do not express COL28A1 (3) vs lines expressing it (47) | 2.00× higher at baseline in the lines without COL28A1 | 0.068 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNAJC6, KIFC3, MLLT3; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD4-AS1]] | B | CNN3-DT activity raises STARD4-AS1's level | lines that do not express CNN3-DT (8) vs lines expressing it (42) | 1.94× lower at baseline in the lines without CNN3-DT | 0.032 | ⚠ within organs, on part of the lines; also absent: MPP2, CNN3, SLC35F1; maybe low, not absent |
| [[C7orf31]] | B | CNN3-DT activity raises C7orf31's level | lines that do not express CNN3-DT (8) vs lines expressing it (42) | 2.30× lower at baseline in the lines without CNN3-DT | 0.047 | ⚠ within organs, on part of the lines; also absent: MPP2, CNN3, SLC35F1; maybe low, not absent |
| [[LRRC8C-DT]] | B | CNN3-DT activity raises LRRC8C-DT's level | lines that do not express CNN3-DT (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without CNN3-DT | 0.060 | ⚠ within organs, on part of the lines; also absent: MPP2, CNN3, SLC35F1; maybe low, not absent |
| [[LRRC8C-DT]] | B | CNN3-DT activity strengthens LRRC8C-DT's drug response | lines that do not express CNN3-DT (8) vs lines expressing it (38) | the lines without CNN3-DT respond 0.50× as strongly (z diff +1.10); strongest at Dinaciclib 0.5 µM: 0.66x vs 1.65x (z diff +3.1) | 0.077 | ⚠ within organs, on part of the lines; also absent: MPP2, CNN3, SLC35F1; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.535). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (16.2, 21.1); signed map (38.4, 0.1). **Vector** length 47.0, 6.72% of its response variance represented; |z| ≥ 3 in 853 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +20.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +9.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.8 | +4.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.7 | +4.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.4 | -5.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.3 | +2.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +2.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -3.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[Ranolazine (drug)]] 0.5 µM |  | -1.0 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | CNN3 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p21.3 — chr1:94,927,361-95,067,545 (+) |
| Ensembl biotype | lncRNA |
| Also known as | RP4-639F20.1; previously ALG14-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54176](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54176) · Entrez [729970](https://www.ncbi.nlm.nih.gov/gene/729970) · Ensembl [ENSG00000235501](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235501)

## Data

Gene col 14022: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14022); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14022, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14022]; `tensor/DDL_lfc|DDL_z.npy` [14022]; `embed/gene_vectors.npy` [14022]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14022 or target_col == 14022). Every well: [[CNN3-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNN3-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
