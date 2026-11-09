---
symbol: "PBX3"
type: "gene"
col: 9410
ensembl_id: "ENSG00000167081"
name: "PBX homeobox 3"
location: "9q33.3"
module: 71
arm: "+"
pooled_cpm: 163.05
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 18
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# PBX3

*PBX homeobox 3* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.54× (z +10.3, q 5e-22, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.262× (z -11.8, q 2e-29, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NSD2]] (+0.61, fdr 7e-06), [[CBFB]] (+0.60, fdr 1e-05), [[FANCC]] (+0.58, fdr 1e-05); moves opposite to [[PPP1R3C]] (-0.53, fdr 4e-05), [[ABHD4]] (-0.51, fdr 1e-05), [[RASSF4]] (-0.51, fdr 5e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RGMB]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9410.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +10.3 | 5e-22 | 30/47 (LoVo, HT-29, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +9.6 | 2e-19 | 35/46 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.1 | 6e-05 | 29/46 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.34×** | +4.8 | 2e-04 | 25/48 (SW480, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +4.6 | 4e-04 | 26/46 (LoVo, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.095 | 20/46 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9410.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.262×** | -11.8 | 2e-29 | 44/47 (RKO, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.484×** | -11.7 | 2e-29 | 35/46 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.335×** | -9.6 | 1e-19 | 37/46 (LOX-IMVI, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.585×** | -7.9 | 4e-13 | 34/46 (LOX-IMVI, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.681×** | -6.5 | 1e-08 | 40/46 (LOX-IMVI, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.670×** | -6.4 | 2e-08 | 34/46 (A-172, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.698×** | -6.0 | 1e-07 | 25/46 (A-172, A549, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.718×** | -5.1 | 2e-05 | 28/43 (LOX-IMVI, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.763×** | -4.6 | 3e-04 | 24/46 (LOX-IMVI, A-427, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.769×** | -4.4 | 6e-04 | 28/46 (LOX-IMVI, COLO 205, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.832×** | -4.4 | 6e-04 | 22/46 (A-172, A549, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **0.772×** | -4.3 | 7e-04 | 27/46 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.781×** | -4.0 | 0.003 | 23/45 (NCI-H23, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.654×** | -3.7 | 0.007 | 19/37 (NCI-H2030, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.806×** | -3.6 | 0.011 | 23/46 (SHP-77, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9410. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 915 | 0 | 20 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.103× (z -22.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.235× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 1,173 | 0 | 18 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -20.9) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.135× (z -15.8) |
| [[A-172 (line)]] | wt | 511 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -24.8) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.204× (z -13.5) |
| [[J82 (line)]] | alt | 318 | 0 | 7 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.226× (z -15.4) |
| [[A-427 (line)]] | wt | 129 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.267× (z -14.0) |
| [[A498 (line)]] | wt | 153 | 2 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +14.0) | [[Harringtonine (drug)]] 5 µM 0.255× (z -17.4) |
| [[NCI-H23 (line)]] | alt | 155 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.340× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 94.4 | 3 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +16.5) | [[Harringtonine (drug)]] 5 µM 0.325× (z -10.1) |
| [[A549 (line)]] | wt | 118 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -21.8) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.179× (z -16.9) |
| [[HEC-1-A (line)]] | alt | 120 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -13.7) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.249× (z -13.2) |
| [[LoVo (line)]] | wt | 70.0 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.61× (z +23.0) | — |
| [[SHP-77 (line)]] | alt | 357 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.383× (z -11.6) |
| [[HS-578T (line)]] | alt | 96.0 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.241× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 93.9 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.266× (z -11.7) |
| [[SNU-1 (line)]] | wt | 149 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +9.5) ⚠ cell-cycle shift, explains ~93% of this change | [[PH-797804 (drug)]] 5 µM 0.0856× (z -10.2) |
| [[SW1417 (line)]] | alt | 98.1 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +12.3) | — |
| [[SW480 (line)]] | alt | 58.5 | 4 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.00× (z +14.0) | — |
| [[AN3 CA (line)]] | alt | 266 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.310× (z -8.8) |
| [[C-33 A (line)]] | alt | 219 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.205× (z -8.5) |
| [[COLO 205 (line)]] | alt | 114 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.5) | [[Auranofin (drug)]] 5 µM 0.314× (z -10.0) |
| [[HOP62 (line)]] | alt | 192 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.299× (z -12.1) |
| [[HT-29 (line)]] | alt | 61.9 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +19.3) | — |
| [[Panc 03.27 (line)]] | alt | 91.0 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +15.5) | [[PH-797804 (drug)]] 5 µM 0.228× (z -8.7) |
| [[PANC-1 (line)]] | alt | 167 | 0 | 3 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.248× (z -10.4) |
| [[BT-474 (line)]] | alt | 134 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -11.1) ⚠ cell-cycle shift, explains ~93% of this change |
| [[SNU-423 (line)]] | alt | 176 | 1 | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.0) | [[TAK-901 (drug)]] 5 µM 0.221× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 45.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +10.5) | — |
| [[H4 (line)]] | wt | 88.0 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 44.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.73× (z +13.7) | — |
| [[Hs 766T (line)]] | wt | 69.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +13.9) | — |
| [[hTERT-HPNE (line)]] | wt | 168 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.143× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 67.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +11.8) | — |
| [[RPMI-7951 (line)]] | alt | 97.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 161 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0877× (z -21.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 96.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.358× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 102 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.4 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 38.5 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 453 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 457 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 72.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9410), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSD2]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[CBFB]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[FANCC]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SATB2]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[SCHIP1]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[SNRPB]] | +0.56 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[GBX2-AS1]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[NHSL1]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[FARP1]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[DOCK1]] | +0.55 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[SLC4A7]] | +0.55 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[KIAA1549L]] | +0.54 | +0.46 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R3C]] | -0.53 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[ABHD4]] | -0.51 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[RASSF4]] | -0.51 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[THAP8]] | -0.51 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[ZNF205]] | -0.50 | -0.49 / -0.40 | both halves | 4e-05 |  |
| [[GOLPH3L]] | -0.49 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[ASB8]] | -0.49 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[TBC1D17]] | -0.48 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[PICK1]] | -0.48 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[MVP]] | -0.48 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[ALDH3B1]] | -0.48 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[NFKBIL1]] | -0.48 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PBX3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 1.7% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ALDH3B1]] | B | ALDH3B1 activity lowers PBX3's level | lines that do not express ALDH3B1 (9) vs lines expressing it (41) | 2.89× higher at baseline in the lines without ALDH3B1 | 0.008 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[ALDH3B1]] | B | ALDH3B1 activity weakens PBX3's drug response | lines that do not express ALDH3B1 (9) vs lines expressing it (38) | the lines without ALDH3B1 respond 0.89× as strongly (z diff -0.02); strongest at Ixazomib citrate 5 µM: 0.57x vs 0.69x (z diff -2.6) | 0.080 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers PBX3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers PBX3's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[NOD2]] | B | NOD2 activity lowers PBX3's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 1.76× higher at baseline in the lines without NOD2 | 0.096 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[CENPP]] | C | CENPP activity raises PBX3's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.48× lower at baseline in the lines without CENPP | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGMB]] | C | PBX3's natural level weakens RGMB's drug response | PBX3's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.67, reverse +0.08; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.432). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.8, -38.2); signed map (-20.3, 47.7). **Vector** length 131, 42.3% of its response variance represented; |z| ≥ 3 in 1,425 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +10.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +9.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.6 | +0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.5 | +2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +5.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.3 | +2.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.3 | +2.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -7.0 | -11.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.8 | -9.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -7.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.2 | -11.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.4 | -6.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.7 | -1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.3 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | PBX homeobox 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:125,747,345-125,967,377 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | TALE class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [P40426](https://www.uniprot.org/uniprotkb/P40426) (Pre-B-cell leukemia transcription factor 3):

> Transcriptional activator that binds the sequence 5'-ATCAATCAA-3'.

**Summary**, from NCBI Gene [5090](https://www.ncbi.nlm.nih.gov/gene/5090):

> Predicted to enable DNA-binding transcription activator activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in several processes, including eye development; nervous system development; and positive regulation of transcription by RNA polymerase II. Predicted to act upstream of or within several processes, including adult locomotory behavior; dorsal spinal cord development; and regulation of respiratory …

**Accessions** — [HGNC:8634](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8634) · Entrez [5090](https://www.ncbi.nlm.nih.gov/gene/5090) · UniProt [P40426](https://www.uniprot.org/uniprotkb/P40426) · Ensembl [ENSG00000167081](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167081)

## Data

Gene col 9410: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9410); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9410, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9410]; `tensor/DDL_lfc|DDL_z.npy` [9410]; `embed/gene_vectors.npy` [9410]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9410 or target_col == 9410). Every well: [[PBX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PBX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
