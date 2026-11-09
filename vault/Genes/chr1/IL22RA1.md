---
symbol: "IL22RA1"
type: "gene"
col: 6647
ensembl_id: "ENSG00000142677"
name: "interleukin 22 receptor subunit alpha 1"
location: "1p36.11"
module: 8
arm: "+"
pooled_cpm: 6.17
n_lines_expressing: 33
n_dd_up: 10
n_dd_down: 35
n_dd_up_clean: 9
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 76
direction_downstream: 16
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# IL22RA1

*interleukin 22 receptor subunit alpha 1* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.95× (z +8.6, q 5e-15, up in 10 of 22 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.46× (z +5.1, q 1e-04, up in 9 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.362× (z -13.6, q 3e-39, down in 24 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNF4A]] (+0.67, fdr 1e-05), [[PLEKHG6]] (+0.65, fdr 1e-05), [[TC2N]] (+0.64, fdr 1e-05); moves opposite to [[ZNF717]] (-0.50, fdr 3e-05), [[SUMF1]] (-0.49, fdr 3e-05), [[AGPAT5]] (-0.49, fdr 4e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 76 arrows point to it, the strongest [[SLC44A4]] → it (grade B ⚠); 16 go from it, the strongest it → [[LGALS9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6647.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +8.6 | 5e-15 | 10/22 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +5.1 | 1e-04 | 9/30 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +5.0 | 1e-04 | 9/30 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.42×** | +4.4 | 0.002 | 5/28 (SW480, HS-578T, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +4.2 | 0.003 | 8/29 (HCT15, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.003 | 8/30 (KATO III, PANC-1, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.004 | 4/30 (PANC-1, COLO 205, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.079 | 3/27 (A549, SW48, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.093 | 2/30 (KATO III, SW48) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.093 | 5/30 (AsPC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 0.05 µM |  | 1.27× | +3.0 | 0.12 | 3/29 (RPMI-7951, NCI-H2347, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.37× | +3.0 | 0.12 | 4/23 (NCI-H460, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6647.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.362×** | -13.6 | 3e-39 | 24/30 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.555×** | -11.1 | 3e-26 | 23/27 (AsPC-1, LoVo, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.452×** | -10.6 | 5e-24 | 21/30 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.456×** | -10.5 | 2e-23 | 20/30 (AsPC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.594×** | -9.8 | 1e-20 | 20/28 (HT-29, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.489×** | -9.5 | 1e-19 | 21/28 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.495×** | -9.0 | 1e-17 | 19/29 (AsPC-1, A549, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.531×** | -8.4 | 2e-15 | 19/30 (HT-29, A-427, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.536×** | -8.3 | 5e-15 | 20/27 (LoVo, SW1417, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.570×** | -7.5 | 4e-12 | 16/30 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.568×** | -7.2 | 2e-11 | 15/24 (LoVo, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.599×** | -6.8 | 4e-10 | 13/30 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.475×** | -5.2 | 9e-06 | 14/29 (Panc 03.27, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.685×** | -5.0 | 2e-05 | 16/20 (LoVo, HT-29, …) | inconsistent across doses | composition shift |
| [[Mebendazole (drug)]] 5 µM |  | **0.686×** | -4.8 | 5e-05 | 6/30 (NCI-H460, AsPC-1, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -4.8 | 6e-05 | 11/23 (HT-29, SW48, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.692×** | -4.7 | 8e-05 | 12/27 (HT-29, A-172, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.694×** | -4.7 | 9e-05 | 12/30 (HT-29, RKO, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.517×** | -4.6 | 1e-04 | 12/30 (AsPC-1, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.531×** | -4.4 | 3e-04 | 10/26 (Panc 03.27, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.735×** | -4.1 | 0.001 | 6/30 (A-172, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6647. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 30.0 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0513× (z -21.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.201× (z -11.7) |
| [[LS 180 (line)]] | wt | 21.6 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -14.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 15.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0634× (z -21.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0881× (z -13.4) |
| [[HT-29 (line)]] | alt | 38.1 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -16.9) |
| [[NCI-H460 (line)]] | wt | 6.88 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -13.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0797× (z -13.2) |
| [[A-172 (line)]] | wt | 3.69 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0399× (z -11.4) |
| [[A498 (line)]] | wt | 4.01 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -12.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0874× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 6.69 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 4.09 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0840× (z -8.6) |
| [[A549 (line)]] | wt | 4.67 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0706× (z -10.2) |
| [[COLO 205 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -9.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HepG2_C3A (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.118× (z -8.8) ⚠ toxic |
| [[SW1417 (line)]] | alt | 9.22 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0578× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[AN3 CA (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.845 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.688 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.752 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.844 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.935 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.542 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6647), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNF4A]] | +0.67 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[PLEKHG6]] | +0.65 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[TC2N]] | +0.64 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[ARHGEF16]] | +0.63 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[MUC3A]] | +0.61 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[DSG3]] | +0.61 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[FA2H]] | +0.61 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[PIK3C2B]] | +0.60 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[CLIC5]] | +0.60 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[USH1C]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[JUP]] | +0.60 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[HSH2D]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF717]] | -0.50 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[SUMF1]] | -0.49 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[AGPAT5]] | -0.49 | -0.42 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*76 arrows, 76 of them with an alert ⚠; grade A 0, B 54, C 22. Shown: the 12 strongest; 64 more arrows (64 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A4]] | B | SLC44A4 activity raises IL22RA1's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 3.95× lower at baseline in the lines without SLC44A4 | 4e-04 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[SERPINB5]] | B | SERPINB5 activity raises IL22RA1's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 3.28× lower at baseline in the lines without SERPINB5 | 4e-04 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[ADGRF1]] | B | ADGRF1 activity raises IL22RA1's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 3.40× lower at baseline in the lines without ADGRF1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises IL22RA1's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.17× lower at baseline in the lines without TMPRSS4 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[GCNT3]] | B | GCNT3 activity raises IL22RA1's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.99× lower at baseline in the lines without GCNT3 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[P2RY2]] | B | P2RY2 activity raises IL22RA1's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 2.87× lower at baseline in the lines without P2RY2 | 0.002 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[CLIC5]] | B | CLIC5 activity raises IL22RA1's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 3.38× lower at baseline in the lines without CLIC5 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[GDA]] | B | GDA activity raises IL22RA1's level | lines that do not express GDA (35) vs lines expressing it (15) | 3.31× lower at baseline in the lines without GDA | 0.004 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4 |
| [[KLK10]] | B | KLK10 activity raises IL22RA1's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 3.21× lower at baseline in the lines without KLK10 | 0.004 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[EPS8L3]] | B | EPS8L3 activity raises IL22RA1's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 3.72× lower at baseline in the lines without EPS8L3 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[MUC13]] | B | MUC13 activity raises IL22RA1's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 3.80× lower at baseline in the lines without MUC13 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[ST14]] | B | ST14 activity raises IL22RA1's level | lines that do not express ST14 (32) vs lines expressing it (18) | 2.97× lower at baseline in the lines without ST14 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 7, C 9. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGALS9]] | B | IL22RA1 activity raises LGALS9's level | lines that do not express IL22RA1 (17) vs lines expressing it (33) | 2.13× lower at baseline in the lines without IL22RA1 | 0.039 | ⚠ within organs, on part of the lines; also absent: SH2D4A, GOLT1A, ARHGEF5 |
| [[ADGRF1]] | B | IL22RA1 activity raises ADGRF1's level | lines that do not express IL22RA1 (17) vs lines expressing it (33) | 3.24× lower at baseline in the lines without IL22RA1 | 0.059 | ⚠ within organs, on part of the lines; also absent: SH2D4A, GOLT1A, ARHGEF5 |
| [[RHPN2]] | B | IL22RA1 activity raises RHPN2's level | lines that do not express IL22RA1 (17) vs lines expressing it (33) | 2.33× lower at baseline in the lines without IL22RA1 | 0.068 | ⚠ within organs, on part of the lines; also absent: SH2D4A, GOLT1A, ARHGEF5 |
| [[KIAA1522]] | B | IL22RA1 activity raises KIAA1522's level | lines that do not express IL22RA1 (17) vs lines expressing it (33) | 2.33× lower at baseline in the lines without IL22RA1 | 0.074 | ⚠ within organs, on part of the lines; also absent: SH2D4A, GOLT1A, ARHGEF5 |
| [[TTC22]] | B | IL22RA1 activity raises TTC22's level | lines that do not express IL22RA1 (17) vs lines expressing it (33) | 2.25× lower at baseline in the lines without IL22RA1 | 0.075 | ⚠ within organs, on part of the lines; also absent: SH2D4A, GOLT1A, ARHGEF5 |
| [[VILL]] | B | IL22RA1 activity raises VILL's level | lines that do not express IL22RA1 (17) vs lines expressing it (33) | 1.60× lower at baseline in the lines without IL22RA1 | 0.084 | ⚠ within organs, on part of the lines; also absent: SH2D4A, GOLT1A, ARHGEF5 |
| [[LPAR5]] | B | IL22RA1 activity raises LPAR5's level | lines that do not express IL22RA1 (17) vs lines expressing it (33) | 1.90× lower at baseline in the lines without IL22RA1 | 0.084 | ⚠ within organs, on part of the lines; also absent: SH2D4A, GOLT1A, ARHGEF5 |
| [[CYP2S1]] | C | IL22RA1 activity raises CYP2S1's level | lines that do not express IL22RA1 (17) vs lines expressing it (33) | 3.92× lower at baseline in the lines without IL22RA1 | 0.011 | ⚠ within organs, on part of the lines; also absent: SH2D4A, GOLT1A, ARHGEF5; co-absent with the target |
| [[IFNLR1]] | C | IL22RA1 activity raises IFNLR1's level | lines that do not express IL22RA1 (17) vs lines expressing it (33) | 3.18× lower at baseline in the lines without IL22RA1 | 0.013 | ⚠ within organs, on part of the lines; also absent: SH2D4A, GOLT1A, ARHGEF5; co-absent with the target |
| [[INAVA]] | C | IL22RA1 activity raises INAVA's level | lines that do not express IL22RA1 (17) vs lines expressing it (33) | 4.15× lower at baseline in the lines without IL22RA1 | 0.017 | ⚠ within organs, on part of the lines; also absent: SH2D4A, GOLT1A, ARHGEF5; co-absent with the target |
| [[CBLC]] | C | IL22RA1 activity raises CBLC's level | lines that do not express IL22RA1 (17) vs lines expressing it (33) | 3.63× lower at baseline in the lines without IL22RA1 | 0.024 | ⚠ within organs, on part of the lines; also absent: SH2D4A, GOLT1A, ARHGEF5; co-absent with the target |
| [[JUP]] | C | IL22RA1 activity raises JUP's level | lines that do not express IL22RA1 (17) vs lines expressing it (33) | 3.49× lower at baseline in the lines without IL22RA1 | 0.045 | ⚠ within organs, on part of the lines; also absent: SH2D4A, GOLT1A, ARHGEF5; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.529). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.6, 53.7); signed map (60.7, 6.2). **Vector** length 64.1, 13.2% of its response variance represented; |z| ≥ 3 in 786 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +8.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.0 | +5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +5.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | -2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +0.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +1.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -7.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -10.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -13.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -8.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -4.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 22 receptor subunit alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:24,119,771-24,143,140 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CRF2-9; previously IL22R |
| Gene groups (HGNC) | Interleukin receptors |
| Reactome | 3 pathways, smallest: Interleukin-20 family signaling; Signaling by Interleukins; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N6P7](https://www.uniprot.org/uniprotkb/Q8N6P7) (Interleukin-22 receptor subunit alpha-1):

> Component of the receptor for IL20, IL22 and IL24. Component of IL22 receptor formed by IL22RA1 and IL10RB enabling IL22 signaling via JAK/STAT pathways. IL22 also induces activation of MAPK1/MAPK3 and Akt kinases pathways. Component of one of the receptor for IL20 and IL24 formed by IL22RA1 and IL20RB also signaling through STATs activation. Mediates IL24 antiangiogenic activity as well as IL24 inhibitory effect on endothelial cell tube formation and differentiation.

**Summary**, from NCBI Gene [58985](https://www.ncbi.nlm.nih.gov/gene/58985):

> The protein encoded by this gene belongs to the class II cytokine receptor family, and has been shown to be a receptor for interleukin 22 (IL22). IL22 receptor is a protein complex that consists of this protein and interleukin 10 receptor, beta (IL10BR/CRFB4), a subunit also shared by the receptor complex for interleukin 10 (IL10). This gene and interleukin 28 receptor, alpha (IL28RA) form a cytokine receptor gene cluster in the chromosomal region 1p36. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:13700](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13700) · Entrez [58985](https://www.ncbi.nlm.nih.gov/gene/58985) · UniProt [Q8N6P7](https://www.uniprot.org/uniprotkb/Q8N6P7) · Ensembl [ENSG00000142677](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142677)

## Data

Gene col 6647: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6647); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6647, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6647]; `tensor/DDL_lfc|DDL_z.npy` [6647]; `embed/gene_vectors.npy` [6647]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6647 or target_col == 6647). Every well: [[IL22RA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL22RA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
