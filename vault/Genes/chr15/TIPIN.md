---
symbol: "TIPIN"
type: "gene"
col: 1100
ensembl_id: "ENSG00000075131"
name: "TIMELESS interacting protein"
location: "15q22.31"
module: 10
arm: "+"
pooled_cpm: 14.28
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# TIPIN

*TIMELESS interacting protein* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.16× (z +18.3, q 0e+00, up in 39 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Azithromycin (hydrate) (drug)]] 0.5 µM in 1 line (SNU-1 0.0802×); [[Pimozide (drug)]] 0.05 µM in 1 line (BT-474 0.104×); [[Tadalafil (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0711×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRR3]] (+0.58, fdr 1e-04), [[CTTN-DT]] (+0.58, fdr 4e-05), [[YARS2]] (+0.57, fdr 8e-05); moves opposite to [[SESN3]] (-0.51, fdr 3e-04), [[GNB2]] (-0.48, fdr 2e-04), [[PIP5K1C]] (-0.47, fdr 3e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CLU]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1100.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +18.3 | 0e+00 | 39/46 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.66×** | +15.3 | 0e+00 | 37/42 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.51×** | +14.3 | 3e-44 | 23/32 (NCI-H1573, LoVo, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.71×** | +11.5 | 1e-28 | 42/48 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +11.0 | 3e-26 | 35/47 (J82, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +9.8 | 2e-20 | 31/47 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.75×** | +9.5 | 3e-19 | 37/48 (LoVo, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.65×** | +8.4 | 3e-15 | 32/48 (LoVo, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +7.9 | 1e-13 | 27/47 (SHP-77, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +7.9 | 1e-13 | 27/45 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +7.1 | 5e-11 | 25/48 (HOP62, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +7.1 | 8e-11 | 25/47 (LoVo, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.50×** | +6.9 | 3e-10 | 21/39 (NCI-H460, SNU-423, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.49×** | +6.7 | 7e-10 | 28/47 (A549, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +6.3 | 1e-08 | 23/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.18× | +4.1 | 0.001 | 10/48 (PANC-1, RPMI-7951, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +3.9 | 0.002 | 14/43 (HS-578T, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.55×** | +3.8 | 0.003 | 5/46 (A549, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.24×** | +3.5 | 0.012 | 10/48 (SW480, CFPAC-1, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **1.48×** | +3.5 | 0.012 | 6/45 (CFPAC-1, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.014 | 0/48 | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1100.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Azithromycin (hydrate) (drug)]] 0.5 µM in 1 line (SNU-1 0.0802×); [[Pimozide (drug)]] 0.05 µM in 1 line (BT-474 0.104×); [[Tadalafil (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0711×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.927× | -4.2 | 0.013 | 4/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Pentagastrin (drug)]] 5 µM |  | 0.863× | -3.5 | 0.14 | 7/48 (SNU-1, CFPAC-1, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.822× | -3.3 | 0.20 | 9/47 (SNU-423, A-427, …) | two highest doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1100. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.28× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +8.5) | — |
| [[A-172 (line)]] | wt | 14.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change |
| [[hTERT-HPNE (line)]] | wt | 10.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +8.5) | [[Tadalafil (drug)]] 5 µM 0.0711× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 9.03 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 10.1× (z +11.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 17.5 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.57× (z +11.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +8.5) | — |
| [[A549 (line)]] | wt | 12.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +10.7) | — |
| [[AsPC-1 (line)]] | alt | 5.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.21× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 8.43 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.104× (z -9.5) |
| [[C32 (line)]] | wt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.35× (z +9.8) | — |
| [[H4 (line)]] | wt | 15.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.88× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.47× (z +14.1) | — |
| [[HS-578T (line)]] | alt | 9.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.24× (z +12.6) | — |
| [[LoVo (line)]] | wt | 10.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.57× (z +9.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 9.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +10.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 13.4 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 6.59× (z +10.1) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 12.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.35× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 27.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.16× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 19.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +10.4) | — |
| [[SNU-1 (line)]] | wt | 12.0 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0802× (z -9.9) |
| [[SW 900 (line)]] | alt | 11.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +9.1) | — |
| [[A-427 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1100), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR3]] | +0.58 | +0.59 / +0.36 | both halves | 1e-04 |  |
| [[CTTN-DT]] | +0.58 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[YARS2]] | +0.57 | +0.56 / +0.37 | both halves | 8e-05 |  |
| [[FBXO4]] | +0.57 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[FAM120C]] | +0.57 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[THBS4]] | +0.56 | +0.58 / +0.28 | both halves | 3e-04 |  |
| [[TEX22]] | +0.56 | +0.50 / +0.36 | both halves | 9e-05 |  |
| [[SLC16A1-AS1]] | +0.55 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[ZNF26]] | +0.55 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[COX10-DT]] | +0.55 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[TMEM186]] | +0.55 | +0.56 / +0.36 | both halves | 1e-04 |  |
| [[CCNT2]] | +0.55 | +0.47 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SESN3]] | -0.51 | -0.28 / -0.32 | both halves | 3e-04 |  |
| [[GNB2]] | -0.48 | -0.56 / -0.29 | both halves | 2e-04 |  |
| [[PIP5K1C]] | -0.47 | -0.40 / -0.28 | both halves | 3e-04 |  |
| [[LIFR]] | -0.47 | -0.43 / -0.26 | both halves | 4e-04 |  |
| [[TAOK3]] | -0.46 | -0.26 / -0.33 | both halves | 3e-04 |  |
| [[CHP1]] | -0.46 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[RAPGEF2]] | -0.46 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[ABCD3]] | -0.46 | -0.33 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLU]] | B | CLU activity raises TIPIN's level | lines that do not express CLU (11) vs lines expressing it (39) | 1.41× lower at baseline in the lines without CLU | 0.020 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.445). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-1.9, 18.7); signed map (28.1, -16.5). **Vector** length 61.7, 9.30% of its response variance represented; |z| ≥ 3 in 985 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.1 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +14.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +9.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +18.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +6.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +1.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.8 | +3.0 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | +1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -1.7 | +3.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -0.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.2 | -1.6 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | TIMELESS interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:66,336,191-66,386,746 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20516 |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes |
| Hallmark sets | E2F_TARGETS |
| Reactome | 5 pathways, smallest: Processing of DNA double-strand break ends; HDR through Homologous Recombination (HRR) or Single Strand Annealing (SSA); Homology Directed Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVW5](https://www.uniprot.org/uniprotkb/Q9BVW5) (TIMELESS-interacting protein):

> Plays an important role in the control of DNA replication and the maintenance of replication fork stability. Important for cell survival after DNA damage or replication stress. May be specifically required for the ATR-CHEK1 pathway in the replication checkpoint induced by hydroxyurea or ultraviolet light. Forms a complex with TIMELESS and this complex regulates DNA replication processes under both normal and stress conditions, stabilizes replication forks and influences both CHEK1 …

**Summary**, from NCBI Gene [54962](https://www.ncbi.nlm.nih.gov/gene/54962):

> The protein encoded by this gene is part of the replisome complex, a group of proteins that support DNA replication. It binds TIM, which is involved in circadian rhythm regulation, and aids in protecting cells against DNA damage and stress. Two pseudogenes and two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:30750](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30750) · Entrez [54962](https://www.ncbi.nlm.nih.gov/gene/54962) · UniProt [Q9BVW5](https://www.uniprot.org/uniprotkb/Q9BVW5) · Ensembl [ENSG00000075131](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075131)

## Data

Gene col 1100: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1100); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1100, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1100]; `tensor/DDL_lfc|DDL_z.npy` [1100]; `embed/gene_vectors.npy` [1100]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1100 or target_col == 1100). Every well: [[TIPIN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIPIN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
