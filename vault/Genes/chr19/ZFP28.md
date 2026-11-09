---
symbol: "ZFP28"
type: "gene"
col: 12295
ensembl_id: "ENSG00000196867"
name: "ZFP28 zinc finger protein"
location: "19q13.43"
module: 129
arm: "+"
pooled_cpm: 7.53
n_lines_expressing: 29
n_dd_up: 1
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 15
direction_downstream: 25
tags: ["gene", "module/129"]
generated_by: "tahoemap"
---

# ZFP28

*ZFP28 zinc finger protein* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.47× (z +3.8, q 0.067, up in 11 of 24 measured lines) ⚠ cell-cycle shift, explains ~25% of this change.
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (13 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.434× (z -8.7, q 1e-15, down in 17 of 26 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.505× (z -6.9, q 1e-09, down in 19 of 24 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF71]] (+0.70, fdr 7e-06, ⚠ same locus), [[ZNF470]] (+0.70, fdr 7e-06, ⚠ same locus), [[ZIM2-AS1]] (+0.67, fdr 1e-05, ⚠ same locus), [[ZNF177]] (+0.62, fdr 1e-05), [[ZNF527]] (+0.57, fdr 3e-05), [[ZNF70]] (+0.55, fdr 1e-04); moves opposite to [[SRGN]] (-0.49, fdr 3e-05), [[RASSF5]] (-0.47, fdr 1e-04), [[RAMP1]] (-0.47, fdr 2e-04).
> It is in [[Module 129]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 25 go from it, the strongest it → [[HNF4G]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12295.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.47×** | +3.8 | 0.067 | 11/24 (RPMI-7951, A549, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.39× | +3.4 | 0.21 | 8/26 (RPMI-7951, H4, …) | rises with dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.2 | 0.22 | 0/27 | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.34× | +3.0 | 0.36 | 7/26 (HS-578T, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12295.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.434×** | -8.7 | 1e-15 | 17/26 (HOP62, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.465×** | -7.7 | 4e-12 | 15/25 (HOP62, A-172, …) | top dose only | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.505×** | -6.9 | 1e-09 | 19/24 (A-172, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~23% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.523×** | -6.8 | 2e-09 | 18/24 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.638×** | -6.7 | 3e-09 | 17/25 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.658×** | -6.2 | 5e-08 | 13/25 (HS-578T, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.545×** | -6.1 | 8e-08 | 15/22 (NCI-H460, A-172, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.611×** | -5.2 | 2e-05 | 15/26 (SW 900, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.602×** | -5.1 | 2e-05 | 15/24 (NCI-H23, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.720×** | -4.9 | 6e-05 | 13/27 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.638×** | -4.7 | 1e-04 | 15/25 (hTERT-HPNE, SW 900, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.668×** | -4.1 | 0.002 | 11/23 (SK-MEL-2, HS-578T, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.698×** | -3.8 | 0.007 | 10/26 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.701×** | -3.7 | 0.007 | 10/25 (H4, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.701×** | -3.7 | 0.007 | 8/24 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.661×** | -3.0 | 0.080 | 7/25 (NCI-H460, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.746×** | -3.0 | 0.088 | 7/25 (RPMI-7951, SK-MEL-2, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **0.750×** | -2.9 | 0.099 | 8/24 (A-172, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12295. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 29.3 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0440× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -12.5) |
| [[A549 (line)]] | wt | 23.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 11.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -10.6) |
| [[HOP62 (line)]] | alt | 11.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0695× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 13.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -13.4) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 16.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 13.0 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -9.6) |
| [[BT-474 (line)]] | alt | 12.2 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -11.4) ⚠ cell-cycle shift, explains ~66% of this change |
| [[RPMI-7951 (line)]] | alt | 22.8 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.1000× (z -12.2) |
| [[SK-MEL-2 (line)]] | alt | 31.6 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -9.0) |
| [[SW 900 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.122× (z -10.2) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A-427 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.429 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.500 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.514 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.538 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.468 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.634 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.463 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.700 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.450 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.542 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.560 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.647 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 10.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12295), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 6 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF71]] | +0.70 | +0.76 / +0.59 | both halves | 7e-06 | same gene group; ⚠ same locus (38.5 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF470]] | +0.70 | +0.73 / +0.59 | both halves | 7e-06 | same gene group; STRING 460; ⚠ same locus (10.7 kb, same strand: neighbours can correlate without regulation) |
| [[ZIM2-AS1]] | +0.67 | +0.69 / +0.54 | both halves | 1e-05 | ⚠ same locus (38.5 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF471]] | +0.65 | +0.61 / +0.63 | both halves | 7e-06 | same gene group; ⚠ same locus (8.7 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF177]] | +0.62 | +0.57 / +0.54 | both halves | 1e-05 | same gene group |
| [[ZNF527]] | +0.57 | +0.55 / +0.43 | both halves | 3e-05 | same gene group |
| [[ZNF70]] | +0.55 | +0.59 / +0.36 | both halves | 1e-04 | same gene group |
| [[ZNF583]] | +0.54 | +0.61 / +0.42 | both halves | 4e-05 | same gene group |
| [[AP1M1]] | +0.52 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[RNF216P1]] | +0.51 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[ZNF571]] | +0.51 | +0.51 / +0.35 | both halves | 1e-04 | same gene group |
| [[ZC3H10]] | +0.50 | +0.32 / +0.46 | both halves | 2e-04 |  |
| [[ZNF17]] | +0.50 | +0.46 / +0.49 | both halves | 3e-05 | same gene group |
| [[ZFP90]] | +0.49 | +0.27 / +0.43 | both halves | 3e-04 | same gene group |
| [[BVES]] | +0.49 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[ZNF568]] | +0.49 | +0.57 / +0.29 | both halves | 2e-04 | same gene group |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGN]] | -0.49 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[RASSF5]] | -0.47 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[RAMP1]] | -0.47 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[ATXN7L1]] | -0.46 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[MICOS10]] | -0.46 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[ITPKB]] | -0.45 | -0.30 / -0.31 | both halves | 2e-04 |  |
| [[SLC44A3]] | -0.45 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[ARL15]] | -0.45 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[DEPTOR]] | -0.44 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[TJP2]] | -0.44 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[SLC44A3-AS1]] | -0.44 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[HNF4G]] | -0.44 | -0.45 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 6, C 9. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ZFP28's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HNF4G]] | B | HNF4G activity lowers ZFP28's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 3.83× higher at baseline in the lines without HNF4G | 0.030 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[ZNF329]] | B | ZNF329 activity raises ZFP28's level | lines that do not express ZNF329 (7) vs lines expressing it (43) | 1.88× lower at baseline in the lines without ZNF329 | 0.074 | ⚠ within organs, on part of the lines; also absent: C2orf27A |
| [[SARDH]] | B | SARDH activity raises ZFP28's level | lines that do not express SARDH (21) vs lines expressing it (29) | 2.14× lower at baseline in the lines without SARDH | 0.086 | ⚠ within organs, on part of the lines; also absent: PKD1L1-AS1, ZNF90, ENSG00000222032; maybe low, not absent |
| [[L1CAM]] | B | L1CAM activity raises ZFP28's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 2.53× lower at baseline in the lines without L1CAM | 0.093 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |
| [[TMEM92-AS1]] | B | TMEM92-AS1 activity strengthens ZFP28's drug response | lines that do not express TMEM92-AS1 (8) vs lines expressing it (19) | the lines without TMEM92-AS1 respond 0.34× as strongly (z diff +2.09); strongest at Homoharringtonine 5 µM: 1.87x vs 0.50x (z diff +8.5) | 0.095 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2; target measured in part of the lines; artifact flags |
| [[ZNF470]] | C | ZNF470 activity raises ZFP28's level | lines that do not express ZNF470 (18) vs lines expressing it (32) | 7.17× lower at baseline in the lines without ZNF470 | 2e-04 | ⚠ within organs, on part of the lines; also absent: ZFP28, ZNF71, ZIM2-AS1; co-absent with the target |
| [[ZNF471]] | C | ZNF471 activity raises ZFP28's level | lines that do not express ZNF471 (28) vs lines expressing it (22) | 5.89× lower at baseline in the lines without ZNF471 | 0.001 | ⚠ within organs, on part of the lines; also absent: TRIML2, ZNF667, ZNF667-AS1; co-absent with the target |
| [[ZNF71]] | C | ZNF71 activity raises ZFP28's level | lines that do not express ZNF71 (15) vs lines expressing it (35) | 6.05× lower at baseline in the lines without ZNF71 | 0.002 | ⚠ within organs, on part of the lines; also absent: ZIM2-AS1, ZNF470, ZFP28; co-absent with the target |
| [[ZIM2-AS1]] | C | ZIM2-AS1 activity raises ZFP28's level | lines that do not express ZIM2-AS1 (13) vs lines expressing it (37) | 5.47× lower at baseline in the lines without ZIM2-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ZNF71, ZNF470, ZFP28; co-absent with the target |
| [[C14orf132]] | C | C14orf132 activity raises ZFP28's level | lines that do not express C14orf132 (19) vs lines expressing it (31) | 4.28× lower at baseline in the lines without C14orf132 | 0.018 | ⚠ within organs, on part of the lines; also absent: SLC22A17, ZFP28, ADAMTS7; co-absent with the target |
| [[ZNF549]] | C | ZNF549 activity raises ZFP28's level | lines that do not express ZNF549 (17) vs lines expressing it (33) | 4.67× lower at baseline in the lines without ZNF549 | 0.023 | ⚠ within organs, on part of the lines; also absent: SDK2, SNRPN, CHST10; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 14, C 11. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HNF4G]] | B | ZFP28 activity lowers HNF4G's level | lines that do not express ZFP28 (21) vs lines expressing it (29) | 3.95× higher at baseline in the lines without ZFP28 | 0.018 | ⚠ within organs, on part of the lines; also absent: ZNF470, ZNF471, MAP6 |
| [[ZNF284]] | B | ZFP28 activity raises ZNF284's level | lines that do not express ZFP28 (21) vs lines expressing it (29) | 2.04× lower at baseline in the lines without ZFP28 | 0.024 | ⚠ within organs, on part of the lines; also absent: ZNF470, ZNF471, MAP6 |
| [[ZNF559]] | B | ZFP28 activity raises ZNF559's level | lines that do not express ZFP28 (21) vs lines expressing it (29) | 2.41× lower at baseline in the lines without ZFP28 | 0.032 | ⚠ within organs, on part of the lines; also absent: ZNF470, ZNF471, MAP6 |
| [[ZNF70]] | B | ZFP28 activity raises ZNF70's level | lines that do not express ZFP28 (21) vs lines expressing it (29) | 1.46× lower at baseline in the lines without ZFP28 | 0.036 | ⚠ within organs, on part of the lines; also absent: ZNF470, ZNF471, MAP6 |
| [[DEPTOR]] | B | ZFP28 activity lowers DEPTOR's level | lines that do not express ZFP28 (21) vs lines expressing it (29) | 1.86× higher at baseline in the lines without ZFP28 | 0.045 | ⚠ within organs, on part of the lines; also absent: ZNF470, ZNF471, MAP6 |
| [[ZNF329]] | B | ZFP28 activity raises ZNF329's level | lines that do not express ZFP28 (21) vs lines expressing it (29) | 1.71× lower at baseline in the lines without ZFP28 | 0.051 | ⚠ within organs, on part of the lines; also absent: ZNF470, ZNF471, MAP6 |
| [[ZNF420]] | B | ZFP28 activity raises ZNF420's level | lines that do not express ZFP28 (21) vs lines expressing it (29) | 2.56× lower at baseline in the lines without ZFP28 | 0.052 | ⚠ within organs, on part of the lines; also absent: ZNF470, ZNF471, MAP6 |
| [[ZNF385A]] | B | ZFP28 activity raises ZNF385A's level | lines that do not express ZFP28 (21) vs lines expressing it (29) | 1.91× lower at baseline in the lines without ZFP28 | 0.063 | ⚠ within organs, on part of the lines; also absent: ZNF470, ZNF471, MAP6 |
| [[ZNF177]] | B | ZFP28 activity raises ZNF177's level | lines that do not express ZFP28 (21) vs lines expressing it (29) | 1.84× lower at baseline in the lines without ZFP28 | 0.068 | ⚠ within organs, on part of the lines; also absent: ZNF470, ZNF471, MAP6 |
| [[SARDH]] | B | ZFP28 activity raises SARDH's level | lines that do not express ZFP28 (21) vs lines expressing it (29) | 1.67× lower at baseline in the lines without ZFP28 | 0.075 | ⚠ within organs, on part of the lines; also absent: ZNF470, ZNF471, MAP6 |
| [[ZNF607]] | B | ZFP28 activity raises ZNF607's level | lines that do not express ZFP28 (21) vs lines expressing it (29) | 1.71× lower at baseline in the lines without ZFP28 | 0.084 | ⚠ within organs, on part of the lines; also absent: ZNF470, ZNF471, MAP6 |
| [[ZNF527]] | B | ZFP28 activity raises ZNF527's level | lines that do not express ZFP28 (21) vs lines expressing it (29) | 1.66× lower at baseline in the lines without ZFP28 | 0.087 | ⚠ within organs, on part of the lines; also absent: ZNF470, ZNF471, MAP6 |

