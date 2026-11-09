---
symbol: "TRPM8"
type: "gene"
col: 6886
ensembl_id: "ENSG00000144481"
name: "transient receptor potential cation channel subfamily M member 8"
location: "2q37.1"
module: 87
arm: "+"
pooled_cpm: 2.22
n_lines_expressing: 22
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 11
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# TRPM8

*transient receptor potential cation channel subfamily M member 8* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.48× (z +13.1, q 2e-36, up in 4 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.48× (z +9.9, q 1e-20, up in 3 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (SK-MEL-2 0.0854×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SNU-423 0.0818×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.104×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.115×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.260×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TYR]] (+0.66, fdr 7e-06), [[RMEL3]] (+0.65, fdr 7e-06), [[MIR3681HG]] (+0.64, fdr 2e-05).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CA8]] → it (grade B ⚠); 11 go from it, the strongest it → [[SORCS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6886.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.48×** | +13.1 | 2e-36 | 4/5 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.45×** | +12.5 | 1e-33 | 1/2 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.48×** | +9.9 | 1e-20 | 3/11 (SW1417, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.40×** | +8.6 | 8e-16 | 1/4 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.01×** | +7.6 | 4e-12 | 8/16 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +7.2 | 7e-11 | 1/11 (PANC-1) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.97×** | +5.2 | 2e-05 | 1/15 (A-172) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.96×** | +5.1 | 2e-05 | 1/7 (HEC-1-A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.44×** | +4.9 | 7e-05 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +4.3 | 9e-04 | 2/10 (HEC-1-A, MIA PaCa-2) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +4.3 | 9e-04 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +4.1 | 0.002 | 3/13 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +4.0 | 0.002 | 2/8 (SNU-423, SHP-77) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.65×** | +3.8 | 0.005 | 1/10 (MIA PaCa-2) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.009 | 0/16 | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.88×** | +3.5 | 0.017 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +3.2 | 0.037 | 1/14 (A-172) | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.065 | 1/11 (RPMI-7951) | inconsistent across doses |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.49×** | +3.0 | 0.066 | 1/11 (SNU-1) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +2.9 | 0.090 | 3/11 (HEC-1-A, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6886.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (SK-MEL-2 0.0854×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SNU-423 0.0818×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.104×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.115×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.260×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | 0.656× | -3.1 | 0.68 | 8/13 (LS 180, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6886. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 22.7 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0854× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 2.45 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.334× (z -9.3) ⚠ position not correctable |
| [[SHP-77 (line)]] | alt | 5.71 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -9.1) |
| [[SNU-423 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0818× (z -10.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.266 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.609 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.689 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.338 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.676 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.409 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.415 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.632 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.575 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.384 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.398 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.399 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.912 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.300 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.996 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.850 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.840 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.368 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.425 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6886), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYR]] | +0.66 | +0.63 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[RMEL3]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[MIR3681HG]] | +0.64 | +0.48 / +0.67 | both halves | 2e-05 | **novel candidate** |
| [[LINC02941]] | +0.63 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[LHFPL3-AS1]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[EDNRB]] | +0.62 | +0.53 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[LINC02566]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[GRIA2]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[PI15]] | +0.61 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[FCRLA]] | +0.60 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[LDB2]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[SOX10]] | +0.60 | +0.54 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA8]] | B | CA8 activity raises TRPM8's level | lines that do not express CA8 (27) vs lines expressing it (23) | 1.42× lower at baseline in the lines without CA8 | 0.089 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |
| [[PDE10A]] | C | PDE10A activity raises TRPM8's level | lines that do not express PDE10A (24) vs lines expressing it (26) | 1.92× lower at baseline in the lines without PDE10A | 0.024 | ⚠ within organs, on part of the lines; also absent: ZMAT4, UBE2QL1, C10orf90; co-absent with the target |
| [[TOX]] | C | TOX activity raises TRPM8's level | lines that do not express TOX (30) vs lines expressing it (20) | 1.09× lower at baseline in the lines without TOX | 0.087 | ⚠ within organs, on part of the lines; also absent: CDH6, DKK3, MXRA5; co-absent with the target |
| [[FRMPD4]] | C | FRMPD4 activity raises TRPM8's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 1.59× lower at baseline in the lines without FRMPD4 | 0.097 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 5, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SORCS1]] | B | TRPM8 activity raises SORCS1's level | lines that do not express TRPM8 (28) vs lines expressing it (22) | 1.85× lower at baseline in the lines without TRPM8 | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC01320, LINC02335; maybe low, not absent |
| [[MOXD1]] | B | TRPM8 activity raises MOXD1's level | lines that do not express TRPM8 (28) vs lines expressing it (22) | 2.62× lower at baseline in the lines without TRPM8 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC01320, LINC02335; maybe low, not absent |
| [[LOXL3]] | B | TRPM8 activity raises LOXL3's level | lines that do not express TRPM8 (28) vs lines expressing it (22) | 2.78× lower at baseline in the lines without TRPM8 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC01320, LINC02335; maybe low, not absent |
| [[OFCC1]] | B | TRPM8 activity raises OFCC1's level | lines that do not express TRPM8 (28) vs lines expressing it (22) | 2.11× lower at baseline in the lines without TRPM8 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC01320, LINC02335; maybe low, not absent |
| [[CA8]] | B | TRPM8 activity raises CA8's level | lines that do not express TRPM8 (28) vs lines expressing it (22) | 2.13× lower at baseline in the lines without TRPM8 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC01320, LINC02335; maybe low, not absent |
| [[FRMPD4]] | C | TRPM8 activity raises FRMPD4's level | lines that do not express TRPM8 (28) vs lines expressing it (22) | 3.09× lower at baseline in the lines without TRPM8 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC01320, LINC02335; maybe low, not absent; co-absent with the target |
| [[RMEL3]] | C | TRPM8 activity raises RMEL3's level | lines that do not express TRPM8 (28) vs lines expressing it (22) | 1.97× lower at baseline in the lines without TRPM8 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC01320, LINC02335; maybe low, not absent; co-absent with the target |
| [[LINC02055]] | C | TRPM8 activity raises LINC02055's level | lines that do not express TRPM8 (28) vs lines expressing it (22) | 2.61× lower at baseline in the lines without TRPM8 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC01320, LINC02335; maybe low, not absent; co-absent with the target |
| [[C10orf90]] | C | TRPM8 activity raises C10orf90's level | lines that do not express TRPM8 (28) vs lines expressing it (22) | 2.24× lower at baseline in the lines without TRPM8 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC01320, LINC02335; maybe low, not absent; co-absent with the target |
| [[PDE10A]] | C | TRPM8 activity raises PDE10A's level | lines that do not express TRPM8 (28) vs lines expressing it (22) | 2.81× lower at baseline in the lines without TRPM8 | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC01320, LINC02335; maybe low, not absent; co-absent with the target |
| [[PPP2R2B]] | C | TRPM8 activity raises PPP2R2B's level | lines that do not express TRPM8 (28) vs lines expressing it (22) | 1.88× lower at baseline in the lines without TRPM8 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC01320, LINC02335; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.726). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.0, 29.0); signed map (30.0, 39.1). **Vector** length 30.8, 6.60% of its response variance represented; |z| ≥ 3 in 399 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +13.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +9.9 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +0.9 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | +3.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.8 | +2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.7 | +0.0 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.0 | -1.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -2.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -0.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | transient receptor potential cation channel subfamily M member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:233,917,373-234,019,522 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 4 pathways, smallest: TRP channels; Stimuli-sensing channels; Ion channel transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z2W7](https://www.uniprot.org/uniprotkb/Q7Z2W7) (Transient receptor potential cation channel subfamily M member 8):

