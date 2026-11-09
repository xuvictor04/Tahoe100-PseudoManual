---
symbol: "PNLIPRP3"
type: "gene"
col: 12794
ensembl_id: "ENSG00000203837"
name: "pancreatic lipase related protein 3"
location: "10q25.3"
module: 125
arm: "+"
pooled_cpm: 2.94
n_lines_expressing: 18
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 9
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# PNLIPRP3

*pancreatic lipase related protein 3* — 10q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.37× (z +10.4, q 2e-22, up in 8 of 10 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 1 line (NCI-H1573 0.0371×); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0383×); [[Dexamethasone (drug)]] 0.05 µM in 1 line (NCI-H460 0.0510×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02154]] (+0.72, fdr 7e-06), [[CCL3]] (+0.70, fdr 7e-06), [[LINC00520]] (+0.66, fdr 1e-05); moves opposite to [[PIGS]] (-0.52, fdr 4e-05), [[GLT8D1]] (-0.45, fdr 9e-05), [[SETD3]] (-0.43, fdr 1e-04).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LINC00457]] → it (grade C ⚠); 9 go from it, the strongest it → [[LINC01933]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12794.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.37×** | +10.4 | 2e-22 | 8/10 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.75×** | +8.2 | 5e-14 | 0/1 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.22×** | +7.9 | 5e-13 | 0/5 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.54×** | +7.7 | 2e-12 | 0/3 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.42×** | +6.5 | 9e-09 | 10/11 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +6.4 | 2e-08 | 1/11 (A549) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.53×** | +6.3 | 2e-08 | 9/12 (NCI-H460, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.22×** | +6.2 | 5e-08 | 3/4 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.86×** | +5.8 | 6e-07 | 5/7 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.45×** | +4.7 | 1e-04 | 3/5 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.32×** | +4.7 | 1e-04 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.85×** | +4.6 | 2e-04 | 1/12 (A-172) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.30×** | +4.6 | 2e-04 | 9/12 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.15×** | +4.2 | 0.001 | 8/13 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.10×** | +4.0 | 0.002 | 1/3 (NCI-H1573) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.13×** | +3.9 | 0.003 | 4/11 (NCI-H1573, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +3.7 | 0.007 | 2/10 (A-172, SK-MEL-2) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.87×** | +3.4 | 0.018 | 6/9 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.30×** | +3.3 | 0.029 | 2/8 (NCI-H460, NCI-H1573) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +3.2 | 0.035 | 7/9 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.78×** | +3.1 | 0.040 | 2/7 (NCI-H460, NCI-H1573) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.77×** | +3.1 | 0.042 | 0/10 | inconsistent across doses | position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **1.79×** | +3.1 | 0.047 | 1/7 (A-172) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12794.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 1 line (NCI-H1573 0.0371×); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0383×); [[Dexamethasone (drug)]] 0.05 µM in 1 line (NCI-H460 0.0510×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Decitabine (drug)]] 5 µM |  | 0.569× | -3.0 | 0.97 | 3/10 (J82, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12794. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.0371× (z -10.2) |
| [[A-172 (line)]] | wt | 2.92 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 187× (z +13.0) | — |
| [[hTERT-HPNE (line)]] | wt | 4.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 95.3× (z +11.5) | — |
| [[J82 (line)]] | alt | 2.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.0× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 4.47 | 0 | 1 | — | [[Dexamethasone (drug)]] 0.05 µM 0.0510× (z -9.8) |
| [[A-427 (line)]] | wt | 0.412 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.607 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.872 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 95.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.479 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.379 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.406 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.427 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.327 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.339 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.806 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.772 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.259 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.294 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.415 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.380 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.461 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.310 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12794), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02154]] | +0.72 | +0.71 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[CCL3]] | +0.70 | +0.71 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[LINC00520]] | +0.66 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[C11orf96]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[C12orf50]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[SLC35F1]] | +0.59 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[ENTHD1]] | +0.59 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[NGF]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[LINC01828]] | +0.57 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[SPINK1]] | +0.56 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[ROR1-AS1]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[GRIA4]] | +0.54 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGS]] | -0.52 | -0.43 / -0.51 | both halves | 4e-05 |  |
| [[GLT8D1]] | -0.45 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[SETD3]] | -0.43 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[PTCH1]] | -0.43 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[LDOC1]] | -0.43 | -0.42 / -0.29 | both halves | 2e-04 |  |
| [[PPP2R5D]] | -0.43 | -0.41 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00457]] | C | LINC00457 activity raises PNLIPRP3's level | lines that do not express LINC00457 (29) vs lines expressing it (21) | 1.89× lower at baseline in the lines without LINC00457 | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC01440, LINC01456, NTS; maybe low, not absent; co-absent with the target |
| [[LINC00520]] | C | LINC00520 activity raises PNLIPRP3's level | lines that do not express LINC00520 (31) vs lines expressing it (19) | 2.22× lower at baseline in the lines without LINC00520 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, LINC00589, LINC02930; co-absent with the target |
| [[LINC02220]] | C | LINC02220 activity raises PNLIPRP3's level | lines that do not express LINC02220 (22) vs lines expressing it (28) | 1.86× lower at baseline in the lines without LINC02220 | 0.048 | ⚠ within organs, on part of the lines; also absent: COL16A1, SEMA5A, ANKRD30B; maybe low, not absent; co-absent with the target |
| [[NAALADL2-AS2]] | C | NAALADL2-AS2 activity raises PNLIPRP3's level | lines that do not express NAALADL2-AS2 (36) vs lines expressing it (14) | 2.62× lower at baseline in the lines without NAALADL2-AS2 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RNF17, ENSG00000287598, SSX1; co-absent with the target |
| [[PSG4]] | C | PSG4 activity raises PNLIPRP3's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 1.55× lower at baseline in the lines without PSG4 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5; co-absent with the target |
| [[LINC00504]] | C | LINC00504 activity raises PNLIPRP3's level | lines that do not express LINC00504 (31) vs lines expressing it (19) | 2.06× lower at baseline in the lines without LINC00504 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC02930, ENSG00000287474; co-absent with the target |
| [[ENTHD1]] | C | ENTHD1 activity raises PNLIPRP3's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 2.27× lower at baseline in the lines without ENTHD1 | 0.087 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01933]] | B | PNLIPRP3 activity raises LINC01933's level | lines that do not express PNLIPRP3 (32) vs lines expressing it (18) | 1.48× lower at baseline in the lines without PNLIPRP3 | 0.008 | ⚠ within organs, on part of the lines; also absent: RSPO3, ENSG00000225087, PDE1A |
| [[ACTN2]] | B | PNLIPRP3 activity raises ACTN2's level | lines that do not express PNLIPRP3 (32) vs lines expressing it (18) | 2.56× lower at baseline in the lines without PNLIPRP3 | 0.060 | ⚠ within organs, on part of the lines; also absent: RSPO3, ENSG00000225087, PDE1A |
| [[C12orf50]] | B | PNLIPRP3 activity raises C12orf50's level | lines that do not express PNLIPRP3 (32) vs lines expressing it (18) | 1.93× lower at baseline in the lines without PNLIPRP3 | 0.062 | ⚠ within organs, on part of the lines; also absent: RSPO3, ENSG00000225087, PDE1A |
| [[CRYM]] | B | PNLIPRP3 activity raises CRYM's level | lines that do not express PNLIPRP3 (32) vs lines expressing it (18) | 1.89× lower at baseline in the lines without PNLIPRP3 | 0.063 | ⚠ within organs, on part of the lines; also absent: RSPO3, ENSG00000225087, PDE1A |
| [[ENTHD1]] | C | PNLIPRP3 activity raises ENTHD1's level | lines that do not express PNLIPRP3 (32) vs lines expressing it (18) | 2.91× lower at baseline in the lines without PNLIPRP3 | 0.030 | ⚠ within organs, on part of the lines; also absent: RSPO3, ENSG00000225087, PDE1A; co-absent with the target |
| [[LINC00520]] | C | PNLIPRP3 activity raises LINC00520's level | lines that do not express PNLIPRP3 (32) vs lines expressing it (18) | 2.36× lower at baseline in the lines without PNLIPRP3 | 0.040 | ⚠ within organs, on part of the lines; also absent: RSPO3, ENSG00000225087, PDE1A; co-absent with the target |
| [[ANKRD30B]] | C | PNLIPRP3 activity raises ANKRD30B's level | lines that do not express PNLIPRP3 (32) vs lines expressing it (18) | 2.61× lower at baseline in the lines without PNLIPRP3 | 0.059 | ⚠ within organs, on part of the lines; also absent: RSPO3, ENSG00000225087, PDE1A; co-absent with the target |
| [[MAGEA1]] | C | PNLIPRP3 activity raises MAGEA1's level | lines that do not express PNLIPRP3 (32) vs lines expressing it (18) | 2.42× lower at baseline in the lines without PNLIPRP3 | 0.076 | ⚠ within organs, on part of the lines; also absent: RSPO3, ENSG00000225087, PDE1A; co-absent with the target |
| [[LINC00504]] | C | PNLIPRP3 activity raises LINC00504's level | lines that do not express PNLIPRP3 (32) vs lines expressing it (18) | 2.26× lower at baseline in the lines without PNLIPRP3 | 0.089 | ⚠ within organs, on part of the lines; also absent: RSPO3, ENSG00000225087, PDE1A; co-absent with the target |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.731). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.2, 21.6); signed map (37.3, 22.4). **Vector** length 38.7, 11.4% of its response variance represented; |z| ≥ 3 in 363 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.5 | +10.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +2.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.1 | +1.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.0 | +2.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.0 | +1.5 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | +1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | +0.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.8 | -2.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | -0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.7 | -2.6 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.7 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | pancreatic lipase related protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.3 — chr10:116,427,847-116,477,957 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Lipases |
| Reactome | 2 pathways, smallest: Digestion; Digestion and absorption |
| Matched by | ensembl_id |

**Function**, from UniProt [Q17RR3](https://www.uniprot.org/uniprotkb/Q17RR3) (Pancreatic lipase-related protein 3):

> Hydrolyzes triglycerides into diglycerides and subsequently into monoglycerides and free fatty acids.

**Summary**, from NCBI Gene [119548](https://www.ncbi.nlm.nih.gov/gene/119548):

> Predicted to enable glycerophospholipid phospholipase A1 activity and lipoprotein lipase activity. Predicted to be involved in several processes, including cholesterol homeostasis; high-density lipoprotein particle remodeling; and triglyceride catabolic process. Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23492](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23492) · Entrez [119548](https://www.ncbi.nlm.nih.gov/gene/119548) · UniProt [Q17RR3](https://www.uniprot.org/uniprotkb/Q17RR3) · Ensembl [ENSG00000203837](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203837)

## Data

Gene col 12794: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12794); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12794, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12794]; `tensor/DDL_lfc|DDL_z.npy` [12794]; `embed/gene_vectors.npy` [12794]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12794 or target_col == 12794). Every well: [[PNLIPRP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PNLIPRP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
