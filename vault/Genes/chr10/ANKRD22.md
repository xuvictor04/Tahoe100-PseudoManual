---
symbol: "ANKRD22"
type: "gene"
col: 7655
ensembl_id: "ENSG00000152766"
name: "ankyrin repeat domain 22"
location: "10q23.31"
module: 8
arm: "+"
pooled_cpm: 6.23
n_lines_expressing: 16
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 80
direction_downstream: 101
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ANKRD22

*ankyrin repeat domain 22* — 10q23.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.63× (z +8.8, q 8e-16, up in 0 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.98× (z +8.7, q 8e-16, up in 8 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (COLO 205 0.0740×, LS 180 0.239×, NCI-H1573 0.309×; ⚠ cell-cycle shift, explains ~25% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HT-29 0.141×, LS 180 0.181×, COLO 205 0.154×); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.174×, LS 180 0.165×, COLO 205 0.155×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (COLO 205 0.159×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (NCI-H1573 0.302×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SULT2B1]] (+0.69, fdr 1e-05), [[TMEM45B]] (+0.68, fdr 9e-06), [[PLS1]] (+0.66, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 80 arrows point to it, the strongest [[DAPP1]] → it (grade C ⚠); 101 go from it, the strongest it → [[PIK3C2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7655.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.63×** | +8.8 | 8e-16 | 0/9 | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.98×** | +8.7 | 8e-16 | 8/13 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.79×** | +8.6 | 2e-15 | 0/8 | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +8.1 | 6e-14 | 0/7 | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.10×** | +6.7 | 2e-09 | 1/11 (KATO III) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.87×** | +5.7 | 1e-06 | 9/12 (NCI-H2347, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +5.2 | 2e-05 | 10/13 (BT-474, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.1 | 2e-05 | 0/12 | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.39×** | +4.2 | 0.002 | 6/13 (NCI-H2347, HT-29, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +3.6 | 0.016 | 5/12 (BT-474, LS 180, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.18×** | +3.6 | 0.016 | 0/9 | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.4 | 0.036 | 1/10 (CFPAC-1) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.03×** | +3.3 | 0.046 | 1/3 (HT-29) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 0.05 µM |  | **1.43×** | +3.1 | 0.092 | 0/13 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7655.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (COLO 205 0.0740×, LS 180 0.239×, NCI-H1573 0.309×; ⚠ cell-cycle shift, explains ~25% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HT-29 0.141×, LS 180 0.181×, COLO 205 0.154×); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.174×, LS 180 0.165×, COLO 205 0.155×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (COLO 205 0.159×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (NCI-H1573 0.302×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.759× | -3.6 | 0.12 | 4/13 (HCT15, SW1417, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.687× | -3.4 | 0.12 | 4/13 (LS 180, NCI-H1573, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.667× | -3.4 | 0.12 | 2/13 (LS 180, KATO III) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.712× | -3.1 | 0.17 | 3/13 (COLO 205, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | 0.703× | -3.1 | 0.17 | 2/13 (LoVo, NCI-H1573) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.523× | -3.0 | 0.17 | 2/13 (CFPAC-1, LS 180) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | 0.524× | -3.0 | 0.17 | 2/13 (Panc 03.27, NCI-H1573) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.701× | -3.0 | 0.17 | 0/13 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7655. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 83.1 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -15.4) |
| [[NCI-H1573 (line)]] | alt | 50.7 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.302× (z -8.6) |
| [[COLO 205 (line)]] | alt | 43.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0740× (z -19.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -14.0) |
| [[HT-29 (line)]] | alt | 29.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -15.7) |
| [[A-172 (line)]] | wt | 0.672 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.522 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.572 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.680 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.864 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.761 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.658 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.759 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.855 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.617 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.859 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.800 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.585 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.757 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.643 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.652 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.754 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.935 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.659 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7655), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SULT2B1]] | +0.69 | +0.56 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[TMEM45B]] | +0.68 | +0.57 / +0.70 | both halves | 9e-06 |  |
| [[PLS1]] | +0.66 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.66 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[MPZL2]] | +0.65 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[ILDR2]] | +0.62 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[ITGB6]] | +0.62 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[CYP3A5]] | +0.61 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[SLC5A1]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[LIPH]] | +0.60 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[LINC03040]] | +0.59 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[ST14]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*80 arrows, 80 of them with an alert ⚠; grade A 0, B 0, C 80. Shown: the 12 strongest; 68 more arrows (68 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DAPP1]] | C | DAPP1 activity raises ANKRD22's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 6.04× lower at baseline in the lines without DAPP1 | 1e-04 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises ANKRD22's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 5.50× lower at baseline in the lines without TMPRSS4 | 2e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[TMEM125]] | C | TMEM125 activity raises ANKRD22's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 5.39× lower at baseline in the lines without TMEM125 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; co-absent with the target |
| [[ARHGEF38]] | C | ARHGEF38 activity raises ANKRD22's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 5.99× lower at baseline in the lines without ARHGEF38 | 2e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1; co-absent with the target |
| [[ATP2C2]] | C | ATP2C2 activity raises ANKRD22's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 4.99× lower at baseline in the lines without ATP2C2 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |
| [[SLC6A14]] | C | SLC6A14 activity raises ANKRD22's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 5.89× lower at baseline in the lines without SLC6A14 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1; co-absent with the target |
| [[MAL2]] | C | MAL2 activity raises ANKRD22's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 4.44× lower at baseline in the lines without MAL2 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; co-absent with the target |
| [[SLC28A3]] | C | SLC28A3 activity raises ANKRD22's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 3.41× lower at baseline in the lines without SLC28A3 | 2e-04 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14; co-absent with the target |
| [[ST6GALNAC1]] | C | ST6GALNAC1 activity raises ANKRD22's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 5.28× lower at baseline in the lines without ST6GALNAC1 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4; co-absent with the target |
| [[ST14]] | C | ST14 activity raises ANKRD22's level | lines that do not express ST14 (32) vs lines expressing it (18) | 4.96× lower at baseline in the lines without ST14 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1; co-absent with the target |
| [[TRIM15]] | C | TRIM15 activity raises ANKRD22's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 4.60× lower at baseline in the lines without TRIM15 | 5e-04 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises ANKRD22's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 4.97× lower at baseline in the lines without ADGRF1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |

