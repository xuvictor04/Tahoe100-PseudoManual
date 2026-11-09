---
symbol: "ORC1"
type: "gene"
col: 1443
ensembl_id: "ENSG00000085840"
name: "origin recognition complex subunit 1"
location: "1p32.3"
module: 6
arm: "+"
pooled_cpm: 11.38
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# ORC1

*origin recognition complex subunit 1* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (21 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.00× (z +9.4, q 3e-18, up in 30 of 46 measured lines) ⚠ cell-cycle shift, explains ~82% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.82× (z +8.0, q 1e-13, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Neratinib (maleate) (drug)]] 0.5 µM: 0.701× (z -4.8, q 4e-04, down in 21 of 44 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 0.749× (z -3.9, q 0.010, down in 19 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXO1]] (+0.87, fdr 7e-06), [[CDC45]] (+0.85, fdr 7e-06), [[DTL]] (+0.85, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 23 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1443.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **2.00×** | +9.4 | 3e-18 | 30/46 (PANC-1, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **2.00×** | +9.3 | 3e-18 | 28/46 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.97×** | +9.1 | 2e-17 | 29/46 (SW480, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.95×** | +9.0 | 4e-17 | 28/46 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.82×** | +8.0 | 1e-13 | 30/46 (SW480, HOP62, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +6.8 | 1e-09 | 11/47 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.54×** | +5.8 | 6e-07 | 22/45 (PANC-1, NCI-H23, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.51×** | +5.5 | 2e-06 | 19/46 (SW480, J82, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.50×** | +5.5 | 3e-06 | 16/45 (PANC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.49×** | +5.4 | 4e-06 | 17/46 (MIA PaCa-2, SW480, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **1.44×** | +5.0 | 4e-05 | 17/44 (PANC-1, J82, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~96% of this change | **1.41×** | +4.5 | 4e-04 | 18/39 (SW480, PANC-1, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.37×** | +4.2 | 0.001 | 13/46 (RKO, HT-29, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.35×** | +4.0 | 0.003 | 12/45 (PANC-1, SW480, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.34×** | +3.9 | 0.004 | 13/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +3.7 | 0.006 | 9/44 (A549, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.016 | 7/43 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.25×** | +2.9 | 0.069 | 4/47 (HEC-1-A, SNU-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1443.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.701×** | -4.8 | 4e-04 | 21/44 (LoVo, A-427, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.702×** | -4.8 | 4e-04 | 21/44 (A498, COLO 205, …) | two highest doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.665×** | -4.0 | 0.010 | 8/47 (SW480, A498, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.749×** | -3.9 | 0.010 | 19/45 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.741×** | -3.9 | 0.010 | 16/44 (SK-MEL-2, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.762×** | -3.7 | 0.020 | 12/44 (NCI-H460, HOP62, …) | two highest doses |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.827×** | -3.7 | 0.020 | 10/47 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.770×** | -3.6 | 0.026 | 17/43 (A498, A-427, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.783×** | -3.3 | 0.053 | 11/45 (A-172, C32, …) | rises with dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.851× | -3.1 | 0.10 | 11/47 (CHP-212, NCI-H460, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.728× | -3.1 | 0.11 | 8/43 (NCI-H460, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.02 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1443. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 20.1 | 0 | 4 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.249× (z -12.5) ⚠ cell-cycle shift, explains ~69% of this change |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0873× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Saquinavir (drug)]] 0.05 µM 0.0994× (z -9.5) |
| [[A549 (line)]] | wt | 6.73 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0743× (z -10.7) |
| [[C32 (line)]] | wt | 8.76 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.112× (z -9.1) |
| [[H4 (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0871× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 9.73 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0931× (z -11.1) |
| [[SW48 (line)]] | wt | 13.4 | 0 | 1 | — | [[Phenytoin (sodium) (drug)]] 0.05 µM 0.0746× (z -8.9) |
| [[A-172 (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1443), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXO1]] | +0.87 | +0.84 / +0.88 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 932 |
| [[CDC45]] | +0.85 | +0.83 / +0.85 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 990 |
| [[DTL]] | +0.85 | +0.81 / +0.84 | both halves | 7e-06 | STRING 856 |
| [[RRM1]] | +0.83 | +0.83 / +0.82 | both halves | 7e-06 | STRING 655 |
| [[WDR76]] | +0.83 | +0.82 / +0.83 | both halves | 7e-06 |  |
| [[RFC5]] | +0.83 | +0.84 / +0.81 | both halves | 7e-06 | same gene group; pathway: Activation of ATR in response to replication stress; STRING 491 |
| [[MMS22L]] | +0.83 | +0.80 / +0.81 | both halves | 7e-06 |  |
| [[POLQ]] | +0.83 | +0.78 / +0.83 | both halves | 7e-06 | STRING 451 |
| [[DSCC1]] | +0.82 | +0.77 / +0.84 | both halves | 7e-06 | STRING 611 |
| [[BLM]] | +0.82 | +0.82 / +0.80 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 524 |
| [[FANCI]] | +0.82 | +0.80 / +0.80 | both halves | 7e-06 |  |
| [[RFC4]] | +0.82 | +0.78 / +0.83 | both halves | 7e-06 | same gene group; pathway: Activation of ATR in response to replication stress; STRING 492 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises ORC1's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.04× lower at baseline in the lines without TCF19 | 0.043 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[PBK]] | C | PBK activity raises ORC1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.04× lower at baseline in the lines without PBK | 0.040 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises ORC1's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.99× lower at baseline in the lines without DSCC1 | 0.047 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[MELK]], [[TK1]] | C | MELK, TK1 activity raises ORC1's level | lines that do not express MELK, TK1 (3) vs lines expressing them (47) | 2.20× lower at baseline in the lines without MELK, TK1 | 0.070 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.854). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.6, -45.5); signed map (-38.0, -43.1). **Vector** length 102, 23.4% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.64 to 65); *DNA strand elongation* (reactome, mean cos +0.70 to 28); *E2F G1/S* (control, mean cos +0.69 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +3.7 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +8.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.7 | +9.1 |
|  | [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +1.3 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.6 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +2.7 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +1.9 | +3.4 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.8 | +2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.6 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -5.5 | -3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -1.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -3.6 | -2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -1.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.8 | -3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | origin recognition complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:52,372,829-52,404,423 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSORC1, PARC1; previously ORC1L |
| Gene groups (HGNC) | AAA ATPases; Origin recognition complex |
| Reactome | 20 pathways, smallest: CDC6 association with the ORC:origin complex; E2F-enabled inhibition of pre-replication complex formation; E2F mediated regulation of DNA replication |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13415](https://www.uniprot.org/uniprotkb/Q13415) (Origin recognition complex subunit 1):

> Component of the origin recognition complex (ORC) that binds origins of replication. DNA-binding is ATP-dependent. The DNA sequences that define origins of replication have not been identified yet. ORC is required to assemble the pre-replication complex necessary to initiate DNA replication.

**Summary**, from NCBI Gene [4998](https://www.ncbi.nlm.nih.gov/gene/4998):

> The origin recognition complex (ORC) is a highly conserved six subunits protein complex essential for the initiation of the DNA replication in eukaryotic cells. Studies in yeast demonstrated that ORC binds specifically to origins of replication and serves as a platform for the assembly of additional initiation factors such as Cdc6 and Mcm proteins. The protein encoded by this gene is the largest subunit of the ORC complex. While other ORC subunits are stable throughout the cell cycle, the …

**Accessions** — [HGNC:8487](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8487) · Entrez [4998](https://www.ncbi.nlm.nih.gov/gene/4998) · UniProt [Q13415](https://www.uniprot.org/uniprotkb/Q13415) · Ensembl [ENSG00000085840](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085840)

## Data

Gene col 1443: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1443); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1443, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1443]; `tensor/DDL_lfc|DDL_z.npy` [1443]; `embed/gene_vectors.npy` [1443]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1443 or target_col == 1443). Every well: [[ORC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ORC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
