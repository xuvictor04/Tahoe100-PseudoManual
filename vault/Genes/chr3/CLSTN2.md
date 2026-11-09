---
symbol: "CLSTN2"
type: "gene"
col: 8146
ensembl_id: "ENSG00000158258"
name: "calsyntenin 2"
location: "3q23"
module: 61
arm: "+"
pooled_cpm: 11.77
n_lines_expressing: 20
n_dd_up: 35
n_dd_down: 0
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# CLSTN2

*calsyntenin 2* — 3q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.07× (z +25.1, q 0e+00, up in 8 of 12 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (SW480 0.321×; ⚠ transcription drop).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NTRK3]] (+0.54, fdr 1e-05), [[VIPR2]] (+0.53, fdr 4e-05), [[FBLN2]] (+0.49, fdr 6e-05); moves opposite to [[GLE1]] (-0.47, fdr 1e-04), [[TCEANC2]] (-0.46, fdr 2e-04), [[PEX11B]] (-0.45, fdr 1e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[OSBP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8146.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.07×** | +25.1 | 0e+00 | 8/12 (A-172, SW1417, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.65×** | +23.8 | 0e+00 | 11/13 (A-172, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **3.26×** | +18.3 | 0e+00 | 13/15 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **4.82×** | +17.2 | 0e+00 | 16/17 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.12×** | +15.5 | 0e+00 | 15/16 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.94×** | +15.0 | 0e+00 | 6/10 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.79×** | +14.6 | 0e+00 | 16/17 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.79×** | +14.0 | 9e-43 | 5/7 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.46×** | +13.6 | 4e-40 | 10/14 (A-172, SW1417, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.30×** | +12.1 | 8e-32 | 3/7 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.74×** | +11.0 | 2e-26 | 7/12 (A-172, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.53×** | +10.2 | 1e-22 | 16/17 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +9.2 | 2e-18 | 6/13 (BT-474, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +9.0 | 8e-18 | 5/13 (H4, A-172, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.26×** | +8.9 | 2e-17 | 12/14 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +6.9 | 1e-10 | 3/13 (A-172, C-33 A, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.87×** | +6.6 | 2e-09 | 8/16 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +6.3 | 8e-09 | 5/15 (BT-474, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.1 | 9e-06 | 2/17 (A-172, H4) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8146.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (SW480 0.321×; ⚠ transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.815× | -3.2 | 0.51 | 0/16 | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8146. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 31.8 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +19.0) | — |
| [[NCI-H1573 (line)]] | alt | 3.26 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 60.6× (z +17.5) | — |
| [[SW480 (line)]] | alt | 76.8 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +12.5) | [[Docetaxel (drug)]] 0.05 µM 0.321× (z -8.6) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 46.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +21.5) | — |
| [[H4 (line)]] | wt | 4.86 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 45.6× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 14.2 | 1 | 0 | [[Retinoic acid (drug)]] 5 µM 5.40× (z +9.1) | — |
| [[J82 (line)]] | alt | 39.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.56× (z +15.4) | — |
| [[SHP-77 (line)]] | alt | 33.6 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 6.42× (z +8.7) ⚠ unreliable plate only | — |
| [[SW 900 (line)]] | alt | 4.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +9.8) | — |
| [[A-427 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.98 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8146), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NTRK3]] | +0.54 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[VIPR2]] | +0.53 | +0.40 / +0.51 | both halves | 4e-05 |  |
| [[FBLN2]] | +0.49 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[FAM110B]] | +0.47 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[SH3GL2]] | +0.47 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[STON2]] | +0.46 | +0.36 / +0.50 | both halves | 9e-05 |  |
| [[TMEFF2]] | +0.46 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[PGBD5]] | +0.45 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[OLFM2]] | +0.45 | +0.41 / +0.40 | both halves | 4e-05 |  |
| [[GFRA1]] | +0.45 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[RGS7]] | +0.45 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[C1orf226]] | +0.45 | +0.31 / +0.42 | both halves | 2e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLE1]] | -0.47 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[TCEANC2]] | -0.46 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[PEX11B]] | -0.45 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[TRAPPC13]] | -0.45 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[NIF3L1]] | -0.43 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[ZNF500]] | -0.42 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[WDR53]] | -0.41 | -0.16 / -0.42 | ⚠ not reproduced | 0.001 |  |
| [[TMED8]] | -0.41 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[CDADC1]] | -0.41 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[EIF4ENIF1]] | -0.41 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[EXOSC1]] | -0.41 | -0.33 / -0.27 | both halves | 3e-04 |  |
| [[DZANK1]] | -0.40 | -0.29 / -0.49 | both halves | 3e-04 |  |
| [[ASB7]] | -0.40 | -0.36 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CLSTN2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[C11orf96]] | B | C11orf96 activity raises CLSTN2's level | lines that do not express C11orf96 (17) vs lines expressing it (33) | 2.00× lower at baseline in the lines without C11orf96 | 0.073 | ⚠ within organs, on part of the lines; also absent: UPK1A-AS1, ZNF569, PPP1R3C |
| [[PDLIM3]] | B | PDLIM3 activity raises CLSTN2's level | lines that do not express PDLIM3 (18) vs lines expressing it (32) | 2.08× lower at baseline in the lines without PDLIM3 | 0.084 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, SOX5, PTX3 |
| [[PGBD5]] | C | PGBD5 activity raises CLSTN2's level | lines that do not express PGBD5 (28) vs lines expressing it (22) | 2.62× lower at baseline in the lines without PGBD5 | 0.029 | ⚠ within organs, on part of the lines; also absent: TMEM163, LRRN1, ELAVL2; co-absent with the target |
| [[STXBP5L]] | C | STXBP5L activity raises CLSTN2's level | lines that do not express STXBP5L (35) vs lines expressing it (15) | 2.56× lower at baseline in the lines without STXBP5L | 0.048 | ⚠ within organs, on part of the lines; also absent: PCSK1, ENSG00000287211, GABRG2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSBP2]] | B | CLSTN2 activity raises OSBP2's level | lines that do not express CLSTN2 (30) vs lines expressing it (20) | 1.21× lower at baseline in the lines without CLSTN2 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, CCDC144NL-AS1, ENSG00000264660 |
| [[CDADC1]] | B | CLSTN2 activity raises CDADC1's level | lines that do not express CLSTN2 (30) vs lines expressing it (20) | 1.07× lower at baseline in the lines without CLSTN2 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, CCDC144NL-AS1, ENSG00000264660 |
| [[STXBP5L]] | C | CLSTN2 activity raises STXBP5L's level | lines that do not express CLSTN2 (30) vs lines expressing it (20) | 2.55× lower at baseline in the lines without CLSTN2 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, CCDC144NL-AS1, ENSG00000264660; co-absent with the target |
| [[GPNMB]] | C | CLSTN2 activity raises GPNMB's level | lines that do not express CLSTN2 (30) vs lines expressing it (20) | 2.80× lower at baseline in the lines without CLSTN2 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, CCDC144NL-AS1, ENSG00000264660; co-absent with the target |
| [[COLEC12]] | C | CLSTN2 activity raises COLEC12's level | lines that do not express CLSTN2 (30) vs lines expressing it (20) | 2.95× lower at baseline in the lines without CLSTN2 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, CCDC144NL-AS1, ENSG00000264660; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.493). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.7, 35.3); signed map (33.1, 23.7). **Vector** length 38.9, 8.46% of its response variance represented; |z| ≥ 3 in 438 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +18.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +14.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +6.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +0.8 | +1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.8 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.7 | +1.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.7 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.0 | -2.9 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.7 | -1.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -0.6 | -0.2 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -0.6 | -1.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -0.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | calsyntenin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q23 — chr3:139,935,185-140,577,397 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CSTN2, CS2, FLJ39113, CDHR13 |
| Gene groups (HGNC) | Cadherin related |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4D0](https://www.uniprot.org/uniprotkb/Q9H4D0) (Calsyntenin-2):

> Postsynaptic adhesion molecule that binds to presynaptic neurexins to mediate synapse formation, and which is involved in learning and memory (By similarity). Promotes synapse development by acting as a cell adhesion molecule at the postsynaptic membrane, which associates with neurexin-alpha at the presynaptic membrane (By similarity).

**Summary**, from NCBI Gene [64084](https://www.ncbi.nlm.nih.gov/gene/64084):

> Predicted to enable cell-cell adhesion mediator activity. Predicted to be involved in homophilic cell-cell adhesion; positive regulation of synapse assembly; and positive regulation of synaptic transmission. Predicted to be located in several cellular components, including Golgi membrane; postsynaptic density; and postsynaptic membrane. Predicted to be active in cell surface and postsynaptic density membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17448](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17448) · Entrez [64084](https://www.ncbi.nlm.nih.gov/gene/64084) · UniProt [Q9H4D0](https://www.uniprot.org/uniprotkb/Q9H4D0) · Ensembl [ENSG00000158258](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158258)

## Data

Gene col 8146: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8146); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8146, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8146]; `tensor/DDL_lfc|DDL_z.npy` [8146]; `embed/gene_vectors.npy` [8146]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8146 or target_col == 8146). Every well: [[CLSTN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLSTN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
