---
symbol: "DPYSL5"
type: "gene"
col: 8106
ensembl_id: "ENSG00000157851"
name: "dihydropyrimidinase like 5"
location: "2p23.3"
module: 82
arm: "+"
pooled_cpm: 4.17
n_lines_expressing: 20
n_dd_up: 41
n_dd_down: 0
n_dd_up_clean: 30
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 13
direction_downstream: 35
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# DPYSL5

*dihydropyrimidinase like 5* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.31× (z +27.6, q 0e+00, up in 12 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.157×, A-172 0.234×, BT-474 0.173×); [[Harringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.106×, A-172 0.0993×; ⚠ cell-cycle shift, explains ~12% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.124×, A-172 0.157×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (A-427 0.256×, A-172 0.228×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JAKMIP1]] (+0.75, fdr 7e-06), [[GPC3]] (+0.70, fdr 7e-06), [[KCNQ2]] (+0.70, fdr 7e-06).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 35 go from it, the strongest it → [[MAPT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8106.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.31×** | +27.6 | 0e+00 | 12/15 (A549, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.30×** | +17.4 | 0e+00 | 3/5 (SHP-77, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **4.50×** | +14.8 | 0e+00 | 7/17 (C32, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.48×** | +14.7 | 0e+00 | 8/12 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.53×** | +12.8 | 1e-35 | 15/17 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.34×** | +11.8 | 6e-30 | 4/15 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.50×** | +11.4 | 5e-28 | 3/8 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.16×** | +11.3 | 1e-27 | 12/17 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.80×** | +10.1 | 4e-22 | 12/17 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.75×** | +9.9 | 2e-21 | 13/17 (HOP62, SW 900, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.22×** | +7.8 | 3e-13 | 15/17 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.20×** | +7.7 | 5e-13 | 12/14 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.20×** | +7.7 | 6e-13 | 14/16 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.03×** | +6.9 | 2e-10 | 2/10 (LoVo, NCI-H2030) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +6.3 | 2e-08 | 4/14 (BT-474, LoVo, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.19×** | +6.0 | 9e-08 | 12/16 (NCI-H23, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.5 | 1e-06 | 1/17 (SW 900) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +4.4 | 3e-04 | 1/14 (C32) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.55×** | +4.3 | 5e-04 | 3/17 (A-172, NCI-H23, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8106.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.157×, A-172 0.234×, BT-474 0.173×); [[Harringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.106×, A-172 0.0993×; ⚠ cell-cycle shift, explains ~12% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.124×, A-172 0.157×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (A-427 0.256×, A-172 0.228×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.693× | -3.6 | 0.15 | 10/17 (A-427, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Perindopril (erbumine) (drug)]] 0.5 µM |  | 0.716× | -3.3 | 0.24 | 1/17 (H4) | inconsistent across doses |  |
| [[Malotilate (drug)]] 5 µM |  | 0.737× | -3.0 | 0.44 | 2/17 (C-33 A, BT-474) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8106. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 39.8 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -20.6) |
| [[A-172 (line)]] | wt | 17.6 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0993× (z -13.7) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.234× (z -12.2) |
| [[BT-474 (line)]] | alt | 9.11 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0505× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Omeprazole (drug)]] 0.5 µM 0.0750× (z -9.8) |
| [[A549 (line)]] | wt | 4.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +12.2) | — |
| [[LoVo (line)]] | wt | 3.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.57× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 7.96 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0763× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[NCI-H23 (line)]] | alt | 6.43 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0901× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[A498 (line)]] | wt | 0.707 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.586 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.597 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.609 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.652 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.483 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.596 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.690 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.561 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.740 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.487 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.550 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.676 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.535 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.733 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8106), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JAKMIP1]] | +0.75 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[GPC3]] | +0.70 | +0.61 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[KCNQ2]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[RET]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[SEPTIN3]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ADCY1]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[KIF26A]] | +0.64 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[CRMP1]] | +0.62 | +0.46 / +0.57 | both halves | 2e-05 | same gene group; pathway: CRMPs in Sema3A signaling; STRING 482 |
| [[GRID1]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[MAP6]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[JPH3]] | +0.60 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[ADD2]] | +0.60 | +0.55 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 2, C 11. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DPYSL5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.7% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TMEM150C]] | B | TMEM150C activity raises DPYSL5's level | lines that do not express TMEM150C (13) vs lines expressing it (37) | 2.35× lower at baseline in the lines without TMEM150C | 0.089 | ⚠ within organs, on part of the lines; also absent: AP3B2, MED12L, RAB6B; maybe low, not absent |
| [[CHD5]] | C | CHD5 activity raises DPYSL5's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 3.67× lower at baseline in the lines without CHD5 | 4e-04 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent; co-absent with the target |
| [[NFASC]] | C | NFASC activity raises DPYSL5's level | lines that do not express NFASC (27) vs lines expressing it (23) | 3.04× lower at baseline in the lines without NFASC | 0.001 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A; co-absent with the target |
| [[KIF1A]] | C | KIF1A activity raises DPYSL5's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 3.44× lower at baseline in the lines without KIF1A | 0.005 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7; co-absent with the target |
| [[RET]] | C | RET activity raises DPYSL5's level | lines that do not express RET (28) vs lines expressing it (22) | 3.07× lower at baseline in the lines without RET | 0.014 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1; co-absent with the target |
| [[MYT1]] | C | MYT1 activity raises DPYSL5's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 2.59× lower at baseline in the lines without MYT1 | 0.019 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2; co-absent with the target |
| [[MED12L]] | C | MED12L activity raises DPYSL5's level | lines that do not express MED12L (18) vs lines expressing it (32) | 2.49× lower at baseline in the lines without MED12L | 0.029 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2; co-absent with the target |
| [[LMX1B]] | C | LMX1B activity raises DPYSL5's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 2.81× lower at baseline in the lines without LMX1B | 0.036 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2; co-absent with the target |
| [[KIF26A]] | C | KIF26A activity raises DPYSL5's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.58× lower at baseline in the lines without KIF26A | 0.043 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN; co-absent with the target |
| [[CECR2]] | C | CECR2 activity raises DPYSL5's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 2.72× lower at baseline in the lines without CECR2 | 0.052 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent; co-absent with the target |
| [[SCN8A]] | C | SCN8A activity raises DPYSL5's level | lines that do not express SCN8A (18) vs lines expressing it (32) | 2.25× lower at baseline in the lines without SCN8A | 0.053 | ⚠ within organs, on part of the lines; also absent: DPYSL5, PDZD4, STOX2; co-absent with the target |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 18, C 17. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAPT]] | B | DPYSL5 activity raises MAPT's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.82× lower at baseline in the lines without DPYSL5 | 0.006 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[TMEM150C]] | B | DPYSL5 activity raises TMEM150C's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.85× lower at baseline in the lines without DPYSL5 | 0.012 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[GPRIN1]] | B | DPYSL5 activity raises GPRIN1's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.11× lower at baseline in the lines without DPYSL5 | 0.014 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[KCNK13]] | B | DPYSL5 activity raises KCNK13's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 1.74× lower at baseline in the lines without DPYSL5 | 0.027 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[VASH1]] | B | DPYSL5 activity raises VASH1's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.21× lower at baseline in the lines without DPYSL5 | 0.030 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[CACNA2D2]] | B | DPYSL5 activity raises CACNA2D2's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.29× lower at baseline in the lines without DPYSL5 | 0.031 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[SBK1]] | B | DPYSL5 activity raises SBK1's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.58× lower at baseline in the lines without DPYSL5 | 0.035 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[EBF4]] | B | DPYSL5 activity raises EBF4's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.68× lower at baseline in the lines without DPYSL5 | 0.046 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[DBNDD1]] | B | DPYSL5 activity raises DBNDD1's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 1.54× lower at baseline in the lines without DPYSL5 | 0.057 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[CAMK2B]] | B | DPYSL5 activity raises CAMK2B's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 1.65× lower at baseline in the lines without DPYSL5 | 0.059 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[RASGEF1C]] | B | DPYSL5 activity raises RASGEF1C's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.08× lower at baseline in the lines without DPYSL5 | 0.062 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[CDH23]] | B | DPYSL5 activity raises CDH23's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 1.64× lower at baseline in the lines without DPYSL5 | 0.072 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.754). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.3, 39.0); signed map (26.7, 27.2). **Vector** length 42.6, 10.1% of its response variance represented; |z| ≥ 3 in 500 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cardiac conduction* (reactome, mean cos +0.51 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +12.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +17.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +14.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +11.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +14.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +6.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +5.5 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -1.5 | +0.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.4 | +3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -2.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -2.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.8 | +0.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | -0.8 | +0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.7 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | dihydropyrimidinase like 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:26,847,747-26,950,351 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CRMP5, Ulip6, CRMP-5, CRAM, CV2 |
| Gene groups (HGNC) | M38 metallopeptidases |
| Reactome | 4 pathways, smallest: CRMPs in Sema3A signaling; Semaphorin interactions; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BPU6](https://www.uniprot.org/uniprotkb/Q9BPU6) (Dihydropyrimidinase-related protein 5):

> Involved in the negative regulation of dendrite outgrowth.

**Summary**, from NCBI Gene [56896](https://www.ncbi.nlm.nih.gov/gene/56896):

> This gene encodes a member of the CRMP (collapsing response mediator protein) family thought to be involved in neural development. Antibodies to the encoded protein were found in some patients with neurologic symptoms who had paraneoplastic syndrome. A pseudogene of this gene is found on chromosome 11. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:20637](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20637) · Entrez [56896](https://www.ncbi.nlm.nih.gov/gene/56896) · UniProt [Q9BPU6](https://www.uniprot.org/uniprotkb/Q9BPU6) · Ensembl [ENSG00000157851](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157851)

## Data

Gene col 8106: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8106); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8106, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8106]; `tensor/DDL_lfc|DDL_z.npy` [8106]; `embed/gene_vectors.npy` [8106]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8106 or target_col == 8106). Every well: [[DPYSL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPYSL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
