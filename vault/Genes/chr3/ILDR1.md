---
symbol: "ILDR1"
type: "gene"
col: 6957
ensembl_id: "ENSG00000145103"
name: "immunoglobulin like domain containing receptor 1"
location: "3q13.33"
module: 27
arm: "+"
pooled_cpm: 2.26
n_lines_expressing: 19
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 55
direction_downstream: 54
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# ILDR1

*immunoglobulin like domain containing receptor 1* — 3q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.92× (z +11.1, q 9e-26, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.54× (z +9.5, q 4e-19, up in 1 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 4 lines (NCI-H1573 0.0280×, SW480 0.0693×, HCT15 0.0375×, CFPAC-1 0.109×); [[Digitoxin (drug)]] 0.5 µM in 2 lines (SW480 0.0822×, NCI-H2347 0.0568×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.112×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00992]] (+0.69, fdr 7e-06), [[LINC02253]] (+0.69, fdr 1e-05), [[CDX2]] (+0.66, fdr 8e-06); moves opposite to [[PSD3]] (-0.49, fdr 3e-05), [[SENP5]] (-0.46, fdr 5e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 55 arrows point to it, the strongest [[MANSC1]] → it (grade B ⚠); 54 go from it, the strongest it → [[TMEM184A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6957.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.92×** | +11.1 | 9e-26 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.54×** | +9.5 | 4e-19 | 1/14 (LoVo) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.92×** | +9.1 | 1e-17 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.38×** | +8.8 | 2e-16 | 1/10 (NCI-H1573) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.25×** | +8.3 | 1e-14 | 3/14 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.24×** | +5.8 | 6e-07 | 3/9 (HCT15, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.75×** | +5.7 | 8e-07 | 4/17 (LS 180, KATO III, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.70×** | +5.4 | 5e-06 | 7/16 (NCI-H2347, HS-578T, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.84×** | +5.4 | 5e-06 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +4.6 | 3e-04 | 0/11 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +4.5 | 3e-04 | 0/12 | top dose only | cell-cycle shift (explains ~2% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.81×** | +4.3 | 8e-04 | 1/15 (A-427) | top dose only |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +4.2 | 0.001 | 2/14 (HT-29, CFPAC-1) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +4.0 | 0.002 | 2/14 (LS 180, HCT15) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.00×** | +3.6 | 0.013 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +3.3 | 0.030 | 7/15 (NCI-H2347, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +3.3 | 0.033 | 11/17 (NCI-H2347, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +3.3 | 0.034 | 0/14 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +3.2 | 0.035 | 3/15 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +2.9 | 0.095 | 3/13 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.49×** | +2.9 | 0.097 | 2/15 (BT-474, KATO III) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6957.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 4 lines (NCI-H1573 0.0280×, SW480 0.0693×, HCT15 0.0375×, CFPAC-1 0.109×); [[Digitoxin (drug)]] 0.5 µM in 2 lines (SW480 0.0822×, NCI-H2347 0.0568×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.112×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.578× | -3.7 | 0.14 | 1/16 (HEC-1-A) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.604× | -3.4 | 0.20 | 0/16 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.637× | -3.3 | 0.20 | 15/17 (NCI-H1573, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 0.5 µM |  | 0.644× | -3.2 | 0.20 | 1/16 (KATO III) | inconsistent across doses |  |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.653× | -3.1 | 0.20 | 2/15 (LoVo, BT-474) | inconsistent across doses |  |
| [[Pimozide (drug)]] 5 µM |  | 0.654× | -3.1 | 0.20 | 2/16 (HS-578T, SW1417) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6957. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 3.50 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0693× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 6.88 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0280× (z -15.2) |
| [[BT-474 (line)]] | alt | 10.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -13.0) |
| [[CFPAC-1 (line)]] | alt | 4.59 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.109× (z -8.7) |
| [[COLO 205 (line)]] | alt | 5.25 | 0 | 1 | — | [[Amsacrine (drug)]] 0.5 µM 0.0432× (z -8.9) |
| [[HCT15 (line)]] | alt | 5.89 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0375× (z -9.9) |
| [[KATO III (line)]] | alt | 5.60 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0780× (z -9.3) ⚠ toxic |
| [[LS 180 (line)]] | wt | 6.72 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.104× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 2.23 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0568× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 3.92 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0689× (z -8.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 0.288 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.236 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.286 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.293 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.396 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.315 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.321 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.225 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.609 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.567 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.891 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.297 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.247 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.239 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.217 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.282 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.335 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.515 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.535 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.365 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6957), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00992]] | +0.69 | +0.70 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[LINC02253]] | +0.69 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[CDX2]] | +0.66 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[FGD3]] | +0.65 | +0.60 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[KCNE3]] | +0.64 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[MGC32805]] | +0.64 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[TMEM139]] | +0.63 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[ENPP5]] | +0.62 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[ANK3]] | +0.60 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[ARHGEF38]] | +0.60 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[TMEM125]] | +0.60 | +0.66 / +0.36 | both halves | 1e-04 |  |
| [[FAAH2]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSD3]] | -0.49 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[SENP5]] | -0.46 | -0.39 / -0.49 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*55 arrows, 55 of them with an alert ⚠; grade A 0, B 6, C 49. Shown: the 12 strongest; 43 more arrows (43 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MANSC1]] | B | MANSC1 activity raises ILDR1's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 1.96× lower at baseline in the lines without MANSC1 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[ENPP4]] | B | ENPP4 activity raises ILDR1's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 2.05× lower at baseline in the lines without ENPP4 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |
| [[ADGRG1]] | B | ADGRG1 activity raises ILDR1's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 1.65× lower at baseline in the lines without ADGRG1 | 0.070 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[LINC01876]] | B | LINC01876 activity raises ILDR1's level | lines that do not express LINC01876 (24) vs lines expressing it (26) | 1.55× lower at baseline in the lines without LINC01876 | 0.073 | ⚠ within organs, on part of the lines; also absent: TOX3, TFF1, TMEM45B |
| [[SLC44A3]] | B | SLC44A3 activity raises ILDR1's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 1.91× lower at baseline in the lines without SLC44A3 | 0.076 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[MROH7]] | B | MROH7 activity raises ILDR1's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 1.63× lower at baseline in the lines without MROH7 | 0.089 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |
| [[TMEM125]] | C | TMEM125 activity raises ILDR1's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 3.79× lower at baseline in the lines without TMEM125 | 8e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; co-absent with the target |
| [[BSPRY]] | C | BSPRY activity raises ILDR1's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 3.11× lower at baseline in the lines without BSPRY | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25; co-absent with the target |
| [[KDF1]] | C | KDF1 activity raises ILDR1's level | lines that do not express KDF1 (30) vs lines expressing it (20) | 3.33× lower at baseline in the lines without KDF1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3; co-absent with the target |
| [[ARHGEF38]] | C | ARHGEF38 activity raises ILDR1's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 3.94× lower at baseline in the lines without ARHGEF38 | 2e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1; co-absent with the target |
| [[TJP3]] | C | TJP3 activity raises ILDR1's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 3.12× lower at baseline in the lines without TJP3 | 4e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1; co-absent with the target |
| [[RORC]] | C | RORC activity raises ILDR1's level | lines that do not express RORC (30) vs lines expressing it (20) | 2.70× lower at baseline in the lines without RORC | 8e-04 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2; co-absent with the target |

