---
symbol: "CARNMT1"
type: "gene"
col: 7940
ensembl_id: "ENSG00000156017"
name: "carnosine N-methyltransferase 1"
location: "9q21.13"
module: 18
arm: "+"
pooled_cpm: 48.03
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 10
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# CARNMT1

*carnosine N-methyltransferase 1* — 9q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.59× (z +11.3, q 7e-27, up in 30 of 48 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H1792 6.63×, HT-29 2.81×, NCI-H460 2.09×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1792 5.42×, Hs 766T 2.82×; ⚠ toxic; transcription drop); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 2.27×; ⚠ unreliable plate only).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.605× (z -17.3, q 0e+00, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAP1]] (+0.77, fdr 7e-06), [[CAD]] (+0.71, fdr 7e-06), [[SEH1L]] (+0.70, fdr 7e-06); moves opposite to [[SYNRG]] (-0.57, fdr 1e-05), [[ZNF446]] (-0.57, fdr 2e-05), [[IST1]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[DUXAP8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 8 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7940.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H1792 6.63×, HT-29 2.81×, NCI-H460 2.09×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1792 5.42×, Hs 766T 2.82×; ⚠ toxic; transcription drop); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 2.27×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +11.3 | 7e-27 | 30/48 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +10.7 | 3e-24 | 30/40 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +8.2 | 6e-14 | 35/48 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +6.8 | 1e-09 | 27/45 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.24×** | +5.4 | 1e-05 | 22/48 (LOX-IMVI, A549, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.19× | +4.2 | 0.003 | 19/48 (SNU-423, NCI-H2347, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | 1.17× | +3.8 | 0.013 | 18/47 (CFPAC-1, NCI-H23, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.16× | +3.7 | 0.014 | 18/48 (J82, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠; shown: the 15 strongest. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7940.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.605×** | -17.3 | 0e+00 | 37/48 (SNU-423, RKO, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.598×** | -12.5 | 1e-33 | 31/48 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.638×** | -10.9 | 1e-25 | 32/47 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.449×** | -10.2 | 3e-22 | 39/49 (RKO, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.751×** | -9.8 | 1e-20 | 31/48 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.913× | -7.6 | 3e-12 | 5/49 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.752×** | -6.9 | 4e-10 | 25/48 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.770×** | -6.3 | 2e-08 | 26/48 (SW48, LS 180, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.792×** | -5.6 | 1e-06 | 27/48 (SW48, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.644×** | -5.6 | 1e-06 | 22/48 (MIA PaCa-2, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.873× | -4.7 | 2e-04 | 16/48 (A-427, SNU-423, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.831×** | -4.5 | 4e-04 | 22/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.856× | -3.8 | 0.007 | 22/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.874× | -3.1 | 0.072 | 11/47 (CHP-212, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.881× | -3.1 | 0.079 | 18/48 (LoVo, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7940. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 77.5 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -16.7) |
| [[NCI-H460 (line)]] | wt | 59.6 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.09× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -16.0) |
| [[SW480 (line)]] | alt | 68.3 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.395× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -12.5) |
| [[MIA PaCa-2 (line)]] | alt | 59.2 | 1 (1 ⚠) | 3 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.27× (z +8.8) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 0.5 µM 0.221× (z -16.3) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.349× (z -16.1) |
| [[PANC-1 (line)]] | alt | 53.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -15.4) |
| [[HOP62 (line)]] | alt | 30.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -10.3) |
| [[A-427 (line)]] | wt | 44.3 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.441× (z -11.9) |
| [[AN3 CA (line)]] | alt | 58.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -12.2) |
| [[Hs 766T (line)]] | wt | 55.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -9.0) |
| [[KATO III (line)]] | alt | 59.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.287× (z -13.4) |
| [[LS 180 (line)]] | wt | 74.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.441× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.492× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 28.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.272× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 34.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.63× (z +15.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 48.1 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 43.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -18.1) |
| [[SW48 (line)]] | wt | 88.3 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.236× (z -12.1) |
| [[A498 (line)]] | wt | 53.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -11.1) |
| [[A549 (line)]] | wt | 43.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -9.0) |
| [[C-33 A (line)]] | alt | 98.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -18.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 52.2 | 0 | 1 (1 ⚠) | — | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0782× (z -9.8) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 87.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.590× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 38.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.308× (z -8.6) |
| [[HS-578T (line)]] | alt | 30.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -9.1) |
| [[HT-29 (line)]] | alt | 40.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.81× (z +9.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 55.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -12.9) |
| [[LoVo (line)]] | wt | 61.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.598× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 58.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -14.6) |
| [[NCI-H2030 (line)]] | alt | 26.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 38.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -13.4) |
| [[A-172 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 64.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 56.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7940), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAP1]] | +0.77 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[CAD]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[SEH1L]] | +0.70 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[DKC1]] | +0.69 | +0.76 / +0.56 | both halves | 1e-05 |  |
| [[MDN1]] | +0.68 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[MTG1]] | +0.67 | +0.42 / +0.73 | both halves | 4e-05 |  |
| [[FXN]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[ADAT2]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[ATIC]] | +0.65 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[RIOX2]] | +0.64 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[ANKS6]] | +0.64 | +0.70 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYNRG]] | -0.57 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ZNF446]] | -0.57 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[IST1]] | -0.55 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[TMUB2]] | -0.55 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[KBTBD4]] | -0.54 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[ARID4B]] | -0.54 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[KDM5A]] | -0.53 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[SMIM27]] | -0.53 | -0.33 / -0.54 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUXAP8]] | B | DUXAP8 activity raises CARNMT1's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.54× lower at baseline in the lines without DUXAP8 | 0.011 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |
| [[DUXAP9]] | B | DUXAP9 activity raises CARNMT1's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 1.41× lower at baseline in the lines without DUXAP9 | 0.016 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent |
| [[MCOLN2]] | B | MCOLN2 activity raises CARNMT1's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.15× lower at baseline in the lines without MCOLN2 | 0.048 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.694). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.8, -37.3); signed map (-4.7, -51.4). **Vector** length 104, 24.7% of its response variance represented; |z| ≥ 3 in 957 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.58 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.0 | +8.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.7 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.4 | +5.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +2.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | +1.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.2 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.8 | -9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.6 | -17.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.4 | -4.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.9 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.2 | -2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | carnosine N-methyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.13 — chr9:74,980,790-75,028,423 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25795; previously C9orf41 |
| Gene groups (HGNC) | 7BS protein methyltransferases; 7BS small molecule methyltransferases; 7BS protein histidine methyltransferases; Histidine methyltransferases; Small molecule methyltransferases |
| Reactome | 2 pathways, smallest: Histidine catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4J0](https://www.uniprot.org/uniprotkb/Q8N4J0) (Protein-L-histidine N-pros-methyltransferase CARNMT1):

> Protein-histidine N-methyltransferase that specifically catalyzes the N1-methylation (pros-methylation) of histidine residues in a wide range of proteins. It primarily monomethylates proteins containing RNA-binding C3H1 zinc finger motifs, such as U2AF1, ZC3H15, ZC3H18, PPP1R10, PRR3 and RNF113A, thereby modulating mRNA splicing and turnover. Additionally, methylates the dipeptide carnosine (beta-alanyl-L-histidine) at the N1 position to generate anserine, an abundant component of vertebrate …

**Summary**, from NCBI Gene [138199](https://www.ncbi.nlm.nih.gov/gene/138199):

> The protein encoded by this gene is a methyltransferase that converts carnosine to anserine, a dipeptide found abundantly in skeletal muscle. The encoded protein can methylate other dipeptides as well. Three transcript variants encoding two different isoforms have been found for this gene. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:23435](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23435) · Entrez [138199](https://www.ncbi.nlm.nih.gov/gene/138199) · UniProt [Q8N4J0](https://www.uniprot.org/uniprotkb/Q8N4J0) · Ensembl [ENSG00000156017](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156017)

## Data

Gene col 7940: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7940); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7940, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7940]; `tensor/DDL_lfc|DDL_z.npy` [7940]; `embed/gene_vectors.npy` [7940]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7940 or target_col == 7940). Every well: [[CARNMT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CARNMT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
