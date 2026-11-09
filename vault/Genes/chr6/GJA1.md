---
symbol: "GJA1"
type: "gene"
col: 7648
ensembl_id: "ENSG00000152661"
name: "gap junction protein alpha 1"
location: "6q22.31"
module: 19
arm: "+"
pooled_cpm: 50.29
n_lines_expressing: 24
n_dd_up: 10
n_dd_down: 41
n_dd_up_clean: 6
n_dd_down_clean: 38
in_vector_space: true
direction_upstream: 9
direction_downstream: 45
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# GJA1

*gap junction protein alpha 1* — 6q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.55× (z +12.4, q 2e-32, up in 4 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.35× (z +5.7, q 2e-06, up in 5 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.447× (z -15.0, q 0e+00, down in 22 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VEGFC]] (+0.72, fdr 7e-06), [[AADACP1]] (+0.71, fdr 7e-06), [[SERPIND1]] (+0.70, fdr 7e-06); moves opposite to [[FGD4]] (-0.55, fdr 3e-05), [[ACSL1]] (-0.53, fdr 1e-05), [[STOM]] (-0.51, fdr 4e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ADGRG2]] → it (grade B ⚠); 45 go from it, the strongest it → [[VEGFC]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7648.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.55×** | +12.4 | 2e-32 | 4/21 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +8.2 | 5e-14 | 7/19 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +6.1 | 2e-07 | 1/19 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +5.7 | 2e-06 | 5/22 (RPMI-7951, J82, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.52×** | +5.1 | 4e-05 | 16/21 (A549, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.4 | 9e-04 | 6/22 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.071 | 4/21 (NCI-H2030, HS-578T, …) | top dose only |  |
| [[Flutamide (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.071 | 5/22 (NCI-H2030, HS-578T, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.072 | 6/22 (J82, A549, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.27×** | +3.2 | 0.077 | 6/22 (RPMI-7951, NCI-H23, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.084 | 4/22 (Hs 766T, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 3 with an alert ⚠; shown: the 15 strongest. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7648.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.447×** | -15.0 | 0e+00 | 22/22 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.452×** | -10.5 | 4e-23 | 20/22 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.479×** | -9.7 | 6e-20 | 19/22 (SW 900, HS-578T, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.521×** | -8.6 | 1e-15 | 20/22 (C-33 A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.527×** | -8.4 | 4e-15 | 18/22 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.598×** | -6.7 | 1e-09 | 17/22 (HS-578T, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.605×** | -6.6 | 3e-09 | 17/22 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.715×** | -6.2 | 3e-08 | 18/22 (NCI-H1573, HS-578T, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.626×** | -6.1 | 5e-08 | 12/22 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.650×** | -5.7 | 8e-07 | 12/22 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.650×** | -5.6 | 8e-07 | 12/22 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.650×** | -5.6 | 8e-07 | 15/22 (HS-578T, NCI-H1573, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.653×** | -5.6 | 9e-07 | 15/22 (HS-578T, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.645×** | -5.5 | 1e-06 | 11/22 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.660×** | -5.5 | 2e-06 | 12/22 (NCI-H1573, HS-578T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7648. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 230 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -24.5) |
| [[NCI-H460 (line)]] | wt | 90.3 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -27.2) |
| [[NCI-H1573 (line)]] | alt | 50.3 | 1 (1 ⚠) | 10 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.22× (z +8.9) ⚠ cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.0635× (z -29.6) |
| [[C-33 A (line)]] | alt | 505 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -18.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.328× (z -14.6) |
| [[Hs 766T (line)]] | wt | 79.5 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -22.1) |
| [[NCI-H2030 (line)]] | alt | 138 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -21.0) |
| [[SW 900 (line)]] | alt | 97.1 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -17.0) |
| [[A-427 (line)]] | wt | 459 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -15.8) |
| [[HOP62 (line)]] | alt | 50.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -19.0) |
| [[NCI-H1792 (line)]] | alt | 143 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -22.2) |
| [[A-172 (line)]] | wt | 72.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -11.6) |
| [[A549 (line)]] | wt | 85.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -15.4) |
| [[H4 (line)]] | wt | 43.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0661× (z -18.9) |
| [[SNU-423 (line)]] | alt | 72.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -12.9) |
| [[SW 1088 (line)]] | alt | 72.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0654× (z -10.9) |
| [[A498 (line)]] | wt | 53.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -8.7) ⚠ cell-cycle shift, explains ~48% of this change |
| [[RPMI-7951 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0712× (z -10.6) ⚠ cell-cycle shift, explains ~48% of this change |
| [[AN3 CA (line)]] | alt | 6.36 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.04 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.35 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.11 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.00 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.71 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.26 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.44 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.76 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.88 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7648), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VEGFC]] | +0.72 | +0.75 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[AADACP1]] | +0.71 | +0.68 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SERPIND1]] | +0.70 | +0.59 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[CRLF2]] | +0.70 | +0.65 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[BMPER]] | +0.68 | +0.64 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[AADAC]] | +0.67 | +0.60 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[NHS]] | +0.66 | +0.70 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[PTGS2]] | +0.66 | +0.61 / +0.69 | both halves | 7e-06 | STRING 470 |
| [[SIRLNT]] | +0.64 | +0.66 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[KCNMA1]] | +0.62 | +0.72 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[STEAP1B-AS1]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[SGIP1]] | +0.61 | +0.61 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGD4]] | -0.55 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[ACSL1]] | -0.53 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[STOM]] | -0.51 | -0.51 / -0.42 | both halves | 4e-05 | pathway: RHOJ GTPase cycle; STRING 474 |
| [[EDN2]] | -0.49 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[FLVCR2]] | -0.49 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[MAOA]] | -0.49 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[COPS8]] | -0.49 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[RTN4RL1]] | -0.48 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[CCND3]] | -0.48 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ADGRG2]] | -0.48 | -0.43 / -0.48 | both halves | 4e-05 |  |
| [[KLF9]] | -0.47 | -0.52 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRG2]] | B | ADGRG2 activity raises GJA1's level | lines that do not express ADGRG2 (10) vs lines expressing it (40) | 3.53× lower at baseline in the lines without ADGRG2 | 0.046 | ⚠ within organs, on part of the lines; also absent: KCNN3, SLC17A7, STARD8; maybe low, not absent |
| [[NT5E]] | B | NT5E activity raises GJA1's level | lines that do not express NT5E (14) vs lines expressing it (36) | 3.25× lower at baseline in the lines without NT5E | 0.074 | ⚠ within organs, on part of the lines; also absent: MDFIC, PAPSS2, ENSG00000289526 |
| [[CYP26B1]] | B | CYP26B1 activity raises GJA1's level | lines that do not express CYP26B1 (23) vs lines expressing it (27) | 2.36× lower at baseline in the lines without CYP26B1 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000286385, ENSG00000242029, ELOVL2 |
| [[NR3C1]] | B | NR3C1 activity lowers GJA1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 7.3% of all compounds | 0.099 | ⚠ off-target possible; 3 compounds |
| [[GNG11]] | C | GNG11 activity raises GJA1's level | lines that do not express GNG11 (21) vs lines expressing it (29) | 5.58× lower at baseline in the lines without GNG11 | 0.011 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN; co-absent with the target |
| [[TWIST2]] | C | TWIST2 activity raises GJA1's level | lines that do not express TWIST2 (26) vs lines expressing it (24) | 6.16× lower at baseline in the lines without TWIST2 | 0.058 | ⚠ within organs, on part of the lines; also absent: TSHZ3, STAC, SALL1; co-absent with the target |
| [[RAB31]] | C | RAB31 activity raises GJA1's level | lines that do not express RAB31 (16) vs lines expressing it (34) | 7.24× lower at baseline in the lines without RAB31 | 0.065 | ⚠ within organs, on part of the lines; also absent: VEGFC, HERC5, NR3C1; co-absent with the target |
| [[SHISAL1]] | C | SHISAL1 activity raises GJA1's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 7.86× lower at baseline in the lines without SHISAL1 | 0.072 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11; co-absent with the target |
| [[IL1B]] | C | IL1B activity raises GJA1's level | lines that do not express IL1B (30) vs lines expressing it (20) | 3.60× lower at baseline in the lines without IL1B | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA; co-absent with the target |

