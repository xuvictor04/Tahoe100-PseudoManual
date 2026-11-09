---
symbol: "DEGS1"
type: "gene"
col: 6796
ensembl_id: "ENSG00000143753"
name: "delta 4-desaturase, sphingolipid 1"
location: "1q42.11"
module: 65
arm: "-"
pooled_cpm: 29.02
n_lines_expressing: 48
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# DEGS1

*delta 4-desaturase, sphingolipid 1* — 1q42.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.51× (z +6.3, q 2e-07, up in 31 of 46 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 1.50× (z +6.2, q 2e-07, up in 32 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.718× (z -4.9, q 6e-04, down in 22 of 45 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKNOX1]] (+0.55, fdr 1e-05), [[CCDC71L]] (+0.55, fdr 2e-05), [[ZNF281]] (+0.51, fdr 2e-05); moves opposite to [[MINDY3]] (-0.53, fdr 3e-05), [[VTI1B]] (-0.52, fdr 4e-05), [[LONP2]] (-0.50, fdr 4e-05).
> It sits in the **-** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HEG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6796.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.51×** | +6.3 | 2e-07 | 31/46 (SW480, AsPC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +6.2 | 2e-07 | 32/45 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +6.0 | 4e-07 | 24/46 (MIA PaCa-2, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +5.9 | 6e-07 | 24/46 (MIA PaCa-2, KATO III, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +5.6 | 2e-06 | 22/46 (Panc 03.27, HOP62, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +5.6 | 2e-06 | 24/43 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +5.5 | 3e-06 | 21/44 (NCI-H2347, HCT15, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.42×** | +5.4 | 5e-06 | 26/44 (SW480, AsPC-1, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +4.6 | 2e-04 | 17/46 (SNU-423, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.35×** | +4.4 | 6e-04 | 12/30 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.33×** | +4.3 | 9e-04 | 24/46 (SW480, AsPC-1, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 0.001 | 19/46 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.32×** | +4.1 | 0.002 | 18/45 (NCI-H460, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **1.30×** | +4.1 | 0.002 | 17/40 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.002 | 17/46 (MIA PaCa-2, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6796.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.718×** | -4.9 | 6e-04 | 22/45 (NCI-H23, SNU-423, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.550×** | -4.6 | 1e-03 | 22/44 (SK-MEL-2, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.634×** | -3.5 | 0.064 | 12/44 (A-172, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.795×** | -3.5 | 0.064 | 18/46 (A498, HS-578T, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.669× | -3.1 | 0.21 | 14/46 (NCI-H460, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6796. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 133 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -19.9) ⚠ cell-cycle shift, explains ~95% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -14.9) |
| [[MIA PaCa-2 (line)]] | alt | 22.0 | 2 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 7.53× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[A-172 (line)]] | wt | 74.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -13.7) ⚠ cell-cycle shift, explains ~95% of this change |
| [[NCI-H23 (line)]] | alt | 32.8 | 0 | 3 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -16.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SW480 (line)]] | alt | 13.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +8.8) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 5 µM 0.229× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[KATO III (line)]] | alt | 7.93 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.30× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0981× (z -15.1) ⚠ cell-cycle shift, explains ~68% of this change |
| [[LoVo (line)]] | wt | 13.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.166× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[NCI-H460 (line)]] | wt | 32.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[RKO (line)]] | wt | 28.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -10.1) ⚠ cell-cycle shift, explains ~93% of this change |
| [[A-427 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.73 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.70 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6796), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKNOX1]] | +0.55 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[CCDC71L]] | +0.55 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[ZNF281]] | +0.51 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[ZNF672]] | +0.49 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[TSC22D1]] | +0.49 | +0.45 / +0.39 | both halves | 5e-05 |  |
| [[ARSB]] | +0.48 | +0.56 / +0.32 | both halves | 2e-04 | pathway: Sphingolipid metabolism |
| [[SIK3]] | +0.48 | +0.45 / +0.35 | both halves | 1e-04 |  |
| [[IL6]] | +0.47 | +0.44 / +0.41 | both halves | 4e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[PREX2]] | +0.47 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[OSMR]] | +0.47 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[ZCCHC2]] | +0.46 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[CXCL10]] | +0.46 | +0.34 / +0.46 | both halves | 1e-04 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MINDY3]] | -0.53 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[VTI1B]] | -0.52 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[LONP2]] | -0.50 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[FIG4]] | -0.49 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[BLTP1]] | -0.48 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[FRG1BP]] | -0.48 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[MTMR10]] | -0.48 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[VAMP7]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[SLC25A14]] | -0.46 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[RBL2]] | -0.46 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[WDR11]] | -0.46 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[AQR]] | -0.45 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HEG1]] | B | HEG1 activity raises DEGS1's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 1.98× lower at baseline in the lines without HEG1 | 0.047 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **-** arm (projection on the module's main direction -0.397). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (34.1, 8.0); signed map (10.7, 24.3). **Vector** length 83.4, 16.6% of its response variance represented; |z| ≥ 3 in 845 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.1 | +6.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.6 | +4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.6 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +5.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +1.0 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.1 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -4.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.5 | -2.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.0 | -1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -4.9 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | delta 4-desaturase, sphingolipid 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.11 — chr1:224,175,756-224,193,441 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MLD, Des-1, DES1, FADS7, DEGS-1 |
| Gene groups (HGNC) | Fatty acid desaturases |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 5 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [O15121](https://www.uniprot.org/uniprotkb/O15121) (Sphingolipid delta(4)-desaturase DES1):

> Has sphingolipid-delta-4-desaturase activity. Converts D-erythro-sphinganine to D-erythro-sphingosine (E-sphing-4-enine). Catalyzes the equilibrium isomerization of retinols (By similarity).

**Summary**, from NCBI Gene [8560](https://www.ncbi.nlm.nih.gov/gene/8560):

> This gene encodes a member of the membrane fatty acid desaturase family which is responsible for inserting double bonds into specific positions in fatty acids. This protein contains three His-containing consensus motifs that are characteristic of a group of membrane fatty acid desaturases. It is predicted to be a multiple membrane-spanning protein localized to the endoplasmic reticulum. Overexpression of this gene inhibited biosynthesis of the EGF receptor, suggesting a possible role of a fatty …

**Accessions** — [HGNC:13709](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13709) · Entrez [8560](https://www.ncbi.nlm.nih.gov/gene/8560) · UniProt [O15121](https://www.uniprot.org/uniprotkb/O15121) · Ensembl [ENSG00000143753](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143753)

## Data

Gene col 6796: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6796); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6796, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6796]; `tensor/DDL_lfc|DDL_z.npy` [6796]; `embed/gene_vectors.npy` [6796]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6796 or target_col == 6796). Every well: [[DEGS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DEGS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
