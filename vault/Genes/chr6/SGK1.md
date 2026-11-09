---
symbol: "SGK1"
type: "gene"
col: 4000
ensembl_id: "ENSG00000118515"
name: "serum/glucocorticoid regulated kinase 1"
location: "6q23.2"
module: 113
arm: "+"
pooled_cpm: 35.95
n_lines_expressing: 38
n_dd_up: 11
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# SGK1

*serum/glucocorticoid regulated kinase 1* — 6q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.84× (z +10.2, q 7e-22, up in 32 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.539× (z -7.3, q 2e-10, down in 29 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIB1]] (+0.68, fdr 7e-06), [[ADRB2]] (+0.67, fdr 7e-06), [[DUSP1]] (+0.61, fdr 1e-05); moves opposite to [[TCEA1]] (-0.48, fdr 4e-05), [[NAPB]] (-0.48, fdr 3e-05), [[RUFY2]] (-0.47, fdr 6e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[CCDC71L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4000.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +10.2 | 7e-22 | 32/36 (A498, SW1417, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.86×** | +7.3 | 6e-11 | 22/36 (C32, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.67×** | +6.1 | 2e-07 | 26/36 (NCI-H460, SNU-423, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.61×** | +5.5 | 6e-06 | 21/36 (CFPAC-1, A498, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.58×** | +5.4 | 7e-06 | 17/36 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.56×** | +5.3 | 1e-05 | 20/36 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +5.0 | 5e-05 | 23/36 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +4.3 | 0.001 | 18/36 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.98×** | +4.2 | 0.001 | 16/37 (MIA PaCa-2, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Uridine (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.075 | 9/36 (NCI-H1792, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.31×** | +3.2 | 0.075 | 13/36 (C32, A498, …) | inconsistent across doses |  |
| [[Gefitinib (drug)]] 5 µM |  | 1.29× | +3.0 | 0.12 | 11/36 (NCI-H460, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4000.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.539×** | -7.3 | 2e-10 | 29/36 (COLO 205, KATO III, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.619×** | -5.7 | 4e-06 | 22/35 (A-427, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.882× | -4.8 | 2e-04 | 8/36 (MIA PaCa-2, C32, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.683×** | -4.5 | 0.001 | 17/36 (LOX-IMVI, J82, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.688×** | -4.2 | 0.003 | 18/36 (J82, LOX-IMVI, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.792×** | -3.9 | 0.010 | 15/36 (hTERT-HPNE, A-172, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.794×** | -3.8 | 0.010 | 15/36 (COLO 205, AsPC-1, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.548×** | -3.7 | 0.014 | 14/36 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.731×** | -3.5 | 0.025 | 18/36 (A549, NCI-H23, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.751×** | -3.2 | 0.066 | 15/29 (MIA PaCa-2, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.761×** | -3.2 | 0.066 | 16/36 (hTERT-HPNE, COLO 205, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.764×** | -3.2 | 0.071 | 12/36 (KATO III, AsPC-1, …) | rises with dose | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.769×** | -3.1 | 0.089 | 11/35 (A498, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4000. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 103 | 6 (3 ⚠) | 3 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 24.7× (z +13.7) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 258 | 3 (1 ⚠) | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 14.8× (z +14.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -19.7) |
| [[COLO 205 (line)]] | alt | 86.5 | 0 | 8 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0773× (z -13.2) |
| [[NCI-H23 (line)]] | alt | 129 | 1 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 8.28× (z +8.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0225× (z -28.3) |
| [[NCI-H460 (line)]] | wt | 57.3 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 4.96× (z +11.1) | — |
| [[LOX-IMVI (line)]] | wt | 70.6 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -10.7) |
| [[A-427 (line)]] | wt | 61.2 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.87× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0938× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -8.5) |
| [[J82 (line)]] | alt | 78.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 14.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +16.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 3.95× (z +12.0) | — |
| [[HepG2_C3A (line)]] | wt | 48.5 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.221× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 78.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0465× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 20.6 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.18× (z +8.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[CFPAC-1 (line)]] | alt | 18.2 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.26× (z +9.0) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[Hs 766T (line)]] | wt | 19.0 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.188× (z -8.5) |
| [[HT-29 (line)]] | alt | 28.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.58× (z +9.5) | — |
| [[KATO III (line)]] | alt | 16.8 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.170× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 35.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.224× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 28.7 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 6.09× (z +9.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 35.1 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 5.19× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 24.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.06× (z +9.8) | — |
| [[A-172 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.34 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.80 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 68.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.09 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.67 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.47 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.01 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.81 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.10 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.23 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.54 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.42 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4000), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIB1]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ADRB2]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[DUSP1]] | +0.61 | +0.55 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 611 |
| [[CITED2]] | +0.61 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[SLC38A2]] | +0.59 | +0.60 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[TIPARP]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ABL2]] | +0.58 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[EPAS1]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[MYC]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 647 |
| [[TCIM]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[NFKBIZ]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[CCL20]] | +0.57 | +0.47 / +0.56 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCEA1]] | -0.48 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[NAPB]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[RUFY2]] | -0.47 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[ATPAF1]] | -0.47 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[RTCA]] | -0.47 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[MTO1]] | -0.47 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[ALG5]] | -0.46 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[CDC23]] | -0.46 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[SASS6]] | -0.45 | -0.48 / -0.37 | both halves | 9e-05 |  |
| [[TRAPPC13]] | -0.45 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[ACTR10]] | -0.45 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[PRPSAP2]] | -0.45 | -0.43 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC71L]] | B | SGK1 activity raises CCDC71L's level | lines that do not express SGK1 (12) vs lines expressing it (38) | 2.16× lower at baseline in the lines without SGK1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with WNK2, PRDM2; also absent: RNF182, FRG1DP, DPYSL3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.620). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.3, 8.2); signed map (10.3, 29.6). **Vector** length 106, 26.3% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +10.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +5.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +3.9 | +6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.8 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +2.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.6 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.6 | +1.5 |
|  | [[Thymol (drug)]] 5 µM |  | +2.3 | +2.0 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -5.6 | -7.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.4 | -3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | -2.7 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.7 | -3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -3.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.5 | -2.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | serum/glucocorticoid regulated kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.2 — chr6:134,169,248-134,318,112 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SGK |
| Gene groups (HGNC) | Serum/glucocorticoid regulated kinase family |
| Hallmark sets | ANDROGEN_RESPONSE, KRAS_SIGNALING_DN, ESTROGEN_RESPONSE_LATE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 15 pathways, smallest: NGF-stimulated transcription; Regulation of TP53 Degradation; Regulation of TP53 Expression and Degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [O00141](https://www.uniprot.org/uniprotkb/O00141) (Serine/threonine-protein kinase Sgk1):

> Serine/threonine-protein kinase which is involved in the regulation of a wide variety of ion channels, membrane transporters, cellular enzymes, transcription factors, neuronal excitability, cell growth, proliferation, survival, migration and apoptosis. Plays an important role in cellular stress response. Contributes to regulation of renal Na(+) retention, renal K(+) elimination, salt appetite, gastric acid secretion, intestinal Na(+)/H(+) exchange and nutrient transport, insulin-dependent salt …

**Summary**, from NCBI Gene [6446](https://www.ncbi.nlm.nih.gov/gene/6446):

> This gene encodes a serine/threonine protein kinase that plays an important role in cellular stress response. This kinase activates certain potassium, sodium, and chloride channels, suggesting an involvement in the regulation of processes such as cell survival, neuronal excitability, and renal sodium excretion. High levels of expression of this gene may contribute to conditions such as hypertension and diabetic nephropathy. Several alternatively spliced transcript variants encoding different …

**Accessions** — [HGNC:10810](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10810) · Entrez [6446](https://www.ncbi.nlm.nih.gov/gene/6446) · UniProt [O00141](https://www.uniprot.org/uniprotkb/O00141) · Ensembl [ENSG00000118515](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118515)

## Data

Gene col 4000: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4000); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4000, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4000]; `tensor/DDL_lfc|DDL_z.npy` [4000]; `embed/gene_vectors.npy` [4000]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4000 or target_col == 4000). Every well: [[SGK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
