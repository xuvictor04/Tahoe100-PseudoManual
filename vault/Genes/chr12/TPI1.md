---
symbol: "TPI1"
type: "gene"
col: 3256
ensembl_id: "ENSG00000111669"
name: "triosephosphate isomerase 1"
location: "12p13.31"
module: 99
arm: "+"
pooled_cpm: 311.9
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 2
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# TPI1

*triosephosphate isomerase 1* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.29× (z +7.4, q 1e-10, up in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.48× (z +4.9, q 1e-04, up in 37 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (A498 4.26×, SHP-77 3.84×, PANC-1 3.57×, NCI-H1792 4.29×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H1573 2.88×, AsPC-1 2.03×, A549 2.44×); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 4.17×, SHP-77 4.30×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.437× (z -10.4, q 1e-22, down in 44 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (NCI-H23 0.181×, A-427 0.177×, CHP-212 0.139×, BT-474 0.237×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.193×, SNU-1 0.233×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[P4HA2]] (+0.61, fdr 1e-05), [[DIPK2A]] (+0.60, fdr 1e-05), [[ABCB6]] (+0.60, fdr 1e-05); moves opposite to [[TYW5]] (-0.56, fdr 1e-05), [[MDM4]] (-0.56, fdr 5e-05), [[ZSWIM7]] (-0.54, fdr 2e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3256.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (A498 4.26×, SHP-77 3.84×, PANC-1 3.57×, NCI-H1792 4.29×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H1573 2.88×, AsPC-1 2.03×, A549 2.44×); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 4.17×, SHP-77 4.30×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.29×** | +7.4 | 1e-10 | 47/49 (A498, SHP-77, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.05×** | +6.1 | 2e-07 | 37/44 (A498, SHP-77, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.9 | 1e-04 | 37/49 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.64×** | +4.1 | 0.006 | 29/45 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~66% of this change | **1.51×** | +3.7 | 0.027 | 39/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.099 | 31/48 (MIA PaCa-2, NCI-H1573, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.46×** | +3.2 | 0.099 | 35/50 (MIA PaCa-2, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3256.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (NCI-H23 0.181×, A-427 0.177×, CHP-212 0.139×, BT-474 0.237×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.193×, SNU-1 0.233×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.437×** | -10.4 | 1e-22 | 44/48 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.521×** | -5.8 | 2e-06 | 40/48 (A-427, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | 0.675× | -3.4 | 0.12 | 33/48 (BT-474, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Baicalin (drug)]] 5 µM |  | 0.770× | -3.3 | 0.12 | 42/49 (NCI-H23, SNU-1, …) | top dose only |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.495× | -3.3 | 0.12 | 44/49 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3256. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 399 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -10.8) |
| [[SW480 (line)]] | alt | 347 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -12.8) |
| [[A-427 (line)]] | wt | 659 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -20.2) |
| [[A498 (line)]] | wt | 229 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[A549 (line)]] | wt | 251 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 233 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -10.1) |
| [[BT-474 (line)]] | alt | 218 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -16.9) |
| [[C-33 A (line)]] | alt | 274 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -15.5) |
| [[HOP62 (line)]] | alt | 429 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -8.6) |
| [[SHP-77 (line)]] | alt | 110 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[SNU-1 (line)]] | wt | 270 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -12.4) |
| [[A-172 (line)]] | wt | 242 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -12.9) |
| [[AN3 CA (line)]] | alt | 326 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -9.2) |
| [[CHP-212 (line)]] | wt | 248 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -18.0) |
| [[H4 (line)]] | wt | 477 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -10.8) |
| [[HCT15 (line)]] | alt | 415 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -16.5) |
| [[HEC-1-A (line)]] | alt | 408 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 195 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -13.0) |
| [[Hs 766T (line)]] | wt | 207 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -11.5) |
| [[HT-29 (line)]] | alt | 320 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -10.2) |
| [[J82 (line)]] | alt | 359 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -9.8) |
| [[KATO III (line)]] | alt | 242 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 239 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 193 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H23 (line)]] | alt | 849 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -20.4) |
| [[NCI-H2347 (line)]] | alt | 377 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 261 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 467 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -14.7) |
| [[PANC-1 (line)]] | alt | 190 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[RKO (line)]] | wt | 193 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 377 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -10.9) |
| [[C32 (line)]] | wt | 332 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 266 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 297 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 361 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 331 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 341 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 296 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 395 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 271 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 93.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 332 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 410 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 418 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 232 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3256), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P4HA2]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[DIPK2A]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[ABCB6]] | +0.60 | +0.49 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[VDAC1]] | +0.59 | +0.59 / +0.63 | both halves | 7e-06 | STRING 561 |
| [[LDHA]] | +0.57 | +0.64 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 913 |
| [[PKM]] | +0.57 | +0.67 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS; STRING 963 |
| [[PLOD2]] | +0.57 | +0.61 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[BSG]] | +0.57 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[DDX41]] | +0.57 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[LNPK]] | +0.57 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[MLLT3]] | +0.56 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[BNIP3]] | +0.56 | +0.58 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYW5]] | -0.56 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[MDM4]] | -0.56 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[ZSWIM7]] | -0.54 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[ZC3H7B]] | -0.53 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ZNF354A]] | -0.53 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[FBXW8]] | -0.53 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[C5orf63]] | -0.52 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[TXNRD3]] | -0.51 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[GCFC2]] | -0.51 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[ZNHIT6]] | -0.50 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[FBXO4]] | -0.50 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[COA7]] | -0.50 | -0.38 / -0.52 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TPI1's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.9, -19.3); signed map (-40.1, 28.3). **Vector** length 89.2, 41.0% of its response variance represented; |z| ≥ 3 in 643 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.8 | +3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +1.9 |
|  | [[Relugolix (drug)]] 0.5 µM |  | +2.1 | +1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +0.4 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | +1.7 | +0.7 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -7.2 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | -6.9 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -6.9 | +7.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.6 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -5.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.6 | +0.6 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.2 | -0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -1.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | triosephosphate isomerase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,867,119-6,870,948 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | GLYCOLYSIS, HYPOXIA, MTORC1_SIGNALING |
| Reactome | 4 pathways, smallest: Gluconeogenesis; Glycolysis; Glucose metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P60174](https://www.uniprot.org/uniprotkb/P60174) (Triosephosphate isomerase):

> Triosephosphate isomerase is an extremely efficient metabolic enzyme that catalyzes the interconversion between dihydroxyacetone phosphate (DHAP) and D-glyceraldehyde-3-phosphate (G3P) in glycolysis and gluconeogenesis.; It is also responsible for the non-negligible production of methylglyoxal a reactive cytotoxic side-product that modifies and can alter proteins, DNA and lipids.

**Summary**, from NCBI Gene [7167](https://www.ncbi.nlm.nih.gov/gene/7167):

> This gene encodes an enzyme, consisting of two identical proteins, which catalyzes the isomerization of glyceraldehydes 3-phosphate (G3P) and dihydroxy-acetone phosphate (DHAP) in glycolysis and gluconeogenesis. Mutations in this gene are associated with triosephosphate isomerase deficiency. Pseudogenes have been identified on chromosomes 1, 4, 6 and 7. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:12009](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12009) · Entrez [7167](https://www.ncbi.nlm.nih.gov/gene/7167) · UniProt [P60174](https://www.uniprot.org/uniprotkb/P60174) · Ensembl [ENSG00000111669](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111669)

## Data

Gene col 3256: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3256); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3256, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3256]; `tensor/DDL_lfc|DDL_z.npy` [3256]; `embed/gene_vectors.npy` [3256]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3256 or target_col == 3256). Every well: [[TPI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
