---
symbol: "SLC48A1"
type: "gene"
col: 13066
ensembl_id: "ENSG00000211584"
name: "solute carrier family 48 member 1"
location: "12q13.11"
module: 4
arm: "+"
pooled_cpm: 11.2
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# SLC48A1

*solute carrier family 48 member 1* — 12q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.32× (z +11.8, q 2e-29, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.674× (z -7.8, q 3e-12, down in 26 of 42 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.777× (z -5.0, q 2e-04, down in 20 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPKAPK3]] (+0.62, fdr 7e-06), [[SDC3]] (+0.61, fdr 1e-05), [[SH3TC2]] (+0.59, fdr 1e-05); moves opposite to [[MLANA]] (-0.56, fdr 2e-05), [[NDUFC1]] (-0.55, fdr 2e-05), [[ANKHD1]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CACNA1H]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13066.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.32×** | +11.8 | 2e-29 | 38/46 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +11.1 | 3e-26 | 15/20 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.13×** | +10.6 | 5e-24 | 25/32 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.55×** | +6.2 | 9e-08 | 22/47 (A498, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.58×** | +5.9 | 4e-07 | 12/23 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +5.3 | 1e-05 | 20/47 (A498, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.45×** | +5.2 | 2e-05 | 17/47 (LoVo, KATO III, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.40×** | +4.7 | 1e-04 | 18/47 (A498, NCI-H2347, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +4.7 | 1e-04 | 18/45 (HEC-1-A, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +4.3 | 0.001 | 11/43 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +4.2 | 0.001 | 9/47 (PANC-1, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.32×** | +3.9 | 0.004 | 18/47 (NCI-H2347, RPMI-7951, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.006 | 12/47 (HEC-1-A, C32, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.30×** | +3.7 | 0.010 | 12/35 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.6 | 0.013 | 8/48 (A-172, HS-578T, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13066.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.674×** | -7.8 | 3e-12 | 26/42 (NCI-H460, SW480, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.777×** | -5.0 | 2e-04 | 20/44 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.514×** | -4.9 | 2e-04 | 19/45 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.529×** | -4.7 | 4e-04 | 18/41 (Hs 766T, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.723×** | -4.5 | 6e-04 | 17/47 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | 0.642× | -3.3 | 0.11 | 10/46 (A-427, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.805× | -3.1 | 0.16 | 14/48 (C32, SW480, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Trimetrexate (drug)]] 0.05 µM |  | 0.805× | -3.0 | 0.16 | 5/44 (Panc 03.27, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.664× | -3.0 | 0.17 | 8/37 (HT-29, BT-474, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13066. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 24.8 | 0 | 6 (1 ⚠) | — | [[Binimetinib (drug)]] 5 µM 0.104× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 20.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.32× (z +8.8) | — |
| [[SW480 (line)]] | alt | 22.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -10.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -8.5) |
| [[LoVo (line)]] | wt | 15.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0421× (z -24.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 10.0 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0996× (z -9.4) |
| [[HS-578T (line)]] | alt | 6.00 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0700× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 5.22 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.112× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -8.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 4.53 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0879× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 14.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -15.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 9.58 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13066), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK3]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[SDC3]] | +0.61 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[SH3TC2]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[SPTBN2]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[ADAMTSL5]] | +0.58 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[SLC35F6]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[ATP13A2]] | +0.55 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[USB1]] | +0.55 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[PGAM5]] | +0.55 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[ARHGAP4]] | +0.54 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[EPHB6]] | +0.54 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[MYEOV]] | +0.53 | +0.51 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLANA]] | -0.56 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[NDUFC1]] | -0.55 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[ANKHD1]] | -0.55 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[TERF2IP]] | -0.55 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ZMYM5]] | -0.53 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[NDUFA1]] | -0.52 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[SERF2]] | -0.52 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[BBOF1]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[TMEM91]] | -0.51 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[GTF2IRD2B]] | -0.51 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[TRNAU1AP]] | -0.51 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[FLJ46284]] | -0.51 | -0.50 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA1H]] | B | CACNA1H activity raises SLC48A1's level | lines that do not express CACNA1H (23) vs lines expressing it (27) | 1.39× lower at baseline in the lines without CACNA1H | 0.013 | ⚠ within organs, on part of the lines; also absent: LHX2, LMX1B, JPH3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.466). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (7.4, 42.6); signed map (-15.6, 41.7). **Vector** length 75.5, 12.6% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.9 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +3.8 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +4.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.2 | +2.5 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.2 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.6 | -7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -5.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.9 | -4.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -2.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -2.5 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -4.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 48 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.11 — chr12:47,753,916-47,782,751 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20489, hHRG-1, HRG1 |
| Gene groups (HGNC) | Solute carrier family 48 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P1K1](https://www.uniprot.org/uniprotkb/Q6P1K1) (Heme transporter HRG1):

> Heme transporter that regulates intracellular heme availability through the endosomal or lysosomal compartment. In macrophages of the reticuloendothelial system, is the heme transporter for heme-iron recycling. Essential for macrophage iron homeostasis, transports heme from the phagolysosome to the cytoplasm during erythrophagocytosis (EP).

**Summary**, from NCBI Gene [55652](https://www.ncbi.nlm.nih.gov/gene/55652):

> Enables heme binding activity and heme transmembrane transporter activity. Involved in heme transport. Located in endosome membrane; lysosomal membrane; and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26035](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26035) · Entrez [55652](https://www.ncbi.nlm.nih.gov/gene/55652) · UniProt [Q6P1K1](https://www.uniprot.org/uniprotkb/Q6P1K1) · Ensembl [ENSG00000211584](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000211584)

## Data

Gene col 13066: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13066); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13066, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13066]; `tensor/DDL_lfc|DDL_z.npy` [13066]; `embed/gene_vectors.npy` [13066]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13066 or target_col == 13066). Every well: [[SLC48A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC48A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
