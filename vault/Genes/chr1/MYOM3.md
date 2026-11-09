---
symbol: "MYOM3"
type: "gene"
col: 6643
ensembl_id: "ENSG00000142661"
name: "myomesin 3"
location: "1p36.11"
module: 55
arm: "+"
pooled_cpm: 3.99
n_lines_expressing: 23
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 30
direction_downstream: 37
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# MYOM3

*myomesin 3* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.51× (z +14.7, q 0e+00, up in 6 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.49× (z +5.0, q 5e-05, up in 4 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.627× (z -4.2, q 0.012, down in 11 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BTBD16]] (+0.59, fdr 2e-05), [[LINC01559]] (+0.50, fdr 1e-04), [[LINC03040]] (+0.49, fdr 3e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[SEC16B]] → it (grade B ⚠); 37 go from it, the strongest it → [[PLA2R1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6643.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.51×** | +14.7 | 0e+00 | 6/8 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.88×** | +12.2 | 1e-31 | 3/12 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.06×** | +9.3 | 3e-18 | 3/10 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +5.6 | 3e-06 | 1/11 (A498) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +5.0 | 5e-05 | 4/20 (HOP62, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.65×** | +4.5 | 7e-04 | 8/17 (HOP62, CFPAC-1, …) | two highest doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +4.3 | 0.002 | 1/17 (LoVo) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +4.2 | 0.002 | 5/20 (KATO III, SW480, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.58×** | +4.1 | 0.003 | 1/13 (HepG2/C3A) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.9 | 0.005 | 0/15 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.005 | 0/15 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.54×** | +3.9 | 0.005 | 0/15 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.83×** | +3.9 | 0.005 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.56×** | +3.8 | 0.006 | 0/14 | top dose only |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.8 | 0.006 | 3/13 (A-172, A549, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.64×** | +3.2 | 0.053 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.061 | 7/20 (HT-29, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +3.0 | 0.085 | 4/17 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +2.9 | 0.088 | 2/17 (COLO 205, LS 180) | inconsistent across doses | cell-cycle shift (explains ~21% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6643.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.627×** | -4.2 | 0.012 | 11/20 (A-172, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.635×** | -4.1 | 0.012 | 10/18 (HEC-1-A, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.656×** | -3.8 | 0.027 | 12/20 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.471×** | -3.5 | 0.056 | 8/16 (HepG2/C3A, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.477×** | -3.5 | 0.057 | 7/17 (HepG2/C3A, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ritonavir (drug)]] 0.05 µM |  | **0.685×** | -3.4 | 0.063 | 4/18 (AsPC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | **0.693×** | -3.3 | 0.078 | 3/20 (SW48, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6643. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 17.1 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -10.0) |
| [[A-172 (line)]] | wt | 16.3 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.181× (z -8.6) |
| [[HT-29 (line)]] | alt | 20.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0665× (z -19.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -11.6) |
| [[A549 (line)]] | wt | 5.23 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0844× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 2.39 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0405× (z -11.5) ⚠ cell-cycle shift, explains ~51% of this change |
| [[HepG2_C3A (line)]] | wt | 50.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -13.7) |
| [[LS 180 (line)]] | wt | 9.86 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 6.31 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 7.51 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0663× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 0.594 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.520 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.458 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.500 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.744 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.426 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.609 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.618 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.623 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.816 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.475 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.435 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.757 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.550 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.452 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.715 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6643), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTBD16]] | +0.59 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[LINC01559]] | +0.50 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[LINC03040]] | +0.49 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[VILL]] | +0.48 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[LINC02474]] | +0.48 | +0.36 / +0.42 | both halves | 1e-04 |  |
| [[HR]] | +0.48 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[DSCAML1]] | +0.48 | +0.55 / +0.34 | both halves | 1e-04 | same gene group |
| [[USH1C]] | +0.47 | +0.36 / +0.55 | both halves | 1e-04 |  |
| [[TPRXL]] | +0.47 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[ZNF736P9Y]] | +0.47 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[IL22RA1]] | +0.46 | +0.49 / +0.39 | both halves | 5e-05 | ⚠ same locus (7.6 kb, same strand: neighbours can correlate without regulation) |
| [[HNF4A]] | +0.46 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[GDA]] | +0.45 | +0.42 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 4, C 26. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEC16B]] | B | SEC16B activity raises MYOM3's level | lines that do not express SEC16B (13) vs lines expressing it (37) | 2.11× lower at baseline in the lines without SEC16B | 0.050 | ⚠ within organs, on part of the lines; also absent: CRYZL2P, CYP2S1, GRHL3 |
| [[NMRAL2P]] | B | NMRAL2P activity raises MYOM3's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 2.04× lower at baseline in the lines without NMRAL2P | 0.052 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[PLA2R1]] | B | PLA2R1 activity raises MYOM3's level | lines that do not express PLA2R1 (19) vs lines expressing it (31) | 1.61× lower at baseline in the lines without PLA2R1 | 0.068 | ⚠ within organs, on part of the lines; also absent: CYP2S1, RARRES1, IL18 |
| [[CRYZL2P]] | B | CRYZL2P activity raises MYOM3's level | lines that do not express CRYZL2P (14) vs lines expressing it (36) | 1.89× lower at baseline in the lines without CRYZL2P | 0.074 | ⚠ within organs, on part of the lines; also absent: SEC16B |
| [[POF1B]] | C | POF1B activity raises MYOM3's level | lines that do not express POF1B (34) vs lines expressing it (16) | 1.79× lower at baseline in the lines without POF1B | 0.012 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises MYOM3's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 2.15× lower at baseline in the lines without MUC13 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[GDA]] | C | GDA activity raises MYOM3's level | lines that do not express GDA (35) vs lines expressing it (15) | 2.40× lower at baseline in the lines without GDA | 0.021 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4; co-absent with the target |
| [[LASTR]] | C | LASTR activity raises MYOM3's level | lines that do not express LASTR (22) vs lines expressing it (28) | 1.94× lower at baseline in the lines without LASTR | 0.024 | ⚠ within organs, on part of the lines; also absent: TINAGL1, PCSK9, ANXA3; maybe low, not absent; co-absent with the target |
| [[B3GNT3]] | C | B3GNT3 activity raises MYOM3's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 2.20× lower at baseline in the lines without B3GNT3 | 0.028 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1; co-absent with the target |
| [[MUC17]] | C | MUC17 activity raises MYOM3's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 2.17× lower at baseline in the lines without MUC17 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1; co-absent with the target |
| [[IGFL2-AS1]] | C | IGFL2-AS1 activity raises MYOM3's level | lines that do not express IGFL2-AS1 (36) vs lines expressing it (14) | 2.56× lower at baseline in the lines without IGFL2-AS1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, CLRN3, LINC01559; co-absent with the target |
| [[CYP4F3]] | C | CYP4F3 activity raises MYOM3's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 2.62× lower at baseline in the lines without CYP4F3 | 0.038 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6; co-absent with the target |

### Downstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 8, C 29. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLA2R1]] | B | MYOM3 activity raises PLA2R1's level | lines that do not express MYOM3 (27) vs lines expressing it (23) | 2.62× lower at baseline in the lines without MYOM3 | 0.003 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, USH1C |
| [[NOSTRIN]] | B | MYOM3 activity raises NOSTRIN's level | lines that do not express MYOM3 (27) vs lines expressing it (23) | 2.43× lower at baseline in the lines without MYOM3 | 0.007 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, USH1C |
| [[MROH7]] | B | MYOM3 activity raises MROH7's level | lines that do not express MYOM3 (27) vs lines expressing it (23) | 2.35× lower at baseline in the lines without MYOM3 | 0.021 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, USH1C |
| [[VILL]] | B | MYOM3 activity raises VILL's level | lines that do not express MYOM3 (27) vs lines expressing it (23) | 1.88× lower at baseline in the lines without MYOM3 | 0.022 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, USH1C |
| [[LINC02580]] | B | MYOM3 activity raises LINC02580's level | lines that do not express MYOM3 (27) vs lines expressing it (23) | 1.87× lower at baseline in the lines without MYOM3 | 0.036 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, USH1C |
| [[HGD]] | B | MYOM3 activity raises HGD's level | lines that do not express MYOM3 (27) vs lines expressing it (23) | 3.10× lower at baseline in the lines without MYOM3 | 0.042 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, USH1C |
| [[HTR1D]] | B | MYOM3 activity raises HTR1D's level | lines that do not express MYOM3 (27) vs lines expressing it (23) | 1.44× lower at baseline in the lines without MYOM3 | 0.050 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, USH1C |
| [[FUT2]] | B | MYOM3 activity raises FUT2's level | lines that do not express MYOM3 (27) vs lines expressing it (23) | 1.95× lower at baseline in the lines without MYOM3 | 0.088 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, USH1C |
| [[EPS8L3]] | C | MYOM3 activity raises EPS8L3's level | lines that do not express MYOM3 (27) vs lines expressing it (23) | 4.66× lower at baseline in the lines without MYOM3 | 0.001 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, USH1C; co-absent with the target |
| [[HNF4A]] | C | MYOM3 activity raises HNF4A's level | lines that do not express MYOM3 (27) vs lines expressing it (23) | 7.72× lower at baseline in the lines without MYOM3 | 0.001 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, USH1C; co-absent with the target |
| [[GPR35]] | C | MYOM3 activity raises GPR35's level | lines that do not express MYOM3 (27) vs lines expressing it (23) | 3.68× lower at baseline in the lines without MYOM3 | 0.001 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, USH1C; co-absent with the target |
| [[USH1C]] | C | MYOM3 activity raises USH1C's level | lines that do not express MYOM3 (27) vs lines expressing it (23) | 4.75× lower at baseline in the lines without MYOM3 | 0.002 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, USH1C; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.483). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.8, 52.0); signed map (62.3, 8.9). **Vector** length 44.8, 10.2% of its response variance represented; |z| ≥ 3 in 519 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -4.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | -1.7 | -1.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.6 | -0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.4 | -3.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.1 | -2.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -2.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -0.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | myomesin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:24,056,035-24,112,135 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35961 |
| Gene groups (HGNC) | I-set domain containing; Myosin binding proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VTT5](https://www.uniprot.org/uniprotkb/Q5VTT5) (Myomesin-3):

> May link the intermediate filament cytoskeleton to the M-disk of the myofibrils in striated muscle.

**Summary**, from NCBI Gene [127294](https://www.ncbi.nlm.nih.gov/gene/127294):

> Predicted to enable protein homodimerization activity. Predicted to be a structural constituent of muscle. Predicted to be involved in sarcomere organization. Predicted to be active in M band. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26679](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26679) · Entrez [127294](https://www.ncbi.nlm.nih.gov/gene/127294) · UniProt [Q5VTT5](https://www.uniprot.org/uniprotkb/Q5VTT5) · Ensembl [ENSG00000142661](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142661)

## Data

Gene col 6643: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6643); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6643, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6643]; `tensor/DDL_lfc|DDL_z.npy` [6643]; `embed/gene_vectors.npy` [6643]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6643 or target_col == 6643). Every well: [[MYOM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYOM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
