---
symbol: "CRAT"
type: "gene"
col: 1742
ensembl_id: "ENSG00000095321"
name: "carnitine O-acetyltransferase"
location: "9q34.11"
module: 2
arm: "+"
pooled_cpm: 11.45
n_lines_expressing: 48
n_dd_up: 5
n_dd_down: 19
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CRAT

*carnitine O-acetyltransferase* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.75× (z +6.9, q 3e-09, up in 9 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.30× (z +3.3, q 0.095, up in 7 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.325× (z -14.5, q 1e-44, down in 34 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TESK1]] (+0.72, fdr 7e-06), [[PPP2R5D]] (+0.69, fdr 7e-06), [[NAGA]] (+0.68, fdr 7e-06); moves opposite to [[RPL7L1]] (-0.58, fdr 3e-05), [[CFLAR-AS1]] (-0.56, fdr 3e-05), [[PBDC1]] (-0.54, fdr 3e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CERCAM]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1742.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +6.9 | 3e-09 | 9/20 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +5.8 | 2e-06 | 20/34 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +3.6 | 0.054 | 8/26 (LS 180, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.32×** | +3.6 | 0.054 | 12/37 (Panc 03.27, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.095 | 7/45 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.2 | 0.13 | 1/46 (NCI-H23) | inconsistent across doses |  |
| [[venetoclax (drug)]] 0.05 µM |  | 1.30× | +3.2 | 0.13 | 6/45 (SW480, HOP62, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1742.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.325×** | -14.5 | 1e-44 | 34/41 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.460×** | -14.1 | 9e-43 | 35/42 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.411×** | -11.0 | 7e-26 | 37/44 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.540×** | -7.9 | 3e-13 | 28/44 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.615×** | -6.3 | 4e-08 | 23/42 (C32, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.641×** | -5.7 | 9e-07 | 27/45 (SW 900, H4, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.642×** | -5.7 | 9e-07 | 24/45 (SNU-1, J82, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.664×** | -5.0 | 5e-05 | 21/45 (C32, RPMI-7951, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.708×** | -4.4 | 6e-04 | 21/45 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.529×** | -4.3 | 0.001 | 17/43 (A498, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.548×** | -4.0 | 0.003 | 17/40 (KATO III, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.736×** | -3.9 | 0.004 | 15/45 (LOX-IMVI, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.751×** | -3.7 | 0.010 | 16/45 (HS-578T, LS 180, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.735×** | -3.7 | 0.010 | 14/41 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Ciclopirox (drug)]] 5 µM |  | **0.819×** | -3.6 | 0.010 | 13/45 (HepG2/C3A, RPMI-7951, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.757×** | -3.6 | 0.012 | 15/45 (LoVo, A-427, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1742. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 29.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -16.1) |
| [[A498 (line)]] | wt | 22.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -13.8) |
| [[C32 (line)]] | wt | 8.86 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0774× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Hydroxyurea (drug)]] 0.05 µM 0.0927× (z -9.6) |
| [[HOP62 (line)]] | alt | 12.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -13.3) |
| [[HS-578T (line)]] | alt | 12.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 8.36 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0311× (z -15.8) |
| [[NCI-H2030 (line)]] | alt | 7.33 | 0 | 2 (2 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0974× (z -10.6) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 10.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.200× (z -10.4) |
| [[A549 (line)]] | wt | 14.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -9.3) |
| [[BT-474 (line)]] | alt | 42.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -11.5) |
| [[HCT15 (line)]] | alt | 16.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0978× (z -9.9) |
| [[HepG2_C3A (line)]] | wt | 10.3 | 0 | 1 | — | [[Ciclopirox (drug)]] 5 µM 0.182× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -8.6) |
| [[J82 (line)]] | alt | 14.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 23.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -9.9) |
| [[PANC-1 (line)]] | alt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.334× (z -8.5) |
| [[RKO (line)]] | wt | 28.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -9.0) |
| [[SHP-77 (line)]] | alt | 9.86 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.120× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 10.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.118× (z -9.0) |
| [[SNU-1 (line)]] | wt | 9.02 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0431× (z -10.1) |
| [[SW 900 (line)]] | alt | 6.80 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0819× (z -8.9) |
| [[A-427 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.77 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1742), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TESK1]] | +0.72 | +0.61 / +0.76 | both halves | 7e-06 |  |
| [[PPP2R5D]] | +0.69 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[NAGA]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[PIK3R2]] | +0.68 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[HECTD3]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[SBF1]] | +0.66 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[SDHA]] | +0.65 | +0.65 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[ZDHHC16]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[REEP4]] | +0.65 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[GIT1]] | +0.64 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[MAN2B2]] | +0.64 | +0.60 / +0.57 | both halves | 8e-06 |  |
| [[HMG20B]] | +0.64 | +0.62 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL7L1]] | -0.58 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[CFLAR-AS1]] | -0.56 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[PBDC1]] | -0.54 | -0.60 / -0.29 | both halves | 3e-04 |  |
| [[HELQ]] | -0.53 | -0.53 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CERCAM]] | B | CERCAM activity raises CRAT's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 1.44× lower at baseline in the lines without CERCAM | 0.070 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.654). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.0, -21.1); signed map (-48.0, -11.9). **Vector** length 69.8, 12.0% of its response variance represented; |z| ≥ 3 in 840 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.4 | +3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +6.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +1.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | +0.0 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | +1.6 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -14.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -11.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.6 | -7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | -14.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -4.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -0.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | carnitine O-acetyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:129,094,142-129,111,189 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CAT1 |
| Gene groups (HGNC) | Carnitine acyltransferases |
| Hallmark sets | PEROXISOME, FATTY_ACID_METABOLISM, MYOGENESIS, APICAL_JUNCTION, ADIPOGENESIS |
| Reactome | 8 pathways, smallest: Beta-oxidation of pristanoyl-CoA; Branched-chain amino acid catabolism; Peroxisomal lipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P43155](https://www.uniprot.org/uniprotkb/P43155) (Carnitine O-acetyltransferase):

> Catalyzes the reversible transfer of acyl groups from carnitine to coenzyme A (CoA) and regulates the acyl-CoA/CoA ratio. Also plays a crucial role in the transport of fatty acids for beta-oxidation. Responsible for the synthesis of short- and branched-chain acylcarnitines. Active towards some branched-chain amino acid oxidation pathway (BCAAO) intermediates. Trans-2-enoyl-CoAs and 2-methylacyl-CoAs are poor substrates.

**Summary**, from NCBI Gene [1384](https://www.ncbi.nlm.nih.gov/gene/1384):

> This gene encodes carnitine O-acetyltransferase, a member of the carnitine acyltransferase family and a key metabolic pathway enzyme which plays an important role in energy homeostasis and fat metabolism. This enzyme catalyzes the reversible transfer of acyl groups from an acyl-CoA thioester to carnitine and regulates the ratio of acyl-CoA/CoA. It is found in both the mitochondria and the peroxisome. Alternative splicing results in transcript variants encoding different isoforms that may …

**Accessions** — [HGNC:2342](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2342) · Entrez [1384](https://www.ncbi.nlm.nih.gov/gene/1384) · UniProt [P43155](https://www.uniprot.org/uniprotkb/P43155) · Ensembl [ENSG00000095321](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095321)

## Data

Gene col 1742: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1742); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1742, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1742]; `tensor/DDL_lfc|DDL_z.npy` [1742]; `embed/gene_vectors.npy` [1742]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1742 or target_col == 1742). Every well: [[CRAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