### Downstream of this gene

*45 arrows, 45 of them with an alert ⚠; grade A 0, B 17, C 28. Shown: the 12 strongest; 33 more arrows (33 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VEGFC]] | B | GJA1 activity strengthens VEGFC's drug response | lines that do not express GJA1 (7) vs lines expressing it (20) | the lines without GJA1 respond 0.76× as strongly (z diff +2.25); strongest at Dinaciclib 0.05 µM: 0.69x vs 0.27x (z diff +6.0) | 0.023 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1; target measured in part of the lines; artifact flags |
| [[GLIS3]] | B | GJA1 activity raises GLIS3's level | lines that do not express GJA1 (26) vs lines expressing it (24) | 3.81× lower at baseline in the lines without GJA1 | 0.038 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1 |
| [[AGPAT4]] | B | GJA1 activity strengthens AGPAT4's drug response | lines that do not express GJA1 (21) vs lines expressing it (22) | the lines without GJA1 respond 0.86× as strongly (z diff +0.76); strongest at Dinaciclib 0.5 µM: 0.74x vs 0.42x (z diff +4.2) | 0.055 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1; target measured in part of the lines; both ways; artifact flags |
| [[SLC16A2]] | B | GJA1 activity raises SLC16A2's level | lines that do not express GJA1 (26) vs lines expressing it (24) | 3.11× lower at baseline in the lines without GJA1 | 0.055 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1 |
| cells under [[Doxycycline (monohydrate) (drug)]] 5 µM | B | GJA1 activity lowers the cells' numbers under Doxycycline (monohydrate) 5 µM (makes them more sensitive) | lines that do not express GJA1 (26) vs lines expressing it (22) | the lines without GJA1: 1.36× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1 |
| [[SMOX]] | B | GJA1 activity raises SMOX's level | lines that do not express GJA1 (26) vs lines expressing it (24) | 1.93× lower at baseline in the lines without GJA1 | 0.073 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1 |
| [[RAI14]] | B | GJA1 activity raises RAI14's level | lines that do not express GJA1 (26) vs lines expressing it (24) | 3.21× lower at baseline in the lines without GJA1 | 0.073 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1 |
| cells under [[Naproxen (drug)]] 5 µM | B | GJA1 activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express GJA1 (26) vs lines expressing it (22) | the lines without GJA1: 0.84× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1 |
| [[FGD4]] | B | GJA1 activity lowers FGD4's level | lines that do not express GJA1 (26) vs lines expressing it (24) | 2.40× higher at baseline in the lines without GJA1 | 0.076 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1 |
| cells under [[Malotilate (drug)]] 0.05 µM | B | GJA1 activity raises the cells' numbers under Malotilate 0.05 µM (protects the cells) | lines that do not express GJA1 (26) vs lines expressing it (22) | the lines without GJA1: 0.82× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1 |
| cells under [[Peretinoin (drug)]] 0.5 µM | B | GJA1 activity lowers the cells' numbers under Peretinoin 0.5 µM (makes them more sensitive) | lines that do not express GJA1 (26) vs lines expressing it (22) | the lines without GJA1: 1.39× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1 |
| cells under [[Cabozantinib (S-malate) (drug)]] 5 µM | B | GJA1 activity lowers the cells' numbers under Cabozantinib (S-malate) 5 µM (makes them more sensitive) | lines that do not express GJA1 (26) vs lines expressing it (22) | the lines without GJA1: 1.13× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1 |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.462). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.8, 16.0); signed map (19.3, 52.5). **Vector** length 100, 31.7% of its response variance represented; |z| ≥ 3 in 937 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +12.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +4.1 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.9 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.7 | +1.6 |
| fall | [[Clobetasol propionate (drug)]] 5 µM |  | -4.5 | -6.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.5 | -5.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -4.3 | -5.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.3 | -6.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.2 | -6.2 |

