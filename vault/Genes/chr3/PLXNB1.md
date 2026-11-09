---
symbol: "PLXNB1"
type: "gene"
col: 8845
ensembl_id: "ENSG00000164050"
name: "plexin B1"
location: "3p21.31"
module: 126
arm: "+"
pooled_cpm: 10.87
n_lines_expressing: 48
n_dd_up: 2
n_dd_down: 20
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# PLXNB1

*plexin B1* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.47× (z +4.3, q 0.011, up in 8 of 30 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HOP62 3.93×; ⚠ cell-cycle shift, explains ~77% of this change).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.368× (z -11.5, q 5e-28, down in 35 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STRN4]] (+0.67, fdr 1e-05), [[MTA2]] (+0.64, fdr 1e-05), [[ADCY6]] (+0.63, fdr 7e-06); moves opposite to [[LGALS1]] (-0.55, fdr 4e-05), [[NDUFA7]] (-0.52, fdr 3e-05), [[CEP170]] (-0.51, fdr 1e-04).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[DMTN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8845.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HOP62 3.93×; ⚠ cell-cycle shift, explains ~77% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +4.3 | 0.011 | 8/30 (HEC-1-A, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +3.6 | 0.079 | 11/24 (NCI-H2347, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Budesonide (drug)]] 5 µM |  | 1.32× | +3.1 | 0.32 | 11/43 (Hs 766T, A498, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8845.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.368×** | -11.5 | 5e-28 | 35/43 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.370×** | -11.5 | 6e-28 | 38/43 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.436×** | -9.6 | 2e-19 | 35/43 (KATO III, SHP-77, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.553×** | -6.6 | 7e-09 | 23/40 (LOX-IMVI, COLO 205, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.606×** | -5.8 | 8e-07 | 20/39 (SW48, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.650×** | -5.0 | 6e-05 | 20/43 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.742×** | -4.9 | 8e-05 | 22/38 (COLO 205, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.650×** | -4.7 | 2e-04 | 15/42 (HS-578T, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.762×** | -4.5 | 5e-04 | 19/38 (SW1417, SW480, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.702×** | -4.0 | 0.004 | 13/42 (SW48, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.713×** | -3.9 | 0.005 | 15/43 (SW480, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.723×** | -3.8 | 0.008 | 15/43 (AN3 CA, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.743×** | -3.3 | 0.046 | 2/44 (HOP62, C-33 A) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | **0.822×** | -3.2 | 0.052 | 8/43 (NCI-H23, NCI-H460, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.828×** | -3.1 | 0.074 | 14/43 (SW48, SW480, …) | top dose only | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.771×** | -3.0 | 0.083 | 9/44 (SK-MEL-2, LS 180, …) | top dose only |  |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.767×** | -3.0 | 0.083 | 12/43 (CHP-212, HT-29, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | **0.764×** | -3.0 | 0.083 | 5/43 (SW48, J82, …) | top dose only | position effect removed |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.834× | -3.0 | 0.083 | 12/43 (NCI-H2347, HEC-1-A, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8845. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -12.3) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.121× (z -8.9) |
| [[KATO III (line)]] | alt | 16.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.118× (z -11.8) |
| [[LoVo (line)]] | wt | 16.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.110× (z -14.3) |
| [[LS 180 (line)]] | wt | 21.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -13.3) |
| [[SW1417 (line)]] | alt | 39.6 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.262× (z -9.6) |
| [[SW48 (line)]] | wt | 30.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0415× (z -14.9) |
| [[SW480 (line)]] | alt | 31.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 4.41 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0503× (z -10.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0873× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 4.11 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0859× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.166× (z -8.5) |
| [[HOP62 (line)]] | alt | 6.59 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +9.5) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[HT-29 (line)]] | alt | 17.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.142× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 4.58 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0843× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -11.0) ⚠ cell-cycle shift, explains ~77% of this change |
| [[SHP-77 (line)]] | alt | 18.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.161× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 11.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.110× (z -9.4) |
| [[A-172 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8845), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRN4]] | +0.67 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[MTA2]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[ADCY6]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[INPPL1]] | +0.62 | +0.57 / +0.55 | both halves | 1e-05 | STRING 525 |
| [[AKT2]] | +0.62 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[MTA1]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[EME2]] | +0.60 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[MAN2A2]] | +0.60 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[WASH8P]] ⚠ | +0.60 | +0.46 / +0.58 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[U2AF2]] | +0.59 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[RCC2]] | +0.58 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[GRK2]] | +0.58 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[CERS2]] | +0.57 | +0.41 / +0.55 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LGALS1]] | -0.55 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[NDUFA7]] | -0.52 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[CEP170]] | -0.51 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[TMEM191A-1]] | -0.51 | -0.20 / -0.51 | ⚠ one half (not replicated) | 8e-04 |  |
| [[EFL1]] | -0.49 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[LINC00888-1]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[VIM]] | -0.48 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[PSMA7]] | -0.48 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[SH3BGRL3]] | -0.48 | -0.24 / -0.40 | both halves | 5e-04 |  |
| [[CHCHD2]] | -0.47 | -0.25 / -0.44 | both halves | 4e-04 |  |
| [[YIPF5]] | -0.47 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[UPK1A-AS1]] | -0.47 | -0.29 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DMTN]] | B | DMTN activity raises PLXNB1's level | lines that do not express DMTN (14) vs lines expressing it (36) | 2.01× lower at baseline in the lines without DMTN | 0.014 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |
| [[MUC6]] | B | MUC6 activity raises PLXNB1's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 1.72× lower at baseline in the lines without MUC6 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB |
| [[EVPL]] | B | EVPL activity raises PLXNB1's level | lines that do not express EVPL (16) vs lines expressing it (34) | 1.53× lower at baseline in the lines without EVPL | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: PTK6, MYO5C, SFN |
| [[CPLX2]] | B | CPLX2 activity raises PLXNB1's level | lines that do not express CPLX2 (41) vs lines expressing it (9) | 1.55× lower at baseline in the lines without CPLX2 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, TBXT, F5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.742). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.6, -23.8); signed map (-11.6, -34.0). **Vector** length 77.5, 14.7% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.5 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +3.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.2 | +1.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +4.1 | -4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | -0.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +1.3 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -2.5 | -1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -4.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.4 | -2.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.3 | -9.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.2 | -6.6 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.9 | -2.2 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.6 | -3.0 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | plexin B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:48,403,854-48,430,086 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SEP, KIAA0407; previously PLXN5 |
| Gene groups (HGNC) | Plexins; IPT domain containing |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 13 pathways, smallest: Sema4D mediated inhibition of cell attachment and migration; Sema4D induced cell migration and growth-cone collapse; Sema4D in semaphorin signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O43157](https://www.uniprot.org/uniprotkb/O43157) (Plexin-B1):

> Receptor for SEMA4D. Plays a role in GABAergic synapse development (By similarity). Mediates SEMA4A- and SEMA4D-dependent inhibitory synapse development (By similarity). Plays a role in RHOA activation and subsequent changes of the actin cytoskeleton. Plays a role in axon guidance, invasive growth and cell migration.

**Summary**, from NCBI Gene [5364](https://www.ncbi.nlm.nih.gov/gene/5364):

> Enables semaphorin receptor activity. Involved in several processes, including negative regulation of cell adhesion; regulation of cell shape; and semaphorin-plexin signaling pathway. Located in plasma membrane. Part of semaphorin receptor complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9103](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9103) · Entrez [5364](https://www.ncbi.nlm.nih.gov/gene/5364) · UniProt [O43157](https://www.uniprot.org/uniprotkb/O43157) · Ensembl [ENSG00000164050](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164050)

## Data

Gene col 8845: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8845); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8845, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8845]; `tensor/DDL_lfc|DDL_z.npy` [8845]; `embed/gene_vectors.npy` [8845]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8845 or target_col == 8845). Every well: [[PLXNB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLXNB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
