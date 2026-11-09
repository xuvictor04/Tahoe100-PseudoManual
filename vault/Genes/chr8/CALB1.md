---
symbol: "CALB1"
type: "gene"
col: 2442
ensembl_id: "ENSG00000104327"
name: "calbindin 1"
location: "8q21.3"
module: 73
arm: "+"
pooled_cpm: 61.29
n_lines_expressing: 8
n_dd_up: 3
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 46
direction_downstream: 46
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# CALB1

*calbindin 1* — 8q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.00× (z +8.4, q 2e-14, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.569× (z -4.3, q 0.009, down in 5 of 6 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LoVo 0.0748×, LS 180 0.0904×, Hs 766T 0.122×, SW480 0.223×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LoVo 0.134×, LS 180 0.139×, Hs 766T 0.284×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (LoVo 0.113×, LS 180 0.141×, SW480 0.191×); [[Belinostat (drug)]] 5 µM in 3 lines (LoVo 0.152×, SW480 0.144×, LS 180 0.202×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02582]] (+0.86, fdr 7e-06), [[TPRXL]] (+0.85, fdr 7e-06), [[NPSR1]] (+0.83, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 46 arrows point to it, the strongest [[LINC02582]] → it (grade C ⚠); 46 go from it, the strongest it → [[ABHD12B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2442.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.00×** | +8.4 | 2e-14 | 1/5 (HEC-1-A) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.26×** | +6.0 | 5e-07 | 1/5 (HEC-1-A) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +5.3 | 3e-05 | 1/5 (HEC-1-A) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | 1.53× | +3.3 | 0.13 | 0/6 | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.52× | +3.2 | 0.13 | 2/6 (SW480, COLO 205) | two highest doses | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 2.19× | +3.1 | 0.16 | 2/6 (SW480, HEC-1-A) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2442.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LoVo 0.0748×, LS 180 0.0904×, Hs 766T 0.122×, SW480 0.223×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LoVo 0.134×, LS 180 0.139×, Hs 766T 0.284×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (LoVo 0.113×, LS 180 0.141×, SW480 0.191×); [[Belinostat (drug)]] 5 µM in 3 lines (LoVo 0.152×, SW480 0.144×, LS 180 0.202×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.569×** | -4.3 | 0.009 | 5/6 (LS 180, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.616×** | -3.7 | 0.061 | 6/6 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Larotrectinib (drug)]] 5 µM |  | 0.729× | -3.4 | 0.13 | 6/6 (Hs 766T, LoVo, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.892× | -3.1 | 0.27 | 0/7 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | 0.673× | -3.0 | 0.27 | 6/6 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~8% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2442. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 1,144 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0748× (z -22.7) |
| [[LS 180 (line)]] | wt | 383 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0904× (z -19.8) |
| [[SW480 (line)]] | alt | 32.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -12.1) |
| [[Hs 766T (line)]] | wt | 281 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -16.8) |
| [[A-172 (line)]] | wt | 5.01 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.27 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.39 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.75 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.08 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.14 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.15 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.42 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.48 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.43 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.63 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.44 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.86 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.49 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.03 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.47 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.47 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.71 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.45 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.78 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.69 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.48 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.43 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.62 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.44 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.83 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.67 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.39 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.92 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.96 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 8.05 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.71 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2442), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02582]] | +0.86 | +0.78 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[TPRXL]] | +0.85 | +0.80 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[NPSR1]] | +0.83 | +0.74 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[TPTEP1-1]] | +0.83 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[MUC17]] | +0.82 | +0.73 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[DSG4]] | +0.81 | +0.76 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[HEPH]] | +0.78 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[SLC6A20]] | +0.77 | +0.71 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[LINC02474]] | +0.77 | +0.73 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[SERPINB5]] | +0.75 | +0.71 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[INPP5D]] | +0.74 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[SPON1]] | +0.74 | +0.74 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 0, C 46. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02582]] | C | LINC02582 activity raises CALB1's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 7.74× lower at baseline in the lines without LINC02582 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; co-absent with the target |
| [[MUC2]] | C | MUC2 activity raises CALB1's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 7.25× lower at baseline in the lines without MUC2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4; co-absent with the target |
| [[ERG]] | C | ERG activity raises CALB1's level | lines that do not express ERG (30) vs lines expressing it (20) | 1.95× lower at baseline in the lines without ERG | 0.004 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent; co-absent with the target |
| [[SPON1]] | C | SPON1 activity raises CALB1's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 6.26× lower at baseline in the lines without SPON1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A; co-absent with the target |
| [[XACT]] | C | XACT activity raises CALB1's level | lines that do not express XACT (30) vs lines expressing it (20) | 2.31× lower at baseline in the lines without XACT | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, ENSG00000267284, LINC02438; co-absent with the target |
| [[PIWIL1]] | C | PIWIL1 activity raises CALB1's level | lines that do not express PIWIL1 (38) vs lines expressing it (12) | 5.30× lower at baseline in the lines without PIWIL1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, CALB1, CLRN3; co-absent with the target |
| [[KRT6A]] | C | KRT6A activity raises CALB1's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 6.25× lower at baseline in the lines without KRT6A | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588; co-absent with the target |
| [[UGT1A1]] | C | UGT1A1 activity raises CALB1's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 3.64× lower at baseline in the lines without UGT1A1 | 0.006 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1; co-absent with the target |
| [[TPTEP1-1]] | C | TPTEP1-1 activity raises CALB1's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 3.51× lower at baseline in the lines without TPTEP1-1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975; co-absent with the target |
| [[UGT1A6]] | C | UGT1A6 activity raises CALB1's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 3.25× lower at baseline in the lines without UGT1A6 | 0.008 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1; co-absent with the target |
| [[EDAR]] | C | EDAR activity raises CALB1's level | lines that do not express EDAR (36) vs lines expressing it (14) | 5.22× lower at baseline in the lines without EDAR | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3; co-absent with the target |
| [[LINC02474]] | C | LINC02474 activity raises CALB1's level | lines that do not express LINC02474 (40) vs lines expressing it (10) | 4.42× lower at baseline in the lines without LINC02474 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC4, SFTPA2, ENSG00000230975; co-absent with the target |

### Downstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 8, C 38. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABHD12B]] | B | CALB1 activity raises ABHD12B's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 3.63× lower at baseline in the lines without CALB1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588 |
| [[NCF2]] | B | CALB1 activity raises NCF2's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 2.31× lower at baseline in the lines without CALB1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588 |
| [[KPNA2P3]] | B | CALB1 activity raises KPNA2P3's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 1.85× lower at baseline in the lines without CALB1 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588 |
| [[IGSF9]] | B | CALB1 activity raises IGSF9's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 2.22× lower at baseline in the lines without CALB1 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588 |
| [[PITPNM3]] | B | CALB1 activity raises PITPNM3's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 2.10× lower at baseline in the lines without CALB1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588 |
| [[SDCBP2]] | B | CALB1 activity raises SDCBP2's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 4.41× lower at baseline in the lines without CALB1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588 |
| [[PPARG]] | B | CALB1 activity raises PPARG's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 3.89× lower at baseline in the lines without CALB1 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588 |
| [[ALS2CL]] | B | CALB1 activity raises ALS2CL's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 3.70× lower at baseline in the lines without CALB1 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588 |
| [[KRT6A]] | C | CALB1 activity raises KRT6A's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 4.30× lower at baseline in the lines without CALB1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588; co-absent with the target |
| [[LINC02582]] | C | CALB1 activity raises LINC02582's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 8.75× lower at baseline in the lines without CALB1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588; co-absent with the target |
| [[GRIN2B]] | C | CALB1 activity raises GRIN2B's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 7.92× lower at baseline in the lines without CALB1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588; co-absent with the target |
| [[TPRXL]] | C | CALB1 activity raises TPRXL's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 3.75× lower at baseline in the lines without CALB1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588; co-absent with the target |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.886). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.9, 50.4); signed map (65.5, 8.0). **Vector** length 37.9, 21.7% of its response variance represented; |z| ≥ 3 in 130 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.9 | +1.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +0.9 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | +0.2 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | -0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.7 | -1.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -0.6 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.6 | -2.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.6 | -1.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | calbindin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.3 — chr8:90,058,608-90,095,475 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CALB |
| Gene groups (HGNC) | EF-hand domain containing |
| Reactome | 1 pathways, smallest: Amyloid fiber formation |
| Matched by | ensembl_id |

**Function**, from UniProt [P05937](https://www.uniprot.org/uniprotkb/P05937) (Calbindin):

> Buffers cytosolic calcium. May stimulate a membrane Ca(2+)-ATPase and a 3',5'-cyclic nucleotide phosphodiesterase.

**Summary**, from NCBI Gene [793](https://www.ncbi.nlm.nih.gov/gene/793):

> The protein encoded by this gene is a member of the calcium-binding protein superfamily that includes calmodulin and troponin C. Originally described as a 27 kDa protein, it is now known to be a 28 kDa protein. It contains four active calcium-binding domains, and has two modified domains that are thought to have lost their calcium binding capability. This protein is thought to buffer entry of calcium upon stimulation of glutamate receptors. Depletion of this protein was noted in patients with …

**Accessions** — [HGNC:1434](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1434) · Entrez [793](https://www.ncbi.nlm.nih.gov/gene/793) · UniProt [P05937](https://www.uniprot.org/uniprotkb/P05937) · Ensembl [ENSG00000104327](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104327)

## Data

Gene col 2442: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2442); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2442, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2442]; `tensor/DDL_lfc|DDL_z.npy` [2442]; `embed/gene_vectors.npy` [2442]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2442 or target_col == 2442). Every well: [[CALB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CALB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
