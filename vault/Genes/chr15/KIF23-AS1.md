---
symbol: "KIF23-AS1"
type: "gene"
col: 15198
ensembl_id: "ENSG00000259426"
name: "KIF23 and PAQR5 antisense RNA 1"
location: "15q23"
module: 120
arm: "+"
pooled_cpm: 4.85
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 14
n_dd_up_clean: 10
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# KIF23-AS1

*KIF23 and PAQR5 antisense RNA 1* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.70× (z +12.1, q 5e-31, up in 28 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.650× (z -5.3, q 7e-05, down in 20 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARVA]] (+0.49, fdr 3e-05), [[LATS2]] (+0.49, fdr 3e-05), [[GLIPR1]] (+0.49, fdr 3e-05); moves opposite to [[RBIS]] (-0.45, fdr 8e-05), [[PRRG1]] (-0.43, fdr 1e-04), [[SH3PXD2B]] (-0.42, fdr 1e-04).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15198.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.70×** | +12.1 | 5e-31 | 28/38 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.48×** | +11.1 | 4e-26 | 23/38 (Hs 766T, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +5.0 | 1e-04 | 11/28 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +4.9 | 1e-04 | 1/7 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **1.65×** | +4.2 | 0.003 | 12/44 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.42×** | +4.1 | 0.003 | 10/44 (NCI-H460, SNU-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +3.9 | 0.008 | 13/45 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +3.8 | 0.009 | 2/12 (PANC-1, HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +3.8 | 0.009 | 2/21 (HS-578T, hTERT-HPNE) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **1.57×** | +3.8 | 0.010 | 8/42 (C32, A-172, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.54×** | +3.7 | 0.010 | 9/43 (HepG2/C3A, NCI-H460, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.48×** | +3.5 | 0.019 | 6/45 (HEC-1-A, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.052 | 9/44 (SNU-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15198.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.650×** | -5.3 | 7e-05 | 20/45 (SK-MEL-2, A498, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.554×** | -5.1 | 9e-05 | 20/32 (J82, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.587×** | -4.6 | 7e-04 | 16/44 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.601×** | -4.4 | 0.001 | 14/45 (NCI-H460, SNU-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.606×** | -4.3 | 0.001 | 19/42 (HepG2/C3A, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.595×** | -4.3 | 0.001 | 17/41 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.598×** | -4.3 | 0.001 | 16/29 (NCI-H1573, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.635×** | -3.9 | 0.006 | 17/42 (SW1417, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.652×** | -3.7 | 0.013 | 14/45 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.657×** | -3.6 | 0.015 | 18/43 (SNU-423, SK-MEL-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.659×** | -3.6 | 0.015 | 16/44 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.669×** | -3.5 | 0.023 | 15/42 (A498, SNU-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.675×** | -3.4 | 0.028 | 14/43 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.684×** | -3.3 | 0.040 | 12/45 (HepG2/C3A, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15198. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 16.4 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0250× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0391× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 12.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0861× (z -10.5) |
| [[J82 (line)]] | alt | 10.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0648× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 3.73 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0540× (z -8.6) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0689× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 3.29 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0827× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15198), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARVA]] | +0.49 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[LATS2]] | +0.49 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[GLIPR1]] | +0.49 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[MYOF]] | +0.47 | +0.43 / +0.41 | both halves | 4e-05 |  |
| [[ZNF644]] | +0.47 | +0.53 / +0.36 | both halves | 1e-04 |  |
| [[GPR176]] | +0.46 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[GEN1]] | +0.46 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[LANCL2]] | +0.46 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[ACTR3-AS1]] | +0.45 | +0.49 / +0.41 | both halves | 4e-05 | same gene group |
| [[ZNF93]] | +0.45 | +0.34 / +0.43 | both halves | 1e-04 |  |
| [[DDAH1]] | +0.45 | +0.50 / +0.38 | both halves | 6e-05 |  |
| [[CCN2]] | +0.45 | +0.50 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBIS]] | -0.45 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[PRRG1]] | -0.43 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[SH3PXD2B]] | -0.42 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[ABHD6]] | -0.42 | -0.29 / -0.40 | both halves | 3e-04 |  |
| [[MKNK2]] | -0.41 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[STX6]] | -0.41 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[RNF149]] | -0.41 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[MFSD9]] | -0.41 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[BEX4]] | -0.41 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[MARK3]] | -0.41 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[FLYWCH1]] | -0.40 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[CARD19]] | -0.40 | -0.45 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers KIF23-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF93]] | B | ZNF93 activity lowers KIF23-AS1's level | lines that do not express ZNF93 (21) vs lines expressing it (29) | 1.49× higher at baseline in the lines without ZNF93 | 0.051 | ⚠ within organs, on part of the lines; also absent: ZNF665, ZNF682, ZNF347 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.366). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.9, 17.0); signed map (48.8, 14.6). **Vector** length 81.3, 15.1% of its response variance represented; |z| ≥ 3 in 1,076 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +12.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +3.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.1 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +0.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.0 | -4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.5 | -3.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -3.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | KIF23 and PAQR5 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q23 — chr15:69,396,904-69,415,029 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27075](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27075) · Entrez [145694](https://www.ncbi.nlm.nih.gov/gene/145694) · Ensembl [ENSG00000259426](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259426)

## Data

Gene col 15198: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15198); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15198, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15198]; `tensor/DDL_lfc|DDL_z.npy` [15198]; `embed/gene_vectors.npy` [15198]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15198 or target_col == 15198). Every well: [[KIF23-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF23-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
