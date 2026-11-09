---
symbol: "SIM1"
type: "gene"
col: 3343
ensembl_id: "ENSG00000112246"
name: "SIM bHLH transcription factor 1"
location: "6q16.3"
module: 9
arm: "+"
pooled_cpm: 2.9
n_lines_expressing: 7
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 22
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SIM1

*SIM bHLH transcription factor 1* — 6q16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.46× (z +12.4, q 1e-32, up in 3 of 4 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Mebendazole (drug)]] 5 µM: 0.491× (z -4.0, q 0.031, down in 2 of 5 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Belumosudil (drug)]] 5 µM in 1 line (J82 0.0607×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DOK5]] (+0.73, fdr 7e-06), [[PTGIS]] (+0.65, fdr 2e-05), [[CDH6]] (+0.62, fdr 1e-05); moves opposite to [[SLC26A2]] (-0.41, fdr 4e-04), [[TBC1D16]] (-0.40, fdr 7e-05), [[MTG1]] (-0.38, fdr 2e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[DACH1]] → it (grade C ⚠); 22 go from it, the strongest it → [[GRIA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3343.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.46×** | +12.4 | 1e-32 | 3/4 (HEC-1-A, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.76×** | +10.8 | 1e-24 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.47×** | +10.0 | 4e-21 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.78×** | +9.5 | 2e-19 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.95×** | +9.0 | 4e-17 | 1/4 (HEC-1-A) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.82×** | +6.1 | 1e-07 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.50×** | +5.2 | 2e-05 | 0/4 | top dose only | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.45×** | +5.0 | 3e-05 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.29×** | +4.9 | 7e-05 | 1/4 (HEC-1-A) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.90×** | +4.5 | 5e-04 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +4.1 | 0.002 | 2/4 (HEC-1-A, SNU-423) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.89×** | +3.7 | 0.009 | 3/4 (J82, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.57×** | +3.7 | 0.009 | 0/5 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.40×** | +3.7 | 0.010 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | **1.50×** | +3.3 | 0.031 | 0/4 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3343.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Belumosudil (drug)]] 5 µM in 1 line (J82 0.0607×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mebendazole (drug)]] 5 µM |  | **0.491×** | -4.0 | 0.031 | 2/5 (SNU-423, HEC-1-A) | top dose only |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.577× | -3.3 | 0.27 | 1/5 (SNU-423) | inconsistent across doses | position effect removed |
| [[Procainamide (hydrochloride) (drug)]] 0.5 µM |  | 0.589× | -3.1 | 0.27 | 1/5 (LOX-IMVI) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.567× | -3.1 | 0.27 | 0/5 | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.585× | -3.0 | 0.27 | 0/5 | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3343. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 4.92 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0607× (z -9.3) |
| [[A-172 (line)]] | wt | 0.356 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.311 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.308 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.314 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.313 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.350 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.443 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.383 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.577 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.313 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.904 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.307 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.338 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.284 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.327 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.454 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.276 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3343), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOK5]] | +0.73 | +0.65 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[PTGIS]] | +0.65 | +0.48 / +0.66 | both halves | 2e-05 | **novel candidate** |
| [[CDH6]] | +0.62 | +0.62 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[PCDH18]] | +0.57 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[GRIA1]] | +0.56 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[SULF1]] | +0.55 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[ECSCR]] | +0.55 | +0.52 / +0.41 | both halves | 4e-05 | **novel candidate** |
| [[GUCY1A1]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[PTPRB]] | +0.54 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[SLC14A1]] | +0.53 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[SPOCK3]] | +0.52 | +0.56 / +0.33 | both halves | 1e-04 |  |
| [[HTR1F]] | +0.50 | +0.47 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC26A2]] | -0.41 | -0.26 / -0.44 | both halves | 4e-04 |  |
| [[TBC1D16]] | -0.40 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[MTG1]] | -0.38 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[JCAD]] | -0.38 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[PPP2R2C]] | -0.38 | -0.32 / -0.33 | both halves | 1e-04 |  |
| [[HIPK2]] | -0.38 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[FMNL2]] | -0.37 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[HMGA2]] | -0.37 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[LDLRAD3]] | -0.37 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[ATP2C2]] | -0.36 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[MT1A]] | -0.36 | -0.41 / -0.23 | both halves | 5e-04 |  |
| [[USP31]] | -0.36 | -0.30 / -0.35 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DACH1]] | C | DACH1 activity raises SIM1's level | lines that do not express DACH1 (30) vs lines expressing it (20) | 1.49× lower at baseline in the lines without DACH1 | 0.045 | ⚠ within organs, on part of the lines; also absent: FGF20, CSMD3, XKR7; co-absent with the target |
| [[DOK5]] | C | DOK5 activity raises SIM1's level | lines that do not express DOK5 (40) vs lines expressing it (10) | 1.32× lower at baseline in the lines without DOK5 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230258, IGFBP5; co-absent with the target |
| [[CDH6]] | C | CDH6 activity raises SIM1's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 2.09× lower at baseline in the lines without CDH6 | 0.093 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC; co-absent with the target |
| [[CCDC190]] | C | CCDC190 activity raises SIM1's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 1.95× lower at baseline in the lines without CCDC190 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337; co-absent with the target |
| [[LINC01435]] | C | LINC01435 activity raises SIM1's level | lines that do not express LINC01435 (37) vs lines expressing it (13) | 1.63× lower at baseline in the lines without LINC01435 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000203434, TMPRSS15, ENSG00000224865; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 6, C 16. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRIA1]] | B | SIM1 activity raises GRIA1's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 2.08× lower at baseline in the lines without SIM1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5 |
| [[MN1]] | B | SIM1 activity raises MN1's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 2.50× lower at baseline in the lines without SIM1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5 |
| [[MIR325HG]] | B | SIM1 activity raises MIR325HG's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 1.90× lower at baseline in the lines without SIM1 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5 |
| [[MECOM]] | B | SIM1 activity raises MECOM's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 2.68× lower at baseline in the lines without SIM1 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5 |
| [[LRIG3]] | B | SIM1 activity raises LRIG3's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 2.11× lower at baseline in the lines without SIM1 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5 |
| [[LDB2]] | B | SIM1 activity raises LDB2's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 1.49× lower at baseline in the lines without SIM1 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5 |
| [[ECSCR]] | C | SIM1 activity raises ECSCR's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 2.36× lower at baseline in the lines without SIM1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5; co-absent with the target |
| [[SULF1]] | C | SIM1 activity raises SULF1's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 5.03× lower at baseline in the lines without SIM1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5; co-absent with the target |
| [[UGT1A6]] | C | SIM1 activity raises UGT1A6's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 1.95× lower at baseline in the lines without SIM1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5; co-absent with the target |
| [[NPPB]] | C | SIM1 activity raises NPPB's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 2.30× lower at baseline in the lines without SIM1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5; co-absent with the target |
| [[SLC14A1]] | C | SIM1 activity raises SLC14A1's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 1.86× lower at baseline in the lines without SIM1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5; co-absent with the target |
| [[DOK5]] | C | SIM1 activity raises DOK5's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 2.32× lower at baseline in the lines without SIM1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.264). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.6, 20.3); signed map (35.4, 30.4). **Vector** length 19.1, 6.57% of its response variance represented; |z| ≥ 3 in 161 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.1 | +12.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +0.7 | +0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.7 | +2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +0.7 | +9.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +0.7 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.6 | +2.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +0.5 | -0.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.5 | +1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.5 | +2.4 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -0.5 | -1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.5 | +0.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -0.5 | -0.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.4 | -0.2 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | SIM bHLH transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q16.3 — chr6:100,385,009-100,464,921 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bHLHe14 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; PAS domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P81133](https://www.uniprot.org/uniprotkb/P81133) (Single-minded homolog 1):

> Transcriptional factor that may have pleiotropic effects during embryogenesis and in the adult.

**Summary**, from NCBI Gene [6492](https://www.ncbi.nlm.nih.gov/gene/6492):

> SIM1 and SIM2 genes are Drosophila single-minded (sim) gene homologs. SIM1 transcript was detected only in fetal kidney out of various adult and fetal tissues tested. Since the sim gene plays an important role in Drosophila development and has peak levels of expression during the period of neurogenesis,it was proposed that the human SIM gene is a candidate for involvement in certain dysmorphic features (particularly the facial and skull characteristics), abnormalities of brain development, …

**Accessions** — [HGNC:10882](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10882) · Entrez [6492](https://www.ncbi.nlm.nih.gov/gene/6492) · UniProt [P81133](https://www.uniprot.org/uniprotkb/P81133) · Ensembl [ENSG00000112246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112246)

## Data

Gene col 3343: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3343); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3343, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3343]; `tensor/DDL_lfc|DDL_z.npy` [3343]; `embed/gene_vectors.npy` [3343]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3343 or target_col == 3343). Every well: [[SIM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
