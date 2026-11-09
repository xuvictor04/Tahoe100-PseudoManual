---
symbol: "CLBA1"
type: "gene"
col: 6373
ensembl_id: "ENSG00000140104"
name: "clathrin binding box of aftiphilin containing 1"
location: "14q32.33"
module: 12
arm: "+"
pooled_cpm: 5.16
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 10
n_dd_up_clean: 18
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# CLBA1

*clathrin binding box of aftiphilin containing 1* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.01× (z +13.6, q 1e-39, up in 29 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.591× (z -7.3, q 2e-10, down in 20 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.665× (z -5.6, q 5e-06, down in 15 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF408]] (+0.58, fdr 3e-05), [[OSCP1]] (+0.56, fdr 1e-05), [[METTL25B]] (+0.55, fdr 1e-04); moves opposite to [[KPNB1]] (-0.55, fdr 1e-05), [[TBC1D1]] (-0.53, fdr 2e-05), [[PTGES3]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF350]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6373.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.01×** | +13.6 | 1e-39 | 29/39 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.65×** | +13.5 | 8e-39 | 39/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.41×** | +12.2 | 8e-32 | 35/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.30×** | +11.5 | 2e-28 | 34/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +11.4 | 7e-28 | 26/40 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.72×** | +10.5 | 5e-24 | 25/45 (NCI-H2030, HT-29, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +9.4 | 3e-19 | 21/33 (MIA PaCa-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +8.2 | 1e-14 | 1/9 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +6.9 | 4e-10 | 15/38 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.56×** | +5.9 | 2e-07 | 13/43 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.48×** | +5.4 | 3e-06 | 11/47 (MIA PaCa-2, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +5.3 | 7e-06 | 5/15 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +5.2 | 1e-05 | 10/29 (HCT15, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +4.6 | 2e-04 | 8/47 (SHP-77, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.4 | 5e-04 | 10/39 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +4.3 | 7e-04 | 14/43 (A-427, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.010 | 5/40 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.012 | 0/47 | top dose only |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.016 | 9/41 (RKO, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6373.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.591×** | -7.3 | 2e-10 | 20/39 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.665×** | -5.6 | 5e-06 | 15/47 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.693×** | -5.1 | 8e-05 | 14/44 (Panc 03.27, LOX-IMVI, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.700×** | -4.9 | 1e-04 | 14/45 (LOX-IMVI, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.909× | -4.7 | 2e-04 | 9/48 (NCI-H2030, LoVo, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.712×** | -4.7 | 2e-04 | 10/43 (HS-578T, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.720×** | -4.5 | 5e-04 | 14/45 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.764×** | -3.7 | 0.014 | 15/45 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.635×** | -3.3 | 0.062 | 4/35 (C-33 A, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.782×** | -3.3 | 0.062 | 10/31 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 0.5 µM |  | **0.792×** | -3.2 | 0.065 | 8/43 (LS 180, SW48, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6373. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 4.01 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0652× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 3.45 | 0 | 2 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0708× (z -10.5) |
| [[A549 (line)]] | wt | 5.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.00× (z +10.1) | — |
| [[BT-474 (line)]] | alt | 5.06 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 5 µM 0.0523× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 5.24 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[KATO III (line)]] | alt | 4.55 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0597× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 5.01 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0794× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[NCI-H2030 (line)]] | alt | 7.41 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 6.77 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.101× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 3.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +8.8) | — |
| [[SW48 (line)]] | wt | 11.0 | 0 | 1 | — | [[Altretamine (drug)]] 5 µM 0.0716× (z -8.7) |
| [[SW480 (line)]] | alt | 4.88 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -9.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6373), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF408]] | +0.58 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[OSCP1]] | +0.56 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[METTL25B]] | +0.55 | +0.72 / +0.36 | both halves | 1e-04 |  |
| [[ZNF213]] | +0.55 | +0.73 / +0.35 | both halves | 1e-04 |  |
| [[TPRN]] | +0.55 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[STK16]] | +0.54 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[TJAP1]] | +0.54 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[YJU2B]] | +0.54 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ZNF446]] | +0.52 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[HARBI1]] | +0.51 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[RIN1]] | +0.51 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[TOGARAM1]] | +0.51 | +0.46 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNB1]] | -0.55 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[TBC1D1]] | -0.53 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[PTGES3]] | -0.51 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[LDHB]] | -0.51 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[ELOVL5]] | -0.50 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[SYTL4]] | -0.50 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[KPNA3]] | -0.49 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[ARHGEF26]] | -0.49 | -0.54 / -0.21 | both halves | 7e-04 |  |
| [[TNPO1]] | -0.49 | -0.25 / -0.48 | both halves | 4e-04 |  |
| [[ENAH]] | -0.48 | -0.15 / -0.53 | ⚠ one half (not replicated) | 0.001 |  |
| [[ME2]] | -0.48 | -0.39 / -0.37 | both halves | 9e-05 |  |
| [[TXN]] | -0.48 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[MAPK9]] | -0.48 | -0.55 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF350]] | B | ZNF350 activity lowers CLBA1's level | lines that do not express ZNF350 (7) vs lines expressing it (43) | 1.40× higher at baseline in the lines without ZNF350 | 0.042 | ⚠ within organs, on part of the lines |
| [[MAGEA4-AS1]] | B | MAGEA4-AS1 activity raises CLBA1's level | lines that do not express MAGEA4-AS1 (41) vs lines expressing it (9) | 1.41× lower at baseline in the lines without MAGEA4-AS1 | 0.098 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.403). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-33.4, 2.1); signed map (-7.3, -3.6). **Vector** length 51.6, 6.37% of its response variance represented; |z| ≥ 3 in 980 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.1 | +10.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +13.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +9.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.7 | +6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +1.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.3 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +1.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -2.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.4 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -4.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | +1.3 |

## What is on record

|  |  |
|---|---|
| Name | clathrin binding box of aftiphilin containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:104,985,775-105,010,482 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C14orf79 |
| Matched by | ensembl_id |

UniProt [Q96F83](https://www.uniprot.org/uniprotkb/Q96F83) carries no function annotation.

**Summary**, from NCBI Gene [122616](https://www.ncbi.nlm.nih.gov/gene/122616):

> Predicted to enable clathrin binding activity. Predicted to be part of AP-1 adaptor complex. Predicted to be active in trans-Golgi network membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20126](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20126) · Entrez [122616](https://www.ncbi.nlm.nih.gov/gene/122616) · UniProt [Q96F83](https://www.uniprot.org/uniprotkb/Q96F83) · Ensembl [ENSG00000140104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140104)

## Data

Gene col 6373: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6373); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6373, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6373]; `tensor/DDL_lfc|DDL_z.npy` [6373]; `embed/gene_vectors.npy` [6373]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6373 or target_col == 6373). Every well: [[CLBA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLBA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
