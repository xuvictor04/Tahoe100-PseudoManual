---
symbol: "GPC4"
type: "gene"
col: 1162
ensembl_id: "ENSG00000076716"
name: "glypican 4"
location: "Xq26.2"
module: 29
arm: "+"
pooled_cpm: 11.51
n_lines_expressing: 31
n_dd_up: 7
n_dd_down: 18
n_dd_up_clean: 4
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# GPC4

*glypican 4* — Xq26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.73× (z +8.5, q 1e-14, up in 11 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.24× (z +4.7, q 3e-04, up in 8 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.417× (z -13.8, q 2e-40, down in 24 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRPS2]] (+0.70, fdr 7e-06), [[STT3B]] (+0.65, fdr 1e-05), [[CELSR2]] (+0.64, fdr 1e-05); moves opposite to [[NSRP1]] (-0.63, fdr 1e-05), [[ATF4]] (-0.61, fdr 1e-05), [[FCF1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 4 go from it, the strongest it → [[ADCY6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1162.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +8.5 | 1e-14 | 11/21 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +6.2 | 1e-07 | 5/14 (CFPAC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.32×** | +6.2 | 1e-07 | 13/27 (LoVo, RKO, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.7 | 3e-04 | 8/28 (NCI-H2347, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +4.4 | 0.001 | 6/28 (NCI-H23, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +4.0 | 0.005 | 4/27 (NCI-H23, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.048 | 6/27 (NCI-H2347, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.21× | +3.0 | 0.17 | 6/28 (COLO 205, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1162.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.417×** | -13.8 | 2e-40 | 24/27 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.554×** | -13.2 | 4e-37 | 19/27 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.512×** | -10.1 | 7e-22 | 21/27 (A-172, SW48, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.550×** | -9.2 | 3e-18 | 19/27 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.626×** | -7.4 | 2e-11 | 18/27 (HT-29, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.629×** | -7.3 | 2e-11 | 16/28 (H4, A498, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.695×** | -5.7 | 8e-07 | 14/27 (HEC-1-A, A498, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.705×** | -5.2 | 1e-05 | 14/26 (LS 180, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.738×** | -4.8 | 1e-04 | 12/27 (A-172, RKO, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.807×** | -4.8 | 1e-04 | 12/28 (SNU-423, SNU-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.749×** | -4.5 | 3e-04 | 12/27 (COLO 205, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.756×** | -4.4 | 5e-04 | 9/28 (LS 180, AN3 CA, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.780×** | -3.9 | 0.004 | 10/28 (COLO 205, LoVo, …) | two highest doses | composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.784×** | -3.8 | 0.005 | 6/26 (BT-474, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Verteporfin (drug)]] 5 µM |  | **0.777×** | -3.8 | 0.005 | 13/26 (BT-474, C-33 A, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.800×** | -3.4 | 0.026 | 8/26 (CFPAC-1, BT-474, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **0.811×** | -3.3 | 0.032 | 8/27 (H4, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1162. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 24.9 | 1 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +8.6) ⚠ cell-cycle shift, explains ~17% of this change | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -13.0) |
| [[A-172 (line)]] | wt | 9.21 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0271× (z -18.7) |
| [[RKO (line)]] | wt | 21.4 | 1 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +8.9) ⚠ cell-cycle shift, explains ~17% of this change | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -10.2) |
| [[C-33 A (line)]] | alt | 70.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.343× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 17.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -11.6) |
| [[KATO III (line)]] | alt | 23.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.205× (z -10.4) |
| [[LoVo (line)]] | wt | 14.9 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +9.4) ⚠ cell-cycle shift, explains ~17% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 6.20 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0908× (z -11.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.211× (z -10.7) |
| [[SNU-1 (line)]] | wt | 29.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -10.1) |
| [[SW48 (line)]] | wt | 12.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0244× (z -13.2) |
| [[A-427 (line)]] | wt | 25.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.182× (z -13.2) |
| [[C32 (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.167× (z -8.8) ⚠ toxic |
| [[HT-29 (line)]] | alt | 4.29 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0866× (z -8.7) |
| [[SW480 (line)]] | alt | 40.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.385× (z -8.6) ⚠ cell-cycle shift, explains ~84% of this change |
| [[A549 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.705 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 271 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.811 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.804 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.61 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1162), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPS2]] | +0.70 | +0.58 / +0.68 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[STT3B]] | +0.65 | +0.62 / +0.57 | both halves | 1e-05 | pathway: SARS-CoV-2 Infection |
| [[CELSR2]] | +0.64 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[PTGFRN]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[LAPTM4B]] | +0.61 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[CRTAP]] | +0.61 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[GMPS]] | +0.61 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[GLB1L2]] | +0.59 | +0.56 / +0.62 | both halves | 1e-05 | pathway: Glycosaminoglycan metabolism |
| [[TMEM109]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[MMP15]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ADAM15]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[TMEM123]] | +0.58 | +0.58 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSRP1]] | -0.63 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[ATF4]] | -0.61 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[FCF1]] | -0.60 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[C2orf74]] | -0.59 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[CCDC174]] | -0.57 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[NECAP2]] | -0.57 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[MRPS18C]] | -0.56 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[ZNF23]] | -0.55 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[ZCCHC9]] | -0.55 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[NT5C]] | -0.54 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[ZC3H13]] | -0.54 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[LARP7]] | -0.54 | -0.51 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers GPC4's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY6]] | B | GPC4 activity raises ADCY6's level | lines that do not express GPC4 (19) vs lines expressing it (31) | 1.56× lower at baseline in the lines without GPC4 | 0.051 | ⚠ within organs, on part of the lines; also absent: KCNK5, NTN1, FUT3 |
| [[CDH24]] | B | GPC4 activity raises CDH24's level | lines that do not express GPC4 (19) vs lines expressing it (31) | 1.57× lower at baseline in the lines without GPC4 | 0.055 | ⚠ within organs, on part of the lines; also absent: KCNK5, NTN1, FUT3 |
| [[PRKCQ]] | B | GPC4 activity raises PRKCQ's level | lines that do not express GPC4 (19) vs lines expressing it (31) | 2.06× lower at baseline in the lines without GPC4 | 0.088 | ⚠ within organs, on part of the lines; also absent: KCNK5, NTN1, FUT3 |
| [[TP53I11]] | B | GPC4 activity raises TP53I11's level | lines that do not express GPC4 (19) vs lines expressing it (31) | 2.30× lower at baseline in the lines without GPC4 | 0.089 | ⚠ within organs, on part of the lines; also absent: KCNK5, NTN1, FUT3 |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.608). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.3, -25.4); signed map (-29.8, -41.2). **Vector** length 57.9, 11.7% of its response variance represented; |z| ≥ 3 in 616 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +6.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +8.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +2.3 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.1 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +4.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | -0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +0.9 | +3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +0.8 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -7.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -9.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -13.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -7.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.5 | -10.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -3.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | glypican 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.2 — chrX:133,300,103-133,415,489 (-) |
| Ensembl biotype | protein_coding |
| Also known as | K-glypican |
| Gene groups (HGNC) | Glypicans |
| Hallmark sets | GLYCOLYSIS, HYPOXIA |
| Reactome | 34 pathways, smallest: Defective EXT1 causes exostoses 1, TRPS2 and CHDS; Defective EXT2 causes exostoses 2; Defective B3GALT6 causes EDSP2 and SEMDJL1 |
| Matched by | ensembl_id |

