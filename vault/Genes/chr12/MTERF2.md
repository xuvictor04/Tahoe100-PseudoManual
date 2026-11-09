---
symbol: "MTERF2"
type: "gene"
col: 4225
ensembl_id: "ENSG00000120832"
name: "mitochondrial transcription termination factor 2"
location: "12q23.3"
module: 199
arm: "+"
pooled_cpm: 9.56
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/199"]
generated_by: "tahoemap"
---

# MTERF2

*mitochondrial transcription termination factor 2* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.27× (z +25.3, q 0e+00, up in 39 of 45 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Betamethasone dipropionate (drug)]] 0.5 µM in 1 line (C32 0.0573×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CFPAC-1 0.109×); [[Drospirenone (drug)]] 0.05 µM in 1 line (NCI-H2347 0.173×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GALC]] (+0.63, fdr 5e-05), [[ZNF428]] (+0.58, fdr 2e-05), [[PMPCB]] (+0.58, fdr 6e-05); moves opposite to [[C11orf24]] (-0.57, fdr 1e-05), [[ARPC5L]] (-0.53, fdr 1e-04), [[MYO9B]] (-0.53, fdr 3e-05).
> It is in [[Module 199]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KLHL14]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4225.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.27×** | +25.3 | 0e+00 | 39/45 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.10×** | +11.2 | 2e-26 | 38/47 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.99×** | +10.4 | 5e-23 | 32/47 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.96×** | +10.1 | 8e-22 | 36/47 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +8.5 | 2e-15 | 28/46 (AsPC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.74×** | +8.0 | 9e-14 | 27/46 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +7.9 | 3e-13 | 27/48 (A498, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +6.8 | 6e-10 | 24/45 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +5.9 | 3e-07 | 18/38 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +5.9 | 3e-07 | 15/47 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +5.5 | 2e-06 | 20/47 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +4.8 | 6e-05 | 13/27 (NCI-H460, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.001 | 10/48 (A498, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.001 | 16/47 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.67×** | +4.0 | 0.002 | 13/47 (NCI-H460, SW 900, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.010 | 9/47 (BT-474, SW480, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.40×** | +3.6 | 0.010 | 3/47 (NCI-H460, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4225.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Betamethasone dipropionate (drug)]] 0.5 µM in 1 line (C32 0.0573×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CFPAC-1 0.109×); [[Drospirenone (drug)]] 0.05 µM in 1 line (NCI-H2347 0.173×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.818× | -3.0 | 0.68 | 5/47 (A-427, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4225. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 9.37 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +17.5) | — |
| [[C32 (line)]] | wt | 5.97 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.60× (z +9.5) | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.0573× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 13.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +13.7) | — |
| [[A498 (line)]] | wt | 7.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +12.9) | — |
| [[AsPC-1 (line)]] | alt | 6.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.06× (z +12.1) | — |
| [[CFPAC-1 (line)]] | alt | 4.59 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.109× (z -9.1) |
| [[COLO 205 (line)]] | alt | 6.75 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.43× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 7.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +10.0) | — |
| [[HS-578T (line)]] | alt | 5.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.47× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 8.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 8.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.35× (z +10.2) | — |
| [[J82 (line)]] | alt | 9.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +10.3) | — |
| [[KATO III (line)]] | alt | 6.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +9.3) | — |
| [[LoVo (line)]] | wt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +14.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 11.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.83× (z +15.7) | — |
| [[NCI-H23 (line)]] | alt | 12.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +12.1) | — |
| [[NCI-H2347 (line)]] | alt | 5.39 | 0 | 1 | — | [[Drospirenone (drug)]] 0.05 µM 0.173× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 6.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 7.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.31× (z +11.7) | — |
| [[SNU-423 (line)]] | alt | 8.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.72× (z +13.8) | — |
| [[SW480 (line)]] | alt | 9.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.0) | — |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4225), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALC]] | +0.63 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[ZNF428]] | +0.58 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[PMPCB]] | +0.58 | +0.64 / +0.38 | both halves | 6e-05 |  |
| [[CHD3]] | +0.58 | +0.61 / +0.31 | both halves | 2e-04 |  |
| [[SNX16]] | +0.58 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[KRBA2]] | +0.56 | +0.68 / +0.37 | both halves | 8e-05 |  |
| [[POLR2M]] | +0.56 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[SMARCA1]] | +0.56 | +0.46 / +0.35 | both halves | 1e-04 |  |
| [[HPS1]] | +0.56 | +0.68 / +0.28 | both halves | 3e-04 |  |
| [[CC2D2A]] | +0.55 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[CYB5D2]] | +0.55 | +0.62 / +0.39 | both halves | 6e-05 |  |
| [[BDH2]] | +0.54 | +0.64 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf24]] | -0.57 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[ARPC5L]] | -0.53 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[MYO9B]] | -0.53 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[HM13]] | -0.53 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[SDHAF1]] | -0.53 | -0.49 / -0.32 | both halves | 1e-04 |  |
| [[ELOVL1]] | -0.52 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[SLC27A4]] | -0.51 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[TMEM104]] | -0.51 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[FRMD8]] | -0.51 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[ZMYND19]] | -0.51 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[SRGAP2C]] | -0.51 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[TMEM184B]] | -0.51 | -0.59 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLHL14]] | B | KLHL14 activity raises MTERF2's level | lines that do not express KLHL14 (37) vs lines expressing it (13) | 1.33× lower at baseline in the lines without KLHL14 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 199]]; 16 genes; every member is in the + arm (projection on the module's main direction -0.499). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.0, 5.2); signed map (15.4, -19.0). **Vector** length 47.5, 5.45% of its response variance represented; |z| ≥ 3 in 932 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +25.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.6 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.3 | +1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +2.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.6 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.3 | +2.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -1.9 | +10.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.8 | +10.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -1.8 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.6 | +11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.1 | +1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.0 | +2.6 |
|  | [[vincristine (drug)]] 0.05 µM |  | -0.8 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.7 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial transcription termination factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:106,973,120-106,987,163 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14062; previously MTERFD3 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q49AM1](https://www.uniprot.org/uniprotkb/Q49AM1) (Transcription termination factor 2, mitochondrial):

> Binds mitochondrial DNA and plays a role in the regulation of transcription of mitochondrial mRNA and rRNA species.

**Summary**, from NCBI Gene [80298](https://www.ncbi.nlm.nih.gov/gene/80298):

> Enables DNA binding activity. Predicted to be involved in termination of mitochondrial transcription. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30779](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30779) · Entrez [80298](https://www.ncbi.nlm.nih.gov/gene/80298) · UniProt [Q49AM1](https://www.uniprot.org/uniprotkb/Q49AM1) · Ensembl [ENSG00000120832](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120832)

## Data

Gene col 4225: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4225); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4225, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4225]; `tensor/DDL_lfc|DDL_z.npy` [4225]; `embed/gene_vectors.npy` [4225]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4225 or target_col == 4225). Every well: [[MTERF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTERF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