### Downstream of this gene

*54 arrows, 54 of them with an alert ⚠; grade A 0, B 9, C 45. Shown: the 12 strongest; 42 more arrows (42 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM184A]] | B | ILDR1 activity raises TMEM184A's level | lines that do not express ILDR1 (31) vs lines expressing it (19) | 2.59× lower at baseline in the lines without ILDR1 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMEM125, ESRP1, SLC5A1 |
| [[SLC44A3]] | B | ILDR1 activity raises SLC44A3's level | lines that do not express ILDR1 (31) vs lines expressing it (19) | 3.14× lower at baseline in the lines without ILDR1 | 0.004 | ⚠ within organs, on part of the lines; also absent: TMEM125, ESRP1, SLC5A1 |
| [[MROH7]] | B | ILDR1 activity raises MROH7's level | lines that do not express ILDR1 (31) vs lines expressing it (19) | 2.37× lower at baseline in the lines without ILDR1 | 0.022 | ⚠ within organs, on part of the lines; also absent: TMEM125, ESRP1, SLC5A1 |
| [[DTX4]] | B | ILDR1 activity raises DTX4's level | lines that do not express ILDR1 (31) vs lines expressing it (19) | 1.88× lower at baseline in the lines without ILDR1 | 0.024 | ⚠ within organs, on part of the lines; also absent: TMEM125, ESRP1, SLC5A1 |
| [[MANSC1]] | B | ILDR1 activity raises MANSC1's level | lines that do not express ILDR1 (31) vs lines expressing it (19) | 2.52× lower at baseline in the lines without ILDR1 | 0.028 | ⚠ within organs, on part of the lines; also absent: TMEM125, ESRP1, SLC5A1 |
| [[GSTO2]] | B | ILDR1 activity raises GSTO2's level | lines that do not express ILDR1 (31) vs lines expressing it (19) | 2.40× lower at baseline in the lines without ILDR1 | 0.036 | ⚠ within organs, on part of the lines; also absent: TMEM125, ESRP1, SLC5A1 |
| [[ADGRG1]] | B | ILDR1 activity raises ADGRG1's level | lines that do not express ILDR1 (31) vs lines expressing it (19) | 1.92× lower at baseline in the lines without ILDR1 | 0.055 | ⚠ within organs, on part of the lines; also absent: TMEM125, ESRP1, SLC5A1 |
| [[ELF3-AS1]] | B | ILDR1 activity raises ELF3-AS1's level | lines that do not express ILDR1 (31) vs lines expressing it (19) | 2.87× lower at baseline in the lines without ILDR1 | 0.061 | ⚠ within organs, on part of the lines; also absent: TMEM125, ESRP1, SLC5A1 |
| [[FAM111A-DT]] | B | ILDR1 activity raises FAM111A-DT's level | lines that do not express ILDR1 (31) vs lines expressing it (19) | 1.53× lower at baseline in the lines without ILDR1 | 0.068 | ⚠ within organs, on part of the lines; also absent: TMEM125, ESRP1, SLC5A1 |
| [[TMC4]] | C | ILDR1 activity raises TMC4's level | lines that do not express ILDR1 (31) vs lines expressing it (19) | 5.94× lower at baseline in the lines without ILDR1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: TMEM125, ESRP1, SLC5A1; co-absent with the target |
| [[KDF1]] | C | ILDR1 activity raises KDF1's level | lines that do not express ILDR1 (31) vs lines expressing it (19) | 3.99× lower at baseline in the lines without ILDR1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: TMEM125, ESRP1, SLC5A1; co-absent with the target |
| [[BSPRY]] | C | ILDR1 activity raises BSPRY's level | lines that do not express ILDR1 (31) vs lines expressing it (19) | 6.54× lower at baseline in the lines without ILDR1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: TMEM125, ESRP1, SLC5A1; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.618). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.4, 48.5); signed map (56.2, 3.5). **Vector** length 43.5, 11.6% of its response variance represented; |z| ≥ 3 in 382 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.3 | +3.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.2 | +3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +11.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.9 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +2.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.1 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.3 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -0.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.8 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.7 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.7 | +0.2 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.6 | -1.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -0.6 | -1.3 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -0.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | immunoglobulin like domain containing receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.33 — chr3:121,987,323-122,022,247 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC50831; previously DFNB42 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86SU0](https://www.uniprot.org/uniprotkb/Q86SU0) (Immunoglobulin-like domain-containing receptor 1):

