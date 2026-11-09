---
symbol: "MAP3K7CL"
type: "gene"
col: 7965
ensembl_id: "ENSG00000156265"
name: "MAP3K7 C-terminal like"
location: "21q21.3"
module: 26
arm: "+"
pooled_cpm: 8.07
n_lines_expressing: 38
n_dd_up: 14
n_dd_down: 20
n_dd_up_clean: 10
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# MAP3K7CL

*MAP3K7 C-terminal like* — 21q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.66× (z +17.7, q 0e+00, up in 26 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.540× (z -7.9, q 1e-12, down in 21 of 35 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.681× (z -4.9, q 5e-05, down in 16 of 35 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HDAC2-AS2]] (+0.74, fdr 7e-06), [[FBXO38-DT]] (+0.74, fdr 1e-05), [[SYT16]] (+0.70, fdr 1e-05); moves opposite to [[CLTCL1]] (-0.55, fdr 1e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7965.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.66×** | +17.7 | 0e+00 | 26/32 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +10.3 | 3e-22 | 21/35 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +9.3 | 2e-18 | 5/16 (SNU-423, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +7.5 | 1e-11 | 16/36 (HOP62, A498, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +7.1 | 1e-10 | 16/35 (HEC-1-A, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +6.5 | 8e-09 | 4/11 (A498, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +6.2 | 4e-08 | 11/32 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +5.3 | 7e-06 | 12/35 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.7 | 1e-04 | 10/32 (HEC-1-A, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.26×** | +4.1 | 0.002 | 9/36 (NCI-H1573, A498, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.005 | 13/35 (A549, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.35×** | +3.8 | 0.007 | 9/35 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.025 | 10/34 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.068 | 6/35 (SW480, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7965.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.540×** | -7.9 | 1e-12 | 21/35 (LOX-IMVI, H4, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.550×** | -7.7 | 4e-12 | 21/33 (LOX-IMVI, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.566×** | -7.3 | 4e-11 | 21/35 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.609×** | -6.4 | 2e-08 | 20/35 (LOX-IMVI, A-427, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.619×** | -6.2 | 7e-08 | 15/35 (LOX-IMVI, SK-MEL-2, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.645×** | -5.7 | 2e-06 | 11/35 (LOX-IMVI, SK-MEL-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.656×** | -5.4 | 5e-06 | 17/35 (LOX-IMVI, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.681×** | -4.9 | 5e-05 | 16/35 (LOX-IMVI, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.496×** | -4.7 | 2e-04 | 9/31 (SHP-77, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.558×** | -3.9 | 0.005 | 9/33 (LOX-IMVI, hTERT-HPNE, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.743×** | -3.8 | 0.006 | 13/36 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.744×** | -3.8 | 0.006 | 12/35 (LOX-IMVI, SW480, …) | two highest doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.583×** | -3.6 | 0.012 | 8/30 (LOX-IMVI, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.760×** | -3.5 | 0.016 | 9/35 (HCT15, BT-474, …) | two highest doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.602×** | -3.4 | 0.024 | 9/26 (LOX-IMVI, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.703×** | -3.2 | 0.041 | 6/36 (LoVo, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.782×** | -3.2 | 0.049 | 13/35 (SK-MEL-2, LOX-IMVI, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.783×** | -3.2 | 0.050 | 6/35 (LOX-IMVI, H4, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.778×** | -3.1 | 0.065 | 9/34 (LOX-IMVI, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.647×** | -2.9 | 0.096 | 6/32 (LOX-IMVI, J82, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7965. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 103 | 0 | 13 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0874× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.200× (z -12.3) |
| [[A-172 (line)]] | wt | 6.37 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.09× (z +11.3) | — |
| [[A549 (line)]] | wt | 6.28 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0706× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.191× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 26.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.213× (z -8.7) |
| [[SW480 (line)]] | alt | 11.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A498 (line)]] | wt | 2.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.14× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 2.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 5.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 3.43 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.0714× (z -8.7) |
| [[A-427 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.834 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.955 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.29 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7965), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC2-AS2]] | +0.74 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[FBXO38-DT]] | +0.74 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[SYT16]] | +0.70 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[CFAP54]] | +0.66 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[CDK6-AS1]] | +0.64 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[GRM8]] | +0.64 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[LRP2BP]] | +0.64 | +0.63 / +0.39 | both halves | 5e-05 |  |
| [[DRAIC]] | +0.63 | +0.59 / +0.40 | both halves | 4e-05 |  |
| [[CCDC26]] | +0.63 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[MALINC1]] | +0.63 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[ZPLD1]] | +0.63 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[EFCAB5]] | +0.62 | +0.53 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLTCL1]] | -0.55 | -0.39 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MAP3K7CL's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00993]] | B | LINC00993 activity strengthens MAP3K7CL's drug response | lines that do not express LINC00993 (27) vs lines expressing it (9) | the lines without LINC00993 respond 1.09× as strongly (z diff +0.32); strongest at Digitoxin 0.5 µM: 0.56x vs 0.28x (z diff +3.5) | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANKRD30A, KCNH5, KCNB2; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[ANKRD30A]] | B | ANKRD30A activity strengthens MAP3K7CL's drug response | lines that do not express ANKRD30A (27) vs lines expressing it (9) | the lines without ANKRD30A respond 1.09× as strongly (z diff +0.32); strongest at Digitoxin 0.5 µM: 0.56x vs 0.28x (z diff +3.5) | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00993, ENSG00000232252, ASCL1; target measured in part of the lines; both ways; artifact flags |
| [[DGKB]] | B | DGKB activity raises MAP3K7CL's level | lines that do not express DGKB (23) vs lines expressing it (27) | 1.76× lower at baseline in the lines without DGKB | 0.095 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.637). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.3, 15.9); signed map (28.7, 3.1). **Vector** length 71.1, 13.4% of its response variance represented; |z| ≥ 3 in 878 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +17.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.5 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +8.0 | +0.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.6 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.3 | -6.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -3.1 | -5.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -7.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.7 | -6.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -3.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.9 | -2.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | MAP3K7 C-terminal like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q21.3 — chr21:29,077,221-29,175,889 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TAKL, TAK1L, TAKL-1, TAKL-2, TAKL-4; previously C21orf7 |
| Matched by | ensembl_id |

UniProt [P57077](https://www.uniprot.org/uniprotkb/P57077) carries no function annotation.

**Summary**, from NCBI Gene [56911](https://www.ncbi.nlm.nih.gov/gene/56911):

> Located in cytosol and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16457](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16457) · Entrez [56911](https://www.ncbi.nlm.nih.gov/gene/56911) · UniProt [P57077](https://www.uniprot.org/uniprotkb/P57077) · Ensembl [ENSG00000156265](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156265)

## Data

Gene col 7965: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7965); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7965, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7965]; `tensor/DDL_lfc|DDL_z.npy` [7965]; `embed/gene_vectors.npy` [7965]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7965 or target_col == 7965). Every well: [[MAP3K7CL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP3K7CL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
