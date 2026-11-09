---
symbol: "SLC25A6"
type: "gene"
col: 9752
ensembl_id: "ENSG00000169100"
name: "solute carrier family 25 member 6"
location: "Xp22.32 and Yp11.3"
module: 43
arm: "+"
pooled_cpm: 87.36
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# SLC25A6

*solute carrier family 25 member 6* — Xp22.32 and Yp11.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.14× (z +11.0, q 2e-25, up in 46 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.53× (z +4.4, q 0.001, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.535× (z -9.2, q 3e-17, down in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (A-427 0.236×, SW480 0.299×, H4 0.225×, SNU-1 0.284×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SW48 0.171×, A-427 0.316×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPLP0]] (+0.84, fdr 7e-06), [[RACK1]] (+0.84, fdr 7e-06), [[EEF1G]] (+0.82, fdr 7e-06); moves opposite to [[FAM111A]] (-0.55, fdr 1e-05), [[ZNF518A]] (-0.55, fdr 4e-05), [[ZNF620]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9752.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.14×** | +11.0 | 2e-25 | 46/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.33×** | +8.4 | 1e-14 | 39/43 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.84×** | +6.3 | 5e-08 | 40/47 (KATO III, HepG2/C3A, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.89×** | +6.1 | 2e-07 | 38/45 (LoVo, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +4.4 | 0.001 | 33/48 (MIA PaCa-2, KATO III, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +3.7 | 0.020 | 30/48 (CFPAC-1, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +3.6 | 0.023 | 30/48 (J82, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.41×** | +3.6 | 0.024 | 30/47 (AsPC-1, NCI-H460, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.93×** | +3.6 | 0.024 | 31/45 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.90×** | +3.5 | 0.029 | 34/48 (KATO III, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.055 | 32/48 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.058 | 28/48 (J82, NCI-H2030, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.81×** | +3.2 | 0.059 | 30/47 (NCI-H2030, LoVo, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9752.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (A-427 0.236×, SW480 0.299×, H4 0.225×, SNU-1 0.284×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SW48 0.171×, A-427 0.316×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.535×** | -9.2 | 3e-17 | 38/48 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.594×** | -5.4 | 2e-05 | 34/48 (SW48, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9752. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 157 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -10.9) |
| [[SW480 (line)]] | alt | 89.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -14.4) |
| [[A-427 (line)]] | wt | 127 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -18.3) |
| [[C-33 A (line)]] | alt | 65.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -11.3) |
| [[HCT15 (line)]] | alt | 103 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 173 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 193 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 77.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +9.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -9.9) ⚠ cell-cycle shift, explains ~81% of this change |
| [[SNU-1 (line)]] | wt | 172 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -13.0) |
| [[SW48 (line)]] | wt | 138 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -13.1) |
| [[A549 (line)]] | wt | 109 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +10.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 104 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 67.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +8.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 92.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -12.1) |
| [[COLO 205 (line)]] | alt | 30.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.68× (z +9.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 126 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 54.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 115 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 40.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 82.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -11.3) |
| [[LS 180 (line)]] | wt | 70.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 57.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 41.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 181 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 36.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 95.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +9.9) ⚠ cell-cycle shift, explains ~81% of this change | — |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -10.0) |
| [[PANC-1 (line)]] | alt | 41.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -9.1) |
| [[RKO (line)]] | wt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -12.5) |
| [[SNU-423 (line)]] | alt | 149 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 91.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 81.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 110 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 76.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9752), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 14 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPLP0]] | +0.84 | +0.85 / +0.76 | both halves | 7e-06 | pathway: Influenza Infection; STRING 474 |
| [[RACK1]] | +0.84 | +0.84 / +0.79 | both halves | 7e-06 | STRING 465 |
| [[EEF1G]] | +0.82 | +0.81 / +0.80 | both halves | 7e-06 | STRING 495 |
| [[RPL7]] | +0.78 | +0.77 / +0.71 | both halves | 7e-06 | pathway: Influenza Infection |
| [[RPS5]] | +0.77 | +0.74 / +0.69 | both halves | 7e-06 | pathway: Influenza Infection; STRING 718 |
| [[RPL27A]] | +0.77 | +0.79 / +0.70 | both halves | 7e-06 | pathway: Influenza Infection |
| [[EIF3L]] | +0.74 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[RPL29]] | +0.73 | +0.76 / +0.67 | both halves | 7e-06 | pathway: Influenza Infection; STRING 429 |
| [[RPS4X]] | +0.72 | +0.73 / +0.71 | both halves | 7e-06 | pathway: Influenza Infection; STRING 550 |
| [[RPL7A]] | +0.72 | +0.76 / +0.60 | both halves | 7e-06 | pathway: Influenza Infection; STRING 446 |
| [[SNHG29]] | +0.72 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[RPL11]] | +0.72 | +0.68 / +0.65 | both halves | 7e-06 | pathway: Influenza Infection |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM111A]] | -0.55 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[ZNF518A]] | -0.55 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[ZNF620]] | -0.54 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[PYM1]] | -0.54 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[CDC42EP1]] | -0.53 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.684). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-46.6, -30.1); signed map (-61.3, -6.7). **Vector** length 89.3, 31.8% of its response variance represented; |z| ≥ 3 in 658 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.62 to 55); *Peptide chain elongation* (reactome, mean cos +0.62 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.62 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +3.9 | +3.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +1.8 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | +1.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.1 | +2.0 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +1.3 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.6 | +0.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | -1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.9 | -9.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -0.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.5 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.6 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -2.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.8 | +1.1 |
|  | [[vincristine (drug)]] 5 µM |  | -1.4 | +1.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 25 member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.32 and Yp11.3 — chrX:1,386,152-1,392,113 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ANT3Y, MGC17525; previously ANT3 |
| Gene groups (HGNC) | Pseudoautosomal region 1; Solute carrier family 25 |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 14 pathways, smallest: Influenza Virus Induced Apoptosis; Vpr-mediated induction of apoptosis by mitochondrial outer membrane permeabilization; Transport of nucleosides and free purine and pyrimidine bases across the plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [P12236](https://www.uniprot.org/uniprotkb/P12236) (ADP/ATP translocase 3):

> ADP:ATP antiporter that mediates import of ADP into the mitochondrial matrix for ATP synthesis, and export of ATP out to fuel the cell (By similarity). Cycles between the cytoplasmic-open state (c-state) and the matrix-open state (m-state): operates by the alternating access mechanism with a single substrate-binding site intermittently exposed to either the cytosolic (c-state) or matrix (m-state) side of the inner mitochondrial membrane (By similarity). In addition to its ADP:ATP antiporter …

**Summary**, from NCBI Gene [293](https://www.ncbi.nlm.nih.gov/gene/293):

> This gene is a member of the mitochondrial carrier subfamily of solute carrier protein genes. The product of this gene functions as a gated pore that translocates ADP from the cytoplasm into the mitochondrial matrix and ATP from the mitochondrial matrix into the cytoplasm. The protein is implicated in the function of the permability transition pore complex (PTPC), which regulates the release of mitochondrial products that induce apoptosis. The human genome contains several non-transcribed …

**Accessions** — [HGNC:10992](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10992) · Entrez [293](https://www.ncbi.nlm.nih.gov/gene/293) · UniProt [P12236](https://www.uniprot.org/uniprotkb/P12236) · Ensembl [ENSG00000169100](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169100)

## Data

Gene col 9752: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9752); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9752, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9752]; `tensor/DDL_lfc|DDL_z.npy` [9752]; `embed/gene_vectors.npy` [9752]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9752 or target_col == 9752). Every well: [[SLC25A6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC25A6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
