---
symbol: "SNX18"
type: "gene"
col: 10986
ensembl_id: "ENSG00000178996"
name: "sorting nexin 18"
location: "5q11.2"
module: 17
arm: "+"
pooled_cpm: 14.75
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 8
n_dd_up_clean: 16
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# SNX18

*sorting nexin 18* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.05× (z +12.5, q 7e-33, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.500× (z -11.9, q 4e-30, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EHMT2]] (+0.60, fdr 1e-05), [[COG2]] (+0.59, fdr 2e-05), [[RBM18]] (+0.58, fdr 1e-05); moves opposite to [[CCNT2-AS1]] (-0.52, fdr 5e-04), [[NPHP3-ACAD11]] (-0.52, fdr 5e-05), [[PDK1-AS1]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GPD1L]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10986.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.05×** | +12.5 | 7e-33 | 38/47 (J82, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.96×** | +11.6 | 9e-29 | 34/47 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.86×** | +10.7 | 1e-24 | 34/47 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +9.1 | 1e-17 | 28/47 (A498, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +8.4 | 4e-15 | 27/47 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +7.2 | 7e-11 | 25/46 (J82, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.84×** | +5.5 | 3e-06 | 17/47 (C32, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.81×** | +5.4 | 6e-06 | 13/47 (A498, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +4.9 | 7e-05 | 15/45 (HCT15, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +4.9 | 7e-05 | 17/46 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +4.6 | 2e-04 | 13/47 (J82, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.003 | 14/47 (C32, NCI-H2030, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +3.7 | 0.009 | 15/41 (RPMI-7951, SW1417, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.021 | 6/47 (SK-MEL-2, HT-29, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.023 | 11/47 (SNU-423, HS-578T, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.027 | 8/42 (SW480, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10986.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.500×** | -11.9 | 4e-30 | 29/47 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.589×** | -9.1 | 2e-17 | 28/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.680×** | -6.6 | 6e-09 | 22/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.711×** | -5.9 | 6e-07 | 22/46 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.733×** | -5.4 | 1e-05 | 20/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.744×** | -4.9 | 9e-05 | 18/47 (SW 900, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.798×** | -3.9 | 0.008 | 12/47 (NCI-H2347, KATO III, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.819×** | -3.3 | 0.065 | 20/44 (Panc 03.27, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.834× | -3.1 | 0.11 | 8/47 (NCI-H460, SW 1271, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10986. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 62.6 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.471× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 10.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -12.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.204× (z -11.8) |
| [[HepG2_C3A (line)]] | wt | 7.42 | 0 | 2 (1 ⚠) | — | [[Carbamazepine (drug)]] 0.05 µM 0.0567× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 23.3 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -12.1) |
| [[PANC-1 (line)]] | alt | 11.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.252× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.309× (z -8.8) |
| [[A498 (line)]] | wt | 24.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 7.12 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.129× (z -8.6) |
| [[BT-474 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.162× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.205× (z -8.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 14.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.68× (z +8.5) | — |
| [[LoVo (line)]] | wt | 18.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 21.9 | 0 | 1 | — | [[PF-06260933 (drug)]] 5 µM 0.0478× (z -8.8) |
| [[SNU-1 (line)]] | wt | 14.6 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.124× (z -8.7) |
| [[SW1417 (line)]] | alt | 12.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -11.2) |
| [[SW480 (line)]] | alt | 8.38 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -10.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10986), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHMT2]] | +0.60 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[COG2]] | +0.59 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[RBM18]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[SCAP]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ZNF30]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[MRPS31P4]] | +0.57 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[HEATR6]] | +0.57 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[SPIN1]] | +0.56 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[FITM2]] | +0.56 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[ABHD10]] | +0.56 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[ZFAND4]] | +0.56 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[POLR3B]] | +0.55 | +0.50 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNT2-AS1]] | -0.52 | -0.39 / -0.24 | both halves | 5e-04 |  |
| [[NPHP3-ACAD11]] | -0.52 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[PDK1-AS1]] | -0.52 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[KIAA0753]] | -0.51 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[ALG13]] | -0.51 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[SLC25A53]] | -0.51 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[IGF2BP3]] | -0.50 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[TEX21P]] | -0.50 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[BBIP1]] | -0.50 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[TBCE-1]] | -0.50 | -0.26 / -0.39 | both halves | 4e-04 |  |
| [[SPRED3]] | -0.49 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[ADGRL1-AS1]] | -0.49 | -0.51 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPD1L]] | C | GPD1L activity raises SNX18's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 1.72× lower at baseline in the lines without GPD1L | 0.099 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.536). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-28.1, -3.4); signed map (-24.3, -15.5). **Vector** length 84.9, 16.2% of its response variance represented; |z| ≥ 3 in 1,016 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +9.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +12.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +3.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.0 | +5.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.0 | +10.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +4.0 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -4.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -3.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.9 | -9.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.8 | -11.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2 — chr5:54,517,759-54,546,586 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SH3PX2, SH3PXD3B; previously SNAG1 |
| Gene groups (HGNC) | Sorting nexins; PX-BAR domain containing; SH3 domain containing |
| Reactome | 3 pathways, smallest: Clathrin-mediated endocytosis; Membrane Trafficking; Vesicle-mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RF0](https://www.uniprot.org/uniprotkb/Q96RF0) (Sorting nexin-18):

> Involved in endocytosis and intracellular vesicle trafficking, both during interphase and at the end of mitosis. Required for efficient progress through mitosis and cytokinesis. Required for normal formation of the cleavage furrow at the end of mitosis. Plays a role in endocytosis via clathrin-coated pits, but also clathrin-independent, actin-dependent fluid-phase endocytosis. Plays a role in macropinocytosis. Binds to membranes enriched in phosphatidylinositol 4,5-bisphosphate and promotes …

**Summary**, from NCBI Gene [112574](https://www.ncbi.nlm.nih.gov/gene/112574):

> This gene encodes a member of the sorting nexin family. Members of this family contain a phox (PX) domain, which is a phosphoinositide binding domain, and are involved in intracellular trafficking. This protein does not contain a coiled coil region, like some family members, but contains a SH3 domain. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19245](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19245) · Entrez [112574](https://www.ncbi.nlm.nih.gov/gene/112574) · UniProt [Q96RF0](https://www.uniprot.org/uniprotkb/Q96RF0) · Ensembl [ENSG00000178996](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178996)

## Data

Gene col 10986: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10986); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10986, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10986]; `tensor/DDL_lfc|DDL_z.npy` [10986]; `embed/gene_vectors.npy` [10986]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10986 or target_col == 10986). Every well: [[SNX18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
