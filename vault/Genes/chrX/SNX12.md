---
symbol: "SNX12"
type: "gene"
col: 7158
ensembl_id: "ENSG00000147164"
name: "sorting nexin 12"
location: "Xq13.1"
module: 51
arm: "+"
pooled_cpm: 19.52
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# SNX12

*sorting nexin 12* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.61× (z +15.5, q 0e+00, up in 34 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.46× (z +6.0, q 2e-07, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.678× (z -8.9, q 2e-16, down in 37 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (SW1417 0.339×, SK-MEL-2 0.377×, SNU-1 0.300×, RPMI-7951 0.387×, …); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HepG2/C3A 0.102×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SNU-1 0.159×; ⚠ toxic; cell-cycle shift, explains ~14% of this change); [[Drospirenone (drug)]] 0.5 µM in 1 line (SW48 0.0884×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHIC1]] (+0.57, fdr 1e-05), [[SREK1]] (+0.54, fdr 3e-05), [[KIDINS220]] (+0.53, fdr 3e-05); moves opposite to [[MRPL18]] (-0.53, fdr 4e-05), [[KHDC1]] (-0.52, fdr 3e-05), [[SENP5]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7158.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.61×** | +15.5 | 0e+00 | 34/41 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.50×** | +14.2 | 2e-43 | 28/30 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +10.1 | 1e-21 | 30/36 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +6.2 | 6e-08 | 26/46 (NCI-H2347, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +6.0 | 2e-07 | 23/47 (NCI-H460, A-172, …) | all doses, flat | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.27×** | +3.8 | 0.011 | 15/48 (NCI-H460, A498, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.42×** | +3.8 | 0.011 | 13/45 (A498, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.24×** | +3.5 | 0.037 | 15/48 (SW480, NCI-H2347, …) | rises with dose | composition shift |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.068 | 13/47 (NCI-H460, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.22×** | +3.2 | 0.068 | 15/44 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.2 | 0.068 | 13/48 (MIA PaCa-2, NCI-H1792, …) | top dose only | low cells (technical?) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.076 | 12/46 (A-172, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.086 | 7/48 (C32, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.49×** | +3.0 | 0.086 | 3/45 (SK-MEL-2, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.086 | 18/47 (NCI-H460, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.0 | 0.094 | 8/47 (AN3 CA, SW480, …) | all doses, flat | low cells (technical?) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.20×** | +3.0 | 0.100 | 12/47 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7158.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (SW1417 0.339×, SK-MEL-2 0.377×, SNU-1 0.300×, RPMI-7951 0.387×, …); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HepG2/C3A 0.102×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SNU-1 0.159×; ⚠ toxic; cell-cycle shift, explains ~14% of this change); [[Drospirenone (drug)]] 0.5 µM in 1 line (SW48 0.0884×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -8.9 | 2e-16 | 37/47 (SW1417, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.719×** | -5.1 | 1e-04 | 21/48 (KATO III, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.796×** | -3.6 | 0.064 | 15/46 (NCI-H23, SW48, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.822× | -3.2 | 0.19 | 9/47 (KATO III, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7158. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 14.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.37× (z +9.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 24.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 36.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 24.2 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.159× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~14% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -9.3) |
| [[SNU-423 (line)]] | alt | 34.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.51× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 16.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.68× (z +11.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 21.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 22.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +11.1) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 15.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 14.8 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.102× (z -10.4) |
| [[Hs 766T (line)]] | wt | 26.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -8.5) |
| [[HS-578T (line)]] | alt | 11.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.03× (z +8.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 14.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -8.5) |
| [[PANC-1 (line)]] | alt | 24.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +10.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 24.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 28.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -9.9) |
| [[SW1417 (line)]] | alt | 22.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -11.1) |
| [[SW48 (line)]] | wt | 11.6 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.0884× (z -9.3) |
| [[A-427 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.32 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 27.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7158), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHIC1]] | +0.57 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[SREK1]] | +0.54 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[KIDINS220]] | +0.53 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[CHURC1]] | +0.53 | +0.40 / +0.60 | both halves | 4e-05 |  |
| [[EFR3A]] | +0.53 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[HS1BP3]] | +0.53 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[SLC4A2]] | +0.53 | +0.38 / +0.62 | both halves | 7e-05 |  |
| [[DNAH14]] | +0.53 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[FAM50A]] | +0.52 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[SDR39U1]] | +0.51 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[TEX261]] | +0.51 | +0.43 / +0.53 | both halves | 3e-05 | STRING 412 |
| [[RRP15]] | +0.51 | +0.40 / +0.57 | both halves | 4e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL18]] | -0.53 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[KHDC1]] | -0.52 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[SENP5]] | -0.52 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[GOLT1B]] | -0.51 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[KLHL25]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[EEF1AKMT4]] | -0.50 | -0.37 / -0.54 | both halves | 9e-05 |  |
| [[ZCCHC17]] | -0.50 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[MED26]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[ABHD17B]] | -0.49 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[CCDC168]] | -0.49 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[CHST7]] | -0.49 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[SNHG30]] | -0.48 | -0.48 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.455). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-17.1, 13.6); signed map (9.8, -36.8). **Vector** length 71.8, 13.2% of its response variance represented; |z| ≥ 3 in 657 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +15.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.0 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +14.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.1 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +10.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -8.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.5 | -2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.4 | -3.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.3 | -5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:71,056,332-71,073,426 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sorting nexins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UMY4](https://www.uniprot.org/uniprotkb/Q9UMY4) (Sorting nexin-12):

> May be involved in several stages of intracellular trafficking.

**Summary**, from NCBI Gene [29934](https://www.ncbi.nlm.nih.gov/gene/29934):

> This gene encodes a member of the sorting nexin family. Members of this family contain a phox (PX) domain, which is a phosphoinositide binding domain, and are involved in intracellular trafficking. This protein does not contain a coiled coil region, like some family members. A similar protein in mouse may be involved in regulating the neurite outgrowth. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:14976](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14976) · Entrez [29934](https://www.ncbi.nlm.nih.gov/gene/29934) · UniProt [Q9UMY4](https://www.uniprot.org/uniprotkb/Q9UMY4) · Ensembl [ENSG00000147164](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147164)

## Data

Gene col 7158: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7158); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7158, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7158]; `tensor/DDL_lfc|DDL_z.npy` [7158]; `embed/gene_vectors.npy` [7158]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7158 or target_col == 7158). Every well: [[SNX12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
