---
symbol: "KHDC4"
type: "gene"
col: 5359
ensembl_id: "ENSG00000132680"
name: "KH domain containing 4, pre-mRNA splicing factor"
location: "1q22"
module: 179
arm: "+"
pooled_cpm: 131.83
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/179"]
generated_by: "tahoemap"
---

# KHDC4

*KH domain containing 4, pre-mRNA splicing factor* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.07× (z +8.7, q 2e-15, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.491× (z -10.2, q 1e-21, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.749× (z -4.1, q 0.006, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM39A]] (+0.75, fdr 7e-06), [[DPM1]] (+0.72, fdr 7e-06), [[COPA]] (+0.68, fdr 1e-05); moves opposite to [[ROCK2]] (-0.62, fdr 1e-05), [[EEA1]] (-0.62, fdr 7e-06), [[SLK]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 179]] (RHOA GTPase cycle).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5359.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.07×** | +8.7 | 2e-15 | 48/49 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +7.2 | 2e-10 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +7.0 | 5e-10 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +6.9 | 7e-10 | 40/48 (SW480, SHP-77, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.40×** | +6.8 | 1e-09 | 39/48 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.56×** | +6.6 | 5e-09 | 39/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.4 | 9e-04 | 32/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **1.32×** | +4.0 | 0.005 | 27/47 (NCI-H460, SW 900, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.30×** | +3.9 | 0.005 | 29/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.007 | 26/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.26×** | +3.4 | 0.030 | 26/48 (RKO, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.24×** | +3.2 | 0.070 | 29/48 (LS 180, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5359.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.491×** | -10.2 | 1e-21 | 39/44 (A498, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.559×** | -8.7 | 1e-15 | 43/49 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.749×** | -4.1 | 0.006 | 25/48 (CFPAC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.754×** | -4.0 | 0.007 | 31/48 (NCI-H2347, RPMI-7951, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.799×** | -3.3 | 0.092 | 23/48 (SW 900, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.733×** | -3.3 | 0.092 | 24/48 (A-172, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5359. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 258 | 3 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.77× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 131 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.39× (z +12.8) | — |
| [[SW480 (line)]] | alt | 123 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.481× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 168 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.457× (z -8.7) |
| [[KATO III (line)]] | alt | 76.2 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +9.6) | — |
| [[LoVo (line)]] | wt | 121 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.59× (z +10.5) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 2.32× (z +9.6) | — |
| [[A-427 (line)]] | wt | 146 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.420× (z -10.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 202 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -13.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 147 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.74× (z +9.5) ⚠ toxic | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -9.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 148 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -8.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 93.5 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.09× (z +9.8) | — |
| [[LS 180 (line)]] | wt | 116 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +9.7) | — |
| [[RKO (line)]] | wt | 94.5 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.74× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 227 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.21× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.422× (z -10.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 107 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.38× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 113 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.66× (z +8.7) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.352× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.455× (z -9.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.347× (z -9.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 177 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -13.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 168 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -10.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 99.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -8.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -9.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 99.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 288 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -9.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 98.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.34× (z +8.7) | — |
| [[SW48 (line)]] | wt | 121 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +8.8) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[AN3 CA (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 123 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 71.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 69.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 131 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 96.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 114 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5359), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM39A]] | +0.75 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[DPM1]] | +0.72 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[COPA]] | +0.68 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[ECD]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[USPL1]] | +0.66 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[MED26]] | +0.65 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[SNHG21]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[TBC1D22A-DT]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[GPR107]] | +0.63 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[ZFC3H1]] | +0.63 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[PMPCA]] | +0.62 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[QPCTL]] | +0.62 | +0.63 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ROCK2]] | -0.62 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[EEA1]] | -0.62 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[SLK]] | -0.58 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[THOC7]] | -0.58 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[DST]] | -0.56 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[LIG4]] | -0.55 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[CUX1]] | -0.55 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.55 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[RABEP1]] | -0.54 | -0.57 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 179]] — RHOA GTPase cycle; 22 genes; this gene is in the **+** arm (projection on the module's main direction 0.809). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (5.3, -20.3); signed map (-44.1, 11.6). **Vector** length 104, 34.1% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.0 | +6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | +5.9 | +4.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +1.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.5 | +2.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.1 | +1.6 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.8 | +0.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.9 | -4.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.9 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.0 | +1.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.0 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | KH domain containing 4, pre-mRNA splicing factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:155,913,045-155,934,413 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BLOM7, SNORA80EHG; previously KIAA0907 |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z7F0](https://www.uniprot.org/uniprotkb/Q7Z7F0) (KH homology domain-containing protein 4):

> RNA-binding protein involved in pre-mRNA splicing. Interacts with the PRP19C/Prp19 complex/NTC/Nineteen complex which is part of the spliceosome. Involved in regulating splice site selection. Binds preferentially RNA with A/C rich sequences and poly-C stretches.

**Summary**, from NCBI Gene [22889](https://www.ncbi.nlm.nih.gov/gene/22889):

> Enables RNA binding activity. Involved in mRNA splice site recognition. Located in cytoplasm; nucleoplasm; and spliceosomal complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29145](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29145) · Entrez [22889](https://www.ncbi.nlm.nih.gov/gene/22889) · UniProt [Q7Z7F0](https://www.uniprot.org/uniprotkb/Q7Z7F0) · Ensembl [ENSG00000132680](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132680)

## Data

Gene col 5359: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5359); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5359, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5359]; `tensor/DDL_lfc|DDL_z.npy` [5359]; `embed/gene_vectors.npy` [5359]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5359 or target_col == 5359). Every well: [[KHDC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KHDC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