**Function**, from UniProt [O75487](https://www.uniprot.org/uniprotkb/O75487) (Glypican-4):

> Cell surface proteoglycan that bears heparan sulfate. May be involved in the development of kidney tubules and of the central nervous system (By similarity).

**Summary**, from NCBI Gene [2239](https://www.ncbi.nlm.nih.gov/gene/2239):

> Cell surface heparan sulfate proteoglycans are composed of a membrane-associated protein core substituted with a variable number of heparan sulfate chains. Members of the glypican-related integral membrane proteoglycan family (GRIPS) contain a core protein anchored to the cytoplasmic membrane via a glycosyl phosphatidylinositol linkage. These proteins may play a role in the control of cell division and growth regulation. The GPC4 gene is adjacent to the 3' end of GPC3 and may also play a role …

**Accessions** — [HGNC:4452](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4452) · Entrez [2239](https://www.ncbi.nlm.nih.gov/gene/2239) · UniProt [O75487](https://www.uniprot.org/uniprotkb/O75487) · Ensembl [ENSG00000076716](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076716)

## Data

Gene col 1162: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1162); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1162, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1162]; `tensor/DDL_lfc|DDL_z.npy` [1162]; `embed/gene_vectors.npy` [1162]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1162 or target_col == 1162). Every well: [[GPC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