### Downstream of this gene

*101 arrows, 101 of them with an alert ⚠; grade A 0, B 29, C 72. Shown: the 12 strongest; 89 more arrows (89 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIK3C2B]] | B | ANKRD22 activity raises PIK3C2B's level | lines that do not express ANKRD22 (34) vs lines expressing it (16) | 2.37× lower at baseline in the lines without ANKRD22 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25 |
| [[ARHGEF16]] | B | ANKRD22 activity raises ARHGEF16's level | lines that do not express ANKRD22 (34) vs lines expressing it (16) | 3.16× lower at baseline in the lines without ANKRD22 | 0.004 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25 |
| [[TNFRSF21]] | B | ANKRD22 activity raises TNFRSF21's level | lines that do not express ANKRD22 (34) vs lines expressing it (16) | 4.41× lower at baseline in the lines without ANKRD22 | 0.008 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25 |
| [[PLS1]] | B | ANKRD22 activity raises PLS1's level | lines that do not express ANKRD22 (34) vs lines expressing it (16) | 3.92× lower at baseline in the lines without ANKRD22 | 0.011 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25 |
| [[ATP1B1]] | B | ANKRD22 activity raises ATP1B1's level | lines that do not express ANKRD22 (34) vs lines expressing it (16) | 2.89× lower at baseline in the lines without ANKRD22 | 0.012 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25 |
| cells under [[Mifepristone (drug)]] 0.5 µM | B | ANKRD22 activity lowers the cells' numbers under Mifepristone 0.5 µM (makes them more sensitive) | lines that do not express ANKRD22 (34) vs lines expressing it (14) | the lines without ANKRD22: 1.26× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25 |
| [[RHPN2]] | B | ANKRD22 activity raises RHPN2's level | lines that do not express ANKRD22 (34) vs lines expressing it (16) | 2.88× lower at baseline in the lines without ANKRD22 | 0.027 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25 |
| cells under [[Apalutamide (drug)]] 0.5 µM | B | ANKRD22 activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express ANKRD22 (34) vs lines expressing it (14) | the lines without ANKRD22: 1.27× the cells of the other lines | 0.027 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25 |
| [[DTX2]] | B | ANKRD22 activity raises DTX2's level | lines that do not express ANKRD22 (34) vs lines expressing it (16) | 1.81× lower at baseline in the lines without ANKRD22 | 0.034 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25 |
| cells under [[Tirabrutinib (drug)]] 0.5 µM | B | ANKRD22 activity lowers the cells' numbers under Tirabrutinib 0.5 µM (makes them more sensitive) | lines that do not express ANKRD22 (34) vs lines expressing it (14) | the lines without ANKRD22: 1.19× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25 |
| [[SPINT1]] | B | ANKRD22 activity strengthens SPINT1's drug response | lines that do not express ANKRD22 (10) vs lines expressing it (14) | the lines without ANKRD22 respond 0.53× as strongly (z diff +2.57); strongest at Homoharringtonine 5 µM: 0.56x vs 0.34x (z diff +5.2) | 0.039 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25; target measured in part of the lines; artifact flags |
| [[SLC25A25]] | B | ANKRD22 activity raises SLC25A25's level | lines that do not express ANKRD22 (34) vs lines expressing it (16) | 2.07× lower at baseline in the lines without ANKRD22 | 0.043 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.567). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.0, 55.9); signed map (59.7, 8.0). **Vector** length 45.3, 14.7% of its response variance represented; |z| ≥ 3 in 320 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +8.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.1 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +0.9 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -0.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -3.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -3.4 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.31 — chr10:88,819,896-88,851,844 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC22805 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q5VYY1](https://www.uniprot.org/uniprotkb/Q5VYY1) carries no function annotation.

**Summary**, from NCBI Gene [118932](https://www.ncbi.nlm.nih.gov/gene/118932):

> Predicted to act upstream of or within several processes, including calcium ion import; leukocyte migration; and response to wounding. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28321](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28321) · Entrez [118932](https://www.ncbi.nlm.nih.gov/gene/118932) · UniProt [Q5VYY1](https://www.uniprot.org/uniprotkb/Q5VYY1) · Ensembl [ENSG00000152766](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152766)

## Data

Gene col 7655: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7655); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7655, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7655]; `tensor/DDL_lfc|DDL_z.npy` [7655]; `embed/gene_vectors.npy` [7655]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7655 or target_col == 7655). Every well: [[ANKRD22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
