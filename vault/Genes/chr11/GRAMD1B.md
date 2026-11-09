---
symbol: "GRAMD1B"
type: "gene"
col: 339
ensembl_id: "ENSG00000023171"
name: "GRAM domain containing 1B"
location: "11q24.1"
module: 19
arm: "+"
pooled_cpm: 178.79
n_lines_expressing: 19
n_dd_up: 8
n_dd_down: 22
n_dd_up_clean: 5
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 8
direction_downstream: 12
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# GRAMD1B

*GRAM domain containing 1B* — 11q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.92× (z +7.8, q 4e-12, up in 0 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.42× (z +5.9, q 1e-06, up in 4 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.444× (z -13.6, q 1e-39, down in 17 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGIP1]] (+0.74, fdr 7e-06), [[SMOC1]] (+0.67, fdr 7e-06), [[EYA2]] (+0.63, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[STC1]] → it (grade C ⚠); 12 go from it, the strongest it → [[BMPER]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 339.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +7.8 | 4e-12 | 0/18 | two highest doses | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +5.9 | 1e-06 | 4/17 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +4.8 | 3e-04 | 1/17 (SK-MEL-2) | two highest doses | cell-cycle shift (explains ~11% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.5 | 1e-03 | 9/17 (MIA PaCa-2, NCI-H1792, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.059 | 5/18 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.071 | 4/18 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.32×** | +3.3 | 0.071 | 4/17 (SW 900, HOP62, …) | inconsistent across doses |  |
| [[Meloxicam (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.071 | 3/17 (NCI-H1792, H4, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.30× | +3.2 | 0.10 | 0/17 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.30× | +3.0 | 0.15 | 1/19 (NCI-H1573) | top dose only | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 339.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.444×** | -13.6 | 1e-39 | 17/17 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.408×** | -10.7 | 5e-24 | 17/17 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.443×** | -9.3 | 3e-18 | 17/17 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.561×** | -6.9 | 1e-09 | 14/17 (SW 900, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.654×** | -4.7 | 4e-04 | 9/17 (NCI-H460, SK-MEL-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.693×** | -4.3 | 0.001 | 10/17 (NCI-H460, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.696×** | -4.3 | 0.001 | 12/17 (SW 900, H4, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.696×** | -4.3 | 0.001 | 14/18 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.704×** | -4.2 | 0.002 | 9/17 (H4, RPMI-7951, …) | all doses, flat | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -4.1 | 0.002 | 4/19 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.720×** | -3.9 | 0.005 | 9/17 (HT-29, RPMI-7951, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.729×** | -3.7 | 0.008 | 1/17 (RPMI-7951) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.778×** | -3.7 | 0.008 | 11/17 (NCI-H460, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.731×** | -3.7 | 0.008 | 10/17 (RPMI-7951, hTERT-HPNE, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.803×** | -3.6 | 0.012 | 4/17 (SK-MEL-2, NCI-H460, …) | all doses, flat |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.741×** | -3.5 | 0.014 | 6/17 (NCI-H1792, H4, …) | two highest doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.758×** | -3.3 | 0.034 | 8/17 (NCI-H1792, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 339. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 714 | 0 | 15 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -14.3) |
| [[NCI-H23 (line)]] | alt | 1,369 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0460× (z -30.6) |
| [[LOX-IMVI (line)]] | wt | 293 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -15.0) |
| [[NCI-H2030 (line)]] | alt | 1,958 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0953× (z -18.7) |
| [[HT-29 (line)]] | alt | 148 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -12.3) |
| [[A549 (line)]] | wt | 164 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0818× (z -18.7) |
| [[SW 900 (line)]] | alt | 74.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -10.3) |
| [[hTERT-HPNE (line)]] | wt | 131 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 77.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0765× (z -13.7) |
| [[NCI-H1573 (line)]] | alt | 644 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0503× (z -19.1) |
| [[HOP62 (line)]] | alt | 150 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -14.7) |
| [[RPMI-7951 (line)]] | alt | 98.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -11.6) |
| [[SHP-77 (line)]] | alt | 88.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -10.8) |
| [[H4 (line)]] | wt | 115 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 54.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -9.1) |
| [[A-172 (line)]] | wt | 39.3 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 9.95 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 25.5 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 19.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 13.5 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 29.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 19.7 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 15.8 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 13.3 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 13.3 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 14.6 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 89.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 24.3 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 14.3 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 16.2 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.6 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 17.8 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 13.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 26.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 27.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 17.9 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 15.2 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 15.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 339), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGIP1]] | +0.74 | +0.74 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SMOC1]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[EYA2]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[SERPIND1]] | +0.62 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[STC1]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[ST8SIA4]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[AMOTL1]] | +0.60 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[TCF4]] | +0.60 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[UNC5D]] | +0.60 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[CRLF2]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[GNG11]] | +0.58 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[SH2D2A]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STC1]] | C | STC1 activity raises GRAMD1B's level | lines that do not express STC1 (24) vs lines expressing it (26) | 4.19× lower at baseline in the lines without STC1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP; co-absent with the target |
| [[F2RL2]] | C | F2RL2 activity raises GRAMD1B's level | lines that do not express F2RL2 (32) vs lines expressing it (18) | 4.83× lower at baseline in the lines without F2RL2 | 0.010 | ⚠ within organs, on part of the lines; also absent: SRGN, KCNMA1, PAPPA; co-absent with the target |
| [[PAPPA]] | C | PAPPA activity raises GRAMD1B's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 4.46× lower at baseline in the lines without PAPPA | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |
| [[NDNF]] | C | NDNF activity raises GRAMD1B's level | lines that do not express NDNF (25) vs lines expressing it (25) | 3.64× lower at baseline in the lines without NDNF | 0.058 | ⚠ within organs, on part of the lines; also absent: ADAM23, GUCY1B1, CNRIP1; co-absent with the target |
| [[EPGN]] | C | EPGN activity raises GRAMD1B's level | lines that do not express EPGN (41) vs lines expressing it (9) | 6.52× lower at baseline in the lines without EPGN | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, TBXT, ENSG00000289418; co-absent with the target |
| [[RSPO3]] | C | RSPO3 activity raises GRAMD1B's level | lines that do not express RSPO3 (39) vs lines expressing it (11) | 7.38× lower at baseline in the lines without RSPO3 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2; co-absent with the target |
| [[GJA1]] | C | GJA1 activity raises GRAMD1B's level | lines that do not express GJA1 (26) vs lines expressing it (24) | 3.12× lower at baseline in the lines without GJA1 | 0.082 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1; co-absent with the target |
| [[GLIS3]] | C | GLIS3 activity raises GRAMD1B's level | lines that do not express GLIS3 (21) vs lines expressing it (29) | 2.82× lower at baseline in the lines without GLIS3 | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 3, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMPER]] | B | GRAMD1B activity raises BMPER's level | lines that do not express GRAMD1B (31) vs lines expressing it (19) | 2.26× lower at baseline in the lines without GRAMD1B | 0.088 | ⚠ within organs, on part of the lines; also absent: MAGEB2, CD38, ENSG00000253503 |
| [[SMOX]] | B | GRAMD1B activity raises SMOX's level | lines that do not express GRAMD1B (31) vs lines expressing it (19) | 2.10× lower at baseline in the lines without GRAMD1B | 0.095 | ⚠ within organs, on part of the lines; also absent: MAGEB2, CD38, ENSG00000253503 |
| [[RASSF8]] | B | GRAMD1B activity raises RASSF8's level | lines that do not express GRAMD1B (31) vs lines expressing it (19) | 3.09× lower at baseline in the lines without GRAMD1B | 0.097 | ⚠ within organs, on part of the lines; also absent: MAGEB2, CD38, ENSG00000253503 |
| [[STC1]] | C | GRAMD1B activity raises STC1's level | lines that do not express GRAMD1B (31) vs lines expressing it (19) | 6.77× lower at baseline in the lines without GRAMD1B | 0.005 | ⚠ within organs, on part of the lines; also absent: MAGEB2, CD38, ENSG00000253503; co-absent with the target |
| [[F2RL2]] | C | GRAMD1B activity raises F2RL2's level | lines that do not express GRAMD1B (31) vs lines expressing it (19) | 2.45× lower at baseline in the lines without GRAMD1B | 0.021 | ⚠ within organs, on part of the lines; also absent: MAGEB2, CD38, ENSG00000253503; co-absent with the target |
| [[VEGFC]] | C | GRAMD1B activity raises VEGFC's level | lines that do not express GRAMD1B (31) vs lines expressing it (19) | 3.94× lower at baseline in the lines without GRAMD1B | 0.031 | ⚠ within organs, on part of the lines; also absent: MAGEB2, CD38, ENSG00000253503; co-absent with the target |
| [[PDE7B]] | C | GRAMD1B activity raises PDE7B's level | lines that do not express GRAMD1B (31) vs lines expressing it (19) | 2.87× lower at baseline in the lines without GRAMD1B | 0.037 | ⚠ within organs, on part of the lines; also absent: MAGEB2, CD38, ENSG00000253503; co-absent with the target |
| [[GLIS3]] | C | GRAMD1B activity raises GLIS3's level | lines that do not express GRAMD1B (31) vs lines expressing it (19) | 2.59× lower at baseline in the lines without GRAMD1B | 0.040 | ⚠ within organs, on part of the lines; also absent: MAGEB2, CD38, ENSG00000253503; co-absent with the target |
| [[PAPPA]] | C | GRAMD1B activity raises PAPPA's level | lines that do not express GRAMD1B (31) vs lines expressing it (19) | 3.76× lower at baseline in the lines without GRAMD1B | 0.042 | ⚠ within organs, on part of the lines; also absent: MAGEB2, CD38, ENSG00000253503; co-absent with the target |
| [[LGSN]] | C | GRAMD1B activity raises LGSN's level | lines that do not express GRAMD1B (31) vs lines expressing it (19) | 3.30× lower at baseline in the lines without GRAMD1B | 0.057 | ⚠ within organs, on part of the lines; also absent: MAGEB2, CD38, ENSG00000253503; co-absent with the target |
| [[TCF4]] | C | GRAMD1B activity raises TCF4's level | lines that do not express GRAMD1B (31) vs lines expressing it (19) | 3.36× lower at baseline in the lines without GRAMD1B | 0.070 | ⚠ within organs, on part of the lines; also absent: MAGEB2, CD38, ENSG00000253503; co-absent with the target |
| [[NDNF]] | C | GRAMD1B activity raises NDNF's level | lines that do not express GRAMD1B (31) vs lines expressing it (19) | 2.66× lower at baseline in the lines without GRAMD1B | 0.077 | ⚠ within organs, on part of the lines; also absent: MAGEB2, CD38, ENSG00000253503; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.547). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.2, 16.8); signed map (20.2, 52.8). **Vector** length 85.6, 33.8% of its response variance represented; |z| ≥ 3 in 623 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.1 | -1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +1.1 |
|  | [[Vitamin K4 (drug)]] 0.05 µM |  | +1.8 | +2.6 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.9 | -4.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.7 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.9 | -4.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.8 | -3.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.4 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | GRAM domain containing 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.1 — chr11:123,358,428-123,627,774 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LAMb, KIAA1201; previously LINC01059 |
| Gene groups (HGNC) | GRAM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3KR37](https://www.uniprot.org/uniprotkb/Q3KR37) (Protein Aster-B):

> Cholesterol transporter that mediates non-vesicular transport of cholesterol from the plasma membrane (PM) to the endoplasmic reticulum (ER) (By similarity). Contains unique domains for binding cholesterol and the PM, thereby serving as a molecular bridge for the transfer of cholesterol from the PM to the ER (By similarity). Plays a crucial role in cholesterol homeostasis in the adrenal gland and has the unique ability to localize to the PM based on the level of membrane cholesterol (By …

**Summary**, from NCBI Gene [57476](https://www.ncbi.nlm.nih.gov/gene/57476):

> Enables cholesterol transfer activity. Involved in lysosome to ER cholesterol transport. Located in endoplasmic reticulum; endoplasmic reticulum-plasma membrane contact site; and plasma membrane. Is active in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29214](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29214) · Entrez [57476](https://www.ncbi.nlm.nih.gov/gene/57476) · UniProt [Q3KR37](https://www.uniprot.org/uniprotkb/Q3KR37) · Ensembl [ENSG00000023171](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000023171)

## Data

Gene col 339: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 339); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 339, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 339]; `tensor/DDL_lfc|DDL_z.npy` [339]; `embed/gene_vectors.npy` [339]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 339 or target_col == 339). Every well: [[GRAMD1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRAMD1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
