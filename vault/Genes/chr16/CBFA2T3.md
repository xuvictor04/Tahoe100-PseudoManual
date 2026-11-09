---
symbol: "CBFA2T3"
type: "gene"
col: 5013
ensembl_id: "ENSG00000129993"
name: "CBFA2/RUNX1 partner transcriptional co-repressor 3"
location: "16q24.3"
module: 128
arm: "+"
pooled_cpm: 3.3
n_lines_expressing: 26
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 16
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# CBFA2T3

*CBFA2/RUNX1 partner transcriptional co-repressor 3* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.32× (z +14.8, q 0e+00, up in 10 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.243×, A-427 0.173×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.154×, A-172 0.0583×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-427 0.0366×; ⚠ cell-cycle shift, explains ~23% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.163×); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.0825×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELFN1]] (+0.67, fdr 7e-06), [[PALM]] (+0.65, fdr 7e-06), [[SRCIN1]] (+0.64, fdr 7e-06).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[KREMEN2]] → it (grade B ⚠); 16 go from it, the strongest it → [[GSE1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5013.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.32×** | +14.8 | 0e+00 | 10/21 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.41×** | +12.5 | 3e-33 | 8/20 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.96×** | +11.6 | 1e-28 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.65×** | +8.5 | 3e-15 | 13/20 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +8.2 | 2e-14 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.38×** | +7.6 | 3e-12 | 2/7 (HOP62, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +6.2 | 5e-08 | 3/17 (A549, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +5.7 | 1e-06 | 6/22 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.89×** | +4.0 | 0.005 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +3.9 | 0.006 | 3/19 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +3.7 | 0.010 | 9/20 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.71×** | +3.3 | 0.038 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +3.3 | 0.038 | 1/5 (PANC-1) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5013.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.243×, A-427 0.173×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.154×, A-172 0.0583×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-427 0.0366×; ⚠ cell-cycle shift, explains ~23% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.163×); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.0825×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.655× | -3.7 | 0.13 | 10/23 (NCI-H23, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.691× | -3.2 | 0.25 | 7/22 (A-427, NCI-H23, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.692× | -3.2 | 0.25 | 3/20 (A-172, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5013. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 24.0 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -15.8) |
| [[A-427 (line)]] | wt | 10.6 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0366× (z -16.4) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0825× (z -11.9) |
| [[PANC-1 (line)]] | alt | 11.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.07× (z +17.8) | — |
| [[A-172 (line)]] | wt | 3.71 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0583× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 1.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 4.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.78× (z +8.7) | — |
| [[A498 (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.482 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.319 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.617 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.483 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.290 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.685 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.639 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.627 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.388 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.339 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.354 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.560 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.284 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5013), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELFN1]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[PALM]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[SRCIN1]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[KCNQ2]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[NFATC1]] | +0.59 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[KREMEN2]] | +0.58 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[KCNQ4]] | +0.56 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[NKAIN1]] | +0.55 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[ZBTB46]] | +0.55 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[CHD5]] | +0.54 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[KCND3]] | +0.54 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[GALNT9]] | +0.53 | +0.38 / +0.58 | both halves | 6e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KREMEN2]] | B | KREMEN2 activity raises CBFA2T3's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 1.85× lower at baseline in the lines without KREMEN2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |
| [[CECR2]] | B | CECR2 activity raises CBFA2T3's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 1.92× lower at baseline in the lines without CECR2 | 0.061 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent |
| [[ELFN1]] | B | ELFN1 activity raises CBFA2T3's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 1.55× lower at baseline in the lines without ELFN1 | 0.080 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[KIF26A]] | B | KIF26A activity raises CBFA2T3's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.04× lower at baseline in the lines without KIF26A | 0.082 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[ADGRB1]] | B | ADGRB1 activity raises CBFA2T3's level | lines that do not express ADGRB1 (18) vs lines expressing it (32) | 1.95× lower at baseline in the lines without ADGRB1 | 0.097 | ⚠ within organs, on part of the lines; also absent: KSR2, BEGAIN, B4GALNT4; maybe low, not absent |
| [[KIF1A]] | C | KIF1A activity raises CBFA2T3's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 3.17× lower at baseline in the lines without KIF1A | 0.001 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7; co-absent with the target |
| [[BEGAIN]] | C | BEGAIN activity raises CBFA2T3's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 2.30× lower at baseline in the lines without BEGAIN | 0.005 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent; co-absent with the target |
| [[CHD5]] | C | CHD5 activity raises CBFA2T3's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 2.18× lower at baseline in the lines without CHD5 | 0.048 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent; co-absent with the target |
| [[B4GALNT4]] | C | B4GALNT4 activity raises CBFA2T3's level | lines that do not express B4GALNT4 (18) vs lines expressing it (32) | 1.79× lower at baseline in the lines without B4GALNT4 | 0.094 | ⚠ within organs, on part of the lines; also absent: SRRM3, ST6GAL1, KIF26A; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 12, C 4. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GSE1]] | B | CBFA2T3 activity raises GSE1's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 1.82× lower at baseline in the lines without CBFA2T3 | 0.008 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |
| [[MOB3C]] | B | CBFA2T3 activity lowers MOB3C's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 1.37× higher at baseline in the lines without CBFA2T3 | 0.009 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |
| [[AATK]] | B | CBFA2T3 activity raises AATK's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 1.73× lower at baseline in the lines without CBFA2T3 | 0.022 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |
| [[CACNA1H]] | B | CBFA2T3 activity raises CACNA1H's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 2.30× lower at baseline in the lines without CBFA2T3 | 0.028 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |
| [[KREMEN2]] | B | CBFA2T3 activity raises KREMEN2's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 1.85× lower at baseline in the lines without CBFA2T3 | 0.031 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |
| [[PTP4A3]] | B | CBFA2T3 activity raises PTP4A3's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 1.77× lower at baseline in the lines without CBFA2T3 | 0.041 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |
| [[ELFN1]] | B | CBFA2T3 activity raises ELFN1's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 2.00× lower at baseline in the lines without CBFA2T3 | 0.042 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |
| [[PWWP2B]] | B | CBFA2T3 activity raises PWWP2B's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 1.48× lower at baseline in the lines without CBFA2T3 | 0.050 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |
| [[CERS4]] | B | CBFA2T3 activity raises CERS4's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 1.99× lower at baseline in the lines without CBFA2T3 | 0.057 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |
| [[PRDM16]] | B | CBFA2T3 activity raises PRDM16's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 2.36× lower at baseline in the lines without CBFA2T3 | 0.077 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |
| [[NKAIN1]] | B | CBFA2T3 activity raises NKAIN1's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 1.57× lower at baseline in the lines without CBFA2T3 | 0.087 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |
| [[ZBTB46]] | B | CBFA2T3 activity raises ZBTB46's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 1.73× lower at baseline in the lines without CBFA2T3 | 0.089 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.598). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.4, 38.0); signed map (24.6, 23.4). **Vector** length 42.2, 7.79% of its response variance represented; |z| ≥ 3 in 560 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +14.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +11.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +5.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.1 | +2.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.1 | +2.8 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.3 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -0.9 | -1.6 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.8 | -1.9 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | CBFA2/RUNX1 partner transcriptional co-repressor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:88,874,858-88,977,207 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MTGR2, ZMYND4, MTG16, RUNX1T3, ETO2 |
| Gene groups (HGNC) | Zinc fingers MYND-type; A-kinase anchoring proteins |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [O75081](https://www.uniprot.org/uniprotkb/O75081) (Transcriptional corepressor CBFA2T3):

> Transcriptional corepressor which facilitates transcriptional repression via its association with DNA-binding transcription factors and recruitment of other corepressors and histone-modifying enzymes. Can repress the expression of MMP7 in a ZBTB33-dependent manner. Reduces the protein levels and stability of the transcriptinal regulator HIF1A; interacts with EGLN1 and promotes the HIF1A prolyl hydroxylation-dependent ubiquitination and proteasomal degradation pathway. Contributes to inhibition …

**Summary**, from NCBI Gene [863](https://www.ncbi.nlm.nih.gov/gene/863):

> This gene encodes a member of the myeloid translocation gene family which interact with DNA-bound transcription factors and recruit a range of corepressors to facilitate transcriptional repression. The t(16;21)(q24;q22) translocation is one of the less common karyotypic abnormalities in acute myeloid leukemia. The translocation produces a chimeric gene made up of the 5'-region of the runt-related transcription factor 1 gene fused to the 3'-region of this gene. This gene is also a putative …

**Accessions** — [HGNC:1537](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1537) · Entrez [863](https://www.ncbi.nlm.nih.gov/gene/863) · UniProt [O75081](https://www.uniprot.org/uniprotkb/O75081) · Ensembl [ENSG00000129993](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129993)

## Data

Gene col 5013: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5013); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5013, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5013]; `tensor/DDL_lfc|DDL_z.npy` [5013]; `embed/gene_vectors.npy` [5013]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5013 or target_col == 5013). Every well: [[CBFA2T3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CBFA2T3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
