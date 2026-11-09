---
symbol: "BAIAP2L2"
type: "gene"
col: 4874
ensembl_id: "ENSG00000128298"
name: "BAR/IMD domain containing adaptor protein 2 like 2"
location: "22q13.1"
module: 73
arm: "+"
pooled_cpm: 7.61
n_lines_expressing: 37
n_dd_up: 10
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 28
direction_downstream: 12
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# BAIAP2L2

*BAR/IMD domain containing adaptor protein 2 like 2* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.18× (z +13.0, q 1e-35, up in 14 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.587× (z -6.3, q 2e-07, down in 18 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAP1]] (+0.66, fdr 7e-06), [[NEMP2-DT]] (+0.62, fdr 3e-05), [[INPP1]] (+0.62, fdr 9e-06); moves opposite to [[ECI2]] (-0.45, fdr 2e-04), [[ATRN]] (-0.45, fdr 1e-04), [[CBX1]] (-0.44, fdr 8e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[B3GNT3]] → it (grade B ⚠); 12 go from it, the strongest it → [[B3GNT3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4874.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.18×** | +13.0 | 1e-35 | 14/27 (AsPC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.77×** | +11.5 | 2e-28 | 2/10 (SW1417, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +9.6 | 2e-19 | 4/17 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +8.7 | 7e-16 | 11/28 (A549, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +7.7 | 2e-12 | 4/12 (A549, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +6.0 | 2e-07 | 12/20 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.64×** | +5.6 | 2e-06 | 17/29 (AsPC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +3.9 | 0.008 | 8/25 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.029 | 5/29 (LS 180, LoVo, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.066 | 1/25 (LOX-IMVI) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4874.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.587×** | -6.3 | 2e-07 | 18/34 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.668×** | -4.8 | 5e-04 | 17/33 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.691×** | -4.4 | 0.002 | 14/33 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.762× | -3.2 | 0.18 | 1/34 (AN3 CA) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.769× | -3.1 | 0.21 | 6/34 (SNU-423, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4874. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 64.7 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.112× (z -17.3) |
| [[AsPC-1 (line)]] | alt | 24.9 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.211× (z -10.2) |
| [[LoVo (line)]] | wt | 23.1 | 1 (1 ⚠) | 2 | [[Niclosamide (olamine) (drug)]] 5 µM 3.36× (z +8.5) ⚠ toxic | [[Panobinostat (drug)]] 5 µM 0.274× (z -9.5) |
| [[SW480 (line)]] | alt | 11.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.201× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.244× (z -8.7) ⚠ transcription drop |
| [[HEC-1-A (line)]] | alt | 18.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.16× (z +9.3) | — |
| [[A-172 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.76 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4874), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAP1]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[NEMP2-DT]] | +0.62 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[INPP1]] | +0.62 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[SLC22A3]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[HR]] | +0.60 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[TRABD2A]] | +0.59 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[LIME1]] | +0.57 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[SLC16A5]] | +0.56 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[NANOS3]] | +0.54 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[KRT86]] | +0.54 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[SEPTIN9-DT]] | +0.54 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[GPR35]] | +0.54 | +0.47 / +0.65 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECI2]] | -0.45 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[ATRN]] | -0.45 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[CBX1]] | -0.44 | -0.37 / -0.40 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 28, C 0. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B3GNT3]] | B | B3GNT3 activity raises BAIAP2L2's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.42× lower at baseline in the lines without B3GNT3 | 3e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[EPS8L3]] | B | EPS8L3 activity raises BAIAP2L2's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 3.90× lower at baseline in the lines without EPS8L3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[TNNT2]] | B | TNNT2 activity raises BAIAP2L2's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 2.92× lower at baseline in the lines without TNNT2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[TNS4]] | B | TNS4 activity raises BAIAP2L2's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 3.06× lower at baseline in the lines without TNS4 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[SH2D3A]] | B | SH2D3A activity raises BAIAP2L2's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 2.63× lower at baseline in the lines without SH2D3A | 0.005 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[LAD1]] | B | LAD1 activity raises BAIAP2L2's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 2.92× lower at baseline in the lines without LAD1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[GPR35]] | B | GPR35 activity raises BAIAP2L2's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 2.71× lower at baseline in the lines without GPR35 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[CYP3A5]] | B | CYP3A5 activity raises BAIAP2L2's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 3.12× lower at baseline in the lines without CYP3A5 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[SHH]] | B | SHH activity raises BAIAP2L2's level | lines that do not express SHH (29) vs lines expressing it (21) | 2.74× lower at baseline in the lines without SHH | 0.008 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[PADI1]] | B | PADI1 activity raises BAIAP2L2's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 2.47× lower at baseline in the lines without PADI1 | 0.009 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3 |
| [[SLC22A3]] | B | SLC22A3 activity raises BAIAP2L2's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 2.53× lower at baseline in the lines without SLC22A3 | 0.012 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[SULF2]] | B | SULF2 activity raises BAIAP2L2's level | lines that do not express SULF2 (24) vs lines expressing it (26) | 2.06× lower at baseline in the lines without SULF2 | 0.021 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1 |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B3GNT3]] | B | BAIAP2L2 activity raises B3GNT3's level | lines that do not express BAIAP2L2 (13) vs lines expressing it (37) | 3.22× lower at baseline in the lines without BAIAP2L2 | 0.001 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TNFRSF14-AS1]] | B | BAIAP2L2 activity raises TNFRSF14-AS1's level | lines that do not express BAIAP2L2 (13) vs lines expressing it (37) | 1.78× lower at baseline in the lines without BAIAP2L2 | 0.009 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TMEM184A]] | B | BAIAP2L2 activity raises TMEM184A's level | lines that do not express BAIAP2L2 (13) vs lines expressing it (37) | 1.66× lower at baseline in the lines without BAIAP2L2 | 0.032 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[KRT8]] | B | BAIAP2L2 activity raises KRT8's level | lines that do not express BAIAP2L2 (13) vs lines expressing it (37) | 1.39× lower at baseline in the lines without BAIAP2L2 | 0.044 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TNS4]] | B | BAIAP2L2 activity raises TNS4's level | lines that do not express BAIAP2L2 (13) vs lines expressing it (37) | 2.46× lower at baseline in the lines without BAIAP2L2 | 0.047 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SH2D3A]] | B | BAIAP2L2 activity raises SH2D3A's level | lines that do not express BAIAP2L2 (13) vs lines expressing it (37) | 2.29× lower at baseline in the lines without BAIAP2L2 | 0.055 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[EPS8L3]] | B | BAIAP2L2 activity raises EPS8L3's level | lines that do not express BAIAP2L2 (13) vs lines expressing it (37) | 2.23× lower at baseline in the lines without BAIAP2L2 | 0.062 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[RTKN]] | B | BAIAP2L2 activity raises RTKN's level | lines that do not express BAIAP2L2 (13) vs lines expressing it (37) | 1.92× lower at baseline in the lines without BAIAP2L2 | 0.064 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[GPR35]] | B | BAIAP2L2 activity raises GPR35's level | lines that do not express BAIAP2L2 (13) vs lines expressing it (37) | 1.90× lower at baseline in the lines without BAIAP2L2 | 0.079 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LAD1]] | B | BAIAP2L2 activity raises LAD1's level | lines that do not express BAIAP2L2 (13) vs lines expressing it (37) | 2.35× lower at baseline in the lines without BAIAP2L2 | 0.082 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PDE9A]] | B | BAIAP2L2 activity raises PDE9A's level | lines that do not express BAIAP2L2 (13) vs lines expressing it (37) | 1.99× lower at baseline in the lines without BAIAP2L2 | 0.084 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ARHGAP27]] | B | BAIAP2L2 activity raises ARHGAP27's level | lines that do not express BAIAP2L2 (13) vs lines expressing it (37) | 1.38× lower at baseline in the lines without BAIAP2L2 | 0.085 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.580). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (15.3, 48.7); signed map (5.3, 35.8). **Vector** length 54.7, 9.54% of its response variance represented; |z| ≥ 3 in 692 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +13.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.0 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.3 | +3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +8.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.3 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +2.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -2.0 | -4.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.7 | -4.8 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.6 | -1.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.6 | -6.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | -0.3 |
|  | [[vincristine (drug)]] 0.05 µM |  | -1.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | BAR/IMD domain containing adaptor protein 2 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:38,084,652-38,111,015 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22582, pinkbar |
| Gene groups (HGNC) | I-BAR domain containing; SH3 domain containing |
| Reactome | 4 pathways, smallest: RHOF GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UXY1](https://www.uniprot.org/uniprotkb/Q6UXY1) (BAR/IMD domain-containing adapter protein 2-like 2):

> Phosphoinositides-binding protein that induces the formation of planar or gently curved membrane structures. Binds to phosphoinositides, including to phosphatidylinositol 4,5-bisphosphate (PtdIns(4,5)P2) headgroups. There seems to be no clear preference for a specific phosphoinositide (By similarity).

**Summary**, from NCBI Gene [80115](https://www.ncbi.nlm.nih.gov/gene/80115):

> The protein encoded by this gene binds phosphoinositides and promotes the formation of planar or curved membrane structures. The encoded protein is found in RAB13-positive vesicles and at intercellular contacts with the plasma membrane. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:26203](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26203) · Entrez [80115](https://www.ncbi.nlm.nih.gov/gene/80115) · UniProt [Q6UXY1](https://www.uniprot.org/uniprotkb/Q6UXY1) · Ensembl [ENSG00000128298](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128298)

## Data

Gene col 4874: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4874); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4874, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4874]; `tensor/DDL_lfc|DDL_z.npy` [4874]; `embed/gene_vectors.npy` [4874]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4874 or target_col == 4874). Every well: [[BAIAP2L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAIAP2L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
