---
symbol: "C5orf34"
type: "gene"
col: 10228
ensembl_id: "ENSG00000172244"
name: "chromosome 5 open reading frame 34"
location: "5p12"
module: 91
arm: "+"
pooled_cpm: 14.59
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 8
n_dd_up_clean: 24
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# C5orf34

*chromosome 5 open reading frame 34* — 5p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.67× (z +23.1, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.762× (z -6.5, q 5e-08, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF85]] (+0.83, fdr 7e-06), [[ZNF100]] (+0.69, fdr 7e-06), [[ZNF563]] (+0.69, fdr 1e-05); moves opposite to [[RSU1]] (-0.58, fdr 7e-05), [[CADM4]] (-0.56, fdr 1e-04), [[KIAA0930]] (-0.54, fdr 4e-05).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10228.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.67×** | +23.1 | 0e+00 | 43/47 (J82, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +20.3 | 0e+00 | 43/46 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.20×** | +18.6 | 0e+00 | 47/48 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.82×** | +14.1 | 5e-43 | 35/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +12.8 | 2e-35 | 39/45 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.20×** | +12.6 | 3e-34 | 33/42 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **2.10×** | +12.3 | 8e-33 | 39/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +12.2 | 2e-32 | 38/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.75×** | +9.3 | 9e-19 | 37/47 (C-33 A, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +9.1 | 4e-18 | 26/47 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.72×** | +9.0 | 7e-18 | 32/47 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +7.8 | 2e-13 | 27/47 (SW480, C32, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.54×** | +7.1 | 5e-11 | 23/47 (NCI-H2347, J82, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +7.1 | 7e-11 | 20/48 (J82, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.50×** | +6.7 | 8e-10 | 21/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +6.4 | 6e-09 | 23/48 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +6.1 | 3e-08 | 25/48 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10228.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.762×** | -6.5 | 5e-08 | 25/48 (HOP62, Hs 766T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.721×** | -5.3 | 4e-05 | 17/26 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.770×** | -4.4 | 0.002 | 17/36 (NCI-H23, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.816×** | -3.4 | 0.069 | 9/48 (Panc 03.27, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Omeprazole (drug)]] 0.05 µM |  | **0.817×** | -3.4 | 0.069 | 4/48 (NCI-H2347, LS 180, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.810×** | -3.4 | 0.069 | 7/48 (HCT15, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **0.822×** | -3.3 | 0.069 | 5/47 (SW1417, LoVo, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.823×** | -3.3 | 0.069 | 16/46 (NCI-H23, COLO 205, …) | rises with dose |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.833× | -3.1 | 0.12 | 2/48 (HS-578T, SW480) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.834× | -3.1 | 0.12 | 6/47 (SW 900, SW 1271, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10228. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 13.5 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +14.6) | — |
| [[J82 (line)]] | alt | 25.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +15.5) | — |
| [[NCI-H2347 (line)]] | alt | 12.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +13.8) | — |
| [[SW1417 (line)]] | alt | 17.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -8.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 25.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +11.4) | — |
| [[AN3 CA (line)]] | alt | 38.1 | 0 | 2 (1 ⚠) | — | [[LJI308 (drug)]] 0.05 µM 0.0857× (z -9.6) |
| [[HS-578T (line)]] | alt | 12.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 17.6 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.10× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 11.1 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 4.03× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 15.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +10.2) | — |
| [[A-172 (line)]] | wt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +9.7) | — |
| [[A-427 (line)]] | wt | 17.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.46× (z +10.2) | — |
| [[BT-474 (line)]] | alt | 8.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 16.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 8.40 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.5 µM 0.0666× (z -9.6) |
| [[KATO III (line)]] | alt | 9.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +8.5) | — |
| [[LoVo (line)]] | wt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 12.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 9.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.17× (z +12.5) | — |
| [[NCI-H23 (line)]] | alt | 32.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 45.9 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0842× (z -8.9) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 20.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +11.9) | — |
| [[RKO (line)]] | wt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 23.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +8.6) | — |
| [[A498 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10228), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF85]] | +0.83 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[ZNF100]] | +0.69 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[ZNF563]] | +0.69 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[ZNF101]] | +0.66 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[ZNF138]] | +0.65 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[ZNF714]] | +0.65 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ZNF273]] | +0.64 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[CENPL]] | +0.64 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ZNF257]] | +0.64 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[C1orf112]] | +0.62 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[ZNF442]] | +0.62 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[CSTF3-DT]] | +0.61 | +0.60 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSU1]] | -0.58 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[CADM4]] | -0.56 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[KIAA0930]] | -0.54 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[CYP2E1]] | -0.54 | -0.25 / -0.49 | both halves | 4e-04 |  |
| [[SCART1]] | -0.54 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[NOMO1]] | -0.54 | -0.50 / -0.32 | both halves | 1e-04 |  |
| [[TECPR1]] | -0.52 | -0.44 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[ST6GALNAC4]] | -0.51 | -0.56 / -0.27 | both halves | 3e-04 |  |
| [[GTDC1]] | -0.50 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[GTF2E2]] | -0.50 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[SLC23A2]] | -0.50 | -0.40 / -0.25 | both halves | 4e-04 |  |
| [[SMYD3]] | -0.50 | -0.43 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[LRFN3]] | -0.49 | -0.52 / -0.22 | both halves | 6e-04 |  |
| [[GALNS]] | -0.49 | -0.47 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers C5orf34's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PODXL2]] | B | PODXL2 activity raises C5orf34's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.39× lower at baseline in the lines without PODXL2 | 0.078 | ⚠ within organs, on part of the lines |
| [[ZNF724]] | B | ZNF724 activity raises C5orf34's level | lines that do not express ZNF724 (8) vs lines expressing it (42) | 1.38× lower at baseline in the lines without ZNF724 | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000283201, ENSG00000269237, ZNF577 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.730). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-45.4, -46.9); signed map (-39.9, -35.0). **Vector** length 93.0, 20.9% of its response variance represented; |z| ≥ 3 in 1,152 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.53 to 5); *Resolution of D-loop Structures through Holliday Junction Intermediates* (reactome, mean cos +0.53 to 4); *Resolution of D-Loop Structures* (reactome, mean cos +0.53 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.5 | +14.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +12.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.4 | +18.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.1 | +9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +20.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.1 | +9.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +4.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +7.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +3.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.4 | -6.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.4 | +3.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | -5.2 | +5.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.7 | +0.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -4.6 | +4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | +1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -0.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 5 open reading frame 34 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p12 — chr5:43,486,709-43,515,148 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32363 |
| Matched by | ensembl_id |

UniProt [Q96MH7](https://www.uniprot.org/uniprotkb/Q96MH7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:24738](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24738) · Entrez [375444](https://www.ncbi.nlm.nih.gov/gene/375444) · UniProt [Q96MH7](https://www.uniprot.org/uniprotkb/Q96MH7) · Ensembl [ENSG00000172244](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172244)

## Data

Gene col 10228: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10228); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10228, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10228]; `tensor/DDL_lfc|DDL_z.npy` [10228]; `embed/gene_vectors.npy` [10228]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10228 or target_col == 10228). Every well: [[C5orf34 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C5orf34.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
