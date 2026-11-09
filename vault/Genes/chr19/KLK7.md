---
symbol: "KLK7"
type: "gene"
col: 9742
ensembl_id: "ENSG00000169035"
name: "kallikrein related peptidase 7"
location: "19q13.41"
module: 44
arm: "+"
pooled_cpm: 2.46
n_lines_expressing: 12
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 22
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# KLK7

*kallikrein related peptidase 7* — 19q13.41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 9.31× (z +11.1, q 1e-25, up in 5 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.18× (z +5.4, q 9e-06, up in 1 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW48 0.0653×, LS 180 0.109×, SW1417 0.270×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SW48 0.0543×, SW1417 0.149×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLK6]] (+0.79, fdr 7e-06, ⚠ same locus), [[EPCAM]] (+0.71, fdr 7e-06), [[LYZ]] (+0.67, fdr 1e-05), [[GPX2]] (+0.67, fdr 3e-05); moves opposite to [[INO80E]] (-0.45, fdr 4e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ONECUT3]] → it (grade C ⚠); 22 go from it, the strongest it → [[LARGE2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9742.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **9.31×** | +11.1 | 1e-25 | 5/5 (SW1417, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **10.6×** | +10.0 | 3e-21 | 2/2 (SW1417, SW48) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.29×** | +7.3 | 7e-11 | 3/4 (SW1417, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +5.4 | 9e-06 | 1/9 (AsPC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.91×** | +5.3 | 2e-05 | 1/8 (AsPC-1) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.47×** | +4.5 | 8e-04 | 0/10 | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.46×** | +4.4 | 8e-04 | 1/5 (SW1417) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.43×** | +4.3 | 1e-03 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.72×** | +4.2 | 0.001 | 1/5 (LS 180) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.84×** | +4.2 | 0.001 | 0/10 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **5.11×** | +4.2 | 0.001 | 1/1 (SW1417) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +3.8 | 0.006 | 5/10 (SW480, HCT15, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +3.8 | 0.006 | 1/8 (AsPC-1) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.03×** | +3.5 | 0.020 | 2/10 (Panc 03.27, KATO III) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.97×** | +3.3 | 0.034 | 0/6 | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.46×** | +3.2 | 0.055 | 2/5 (SW1417, KATO III) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **2.37×** | +3.0 | 0.078 | 3/6 (SW48, KATO III, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.89×** | +3.0 | 0.088 | 1/8 (KATO III) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +2.9 | 0.099 | 6/10 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW48 0.0653×, LS 180 0.109×, SW1417 0.270×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SW48 0.0543×, SW1417 0.149×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9742. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 21.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -8.7) |
| [[SW48 (line)]] | wt | 128 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0653× (z -18.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0543× (z -13.9) |
| [[LS 180 (line)]] | wt | 9.71 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.265 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.289 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.213 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.196 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.253 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.234 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.755 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.609 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.242 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.254 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.224 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.194 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.319 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.222 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.238 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.189 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.222 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.357 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.285 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.191 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.228 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.206 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.189 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.234 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.255 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.220 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9742), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 7 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLK6]] | +0.79 | +0.76 / +0.76 | both halves | 7e-06 | same gene group; STRING 669; ⚠ same locus (6.8 kb, same strand: neighbours can correlate without regulation) |
| [[EPCAM]] | +0.71 | +0.58 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[LYZ]] | +0.67 | +0.54 / +0.75 | both halves | 1e-05 |  |
| [[GPX2]] | +0.67 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[MSLN]] | +0.67 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[CKMT1A]] | +0.63 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[AZGP1]] | +0.62 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[TFF3]] | +0.62 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[KLK11]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 | same gene group; STRING 473; ⚠ same locus (38.1 kb, same strand: neighbours can correlate without regulation) |
| [[LINC01819]] | +0.62 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[CKMT1B]] | +0.61 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[HEPHL1]] | +0.61 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[PPP1R1B]] | +0.61 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[LINC01559]] | +0.61 | +0.58 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INO80E]] | -0.45 | -0.25 / -0.39 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ONECUT3]] | C | ONECUT3 activity raises KLK7's level | lines that do not express ONECUT3 (37) vs lines expressing it (13) | 3.56× lower at baseline in the lines without ONECUT3 | 0.009 | ⚠ within organs, on part of the lines; also absent: KLK7, KLK11, SLC6A20; co-absent with the target |
| [[KLK11]] | C | KLK11 activity raises KLK7's level | lines that do not express KLK11 (40) vs lines expressing it (10) | 4.22× lower at baseline in the lines without KLK11 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC17, LYZ; co-absent with the target |
| [[KLK6]] | C | KLK6 activity raises KLK7's level | lines that do not express KLK6 (34) vs lines expressing it (16) | 3.12× lower at baseline in the lines without KLK6 | 0.036 | ⚠ within organs, on part of the lines; also absent: EPS8L3, KLK7, TRIM15; co-absent with the target |
| [[SLC6A20]] | C | SLC6A20 activity raises KLK7's level | lines that do not express SLC6A20 (38) vs lines expressing it (12) | 3.64× lower at baseline in the lines without SLC6A20 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, REG4, HEPH; co-absent with the target |
| [[MYB]] | C | MYB activity raises KLK7's level | lines that do not express MYB (24) vs lines expressing it (26) | 1.88× lower at baseline in the lines without MYB | 0.062 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: NOS3, CKMT1B, LINC01748; co-absent with the target |
| [[PCSK9]] | C | PCSK9 activity raises KLK7's level | lines that do not express PCSK9 (28) vs lines expressing it (22) | 2.18× lower at baseline in the lines without PCSK9 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: C6orf132, RNF223, CDH1; co-absent with the target |
| [[EDAR]] | C | EDAR activity raises KLK7's level | lines that do not express EDAR (36) vs lines expressing it (14) | 3.18× lower at baseline in the lines without EDAR | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3; co-absent with the target |
| [[CKMT1A]] | C | CKMT1A activity raises KLK7's level | lines that do not express CKMT1A (28) vs lines expressing it (22) | 2.26× lower at baseline in the lines without CKMT1A | 0.089 | ⚠ within organs, on part of the lines; also absent: CKMT1B, CLDN7, EPCAM; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 1, C 21. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LARGE2]] | B | KLK7 activity raises LARGE2's level | lines that do not express KLK7 (38) vs lines expressing it (12) | 2.23× lower at baseline in the lines without KLK7 | 0.027 | ⚠ within organs, on part of the lines; also absent: KLK11, KLK6, ONECUT3 |
| [[KLK6]] | C | KLK7 activity raises KLK6's level | lines that do not express KLK7 (38) vs lines expressing it (12) | 10.83× lower at baseline in the lines without KLK7 | 0.001 | ⚠ within organs, on part of the lines; also absent: KLK11, KLK6, ONECUT3; co-absent with the target |
| [[KLK10]] | C | KLK7 activity raises KLK10's level | lines that do not express KLK7 (38) vs lines expressing it (12) | 11.76× lower at baseline in the lines without KLK7 | 0.012 | ⚠ within organs, on part of the lines; also absent: KLK11, KLK6, ONECUT3; co-absent with the target |
| [[TSPOAP1]] | C | KLK7 activity raises TSPOAP1's level | lines that do not express KLK7 (38) vs lines expressing it (12) | 2.40× lower at baseline in the lines without KLK7 | 0.013 | ⚠ within organs, on part of the lines; also absent: KLK11, KLK6, ONECUT3; co-absent with the target |
| [[VSNL1]] | C | KLK7 activity raises VSNL1's level | lines that do not express KLK7 (38) vs lines expressing it (12) | 4.19× lower at baseline in the lines without KLK7 | 0.021 | ⚠ within organs, on part of the lines; also absent: KLK11, KLK6, ONECUT3; co-absent with the target |
| [[EPS8L3]] | C | KLK7 activity raises EPS8L3's level | lines that do not express KLK7 (38) vs lines expressing it (12) | 5.12× lower at baseline in the lines without KLK7 | 0.022 | ⚠ within organs, on part of the lines; also absent: KLK11, KLK6, ONECUT3; co-absent with the target |
| [[LAD1]] | C | KLK7 activity raises LAD1's level | lines that do not express KLK7 (38) vs lines expressing it (12) | 5.48× lower at baseline in the lines without KLK7 | 0.026 | ⚠ within organs, on part of the lines; also absent: KLK11, KLK6, ONECUT3; co-absent with the target |
| [[TMEM139]] | C | KLK7 activity raises TMEM139's level | lines that do not express KLK7 (38) vs lines expressing it (12) | 3.48× lower at baseline in the lines without KLK7 | 0.028 | ⚠ within organs, on part of the lines; also absent: KLK11, KLK6, ONECUT3; co-absent with the target |
| [[EPCAM]] | C | KLK7 activity raises EPCAM's level | lines that do not express KLK7 (38) vs lines expressing it (12) | 6.89× lower at baseline in the lines without KLK7 | 0.033 | ⚠ within organs, on part of the lines; also absent: KLK11, KLK6, ONECUT3; co-absent with the target |
| [[MPZL2]] | C | KLK7 activity raises MPZL2's level | lines that do not express KLK7 (38) vs lines expressing it (12) | 5.65× lower at baseline in the lines without KLK7 | 0.039 | ⚠ within organs, on part of the lines; also absent: KLK11, KLK6, ONECUT3; co-absent with the target |
| [[APCDD1]] | C | KLK7 activity raises APCDD1's level | lines that do not express KLK7 (38) vs lines expressing it (12) | 2.37× lower at baseline in the lines without KLK7 | 0.042 | ⚠ within organs, on part of the lines; also absent: KLK11, KLK6, ONECUT3; co-absent with the target |
| [[SKAP1]] | C | KLK7 activity raises SKAP1's level | lines that do not express KLK7 (38) vs lines expressing it (12) | 5.34× lower at baseline in the lines without KLK7 | 0.044 | ⚠ within organs, on part of the lines; also absent: KLK11, KLK6, ONECUT3; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.567). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.5, 59.8); signed map (67.0, 5.0). **Vector** length 23.1, 5.81% of its response variance represented; |z| ≥ 3 in 215 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.4 | +2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.7 | +10.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +11.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +1.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.9 | -0.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.6 | +3.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.5 | +0.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.1 | -2.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.7 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.7 | -1.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.5 | -1.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.5 | -1.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.4 | -0.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | kallikrein related peptidase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.41 — chr19:50,976,468-50,984,099 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SCCE; previously PRSS6 |
| Gene groups (HGNC) | Kallikreins |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 2 pathways, smallest: Degradation of the extracellular matrix; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [P49862](https://www.uniprot.org/uniprotkb/P49862) (Kallikrein-7):

> May catalyze the degradation of intercellular cohesive structures in the cornified layer of the skin in the continuous shedding of cells from the skin surface. Specific for amino acid residues with aromatic side chains in the P1 position. Cleaves insulin A chain at '14-Tyr-|-Gln-15' and insulin B chain at '6-Leu-|-Cys-7', '16-Tyr-|-Leu-17', '25-Phe-|-Tyr-26' and '26-Tyr-|-Thr-27'. Could play a role in the activation of precursors to inflammatory cytokines.

**Summary**, from NCBI Gene [5650](https://www.ncbi.nlm.nih.gov/gene/5650):

> This gene encodes a member of the kallikrein subfamily of serine proteases. These enzymes have diverse physiological functions and many kallikrein genes are biomarkers for cancer. The encoded protein has chymotrypsin-like activity and plays a role in the proteolysis of intercellular cohesive structures that precedes desquamation, the shedding of the outermost layer of the epidermis. The encoded protein may play a role in cancer invasion and metastasis, and increased expression of this gene is …

**Accessions** — [HGNC:6368](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6368) · Entrez [5650](https://www.ncbi.nlm.nih.gov/gene/5650) · UniProt [P49862](https://www.uniprot.org/uniprotkb/P49862) · Ensembl [ENSG00000169035](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169035)

## Data

Gene col 9742: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9742); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9742, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9742]; `tensor/DDL_lfc|DDL_z.npy` [9742]; `embed/gene_vectors.npy` [9742]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9742 or target_col == 9742). Every well: [[KLK7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLK7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
