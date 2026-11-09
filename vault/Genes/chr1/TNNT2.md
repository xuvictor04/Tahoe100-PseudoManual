---
symbol: "TNNT2"
type: "gene"
col: 3969
ensembl_id: "ENSG00000118194"
name: "troponin T2, cardiac type"
location: "1q32.1"
module: 47
arm: "+"
pooled_cpm: 3.34
n_lines_expressing: 21
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 45
direction_downstream: 98
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# TNNT2

*troponin T2, cardiac type* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.87× (z +11.7, q 8e-29, up in 8 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.568× (z -4.5, q 0.003, down in 8 of 17 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (LoVo 0.0533×; ⚠ toxic; transcription drop); [[Ivabradine (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.0452×; ⚠ unreliable plate only); [[Belumosudil (drug)]] 5 µM in 1 line (HT-29 0.0344×); [[Digitoxin (drug)]] 0.05 µM in 1 line (BT-474 0.0469×); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 0.233×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MROH3P]] (+0.65, fdr 7e-06), [[KRT86]] (+0.64, fdr 9e-06), [[SEMA4A]] (+0.63, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 45 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 98 go from it, the strongest it → [[FAM83E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3969.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.87×** | +11.7 | 8e-29 | 8/17 (LoVo, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.01×** | +10.5 | 3e-23 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +8.5 | 4e-15 | 5/17 (NCI-H2347, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.54×** | +7.3 | 5e-11 | 1/13 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.70×** | +7.2 | 7e-11 | 1/8 (NCI-H1573) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.28×** | +6.2 | 5e-08 | 5/13 (NCI-H1573, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.81×** | +4.6 | 3e-04 | 0/14 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +4.2 | 0.002 | 4/17 (LS 180, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +4.1 | 0.003 | 2/17 (LS 180, SW480) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.69×** | +4.1 | 0.003 | 3/17 (NCI-H2347, SW1417, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +3.8 | 0.007 | 1/15 (SW1417) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.91×** | +3.6 | 0.014 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.62×** | +3.6 | 0.014 | 0/16 | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.6 | 0.014 | 4/15 (SW1417, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.58×** | +3.5 | 0.016 | 3/16 (KATO III, HCT15, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +3.3 | 0.030 | 3/17 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.040 | 0/17 | top dose only | position effect removed |
| [[Verteporfin (drug)]] 0.05 µM |  | **1.56×** | +3.2 | 0.040 | 1/17 (HCT15) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3969.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (LoVo 0.0533×; ⚠ toxic; transcription drop); [[Ivabradine (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.0452×; ⚠ unreliable plate only); [[Belumosudil (drug)]] 5 µM in 1 line (HT-29 0.0344×); [[Digitoxin (drug)]] 0.05 µM in 1 line (BT-474 0.0469×); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 0.233×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.568×** | -4.5 | 0.003 | 8/17 (LoVo, HT-29, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.624×** | -3.8 | 0.045 | 9/17 (COLO 205, LoVo, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Riluzole hydrochloride (drug)]] 0.05 µM |  | 0.661× | -3.3 | 0.17 | 1/17 (LS 180) | inconsistent across doses | position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.652× | -3.2 | 0.21 | 0/17 | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.681× | -3.1 | 0.23 | 1/17 (AsPC-1) | all doses, flat | cell-cycle shift (explains ~4% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3969. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 9.80 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +10.7) | [[Digitoxin (drug)]] 5 µM 0.0533× (z -12.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 34.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -9.6) |
| [[SW48 (line)]] | wt | 12.3 | 0 | 2 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 5 µM 0.0452× (z -11.1) ⚠ unreliable plate only · without an alert: [[Ranolazine (drug)]] 0.05 µM 0.0754× (z -9.2) |
| [[BT-474 (line)]] | alt | 6.18 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0469× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 7.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.08× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 6.29 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0344× (z -11.0) |
| [[SW480 (line)]] | alt | 9.10 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.318× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.636 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.322 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.410 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.750 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.861 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.415 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.557 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.433 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.406 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.355 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.539 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.519 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.630 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.396 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.300 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.428 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.908 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3969), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MROH3P]] | +0.65 | +0.61 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[KRT86]] | +0.64 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[SEMA4A]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[LSMEM2]] | +0.62 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[CAPN8]] | +0.62 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[FGD5]] | +0.61 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ADAP1]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[TMEM184A]] | +0.59 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[MPZL2]] | +0.59 | +0.54 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[IL1RN]] | +0.59 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[FSCN2]] | +0.58 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[BTBD16]] | +0.57 | +0.49 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*45 arrows, 45 of them with an alert ⚠; grade A 0, B 7, C 38. Shown: the 12 strongest; 33 more arrows (33 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TNNT2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers TNNT2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SEMA4A]] | B | SEMA4A activity raises TNNT2's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.96× lower at baseline in the lines without SEMA4A | 0.038 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[LSMEM2]] | B | LSMEM2 activity raises TNNT2's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 2.22× lower at baseline in the lines without LSMEM2 | 0.050 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[MFNG]] | B | MFNG activity raises TNNT2's level | lines that do not express MFNG (12) vs lines expressing it (38) | 2.28× lower at baseline in the lines without MFNG | 0.054 | ⚠ within organs, on part of the lines; also absent: CARD10, EPS8L2, KRT8 |
| [[SEPTIN9-DT]] | B | SEPTIN9-DT activity raises TNNT2's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 2.36× lower at baseline in the lines without SEPTIN9-DT | 0.070 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[MROH7]] | B | MROH7 activity raises TNNT2's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 1.76× lower at baseline in the lines without MROH7 | 0.074 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |
| [[LAD1]] | C | LAD1 activity raises TNNT2's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 4.83× lower at baseline in the lines without LAD1 | 2e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1; co-absent with the target |
| [[MPZL2]] | C | MPZL2 activity raises TNNT2's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 4.43× lower at baseline in the lines without MPZL2 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14; co-absent with the target |
| [[MROH3P]] | C | MROH3P activity raises TNNT2's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 3.94× lower at baseline in the lines without MROH3P | 7e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3; co-absent with the target |
| [[ITGB6]] | C | ITGB6 activity raises TNNT2's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 4.24× lower at baseline in the lines without ITGB6 | 1e-04 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4; co-absent with the target |
| [[TMEM45B]] | C | TMEM45B activity raises TNNT2's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 4.20× lower at baseline in the lines without TMEM45B | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881; co-absent with the target |

