---
symbol: "UGT1A9"
type: "gene"
col: 14258
ensembl_id: "ENSG00000241119"
name: "UDP glucuronosyltransferase family 1 member A9"
location: "2q37.1"
module: 44
arm: "+"
pooled_cpm: 2.59
n_lines_expressing: 17
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 28
direction_downstream: 38
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# UGT1A9

*UDP glucuronosyltransferase family 1 member A9* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.70× (z +8.9, q 2e-16, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.51× (z +7.3, q 4e-11, up in 0 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 9 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (HT-29 0.122×, KATO III 0.207×, COLO 205 0.110×, Hs 766T 0.179×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (KATO III 0.0890×, HT-29 0.137×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (KATO III 0.0430×, HT-29 0.0671×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UGT1A8]] (+0.98, fdr 7e-06, ⚠ same locus), [[UGT1A6]] (+0.92, fdr 7e-06, ⚠ same locus), [[UGT1A1]] (+0.86, fdr 7e-06, ⚠ same locus), [[PRR15]] (+0.77, fdr 7e-06), [[PRR15-DT]] (+0.74, fdr 7e-06), [[PIP5K1B]] (+0.74, fdr 7e-06); moves opposite to [[DNAAF9]] (-0.52, fdr 3e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[UGT1A1]] → it (grade C ⚠); 38 go from it, the strongest it → [[PTPN22]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14258.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.70×** | +8.9 | 2e-16 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.31×** | +7.6 | 7e-12 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.51×** | +7.3 | 4e-11 | 0/13 | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.18×** | +6.5 | 1e-08 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.45×** | +5.0 | 7e-05 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.28×** | +4.6 | 3e-04 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.10×** | +3.8 | 0.012 | 0/9 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.48×** | +3.6 | 0.018 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.42×** | +3.6 | 0.018 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.89×** | +3.6 | 0.020 | 2/12 (LoVo, AsPC-1) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +3.4 | 0.030 | 0/12 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.90×** | +3.3 | 0.040 | 0/11 | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.78×** | +3.2 | 0.048 | 2/13 (LoVo, SW480) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.78×** | +3.2 | 0.048 | 3/13 (LS 180, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Saquinavir (drug)]] 5 µM |  | **1.51×** | +3.2 | 0.048 | 0/13 | all doses, stronger at high dose | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.73×** | +3.1 | 0.072 | 0/9 | inconsistent across doses | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.69×** | +2.9 | 0.098 | 0/11 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14258.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 9 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (HT-29 0.122×, KATO III 0.207×, COLO 205 0.110×, Hs 766T 0.179×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (KATO III 0.0890×, HT-29 0.137×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (KATO III 0.0430×, HT-29 0.0671×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mebendazole (drug)]] 5 µM |  | 0.493× | -3.7 | 0.10 | 7/14 (Hs 766T, AsPC-1, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.539× | -3.6 | 0.10 | 4/13 (AsPC-1, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.594× | -3.0 | 0.44 | 13/14 (KATO III, HT-29, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14258. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 30.6 | 0 | 12 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0890× (z -18.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -12.1) |
| [[HT-29 (line)]] | alt | 27.1 | 0 | 11 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -13.7) |
| [[Hs 766T (line)]] | wt | 18.2 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0836× (z -9.6) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -9.5) |
| [[LoVo (line)]] | wt | 3.20 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0332× (z -11.1) ⚠ cell-cycle shift, explains ~51% of this change |
| [[COLO 205 (line)]] | alt | 8.40 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 5.84 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0499× (z -8.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 0.418 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.163 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.235 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.573 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.221 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.228 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.192 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.294 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.303 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.213 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.225 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.278 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.820 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.249 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.215 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.183 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.175 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.171 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.212 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.279 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.180 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.195 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.186 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.251 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.266 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.290 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.243 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.202 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.261 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.742 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14258), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UGT1A8]] | +0.98 | +0.97 / +0.97 | both halves | 7e-06 | same gene group; pathway: Aspirin ADME; STRING 997; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[UGT1A6]] | +0.92 | +0.92 / +0.89 | both halves | 7e-06 | same gene group; pathway: Aspirin ADME; STRING 998; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[UGT1A1]] | +0.86 | +0.87 / +0.80 | both halves | 7e-06 | same gene group; pathway: Aspirin ADME; STRING 998; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PRR15]] | +0.77 | +0.77 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[PRR15-DT]] | +0.74 | +0.69 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[PIP5K1B]] | +0.74 | +0.70 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[GNA14]] | +0.73 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[TSPAN8]] | +0.73 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[MGAM2]] | +0.72 | +0.63 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[ABO]] | +0.71 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[PRR15L]] | +0.71 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[LGALS4]] | +0.70 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[CFTR]] | +0.69 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[HNF1A-AS1]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[GCNT3]] | +0.68 | +0.71 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF9]] | -0.52 | -0.50 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 0, C 28. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UGT1A1]] | C | UGT1A1 activity raises UGT1A9's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 4.58× lower at baseline in the lines without UGT1A1 | 4e-05 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1; co-absent with the target |
| [[UGT1A6]] | C | UGT1A6 activity raises UGT1A9's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 4.17× lower at baseline in the lines without UGT1A6 | 1e-04 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1; co-absent with the target |
| [[CREB3L1]] | C | CREB3L1 activity raises UGT1A9's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 2.50× lower at baseline in the lines without CREB3L1 | 0.002 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1; co-absent with the target |
| [[LINC01133]] | C | LINC01133 activity raises UGT1A9's level | lines that do not express LINC01133 (34) vs lines expressing it (16) | 2.70× lower at baseline in the lines without LINC01133 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPH, IL33, UGT1A1; co-absent with the target |
| [[IL20RA]] | C | IL20RA activity raises UGT1A9's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 2.66× lower at baseline in the lines without IL20RA | 0.031 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10; co-absent with the target |
| [[PTPRR]] | C | PTPRR activity raises UGT1A9's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 2.30× lower at baseline in the lines without PTPRR | 0.033 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises UGT1A9's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 4.08× lower at baseline in the lines without NPSR1 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[TTC22]] | C | TTC22 activity raises UGT1A9's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 2.48× lower at baseline in the lines without TTC22 | 0.042 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5; co-absent with the target |
| [[TPRXL]] | C | TPRXL activity raises UGT1A9's level | lines that do not express TPRXL (32) vs lines expressing it (18) | 2.55× lower at baseline in the lines without TPRXL | 0.042 | ⚠ within organs, on part of the lines; also absent: LINC01559, LGR6, CAPN8; maybe low, not absent; co-absent with the target |
| [[POU5F1]] | C | POU5F1 activity raises UGT1A9's level | lines that do not express POU5F1 (27) vs lines expressing it (23) | 2.31× lower at baseline in the lines without POU5F1 | 0.043 | ⚠ within organs, on part of the lines; also absent: P2RY2, C4BPB, UGT1A6; co-absent with the target |
| [[APOH]] | C | APOH activity raises UGT1A9's level | lines that do not express APOH (41) vs lines expressing it (9) | 1.73× lower at baseline in the lines without APOH | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITIH2, AFP, APOA2; maybe low, not absent; co-absent with the target |
| [[PTGIS]] | C | PTGIS activity raises UGT1A9's level | lines that do not express PTGIS (39) vs lines expressing it (11) | 1.64× lower at baseline in the lines without PTGIS | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, PREX2, GCG; co-absent with the target |

### Downstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 5, C 33. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPN22]] | B | [[UGT1A8]], UGT1A9 activity raises PTPN22's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 1.87× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.023 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent genes |
| [[ADD3-AS1]] | B | [[UGT1A8]], UGT1A9 activity raises ADD3-AS1's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 1.80× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.064 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent genes |
| [[MECOM]] | B | [[UGT1A8]], UGT1A9 activity raises MECOM's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 2.81× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.070 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent genes |
| [[TNFRSF14]] | B | [[UGT1A8]], UGT1A9 activity raises TNFRSF14's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 1.84× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.085 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent genes |
| [[MECOM]] | B | [[UGT1A8]], UGT1A9 activity weakens MECOM's drug response | lines that do not express UGT1A8, UGT1A9 (19) vs lines expressing them (12) | the lines without UGT1A8, UGT1A9 respond 0.89× as strongly (z diff +0.52); strongest at Panobinostat 0.05 µM: 2.10x vs 1.30x (z diff -3.1) | 0.086 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; target measured in part of the lines; both ways; artifact flags; co-absent genes |
| [[UGT1A6]] | C | [[UGT1A8]], UGT1A9 activity raises UGT1A6's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 8.89× lower at baseline in the lines without UGT1A8, UGT1A9 | 5e-05 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent with the target; co-absent genes |
| [[UGT1A1]] | C | [[UGT1A8]], UGT1A9 activity raises UGT1A1's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 4.02× lower at baseline in the lines without UGT1A8, UGT1A9 | 3e-04 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent with the target; co-absent genes |
| [[IL20RA]] | C | [[UGT1A8]], UGT1A9 activity raises IL20RA's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 3.72× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.004 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent with the target; co-absent genes |
| [[RASSF6]] | C | [[UGT1A8]], UGT1A9 activity raises RASSF6's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 3.71× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.007 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent with the target; co-absent genes |
| [[LINC01559]] | C | [[UGT1A8]], UGT1A9 activity raises LINC01559's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 3.05× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.007 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent with the target; co-absent genes |
| [[GALNT5]] | C | [[UGT1A8]], UGT1A9 activity raises GALNT5's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 4.87× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.007 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent with the target; co-absent genes |
| [[ATP10B]] | C | [[UGT1A8]], UGT1A9 activity raises ATP10B's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 2.89× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.008 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent with the target; co-absent genes |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.768). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.7, 51.4); signed map (63.4, 3.9). **Vector** length 56.7, 20.6% of its response variance represented; |z| ≥ 3 in 421 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.51 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.51 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.51 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +7.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.4 | +0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +6.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.3 | +2.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.3 | +2.7 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -3.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -0.9 | -2.6 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -1.3 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.9 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -0.8 | -0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.8 | -0.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | UDP glucuronosyltransferase family 1 member A9 |
| Locus type | complex locus constituent (other) |
| Location | 2q37.1 — chr2:233,671,898-233,773,300 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HLUGP4, LUGP4, UGT1AI |
| Gene groups (HGNC) | UDP glucuronosyltransferases |
| Reactome | 9 pathways, smallest: Glucuronidation; Aspirin ADME; Paracetamol ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [O60656](https://www.uniprot.org/uniprotkb/O60656) (UDP-glucuronosyltransferase 1A9):

> [Isoform 1]: UDP-glucuronosyltransferase (UGT) that catalyzes phase II biotransformation reactions in which lipophilic substrates are conjugated with glucuronic acid to increase the metabolite's water solubility, thereby facilitating excretion into either the urine or bile. Essential for the elimination and detoxification of drugs, xenobiotics and endogenous compounds. Catalyzes the glucuronidation of endogenous estrogen hormones such as estradiol and estrone. Involved in the glucuronidation of …

**Summary**, from NCBI Gene [54600](https://www.ncbi.nlm.nih.gov/gene/54600):

> This gene encodes a UDP-glucuronosyltransferase, an enzyme of the glucuronidation pathway that transforms small lipophilic molecules, such as steroids, bilirubin, hormones, and drugs, into water-soluble, excretable metabolites. This gene is part of a complex locus that encodes several UDP-glucuronosyltransferases. The locus includes thirteen unique alternate first exons followed by four common exons. Four of the alternate first exons are considered pseudogenes. Each of the remaining nine 5' …

**Accessions** — [HGNC:12541](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12541) · Entrez [54600](https://www.ncbi.nlm.nih.gov/gene/54600) · UniProt [O60656](https://www.uniprot.org/uniprotkb/O60656) · Ensembl [ENSG00000241119](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241119)

## Data

Gene col 14258: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14258); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14258, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14258]; `tensor/DDL_lfc|DDL_z.npy` [14258]; `embed/gene_vectors.npy` [14258]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14258 or target_col == 14258). Every well: [[UGT1A9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UGT1A9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
