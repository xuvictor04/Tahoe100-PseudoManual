---
symbol: "GYG1"
type: "gene"
col: 8772
ensembl_id: "ENSG00000163754"
name: "glycogenin 1"
location: "3q24"
module: 68
arm: "+"
pooled_cpm: 16.73
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 3
n_dd_up_clean: 23
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# GYG1

*glycogenin 1* — 3q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.46× (z +20.3, q 0e+00, up in 39 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.392× (z -7.5, q 4e-11, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HACD1]] (+0.69, fdr 1e-05), [[LACC1]] (+0.67, fdr 1e-05), [[NFYB]] (+0.66, fdr 1e-05); moves opposite to [[RNF121]] (-0.65, fdr 3e-05), [[FHIP1B]] (-0.60, fdr 4e-05), [[NUP160]] (-0.58, fdr 3e-04).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8772.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.46×** | +20.3 | 0e+00 | 39/46 (NCI-H2347, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.52×** | +14.7 | 0e+00 | 39/46 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +12.5 | 2e-33 | 39/47 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.24×** | +12.4 | 5e-33 | 41/46 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +12.0 | 4e-31 | 30/39 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.89×** | +10.2 | 2e-22 | 38/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.80×** | +9.0 | 1e-17 | 22/28 (A549, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.68×** | +8.3 | 1e-14 | 30/47 (A498, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +7.2 | 4e-11 | 28/47 (LS 180, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +7.1 | 8e-11 | 18/36 (SNU-423, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +7.0 | 1e-10 | 29/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +6.8 | 5e-10 | 26/47 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +6.5 | 3e-09 | 22/42 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +6.2 | 2e-08 | 26/47 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +6.0 | 7e-08 | 25/48 (A498, HEC-1-A, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.25×** | +5.0 | 3e-05 | 16/48 (HOP62, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +4.3 | 4e-04 | 19/46 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.45×** | +4.1 | 1e-03 | 17/42 (HS-578T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.66×** | +4.0 | 0.001 | 6/43 (A-427, HOP62, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8772.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.392×** | -7.5 | 4e-11 | 29/47 (Panc 03.27, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.545×** | -4.9 | 3e-04 | 23/45 (LOX-IMVI, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.547×** | -4.8 | 3e-04 | 20/46 (A498, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Megestrol (drug)]] 5 µM |  | 0.855× | -3.6 | 0.052 | 15/48 (A498, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8772. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 12.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 8.46 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +13.4) | — |
| [[A-427 (line)]] | wt | 37.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.33× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.277× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 9.33 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +11.1) | — |
| [[COLO 205 (line)]] | alt | 11.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +14.2) | [[Pimozide (drug)]] 0.5 µM 0.102× (z -9.4) ⚠ transcription drop |
| [[HEC-1-A (line)]] | alt | 19.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +10.8) | — |
| [[KATO III (line)]] | alt | 17.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +12.3) | — |
| [[LoVo (line)]] | wt | 11.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 10.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +11.0) | — |
| [[NCI-H460 (line)]] | wt | 10.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +12.1) | — |
| [[Panc 03.27 (line)]] | alt | 33.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.187× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[PANC-1 (line)]] | alt | 22.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +12.6) | — |
| [[A-172 (line)]] | wt | 13.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +9.5) | — |
| [[A549 (line)]] | wt | 15.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 5.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.38× (z +11.3) | — |
| [[C32 (line)]] | wt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +11.8) | — |
| [[HCT15 (line)]] | alt | 8.67 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0755× (z -8.8) |
| [[HT-29 (line)]] | alt | 22.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.15× (z +13.4) | — |
| [[LS 180 (line)]] | wt | 9.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +12.2) | — |
| [[NCI-H1792 (line)]] | alt | 11.1 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.47× (z +9.1) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H2347 (line)]] | alt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +16.1) | — |
| [[SK-MEL-2 (line)]] | alt | 20.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 49.9 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.138× (z -10.0) |
| [[SNU-423 (line)]] | alt | 12.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 15.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +10.2) | — |
| [[SW1417 (line)]] | alt | 20.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +8.5) | — |
| [[SW480 (line)]] | alt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +12.0) | — |
| [[AN3 CA (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8772), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACD1]] | +0.69 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[LACC1]] | +0.67 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[NFYB]] | +0.66 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[TMEM35B]] | +0.66 | +0.61 / +0.37 | both halves | 7e-05 |  |
| [[RXYLT1]] | +0.66 | +0.73 / +0.39 | both halves | 5e-05 | same gene group |
| [[TAF9]] | +0.64 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[ANKRD18A]] | +0.64 | +0.65 / +0.30 | both halves | 2e-04 |  |
| [[LACTB2]] | +0.64 | +0.72 / +0.37 | both halves | 9e-05 |  |
| [[LGALSL-DT]] | +0.63 | +0.65 / +0.36 | both halves | 1e-04 |  |
| [[GCNT4]] | +0.63 | +0.58 / +0.33 | both halves | 1e-04 |  |
| [[PBDC1]] | +0.62 | +0.66 / +0.30 | both halves | 2e-04 |  |
| [[RNF146]] | +0.62 | +0.68 / +0.23 | both halves | 5e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF121]] | -0.65 | -0.69 / -0.43 | both halves | 3e-05 |  |
| [[FHIP1B]] | -0.60 | -0.64 / -0.40 | both halves | 4e-05 |  |
| [[NUP160]] | -0.58 | -0.70 / -0.28 | both halves | 3e-04 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[SLC27A1]] | -0.58 | -0.61 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[SDHAP4]] | -0.58 | -0.69 / -0.43 | both halves | 3e-05 |  |
| [[SHQ1]] | -0.58 | -0.62 / -0.26 | both halves | 4e-04 |  |
| [[GNAI3]] | -0.56 | -0.64 / -0.25 | both halves | 4e-04 |  |
| [[IGSF8]] | -0.56 | -0.55 / -0.22 | both halves | 6e-04 |  |
| [[TMEM41B]] | -0.56 | -0.63 / -0.31 | both halves | 2e-04 |  |
| [[STRAP]] | -0.55 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[WDR37]] | -0.55 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[SDHAP1]] | -0.55 | -0.66 / -0.27 | both halves | 3e-04 |  |
| [[PIK3R2]] | -0.55 | -0.60 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GYG1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.701). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-1.0, 8.0); signed map (20.2, -16.3). **Vector** length 88.4, 19.0% of its response variance represented; |z| ≥ 3 in 961 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.9 | +14.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.4 | +20.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.2 | +12.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.8 | +10.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +12.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +7.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.5 | +5.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +4.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.0 | -7.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.3 | -4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -2.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | +2.0 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.2 | -3.0 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Vilanterol (drug)]] 5 µM |  | -1.0 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | glycogenin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q24 — chr3:148,991,408-149,031,775 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GYG |
| Gene groups (HGNC) | Glycosyltransferase family 8 |
| Reactome | 10 pathways, smallest: Myoclonic epilepsy of Lafora; Glycogen synthesis; Glycogen storage diseases |
| Matched by | ensembl_id |

