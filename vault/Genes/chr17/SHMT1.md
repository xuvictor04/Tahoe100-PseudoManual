---
symbol: "SHMT1"
type: "gene"
col: 10774
ensembl_id: "ENSG00000176974"
name: "serine hydroxymethyltransferase 1"
location: "17p11.2"
module: 6
arm: "+"
pooled_cpm: 13.03
n_lines_expressing: 47
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 10
direction_downstream: 23
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# SHMT1

*serine hydroxymethyltransferase 1* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.60× (z +15.0, q 0e+00, up in 40 of 44 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.41× (z +5.4, q 4e-06, up in 16 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.658× (z -6.3, q 1e-07, down in 21 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCAPD3]] (+0.79, fdr 7e-06), [[RFC5]] (+0.78, fdr 7e-06), [[ORC1]] (+0.78, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); 23 go from it, the strongest it → [[GINS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10774.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.60×** | +15.0 | 0e+00 | 40/44 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.56×** | +14.7 | 0e+00 | 43/44 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.52×** | +14.5 | 3e-45 | 40/44 (PANC-1, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **2.01×** | +10.5 | 1e-23 | 14/22 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **1.63×** | +7.6 | 3e-12 | 22/32 (LS 180, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.51×** | +5.9 | 3e-07 | 16/29 (HEC-1-A, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.45×** | +5.9 | 4e-07 | 17/44 (A549, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.43×** | +5.6 | 2e-06 | 19/42 (A-172, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +5.4 | 4e-06 | 16/44 (HOP62, SNU-423, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.41×** | +5.4 | 5e-06 | 14/44 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.89×** | +5.2 | 8e-06 | 12/44 (A549, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.009 | 12/43 (NCI-H2030, LS 180, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.18× | +3.6 | 0.012 | 13/45 (LS 180, Panc 03.27, …) | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.045 | 9/43 (A498, NCI-H460, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | **1.24×** | +3.2 | 0.047 | 15/36 (SW480, HS-578T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10774.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.658×** | -6.3 | 1e-07 | 21/43 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.723×** | -5.1 | 8e-05 | 19/44 (AN3 CA, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.797×** | -5.1 | 8e-05 | 20/44 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.753×** | -4.5 | 0.001 | 18/40 (MIA PaCa-2, A498, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.791×** | -3.7 | 0.021 | 12/44 (MIA PaCa-2, C32, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.791×** | -3.7 | 0.021 | 14/41 (HepG2/C3A, SK-MEL-2, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.795×** | -3.6 | 0.023 | 15/41 (C32, LS 180, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 0.852× | -3.6 | 0.023 | 14/45 (KATO III, SNU-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.810×** | -3.3 | 0.055 | 18/44 (LOX-IMVI, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.816×** | -3.2 | 0.073 | 12/44 (PANC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.818×** | -3.2 | 0.076 | 10/44 (A498, HEC-1-A, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.683×** | -3.1 | 0.078 | 6/40 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.822×** | -3.1 | 0.084 | 15/44 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.71 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10774. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 26.8 | 4 | 2 (2 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 3.40× (z +8.7) | [[Selinexor (drug)]] 5 µM 0.362× (z -10.3) ⚠ cell-cycle shift, explains ~46% of this change |
| [[MIA PaCa-2 (line)]] | alt | 27.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -15.6) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.273× (z -9.0) |
| [[PANC-1 (line)]] | alt | 6.57 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.83× (z +9.6) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[A-172 (line)]] | wt | 9.89 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -9.7) ⚠ cell-cycle shift, explains ~70% of this change |
| [[C32 (line)]] | wt | 20.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[HCT15 (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.149× (z -9.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[LOX-IMVI (line)]] | wt | 6.75 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.144× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -9.0) ⚠ cell-cycle shift, explains ~70% of this change |
| [[SK-MEL-2 (line)]] | alt | 7.69 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0550× (z -11.3) ⚠ cell-cycle shift, explains ~99% of this change |
| [[SW480 (line)]] | alt | 18.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[A-427 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10774), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCAPD3]] | +0.79 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[RFC5]] | +0.78 | +0.68 / +0.79 | both halves | 7e-06 |  |
| [[ORC1]] | +0.78 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[EXO1]] | +0.77 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[DSCC1]] | +0.76 | +0.66 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[DDX12P]] | +0.76 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[MMS22L]] | +0.75 | +0.66 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[BLM]] | +0.75 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[MSH2]] | +0.75 | +0.60 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[ATAD2]] | +0.75 | +0.71 / +0.71 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS |
| [[CASP2]] | +0.74 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[CENPM]] | +0.74 | +0.68 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 5, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises SHMT1's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.36× lower at baseline in the lines without E2F2 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises SHMT1's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.74× lower at baseline in the lines without TCF19 | 0.018 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises SHMT1's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.63× lower at baseline in the lines without E2F8 | 0.034 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[CDCA7]] | B | CDCA7 activity raises SHMT1's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.33× lower at baseline in the lines without CDCA7 | 0.062 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers SHMT1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DSCC1]] | C | DSCC1 activity raises SHMT1's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.86× lower at baseline in the lines without DSCC1 | 0.021 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises SHMT1's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.82× lower at baseline in the lines without MCM10 | 0.043 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[MCM3]] | C | MCM3 activity raises SHMT1's level | lines that do not express MCM3 (3) vs lines expressing it (47) | 3.18× lower at baseline in the lines without MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target; its own permutation p |
| [[PBK]] | C | PBK activity raises SHMT1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.55× lower at baseline in the lines without PBK | 0.062 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises SHMT1's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 3.08× lower at baseline in the lines without MYBL2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 0, C 23. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GINS1]] | C | SHMT1 activity raises GINS1's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 3.33× lower at baseline in the lines without SHMT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |
| [[FANCA]] | C | SHMT1 activity raises FANCA's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 2.99× lower at baseline in the lines without SHMT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |
| [[SKA3]] | C | SHMT1 activity raises SKA3's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 2.94× lower at baseline in the lines without SHMT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[LRRC20]] | C | SHMT1 activity raises LRRC20's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 2.93× lower at baseline in the lines without SHMT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |
| [[SPC25]] | C | SHMT1 activity raises SPC25's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 2.57× lower at baseline in the lines without SHMT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |
| [[CENPM]] | C | SHMT1 activity raises CENPM's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 2.44× lower at baseline in the lines without SHMT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[SLC25A40]] | C | SHMT1 activity raises SLC25A40's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 1.46× lower at baseline in the lines without SHMT1 | 0.063 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent |
| [[EXO1]] | C | SHMT1 activity raises EXO1's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 3.03× lower at baseline in the lines without SHMT1 | 0.065 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent |
| [[CENPI]] | C | [[SAPCD2]], SHMT1 activity raises CENPI's level | lines that do not express SAPCD2, SHMT1 (3) vs lines expressing them (47) | 2.39× lower at baseline in the lines without SAPCD2, SHMT1 | 0.068 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; co-absent genes |
| [[MCM3]] | C | SHMT1 activity raises MCM3's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 3.69× lower at baseline in the lines without SHMT1 | 0.072 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; co-absent with the target |
| [[MCM2]] | C | SHMT1 activity raises MCM2's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 2.96× lower at baseline in the lines without SHMT1 | 0.086 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; co-absent with the target |
| [[CDC45]] | C | SHMT1 activity raises CDC45's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 2.89× lower at baseline in the lines without SHMT1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.775). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-32.7, -44.8); signed map (-36.7, -42.3). **Vector** length 84.9, 16.8% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.60 to 28); *DNA Replication* (reactome, mean cos +0.60 to 40); *E2F G1/S* (control, mean cos +0.59 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.1 | +15.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.8 | +14.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.7 | +14.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | +2.6 | +10.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +2.3 | +5.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.7 | +2.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +1.7 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +5.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.6 | +0.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -4.7 | -4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | serine hydroxymethyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:18,327,873-18,363,550 (-) |
| Ensembl biotype | protein_coding |
| Also known as | cSHMT, SHMT, MGC15229, MGC24556 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Serine hydroxymethyltransferase family |
| Hallmark sets | E2F_TARGETS |
| Reactome | 5 pathways, smallest: Carnitine synthesis; Metabolism of folate and pterines; Metabolism of water-soluble vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [P34896](https://www.uniprot.org/uniprotkb/P34896) (Serine hydroxymethyltransferase, cytosolic):

> Pyridoxal phosphate (PLP)-dependent enzyme that catalyzes the reversible conversion of serine and tetrahydrofolate (THF) to glycine and 5,10-methylene THF, serving as a critical component of the folate cycle and facilitating one-carbon biosynthetic reactions essential for methionine, purine, and pyrimidine synthesis. While its central activity involves serine cleavage, the detailed catalytic mechanisms remain under study, including both retro-aldol cleavage of the PLP-serine C(alpha)-C(beta) …

**Summary**, from NCBI Gene [6470](https://www.ncbi.nlm.nih.gov/gene/6470):

> This gene encodes the cytosolic form of serine hydroxymethyltransferase, a pyridoxal phosphate-containing enzyme that catalyzes the reversible conversion of serine and tetrahydrofolate to glycine and 5,10-methylene tetrahydrofolate. This reaction provides one-carbon units for synthesis of methionine, thymidylate, and purines in the cytoplasm. This gene is located within the Smith-Magenis syndrome region on chromosome 17. A pseudogene of this gene is located on the short arm of chromosome 1. …

**Accessions** — [HGNC:10850](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10850) · Entrez [6470](https://www.ncbi.nlm.nih.gov/gene/6470) · UniProt [P34896](https://www.uniprot.org/uniprotkb/P34896) · Ensembl [ENSG00000176974](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176974)

## Data

Gene col 10774: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10774); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10774, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10774]; `tensor/DDL_lfc|DDL_z.npy` [10774]; `embed/gene_vectors.npy` [10774]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10774 or target_col == 10774). Every well: [[SHMT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHMT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
