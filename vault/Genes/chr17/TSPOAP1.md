---
symbol: "TSPOAP1"
type: "gene"
col: 80
ensembl_id: "ENSG00000005379"
name: "TSPO associated protein 1"
location: "17q22"
module: 55
arm: "+"
pooled_cpm: 2.55
n_lines_expressing: 25
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 46
direction_downstream: 42
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# TSPOAP1

*TSPO associated protein 1* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.72× (z +14.1, q 4e-42, up in 8 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 2 lines (SW480 0.154×, KATO III 0.0301×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SNU-423 0.103×, LS 180 0.338×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.245×); [[Panobinostat (drug)]] 0.5 µM in 1 line (LS 180 0.217×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCAR3-AS1]] (+0.74, fdr 7e-06), [[LINC01819]] (+0.74, fdr 7e-06), [[KCNE3]] (+0.74, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 46 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 42 go from it, the strongest it → [[TSPOAP1-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 80.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.72×** | +14.1 | 4e-42 | 8/16 (BT-474, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.42×** | +13.6 | 2e-39 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.09×** | +12.1 | 2e-31 | 4/18 (LoVo, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.65×** | +9.8 | 2e-20 | 3/8 (BT-474, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.70×** | +8.1 | 8e-14 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.71×** | +5.7 | 1e-06 | 3/21 (BT-474, SNU-423, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.05×** | +5.2 | 1e-05 | 3/9 (COLO 205, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | **1.97×** | +5.1 | 2e-05 | 3/14 (SNU-423, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +4.7 | 2e-04 | 1/13 (SW480) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.78×** | +4.4 | 8e-04 | 2/17 (SW 900, SW48) | top dose only |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +4.3 | 1e-03 | 2/12 (BT-474, LoVo) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.72×** | +4.1 | 0.002 | 10/22 (HepG2/C3A, SW480, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.08×** | +3.9 | 0.003 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.71×** | +3.9 | 0.003 | 0/1 | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.05×** | +3.9 | 0.004 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.66×** | +3.8 | 0.005 | 1/13 (SNU-423) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +3.0 | 0.066 | 3/16 (SW480, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.62×** | +2.9 | 0.081 | 1/12 (COLO 205) | inconsistent across doses | noisy plate (z scaled) |
| [[Esmolol (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +2.9 | 0.093 | 1/20 (RPMI-7951) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 80.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 2 lines (SW480 0.154×, KATO III 0.0301×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SNU-423 0.103×, LS 180 0.338×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.245×); [[Panobinostat (drug)]] 0.5 µM in 1 line (LS 180 0.217×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.603× | -3.2 | 0.40 | 4/20 (SW48, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 80. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 18.9 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -11.4) |
| [[SW480 (line)]] | alt | 17.0 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.154× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 4.92 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0301× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 3.07 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -9.2) |
| [[A-172 (line)]] | wt | 0.312 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.414 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.203 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.222 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.436 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.913 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.365 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.985 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.189 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.457 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.220 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.210 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.789 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.251 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.980 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.190 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.268 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.260 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.938 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.312 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 80), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAR3-AS1]] | +0.74 | +0.66 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[LINC01819]] | +0.74 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[KCNE3]] | +0.74 | +0.76 / +0.59 | both halves | 7e-06 |  |
| [[EDAR]] | +0.73 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[IL20RA]] | +0.72 | +0.68 / +0.58 | both halves | 8e-06 |  |
| [[C9orf152]] | +0.72 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[GJB1]] | +0.70 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[ZNF503-AS1]] | +0.70 | +0.65 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[BMP4]] | +0.69 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[LINC02331]] | +0.68 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[VWA2]] | +0.68 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[CLRN3]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 5, C 41. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TSPOAP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SMOC2]] | B | SMOC2 activity raises TSPOAP1's level | lines that do not express SMOC2 (33) vs lines expressing it (17) | 1.82× lower at baseline in the lines without SMOC2 | 0.056 | ⚠ within organs, on part of the lines; also absent: LINC01456, TFF3, MIR3667HG; maybe low, not absent |
| [[MROH7]] | B | MROH7 activity raises TSPOAP1's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 1.45× lower at baseline in the lines without MROH7 | 0.078 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |
| [[SEPTIN9-DT]] | B | SEPTIN9-DT activity raises TSPOAP1's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 1.52× lower at baseline in the lines without SEPTIN9-DT | 0.081 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[MAPK13]] | B | MAPK13 activity raises TSPOAP1's level | lines that do not express MAPK13 (15) vs lines expressing it (35) | 1.84× lower at baseline in the lines without MAPK13 | 0.097 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent |
| [[VWA2]] | C | VWA2 activity raises TSPOAP1's level | lines that do not express VWA2 (36) vs lines expressing it (14) | 3.11× lower at baseline in the lines without VWA2 | 0.002 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1; co-absent with the target |
| [[TNNT2]] | C | TNNT2 activity raises TSPOAP1's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 2.41× lower at baseline in the lines without TNNT2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14; co-absent with the target |
| [[KCNE3]] | C | KCNE3 activity raises TSPOAP1's level | lines that do not express KCNE3 (37) vs lines expressing it (13) | 3.18× lower at baseline in the lines without KCNE3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SKAP1, SLC5A1, VWA2; co-absent with the target |
| [[TNFRSF14-AS1]] | C | TNFRSF14-AS1 activity raises TSPOAP1's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 2.04× lower at baseline in the lines without TNFRSF14-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB; co-absent with the target |
| [[SKAP1]] | C | SKAP1 activity raises TSPOAP1's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 2.62× lower at baseline in the lines without SKAP1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1; co-absent with the target |
| [[SLC52A3]] | C | SLC52A3 activity raises TSPOAP1's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 2.05× lower at baseline in the lines without SLC52A3 | 0.008 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7; co-absent with the target |
| [[RNF43]] | C | RNF43 activity raises TSPOAP1's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 2.39× lower at baseline in the lines without RNF43 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1; co-absent with the target |

### Downstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 12, C 30. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPOAP1-AS1]] | B | TSPOAP1 activity raises TSPOAP1-AS1's level | lines that do not express TSPOAP1 (25) vs lines expressing it (25) | 1.66× lower at baseline in the lines without TSPOAP1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RNF39, MAL2, VWA2 |
| [[FCGRT]] | B | TSPOAP1 activity raises FCGRT's level | lines that do not express TSPOAP1 (25) vs lines expressing it (25) | 1.72× lower at baseline in the lines without TSPOAP1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RNF39, MAL2, VWA2 |
| [[VILL]] | B | TSPOAP1 activity raises VILL's level | lines that do not express TSPOAP1 (25) vs lines expressing it (25) | 1.80× lower at baseline in the lines without TSPOAP1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RNF39, MAL2, VWA2 |
| [[FGD3]] | B | TSPOAP1 activity raises FGD3's level | lines that do not express TSPOAP1 (25) vs lines expressing it (25) | 2.06× lower at baseline in the lines without TSPOAP1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RNF39, MAL2, VWA2 |
| [[MAPK13]] | B | TSPOAP1 activity raises MAPK13's level | lines that do not express TSPOAP1 (25) vs lines expressing it (25) | 2.74× lower at baseline in the lines without TSPOAP1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RNF39, MAL2, VWA2 |
| [[FAAH]] | B | TSPOAP1 activity raises FAAH's level | lines that do not express TSPOAP1 (25) vs lines expressing it (25) | 1.50× lower at baseline in the lines without TSPOAP1 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RNF39, MAL2, VWA2 |
| [[STPG4]] | B | TSPOAP1 activity raises STPG4's level | lines that do not express TSPOAP1 (25) vs lines expressing it (25) | 1.98× lower at baseline in the lines without TSPOAP1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RNF39, MAL2, VWA2 |
| [[RAMP1]] | B | TSPOAP1 activity raises RAMP1's level | lines that do not express TSPOAP1 (25) vs lines expressing it (25) | 2.02× lower at baseline in the lines without TSPOAP1 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RNF39, MAL2, VWA2 |
| [[DNAJC15]] | B | TSPOAP1 activity raises DNAJC15's level | lines that do not express TSPOAP1 (25) vs lines expressing it (25) | 2.25× lower at baseline in the lines without TSPOAP1 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RNF39, MAL2, VWA2 |
| [[SEPTIN9-DT]] | B | TSPOAP1 activity raises SEPTIN9-DT's level | lines that do not express TSPOAP1 (25) vs lines expressing it (25) | 1.42× lower at baseline in the lines without TSPOAP1 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RNF39, MAL2, VWA2 |
| [[ADAP1]] | B | TSPOAP1 activity raises ADAP1's level | lines that do not express TSPOAP1 (25) vs lines expressing it (25) | 1.87× lower at baseline in the lines without TSPOAP1 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RNF39, MAL2, VWA2 |
| cells under [[Trifluridine (drug)]] 5 µM | B | TSPOAP1 activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express TSPOAP1 (25) vs lines expressing it (23) | the lines without TSPOAP1: 0.91× the cells of the other lines | 0.086 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RNF39, MAL2, VWA2 |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.773). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.8, 47.6); signed map (63.3, 11.2). **Vector** length 41.9, 8.29% of its response variance represented; |z| ≥ 3 in 561 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +13.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +12.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +1.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -3.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -0.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -0.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | TSPO associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:58,301,228-58,328,795 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRAX-1, KIAA0612, RIM-BP1, RIMBP1; previously BZRAP1 |
| Gene groups (HGNC) | Fibronectin type III domain containing; SH3 domain containing |
| Reactome | 12 pathways, smallest: Pregnenolone biosynthesis; Acetylcholine Neurotransmitter Release Cycle; Norepinephrine Neurotransmitter Release Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O95153](https://www.uniprot.org/uniprotkb/O95153) (Peripheral-type benzodiazepine receptor-associated protein 1):

> Required for synaptic transmission regulation. It probably controls the recruitment of voltage-gated calcium channels to the presynaptic membrane, and modulates neurotransmitter release.

**Summary**, from NCBI Gene [9256](https://www.ncbi.nlm.nih.gov/gene/9256):

> Enables benzodiazepine receptor binding activity. Involved in regulation of neurotransmitter secretion. Located in mitochondrion. Implicated in dystonia 22, adult-onset and dystonia 22, juvenile-onset. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16831](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16831) · Entrez [9256](https://www.ncbi.nlm.nih.gov/gene/9256) · UniProt [O95153](https://www.uniprot.org/uniprotkb/O95153) · Ensembl [ENSG00000005379](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005379)

## Data

Gene col 80: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 80); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 80, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 80]; `tensor/DDL_lfc|DDL_z.npy` [80]; `embed/gene_vectors.npy` [80]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 80 or target_col == 80). Every well: [[TSPOAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPOAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
