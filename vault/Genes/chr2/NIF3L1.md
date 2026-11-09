---
symbol: "NIF3L1"
type: "gene"
col: 12172
ensembl_id: "ENSG00000196290"
name: "NGG1 interacting factor 3 like 1"
location: "2q33.1"
module: 71
arm: "+"
pooled_cpm: 15.51
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 16
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# NIF3L1

*NGG1 interacting factor 3 like 1* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.32× (z +7.7, q 7e-12, up in 21 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.70×); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 2.79×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.530× (z -17.6, q 0e+00, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF4]] (+0.62, fdr 1e-05), [[TTI1]] (+0.62, fdr 1e-05), [[HAUS6]] (+0.61, fdr 1e-05); moves opposite to [[DUSP8]] (-0.53, fdr 2e-05), [[NOTCH2NLC]] (-0.53, fdr 2e-05), [[PEA15]] (-0.52, fdr 3e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RAB20]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12172.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.70×); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 2.79×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +7.7 | 7e-12 | 21/46 (MIA PaCa-2, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.23×** | +4.1 | 0.014 | 13/47 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.39× | +3.4 | 0.13 | 5/30 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12172.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.530×** | -17.6 | 0e+00 | 39/47 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.602×** | -9.5 | 4e-19 | 29/47 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.639×** | -8.4 | 6e-15 | 24/44 (J82, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.654×** | -8.3 | 1e-14 | 25/48 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.673×** | -7.7 | 1e-12 | 28/47 (A498, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.737×** | -6.0 | 2e-07 | 21/46 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.760×** | -5.4 | 6e-06 | 21/38 (NCI-H1573, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.780×** | -4.9 | 8e-05 | 19/47 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.637×** | -4.6 | 2e-04 | 14/37 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.794×** | -4.5 | 3e-04 | 18/47 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.780×** | -4.5 | 3e-04 | 17/34 (HOP62, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.801×** | -4.4 | 6e-04 | 14/47 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.868× | -3.9 | 0.004 | 18/48 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.817×** | -3.8 | 0.006 | 17/48 (SNU-1, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.827×** | -3.7 | 0.007 | 13/47 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.836× | -3.5 | 0.015 | 12/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.785×** | -3.4 | 0.022 | 4/48 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.746×** | -3.0 | 0.074 | 8/44 (A-427, NCI-H2030, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12172. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 18.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.233× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 13.3 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0766× (z -15.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.262× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 16.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 19.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.351× (z -11.2) |
| [[PANC-1 (line)]] | alt | 18.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -12.7) |
| [[SW480 (line)]] | alt | 17.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.229× (z -14.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.292× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 14.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -8.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 16.2 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.156× (z -8.6) |
| [[C32 (line)]] | wt | 15.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -9.8) |
| [[HOP62 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -12.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 8.93 | 0 | 1 | — | [[Macitentan (drug)]] 5 µM 0.100× (z -8.6) |
| [[J82 (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0622× (z -17.1) ⚠ toxic |
| [[LoVo (line)]] | wt | 15.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 13.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -8.8) |
| [[SHP-77 (line)]] | alt | 23.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 16.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -10.3) |
| [[SNU-1 (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0955× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 9.94 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12172), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF4]] | +0.62 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[TTI1]] | +0.62 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[HAUS6]] | +0.61 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[ZNF384]] | +0.60 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[CNOT9]] | +0.59 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[PIK3R4]] | +0.58 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[MTBP]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[PPIH]] | +0.58 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[PHF12]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[TRAIP]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[FANCM]] | +0.57 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[POC1A]] | +0.57 | +0.56 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP8]] | -0.53 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[NOTCH2NLC]] | -0.53 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[PEA15]] | -0.52 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[LIMS1]] | -0.52 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[KTN1]] | -0.51 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[NOTCH2NLB]] | -0.50 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[SHC2]] | -0.49 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[NPIPB4]] | -0.49 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[SMARCA1]] | -0.49 | -0.37 / -0.43 | both halves | 9e-05 |  |
| [[DNAJC21]] | -0.49 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[KRTAP5-AS1]] | -0.48 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[JUND]] | -0.48 | -0.55 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB20]] | B | RAB20 activity lowers NIF3L1's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 1.30× higher at baseline in the lines without RAB20 | 0.080 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.583). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-30.6, -45.9); signed map (-39.1, -39.3). **Vector** length 72.5, 11.7% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +0.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.9 | +2.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.1 | +2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.2 | +1.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.1 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.0 | -17.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.0 | -9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.5 | -5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.1 | -2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -2.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -1.5 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | NGG1 interacting factor 3 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:200,889,327-200,903,938 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CALS-7, MDS015; previously ALS2CR1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZT8](https://www.uniprot.org/uniprotkb/Q9GZT8) (NIF3-like protein 1):

> May function as a transcriptional corepressor through its interaction with COPS2, negatively regulating the expression of genes involved in neuronal differentiation.

**Summary**, from NCBI Gene [60491](https://www.ncbi.nlm.nih.gov/gene/60491):

> Enables RNA polymerase II-specific DNA-binding transcription factor binding activity and identical protein binding activity. Involved in positive regulation of DNA-templated transcription. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13390](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13390) · Entrez [60491](https://www.ncbi.nlm.nih.gov/gene/60491) · UniProt [Q9GZT8](https://www.uniprot.org/uniprotkb/Q9GZT8) · Ensembl [ENSG00000196290](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196290)

## Data

Gene col 12172: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12172); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12172, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12172]; `tensor/DDL_lfc|DDL_z.npy` [12172]; `embed/gene_vectors.npy` [12172]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12172 or target_col == 12172). Every well: [[NIF3L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NIF3L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
