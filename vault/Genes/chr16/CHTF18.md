---
symbol: "CHTF18"
type: "gene"
col: 4825
ensembl_id: "ENSG00000127586"
name: "chromosome transmission fidelity factor 18"
location: "16p13.3"
module: 6
arm: "+"
pooled_cpm: 6.48
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CHTF18

*chromosome transmission fidelity factor 18* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 6.56× (z +18.5, q 0e+00, up in 46 of 46 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 1.42× (z +3.4, q 0.027, up in 5 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.590× (z -7.3, q 1e-10, down in 25 of 45 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.778× (z -3.5, q 0.066, down in 10 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 3 lines (A498 0.262×, HT-29 0.166×, A-427 0.228×; ⚠ cell-cycle shift, explains ~39% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (KATO III 0.0773×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RECQL4]] (+0.84, fdr 7e-06), [[RHPN1]] (+0.75, fdr 7e-06), [[CEP131]] (+0.74, fdr 1e-05); moves opposite to [[YARS2]] (-0.58, fdr 9e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 12 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4825.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **6.56×** | +18.5 | 0e+00 | 46/46 (SW480, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **4.40×** | +14.6 | 1e-45 | 45/46 (SW480, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **3.54×** | +12.4 | 3e-33 | 44/46 (SW480, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **3.38×** | +12.0 | 5e-31 | 22/25 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **3.06×** | +10.6 | 4e-24 | 12/13 (HEC-1-A, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.68×** | +8.1 | 6e-14 | 16/20 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.31×** | +4.3 | 0.001 | 4/15 (A-427, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.51×** | +4.0 | 0.004 | 12/31 (NCI-H2347, SW1417, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.48×** | +3.9 | 0.007 | 9/41 (NCI-H460, KATO III, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~65% of this change | **1.46×** | +3.6 | 0.020 | 10/32 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.44×** | +3.5 | 0.027 | 9/38 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.027 | 5/46 (PANC-1, SW1417, …) | rises with dose | position effect removed |
| [[Rimonabant (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.027 | 5/46 (Hs 766T, A498, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.65×** | +3.2 | 0.053 | 8/42 (J82, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~90% of this change | **1.39×** | +3.1 | 0.069 | 11/33 (NCI-H460, A549, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.61×** | +3.1 | 0.076 | 6/43 (PANC-1, LoVo, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.79×** | +3.0 | 0.095 | 2/31 (RKO, NCI-H2347) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4825.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 3 lines (A498 0.262×, HT-29 0.166×, A-427 0.228×; ⚠ cell-cycle shift, explains ~39% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (KATO III 0.0773×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.590×** | -7.3 | 1e-10 | 25/45 (A498, HT-29, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.470×** | -6.0 | 6e-07 | 19/43 (A498, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -3.6 | 0.066 | 14/47 (MIA PaCa-2, HS-578T, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.778×** | -3.5 | 0.066 | 10/47 (HCT15, LS 180, …) | top dose only | position effect removed |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.593×** | -3.3 | 0.092 | 8/47 (SNU-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | 0.721× | -3.0 | 0.23 | 12/42 (LOX-IMVI, H4, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.87 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4825. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.34 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 12.1× (z +13.9) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[KATO III (line)]] | alt | 8.51 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 8.65× (z +9.2) ⚠ cell-cycle shift, explains ~31% of this change | [[Bosentan (hydrate) (drug)]] 5 µM 0.0773× (z -10.4) |
| [[A-427 (line)]] | wt | 10.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.228× (z -9.6) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A498 (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.262× (z -10.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HT-29 (line)]] | alt | 6.89 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.166× (z -10.4) ⚠ cell-cycle shift, explains ~39% of this change |
| [[LoVo (line)]] | wt | 4.09 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 10.8× (z +9.7) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[LOX-IMVI (line)]] | wt | 5.64 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.93× (z +8.7) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H460 (line)]] | wt | 4.29 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.71× (z +9.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[PANC-1 (line)]] | alt | 8.44 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.38× (z +8.7) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[RKO (line)]] | wt | 8.28 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 17.2× (z +10.3) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4825), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RECQL4]] | +0.84 | +0.83 / +0.84 | both halves | 7e-06 | STRING 951 |
| [[RHPN1]] | +0.75 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[CEP131]] | +0.74 | +0.57 / +0.59 | both halves | 1e-05 | STRING 675 |
| [[TELO2]] | +0.73 | +0.65 / +0.64 | both halves | 7e-06 | STRING 572 |
| [[TONSL]] | +0.73 | +0.73 / +0.78 | both halves | 7e-06 |  |
| [[PKMYT1]] | +0.72 | +0.73 / +0.79 | both halves | 7e-06 | STRING 437 |
| [[TRAIP]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 | STRING 421 |
| [[MSH5]] | +0.71 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[NCAPG2]] | +0.70 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[SPC24]] | +0.70 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[FANCA]] | +0.70 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[NCAPH2]] | +0.69 | +0.70 / +0.69 | both halves | 7e-06 | STRING 424 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YARS2]] | -0.58 | -0.43 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises CHTF18's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.94× lower at baseline in the lines without TCF19 | 0.025 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises CHTF18's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.11× lower at baseline in the lines without AURKB | 0.034 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises CHTF18's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.79× lower at baseline in the lines without DSCC1 | 0.054 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[PKMYT1]] | C | PKMYT1 activity raises CHTF18's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 2.33× lower at baseline in the lines without PKMYT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; its own permutation p |
| [[MYBL2]] | C | MYBL2 activity raises CHTF18's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.02× lower at baseline in the lines without MYBL2 | 0.061 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises CHTF18's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 1.75× lower at baseline in the lines without MCM10 | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[E2F1]] | C | E2F1 activity raises CHTF18's level | lines that do not express E2F1 (3) vs lines expressing it (47) | 1.88× lower at baseline in the lines without E2F1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.644). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-27.9, -45.0); signed map (-35.6, -38.8). **Vector** length 77.6, 16.2% of its response variance represented; |z| ≥ 3 in 757 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.50 to 28); *DNA Replication* (reactome, mean cos +0.51 to 40); *E2F G1/S* (control, mean cos +0.51 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.4 | +18.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | +6.3 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | +6.3 | +12.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.5 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +4.8 | +8.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +2.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.3 | +3.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.2 | +3.2 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +2.2 | +2.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.1 | +1.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -5.0 | -7.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.7 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.0 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -1.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | chromosome transmission fidelity factor 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:788,046-800,737 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CHL12, C321D2.4, Ctf18; previously C16orf41 |
| Gene groups (HGNC) | AAA ATPases |
| Reactome | 6 pathways, smallest: Polymerase switching on the C-strand of the telomere; Telomere C-strand (Lagging Strand) Synthesis; Extension of Telomeres |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVB6](https://www.uniprot.org/uniprotkb/Q8WVB6) (Chromosome transmission fidelity protein 18 homolog):

> Chromosome cohesion factor involved in sister chromatid cohesion and fidelity of chromosome transmission. Component of one of the cell nuclear antigen loader complexes, CTF18-replication factor C (CTF18-RFC), which consists of CTF18, CTF8, DCC1, RFC2, RFC3, RFC4 and RFC5. The CTF18-RFC complex binds to single-stranded and primed DNAs and has weak ATPase activity that is stimulated by the presence of primed DNA, replication protein A (RPA) and by proliferating cell nuclear antigen (PCNA). The …

**Summary**, from NCBI Gene [63922](https://www.ncbi.nlm.nih.gov/gene/63922):

> This gene encodes a protein which is a component of a replication factor C (RFC) complex, which loads proliferating cell nuclear antigen (PCNA) on to DNA during the S phase of cell cycle. The encoded protein may interact with other proteins, including RFC complex 3, to form a clamp loader complex that plays a role in sister chromatid cohesion during metaphase-anaphase transition. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:18435](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18435) · Entrez [63922](https://www.ncbi.nlm.nih.gov/gene/63922) · UniProt [Q8WVB6](https://www.uniprot.org/uniprotkb/Q8WVB6) · Ensembl [ENSG00000127586](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127586)

## Data

Gene col 4825: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4825); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4825, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4825]; `tensor/DDL_lfc|DDL_z.npy` [4825]; `embed/gene_vectors.npy` [4825]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4825 or target_col == 4825). Every well: [[CHTF18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHTF18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
