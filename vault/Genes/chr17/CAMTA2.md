---
symbol: "CAMTA2"
type: "gene"
col: 2956
ensembl_id: "ENSG00000108509"
name: "calmodulin binding transcription activator 2"
location: "17p13.2"
module: 63
arm: "+"
pooled_cpm: 15.63
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 18
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# CAMTA2

*calmodulin binding transcription activator 2* — 17p13.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 5.93×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (13 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.424× (z -12.1, q 5e-31, down in 36 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.684× (z -5.3, q 1e-05, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHKBP1]] (+0.59, fdr 2e-05), [[AARS1]] (+0.56, fdr 1e-05), [[PYCR1]] (+0.56, fdr 2e-05); moves opposite to [[HMGB1]] (-0.47, fdr 8e-05), [[THSD4-AS1]] (-0.46, fdr 1e-04), [[NIPBL]] (-0.45, fdr 1e-04).
> It is in [[Module 063]], a single-armed module (ISR ATF4).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2956.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 5.93×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.26× | +3.2 | 0.68 | 16/47 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2956.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.424×** | -12.1 | 5e-31 | 36/46 (LOX-IMVI, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.524×** | -9.1 | 3e-17 | 33/48 (SW480, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.593×** | -7.4 | 3e-11 | 26/47 (SW 900, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.629×** | -6.5 | 1e-08 | 29/47 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.684×** | -5.3 | 1e-05 | 25/47 (RPMI-7951, HCT15, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.741×** | -4.2 | 0.002 | 20/47 (NCI-H460, KATO III, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.748×** | -3.9 | 0.007 | 16/47 (NCI-H1792, COLO 205, …) | rises with dose | composition shift; position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **0.750×** | -3.9 | 0.007 | 16/47 (NCI-H1792, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.760×** | -3.9 | 0.007 | 14/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.744×** | -3.8 | 0.007 | 16/34 (A-172, PANC-1, …) | inconsistent across doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | **0.765×** | -3.6 | 0.015 | 18/44 (NCI-H460, NCI-H1792, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.775×** | -3.6 | 0.016 | 18/47 (NCI-H661, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.777×** | -3.5 | 0.017 | 16/48 (NCI-H1792, A-172, …) | two highest doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.837× | -3.5 | 0.018 | 21/47 (NCI-H1792, LoVo, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.775×** | -3.4 | 0.027 | 15/48 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.792×** | -3.3 | 0.034 | 21/47 (LS 180, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2956. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 27.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.297× (z -8.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 17.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -9.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 14.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 17.5 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 14.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[SW480 (line)]] | alt | 17.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.235× (z -12.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 22.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[A498 (line)]] | wt | 7.41 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.93× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0568× (z -13.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 14.5 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0586× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 11.1 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0656× (z -11.0) |
| [[KATO III (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 16.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -15.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.294× (z -8.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 16.6 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.175× (z -8.8) |
| [[SNU-423 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.127× (z -10.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.119× (z -11.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW1417 (line)]] | alt | 8.76 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 30.0 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0449× (z -13.7) |
| [[A-427 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2956), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHKBP1]] | +0.59 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[AARS1]] | +0.56 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[PYCR1]] | +0.56 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[MBD6]] | +0.54 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[NEURL4]] | +0.54 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[ATXN2L]] | +0.54 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[RNF187]] | +0.53 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[SHMT2]] | +0.53 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[MAN1B1]] | +0.53 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[INTS11]] | +0.53 | +0.47 / +0.55 | both halves | 2e-05 | same gene group |
| [[XPOT]] | +0.52 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[AAAS]] | +0.52 | +0.53 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGB1]] | -0.47 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[THSD4-AS1]] | -0.46 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[NIPBL]] | -0.45 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[HMGB1P5]] ⚠ | -0.44 | -0.29 / -0.40 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[GSTP1]] | -0.43 | -0.43 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.523). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.6, -23.6); signed map (-15.5, 25.9). **Vector** length 72.5, 12.1% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.2 | +3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.2 | +1.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.6 | +1.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.2 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.1 | -0.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.6 | +1.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +1.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.7 | -6.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.2 | -7.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.0 | -12.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.4 | -9.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | -2.3 | -3.9 |
|  | [[Allantoin (drug)]] 0.5 µM |  | -1.7 | -1.9 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.7 | -2.8 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.6 | -3.9 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.6 | -2.0 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | calmodulin binding transcription activator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:4,967,992-4,987,675 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0909 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; IPT domain containing; Calmodulin binding transcription activators |
| Matched by | ensembl_id |

**Function**, from UniProt [O94983](https://www.uniprot.org/uniprotkb/O94983) (Calmodulin-binding transcription activator 2):

> Transcription activator. May act as tumor suppressor.

**Summary**, from NCBI Gene [23125](https://www.ncbi.nlm.nih.gov/gene/23125):

> The protein encoded by this gene is a member of the calmodulin-binding transcription activator protein family. Members of this family share a common domain structure that consists of a transcription activation domain, a DNA-binding domain, and a calmodulin-binding domain. The encoded protein may be a transcriptional coactivator of genes involved in cardiac growth. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:18807](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18807) · Entrez [23125](https://www.ncbi.nlm.nih.gov/gene/23125) · UniProt [O94983](https://www.uniprot.org/uniprotkb/O94983) · Ensembl [ENSG00000108509](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108509)

## Data

Gene col 2956: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2956); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2956, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2956]; `tensor/DDL_lfc|DDL_z.npy` [2956]; `embed/gene_vectors.npy` [2956]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2956 or target_col == 2956). Every well: [[CAMTA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAMTA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
