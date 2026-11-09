---
symbol: "SIGIRR"
type: "gene"
col: 11636
ensembl_id: "ENSG00000185187"
name: "single Ig and TIR domain containing"
location: "11p15.5"
module: 34
arm: "+"
pooled_cpm: 15.85
n_lines_expressing: 41
n_dd_up: 1
n_dd_down: 18
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 8
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# SIGIRR

*single Ig and TIR domain containing* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.75× (z +4.6, q 0.003, up in 22 of 34 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~34% of this change.
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.472× (z -8.6, q 4e-15, down in 33 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDKN2D]] (+0.73, fdr 1e-05), [[TMEM191A-1]] (+0.69, fdr 2e-05), [[MAP1S]] (+0.65, fdr 3e-05); moves opposite to [[SETD7]] (-0.62, fdr 6e-05), [[NAA50]] (-0.61, fdr 7e-05), [[PSME3IP1]] (-0.61, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 8 go from it, the strongest it → [[DPF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11636.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.75×** | +4.6 | 0.003 | 22/34 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.46× | +3.1 | 0.48 | 12/30 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11636.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.472×** | -8.6 | 4e-15 | 33/38 (Hs 766T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.493×** | -5.7 | 3e-06 | 25/35 (Hs 766T, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.661×** | -4.7 | 4e-04 | 24/38 (AsPC-1, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.320×** | -4.0 | 0.008 | 17/35 (LS 180, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.617×** | -3.9 | 0.010 | 20/38 (Hs 766T, LOX-IMVI, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.349×** | -3.7 | 0.015 | 15/38 (Panc 03.27, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.631×** | -3.7 | 0.015 | 20/38 (NCI-H1792, LOX-IMVI, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.640×** | -3.6 | 0.021 | 15/38 (Hs 766T, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.651×** | -3.5 | 0.033 | 16/38 (Hs 766T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.656×** | -3.4 | 0.037 | 14/39 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.643×** | -3.4 | 0.038 | 16/37 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.667×** | -3.3 | 0.046 | 10/38 (Hs 766T, AsPC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.646×** | -3.3 | 0.046 | 15/38 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.651×** | -3.2 | 0.053 | 10/38 (SW1417, LS 180, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.666×** | -3.2 | 0.060 | 17/35 (HS-578T, Hs 766T, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.669×** | -3.1 | 0.061 | 16/37 (NCI-H1792, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.688×** | -3.0 | 0.081 | 16/37 (SW 1271, Hs 766T, …) | rises with dose |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.668×** | -3.0 | 0.081 | 9/38 (RKO, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11636. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 81.1 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -17.3) |
| [[AsPC-1 (line)]] | alt | 38.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -16.4) |
| [[COLO 205 (line)]] | alt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -8.7) |
| [[HS-578T (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0436× (z -13.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 26.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 13.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -12.9) |
| [[RKO (line)]] | wt | 37.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -8.6) |
| [[SW480 (line)]] | alt | 14.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -10.0) |
| [[A-172 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11636), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN2D]] | +0.73 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[TMEM191A-1]] | +0.69 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[MAP1S]] | +0.65 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[RALGDS]] | +0.64 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[BAIAP3]] | +0.64 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[PAXX]] ⚠ | +0.64 | +0.31 / +0.55 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[TNNI3]] | +0.62 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[DNAAF3]] | +0.62 | +0.53 / +0.31 | both halves | 2e-04 |  |
| [[FCHO1]] | +0.62 | +0.56 / +0.29 | both halves | 3e-04 |  |
| [[TNFRSF25]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[FAM89B]] | +0.61 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[TECPR1]] | +0.61 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[PGPEP1]] | +0.61 | +0.52 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD7]] | -0.62 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[NAA50]] | -0.61 | -0.37 / -0.63 | both halves | 7e-05 |  |
| [[PSME3IP1]] | -0.61 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[DARS2]] | -0.60 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[SNX5]] | -0.60 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[PAPOLA]] | -0.60 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[RCN1]] | -0.59 | -0.26 / -0.57 | both halves | 3e-04 |  |
| [[PNISR-AS1]] | -0.58 | -0.36 / -0.24 | both halves | 5e-04 |  |
| [[ALG8]] | -0.58 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[VPS52]] | -0.57 | -0.28 / -0.33 | both halves | 3e-04 |  |
| [[PSME3]] | -0.57 | -0.37 / -0.56 | both halves | 8e-05 |  |
| [[KARS1]] | -0.57 | -0.49 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPF1]] | B | SIGIRR activity lowers DPF1's level | lines that do not express SIGIRR (9) vs lines expressing it (41) | 2.33× higher at baseline in the lines without SIGIRR | 0.013 | ⚠ within organs, on part of the lines; also absent: CLCF1, LTBR, MYOF |
| [[POLB]] | B | SIGIRR activity lowers POLB's level | lines that do not express SIGIRR (9) vs lines expressing it (41) | 1.26× higher at baseline in the lines without SIGIRR | 0.025 | ⚠ within organs, on part of the lines; also absent: CLCF1, LTBR, MYOF |
| [[DARS2]] | B | SIGIRR activity lowers DARS2's level | lines that do not express SIGIRR (9) vs lines expressing it (41) | 1.24× higher at baseline in the lines without SIGIRR | 0.044 | ⚠ within organs, on part of the lines; also absent: CLCF1, LTBR, MYOF |
| [[POLD4]] | B | SIGIRR activity raises POLD4's level | lines that do not express SIGIRR (9) vs lines expressing it (41) | 1.99× lower at baseline in the lines without SIGIRR | 0.050 | ⚠ within organs, on part of the lines; also absent: CLCF1, LTBR, MYOF |
| [[CBX8]] | B | SIGIRR activity lowers CBX8's level | lines that do not express SIGIRR (9) vs lines expressing it (41) | 1.36× higher at baseline in the lines without SIGIRR | 0.057 | ⚠ within organs, on part of the lines; also absent: CLCF1, LTBR, MYOF |
| [[ZMIZ2]] | B | SIGIRR activity raises ZMIZ2's level | lines that do not express SIGIRR (9) vs lines expressing it (41) | 1.50× lower at baseline in the lines without SIGIRR | 0.073 | ⚠ within organs, on part of the lines; also absent: CLCF1, LTBR, MYOF |
| [[RTN2]] | B | SIGIRR activity lowers RTN2's level | lines that do not express SIGIRR (9) vs lines expressing it (41) | 1.14× higher at baseline in the lines without SIGIRR | 0.074 | ⚠ within organs, on part of the lines; also absent: CLCF1, LTBR, MYOF |
| [[PAFAH1B3]] | B | SIGIRR activity lowers PAFAH1B3's level | lines that do not express SIGIRR (9) vs lines expressing it (41) | 1.44× higher at baseline in the lines without SIGIRR | 0.074 | ⚠ within organs, on part of the lines; also absent: CLCF1, LTBR, MYOF |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.500). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-47.7, 15.7); signed map (-28.5, 14.9). **Vector** length 65.2, 15.2% of its response variance represented; |z| ≥ 3 in 568 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | -0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +0.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | -2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +1.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.8 | +3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +2.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.5 | +2.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -3.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.5 | -3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.3 | -8.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -3.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | single Ig and TIR domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:405,715-417,455 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TIR8, IL-1R8 |
| Gene groups (HGNC) | Immunoglobulin like domain containing; TIR domain containing |
| Reactome | 11 pathways, smallest: Interleukin-37 signaling; MyD88:MAL(TIRAP) cascade initiated on plasma membrane; Toll Like Receptor TLR6:TLR2 Cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IA17](https://www.uniprot.org/uniprotkb/Q6IA17) (Single Ig IL-1-related receptor):

> Acts as a negative regulator of the Toll-like and IL-1R receptor signaling pathways. Attenuates the recruitment of receptor-proximal signaling components to the TLR4 receptor, probably through an TIR-TIR domain interaction with TLR4. Through its extracellular domain interferes with the heterodimerization of Il1R1 and IL1RAP.

**Summary**, from NCBI Gene [59307](https://www.ncbi.nlm.nih.gov/gene/59307):

> Involved in negative regulation of Toll signaling pathway. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30575](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30575) · Entrez [59307](https://www.ncbi.nlm.nih.gov/gene/59307) · UniProt [Q6IA17](https://www.uniprot.org/uniprotkb/Q6IA17) · Ensembl [ENSG00000185187](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185187)

## Data

Gene col 11636: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11636); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11636, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11636]; `tensor/DDL_lfc|DDL_z.npy` [11636]; `embed/gene_vectors.npy` [11636]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11636 or target_col == 11636). Every well: [[SIGIRR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIGIRR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