> Non-selective ion channel permeable to monovalent and divalent cations, including Na(+), K(+), and Ca(2+), with higher permeability for Ca(2+). Activated by multiple factors, such as temperature, voltage, pressure, and changes in osmolality. Activated by cool temperatures (<23-28 degrees Celsius) and by chemical ligands evoking a sensation of coolness, such as menthol and icilin therefore plays a central role in the detection of environmental cold temperatures. TRPM8 is a voltage-dependent …

**Summary**, from NCBI Gene [79054](https://www.ncbi.nlm.nih.gov/gene/79054):

> Predicted to enable ligand-gated calcium channel activity. Predicted to be involved in calcium ion transmembrane transport; positive regulation of cold-induced thermogenesis; and thermoception. Predicted to act upstream of or within calcium ion transport; intracellular calcium ion homeostasis; and response to cold. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17961](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17961) · Entrez [79054](https://www.ncbi.nlm.nih.gov/gene/79054) · UniProt [Q7Z2W7](https://www.uniprot.org/uniprotkb/Q7Z2W7) · Ensembl [ENSG00000144481](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144481)

## Data

Gene col 6886: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6886); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6886, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6886]; `tensor/DDL_lfc|DDL_z.npy` [6886]; `embed/gene_vectors.npy` [6886]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6886 or target_col == 6886). Every well: [[TRPM8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRPM8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