## Where it sits

- **Module**: [[Module 129]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.575). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.8, 28.3); signed map (-17.8, -15.7). **Vector** length 58.6, 13.6% of its response variance represented; |z| ≥ 3 in 601 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.3 | -0.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +2.1 | +3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +1.8 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.4 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.4 | +0.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.1 | -5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.1 | -8.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -2.1 | -6.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -1.9 | -5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -1.8 | -4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.2 | -0.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.9 | -4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -0.9 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | ZFP28 zinc finger protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.43 — chr19:56,538,948-56,556,808 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1431, mkr5 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NHY6](https://www.uniprot.org/uniprotkb/Q8NHY6) (Zinc finger protein 28 homolog):

> May be involved in transcriptional regulation. May have a role in embryonic development.

**Summary**, from NCBI Gene [140612](https://www.ncbi.nlm.nih.gov/gene/140612):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17801](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17801) · Entrez [140612](https://www.ncbi.nlm.nih.gov/gene/140612) · UniProt [Q8NHY6](https://www.uniprot.org/uniprotkb/Q8NHY6) · Ensembl [ENSG00000196867](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196867)

## Data

Gene col 12295: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12295); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12295, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12295]; `tensor/DDL_lfc|DDL_z.npy` [12295]; `embed/gene_vectors.npy` [12295]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12295 or target_col == 12295). Every well: [[ZFP28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFP28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
