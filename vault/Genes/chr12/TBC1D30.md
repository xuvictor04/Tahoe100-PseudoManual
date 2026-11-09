---
symbol: "TBC1D30"
type: "gene"
col: 3237
ensembl_id: "ENSG00000111490"
name: "TBC1 domain family member 30"
location: "12q14.3"
module: 18
arm: "+"
pooled_cpm: 16.06
n_lines_expressing: 42
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# TBC1D30

*TBC1 domain family member 30* — 12q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.33× (z +37.4, q 0e+00, up in 34 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM: 0.805× (z -3.9, q 0.062, down in 9 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SW1417 0.0737×, A-427 0.156×, LoVo 0.198×, NCI-H1573 0.167×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.108×, RKO 0.0825×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW48 0.101×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0520×); [[Pimozide (drug)]] 0.05 µM in 1 line (AsPC-1 0.0762×).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KTN1-AS1]] (+0.58, fdr 1e-05), [[ADCY3]] (+0.57, fdr 1e-05), [[UCK2]] (+0.56, fdr 1e-05); moves opposite to [[POLR2E]] (-0.50, fdr 4e-04), [[SNAP29]] (-0.47, fdr 8e-04, ⚠ not reproduced), [[SERINC3]] (-0.47, fdr 2e-05), [[HIF1AN]] (-0.46, fdr 2e-04).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[COBLL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3237.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.33×** | +37.4 | 0e+00 | 34/36 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +12.2 | 9e-32 | 22/36 (SW480, SNU-423, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +8.6 | 2e-15 | 20/31 (NCI-H1792, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +7.4 | 2e-11 | 11/35 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +6.5 | 1e-08 | 16/40 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +6.4 | 2e-08 | 10/39 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +5.6 | 2e-06 | 16/28 (A-427, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +5.1 | 2e-05 | 12/38 (NCI-H1573, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +5.1 | 3e-05 | 19/39 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.0 | 3e-05 | 10/40 (A-172, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +4.9 | 4e-05 | 16/39 (NCI-H1792, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +4.9 | 5e-05 | 13/36 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.29×** | +4.7 | 1e-04 | 15/39 (SW 900, NCI-H1573, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +4.5 | 3e-04 | 12/32 (BT-474, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.58×** | +4.3 | 6e-04 | 10/38 (NCI-H1792, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 0.001 | 17/37 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.51×** | +3.9 | 0.003 | 6/35 (NCI-H460, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +3.8 | 0.005 | 8/36 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.013 | 5/38 (PANC-1, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.20×** | +3.4 | 0.021 | 14/35 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3237.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SW1417 0.0737×, A-427 0.156×, LoVo 0.198×, NCI-H1573 0.167×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.108×, RKO 0.0825×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW48 0.101×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0520×); [[Pimozide (drug)]] 0.05 µM in 1 line (AsPC-1 0.0762×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.805×** | -3.9 | 0.062 | 9/39 (NCI-H1573, SW 900, …) | inconsistent across doses |  |
| [[OTS514 (drug)]] 5 µM |  | 0.688× | -3.5 | 0.13 | 7/31 (SHP-77, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 0.788× | -3.0 | 0.45 | 10/31 (CFPAC-1, SW1417, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3237. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 62.3 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.307× (z -10.7) |
| [[A-427 (line)]] | wt | 50.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -20.4) |
| [[LOX-IMVI (line)]] | wt | 5.25 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.22× (z +11.2) | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0520× (z -11.8) |
| [[SW480 (line)]] | alt | 17.7 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 7.40 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.34× (z +12.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0812× (z -11.1) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 11.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.54× (z +10.8) | — |
| [[NCI-H2347 (line)]] | alt | 13.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +9.5) | — |
| [[RKO (line)]] | wt | 14.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +8.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.0825× (z -12.7) |
| [[SW1417 (line)]] | alt | 20.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.0737× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 4.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.05× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 7.37 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0762× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 7.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.08× (z +12.7) | — |
| [[COLO 205 (line)]] | alt | 15.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 17.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +14.4) | — |
| [[HepG2_C3A (line)]] | wt | 8.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +8.9) | — |
| [[LoVo (line)]] | wt | 49.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 39.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 8.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.21× (z +17.3) | — |
| [[PANC-1 (line)]] | alt | 13.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.57× (z +17.8) | — |
| [[SNU-423 (line)]] | alt | 4.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +12.1) | — |
| [[SW 900 (line)]] | alt | 8.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.84× (z +11.2) | — |
| [[A498 (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.08 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3237), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KTN1-AS1]] | +0.58 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[ADCY3]] | +0.57 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[UCK2]] | +0.56 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[STARD7-AS1]] | +0.54 | +0.51 / +0.33 | both halves | 1e-04 |  |
| [[NSMAF]] | +0.54 | +0.49 / +0.30 | both halves | 2e-04 |  |
| [[BEND3]] | +0.54 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[TDRD3]] | +0.54 | +0.38 / +0.41 | both halves | 7e-05 |  |
| [[WDR12]] | +0.54 | +0.57 / +0.39 | both halves | 6e-05 |  |
| [[CCNJ]] | +0.53 | +0.46 / +0.32 | both halves | 2e-04 |  |
| [[POU6F1]] | +0.53 | +0.45 / +0.28 | both halves | 3e-04 |  |
| [[GPR63]] | +0.53 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[KLHL42]] | +0.53 | +0.50 / +0.24 | both halves | 5e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2E]] | -0.50 | -0.33 / -0.24 | both halves | 4e-04 |  |
| [[SNAP29]] | -0.47 | -0.32 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[SERINC3]] | -0.47 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[HIF1AN]] | -0.46 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[TMEM92]] | -0.46 | -0.49 / -0.20 | both halves | 7e-04 |  |
| [[IK]] | -0.45 | -0.29 / -0.34 | both halves | 3e-04 |  |
| [[SPAG9]] | -0.45 | -0.38 / -0.27 | both halves | 3e-04 |  |
| [[DDAH2]] | -0.44 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[DCTN3]] | -0.44 | -0.43 / -0.23 | both halves | 5e-04 |  |
| [[DHRS2]] | -0.44 | -0.40 / -0.11 | ⚠ not reproduced | 0.002 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[MKNK1]] | -0.44 | -0.34 / -0.20 | both halves | 7e-04 |  |
| [[NBEAL1]] | -0.44 | -0.38 / -0.25 | both halves | 4e-04 |  |
| [[C8orf82]] | -0.43 | -0.37 / -0.28 | both halves | 3e-04 |  |
| [[DHX40]] | -0.43 | -0.31 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TBC1D30's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COBLL1]] | B | TBC1D30 activity raises COBLL1's level | lines that do not express TBC1D30 (8) vs lines expressing it (42) | 1.68× lower at baseline in the lines without TBC1D30 | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000288591, RAB3IP; maybe low, not absent |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.540). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.9, -37.2); signed map (1.4, -57.4). **Vector** length 79.5, 16.2% of its response variance represented; |z| ≥ 3 in 865 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +37.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +8.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +6.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.1 | +5.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +3.9 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +3.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -3.7 | +2.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -2.7 | +4.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.7 | +4.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | +3.5 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.3 | -1.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 30 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.3 — chr12:64,759,484-64,881,033 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0984 |
| Gene groups (HGNC) | TBC1 domain family members |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2I9](https://www.uniprot.org/uniprotkb/Q9Y2I9) (TBC1 domain family member 30):

> May act as a GTPase-activating protein for Rab family protein(s).

**Summary**, from NCBI Gene [23329](https://www.ncbi.nlm.nih.gov/gene/23329):

> Enables GTPase activator activity and small GTPase binding activity. Involved in negative regulation of cilium assembly and positive regulation of GTPase activity. Located in ciliary basal body and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29164](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29164) · Entrez [23329](https://www.ncbi.nlm.nih.gov/gene/23329) · UniProt [Q9Y2I9](https://www.uniprot.org/uniprotkb/Q9Y2I9) · Ensembl [ENSG00000111490](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111490)

## Data

Gene col 3237: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3237); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3237, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3237]; `tensor/DDL_lfc|DDL_z.npy` [3237]; `embed/gene_vectors.npy` [3237]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3237 or target_col == 3237). Every well: [[TBC1D30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
