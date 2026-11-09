---
symbol: "LCA5"
type: "gene"
col: 5686
ensembl_id: "ENSG00000135338"
name: "lebercilin LCA5"
location: "6q14.1"
module: 59
arm: "+"
pooled_cpm: 18.3
n_lines_expressing: 47
n_dd_up: 27
n_dd_down: 8
n_dd_up_clean: 26
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# LCA5

*lebercilin LCA5* — 6q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.04× (z +16.5, q 0e+00, up in 37 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.665× (z -6.6, q 2e-08, down in 25 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C16orf87]] (+0.65, fdr 7e-06), [[KDM5B]] (+0.64, fdr 1e-05), [[ABCA5]] (+0.63, fdr 7e-06); moves opposite to [[EFTUD2]] (-0.64, fdr 7e-06), [[TIMM23B-AGAP6]] (-0.64, fdr 1e-05), [[WDR4]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAM229B]] → it (grade B ⚠); 2 go from it, the strongest it → [[SNX2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 2 with an alert ⚠; shown: the 15 strongest. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5686.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +16.5 | 0e+00 | 37/44 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.60×** | +15.6 | 0e+00 | 40/44 (HT-29, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +15.3 | 0e+00 | 36/43 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.35×** | +13.9 | 5e-42 | 38/45 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.04×** | +11.6 | 4e-29 | 32/45 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.96×** | +11.0 | 5e-26 | 36/45 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +10.9 | 1e-25 | 33/45 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +10.4 | 2e-23 | 33/44 (KATO III, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.85×** | +10.0 | 9e-22 | 30/43 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +9.2 | 2e-18 | 28/43 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +8.3 | 5e-15 | 24/45 (KATO III, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +7.2 | 3e-11 | 26/44 (RKO, A-427, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +6.8 | 6e-10 | 25/44 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +6.4 | 6e-09 | 25/44 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.12×** | +6.4 | 6e-09 | 27/45 (HT-29, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5686.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.665×** | -6.6 | 2e-08 | 25/44 (Hs 766T, CFPAC-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.710×** | -5.6 | 7e-06 | 20/44 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.758×** | -4.5 | 0.001 | 20/38 (NCI-H661, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.782×** | -4.0 | 0.006 | 11/44 (HT-29, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.767×** | -4.0 | 0.006 | 17/34 (SNU-423, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.783×** | -4.0 | 0.006 | 14/42 (LS 180, CHP-212, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.628×** | -4.0 | 0.006 | 17/45 (Hs 766T, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.802×** | -3.4 | 0.040 | 18/30 (NCI-H661, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | 0.695× | -3.1 | 0.11 | 13/43 (A-427, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 0.695× | -3.1 | 0.11 | 10/26 (SW1417, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.700× | -3.0 | 0.12 | 9/41 (RPMI-7951, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5686. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 19.8 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 2.49× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 13.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +11.4) | — |
| [[LS 180 (line)]] | wt | 7.69 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 19.7 | 2 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.82× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.134× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 6.42 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 29.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +11.0) | — |
| [[SW480 (line)]] | alt | 17.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +13.3) | — |
| [[A-172 (line)]] | wt | 14.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +8.8) | — |
| [[A-427 (line)]] | wt | 20.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.51× (z +10.3) | — |
| [[A549 (line)]] | wt | 12.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +9.2) | — |
| [[C32 (line)]] | wt | 13.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +9.3) | — |
| [[COLO 205 (line)]] | alt | 6.17 | 0 | 1 | — | [[Darinaparsin (drug)]] 0.5 µM 0.0654× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +12.8) | — |
| [[hTERT-HPNE (line)]] | wt | 24.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 5.17 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0901× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 19.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 16.9 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.04× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 6.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +8.5) | — |
| [[RKO (line)]] | wt | 24.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.60× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 46.3 | 0 | 1 (1 ⚠) | — | [[Torkinib (drug)]] 5 µM 0.0780× (z -10.1) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 33.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.307× (z -8.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 14.0 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0336× (z -11.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5686), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C16orf87]] | +0.65 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[KDM5B]] | +0.64 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[ABCA5]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[DCAF6]] | +0.63 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[KMT2A]] | +0.62 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[KMT2E]] | +0.62 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[VPS37D]] | +0.61 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[SNX2]] | +0.61 | +0.57 / +0.67 | both halves | 8e-06 |  |
| [[AKAP1-DT]] | +0.60 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[PRKAB2]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[RAB30]] | +0.60 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[MIER1]] | +0.59 | +0.62 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFTUD2]] | -0.64 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[TIMM23B-AGAP6]] | -0.64 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[WDR4]] | -0.63 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[NIPA2]] | -0.62 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[TOMM40]] | -0.60 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[RBM19]] | -0.60 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[EIF2S1]] | -0.60 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[GNL3L]] | -0.59 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[SSU72]] | -0.59 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[EIPR1]] | -0.58 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.58 | -0.57 / -0.59 | both halves | 8e-06 |  |
| [[PUS1]] | -0.58 | -0.45 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM229B]] | B | FAM229B activity raises LCA5's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 2.96× lower at baseline in the lines without FAM229B | 0.054 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT |
| [[MAP2K1]] | B | MAP2K1 activity lowers LCA5's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNX2]] | C | LCA5 activity raises SNX2's level | lines that do not express LCA5 (3) vs lines expressing it (47) | 1.59× lower at baseline in the lines without LCA5 | 0.073 | ⚠ few lines (3 vs 47); across organs; also absent: NXPE3, E2F7, IFT74; maybe low, not absent |
| [[CFAP36]] | C | LCA5 activity raises CFAP36's level | lines that do not express LCA5 (3) vs lines expressing it (47) | 1.81× lower at baseline in the lines without LCA5 | 0.086 | ⚠ few lines (3 vs 47); across organs; also absent: NXPE3, E2F7, IFT74; maybe low, not absent |

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.669). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-3.2, -37.3); signed map (-7.0, 11.4). **Vector** length 91.1, 20.3% of its response variance represented; |z| ≥ 3 in 1,062 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM |  | +6.0 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +10.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +16.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.8 | +8.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.0 | +5.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +4.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +5.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +4.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.5 | +3.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.5 | -5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -6.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.3 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.8 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | -2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | lebercilin LCA5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.1 — chr6:79,484,991-79,537,458 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C6orf152 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VQ0](https://www.uniprot.org/uniprotkb/Q86VQ0) (Lebercilin):

> Involved in intraflagellar protein (IFT) transport in photoreceptor cilia. Plays a role in the ciliary transport of photoreceptors outer segment proteins.

**Summary**, from NCBI Gene [167691](https://www.ncbi.nlm.nih.gov/gene/167691):

> This gene encodes a protein that is thought to be involved in centrosomal or ciliary functions. Mutations in this gene cause Leber congenital amaurosis type V. Alternatively spliced transcript variants are described. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:31923](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31923) · Entrez [167691](https://www.ncbi.nlm.nih.gov/gene/167691) · UniProt [Q86VQ0](https://www.uniprot.org/uniprotkb/Q86VQ0) · Ensembl [ENSG00000135338](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135338)

## Data

Gene col 5686: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5686); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5686, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5686]; `tensor/DDL_lfc|DDL_z.npy` [5686]; `embed/gene_vectors.npy` [5686]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5686 or target_col == 5686). Every well: [[LCA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LCA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
