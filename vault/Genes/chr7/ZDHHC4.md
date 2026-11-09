---
symbol: "ZDHHC4"
type: "gene"
col: 5843
ensembl_id: "ENSG00000136247"
name: "zDHHC palmitoyltransferase 4"
location: "7p22.1"
module: 28
arm: "+"
pooled_cpm: 18.42
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# ZDHHC4

*zDHHC palmitoyltransferase 4* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.65× (z +14.3, q 8e-44, up in 39 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.34× (z +6.0, q 2e-07, up in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (PANC-1 2.56×, A-172 4.50×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 2.40×, HEC-1-A 3.69×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.515× (z -9.8, q 7e-20, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TADA3]] (+0.68, fdr 7e-06), [[FAM114A2]] (+0.63, fdr 1e-05), [[TYW5]] (+0.62, fdr 1e-05); moves opposite to [[AGAP3]] (-0.50, fdr 4e-05), [[TXN]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CCNYL2-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5843.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (PANC-1 2.56×, A-172 4.50×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 2.40×, HEC-1-A 3.69×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.65×** | +14.3 | 8e-44 | 39/41 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +10.5 | 4e-23 | 28/32 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +8.4 | 7e-15 | 26/36 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +6.0 | 2e-07 | 25/48 (SW480, SNU-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.7 | 3e-04 | 1/48 (HepG2/C3A) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.40×** | +3.5 | 0.041 | 15/44 (A-427, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.36× | +3.2 | 0.10 | 11/48 (A498, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~8% of this change | 1.24× | +3.1 | 0.13 | 15/44 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[LY-2584702 (tosylate salt) (drug)]] 0.5 µM |  | 1.34× | +3.1 | 0.13 | 4/48 (MIA PaCa-2, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5843.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.515×** | -9.8 | 7e-20 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.523×** | -9.6 | 3e-19 | 34/46 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.528×** | -9.4 | 9e-19 | 37/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.617×** | -7.1 | 1e-10 | 31/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.779×** | -5.2 | 2e-05 | 21/46 (AN3 CA, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.720×** | -4.8 | 1e-04 | 27/47 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.722×** | -4.8 | 1e-04 | 22/47 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.729×** | -4.7 | 2e-04 | 22/47 (SK-MEL-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.747×** | -4.3 | 1e-03 | 20/47 (KATO III, J82, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.756×** | -4.1 | 0.002 | 19/48 (A-427, J82, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.751×** | -4.0 | 0.003 | 17/48 (SK-MEL-2, A498, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.764×** | -4.0 | 0.003 | 18/48 (J82, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.757×** | -3.9 | 0.004 | 16/47 (SW 1271, SW48, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.775×** | -3.8 | 0.007 | 18/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.583×** | -3.7 | 0.008 | 15/40 (SNU-423, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.609×** | -3.4 | 0.023 | 12/48 (A-427, SNU-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | 0.855× | -3.3 | 0.033 | 12/48 (A-172, A549, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5843. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 43.9 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.56× (z +10.3) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.408× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.411× (z -10.2) |
| [[SW480 (line)]] | alt | 21.6 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.333× (z -10.7) |
| [[A-172 (line)]] | wt | 15.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.50× (z +9.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 25.5 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0859× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 14.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +8.8) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0843× (z -17.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5843), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TADA3]] | +0.68 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[FAM114A2]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[TYW5]] | +0.62 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[MDM4]] | +0.61 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[TMEM42]] | +0.61 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[POLI]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[LAMTOR1]] | +0.60 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[CZIB]] | +0.60 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[ASNSD1]] | +0.60 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[ZSCAN21]] | +0.59 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[SUPT20H]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[STK16]] | +0.59 | +0.63 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGAP3]] | -0.50 | -0.54 / -0.40 | both halves | 4e-05 |  |
| [[TXN]] | -0.50 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCNYL2-1]] | B | CCNYL2-1 activity raises ZDHHC4's level | lines that do not express CCNYL2-1 (29) vs lines expressing it (21) | 1.20× lower at baseline in the lines without CCNYL2-1 | 0.072 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.611). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-28.3, 4.9); signed map (5.7, -23.9). **Vector** length 63.7, 10.8% of its response variance represented; |z| ≥ 3 in 761 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.6 | +6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | -2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +14.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +0.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.5 | +0.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +1.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.3 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.6 | -9.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -9.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.2 | -7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | -9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -4.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.4 | -2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | zDHHC palmitoyltransferase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:6,577,434-6,589,374 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10479, ZNF374 |
| Gene groups (HGNC) | Zinc fingers DHHC-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPG8](https://www.uniprot.org/uniprotkb/Q9NPG8) (Palmitoyltransferase ZDHHC4):

> Palmitoyltransferase that catalyzes the addition of palmitate onto protein substrates including the D(2) dopamine receptor DRD2, GSK3B or MAVS. Mediates GSK3B palmitoylation to prevent its AKT1-mediated phosphorylation leading to activation of the STAT3 signaling pathway. Also catalyzes MAVS palmitoylation which promotes its stabilization and activation by inhibiting 'Lys-48'- but facilitating 'Lys-63'-linked ubiquitination.

**Summary**, from NCBI Gene [55146](https://www.ncbi.nlm.nih.gov/gene/55146):

> Enables palmitoyltransferase activity. Involved in positive regulation of innate immune response and protein localization to plasma membrane. Located in Golgi apparatus and endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18471](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18471) · Entrez [55146](https://www.ncbi.nlm.nih.gov/gene/55146) · UniProt [Q9NPG8](https://www.uniprot.org/uniprotkb/Q9NPG8) · Ensembl [ENSG00000136247](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136247)

## Data

Gene col 5843: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5843); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5843, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5843]; `tensor/DDL_lfc|DDL_z.npy` [5843]; `embed/gene_vectors.npy` [5843]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5843 or target_col == 5843). Every well: [[ZDHHC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZDHHC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
