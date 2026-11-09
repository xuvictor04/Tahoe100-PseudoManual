---
symbol: "SLC24A1"
type: "gene"
col: 1085
ensembl_id: "ENSG00000074621"
name: "solute carrier family 24 member 1"
location: "15q22.31"
module: 51
arm: "+"
pooled_cpm: 14.92
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 40
n_dd_up_clean: 1
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# SLC24A1

*solute carrier family 24 member 1* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.31× (z +5.1, q 2e-04, up in 21 of 48 measured lines) ⚠ cell-cycle shift, explains ~60% of this change. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 1.39× (z +4.4, q 0.003, up in 19 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (15 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.309× (z -15.5, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CARF]] (+0.64, fdr 1e-05), [[LINC00174]] (+0.62, fdr 1e-05), [[C22orf46]] (+0.61, fdr 1e-05); moves opposite to [[TMEM184B]] (-0.55, fdr 2e-05), [[SLC6A6]] (-0.55, fdr 8e-05), [[TMEM65]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1085.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.31×** | +5.1 | 2e-04 | 21/48 (AsPC-1, RKO, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.39×** | +4.4 | 0.003 | 19/47 (CFPAC-1, KATO III, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.34×** | +3.9 | 0.018 | 15/37 (J82, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +3.7 | 0.033 | 12/28 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.27× | +3.2 | 0.16 | 9/47 (A549, A-172, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.27× | +3.0 | 0.21 | 12/46 (SW480, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1085.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.309×** | -15.5 | 0e+00 | 41/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.321×** | -15.0 | 0e+00 | 40/46 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.327×** | -14.8 | 0e+00 | 43/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.387×** | -12.5 | 8e-34 | 39/47 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.461×** | -10.2 | 2e-22 | 35/47 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.527×** | -8.0 | 1e-13 | 29/41 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.556×** | -7.7 | 9e-13 | 31/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.559×** | -7.7 | 1e-12 | 28/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.571×** | -7.4 | 1e-11 | 28/46 (PANC-1, H4, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.583×** | -7.1 | 7e-11 | 32/47 (PANC-1, LoVo, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.609×** | -6.5 | 3e-09 | 27/47 (NCI-H460, A-427, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.720×** | -6.1 | 6e-08 | 26/47 (PANC-1, A549, …) | two highest doses | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.636×** | -5.6 | 8e-07 | 25/47 (PANC-1, NCI-H2030, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.662×** | -5.4 | 2e-06 | 25/47 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.679×** | -5.1 | 1e-05 | 25/47 (NCI-H23, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.685×** | -5.0 | 2e-05 | 21/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.708×** | -4.5 | 2e-04 | 20/45 (HT-29, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -4.5 | 2e-04 | 16/46 (NCI-H23, HOP62, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.801×** | -4.1 | 0.001 | 19/48 (CFPAC-1, SNU-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.654×** | -4.0 | 0.002 | 11/48 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.568×** | -3.9 | 0.002 | 17/47 (PANC-1, SHP-77, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1085. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 28.2 | 0 | 13 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0980× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.134× (z -17.5) |
| [[A-427 (line)]] | wt | 17.4 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0689× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.113× (z -14.2) |
| [[NCI-H23 (line)]] | alt | 23.5 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0885× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.0928× (z -15.4) |
| [[NCI-H1573 (line)]] | alt | 32.4 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.224× (z -12.4) |
| [[SW480 (line)]] | alt | 18.3 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.172× (z -14.9) |
| [[COLO 205 (line)]] | alt | 32.9 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0639× (z -18.0) |
| [[LoVo (line)]] | wt | 20.5 | 0 | 4 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.228× (z -10.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.265× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 20.6 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.236× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 18.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.115× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.265× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 12.5 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0713× (z -13.4) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 18.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.221× (z -9.6) |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0523× (z -15.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 12.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -9.1) ⚠ cell-cycle shift, explains ~66% of this change |
| [[C-33 A (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.109× (z -10.4) ⚠ transcription drop |
| [[H4 (line)]] | wt | 14.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0868× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 11.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 13.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0790× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 13.1 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0775× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 12.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0795× (z -12.7) |
| [[RKO (line)]] | wt | 11.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.109× (z -10.3) |
| [[SNU-1 (line)]] | wt | 13.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0561× (z -10.8) |
| [[SNU-423 (line)]] | alt | 10.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.119× (z -9.5) |
| [[A-172 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1085), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARF]] | +0.64 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[LINC00174]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[C22orf46]] | +0.61 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[SENP6]] | +0.60 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[TCTN1]] | +0.60 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[ZNF252P]] | +0.59 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[YJU2]] | +0.59 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[EHHADH]] | +0.59 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[ZNF839]] | +0.58 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[FNBP1P1]] | +0.58 | +0.64 / +0.39 | both halves | 5e-05 |  |
| [[PIGV]] | +0.58 | +0.67 / +0.32 | both halves | 2e-04 |  |
| [[GTF3C6]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM184B]] | -0.55 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[SLC6A6]] | -0.55 | -0.59 / -0.37 | both halves | 8e-05 | pathway: SLC-mediated transmembrane transport |
| [[TMEM65]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[CBL]] | -0.52 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[SLC17A5]] | -0.51 | -0.50 / -0.36 | both halves | 9e-05 | pathway: Disorders of transmembrane transporters |
| [[KIAA1958]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[EXTL3]] | -0.50 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[ZCCHC24]] | -0.50 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[NGLY1]] | -0.50 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ENTPD4]] | -0.50 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[TBC1D20]] | -0.49 | -0.47 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.603). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-27.5, 14.1); signed map (12.1, -23.9). **Vector** length 56.8, 9.21% of its response variance represented; |z| ≥ 3 in 1,132 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +4.4 | +5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +3.8 | -6.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.7 | -4.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +2.4 | -5.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.6 | +2.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.3 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +0.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -3.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.0 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.9 | -12.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -14.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.8 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -5.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 24 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:65,611,366-65,660,995 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NCKX1, NCKX, RODX, KIAA0702, HsT17412, CSNB1D |
| Gene groups (HGNC) | Solute carrier family 24 |
| Reactome | 10 pathways, smallest: Activation of the phototransduction cascade; Sodium/Calcium exchangers; The phototransduction cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [O60721](https://www.uniprot.org/uniprotkb/O60721) (Sodium/potassium/calcium exchanger 1):

> Calcium, potassium:sodium antiporter that transports 1 Ca(2+) and 1 K(+) in exchange for 4 Na(+). Is involved in calcium homeostasis in retinal rod photoreceptors and plays a central role in light adaptation. In darkness, it mediates calcium efflux to balance the calcium influx driven by cyclic nucleotide-gated (CNG) channels. Upon illumination, when CNG channels close, it continues to extrude calcium, leading to a rapid decrease in its cytosolic levels. This reduction is essential for the …

**Summary**, from NCBI Gene [9187](https://www.ncbi.nlm.nih.gov/gene/9187):

> This gene encodes a member of the potassium-dependent sodium/calcium exchanger protein family. The encoded protein plays an important role in sodium/calcium exchange in retinal rod and cone photoreceptors by mediating the extrusion of one calcium ion and one potassium ion in exchange for four sodium ions. Mutations in this gene may play a role in congenital stationary night blindness. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. …

**Accessions** — [HGNC:10975](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10975) · Entrez [9187](https://www.ncbi.nlm.nih.gov/gene/9187) · UniProt [O60721](https://www.uniprot.org/uniprotkb/O60721) · Ensembl [ENSG00000074621](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074621)

## Data

Gene col 1085: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1085); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1085, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1085]; `tensor/DDL_lfc|DDL_z.npy` [1085]; `embed/gene_vectors.npy` [1085]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1085 or target_col == 1085). Every well: [[SLC24A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC24A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