### Downstream of this gene

*98 arrows, 98 of them with an alert ⚠; grade A 0, B 54, C 44. Shown: the 12 strongest; 86 more arrows (86 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83E]] | B | TNNT2 activity raises FAM83E's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 4.37× lower at baseline in the lines without TNNT2 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[LSMEM2]] | B | TNNT2 activity raises LSMEM2's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 2.49× lower at baseline in the lines without TNNT2 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[FHDC1]] | B | TNNT2 activity raises FHDC1's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 2.36× lower at baseline in the lines without TNNT2 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[TMEM184A]] | B | TNNT2 activity raises TMEM184A's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 2.76× lower at baseline in the lines without TNNT2 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[BAIAP2L2]] | B | TNNT2 activity raises BAIAP2L2's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 2.92× lower at baseline in the lines without TNNT2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[ADAP1]] | B | TNNT2 activity raises ADAP1's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 3.19× lower at baseline in the lines without TNNT2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[MROH6]] | B | TNNT2 activity raises MROH6's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 2.11× lower at baseline in the lines without TNNT2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[ARHGAP27]] | B | TNNT2 activity raises ARHGAP27's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 2.66× lower at baseline in the lines without TNNT2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[PSD4]] | B | TNNT2 activity raises PSD4's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 3.16× lower at baseline in the lines without TNNT2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[ARMC7]] | B | TNNT2 activity raises ARMC7's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 1.52× lower at baseline in the lines without TNNT2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[UNC13D]] | B | TNNT2 activity raises UNC13D's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 2.91× lower at baseline in the lines without TNNT2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[MROH7]] | B | TNNT2 activity raises MROH7's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 2.47× lower at baseline in the lines without TNNT2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.4, 49.8); signed map (57.2, 12.7). **Vector** length 44.3, 10.3% of its response variance represented; |z| ≥ 3 in 452 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +1.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.2 | +0.5 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -2.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -3.2 |
|  | [[Riluzole hydrochloride (drug)]] 0.05 µM |  | -1.0 | -3.3 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.0 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | troponin T2, cardiac type |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:201,359,008-201,377,764 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CMPD2; previously CMH2, CMD1D |
| Gene groups (HGNC) | Troponin complex subunits |
| Hallmark sets | MYOGENESIS, KRAS_SIGNALING_UP |
| Reactome | 2 pathways, smallest: Striated Muscle Contraction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [P45379](https://www.uniprot.org/uniprotkb/P45379) (Troponin T, cardiac muscle):

> Troponin T is the tropomyosin-binding subunit of troponin, the thin filament regulatory complex which confers calcium-sensitivity to striated muscle actomyosin ATPase activity.

**Summary**, from NCBI Gene [7139](https://www.ncbi.nlm.nih.gov/gene/7139):

> This gene encodes the cardiac isoform of troponin T. The encoded protein is the tropomyosin-binding subunit of the troponin complex, which is located on the thin filament of striated muscles and regulates muscle contraction in response to alterations in intracellular calcium ion concentration. Mutations in this gene have been associated with familial hypertrophic cardiomyopathy as well as with dilated cardiomyopathy. [provided by RefSeq, May 2022]

**Accessions** — [HGNC:11949](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11949) · Entrez [7139](https://www.ncbi.nlm.nih.gov/gene/7139) · UniProt [P45379](https://www.uniprot.org/uniprotkb/P45379) · Ensembl [ENSG00000118194](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118194)

## Data

Gene col 3969: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3969); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3969, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3969]; `tensor/DDL_lfc|DDL_z.npy` [3969]; `embed/gene_vectors.npy` [3969]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3969 or target_col == 3969). Every well: [[TNNT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNNT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
