---
symbol: "RORC"
type: "gene"
col: 6722
ensembl_id: "ENSG00000143365"
name: "RAR related orphan receptor C"
location: "1q21.3"
module: 8
arm: "+"
pooled_cpm: 2.45
n_lines_expressing: 20
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 64
direction_downstream: 92
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# RORC

*RAR related orphan receptor C* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.36× (z +10.2, q 2e-21, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.75× (z +5.0, q 8e-05, up in 1 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.471× (z -4.5, q 0.003, down in 10 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (COLO 205 0.0440×, NCI-H2347 0.118×, CFPAC-1 0.0449×, HT-29 0.0682×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LS 180 0.0846×, COLO 205 0.0482×, NCI-H2347 0.174×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (LS 180 0.0607×, COLO 205 0.0318×; ⚠ cell-cycle shift, explains ~69% of this change); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (COLO 205 0.0597×, LS 180 0.133×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01814]] (+0.78, fdr 7e-06), [[LINC00299]] (+0.76, fdr 7e-06), [[ERBB3]] (+0.76, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 64 arrows point to it, the strongest [[TNFRSF14-AS1]] → it (grade B ⚠); 92 go from it, the strongest it → [[BDH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6722.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.36×** | +10.2 | 2e-21 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.17×** | +7.3 | 1e-10 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.38×** | +7.1 | 2e-10 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +5.0 | 8e-05 | 1/12 (NCI-H1573) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.13×** | +4.8 | 2e-04 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.85×** | +4.7 | 2e-04 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.33×** | +3.8 | 0.012 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.8 | 0.012 | 0/8 | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.77×** | +3.6 | 0.019 | 7/16 (KATO III, LS 180, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.58×** | +3.5 | 0.022 | 5/15 (BT-474, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +3.5 | 0.027 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.69×** | +3.3 | 0.042 | 0/8 | inconsistent across doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.44×** | +3.2 | 0.063 | 9/15 (BT-474, SW480, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.64×** | +3.1 | 0.074 | 3/12 (MIA PaCa-2, SW480, …) | two highest doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +3.0 | 0.092 | 1/12 (SHP-77) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.61×** | +3.0 | 0.097 | 1/13 (NCI-H2347) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6722.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (COLO 205 0.0440×, NCI-H2347 0.118×, CFPAC-1 0.0449×, HT-29 0.0682×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LS 180 0.0846×, COLO 205 0.0482×, NCI-H2347 0.174×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (LS 180 0.0607×, COLO 205 0.0318×; ⚠ cell-cycle shift, explains ~69% of this change); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (COLO 205 0.0597×, LS 180 0.133×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.471×** | -4.5 | 0.003 | 10/14 (COLO 205, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.553×** | -3.7 | 0.056 | 12/14 (LS 180, COLO 205, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.585× | -3.4 | 0.12 | 9/15 (HT-29, LS 180, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.587× | -3.3 | 0.12 | 9/15 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.597× | -3.2 | 0.12 | 14/16 (COLO 205, LS 180, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | 0.598× | -3.2 | 0.12 | 6/16 (SHP-77, COLO 205, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.612× | -3.1 | 0.16 | 8/16 (CFPAC-1, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.47 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6722. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 25.8 | 0 | 11 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0846× (z -17.0) |
| [[COLO 205 (line)]] | alt | 28.6 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0440× (z -17.2) |
| [[NCI-H2347 (line)]] | alt | 15.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -12.6) |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0717× (z -9.4) ⚠ cell-cycle shift, explains ~69% of this change |
| [[CFPAC-1 (line)]] | alt | 3.10 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0449× (z -11.6) |
| [[HT-29 (line)]] | alt | 3.17 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0682× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 5.51 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0283× (z -9.4) ⚠ cell-cycle shift, explains ~69% of this change |
| [[SHP-77 (line)]] | alt | 7.63 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0681× (z -8.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 2.05 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0599× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.383 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.257 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.326 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.319 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.283 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.375 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.637 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.849 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.245 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.300 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.219 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.988 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.261 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.280 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.732 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.840 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.295 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.254 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.277 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.227 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.256 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.820 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.263 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.201 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.621 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.355 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6722), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01814]] | +0.78 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[LINC00299]] | +0.76 | +0.70 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[ERBB3]] | +0.76 | +0.72 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[FAAH2]] | +0.73 | +0.67 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[HNF1A-AS1]] | +0.73 | +0.70 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[RNF183]] | +0.73 | +0.71 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[TMC4]] | +0.71 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[TOX3]] | +0.69 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[SLC44A4]] | +0.69 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[TJP3]] | +0.68 | +0.57 / +0.72 | both halves | 1e-05 |  |
| [[LINC02253]] | +0.68 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[ADCY4]] | +0.68 | +0.60 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*64 arrows, 64 of them with an alert ⚠; grade A 0, B 6, C 58. Shown: the 12 strongest; 52 more arrows (52 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF14-AS1]] | B | TNFRSF14-AS1 activity raises RORC's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 1.65× lower at baseline in the lines without TNFRSF14-AS1 | 0.049 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB |
| [[FGD3]] | B | FGD3 activity raises RORC's level | lines that do not express FGD3 (19) vs lines expressing it (31) | 2.04× lower at baseline in the lines without FGD3 | 0.071 | ⚠ within organs, on part of the lines; also absent: CGN, SPINT1-AS1, SPINT1; maybe low, not absent |
| [[TCEA3]] | B | TCEA3 activity raises RORC's level | lines that do not express TCEA3 (14) vs lines expressing it (36) | 1.79× lower at baseline in the lines without TCEA3 | 0.078 | ⚠ within organs, on part of the lines; also absent: ZNF43, ENSG00000267383, ZNF681; maybe low, not absent |
| [[SPATA6L]] | B | SPATA6L activity raises RORC's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 1.96× lower at baseline in the lines without SPATA6L | 0.088 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[PRR36]] | B | PRR36 activity raises RORC's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 1.94× lower at baseline in the lines without PRR36 | 0.093 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[NSUN7]] | B | NSUN7 activity raises RORC's level | lines that do not express NSUN7 (22) vs lines expressing it (28) | 1.75× lower at baseline in the lines without NSUN7 | 0.099 | ⚠ within organs, on part of the lines; also absent: NEBL, KIF1A, FRMPD3; maybe low, not absent |
| [[AGR3]] | C | AGR3 activity raises RORC's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 4.85× lower at baseline in the lines without AGR3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[MUC5B]] | C | MUC5B activity raises RORC's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 3.18× lower at baseline in the lines without MUC5B | 0.001 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; co-absent with the target |
| [[LINC03040]] | C | LINC03040 activity raises RORC's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 2.77× lower at baseline in the lines without LINC03040 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2; co-absent with the target |
| [[TFF3]] | C | TFF3 activity raises RORC's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 3.89× lower at baseline in the lines without TFF3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |
| [[ST6GALNAC1]] | C | ST6GALNAC1 activity raises RORC's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 2.98× lower at baseline in the lines without ST6GALNAC1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4; co-absent with the target |
| [[FUT3]] | C | FUT3 activity raises RORC's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 2.30× lower at baseline in the lines without FUT3 | 0.005 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004; co-absent with the target |

### Downstream of this gene

*92 arrows, 92 of them with an alert ⚠; grade A 0, B 32, C 60. Shown: the 12 strongest; 80 more arrows (80 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BDH1]] | B | RORC activity raises BDH1's level | lines that do not express RORC (30) vs lines expressing it (20) | 2.84× lower at baseline in the lines without RORC | 0.001 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[IL17RE]] | B | RORC activity raises IL17RE's level | lines that do not express RORC (30) vs lines expressing it (20) | 2.83× lower at baseline in the lines without RORC | 0.002 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[PRRG2]] | B | RORC activity raises PRRG2's level | lines that do not express RORC (30) vs lines expressing it (20) | 2.35× lower at baseline in the lines without RORC | 0.002 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[AP1G2]] | B | RORC activity raises AP1G2's level | lines that do not express RORC (30) vs lines expressing it (20) | 2.25× lower at baseline in the lines without RORC | 0.003 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[SYTL1]] | B | RORC activity raises SYTL1's level | lines that do not express RORC (30) vs lines expressing it (20) | 2.52× lower at baseline in the lines without RORC | 0.005 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[RINL]] | B | RORC activity weakens RINL's drug response | lines that do not express RORC (27) vs lines expressing it (17) | the lines without RORC respond 3.17× as strongly (z diff -1.72); strongest at Idarubicin (hydrochloride) 5 µM: 3.10x vs 0.70x (z diff -6.4) | 0.005 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2; target measured in part of the lines; artifact flags |
| [[BNC2]] | B | RORC activity lowers BNC2's level | lines that do not express RORC (30) vs lines expressing it (20) | 5.00× higher at baseline in the lines without RORC | 0.006 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[OCLN]] | B | RORC activity raises OCLN's level | lines that do not express RORC (30) vs lines expressing it (20) | 3.51× lower at baseline in the lines without RORC | 0.007 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[DCLK2]] | B | RORC activity lowers DCLK2's level | lines that do not express RORC (30) vs lines expressing it (20) | 3.15× higher at baseline in the lines without RORC | 0.008 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[RINL]] | B | RORC activity raises RINL's level | lines that do not express RORC (30) vs lines expressing it (20) | 1.86× lower at baseline in the lines without RORC | 0.009 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[FGD3]] | B | RORC activity raises FGD3's level | lines that do not express RORC (30) vs lines expressing it (20) | 2.06× lower at baseline in the lines without RORC | 0.011 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[SLC44A3]] | B | RORC activity raises SLC44A3's level | lines that do not express RORC (30) vs lines expressing it (20) | 2.33× lower at baseline in the lines without RORC | 0.012 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.690). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.0, 49.0); signed map (58.2, 5.0). **Vector** length 55.5, 18.5% of its response variance represented; |z| ≥ 3 in 480 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +3.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +1.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +3.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -1.4 | -3.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -2.3 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | RAR related orphan receptor C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,806,071-151,831,845 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RZRG, RORG, NR1F3, TOR |
| Gene groups (HGNC) | RAR related orphan receptors |
| Reactome | 10 pathways, smallest: RUNX3 Regulates Immune Response and Cell Migration; Phosphorylated BMAL1:CLOCK (ARNTL:CLOCK) activates expression of core clock genes; RORA,B,C and NR1D1 (REV-ERBA) regulate gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [P51449](https://www.uniprot.org/uniprotkb/P51449) (Nuclear receptor ROR-gamma):

> Nuclear receptor that binds DNA as a monomer to ROR response elements (RORE) containing a single core motif half-site 5'-AGGTCA-3' preceded by a short A-T-rich sequence. Key regulator of cellular differentiation, immunity, peripheral circadian rhythm as well as lipid, steroid, xenobiotics and glucose metabolism. Considered to have intrinsic transcriptional activity, have some natural ligands like oxysterols that act as agonists (25-hydroxycholesterol) or inverse agonists (7-oxygenated sterols), …

**Summary**, from NCBI Gene [6097](https://www.ncbi.nlm.nih.gov/gene/6097):

> The protein encoded by this gene is a DNA-binding transcription factor and is a member of the NR1 subfamily of nuclear hormone receptors. The specific functions of this protein are not known; however, studies of a similar gene in mice have shown that this gene may be essential for lymphoid organogenesis and may play an important regulatory role in thymopoiesis. In addition, studies in mice suggest that the protein encoded by this gene may inhibit the expression of Fas ligand and IL2. Two …

**Accessions** — [HGNC:10260](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10260) · Entrez [6097](https://www.ncbi.nlm.nih.gov/gene/6097) · UniProt [P51449](https://www.uniprot.org/uniprotkb/P51449) · Ensembl [ENSG00000143365](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143365)

## Data

Gene col 6722: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6722); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6722, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6722]; `tensor/DDL_lfc|DDL_z.npy` [6722]; `embed/gene_vectors.npy` [6722]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6722 or target_col == 6722). Every well: [[RORC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RORC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
