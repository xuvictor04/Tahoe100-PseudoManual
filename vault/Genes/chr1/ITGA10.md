---
symbol: "ITGA10"
type: "gene"
col: 6680
ensembl_id: "ENSG00000143127"
name: "integrin subunit alpha 10"
location: "1q21.1"
module: 98
arm: "+"
pooled_cpm: 7.93
n_lines_expressing: 41
n_dd_up: 39
n_dd_down: 10
n_dd_up_clean: 29
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 9
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# ITGA10

*integrin subunit alpha 10* — 1q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.51× (z +19.8, q 0e+00, up in 23 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.575× (z -5.2, q 1e-04, down in 20 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOXC2]] (+0.74, fdr 7e-06), [[TOP1]] (+0.70, fdr 7e-06), [[RIPOR2]] (+0.70, fdr 7e-06); moves opposite to [[SIRLNT]] (-0.57, fdr 1e-05), [[CD5L]] (-0.57, fdr 1e-05), [[ADAMTS16]] (-0.55, fdr 1e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ABCA6]] → it (grade B ⚠); 9 go from it, the strongest it → [[FGD4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6680.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.51×** | +19.8 | 0e+00 | 23/31 (HEC-1-A, PANC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | **2.86×** | +13.8 | 6e-41 | 24/33 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **3.44×** | +11.5 | 3e-28 | 22/33 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **3.42×** | +10.6 | 7e-24 | 20/32 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.99×** | +10.2 | 4e-22 | 24/35 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **2.10×** | +9.7 | 2e-20 | 27/37 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.85×** | +9.7 | 2e-20 | 26/36 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **2.79×** | +9.5 | 1e-19 | 24/35 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **2.65×** | +9.0 | 1e-17 | 23/35 (NCI-H1792, Hs 766T, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.56×** | +8.4 | 2e-15 | 6/11 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dexamethasone (drug)]] 0.05 µM |  | **2.46×** | +8.3 | 4e-15 | 24/36 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.50×** | +8.2 | 1e-14 | 23/35 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **2.29×** | +7.7 | 6e-13 | 22/37 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **2.22×** | +7.4 | 7e-12 | 23/37 (NCI-H1792, Hs 766T, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **2.17×** | +7.2 | 3e-11 | 24/37 (NCI-H1792, Hs 766T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **2.14×** | +7.1 | 6e-11 | 21/36 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **2.13×** | +7.0 | 8e-11 | 22/37 (NCI-H1792, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6680.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.575×** | -5.2 | 1e-04 | 20/36 (SNU-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.654×** | -4.2 | 0.005 | 14/38 (SNU-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.629×** | -4.2 | 0.005 | 13/35 (SNU-1, SK-MEL-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.703×** | -4.2 | 0.005 | 11/37 (SNU-1, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.650×** | -4.1 | 0.005 | 15/38 (SNU-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.692×** | -3.5 | 0.040 | 9/37 (SNU-1, NCI-H2030, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.672×** | -3.5 | 0.040 | 15/37 (SNU-1, C32, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.704×** | -3.3 | 0.062 | 17/37 (NCI-H2030, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.789×** | -3.2 | 0.099 | 13/37 (SNU-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.719×** | -3.1 | 0.099 | 15/28 (SNU-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.724× | -3.1 | 0.11 | 15/35 (NCI-H2030, A549, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.798× | -3.1 | 0.11 | 12/37 (C32, HCT15, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.745× | -3.0 | 0.11 | 10/39 (SNU-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6680. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 103 | 0 | 25 (8 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0831× (z -15.9) |
| [[NCI-H1792 (line)]] | alt | 14.2 | 21 (1 ⚠) | 0 | [[Triamcinolone (drug)]] 5 µM 10.5× (z +12.9) | — |
| [[NCI-H460 (line)]] | wt | 3.98 | 17 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.81× (z +12.4) ⚠ position correction uncertain · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 12.5× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 37.4 | 12 | 1 (1 ⚠) | [[Triamcinolone (drug)]] 5 µM 4.04× (z +10.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -8.5) ⚠ position correction uncertain |
| [[SW 900 (line)]] | alt | 10.8 | 5 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 17.0× (z +9.2) | — |
| [[LoVo (line)]] | wt | 3.89 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +12.5) ⚠ position correction uncertain | [[Pemetrexed (drug)]] 0.05 µM 0.0603× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 6.35 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0634× (z -10.3) |
| [[PANC-1 (line)]] | alt | 6.37 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +9.2) | [[Cobimetinib (drug)]] 0.5 µM 0.0528× (z -14.5) |
| [[A-172 (line)]] | wt | 2.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.9× (z +8.9) | — |
| [[C32 (line)]] | wt | 31.3 | 1 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 4.42× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 4.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.42× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 2.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.79× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 21.1 | 1 | 0 | [[Budesonide (drug)]] 0.5 µM 8.87× (z +8.6) | — |
| [[SW480 (line)]] | alt | 2.94 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.91× (z +10.8) ⚠ position correction uncertain | — |
| [[A-427 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6680), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXC2]] | +0.74 | +0.73 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[TOP1]] | +0.70 | +0.62 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[RIPOR2]] | +0.70 | +0.61 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[VSTM2L]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[ADAMTS9]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[STXBP5-AS1]] | +0.67 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[ADPRHL1]] | +0.67 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[ZMYND8]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[DNER]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[KLF9]] | +0.64 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[IRX3]] | +0.64 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[SH3RF3]] | +0.62 | +0.54 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRLNT]] | -0.57 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[CD5L]] | -0.57 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[ADAMTS16]] | -0.55 | -0.50 / -0.57 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[SLAMF7]] | -0.55 | -0.36 / -0.65 | both halves | 1e-04 |  |
| [[IGFN1]] | -0.52 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[CD47]] | -0.51 | -0.45 / -0.53 | both halves | 3e-05 | pathway: Extracellular matrix organization |
| [[LINC01411]] | -0.48 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[CPA4]] | -0.47 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[PSG9]] | -0.46 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[TNFRSF9]] | -0.46 | -0.33 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA6]] | B | ABCA6 activity raises ITGA10's level | lines that do not express ABCA6 (26) vs lines expressing it (24) | 2.44× lower at baseline in the lines without ABCA6 | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC02154, IGF2, LYPLAL1-DT |
| [[AOX1]] | B | AOX1 activity raises ITGA10's level | lines that do not express AOX1 (17) vs lines expressing it (33) | 2.05× lower at baseline in the lines without AOX1 | 0.046 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[ADGRG2]] | B | ADGRG2 activity raises ITGA10's level | lines that do not express ADGRG2 (10) vs lines expressing it (40) | 2.04× lower at baseline in the lines without ADGRG2 | 0.073 | ⚠ within organs, on part of the lines; also absent: KCNN3, SLC17A7, STARD8; maybe low, not absent |
| [[ENOX1]] | B | ENOX1 activity raises ITGA10's level | lines that do not express ENOX1 (12) vs lines expressing it (38) | 2.02× lower at baseline in the lines without ENOX1 | 0.089 | ⚠ within organs, on part of the lines; also absent: CYP1B1-AS1, HTR7, SLC1A3; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity raises ITGA10's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 7.0% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGD4]] | B | ITGA10 activity lowers FGD4's level | lines that do not express ITGA10 (9) vs lines expressing it (41) | 3.59× higher at baseline in the lines without ITGA10 | 0.015 | ⚠ within organs, on part of the lines; also absent: SLC17A7, ZEB1, BOLA3-DT; maybe low, not absent |
| [[ZNF624]] | B | ITGA10 activity raises ZNF624's level | lines that do not express ITGA10 (9) vs lines expressing it (41) | 1.73× lower at baseline in the lines without ITGA10 | 0.020 | ⚠ within organs, on part of the lines; also absent: SLC17A7, ZEB1, BOLA3-DT; maybe low, not absent |
| [[HS3ST3B1]] | B | ITGA10 activity raises HS3ST3B1's level | lines that do not express ITGA10 (9) vs lines expressing it (41) | 3.02× lower at baseline in the lines without ITGA10 | 0.047 | ⚠ within organs, on part of the lines; also absent: SLC17A7, ZEB1, BOLA3-DT; maybe low, not absent |
| [[PYY]] | B | ITGA10 activity raises PYY's level | lines that do not express ITGA10 (9) vs lines expressing it (41) | 1.77× lower at baseline in the lines without ITGA10 | 0.048 | ⚠ within organs, on part of the lines; also absent: SLC17A7, ZEB1, BOLA3-DT; maybe low, not absent |
| [[ANGPTL4]] | B | ITGA10 activity raises ANGPTL4's level | lines that do not express ITGA10 (9) vs lines expressing it (41) | 2.99× lower at baseline in the lines without ITGA10 | 0.073 | ⚠ within organs, on part of the lines; also absent: SLC17A7, ZEB1, BOLA3-DT; maybe low, not absent |
| [[IRX3]] | B | ITGA10 activity raises IRX3's level | lines that do not express ITGA10 (9) vs lines expressing it (41) | 2.39× lower at baseline in the lines without ITGA10 | 0.074 | ⚠ within organs, on part of the lines; also absent: SLC17A7, ZEB1, BOLA3-DT; maybe low, not absent |
| cells under [[Minodronic acid (drug)]] 0.5 µM | B | ITGA10 activity raises the cells' numbers under Minodronic acid 0.5 µM (protects the cells) | lines that do not express ITGA10 (9) vs lines expressing it (39) | the lines without ITGA10: 0.86× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: SLC17A7, ZEB1, BOLA3-DT; maybe low, not absent |
| [[B3GNT5]] | B | ITGA10 activity lowers B3GNT5's level | lines that do not express ITGA10 (9) vs lines expressing it (41) | 2.35× higher at baseline in the lines without ITGA10 | 0.080 | ⚠ within organs, on part of the lines; also absent: SLC17A7, ZEB1, BOLA3-DT; maybe low, not absent |
| [[MT2A]] | B | ITGA10 activity raises MT2A's level | lines that do not express ITGA10 (9) vs lines expressing it (41) | 2.37× lower at baseline in the lines without ITGA10 | 0.097 | ⚠ within organs, on part of the lines; also absent: SLC17A7, ZEB1, BOLA3-DT; maybe low, not absent |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.774). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.0, 15.4); signed map (17.5, 32.5). **Vector** length 109, 26.0% of its response variance represented; |z| ≥ 3 in 1,412 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | +7.6 | +13.8 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +5.8 | +9.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +5.8 | +11.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.8 | +10.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +5.7 | +9.7 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +5.6 | +9.0 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.2 | -4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.0 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.9 | -3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit alpha 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.1 — chr1:145,891,208-145,910,111 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Integrin alpha subunits |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 8 pathways, smallest: CHL1 interactions; Platelet Adhesion to exposed collagen; Integrin cell surface interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [O75578](https://www.uniprot.org/uniprotkb/O75578) (Integrin alpha-10):

> Integrin alpha-10/beta-1 is a receptor for collagen.

**Summary**, from NCBI Gene [8515](https://www.ncbi.nlm.nih.gov/gene/8515):

> Integrins are integral transmembrane glycoproteins composed of noncovalently linked alpha and beta chains. They participate in cell adhesion as well as cell-surface mediated signalling. This gene encodes an integrin alpha chain and is expressed at high levels in chondrocytes, where it is transcriptionally regulated by AP-2epsilon and Ets-1. The protein encoded by this gene binds to collagen. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:6135](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6135) · Entrez [8515](https://www.ncbi.nlm.nih.gov/gene/8515) · UniProt [O75578](https://www.uniprot.org/uniprotkb/O75578) · Ensembl [ENSG00000143127](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143127)

## Data

Gene col 6680: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6680); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6680, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6680]; `tensor/DDL_lfc|DDL_z.npy` [6680]; `embed/gene_vectors.npy` [6680]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6680 or target_col == 6680). Every well: [[ITGA10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGA10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
