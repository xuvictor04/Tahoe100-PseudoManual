---
symbol: "COQ3"
type: "gene"
col: 5316
ensembl_id: "ENSG00000132423"
name: "coenzyme Q3, methyltransferase"
location: "6q16.2"
module: 39
arm: "+"
pooled_cpm: 6.94
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# COQ3

*coenzyme Q3, methyltransferase* — 6q16.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.78× (z +19.2, q 0e+00, up in 37 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[HI-TOPK-032 (drug)]] 0.05 µM: 0.738× (z -3.8, q 0.074, down in 13 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idoxuridine (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0359×); [[Clofarabine (drug)]] 0.05 µM in 1 line (KATO III 0.0512×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (SNU-423 0.0825×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01030]] (+0.66, fdr 1e-05), [[ARL9]] (+0.65, fdr 1e-05), [[BAAT]] (+0.64, fdr 3e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ROPN1L]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5316.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.78×** | +19.2 | 0e+00 | 37/43 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.42×** | +16.6 | 0e+00 | 39/43 (SNU-423, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.52×** | +11.8 | 6e-30 | 32/37 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.76×** | +10.7 | 2e-24 | 28/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +8.6 | 1e-15 | 27/42 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +7.2 | 7e-11 | 10/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +7.0 | 2e-10 | 26/47 (PANC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.72×** | +6.9 | 3e-10 | 20/45 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.66×** | +6.7 | 1e-09 | 22/47 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.45×** | +6.2 | 3e-08 | 21/46 (NCI-H460, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.33×** | +5.9 | 2e-07 | 17/44 (LoVo, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.25×** | +5.6 | 8e-07 | 10/15 (NCI-H460, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.52×** | +5.6 | 9e-07 | 16/47 (HT-29, COLO 205, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.0 | 3e-05 | 13/48 (HOP62, BT-474, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.48×** | +4.9 | 3e-05 | 14/46 (LOX-IMVI, A-172, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.9 | 3e-05 | 16/48 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +4.8 | 4e-05 | 16/44 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +4.2 | 8e-04 | 13/46 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.002 | 14/45 (LoVo, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.005 | 10/47 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.030 | 8/44 (SHP-77, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5316.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idoxuridine (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0359×); [[Clofarabine (drug)]] 0.05 µM in 1 line (KATO III 0.0512×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (SNU-423 0.0825×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.738×** | -3.8 | 0.074 | 13/45 (A-427, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.768× | -3.5 | 0.12 | 10/45 (J82, SW48, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.788× | -3.1 | 0.42 | 9/45 (NCI-H2030, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5316. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 9.49 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.96× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 5.72 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.91× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 4.70 | 0 | 2 | — | [[Simotinib (drug)]] 0.05 µM 0.0576× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 5.99 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.09× (z +18.1) | — |
| [[RPMI-7951 (line)]] | alt | 11.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +11.3) | — |
| [[SNU-423 (line)]] | alt | 8.12 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.98× (z +10.7) | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0825× (z -9.9) |
| [[A498 (line)]] | wt | 3.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 17.4 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0643× (z -8.6) |
| [[C32 (line)]] | wt | 8.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.86× (z +10.0) | — |
| [[HCT15 (line)]] | alt | 8.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.09× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 5.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 6.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.26× (z +9.4) | — |
| [[KATO III (line)]] | alt | 6.56 | 0 | 1 | — | [[Clofarabine (drug)]] 0.05 µM 0.0512× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.82× (z +12.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 7.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 7.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 4.04 | 0 | 1 | — | [[Idoxuridine (drug)]] 0.05 µM 0.0359× (z -15.2) |
| [[PANC-1 (line)]] | alt | 6.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +11.2) | — |
| [[SK-MEL-2 (line)]] | alt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +9.2) | — |
| [[SW480 (line)]] | alt | 5.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +8.9) | — |
| [[A-172 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5316), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01030]] | +0.66 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[ARL9]] | +0.65 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[BAAT]] | +0.64 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[HVCN1]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[C2CD6]] | +0.60 | +0.67 / +0.46 | both halves | 2e-05 |  |
| [[IL34]] | +0.60 | +0.67 / +0.38 | both halves | 7e-05 |  |
| [[FNDC7]] | +0.60 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[MYOCOS]] | +0.59 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[CATSPERD]] | +0.59 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[C21orf91-OT1]] | +0.59 | +0.64 / +0.37 | both halves | 7e-05 |  |
| [[CCDC181]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ZNF610]] | +0.58 | +0.61 / +0.24 | both halves | 5e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ROPN1L]] | C | ROPN1L activity raises COQ3's level | lines that do not express ROPN1L (3) vs lines expressing it (47) | 1.77× lower at baseline in the lines without ROPN1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NBEAP2, FAM229B, SPDL1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.528). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.1, -9.7); signed map (22.4, 10.9). **Vector** length 65.0, 9.79% of its response variance represented; |z| ≥ 3 in 991 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +19.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.1 | +10.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.3 | +11.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +16.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.0 | +8.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.8 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +5.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +5.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -2.4 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.3 | +5.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.0 | +0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | coenzyme Q3, methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q16.2 — chr6:99,369,401-99,394,195 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA9819.1 |
| Gene groups (HGNC) | 7BS small molecule methyltransferases; Small molecule methyltransferases |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 3 pathways, smallest: Ubiquinol biosynthesis; Metabolism of cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZJ6](https://www.uniprot.org/uniprotkb/Q9NZJ6) (Ubiquinone biosynthesis O-methyltransferase, mitochondrial):

> O-methyltransferase required for two non-consecutive steps during ubiquinone biosynthesis (By similarity). Catalyzes the 2 O-methylation of 3,4-dihydroxy-5-(all-trans-decaprenyl)benzoic acid into 4-hydroxy-3-methoxy-5-(all-trans-decaprenyl)benzoic acid (By similarity). Also catalyzes the last step of ubiquinone biosynthesis by mediating methylation of 3-demethylubiquinone into ubiquinone (By similarity). Also able to mediate the methylation of 3-demethylubiquinol-10 into ubiquinol-10 (By …

**Summary**, from NCBI Gene [51805](https://www.ncbi.nlm.nih.gov/gene/51805):

> Ubiquinone, also known as coenzyme Q, or Q, is a critical component of the electron transport pathways of both eukaryotes and prokaryotes (Jonassen and Clarke, 2000 [PubMed 10777520]). This lipid consists of a hydrophobic isoprenoid tail and a quinone head group. The tail varies in length depending on the organism, but its purpose is to anchor coenzyme Q to the membrane. The quinone head group is responsible for the activity of coenzyme Q in the respiratory chain. The S. cerevisiae COQ3 gene …

**Accessions** — [HGNC:18175](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18175) · Entrez [51805](https://www.ncbi.nlm.nih.gov/gene/51805) · UniProt [Q9NZJ6](https://www.uniprot.org/uniprotkb/Q9NZJ6) · Ensembl [ENSG00000132423](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132423)

## Data

Gene col 5316: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5316); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5316, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5316]; `tensor/DDL_lfc|DDL_z.npy` [5316]; `embed/gene_vectors.npy` [5316]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5316 or target_col == 5316). Every well: [[COQ3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COQ3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
