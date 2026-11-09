---
symbol: "ZMAT4"
type: "gene"
col: 9060
ensembl_id: "ENSG00000165061"
name: "zinc finger matrin-type 4"
location: "8p11.21"
module: 152
arm: "+"
pooled_cpm: 11.66
n_lines_expressing: 19
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 15
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# ZMAT4

*zinc finger matrin-type 4* — 8p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.84× (z +20.4, q 0e+00, up in 17 of 17 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HS-578T 0.322×); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.275×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A549 0.231×); [[Budesonide (drug)]] 0.05 µM in 1 line (HS-578T 0.290×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIMP3]] (+0.66, fdr 7e-06), [[GUCY1B1]] (+0.63, fdr 1e-05), [[SYT11]] (+0.63, fdr 1e-05); moves opposite to [[TCEANC2]] (-0.47, fdr 1e-04).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NCAM1]] → it (grade C ⚠); 15 go from it, the strongest it → [[ITPR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9060.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.84×** | +20.4 | 0e+00 | 17/17 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.41×** | +13.1 | 5e-37 | 4/11 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +12.0 | 6e-31 | 4/14 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.99×** | +11.7 | 1e-29 | 16/16 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.72×** | +10.7 | 1e-24 | 15/15 (HS-578T, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.64×** | +10.0 | 1e-21 | 3/8 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.42×** | +9.5 | 2e-19 | 13/15 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +8.9 | 3e-17 | 4/14 (HOP62, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.16×** | +8.2 | 1e-14 | 6/15 (SHP-77, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.99×** | +7.4 | 8e-12 | 12/15 (HS-578T, SHP-77, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +7.0 | 1e-10 | 2/10 (SNU-423, NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.0 | 1e-07 | 5/17 (A-172, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +5.2 | 7e-06 | 13/16 (HS-578T, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +4.9 | 4e-05 | 7/15 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +4.6 | 2e-04 | 0/11 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.87×** | +3.5 | 0.014 | 8/16 (NCI-H23, HS-578T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.028 | 1/15 (NCI-H23) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.51×** | +3.2 | 0.044 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.071 | 2/17 (NCI-H1792, NCI-H460) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9060.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HS-578T 0.322×); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.275×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A549 0.231×); [[Budesonide (drug)]] 0.05 µM in 1 line (HS-578T 0.290×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.721× | -3.3 | 0.40 | 1/15 (NCI-H23) | inconsistent across doses |  |
| [[Decitabine (drug)]] 5 µM |  | 0.734× | -3.2 | 0.40 | 1/15 (NCI-H23) | top dose only |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.753× | -3.1 | 0.40 | 1/17 (SW 1088) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9060. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 138 | 2 | 2 | [[Panobinostat (drug)]] 5 µM 4.21× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -11.0) |
| [[HOP62 (line)]] | alt | 4.97 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 8.35× (z +12.1) | — |
| [[NCI-H23 (line)]] | alt | 2.98 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 11.7× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 4.42 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.77× (z +12.2) | — |
| [[SHP-77 (line)]] | alt | 251 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.33× (z +9.7) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.275× (z -10.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 27.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -9.8) |
| [[C32 (line)]] | wt | 21.1 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.105× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 4.63 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.35× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 5.09 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 17.6× (z +11.5) | — |
| [[SNU-423 (line)]] | alt | 4.55 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.94× (z +9.6) | — |
| [[A-172 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.76 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9060), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMP3]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[GUCY1B1]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[SYT11]] | +0.63 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[ARHGAP28]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[ALK]] | +0.62 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[CPA4]] | +0.62 | +0.57 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[TMEM108]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[ANOS1]] | +0.61 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[NCAM1]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[GAP43]] | +0.57 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[AFF2]] | +0.57 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[OR4F15]] | +0.56 | +0.47 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCEANC2]] | -0.47 | -0.37 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCAM1]] | C | NCAM1 activity raises ZMAT4's level | lines that do not express NCAM1 (34) vs lines expressing it (16) | 3.56× lower at baseline in the lines without NCAM1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, ENSG00000237268, SOX11; co-absent with the target |
| [[RNF17]] | C | RNF17 activity raises ZMAT4's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 4.71× lower at baseline in the lines without RNF17 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD; co-absent with the target |
| [[IGFBP5]] | C | IGFBP5 activity raises ZMAT4's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 4.08× lower at baseline in the lines without IGFBP5 | 0.031 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2; co-absent with the target |
| [[CACNA2D3]] | C | CACNA2D3 activity raises ZMAT4's level | lines that do not express CACNA2D3 (36) vs lines expressing it (14) | 2.94× lower at baseline in the lines without CACNA2D3 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NCAM1, LINC01287, LINC00824; co-absent with the target |
| [[LRP2]] | C | LRP2 activity raises ZMAT4's level | lines that do not express LRP2 (22) vs lines expressing it (28) | 2.68× lower at baseline in the lines without LRP2 | 0.087 | ⚠ within organs, on part of the lines; also absent: KCNJ6, COL15A1, AIM2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 2, C 13. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITPR1]] | B | ZMAT4 activity raises ITPR1's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 3.20× lower at baseline in the lines without ZMAT4 | 0.039 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11 |
| [[TRIM9]] | B | ZMAT4 activity raises TRIM9's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 3.51× lower at baseline in the lines without ZMAT4 | 0.082 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11 |
| [[SNAP25]] | C | ZMAT4 activity raises SNAP25's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 6.43× lower at baseline in the lines without ZMAT4 | 0.002 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11; co-absent with the target |
| [[RARB]] | C | ZMAT4 activity raises RARB's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 4.72× lower at baseline in the lines without ZMAT4 | 0.012 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11; co-absent with the target |
| [[DPYSL3]] | C | ZMAT4 activity raises DPYSL3's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 4.96× lower at baseline in the lines without ZMAT4 | 0.033 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11; co-absent with the target |
| [[NCAM1]] | C | ZMAT4 activity raises NCAM1's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 5.36× lower at baseline in the lines without ZMAT4 | 0.040 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11; co-absent with the target |
| [[LRP2]] | C | ZMAT4 activity raises LRP2's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 2.14× lower at baseline in the lines without ZMAT4 | 0.045 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11; co-absent with the target |
| [[CRTAC1]] | C | ZMAT4 activity raises CRTAC1's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 3.15× lower at baseline in the lines without ZMAT4 | 0.048 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11; co-absent with the target |
| [[LINC01411]] | C | ZMAT4 activity raises LINC01411's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 4.81× lower at baseline in the lines without ZMAT4 | 0.067 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11; co-absent with the target |
| [[TMEM178B]] | C | ZMAT4 activity raises TMEM178B's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 3.01× lower at baseline in the lines without ZMAT4 | 0.083 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11; co-absent with the target |
| [[SLFN11]] | C | ZMAT4 activity raises SLFN11's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 3.01× lower at baseline in the lines without ZMAT4 | 0.087 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11; co-absent with the target |
| [[MIR3681HG]] | C | ZMAT4 activity raises MIR3681HG's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 4.05× lower at baseline in the lines without ZMAT4 | 0.091 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11; co-absent with the target |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.686). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.9, 31.1); signed map (33.7, 33.6). **Vector** length 49.1, 13.0% of its response variance represented; |z| ≥ 3 in 462 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +20.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +13.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +6.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +1.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +2.6 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.4 | -0.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger matrin-type 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.21 — chr8:40,530,590-40,897,833 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13842 |
| Gene groups (HGNC) | Zinc fingers matrin-type |
| Matched by | ensembl_id |

UniProt [Q9H898](https://www.uniprot.org/uniprotkb/Q9H898) carries no function annotation.

**Summary**, from NCBI Gene [79698](https://www.ncbi.nlm.nih.gov/gene/79698):

> Enables identical protein binding activity. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25844](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25844) · Entrez [79698](https://www.ncbi.nlm.nih.gov/gene/79698) · UniProt [Q9H898](https://www.uniprot.org/uniprotkb/Q9H898) · Ensembl [ENSG00000165061](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165061)

## Data

Gene col 9060: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9060); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9060, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9060]; `tensor/DDL_lfc|DDL_z.npy` [9060]; `embed/gene_vectors.npy` [9060]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9060 or target_col == 9060). Every well: [[ZMAT4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZMAT4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
