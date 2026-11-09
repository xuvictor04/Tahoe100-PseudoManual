---
symbol: "LRRN2"
type: "gene"
col: 9944
ensembl_id: "ENSG00000170382"
name: "leucine rich repeat neuronal 2"
location: "1q32.1"
module: 102
arm: "+"
pooled_cpm: 2.49
n_lines_expressing: 20
n_dd_up: 28
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 13
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# LRRN2

*leucine rich repeat neuronal 2* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.73× (z +10.9, q 5e-25, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +6.4, q 3e-08, up in 4 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.486× (z -5.3, q 7e-05, down in 13 of 16 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A549 0.0331×, A-172 0.113×, A-427 0.122×, LoVo 0.263×); [[Belinostat (drug)]] 5 µM in 3 lines (LoVo 0.0936×, SHP-77 0.122×, A549 0.0972×; ⚠ cell-cycle shift, explains ~26% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (LoVo 0.0421×, A549 0.0310×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 0.0880×); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (NCI-H23 0.0613×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSI1]] (+0.65, fdr 7e-06), [[DGCR5]] (+0.62, fdr 9e-06), [[ADAP2]] (+0.60, fdr 3e-05); moves opposite to [[ETFB]] (-0.47, fdr 9e-04, ⚠ not reproduced), [[EFHC1]] (-0.46, fdr 6e-04), [[TXNDC17]] (-0.44, fdr 3e-04).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 13 go from it, the strongest it → [[DNMT3A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9944.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.73×** | +10.9 | 5e-25 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.02×** | +10.2 | 9e-22 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.58×** | +8.6 | 1e-15 | 1/5 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +6.4 | 3e-08 | 4/13 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.73×** | +5.2 | 2e-05 | 0/10 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.97×** | +4.9 | 8e-05 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +4.8 | 1e-04 | 1/9 (A-172) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +4.5 | 5e-04 | 1/13 (CHP-212) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.82×** | +4.4 | 8e-04 | 7/17 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.52×** | +4.3 | 0.001 | 3/17 (LoVo, NCI-H23, …) | top dose only | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.78×** | +4.2 | 0.001 | 3/10 (NCI-H23, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +4.0 | 0.004 | 4/14 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.006 | 6/16 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.68×** | +3.8 | 0.006 | 0/13 | inconsistent across doses | low cells (technical?) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.8 | 0.006 | 2/12 (SW 900, NCI-H23) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.96×** | +3.5 | 0.016 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.60×** | +3.4 | 0.020 | 1/13 (NCI-H2030) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.024 | 4/16 (A-427, NCI-H1573, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.89×** | +3.3 | 0.028 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.55×** | +3.2 | 0.037 | 0/9 | inconsistent across doses | low cells (technical?) |
| [[Bendamustine (drug)]] 5 µM |  | **1.55×** | +3.1 | 0.053 | 0/13 | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +3.1 | 0.054 | 0/16 | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +3.0 | 0.059 | 1/15 (LoVo) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9944.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A549 0.0331×, A-172 0.113×, A-427 0.122×, LoVo 0.263×); [[Belinostat (drug)]] 5 µM in 3 lines (LoVo 0.0936×, SHP-77 0.122×, A549 0.0972×; ⚠ cell-cycle shift, explains ~26% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (LoVo 0.0421×, A549 0.0310×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 0.0880×); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (NCI-H23 0.0613×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.486×** | -5.3 | 7e-05 | 13/16 (LoVo, SHP-77, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.575×** | -4.1 | 0.013 | 10/15 (LoVo, SHP-77, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.637× | -3.3 | 0.18 | 9/16 (LoVo, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9944. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 12.0 | 0 | 9 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0421× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.263× (z -10.1) |
| [[A549 (line)]] | wt | 12.5 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0331× (z -22.0) |
| [[A-427 (line)]] | wt | 14.8 | 0 | 4 (3 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0463× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.122× (z -10.1) |
| [[A-172 (line)]] | wt | 7.46 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -12.0) |
| [[SHP-77 (line)]] | alt | 21.0 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.122× (z -11.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H23 (line)]] | alt | 4.88 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0613× (z -9.3) |
| [[A498 (line)]] | wt | 0.250 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.313 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.335 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.591 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.304 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.269 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.352 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.337 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.296 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.877 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.787 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.535 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.961 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.760 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.310 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.302 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.255 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.340 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.641 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.357 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.520 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9944), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSI1]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[DGCR5]] | +0.62 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[ADAP2]] | +0.60 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[GRID1]] | +0.60 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[RBPMS2]] | +0.59 | +0.63 / +0.40 | both halves | 4e-05 |  |
| [[FAXC]] | +0.59 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[RFPL1S]] | +0.57 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[TBKBP1]] | +0.57 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[MRAS]] | +0.57 | +0.48 / +0.37 | both halves | 8e-05 |  |
| [[CHMP1B2P]] | +0.56 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[LINC00466]] | +0.56 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[SMO]] | +0.55 | +0.57 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETFB]] | -0.47 | -0.40 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[EFHC1]] | -0.46 | -0.35 / -0.22 | both halves | 6e-04 |  |
| [[TXNDC17]] | -0.44 | -0.28 / -0.32 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises LRRN2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RET]] | C | RET activity raises LRRN2's level | lines that do not express RET (28) vs lines expressing it (22) | 2.93× lower at baseline in the lines without RET | 0.015 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1; co-absent with the target |
| [[CECR2]] | C | CECR2 activity raises LRRN2's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 2.02× lower at baseline in the lines without CECR2 | 0.022 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent; co-absent with the target |
| [[ANKRD6]] | C | ANKRD6 activity raises LRRN2's level | lines that do not express ANKRD6 (16) vs lines expressing it (34) | 2.21× lower at baseline in the lines without ANKRD6 | 0.039 | ⚠ within organs, on part of the lines; also absent: MAP9, RIMKLB, TUB; co-absent with the target |
| [[ARHGEF25]] | C | ARHGEF25 activity raises LRRN2's level | lines that do not express ARHGEF25 (15) vs lines expressing it (35) | 2.16× lower at baseline in the lines without ARHGEF25 | 0.079 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, RASSF8-AS1, CHST10; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 8, C 5. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNMT3A]] | B | LRRN2 activity raises DNMT3A's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 1.47× lower at baseline in the lines without LRRN2 | 0.018 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL |
| [[SMO]] | B | LRRN2 activity raises SMO's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 1.84× lower at baseline in the lines without LRRN2 | 0.055 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL |
| [[KCND3]] | B | LRRN2 activity raises KCND3's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 1.48× lower at baseline in the lines without LRRN2 | 0.056 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL |
| [[MVB12B]] | B | LRRN2 activity raises MVB12B's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 1.21× lower at baseline in the lines without LRRN2 | 0.079 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL |
| [[FAM124A]] | B | LRRN2 activity raises FAM124A's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 1.67× lower at baseline in the lines without LRRN2 | 0.088 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL |
| [[GNAL]] | B | LRRN2 activity raises GNAL's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 1.71× lower at baseline in the lines without LRRN2 | 0.091 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL |
| [[ATP6V1E2]] | B | LRRN2 activity raises ATP6V1E2's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 1.52× lower at baseline in the lines without LRRN2 | 0.091 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL |
| [[USP46]] | B | LRRN2 activity raises USP46's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 1.21× lower at baseline in the lines without LRRN2 | 0.092 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL |
| [[CECR2]] | C | LRRN2 activity raises CECR2's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 3.26× lower at baseline in the lines without LRRN2 | 0.018 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL; co-absent with the target |
| [[RET]] | C | LRRN2 activity raises RET's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 2.71× lower at baseline in the lines without LRRN2 | 0.042 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL; co-absent with the target |
| [[ANKRD6]] | C | LRRN2 activity raises ANKRD6's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 2.38× lower at baseline in the lines without LRRN2 | 0.044 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL; co-absent with the target |
| [[PALM]] | C | LRRN2 activity raises PALM's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 2.59× lower at baseline in the lines without LRRN2 | 0.089 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL; co-absent with the target |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.681). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.1, 36.3); signed map (26.4, 24.8). **Vector** length 39.1, 8.99% of its response variance represented; |z| ≥ 3 in 420 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -1.6 | -3.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -1.4 | -5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.4 | -4.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -1.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -2.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat neuronal 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:204,617,170-204,685,738 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GAC1, LRANK1, FIGLER7; previously LRRN5 |
| Gene groups (HGNC) | I-set domain containing |
| Matched by | ensembl_id |

UniProt [O75325](https://www.uniprot.org/uniprotkb/O75325) carries no function annotation.

**Summary**, from NCBI Gene [10446](https://www.ncbi.nlm.nih.gov/gene/10446):

> The protein encoded by this gene belongs to the leucine-rich repeat superfamily. This gene was found to be amplified and overexpressed in malignant gliomas. The encoded protein has homology with other proteins that function as cell-adhesion molecules or as signal transduction receptors and is a candidate for the target gene in the 1q32.1 amplicon in malignant gliomas. Two alternatively spliced transcript variants encoding the same protein have been described for this gene. [provided by RefSeq, …

**Accessions** — [HGNC:16914](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16914) · Entrez [10446](https://www.ncbi.nlm.nih.gov/gene/10446) · UniProt [O75325](https://www.uniprot.org/uniprotkb/O75325) · Ensembl [ENSG00000170382](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170382)

## Data

Gene col 9944: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9944); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9944, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9944]; `tensor/DDL_lfc|DDL_z.npy` [9944]; `embed/gene_vectors.npy` [9944]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9944 or target_col == 9944). Every well: [[LRRN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
