---
symbol: "NCMAP"
type: "gene"
col: 11539
ensembl_id: "ENSG00000184454"
name: "non-compact myelin associated protein"
location: "1p36.11"
module: 44
arm: "+"
pooled_cpm: 2.76
n_lines_expressing: 24
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 19
direction_downstream: 35
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# NCMAP

*non-compact myelin associated protein* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.76× (z +17.1, q 0e+00, up in 3 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LoVo 0.0612×, HepG2/C3A 0.129×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.242×); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.166×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.284×); [[Selinexor (drug)]] 5 µM in 1 line (CFPAC-1 0.274×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TJP3]] (+0.69, fdr 7e-06), [[LMTK3]] (+0.65, fdr 2e-05), [[GALM]] (+0.61, fdr 1e-05); moves opposite to [[SPRY3]] (-0.51, fdr 1e-04), [[PRR14L]] (-0.51, fdr 6e-05), [[ENOX2]] (-0.51, fdr 1e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[NR3C2]] → it (grade B ⚠); 35 go from it, the strongest it → [[RHPN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11539.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.76×** | +17.1 | 0e+00 | 3/15 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.21×** | +13.2 | 5e-37 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.27×** | +12.8 | 5e-35 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.79×** | +11.1 | 1e-26 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.04×** | +9.2 | 4e-18 | 15/21 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.98×** | +6.2 | 5e-08 | 12/21 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +5.8 | 4e-07 | 13/20 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.57×** | +5.8 | 5e-07 | 3/18 (NCI-H2347, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.80×** | +5.3 | 6e-06 | 11/20 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.79×** | +5.3 | 6e-06 | 13/18 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +5.2 | 1e-05 | 1/11 (HEC-1-A) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.7 | 1e-04 | 2/14 (HepG2/C3A, NCI-H2347) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +4.5 | 3e-04 | 4/18 (SW480, HCT15, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.51×** | +4.4 | 5e-04 | 0/3 | top dose only | noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +4.1 | 0.001 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +3.7 | 0.005 | 11/21 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.49×** | +3.7 | 0.007 | 1/12 (HEC-1-A) | inconsistent across doses | low cells (technical?) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.49×** | +3.6 | 0.008 | 0/15 | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.70×** | +3.5 | 0.014 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.42×** | +3.2 | 0.038 | 4/21 (COLO 205, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.057 | 1/21 (LoVo) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.26×** | +2.9 | 0.069 | 1/16 (HT-29) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11539.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LoVo 0.0612×, HepG2/C3A 0.129×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.242×); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.166×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.284×); [[Selinexor (drug)]] 5 µM in 1 line (CFPAC-1 0.274×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | 0.694× | -3.4 | 0.40 | 3/21 (Panc 03.27, SW48, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.695× | -3.1 | 0.41 | 1/21 (NCI-H2030) | inconsistent across doses |  |
| [[OTS514 (drug)]] 0.5 µM |  | 0.634× | -3.0 | 0.41 | 0/21 | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11539. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 47.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.242× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 16.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.274× (z -9.3) |
| [[HT-29 (line)]] | alt | 13.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -9.5) |
| [[LoVo (line)]] | wt | 4.27 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0612× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 3.45 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0679× (z -8.6) |
| [[A-172 (line)]] | wt | 0.439 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.764 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.923 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.649 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.570 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.448 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.510 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.462 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.661 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.915 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.718 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.748 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.929 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.404 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11539), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TJP3]] | +0.69 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[LMTK3]] | +0.65 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[GALM]] | +0.61 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[SERPINA5]] | +0.60 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[ESPN]] | +0.58 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[CYP4F12]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[AGFG2]] | +0.58 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[RNF183]] | +0.56 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[ENPP5]] | +0.56 | +0.37 / +0.49 | both halves | 7e-05 |  |
| [[SHF]] | +0.55 | +0.39 / +0.54 | both halves | 6e-05 |  |
| [[MGAT4A]] | +0.55 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[TNNI3]] | +0.54 | +0.37 / +0.48 | both halves | 8e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRY3]] | -0.51 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[PRR14L]] | -0.51 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[ENOX2]] | -0.51 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[POLDIP2]] | -0.49 | -0.37 / -0.41 | both halves | 7e-05 |  |
| [[CSTF3]] | -0.48 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[RNASEH1]] | -0.48 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[DNAAF10]] | -0.48 | -0.32 / -0.30 | both halves | 2e-04 |  |
| [[MTHFSD]] | -0.47 | -0.29 / -0.48 | both halves | 3e-04 |  |
| [[TRIM66]] | -0.47 | -0.30 / -0.34 | both halves | 2e-04 |  |
| [[MAPKAPK5]] | -0.47 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[UBE3B]] | -0.47 | -0.26 / -0.40 | both halves | 4e-04 |  |
| [[SLC30A9]] | -0.47 | -0.37 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 4, C 15. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C2]] | B | NR3C2 activity raises NCMAP's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.77× lower at baseline in the lines without NR3C2 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[CDS1]] | B | CDS1 activity raises NCMAP's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 1.82× lower at baseline in the lines without CDS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[LNX1]] | B | LNX1 activity raises NCMAP's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 1.83× lower at baseline in the lines without LNX1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[ATP8B1]] | B | ATP8B1 activity raises NCMAP's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 1.87× lower at baseline in the lines without ATP8B1 | 0.091 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[ATP2C2]] | C | ATP2C2 activity raises NCMAP's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 2.24× lower at baseline in the lines without ATP2C2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |
| [[ENPP5]] | C | ENPP5 activity raises NCMAP's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 1.82× lower at baseline in the lines without ENPP5 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004; co-absent with the target |
| [[RNF183]] | C | RNF183 activity raises NCMAP's level | lines that do not express RNF183 (36) vs lines expressing it (14) | 2.83× lower at baseline in the lines without RNF183 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, LINC02964, VIL1; co-absent with the target |
| [[MPP7]] | C | MPP7 activity raises NCMAP's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 2.03× lower at baseline in the lines without MPP7 | 0.012 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent; co-absent with the target |
| [[ANKRD22]] | C | ANKRD22 activity raises NCMAP's level | lines that do not express ANKRD22 (34) vs lines expressing it (16) | 1.99× lower at baseline in the lines without ANKRD22 | 0.013 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25; co-absent with the target |
| [[TJP3]] | C | TJP3 activity raises NCMAP's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.60× lower at baseline in the lines without TJP3 | 0.016 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1; co-absent with the target |
| [[PLEKHG6]] | C | PLEKHG6 activity raises NCMAP's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 2.59× lower at baseline in the lines without PLEKHG6 | 0.018 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent; co-absent with the target |
| [[ALOX5]] | C | ALOX5 activity raises NCMAP's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 1.73× lower at baseline in the lines without ALOX5 | 0.025 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6; co-absent with the target |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 19, C 16. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHPN2]] | B | NCMAP activity raises RHPN2's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 2.61× lower at baseline in the lines without NCMAP | 0.001 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent |
| [[CLMN]] | B | NCMAP activity raises CLMN's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 2.50× lower at baseline in the lines without NCMAP | 0.008 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent |
| [[WDR27]] | B | NCMAP activity lowers WDR27's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 1.48× higher at baseline in the lines without NCMAP | 0.016 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent |
| [[PNKD]] | B | NCMAP activity raises PNKD's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 1.31× lower at baseline in the lines without NCMAP | 0.022 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent |
| [[CDS1]] | B | NCMAP activity raises CDS1's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 3.59× lower at baseline in the lines without NCMAP | 0.027 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent |
| [[VAV1]] | B | NCMAP activity raises VAV1's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 2.12× lower at baseline in the lines without NCMAP | 0.029 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent |
| [[RABL2B]] | B | NCMAP activity lowers RABL2B's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 1.25× higher at baseline in the lines without NCMAP | 0.034 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent |
| [[RHPN2]] | B | NCMAP activity strengthens RHPN2's drug response | lines that do not express NCMAP (23) vs lines expressing it (23) | the lines without NCMAP respond 0.72× as strongly (z diff +2.44); strongest at Homoharringtonine 5 µM: 0.80x vs 0.45x (z diff +5.4) | 0.069 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[GALM]] | B | NCMAP activity raises GALM's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 2.01× lower at baseline in the lines without NCMAP | 0.072 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent |
| [[GCHFR]] | B | NCMAP activity raises GCHFR's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 2.20× lower at baseline in the lines without NCMAP | 0.073 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent |
| [[CARD14]] | B | NCMAP activity raises CARD14's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 1.60× lower at baseline in the lines without NCMAP | 0.077 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent |
| [[FMO5]] | B | NCMAP activity raises FMO5's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 1.59× lower at baseline in the lines without NCMAP | 0.077 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.462). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.2, 51.2); signed map (69.1, 15.8). **Vector** length 38.9, 8.19% of its response variance represented; |z| ≥ 3 in 436 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +12.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +11.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +0.9 | +2.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.8 | +2.6 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.4 | +0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -2.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -1.1 | +3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.1 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -0.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.0 | +0.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | non-compact myelin associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:24,556,087-24,609,328 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ42528, MP11; previously C1orf130 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T1S8](https://www.uniprot.org/uniprotkb/Q5T1S8) (Noncompact myelin-associated protein):

> Plays a role in myelin formation.

**Summary**, from NCBI Gene [400746](https://www.ncbi.nlm.nih.gov/gene/400746):

> Predicted to be a structural constituent of myelin sheath. Predicted to be involved in peripheral nervous system myelin formation and positive regulation of myelination. Predicted to be located in plasma membrane. Predicted to be active in Schmidt-Lanterman incisure and paranode region of axon. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29332](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29332) · Entrez [400746](https://www.ncbi.nlm.nih.gov/gene/400746) · UniProt [Q5T1S8](https://www.uniprot.org/uniprotkb/Q5T1S8) · Ensembl [ENSG00000184454](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184454)

## Data

Gene col 11539: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11539); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11539, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11539]; `tensor/DDL_lfc|DDL_z.npy` [11539]; `embed/gene_vectors.npy` [11539]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11539 or target_col == 11539). Every well: [[NCMAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCMAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