> Maintains epithelial barrier function by recruiting MARVELD2/tricellulin to tricellular tight junctions (tTJs). Crucial for normal hearing by maintaining the structural and functional integrity of tTJs, which are critical for the survival of auditory neurosensory HCs. Mediates fatty acids and lipoproteins-stimulated CCK/cholecystokinin secretion in the small intestine. In the inner ear, may regulate alternative pre-mRNA splicing via binding to TRA2A, TRA2B and SRSF1 (By similarity).; (Microbial …

**Summary**, from NCBI Gene [286676](https://www.ncbi.nlm.nih.gov/gene/286676):

> This gene encodes a protein that contains an immunoglobulin-like domain. The encoded protein may function as a multimeric receptor at the cell surface. The expression of this gene may be a diagnostic marker for cancer progression. Alternatively spliced transcript variants encoding multiple protein isoforms have been observed for this gene. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:28741](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28741) · Entrez [286676](https://www.ncbi.nlm.nih.gov/gene/286676) · UniProt [Q86SU0](https://www.uniprot.org/uniprotkb/Q86SU0) · Ensembl [ENSG00000145103](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145103)

## Data

Gene col 6957: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6957); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6957, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6957]; `tensor/DDL_lfc|DDL_z.npy` [6957]; `embed/gene_vectors.npy` [6957]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6957 or target_col == 6957). Every well: [[ILDR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ILDR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
