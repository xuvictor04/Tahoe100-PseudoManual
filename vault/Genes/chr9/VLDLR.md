---
symbol: "VLDLR"
type: "gene"
col: 7224
ensembl_id: "ENSG00000147852"
name: "very low density lipoprotein receptor"
location: "9p24.2"
module: 134
arm: "+"
pooled_cpm: 22.14
n_lines_expressing: 42
n_dd_up: 1
n_dd_down: 33
n_dd_up_clean: 1
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# VLDLR

*very low density lipoprotein receptor* — 9p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Roxadustat (drug)]] 5 µM: 1.36× (z +4.4, q 0.005, up in 18 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.140× (z -42.0, q 0e+00, down in 39 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHSY1]] (+0.65, fdr 1e-05), [[CCSAP]] (+0.64, fdr 7e-06), [[ATRN]] (+0.62, fdr 1e-05); moves opposite to [[STAT6]] (-0.57, fdr 8e-05), [[ATXN7L1]] (-0.56, fdr 4e-05), [[ARAP2]] (-0.55, fdr 3e-05).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[STBD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7224.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Roxadustat (drug)]] 5 µM |  | **1.36×** | +4.4 | 0.005 | 18/38 (A-172, SNU-423, …) | top dose only |  |
| [[Erlotinib (drug)]] 5 µM |  | 1.27× | +3.5 | 0.11 | 14/38 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[AT7519 (drug)]] 5 µM |  | 1.49× | +3.1 | 0.32 | 4/38 (HOP62, J82, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7224.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.140×** | -42.0 | 0e+00 | 39/39 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.156×** | -27.0 | 0e+00 | 38/38 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.177×** | -26.1 | 0e+00 | 37/39 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.337×** | -16.4 | 0e+00 | 35/40 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.331×** | -15.4 | 0e+00 | 30/32 (HEC-1-A, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.387×** | -14.3 | 2e-44 | 28/34 (J82, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.403×** | -13.7 | 7e-41 | 33/40 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.631×** | -9.8 | 9e-21 | 29/39 (HS-578T, C32, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.539×** | -9.3 | 7e-19 | 29/39 (HOP62, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.539×** | -9.0 | 2e-17 | 26/28 (NCI-H460, HOP62, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.548×** | -8.7 | 2e-16 | 25/35 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.570×** | -8.5 | 1e-15 | 26/38 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.559×** | -8.4 | 2e-15 | 30/37 (HS-578T, SK-MEL-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.596×** | -7.5 | 3e-12 | 26/39 (RPMI-7951, SW 900, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -7.5 | 3e-12 | 24/37 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.646×** | -6.6 | 2e-09 | 21/40 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.679×** | -5.8 | 2e-07 | 20/39 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.760×** | -5.8 | 2e-07 | 23/40 (A-172, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.781×** | -5.3 | 4e-06 | 22/40 (NCI-H1573, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.713×** | -5.1 | 1e-05 | 19/40 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.733×** | -4.7 | 8e-05 | 18/38 (HOP62, HS-578T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.724×** | -4.6 | 1e-04 | 20/39 (SNU-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.780×** | -3.7 | 0.004 | 15/39 (HOP62, SK-MEL-2, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7224. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.3 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0736× (z -30.8) |
| [[A-172 (line)]] | wt | 39.8 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0402× (z -36.8) |
| [[C32 (line)]] | wt | 42.6 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0406× (z -33.1) |
| [[HS-578T (line)]] | alt | 42.3 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0546× (z -33.3) |
| [[RPMI-7951 (line)]] | alt | 35.3 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -19.5) |
| [[SK-MEL-2 (line)]] | alt | 46.7 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0514× (z -35.7) |
| [[A549 (line)]] | wt | 34.5 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0811× (z -28.3) |
| [[H4 (line)]] | wt | 37.7 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0454× (z -16.5) |
| [[HOP62 (line)]] | alt | 44.8 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0474× (z -37.8) |
| [[J82 (line)]] | alt | 46.4 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0536× (z -33.0) |
| [[SW 900 (line)]] | alt | 38.9 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -18.9) |
| [[HEC-1-A (line)]] | alt | 28.1 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -27.1) |
| [[SNU-1 (line)]] | wt | 54.6 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -16.2) |
| [[BT-474 (line)]] | alt | 12.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -12.6) |
| [[NCI-H1792 (line)]] | alt | 39.0 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0927× (z -16.9) |
| [[PANC-1 (line)]] | alt | 8.21 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0978× (z -22.8) |
| [[A498 (line)]] | wt | 39.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -17.1) |
| [[LOX-IMVI (line)]] | wt | 23.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0671× (z -27.0) |
| [[SNU-423 (line)]] | alt | 26.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -20.5) |
| [[SW480 (line)]] | alt | 20.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -16.8) |
| [[COLO 205 (line)]] | alt | 14.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -12.3) |
| [[HepG2_C3A (line)]] | wt | 40.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0973× (z -21.2) |
| [[Hs 766T (line)]] | wt | 14.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0292× (z -19.5) |
| [[hTERT-HPNE (line)]] | wt | 17.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0225× (z -17.7) |
| [[MIA PaCa-2 (line)]] | alt | 12.5 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0289× (z -18.3) |
| [[NCI-H1573 (line)]] | alt | 5.90 | 0 | 3 | — | [[Belumosudil (drug)]] 5 µM 0.0757× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 10.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.349× (z -9.5) |
| [[HCT15 (line)]] | alt | 33.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0586× (z -22.0) |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0678× (z -21.8) |
| [[SW1417 (line)]] | alt | 18.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 23.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -18.9) |
| [[HT-29 (line)]] | alt | 15.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -14.1) |
| [[LS 180 (line)]] | wt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 8.98 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -12.2) |
| [[SHP-77 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -9.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 4.32 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.36 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.03 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7224), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHSY1]] | +0.65 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[CCSAP]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ATRN]] | +0.62 | +0.59 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[ARL6]] | +0.61 | +0.66 / +0.38 | both halves | 7e-05 |  |
| [[UBE2O]] | +0.61 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[FAM234B]] | +0.60 | +0.72 / +0.38 | both halves | 7e-05 |  |
| [[CABIN1]] | +0.60 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[GPT2]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[LNPK]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[PLEKHA8]] | +0.58 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[HK1]] | +0.57 | +0.67 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_HYPOXIA |
| [[VKORC1]] | +0.57 | +0.66 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STAT6]] | -0.57 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[ATXN7L1]] | -0.56 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[ARAP2]] | -0.55 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[PMF1]] | -0.53 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[GNG4]] | -0.53 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[PTPRK]] | -0.53 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[SH3D19]] | -0.53 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[ITPA]] | -0.52 | -0.57 / -0.30 | both halves | 2e-04 |  |
| [[SPTY2D1OS]] | -0.52 | -0.60 / -0.38 | both halves | 7e-05 |  |
| [[IQCH-AS1]] | -0.50 | -0.64 / -0.25 | both halves | 4e-04 |  |
| [[GABPB2]] | -0.50 | -0.59 / -0.28 | both halves | 3e-04 |  |
| [[SLC9A8]] | -0.49 | -0.58 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises VLDLR's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MLLT3]] | B | MLLT3 activity raises VLDLR's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 2.53× lower at baseline in the lines without MLLT3 | 0.084 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |
| [[PLOD2]] | B | PLOD2 activity raises VLDLR's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 2.47× lower at baseline in the lines without PLOD2 | 0.090 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STBD1]] | B | VLDLR activity raises STBD1's level | lines that do not express VLDLR (8) vs lines expressing it (42) | 1.81× lower at baseline in the lines without VLDLR | 0.032 | ⚠ within organs, on part of the lines; also absent: NEURL3, ALK, ENSG00000258989 |
| [[PLOD2]] | B | VLDLR activity raises PLOD2's level | lines that do not express VLDLR (8) vs lines expressing it (42) | 5.40× lower at baseline in the lines without VLDLR | 0.049 | ⚠ within organs, on part of the lines; also absent: NEURL3, ALK, ENSG00000258989 |
| [[STC2]] | B | VLDLR activity raises STC2's level | lines that do not express VLDLR (8) vs lines expressing it (42) | 3.90× lower at baseline in the lines without VLDLR | 0.067 | ⚠ within organs, on part of the lines; also absent: NEURL3, ALK, ENSG00000258989 |
| [[CCNJL]] | B | VLDLR activity raises CCNJL's level | lines that do not express VLDLR (8) vs lines expressing it (42) | 2.21× lower at baseline in the lines without VLDLR | 0.072 | ⚠ within organs, on part of the lines; also absent: NEURL3, ALK, ENSG00000258989 |
| [[PFKFB4]] | B | VLDLR activity raises PFKFB4's level | lines that do not express VLDLR (8) vs lines expressing it (42) | 2.24× lower at baseline in the lines without VLDLR | 0.073 | ⚠ within organs, on part of the lines; also absent: NEURL3, ALK, ENSG00000258989 |
| [[SFXN3]] | B | VLDLR activity strengthens SFXN3's drug response | lines that do not express VLDLR (8) vs lines expressing it (38) | the lines without VLDLR respond 0.60× as strongly (z diff +2.38); strongest at Homoharringtonine 0.5 µM: 0.49x vs 0.23x (z diff +3.7) | 0.081 | ⚠ within organs, on part of the lines; also absent: NEURL3, ALK, ENSG00000258989; target measured in part of the lines; artifact flags |
| [[MLLT3]] | B | VLDLR activity raises MLLT3's level | lines that do not express VLDLR (8) vs lines expressing it (42) | 2.39× lower at baseline in the lines without VLDLR | 0.082 | ⚠ within organs, on part of the lines; also absent: NEURL3, ALK, ENSG00000258989 |

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.664). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.6, -15.5); signed map (-36.2, 21.9). **Vector** length 86.9, 20.8% of its response variance represented; |z| ≥ 3 in 1,051 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.8 | -0.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.7 | -9.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.6 | -13.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.6 | +2.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.5 | -16.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | -3.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.6 | -0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | -1.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.5 | -27.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.8 | -14.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -4.4 | -9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.9 | -15.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -42.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.2 | -2.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -1.9 | -0.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.8 | -1.1 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | very low density lipoprotein receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.2 — chr9:2,621,182-2,660,056 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CARMQ1, CHRMQ1, VLDLRCH |
| Gene groups (HGNC) | Low density lipoprotein receptors |
| Hallmark sets | HEDGEHOG_SIGNALING, UV_RESPONSE_DN, GLYCOLYSIS, HYPOXIA, MTORC1_SIGNALING |
| Reactome | 8 pathways, smallest: VLDL clearance; Reelin signalling pathway; VLDLR internalisation and degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P98155](https://www.uniprot.org/uniprotkb/P98155) (Very low-density lipoprotein receptor):

> Multifunctional cell surface receptor that binds VLDL and transports it into cells by endocytosis and therefore plays an important role in energy metabolism. Also binds to a wide range of other molecules including Reelin/RELN or apolipoprotein E/APOE-containing ligands as well as clusterin/CLU. In the off-state of the pathway, forms homooligomers or heterooligomers with LRP8. Upon binding to ligands, homooligomers are rearranged to higher order receptor clusters that transmit the extracellular …

**Summary**, from NCBI Gene [7436](https://www.ncbi.nlm.nih.gov/gene/7436):

> The low density lipoprotein receptor (LDLR) gene family consists of cell surface proteins involved in receptor-mediated endocytosis of specific ligands. This gene encodes a lipoprotein receptor that is a member of the LDLR family and plays important roles in VLDL-triglyceride metabolism and the reelin signaling pathway. Mutations in this gene cause VLDLR-associated cerebellar hypoplasia. Alternative splicing generates multiple transcript variants encoding distinct isoforms for this gene. …

**Accessions** — [HGNC:12698](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12698) · Entrez [7436](https://www.ncbi.nlm.nih.gov/gene/7436) · UniProt [P98155](https://www.uniprot.org/uniprotkb/P98155) · Ensembl [ENSG00000147852](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147852)

## Data

Gene col 7224: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7224); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7224, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7224]; `tensor/DDL_lfc|DDL_z.npy` [7224]; `embed/gene_vectors.npy` [7224]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7224 or target_col == 7224). Every well: [[VLDLR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VLDLR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
