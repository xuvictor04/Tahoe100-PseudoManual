---
symbol: "PASD1"
type: "gene"
col: 9232
ensembl_id: "ENSG00000166049"
name: "PAS domain containing repressor 1"
location: "Xq28"
module: 27
arm: "+"
pooled_cpm: 2.12
n_lines_expressing: 9
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 16
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# PASD1

*PAS domain containing repressor 1* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.99× (z +14.0, q 6e-42, up in 0 of 3 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00698]] (+0.49, fdr 6e-05), [[PTPRS]] (+0.49, fdr 1e-04), [[CCDC144A]] (+0.47, fdr 1e-04); moves opposite to [[JAKMIP2-AS1]] (-0.64, fdr 1e-05), [[ST18]] (-0.58, fdr 3e-05), [[LINC01980]] (-0.53, fdr 2e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC00491]] → it (grade C ⚠); 16 go from it, the strongest it → [[LINC02466]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9232.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.99×** | +14.0 | 6e-42 | 0/3 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.72×** | +9.5 | 8e-19 | 1/2 (SW480) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.41×** | +9.3 | 2e-18 | 1/2 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.92×** | +8.3 | 1e-14 | 1/2 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.81×** | +7.6 | 3e-12 | 1/2 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.74×** | +6.9 | 5e-10 | 4/4 (SW480, HS-578T, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.91×** | +5.4 | 6e-06 | 1/2 (SW480) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.72×** | +5.2 | 1e-05 | 0/3 | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.06×** | +5.0 | 3e-05 | 0/5 | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.10×** | +4.2 | 0.001 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.18×** | +4.1 | 0.003 | 0/2 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.16×** | +4.0 | 0.003 | 0/2 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.11×** | +3.9 | 0.005 | 1/1 (SW480) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.70×** | +3.9 | 0.005 | 0/6 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.49×** | +3.4 | 0.026 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +3.3 | 0.029 | 0/4 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.83×** | +3.1 | 0.055 | 2/2 (HS-578T, SW480) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +3.1 | 0.057 | 0/3 | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Pemigatinib (drug)]] 0.05 µM |  | **1.84×** | +3.0 | 0.076 | 1/2 (SW480) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.23×** | +3.0 | 0.076 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9232.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Orlistat (drug)]] 5 µM |  | 0.538× | -3.2 | 0.52 | 0/5 | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.857× | -3.1 | 0.52 | 2/7 (SHP-77, hTERT-HPNE) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9232. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 0.281 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.259 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.348 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.327 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.520 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.504 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.335 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.482 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.322 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.753 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.289 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.508 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.369 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.631 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.268 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.424 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.229 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.624 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.274 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.278 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.339 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.555 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 30.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9232), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00698]] | +0.49 | +0.39 / +0.41 | both halves | 6e-05 |  |
| [[PTPRS]] | +0.49 | +0.38 / +0.35 | both halves | 1e-04 |  |
| [[CCDC144A]] | +0.47 | +0.36 / +0.41 | both halves | 1e-04 |  |
| [[KIF5C]] | +0.47 | +0.28 / +0.44 | both halves | 3e-04 |  |
| [[NEURL1]] | +0.47 | +0.38 / +0.35 | both halves | 1e-04 |  |
| [[MAST1]] | +0.47 | +0.27 / +0.40 | both halves | 3e-04 |  |
| [[KIF1A]] | +0.47 | +0.35 / +0.43 | both halves | 1e-04 |  |
| [[NPAS1]] | +0.46 | +0.37 / +0.34 | both halves | 1e-04 | same gene group; STRING 562 |
| [[GALNT16]] | +0.45 | +0.31 / +0.33 | both halves | 2e-04 |  |
| [[LINC00595]] | +0.45 | +0.33 / +0.42 | both halves | 1e-04 |  |
| [[CPA6]] | +0.45 | +0.45 / +0.34 | both halves | 1e-04 |  |
| [[CSMD2]] | +0.44 | +0.37 / +0.45 | both halves | 8e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JAKMIP2-AS1]] | -0.64 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[ST18]] | -0.58 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[LINC01980]] | -0.53 | -0.58 / -0.29 | both halves | 2e-04 |  |
| [[APCDD1]] | -0.52 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[LINC00491]] | -0.50 | -0.52 / -0.26 | both halves | 4e-04 |  |
| [[HCG11]] | -0.50 | -0.37 / -0.40 | both halves | 7e-05 |  |
| [[LINC01551]] | -0.50 | -0.62 / -0.09 | ⚠ one half (not replicated) | 0.003 |  |
| [[FGF20]] | -0.50 | -0.47 / -0.23 | both halves | 5e-04 |  |
| [[PROX1-AS1]] | -0.50 | -0.53 / -0.27 | both halves | 3e-04 |  |
| [[B3GAT1-DT]] | -0.48 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[LINC02058]] | -0.48 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[SLCO6A1]] | -0.48 | -0.51 / -0.28 | both halves | 3e-04 |  |
| [[SMOC2]] | -0.47 | -0.41 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00491]] | C | LINC00491 activity raises PASD1's level | lines that do not express LINC00491 (33) vs lines expressing it (17) | 1.38× lower at baseline in the lines without LINC00491 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APCDD1L, LINC01905, ADGRG7; co-absent with the target |
| [[JAKMIP2-AS1]] | C | JAKMIP2-AS1 activity raises PASD1's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 1.47× lower at baseline in the lines without JAKMIP2-AS1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[ANKRD20A9P]] | C | ANKRD20A9P activity raises PASD1's level | lines that do not express ANKRD20A9P (40) vs lines expressing it (10) | 1.81× lower at baseline in the lines without ANKRD20A9P | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MTND1P23, ENSG00000291025, LINC00408; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 7, C 9. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02466]] | B | PASD1 activity raises LINC02466's level | lines that do not express PASD1 (41) vs lines expressing it (9) | 2.28× lower at baseline in the lines without PASD1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, RNF17; maybe low, not absent |
| [[SLCO6A1]] | B | PASD1 activity raises SLCO6A1's level | lines that do not express PASD1 (41) vs lines expressing it (9) | 2.28× lower at baseline in the lines without PASD1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, RNF17; maybe low, not absent |
| [[CPA6]] | B | PASD1 activity raises CPA6's level | lines that do not express PASD1 (41) vs lines expressing it (9) | 2.14× lower at baseline in the lines without PASD1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, RNF17; maybe low, not absent |
| [[LINC00595]] | B | PASD1 activity raises LINC00595's level | lines that do not express PASD1 (41) vs lines expressing it (9) | 1.65× lower at baseline in the lines without PASD1 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, RNF17; maybe low, not absent |
| [[PTPRF]] | B | PASD1 activity lowers PTPRF's level | lines that do not express PASD1 (41) vs lines expressing it (9) | 1.40× higher at baseline in the lines without PASD1 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, RNF17; maybe low, not absent |
| [[F10]] | B | PASD1 activity raises F10's level | lines that do not express PASD1 (41) vs lines expressing it (9) | 1.64× lower at baseline in the lines without PASD1 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, RNF17; maybe low, not absent |
| [[EP300]] | B | PASD1 activity raises EP300's level | lines that do not express PASD1 (41) vs lines expressing it (9) | 1.29× lower at baseline in the lines without PASD1 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, RNF17; maybe low, not absent |
| [[LINC00491]] | C | PASD1 activity raises LINC00491's level | lines that do not express PASD1 (41) vs lines expressing it (9) | 3.22× lower at baseline in the lines without PASD1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, RNF17; maybe low, not absent; co-absent with the target |
| [[LINC02315]] | C | PASD1 activity raises LINC02315's level | lines that do not express PASD1 (41) vs lines expressing it (9) | 5.16× lower at baseline in the lines without PASD1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, RNF17; maybe low, not absent; co-absent with the target |
| [[ST18]] | C | PASD1 activity raises ST18's level | lines that do not express PASD1 (41) vs lines expressing it (9) | 3.70× lower at baseline in the lines without PASD1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, RNF17; maybe low, not absent; co-absent with the target |
| [[LINC01980]] | C | PASD1 activity raises LINC01980's level | lines that do not express PASD1 (41) vs lines expressing it (9) | 2.72× lower at baseline in the lines without PASD1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, RNF17; maybe low, not absent; co-absent with the target |
| [[RMST]] | C | PASD1 activity raises RMST's level | lines that do not express PASD1 (41) vs lines expressing it (9) | 3.00× lower at baseline in the lines without PASD1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, RNF17; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction -0.452). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.2, 42.5); signed map (27.9, 30.8). **Vector** length 9.84, 2.27% of its response variance represented; |z| ≥ 3 in 112 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.9 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.9 | +9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.8 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.8 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.7 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.3 | -0.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +0.3 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.2 | +3.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.4 | +1.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.3 | -3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.3 | -1.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.3 | +2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.3 | +0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.3 | -1.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.2 | -0.6 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -0.2 | -0.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.2 | -2.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | PAS domain containing repressor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:151,563,675-151,676,739 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CT63 |
| Gene groups (HGNC) | PAS domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IV76](https://www.uniprot.org/uniprotkb/Q8IV76) (Circadian clock protein PASD1):

> Functions as a suppressor of the biological clock that drives the daily circadian rhythms of cells throughout the body. Acts as a nuclear repressor of the CLOCK-BMAL1 heterodimer-mediated transcriptional activation of the core clock components. Inhibits circadian clock function in cancer cells, when overexpressed.

**Summary**, from NCBI Gene [139135](https://www.ncbi.nlm.nih.gov/gene/139135):

> This gene encodes a protein that is thought to function as a transcription factor. The protein is a cancer-associated antigen that can stimulate autologous T-cell responses, and it is therefore considered to be a potential immunotherapeutic target for the treatment of various hematopoietic malignancies, including diffuse large B-cell lymphoma. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:20686](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20686) · Entrez [139135](https://www.ncbi.nlm.nih.gov/gene/139135) · UniProt [Q8IV76](https://www.uniprot.org/uniprotkb/Q8IV76) · Ensembl [ENSG00000166049](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166049)

## Data

Gene col 9232: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9232); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9232, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9232]; `tensor/DDL_lfc|DDL_z.npy` [9232]; `embed/gene_vectors.npy` [9232]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9232 or target_col == 9232). Every well: [[PASD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PASD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