**Function**, from UniProt [P46976](https://www.uniprot.org/uniprotkb/P46976) (Glycogenin-1):

> Glycogenin participates in the glycogen biosynthetic process along with glycogen synthase and glycogen branching enzyme. It catalyzes the formation of a short alpha (1,4)-glucosyl chain covalently attached via a glucose 1-O-tyrosyl linkage to internal tyrosine residues and these chains act as primers for the elongation reaction catalyzed by glycogen synthase.

**Summary**, from NCBI Gene [2992](https://www.ncbi.nlm.nih.gov/gene/2992):

> This gene encodes a member of the glycogenin family. Glycogenin is a glycosyltransferase that catalyzes the formation of a short glucose polymer from uridine diphosphate glucose in an autoglucosylation reaction. This reaction is followed by elongation and branching of the polymer, catalyzed by glycogen synthase and branching enzyme, to form glycogen. This gene is expressed in muscle and other tissues. Mutations in this gene result in glycogen storage disease XV. This gene has pseudogenes on …

**Accessions** — [HGNC:4699](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4699) · Entrez [2992](https://www.ncbi.nlm.nih.gov/gene/2992) · UniProt [P46976](https://www.uniprot.org/uniprotkb/P46976) · Ensembl [ENSG00000163754](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163754)

## Data

Gene col 8772: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8772); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8772, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8772]; `tensor/DDL_lfc|DDL_z.npy` [8772]; `embed/gene_vectors.npy` [8772]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8772 or target_col == 8772). Every well: [[GYG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GYG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
