---
symbol: "TOR4A"
type: "gene"
col: 12533
ensembl_id: "ENSG00000198113"
name: "torsin family 4 member A"
location: "9q34.3"
module: 34
arm: "+"
pooled_cpm: 8.56
n_lines_expressing: 36
n_dd_up: 4
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 12
direction_downstream: 24
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# TOR4A

*torsin family 4 member A* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.85× (z +8.3, q 6e-14, up in 24 of 30 measured lines) ⚠ transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.37× (z +4.2, q 0.004, up in 12 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.552× (z -11.4, q 2e-27, down in 26 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEK2]] (+0.70, fdr 7e-06), [[EPHA2]] (+0.69, fdr 7e-06), [[PXN]] (+0.67, fdr 7e-06); moves opposite to [[RBKS]] (-0.55, fdr 5e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[PLEK2]] → it (grade B ⚠); 24 go from it, the strongest it → [[PLEKHM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12533.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.85×** | +8.3 | 6e-14 | 24/30 (LOX-IMVI, MIA PaCa-2, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~9% here); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.49×** | +5.4 | 2e-05 | 12/34 (A-172, RKO, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +4.2 | 0.004 | 12/33 (A498, HOP62, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.033 | 11/34 (AsPC-1, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | 1.40× | +3.2 | 0.13 | 2/32 (CFPAC-1, Panc 03.27) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.26× | +3.2 | 0.15 | 7/33 (KATO III, HEC-1-A, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.27× | +3.1 | 0.15 | 9/33 (HOP62, A-172, …) | all doses, flat |  |
| [[Rosiglitazone (drug)]] 5 µM |  | 1.27× | +3.1 | 0.15 | 7/32 (A549, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.17× | +3.0 | 0.15 | 4/33 (HEC-1-A, A549, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, none with an alert; shown: the 15 strongest. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12533.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.552×** | -11.4 | 2e-27 | 26/33 (HT-29, LS 180, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.580×** | -7.1 | 3e-10 | 18/32 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.693×** | -7.1 | 3e-10 | 17/32 (MIA PaCa-2, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.683×** | -6.6 | 5e-09 | 25/33 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.680×** | -6.3 | 3e-08 | 20/33 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.652×** | -6.3 | 3e-08 | 21/33 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.641×** | -5.8 | 5e-07 | 17/32 (A-172, NCI-H2030, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.658×** | -5.3 | 9e-06 | 15/33 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.699×** | -5.3 | 9e-06 | 17/33 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.707×** | -4.7 | 1e-04 | 14/33 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.721×** | -4.5 | 4e-04 | 13/33 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.728×** | -4.2 | 0.001 | 15/33 (AsPC-1, PANC-1, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.565×** | -4.1 | 0.002 | 10/33 (LS 180, HCT15, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.815×** | -3.9 | 0.003 | 10/33 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.580×** | -3.9 | 0.004 | 10/33 (COLO 205, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12533. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 11.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -11.9) |
| [[KATO III (line)]] | alt | 23.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -12.0) |
| [[A-172 (line)]] | wt | 28.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -9.3) |
| [[A549 (line)]] | wt | 11.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -10.4) |
| [[HT-29 (line)]] | alt | 15.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -13.2) |
| [[LS 180 (line)]] | wt | 15.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -12.1) |
| [[Hs 766T (line)]] | wt | 10.5 | 0 | 1 | — | [[vincristine (drug)]] 0.5 µM 0.0794× (z -8.8) |
| [[J82 (line)]] | alt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -9.3) |
| [[LoVo (line)]] | wt | 15.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 7.69 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change |
| [[NCI-H460 (line)]] | wt | 4.95 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.116× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 7.56 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -9.1) |
| [[RKO (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.197× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[SW480 (line)]] | alt | 7.43 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -9.9) |
| [[A-427 (line)]] | wt | 0.754 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.950 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.810 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.90 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.826 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12533), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEK2]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[EPHA2]] | +0.69 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[PXN]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[MYEOV]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[S100A16]] | +0.65 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[CDCP1]] | +0.64 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[GJB3]] | +0.64 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[PAQR5]] | +0.63 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[ASAP2]] | +0.62 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[ARHGEF4]] | +0.62 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[NTSR1]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[LAMC2]] | +0.62 | +0.61 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBKS]] | -0.55 | -0.56 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 8, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEK2]] | B | PLEK2 activity raises TOR4A's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 2.29× lower at baseline in the lines without PLEK2 | 0.047 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[LAMC2]] | B | LAMC2 activity raises TOR4A's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 2.39× lower at baseline in the lines without LAMC2 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[NIBAN2]] | B | NIBAN2 activity raises TOR4A's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 3.61× lower at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[CDYL2]] | B | CDYL2 activity raises TOR4A's level | lines that do not express CDYL2 (19) vs lines expressing it (31) | 2.10× lower at baseline in the lines without CDYL2 | 0.061 | ⚠ within organs, on part of the lines; also absent: B3GALT5, BCL11B, ENSG00000225330 |
| [[MAP2K1]] | B | MAP2K1 activity raises TOR4A's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[MICAL2]] | B | MICAL2 activity raises TOR4A's level | lines that do not express MICAL2 (11) vs lines expressing it (39) | 2.48× lower at baseline in the lines without MICAL2 | 0.084 | ⚠ within organs, on part of the lines; also absent: UBA7, ENSG00000285906, SERPINB1 |
| [[EPHA2]] | B | EPHA2 activity raises TOR4A's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 3.05× lower at baseline in the lines without EPHA2 | 0.085 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |
| [[MYEOV]] | B | MYEOV activity raises TOR4A's level | lines that do not express MYEOV (19) vs lines expressing it (31) | 2.03× lower at baseline in the lines without MYEOV | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000260877, MALL, LAMC2 |
| [[S100A16]] | C | S100A16 activity raises TOR4A's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 3.14× lower at baseline in the lines without S100A16 | 0.013 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2; co-absent with the target |
| [[PTK6]] | C | PTK6 activity raises TOR4A's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 2.84× lower at baseline in the lines without PTK6 | 0.028 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent; co-absent with the target |
| [[CDCP1]] | C | CDCP1 activity raises TOR4A's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 2.74× lower at baseline in the lines without CDCP1 | 0.059 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C; co-absent with the target |
| [[FLNB]] | C | FLNB activity raises TOR4A's level | lines that do not express FLNB (3) vs lines expressing it (47) | 3.43× lower at baseline in the lines without FLNB | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent; its own permutation p |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 21, C 3. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHM1]] | B | TOR4A activity raises PLEKHM1's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 1.77× lower at baseline in the lines without TOR4A | 0.015 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[PLEK2]] | B | TOR4A activity raises PLEK2's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 4.33× lower at baseline in the lines without TOR4A | 0.017 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[EHD1]] | B | TOR4A activity raises EHD1's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 1.74× lower at baseline in the lines without TOR4A | 0.019 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[PLEKHM1P1]] | B | TOR4A activity raises PLEKHM1P1's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 1.55× lower at baseline in the lines without TOR4A | 0.021 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[BCAR3]] | B | TOR4A activity raises BCAR3's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 1.86× lower at baseline in the lines without TOR4A | 0.021 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[NIBAN2]] | B | TOR4A activity raises NIBAN2's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 2.12× lower at baseline in the lines without TOR4A | 0.023 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[MYEOV]] | B | TOR4A activity raises MYEOV's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 2.82× lower at baseline in the lines without TOR4A | 0.025 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[NT5E]] | B | TOR4A activity raises NT5E's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 2.43× lower at baseline in the lines without TOR4A | 0.028 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[DUSP5]] | B | TOR4A activity raises DUSP5's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 2.57× lower at baseline in the lines without TOR4A | 0.031 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[FLNB]] | B | TOR4A activity raises FLNB's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 1.87× lower at baseline in the lines without TOR4A | 0.032 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[ITGA2]] | B | TOR4A activity raises ITGA2's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 2.87× lower at baseline in the lines without TOR4A | 0.033 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[FOSL1]] | B | TOR4A activity raises FOSL1's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 2.38× lower at baseline in the lines without TOR4A | 0.033 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.0, 3.0); signed map (5.3, 40.2). **Vector** length 64.1, 12.7% of its response variance represented; |z| ≥ 3 in 687 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | -0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | -2.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.5 | +8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.4 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.6 | -6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -6.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -7.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.9 | -5.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.9 | -6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | torsin family 4 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,277,726-137,282,641 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20245; previously C9orf167 |
| Gene groups (HGNC) | Torsins |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

UniProt [Q9NXH8](https://www.uniprot.org/uniprotkb/Q9NXH8) carries no function annotation.

**Summary**, from NCBI Gene [54863](https://www.ncbi.nlm.nih.gov/gene/54863):

> Predicted to enable ATP binding activity and ATP hydrolysis activity. Predicted to be located in extracellular region and platelet alpha granule lumen. Predicted to be active in endoplasmic reticulum lumen and nuclear envelope. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25981](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25981) · Entrez [54863](https://www.ncbi.nlm.nih.gov/gene/54863) · UniProt [Q9NXH8](https://www.uniprot.org/uniprotkb/Q9NXH8) · Ensembl [ENSG00000198113](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198113)

## Data

Gene col 12533: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12533); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12533, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12533]; `tensor/DDL_lfc|DDL_z.npy` [12533]; `embed/gene_vectors.npy` [12533]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12533 or target_col == 12533). Every well: [[TOR4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOR4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