## What is on record

|  |  |
|---|---|
| Name | gap junction protein alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.31 — chr6:121,435,595-121,449,727 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CX43, ODD, ODOD, SDTY3; previously ODDD, GJAL |
| Gene groups (HGNC) | Gap junction proteins |
| Hallmark sets | UV_RESPONSE_DN, EPITHELIAL_MESENCHYMAL_TRANSITION, ESTROGEN_RESPONSE_EARLY |
| Reactome | 25 pathways, smallest: Oligomerization of connexins into connexons; Regulation of gap junction activity; Transport of connexins along the secretory pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P17302](https://www.uniprot.org/uniprotkb/P17302) (Gap junction alpha-1 protein):

> Structural component of the gap junction, a specialized intercellular structure consisting of a cluster of closely packed pairs of transmembrane channels, the connexons, that allow passage of small molecules and electrical signals between neighboring cells (By similarity). Forms homotypic and heterotypic channels gated by transjunctional voltage (By similarity). May play a critical role in the physiology of hearing by participating in the recycling of potassium to the cochlear endolymph …

**Summary**, from NCBI Gene [2697](https://www.ncbi.nlm.nih.gov/gene/2697):

> This gene is a member of the connexin gene family. The encoded protein is a component of gap junctions, which are composed of arrays of intercellular channels that provide a route for the diffusion of low molecular weight materials from cell to cell. The encoded protein is the major protein of gap junctions in the heart that are thought to have a crucial role in the synchronized contraction of the heart and in embryonic development. A related intronless pseudogene has been mapped to chromosome …

**Accessions** — [HGNC:4274](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4274) · Entrez [2697](https://www.ncbi.nlm.nih.gov/gene/2697) · UniProt [P17302](https://www.uniprot.org/uniprotkb/P17302) · Ensembl [ENSG00000152661](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152661)

## Data

Gene col 7648: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7648); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7648, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7648]; `tensor/DDL_lfc|DDL_z.npy` [7648]; `embed/gene_vectors.npy` [7648]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7648 or target_col == 7648). Every well: [[GJA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GJA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
