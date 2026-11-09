---
symbol: "FAM171B"
type: "gene"
col: 6872
ensembl_id: "ENSG00000144369"
name: "family with sequence similarity 171 member B"
location: "2q32.1"
module: 52
arm: "-"
pooled_cpm: 24.13
n_lines_expressing: 43
n_dd_up: 28
n_dd_down: 4
n_dd_up_clean: 21
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 6
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# FAM171B

*family with sequence similarity 171 member B* — 2q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.06× (z +23.3, q 0e+00, up in 38 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 0.682× (z -4.1, q 0.027, down in 18 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STK26]] (+0.57, fdr 1e-05), [[CCDC136]] (+0.56, fdr 1e-05), [[CACHD1]] (+0.54, fdr 7e-06); moves opposite to [[ACAD10]] (-0.63, fdr 2e-05), [[ZNF333]] (-0.58, fdr 8e-05), [[DGCR2]] (-0.55, fdr 3e-05).
> It sits in the **-** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[FAM184A]] → it (grade B ⚠); 6 go from it, the strongest it → [[CYP2U1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6872.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.06×** | +23.3 | 0e+00 | 38/41 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.02×** | +14.7 | 0e+00 | 37/41 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.40×** | +12.9 | 1e-35 | 34/40 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.33×** | +12.4 | 2e-33 | 38/40 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.25×** | +11.9 | 9e-31 | 28/40 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.72×** | +11.2 | 3e-27 | 34/41 (NCI-H2347, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.10×** | +10.5 | 7e-24 | 32/40 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.88×** | +9.3 | 1e-18 | 27/40 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.80×** | +8.7 | 3e-16 | 28/40 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.80×** | +8.6 | 4e-16 | 25/40 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +8.6 | 4e-16 | 29/40 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.66×** | +7.4 | 5e-12 | 27/40 (RKO, A549, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.71×** | +7.4 | 5e-12 | 25/41 (HOP62, H4, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.64×** | +6.9 | 3e-10 | 25/40 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.49×** | +6.5 | 4e-09 | 20/33 (HOP62, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +6.3 | 1e-08 | 24/40 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~18% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6872.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.682×** | -4.1 | 0.027 | 18/39 (HCT15, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | **0.719×** | -3.5 | 0.089 | 13/40 (SNU-1, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.793×** | -3.5 | 0.089 | 15/40 (hTERT-HPNE, CHP-212, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.725×** | -3.4 | 0.089 | 11/40 (SNU-1, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 0.795× | -3.3 | 0.11 | 13/40 (AN3 CA, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6872. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.6 | 6 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.16× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 20.0 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +12.4) | — |
| [[RKO (line)]] | wt | 28.9 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +11.9) | — |
| [[HOP62 (line)]] | alt | 12.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.91× (z +16.2) | — |
| [[A498 (line)]] | wt | 29.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +13.7) | — |
| [[AN3 CA (line)]] | alt | 95.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -10.9) |
| [[H4 (line)]] | wt | 27.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 12.6× (z +11.8) | — |
| [[J82 (line)]] | alt | 9.89 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +11.6) | — |
| [[NCI-H1792 (line)]] | alt | 53.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +12.8) | — |
| [[NCI-H2347 (line)]] | alt | 17.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +15.6) | — |
| [[SW 900 (line)]] | alt | 44.0 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.73× (z +8.5) | [[Docetaxel (drug)]] 0.05 µM 0.185× (z -10.9) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 24.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +10.6) | — |
| [[A-427 (line)]] | wt | 46.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -11.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 14.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.95× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[C32 (line)]] | wt | 13.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 12.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.37× (z +15.1) | — |
| [[HCT15 (line)]] | alt | 47.4 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0576× (z -11.1) |
| [[HS-578T (line)]] | alt | 11.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 6.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 44.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.67× (z +15.7) | — |
| [[LoVo (line)]] | wt | 22.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +13.6) | — |
| [[NCI-H1573 (line)]] | alt | 14.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +13.3) | — |
| [[NCI-H2030 (line)]] | alt | 37.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.31× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 30.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +14.4) | — |
| [[RPMI-7951 (line)]] | alt | 16.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 92.9 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0858× (z -10.4) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 17.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 31.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.50× (z +8.8) | — |
| [[SW48 (line)]] | wt | 15.8 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0791× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.38 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.40 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 76.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.02 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 413 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 31.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6872), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK26]] | +0.57 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[CCDC136]] | +0.56 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[CACHD1]] | +0.54 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[ENPP4]] | +0.53 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[TUSC3]] | +0.52 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[PDGFD]] | +0.52 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[ABLIM1]] | +0.52 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[TRAK1]] | +0.51 | +0.33 / +0.63 | both halves | 1e-04 |  |
| [[CCN3]] | +0.51 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[C8orf88]] | +0.50 | +0.36 / +0.55 | both halves | 9e-05 |  |
| [[TSPAN6]] | +0.50 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[RFK]] | +0.50 | +0.39 / +0.63 | both halves | 6e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACAD10]] | -0.63 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[ZNF333]] | -0.58 | -0.64 / -0.37 | both halves | 8e-05 |  |
| [[DGCR2]] | -0.55 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[KIAA0319L]] | -0.55 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[WDR53]] | -0.54 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[USP20]] | -0.54 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[C19orf25]] | -0.54 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[ANKS3]] | -0.52 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[FBH1]] | -0.52 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[PGS1]] | -0.51 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[CRAMP1]] | -0.51 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[FBXL12]] | -0.51 | -0.48 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM184A]] | B | FAM184A activity raises FAM171B's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 2.36× lower at baseline in the lines without FAM184A | 0.026 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[C8orf88]] | B | C8orf88 activity raises FAM171B's level | lines that do not express C8orf88 (12) vs lines expressing it (38) | 2.49× lower at baseline in the lines without C8orf88 | 0.060 | ⚠ within organs, on part of the lines; also absent: TUSC3, MAP9, BVES-AS1; maybe low, not absent |
| [[CCDC169]] | B | CCDC169 activity raises FAM171B's level | lines that do not express CCDC169 (17) vs lines expressing it (33) | 1.80× lower at baseline in the lines without CCDC169 | 0.074 | ⚠ within organs, on part of the lines; also absent: SPART-AS1, SPART, FIGN; its own permutation p |
| [[MPDZ]] | B | MPDZ activity raises FAM171B's level | lines that do not express MPDZ (17) vs lines expressing it (33) | 2.17× lower at baseline in the lines without MPDZ | 0.078 | ⚠ within organs, on part of the lines; also absent: GNB4, BVES, BVES-AS1 |
| [[CFL2]] | C | CFL2 activity raises FAM171B's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 4.88× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP2U1]] | B | FAM171B activity raises CYP2U1's level | lines that do not express FAM171B (7) vs lines expressing it (43) | 1.97× lower at baseline in the lines without FAM171B | 0.044 | ⚠ within organs, on part of the lines; also absent: NXPE3, GXYLT2, TMOD2; maybe low, not absent |
| [[MPDZ]] | B | FAM171B activity raises MPDZ's level | lines that do not express FAM171B (7) vs lines expressing it (43) | 6.59× lower at baseline in the lines without FAM171B | 0.049 | ⚠ within organs, on part of the lines; also absent: NXPE3, GXYLT2, TMOD2; maybe low, not absent |
| [[CCDC169]] | B | FAM171B activity raises CCDC169's level | lines that do not express FAM171B (7) vs lines expressing it (43) | 2.93× lower at baseline in the lines without FAM171B | 0.058 | ⚠ within organs, on part of the lines; also absent: NXPE3, GXYLT2, TMOD2; maybe low, not absent |
| [[CFL2]] | B | FAM171B activity raises CFL2's level | lines that do not express FAM171B (7) vs lines expressing it (43) | 2.37× lower at baseline in the lines without FAM171B | 0.064 | ⚠ within organs, on part of the lines; also absent: NXPE3, GXYLT2, TMOD2; maybe low, not absent |
| [[C8orf88]] | B | FAM171B activity raises C8orf88's level | lines that do not express FAM171B (7) vs lines expressing it (43) | 3.00× lower at baseline in the lines without FAM171B | 0.089 | ⚠ within organs, on part of the lines; also absent: NXPE3, GXYLT2, TMOD2; maybe low, not absent |
| [[NXPE3]] | C | FAM171B activity raises NXPE3's level | lines that do not express FAM171B (7) vs lines expressing it (43) | 3.59× lower at baseline in the lines without FAM171B | 0.033 | ⚠ within organs, on part of the lines; also absent: NXPE3, GXYLT2, TMOD2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **-** arm (projection on the module's main direction -0.452). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-14.4, 22.9); signed map (29.7, 25.2). **Vector** length 102, 25.3% of its response variance represented; |z| ≥ 3 in 1,085 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.0 | +14.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.3 | +12.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +8.4 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +7.2 | +11.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +4.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.2 | +3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +5.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +3.1 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | -0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -0.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | +9.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | +0.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.0 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -1.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 171 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.1 — chr2:186,694,060-186,765,959 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34104; previously KIAA1946 |
| Matched by | ensembl_id |

UniProt [Q6P995](https://www.uniprot.org/uniprotkb/Q6P995) carries no function annotation.

**Summary**, from NCBI Gene [165215](https://www.ncbi.nlm.nih.gov/gene/165215):

> Predicted to be located in membrane. Predicted to be active in synapse. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29412](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29412) · Entrez [165215](https://www.ncbi.nlm.nih.gov/gene/165215) · UniProt [Q6P995](https://www.uniprot.org/uniprotkb/Q6P995) · Ensembl [ENSG00000144369](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144369)

## Data

Gene col 6872: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6872); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6872, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6872]; `tensor/DDL_lfc|DDL_z.npy` [6872]; `embed/gene_vectors.npy` [6872]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6872 or target_col == 6872). Every well: [[FAM171B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM171B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
