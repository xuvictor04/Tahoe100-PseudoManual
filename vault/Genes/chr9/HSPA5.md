---
symbol: "HSPA5"
type: "gene"
col: 502
ensembl_id: "ENSG00000044574"
name: "heat shock protein family A (Hsp70) member 5"
location: "9q33.3"
module: 42
arm: "+"
pooled_cpm: 705.6
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 13
n_dd_up_clean: 14
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# HSPA5

*heat shock protein family A (Hsp70) member 5* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.35× (z +10.7, q 9e-24, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.430× (z -9.5, q 2e-18, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSP90B1]] (+0.88, fdr 7e-06), [[PDIA4]] (+0.84, fdr 7e-06), [[SEL1L]] (+0.82, fdr 7e-06); moves opposite to [[ZC3H7B]] (-0.67, fdr 7e-06), [[ST7L]] (-0.63, fdr 4e-05), [[ZNF462]] (-0.62, fdr 3e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF85]] → it (grade B ⚠); 1 goes from it, the strongest it → [[HYOU1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 502.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.35×** | +10.7 | 9e-24 | 48/48 (A549, J82, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.14×** | +10.1 | 2e-21 | 46/48 (A549, J82, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.83×** | +9.2 | 9e-18 | 44/48 (SW480, C-33 A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.78×** | +9.0 | 3e-17 | 45/48 (C-33 A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.41×** | +7.8 | 1e-12 | 47/48 (A549, J82, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.18×** | +6.9 | 5e-10 | 45/48 (C-33 A, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.17×** | +6.5 | 8e-09 | 43/48 (SNU-1, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +5.3 | 6e-06 | 42/48 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.20× | +5.1 | 2e-05 | 28/50 (A549, PANC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.97×** | +5.0 | 3e-05 | 38/45 (SNU-1, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.70×** | +4.7 | 2e-04 | 37/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +4.5 | 3e-04 | 30/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +4.5 | 4e-04 | 33/48 (J82, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.00×** | +4.3 | 6e-04 | 38/49 (LOX-IMVI, SNU-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.61×** | +4.2 | 9e-04 | 34/48 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Lipoic acid (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.024 | 30/48 (hTERT-HPNE, PANC-1, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.90×** | +2.9 | 0.095 | 25/48 (A-427, SNU-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 502.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.430×** | -9.5 | 2e-18 | 42/48 (NCI-H661, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.345×** | -9.1 | 4e-17 | 46/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.460×** | -6.9 | 1e-09 | 41/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.491×** | -6.3 | 4e-08 | 47/48 (NCI-H2347, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.631×** | -5.3 | 2e-05 | 40/48 (J82, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.619×** | -4.1 | 0.004 | 34/47 (A-172, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.638×** | -4.0 | 0.005 | 29/48 (A-172, NCI-H661, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.585×** | -3.8 | 0.012 | 33/48 (A-172, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.651×** | -3.5 | 0.027 | 34/47 (A-427, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.677×** | -3.5 | 0.030 | 37/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.735×** | -3.3 | 0.059 | 37/48 (C32, H4, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.697×** | -3.2 | 0.065 | 28/48 (HS-578T, H4, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.757×** | -3.1 | 0.089 | 25/48 (RKO, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 502. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 476 | 9 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 4.23× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -13.0) |
| [[A-172 (line)]] | wt | 1,452 | 4 | 5 | [[Panobinostat (drug)]] 0.5 µM 4.91× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.0878× (z -22.2) |
| [[C-33 A (line)]] | alt | 199 | 7 (1 ⚠) | 2 | [[Auranofin (drug)]] 5 µM 5.56× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -9.2) |
| [[A-427 (line)]] | wt | 287 | 4 (1 ⚠) | 4 | [[Ixazomib citrate (drug)]] 0.5 µM 3.44× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -17.0) |
| [[LOX-IMVI (line)]] | wt | 289 | 8 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.87× (z +12.6) | — |
| [[RPMI-7951 (line)]] | alt | 861 | 6 | 2 | [[Ixazomib citrate (drug)]] 5 µM 4.32× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -13.3) |
| [[SW480 (line)]] | alt | 294 | 8 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.49× (z +14.0) | — |
| [[J82 (line)]] | alt | 771 | 5 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 5.17× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 455 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.84× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 5.72× (z +9.3) | — |
| [[NCI-H2347 (line)]] | alt | 1,440 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -18.9) |
| [[NCI-H460 (line)]] | wt | 820 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 6.58× (z +10.8) | — |
| [[SNU-1 (line)]] | wt | 764 | 5 | 0 | [[Bortezomib (drug)]] 0.05 µM 6.32× (z +13.0) | — |
| [[PANC-1 (line)]] | alt | 419 | 1 | 3 | [[Panobinostat (drug)]] 0.5 µM 3.14× (z +9.5) | [[Harringtonine (drug)]] 0.5 µM 0.297× (z -10.1) |
| [[A498 (line)]] | wt | 834 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.99× (z +12.9) | — |
| [[A549 (line)]] | wt | 266 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.27× (z +13.7) | — |
| [[H4 (line)]] | wt | 1,753 | 1 | 2 | [[Ixazomib citrate (drug)]] 5 µM 4.47× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -15.5) |
| [[HCT15 (line)]] | alt | 871 | 2 | 1 | [[Ixazomib citrate (drug)]] 5 µM 6.94× (z +10.5) | [[Harringtonine (drug)]] 5 µM 0.149× (z -9.9) |
| [[HOP62 (line)]] | alt | 572 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.71× (z +10.8) | — |
| [[NCI-H661 (line)]] | alt | 929 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0594× (z -23.1) |
| [[AsPC-1 (line)]] | alt | 398 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.66× (z +10.5) | — |
| [[BT-474 (line)]] | alt | 572 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.86× (z +11.2) | — |
| [[Hs 766T (line)]] | wt | 509 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.22× (z +11.6) | — |
| [[HS-578T (line)]] | alt | 1,687 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -13.9) |
| [[KATO III (line)]] | alt | 1,531 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -14.8) |
| [[NCI-H1573 (line)]] | alt | 483 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.82× (z +11.5) | — |
| [[Panc 03.27 (line)]] | alt | 490 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.33× (z +11.3) | — |
| [[RKO (line)]] | wt | 1,103 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -20.5) |
| [[SNU-423 (line)]] | alt | 343 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.77× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 820 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.40× (z +9.7) | — |
| [[SW48 (line)]] | wt | 1,100 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.106× (z -10.8) |
| [[AN3 CA (line)]] | alt | 340 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.24× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 721 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -8.5) |
| [[CHP-212 (line)]] | wt | 452 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 425 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.04× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 681 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.78× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 881 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.04× (z +8.9) | — |
| [[LoVo (line)]] | wt | 624 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.58× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 1,119 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.158× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 699 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.90× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 640 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -11.5) |
| [[C32 (line)]] | wt | 641 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 737 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 590 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 803 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 644 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 696 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 613 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1,348 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 370 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 461 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 502), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSP90B1]] | +0.88 | +0.87 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 999 |
| [[PDIA4]] | +0.84 | +0.84 / +0.82 | both halves | 7e-06 | STRING 990 |
| [[SEL1L]] | +0.82 | +0.83 / +0.78 | both halves | 7e-06 | STRING 949 |
| [[P4HB]] | +0.78 | +0.79 / +0.70 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication; STRING 996 |
| [[TMED9]] | +0.78 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[DNAJC3]] | +0.78 | +0.78 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 978 |
| [[CALR]] | +0.77 | +0.78 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 995 |
| [[GFPT1]] | +0.77 | +0.72 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[HERPUD1]] | +0.75 | +0.72 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 792 |
| [[LMAN1]] | +0.75 | +0.76 / +0.68 | both halves | 7e-06 | STRING 588 |
| [[COPA]] | +0.75 | +0.80 / +0.66 | both halves | 7e-06 |  |
| [[MANF]] | +0.74 | +0.71 / +0.74 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation; STRING 996 |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H7B]] | -0.67 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[ST7L]] | -0.63 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[ZNF462]] | -0.62 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[POGLUT1]] | -0.62 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[ZNF764]] | -0.61 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[ZNF620]] | -0.61 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[AASDHPPT]] | -0.60 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[NHLRC2]] | -0.60 | -0.56 / -0.60 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation |
| [[ITPA]] | -0.60 | -0.51 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF85]] | B | ZNF85 activity raises HSPA5's level | lines that do not express ZNF85 (17) vs lines expressing it (33) | 1.51× lower at baseline in the lines without ZNF85 | 0.052 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF66, ZNF726 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HYOU1]] | C | HSPA5's natural level weakens HYOU1's drug response | HSPA5's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse -0.23; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.794). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.8, -30.9); signed map (-53.9, 7.6). **Vector** length 160, 65.0% of its response variance represented; |z| ≥ 3 in 1,486 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cargo concentration in the ER* (reactome, mean cos +0.52 to 7); *N-glycan trimming in the ER and Calnexin/Calreticulin cycle* (reactome, mean cos +0.55 to 7); *Calnexin/calreticulin cycle* (reactome, mean cos +0.55 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +10.8 | +10.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +10.8 | +10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.5 | +9.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +9.1 | +5.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.9 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +6.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.6 | +2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.6 | +4.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -16.6 | -9.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -11.9 | -6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -11.0 | -9.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.5 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.6 | -3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.9 | -3.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.2 | -2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.1 | -1.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.7 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein family A (Hsp70) member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:125,234,853-125,241,382 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BiP; previously GRP78 |
| Gene groups (HGNC) | Heat shock 70kDa proteins |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, COMPLEMENT, GLYCOLYSIS, HYPOXIA, MTORC1_SIGNALING |
| Reactome | 27 pathways, smallest: ATF6B (ATF6-beta) activates chaperones; ATF6 (ATF6-alpha) activates chaperone genes; ATF6 (ATF6-alpha) activates chaperones |
| Matched by | ensembl_id |

**Function**, from UniProt [P11021](https://www.uniprot.org/uniprotkb/P11021) (Endoplasmic reticulum chaperone BiP):

> Endoplasmic reticulum chaperone that plays a key role in protein folding and quality control in the endoplasmic reticulum lumen. Involved in the correct folding of proteins and degradation of misfolded proteins via its interaction with DNAJC10/ERdj5, probably to facilitate the release of DNAJC10/ERdj5 from its substrate (By similarity). Acts as a key repressor of the EIF2AK3/PERK and ERN1/IRE1-mediated unfolded protein response (UPR). In the unstressed endoplasmic reticulum, recruited by …

**Summary**, from NCBI Gene [3309](https://www.ncbi.nlm.nih.gov/gene/3309):

> The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interacts with the transmembrane stress sensor proteins PERK (protein kinase R-like endoplasmic reticulum …

**Accessions** — [HGNC:5238](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5238) · Entrez [3309](https://www.ncbi.nlm.nih.gov/gene/3309) · UniProt [P11021](https://www.uniprot.org/uniprotkb/P11021) · Ensembl [ENSG00000044574](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000044574)

## Data

Gene col 502: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 502); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 502, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 502]; `tensor/DDL_lfc|DDL_z.npy` [502]; `embed/gene_vectors.npy` [502]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 502 or target_col == 502). Every well: [[HSPA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSPA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
