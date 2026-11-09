---
symbol: "RFC4"
type: "gene"
col: 8809
ensembl_id: "ENSG00000163918"
name: "replication factor C subunit 4"
location: "3q27.3"
module: 6
arm: "+"
pooled_cpm: 20.07
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 22
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# RFC4

*replication factor C subunit 4* — 3q27.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.83× (z +9.9, q 3e-20, up in 35 of 48 measured lines) ⚠ cell-cycle shift, explains ~73% of this change. The strongest without an alert is [[Raltitrexed (drug)]] 0.5 µM: 1.21× (z +3.1, q 0.068, up in 9 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.521× (z -15.1, q 0e+00, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DSCC1]] (+0.91, fdr 7e-06), [[BLM]] (+0.88, fdr 7e-06), [[EXO1]] (+0.88, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TP73]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 17 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8809.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.83×** | +9.9 | 3e-20 | 35/48 (LoVo, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.79×** | +9.5 | 6e-19 | 32/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.60×** | +7.7 | 3e-12 | 28/47 (LoVo, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.45×** | +6.1 | 1e-07 | 21/41 (NCI-H1792, CFPAC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | 1.19× | +4.0 | 0.006 | 14/48 (SW480, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~93% of this change | **1.29×** | +4.0 | 0.007 | 17/43 (SW480, SW 900, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.26×** | +3.8 | 0.010 | 13/43 (AsPC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | 1.18× | +3.8 | 0.010 | 15/48 (A-427, SW48, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.26×** | +3.7 | 0.012 | 7/48 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.27×** | +3.7 | 0.012 | 9/27 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.26×** | +3.7 | 0.012 | 9/47 (A-427, SW480, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | 1.17× | +3.7 | 0.012 | 11/48 (LoVo, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.27×** | +3.6 | 0.016 | 12/38 (HS-578T, A549, …) | all doses, flat | composition shift; position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.24×** | +3.5 | 0.017 | 11/47 (A-427, SW480, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.1 | 0.063 | 4/32 (MIA PaCa-2, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.068 | 9/46 (Hs 766T, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8809.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.521×** | -15.1 | 0e+00 | 38/47 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.635×** | -7.5 | 3e-11 | 24/47 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.664×** | -6.5 | 2e-08 | 26/46 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.825×** | -4.5 | 0.001 | 24/48 (A-427, H4, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.766×** | -4.4 | 0.001 | 18/47 (H4, LS 180, …) | all doses, flat |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.710×** | -4.0 | 0.006 | 16/48 (SW480, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.715×** | -3.9 | 0.007 | 15/48 (Hs 766T, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.789×** | -3.9 | 0.007 | 16/47 (HEC-1-A, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.785×** | -3.8 | 0.007 | 15/45 (A-427, HOP62, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.849× | -3.8 | 0.007 | 12/48 (HCT15, hTERT-HPNE, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.849× | -3.8 | 0.007 | 8/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.785×** | -3.8 | 0.008 | 16/48 (NCI-H460, HCT15, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.800×** | -3.7 | 0.010 | 8/48 (MIA PaCa-2, J82, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.797×** | -3.6 | 0.013 | 11/47 (A-427, H4, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.785×** | -3.5 | 0.016 | 12/48 (A-427, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.801×** | -3.4 | 0.020 | 11/47 (SW48, A-172, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.654×** | -3.3 | 0.029 | 9/47 (A-427, KATO III, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.818×** | -3.3 | 0.029 | 15/47 (SW480, HOP62, …) | rises with dose | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.819×** | -3.3 | 0.029 | 13/45 (hTERT-HPNE, HT-29, …) | all doses, stronger at high dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.869× | -3.3 | 0.029 | 10/48 (BT-474, HS-578T, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.870× | -3.3 | 0.030 | 11/48 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.662×** | -3.2 | 0.032 | 7/48 (H4, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.78 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8809. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 26.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -22.2) |
| [[HEC-1-A (line)]] | alt | 37.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -12.9) |
| [[A-172 (line)]] | wt | 17.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -13.4) |
| [[A-427 (line)]] | wt | 59.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0648× (z -24.0) |
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 19.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -12.9) |
| [[PANC-1 (line)]] | alt | 29.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -12.1) |
| [[HepG2_C3A (line)]] | wt | 7.42 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0924× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -9.4) |
| [[HS-578T (line)]] | alt | 17.7 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.231× (z -10.1) |
| [[KATO III (line)]] | alt | 28.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -11.2) |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 11.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 18.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -12.7) |
| [[SW48 (line)]] | wt | 26.7 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.138× (z -9.8) |
| [[SW480 (line)]] | alt | 38.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -12.6) |
| [[A549 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8809), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DSCC1]] | +0.91 | +0.87 / +0.89 | both halves | 7e-06 | pathway: Chromosome Maintenance; STRING 998 |
| [[BLM]] | +0.88 | +0.86 / +0.87 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 871 |
| [[EXO1]] | +0.88 | +0.84 / +0.88 | both halves | 7e-06 | pathway: Affinity selection of immunoglobulins; STRING 955 |
| [[RAD51]] | +0.87 | +0.85 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_DNA_REPAIR; STRING 888 |
| [[WDHD1]] | +0.87 | +0.80 / +0.89 | both halves | 7e-06 | STRING 738 |
| [[FANCI]] | +0.86 | +0.87 / +0.83 | both halves | 7e-06 | STRING 560 |
| [[CENPK]] | +0.85 | +0.84 / +0.84 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 561 |
| [[RAD54L]] | +0.85 | +0.83 / +0.87 | both halves | 7e-06 | STRING 538 |
| [[FANCB]] | +0.85 | +0.80 / +0.82 | both halves | 7e-06 |  |
| [[DDX12P]] | +0.84 | +0.85 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[DTL]] | +0.84 | +0.81 / +0.86 | both halves | 7e-06 | pathway: DNA Damage Bypass; STRING 763 |
| [[MMS22L]] | +0.84 | +0.79 / +0.85 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP73]] | B | TP73 activity raises RFC4's level | lines that do not express TP73 (14) vs lines expressing it (36) | 1.45× lower at baseline in the lines without TP73 | 0.062 | ⚠ within organs, on part of the lines; also absent: SPTB, PRR36, EMID1; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises RFC4's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.99× lower at baseline in the lines without CDC25A | 0.071 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises RFC4's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DSCC1]] | C | DSCC1 activity raises RFC4's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.12× lower at baseline in the lines without DSCC1 | 0.041 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.878). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.3, -45.8); signed map (-38.1, -42.7). **Vector** length 110, 26.7% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.64 to 65); *E2F G1/S* (control, mean cos +0.67 to 23); *Activation of the pre-replicative complex* (reactome, mean cos +0.71 to 22).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | +4.2 | +7.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +4.1 | +9.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | +4.0 | +9.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +1.9 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +3.0 | +3.5 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +2.0 | +2.2 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +2.0 | +3.1 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.0 | -15.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.4 | -7.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -6.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | -3.9 | -3.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | -3.8 | -4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.5 | -3.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.5 | -1.7 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | replication factor C subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.3 — chr3:186,789,880-186,807,058 (-) |
| Ensembl biotype | protein_coding |
| Also known as | A1, RFC37 |
| Gene groups (HGNC) | AAA ATPases; Replication factor C |
| Hallmark sets | SPERMATOGENESIS, DNA_REPAIR, UV_RESPONSE_UP, MYC_TARGETS_V1 |
| Reactome | 59 pathways, smallest: Leading Strand Synthesis; Polymerase switching; Translesion synthesis by REV1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P35249](https://www.uniprot.org/uniprotkb/P35249) (Replication factor C subunit 4):

> Subunit of the replication factor C (RFC) complex which acts during elongation of primed DNA templates by DNA polymerases delta and epsilon, and is necessary for ATP-dependent loading of proliferating cell nuclear antigen (PCNA) onto primed DNA. The RFC4 subunit probably functions as a scaffold on which the other complex components can assemble.

**Summary**, from NCBI Gene [5984](https://www.ncbi.nlm.nih.gov/gene/5984):

> The elongation of primed DNA templates by DNA polymerase delta and DNA polymerase epsilon requires the accessory proteins proliferating cell nuclear antigen (PCNA) and replication factor C (RFC). RFC, also named activator 1, is a protein complex consisting of five distinct subunits of 140, 40, 38, 37, and 36 kD. This gene encodes the 37 kD subunit. This subunit forms a core complex with the 36 and 40 kDa subunits. The core complex possesses DNA-dependent ATPase activity, which was found to be …

**Accessions** — [HGNC:9972](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9972) · Entrez [5984](https://www.ncbi.nlm.nih.gov/gene/5984) · UniProt [P35249](https://www.uniprot.org/uniprotkb/P35249) · Ensembl [ENSG00000163918](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163918)

## Data

Gene col 8809: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8809); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8809, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8809]; `tensor/DDL_lfc|DDL_z.npy` [8809]; `embed/gene_vectors.npy` [8809]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8809 or target_col == 8809). Every well: [[RFC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
