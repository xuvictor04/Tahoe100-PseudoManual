---
symbol: "MAPKAPK3"
type: "gene"
col: 3578
ensembl_id: "ENSG00000114738"
name: "MAPK activated protein kinase 3"
location: "3p21.2"
module: 4
arm: "+"
pooled_cpm: 11.44
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 10
n_dd_up_clean: 15
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# MAPKAPK3

*MAPK activated protein kinase 3* — 3p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.69× (z +16.1, q 0e+00, up in 30 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.49× (z +6.5, q 1e-08, up in 23 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.612× (z -11.3, q 5e-27, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STK25]] (+0.72, fdr 7e-06), [[BOP1]] (+0.69, fdr 7e-06), [[TTLL12]] (+0.68, fdr 1e-05); moves opposite to [[ARID4B]] (-0.67, fdr 7e-06), [[TERF2IP]] (-0.64, fdr 7e-06), [[NDUFC1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SACS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3578.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.69×** | +16.1 | 0e+00 | 30/33 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +15.3 | 0e+00 | 14/16 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.43×** | +13.4 | 2e-38 | 21/25 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +7.5 | 8e-12 | 24/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +6.5 | 1e-08 | 23/44 (PANC-1, HOP62, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +6.3 | 4e-08 | 17/46 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +5.9 | 4e-07 | 13/37 (NCI-H2347, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +4.8 | 9e-05 | 13/47 (PANC-1, C32, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +4.8 | 1e-04 | 13/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.34×** | +4.7 | 1e-04 | 10/44 (NCI-H460, NCI-H1573, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.73×** | +4.6 | 2e-04 | 6/43 (SW1417, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.69×** | +4.5 | 4e-04 | 14/43 (SK-MEL-2, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +4.3 | 7e-04 | 10/47 (HOP62, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.64×** | +4.2 | 0.001 | 7/44 (Hs 766T, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.20× | +4.1 | 0.001 | 11/48 (SW480, HT-29, …) | two highest doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.56×** | +3.8 | 0.006 | 3/43 (RKO, SW1417, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.007 | 10/45 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.013 | 5/47 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +3.5 | 0.013 | 10/48 (A-172, NCI-H1792, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.013 | 7/46 (SNU-423, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3578.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.612×** | -11.3 | 5e-27 | 32/45 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.744×** | -6.8 | 2e-09 | 25/46 (NCI-H23, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.720×** | -5.2 | 4e-05 | 21/44 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trimetrexate (drug)]] 5 µM |  | **0.823×** | -4.5 | 9e-04 | 12/47 (LOX-IMVI, RKO, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.769×** | -4.3 | 0.002 | 18/44 (A549, A498, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.780×** | -4.1 | 0.004 | 14/46 (A-427, HOP62, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.777×** | -4.0 | 0.006 | 16/46 (NCI-H23, SNU-1, …) | top dose only | composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **0.800×** | -3.9 | 0.007 | 7/48 (HEC-1-A, AN3 CA, …) | all doses, flat | noisy plate (z scaled) |
| [[Bergenin (drug)]] 0.5 µM |  | **0.809×** | -3.5 | 0.032 | 10/45 (Hs 766T, SNU-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.869× | -3.2 | 0.082 | 6/48 (HEC-1-A, SW480, …) | all doses, flat |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | **0.829×** | -3.1 | 0.098 | 6/47 (hTERT-HPNE, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.704× | -3.0 | 0.13 | 7/46 (HEC-1-A, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3578. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 22.3 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +10.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -12.2) |
| [[HEC-1-A (line)]] | alt | 40.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.64× (z +10.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 28.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +10.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 5.27 | 0 | 2 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0985× (z -8.9) |
| [[A549 (line)]] | wt | 5.42 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0858× (z -10.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 8.78 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0489× (z -13.3) |
| [[C-33 A (line)]] | alt | 9.75 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0841× (z -8.9) ⚠ cell-cycle shift, explains ~6% of this change |
| [[LoVo (line)]] | wt | 12.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.26× (z +12.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 10.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.33× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 7.20 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.107× (z -9.7) ⚠ cell-cycle shift, explains ~14% of this change |
| [[RKO (line)]] | wt | 26.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -8.8) |
| [[SW 900 (line)]] | alt | 7.20 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0773× (z -9.8) |
| [[A-172 (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3578), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK25]] | +0.72 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[BOP1]] | +0.69 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[TTLL12]] | +0.68 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[PGAM5]] | +0.67 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[SLC19A1]] | +0.66 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[ADAMTSL5]] | +0.65 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[NBEAL2]] | +0.63 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[NLE1]] | +0.62 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[PRPF19]] | +0.62 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[ATP13A2]] | +0.62 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ITPR3]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 | pathway: Signaling by VEGF |
| [[SLC48A1]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID4B]] | -0.67 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[TERF2IP]] | -0.64 | -0.59 / -0.58 | both halves | 7e-06 | pathway: Cellular Senescence |
| [[NDUFC1]] | -0.64 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[RSF1]] | -0.61 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[GTF2IRD2B]] | -0.61 | -0.68 / -0.42 | both halves | 4e-05 |  |
| [[SYNRG]] | -0.60 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ASH1L]] | -0.59 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[B2M]] | -0.59 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[PSME2]] | -0.58 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[DLEU2]] | -0.57 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[TESK2]] | -0.57 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[SMIM14]] | -0.57 | -0.58 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SACS]] | B | SACS activity raises MAPKAPK3's level | lines that do not express SACS (5) vs lines expressing it (45) | 1.79× lower at baseline in the lines without SACS | 0.011 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[SLC4A3]] | B | SLC4A3 activity raises MAPKAPK3's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 1.38× lower at baseline in the lines without SLC4A3 | 0.091 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.602). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-10.0, -28.1); signed map (-27.2, -45.5). **Vector** length 81.3, 14.7% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.8 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +16.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +13.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.8 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +6.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.9 | +4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +4.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +4.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.7 | -6.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -5.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.4 | -3.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.2 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -2.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | MAPK activated protein kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.2 — chr3:50,611,520-50,649,291 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 3pK, MAPKAP3, 3PK, MK-3, MK3 |
| Gene groups (HGNC) | MAPK activated protein kinases; MAPKAPK family |
| Hallmark sets | P53_PATHWAY |
| Reactome | 34 pathways, smallest: p38MAPK events; Signalling to RAS; activated TAK1 mediates p38 MAPK activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16644](https://www.uniprot.org/uniprotkb/Q16644) (MAP kinase-activated protein kinase 3):

> Stress-activated serine/threonine-protein kinase involved in cytokines production, endocytosis, cell migration, chromatin remodeling and transcriptional regulation. Following stress, it is phosphorylated and activated by MAP kinase p38-alpha/MAPK14, leading to phosphorylation of substrates. Phosphorylates serine in the peptide sequence, Hyd-X-R-X(2)-S, where Hyd is a large hydrophobic residue. MAPKAPK2 and MAPKAPK3, share the same function and substrate specificity, but MAPKAPK3 kinase activity …

**Summary**, from NCBI Gene [7867](https://www.ncbi.nlm.nih.gov/gene/7867):

> This gene encodes a member of the Ser/Thr protein kinase family. This kinase functions as a mitogen-activated protein kinase (MAP kinase)- activated protein kinase. MAP kinases are also known as extracellular signal-regulated kinases (ERKs), act as an integration point for multiple biochemical signals. This kinase was shown to be activated by growth inducers and stress stimulation of cells. In vitro studies demonstrated that ERK, p38 MAP kinase and Jun N-terminal kinase were all able to …

**Accessions** — [HGNC:6888](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6888) · Entrez [7867](https://www.ncbi.nlm.nih.gov/gene/7867) · UniProt [Q16644](https://www.uniprot.org/uniprotkb/Q16644) · Ensembl [ENSG00000114738](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114738)

## Data

Gene col 3578: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3578); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3578, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3578]; `tensor/DDL_lfc|DDL_z.npy` [3578]; `embed/gene_vectors.npy` [3578]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3578 or target_col == 3578). Every well: [[MAPKAPK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPKAPK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
