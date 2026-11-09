---
symbol: "SOX4"
type: "gene"
col: 4564
ensembl_id: "ENSG00000124766"
name: "SRY-box transcription factor 4"
location: "6p22.3"
module: 20
arm: "-"
pooled_cpm: 131.27
n_lines_expressing: 44
n_dd_up: 5
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# SOX4

*SRY-box transcription factor 4* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.74× (z +7.2, q 3e-10, up in 35 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.332× (z -5.3, q 7e-05, down in 33 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSX2]] (+0.68, fdr 1e-05), [[BTG1]] (+0.60, fdr 1e-05), [[BMF]] (+0.60, fdr 1e-05); moves opposite to [[RPN1]] (-0.58, fdr 3e-05), [[SMPD4]] (-0.55, fdr 2e-05), [[LY6G5B]] (-0.55, fdr 4e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAM107B]] → it (grade B ⚠); 4 go from it, the strongest it → [[DAAM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4564.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +7.2 | 3e-10 | 35/42 (HT-29, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +6.3 | 9e-08 | 25/43 (LoVo, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +4.0 | 0.010 | 29/43 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +3.8 | 0.018 | 24/42 (LoVo, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.49×** | +3.7 | 0.023 | 24/41 (A-172, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | 1.39× | +3.0 | 0.22 | 24/42 (HT-29, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4564.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.332×** | -5.3 | 7e-05 | 33/43 (SW 900, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.602×** | -4.4 | 0.004 | 29/42 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.419×** | -4.2 | 0.006 | 27/42 (AN3 CA, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.643×** | -4.0 | 0.008 | 29/42 (SW 900, NCI-H2347, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.655×** | -3.9 | 0.013 | 27/42 (SW480, SW 900, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.671×** | -3.6 | 0.027 | 27/42 (SW48, SW480, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.681×** | -3.5 | 0.038 | 25/42 (SW 900, NCI-H460, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.768×** | -3.4 | 0.050 | 28/42 (RPMI-7951, A-427, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.771×** | -3.3 | 0.054 | 21/42 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.708×** | -3.1 | 0.087 | 22/42 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.708×** | -3.1 | 0.087 | 19/42 (SW 900, NCI-H460, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.790× | -3.0 | 0.12 | 22/42 (NCI-H2030, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4564. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 873 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -19.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -15.4) |
| [[SW 900 (line)]] | alt | 273 | 0 | 8 (3 ⚠) | — | [[Budesonide (drug)]] 5 µM 0.179× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 317 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -19.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -10.2) |
| [[COLO 205 (line)]] | alt | 72.2 | 6 (2 ⚠) | 0 | [[Daptomycin (drug)]] 0.5 µM 5.84× (z +9.7) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 5 µM 6.13× (z +9.6) | — |
| [[NCI-H2347 (line)]] | alt | 375 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -14.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -10.4) |
| [[SW480 (line)]] | alt | 221 | 0 | 6 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.272× (z -10.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM 0.291× (z -9.2) |
| [[A-172 (line)]] | wt | 34.8 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.32× (z +16.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +11.3) | — |
| [[LoVo (line)]] | wt | 39.6 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.86× (z +15.5) | — |
| [[A498 (line)]] | wt | 69.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +18.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C-33 A (line)]] | alt | 502 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 114 | 2 | 0 | [[Binimetinib (drug)]] 5 µM 3.36× (z +8.8) | — |
| [[J82 (line)]] | alt | 106 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +13.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 169 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 34.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.69× (z +10.2) | — |
| [[HOP62 (line)]] | alt | 75.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 43.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 125 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +10.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HT-29 (line)]] | alt | 125 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.60× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 70.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.78× (z +14.1) | — |
| [[LS 180 (line)]] | wt | 212 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 3.85× (z +9.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H596 (line)]] | alt | 175 | 0 | 1 | — | [[olaparib (drug)]] 5 µM 0.0968× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 250 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.232× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 62.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 201 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 102 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +9.1) | — |
| [[SW48 (line)]] | wt | 130 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +11.0) | — |
| [[A-427 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 63.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 194 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.4 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 27.8 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 163 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.8 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 192 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.4 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 191 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4564), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSX2]] | +0.68 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[BTG1]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[BMF]] | +0.60 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[C15orf48]] | +0.58 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[BMP2]] | +0.56 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ZNF503]] | +0.56 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[FOXA2]] | +0.55 | +0.38 / +0.62 | both halves | 6e-05 |  |
| [[DAAM1]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 | pathway: Signaling by WNT |
| [[FOXC1]] | +0.54 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[MAF]] | +0.54 | +0.55 / +0.47 | both halves | 2e-05 | STRING 567 |
| [[RND1]] | +0.54 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[TLE3]] | +0.53 | +0.45 / +0.51 | both halves | 3e-05 | pathway: Deactivation of the beta-catenin transactivating complex |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPN1]] | -0.58 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[SMPD4]] | -0.55 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[LY6G5B]] | -0.55 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[ATL3]] | -0.54 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[IPO5]] | -0.53 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[UBQLN1]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[NDUFA10]] | -0.52 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[SPTLC1]] | -0.52 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[CMPK1]] | -0.51 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[DLST]] | -0.51 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[EIF3F]] | -0.51 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[FKBP9]] | -0.50 | -0.43 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM107B]] | B | FAM107B activity raises SOX4's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 1.71× lower at baseline in the lines without FAM107B | 0.047 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SOX4's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DAAM1]] | B | SOX4 activity raises DAAM1's level | lines that do not express SOX4 (6) vs lines expressing it (44) | 2.15× lower at baseline in the lines without SOX4 | 0.019 | ⚠ within organs, on part of the lines; also absent: B3GNT5, PLCXD2, PMEPA1; maybe low, not absent |
| [[TYMP]] | B | SOX4 activity raises TYMP's level | lines that do not express SOX4 (6) vs lines expressing it (44) | 3.48× lower at baseline in the lines without SOX4 | 0.028 | ⚠ within organs, on part of the lines; also absent: B3GNT5, PLCXD2, PMEPA1; maybe low, not absent |
| [[MSX2]] | B | SOX4 activity raises MSX2's level | lines that do not express SOX4 (6) vs lines expressing it (44) | 2.04× lower at baseline in the lines without SOX4 | 0.042 | ⚠ within organs, on part of the lines; also absent: B3GNT5, PLCXD2, PMEPA1; maybe low, not absent |
| [[ANKRD12]] | B | SOX4 activity lowers ANKRD12's level | lines that do not express SOX4 (6) vs lines expressing it (44) | 1.38× higher at baseline in the lines without SOX4 | 0.089 | ⚠ within organs, on part of the lines; also absent: B3GNT5, PLCXD2, PMEPA1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (25.6, -1.2); signed map (47.2, 9.6). **Vector** length 130, 40.4% of its response variance represented; |z| ≥ 3 in 1,170 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.8 | +7.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +4.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.0 | +2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.6 | +1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +2.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.2 | +3.0 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +2.9 | +2.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.8 | +2.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.8 | +2.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.8 | -0.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.7 | +0.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -4.4 | -4.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.1 | -3.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.9 | -3.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.8 | -3.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | SRY-box transcription factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:21,593,751-21,598,619 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | SRY-box transcription factors |
| Reactome | 3 pathways, smallest: Deactivation of the beta-catenin transactivating complex; TCF dependent signaling in response to WNT; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06945](https://www.uniprot.org/uniprotkb/Q06945) (Transcription factor SOX-4):

> Transcriptional activator that binds with high affinity to the T-cell enhancer motif 5'-AACAAAG-3' motif. Required for IL17A-producing Vgamma2-positive gamma-delta T-cell maturation and development, via binding to regulator loci of RORC to modulate expression (By similarity). Involved in skeletal myoblast differentiation by promoting gene expression of CALD1.

**Summary**, from NCBI Gene [6659](https://www.ncbi.nlm.nih.gov/gene/6659):

> This intronless gene encodes a member of the SOX (SRY-related HMG-box) family of transcription factors involved in the regulation of embryonic development and in the determination of the cell fate. The encoded protein may act as a transcriptional regulator after forming a protein complex with other proteins, such as syndecan binding protein (syntenin). The protein may function in the apoptosis pathway leading to cell death as well as to tumorigenesis and may mediate downstream effects of …

**Accessions** — [HGNC:11200](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11200) · Entrez [6659](https://www.ncbi.nlm.nih.gov/gene/6659) · UniProt [Q06945](https://www.uniprot.org/uniprotkb/Q06945) · Ensembl [ENSG00000124766](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124766)

## Data

Gene col 4564: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4564); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4564, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4564]; `tensor/DDL_lfc|DDL_z.npy` [4564]; `embed/gene_vectors.npy` [4564]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4564 or target_col == 4564). Every well: [[SOX4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOX4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
