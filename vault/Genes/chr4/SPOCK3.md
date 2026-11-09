---
symbol: "SPOCK3"
type: "gene"
col: 12130
ensembl_id: "ENSG00000196104"
name: "SPARC (osteonectin), cwcv and kazal like domains proteoglycan 3"
location: "4q32.3"
module: 9
arm: "+"
pooled_cpm: 4.23
n_lines_expressing: 28
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 4
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SPOCK3

*SPARC (osteonectin), cwcv and kazal like domains proteoglycan 3* — 4q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.22× (z +19.1, q 0e+00, up in 12 of 17 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 2 lines (HOP62 0.119×, Hs 766T 0.238×; ⚠ transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (Hs 766T 0.257×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (Hs 766T 0.161×; ⚠ cell-cycle shift, explains ~1% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Hs 766T 0.292×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (Hs 766T 0.204×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNC80]] (+0.72, fdr 7e-06), [[GRIA1]] (+0.70, fdr 7e-06), [[MIR325HG]] (+0.66, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ANGPT1]] → it (grade B ⚠); 4 go from it, the strongest it → [[SLC9A9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12130.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.22×** | +19.1 | 0e+00 | 12/17 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.86×** | +13.9 | 1e-41 | 18/22 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.28×** | +13.6 | 5e-40 | 5/11 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.53×** | +12.3 | 1e-32 | 10/18 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.61×** | +11.1 | 1e-26 | 2/6 (HOP62, CFPAC-1) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.30×** | +10.8 | 4e-25 | 3/6 (NCI-H1792, HOP62, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.58×** | +8.9 | 5e-17 | 12/20 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.20×** | +7.4 | 9e-12 | 15/19 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +6.0 | 2e-07 | 7/20 (HOP62, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.5 | 2e-06 | 8/22 (HEC-1-A, NCI-H460, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +4.9 | 5e-05 | 0/16 | top dose only | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.67×** | +4.8 | 8e-05 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.4 | 5e-04 | 1/13 (HOP62) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.51×** | +3.8 | 0.005 | 0/13 | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +3.7 | 0.007 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +3.4 | 0.024 | 6/21 (NCI-H23, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Apalutamide (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.025 | 0/22 | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.65×** | +3.3 | 0.025 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.031 | 2/20 (NCI-H460, A498) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.031 | 9/22 (NCI-H1792, NCI-H2347, …) | rises with dose | position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.031 | 1/13 (HOP62) | inconsistent across doses |  |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.042 | 1/18 (HOP62) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12130.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 2 lines (HOP62 0.119×, Hs 766T 0.238×; ⚠ transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (Hs 766T 0.257×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (Hs 766T 0.161×; ⚠ cell-cycle shift, explains ~1% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Hs 766T 0.292×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (Hs 766T 0.204×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.904× | -3.5 | 0.27 | 7/23 (CFPAC-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.703× | -3.1 | 0.58 | 2/21 (NCI-H460, NCI-H2347) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12130. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 75.4 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -11.5) |
| [[HOP62 (line)]] | alt | 6.82 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +8.5) | [[Docetaxel (drug)]] 0.05 µM 0.119× (z -9.1) ⚠ transcription drop |
| [[CFPAC-1 (line)]] | alt | 4.20 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.73× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 1.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.1× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 1.25 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.26× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 43.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.774 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.848 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.955 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.949 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.846 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.952 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.902 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.967 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.842 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.872 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.890 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.971 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.862 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.875 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.890 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.841 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.953 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.885 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12130), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC80]] | +0.72 | +0.73 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[GRIA1]] | +0.70 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[MIR325HG]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[COL21A1]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[TLL1]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 | pathway: Degradation of the extracellular matrix |
| [[GPM6A]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[GUCY1A1]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[PLCL1]] | +0.62 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[PPFIA2]] | +0.61 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[LDB2]] | +0.61 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[MAPK10]] | +0.60 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[RALYL]] | +0.60 | +0.60 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANGPT1]] | B | ANGPT1 activity raises SPOCK3's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 1.84× lower at baseline in the lines without ANGPT1 | 0.033 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5 |
| [[CCN3]] | B | CCN3 activity raises SPOCK3's level | lines that do not express CCN3 (20) vs lines expressing it (30) | 1.77× lower at baseline in the lines without CCN3 | 0.040 | ⚠ within organs, on part of the lines; also absent: SNAI2, FAR2, ENSG00000228033 |
| [[GAS7]] | B | GAS7 activity lowers SPOCK3's level | lines that do not express GAS7 (24) vs lines expressing it (26) | 1.26× higher at baseline in the lines without GAS7 | 0.047 | ⚠ within organs, on part of the lines; also absent: COLEC12, ADCY1, MAPK4 |
| [[NYAP2]] | B | NYAP2 activity raises SPOCK3's level | lines that do not express NYAP2 (16) vs lines expressing it (34) | 1.82× lower at baseline in the lines without NYAP2 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, CHSY3, AIM2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SPOCK3's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CHRNA7]] | B | CHRNA7 activity lowers SPOCK3's level | lines that do not express CHRNA7 (19) vs lines expressing it (31) | 1.61× higher at baseline in the lines without CHRNA7 | 0.062 | ⚠ within organs, on part of the lines; also absent: LRRC4B, NKD2, IGFL4; maybe low, not absent |
| [[KCTD8]] | C | KCTD8 activity raises SPOCK3's level | lines that do not express KCTD8 (30) vs lines expressing it (20) | 2.33× lower at baseline in the lines without KCTD8 | 0.034 | ⚠ within organs, on part of the lines; also absent: NOL4, DSCAM, IQCA1; co-absent with the target |
| [[SULF1]] | C | SULF1 activity raises SPOCK3's level | lines that do not express SULF1 (35) vs lines expressing it (15) | 1.95× lower at baseline in the lines without SULF1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00958, LINC01592, TBXT; co-absent with the target |
| [[CDH6]] | C | CDH6 activity raises SPOCK3's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 2.23× lower at baseline in the lines without CDH6 | 0.063 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC9A9]] | B | SPOCK3 activity raises SLC9A9's level | lines that do not express SPOCK3 (22) vs lines expressing it (28) | 2.33× lower at baseline in the lines without SPOCK3 | 0.017 | ⚠ within organs, on part of the lines; also absent: CTSF, NCAM2, LRP1B; maybe low, not absent |
| [[GRIP2]] | B | SPOCK3 activity lowers GRIP2's level | lines that do not express SPOCK3 (22) vs lines expressing it (28) | 1.26× higher at baseline in the lines without SPOCK3 | 0.036 | ⚠ within organs, on part of the lines; also absent: CTSF, NCAM2, LRP1B; maybe low, not absent |
| [[CCN3]] | B | SPOCK3 activity raises CCN3's level | lines that do not express SPOCK3 (22) vs lines expressing it (28) | 2.12× lower at baseline in the lines without SPOCK3 | 0.060 | ⚠ within organs, on part of the lines; also absent: CTSF, NCAM2, LRP1B; maybe low, not absent |
| [[CHRNA7]] | B | SPOCK3 activity lowers CHRNA7's level | lines that do not express SPOCK3 (22) vs lines expressing it (28) | 1.62× higher at baseline in the lines without SPOCK3 | 0.092 | ⚠ within organs, on part of the lines; also absent: CTSF, NCAM2, LRP1B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.1, 29.9); signed map (34.2, 18.1). **Vector** length 40.7, 7.65% of its response variance represented; |z| ≥ 3 in 567 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +13.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +11.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +5.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +3.2 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -3.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -1.4 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | SPARC (osteonectin), cwcv and kazal like domains proteoglycan 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.3 — chr4:166,733,384-167,234,796 (-) |
| Ensembl biotype | protein_coding |
| Also known as | testican-3 |
| Gene groups (HGNC) | SPARC family |
| Reactome | 3 pathways, smallest: Activation of Matrix Metalloproteinases; Degradation of the extracellular matrix; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQ16](https://www.uniprot.org/uniprotkb/Q9BQ16) (Testican-3):

> May participate in diverse steps of neurogenesis. Inhibits the processing of pro-matrix metalloproteinase 2 (MMP-2) by MT1-MMP and MT3-MMP. May interfere with tumor invasion.

**Summary**, from NCBI Gene [50859](https://www.ncbi.nlm.nih.gov/gene/50859):

> This gene encodes a member of a novel family of calcium-binding proteoglycan proteins that contain thyroglobulin type-1 and Kazal-like domains. The encoded protein and may play a role in adult T-cell leukemia by inhibiting the activity of membrane-type matrix metalloproteinases. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:13565](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13565) · Entrez [50859](https://www.ncbi.nlm.nih.gov/gene/50859) · UniProt [Q9BQ16](https://www.uniprot.org/uniprotkb/Q9BQ16) · Ensembl [ENSG00000196104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196104)

## Data

Gene col 12130: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12130); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12130, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12130]; `tensor/DDL_lfc|DDL_z.npy` [12130]; `embed/gene_vectors.npy` [12130]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12130 or target_col == 12130). Every well: [[SPOCK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPOCK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
