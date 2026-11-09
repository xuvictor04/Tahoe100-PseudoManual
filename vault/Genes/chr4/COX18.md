---
symbol: "COX18"
type: "gene"
col: 8735
ensembl_id: "ENSG00000163626"
name: "cytochrome c oxidase assembly factor COX18"
location: "4q13.3"
module: 148
arm: "+"
pooled_cpm: 9.43
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# COX18

*cytochrome c oxidase assembly factor COX18* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.26× (z +18.6, q 0e+00, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.545× (z -9.8, q 5e-20, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ICE2]] (+0.70, fdr 1e-05), [[INTS2]] (+0.69, fdr 1e-05), [[MAGOHB]] (+0.69, fdr 2e-05); moves opposite to [[SNN]] (-0.68, fdr 8e-05), [[GNB2]] (-0.63, fdr 2e-05), [[STRN]] (-0.61, fdr 5e-04).
> It sits in the **+** arm of [[Module 148]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8735.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.26×** | +18.6 | 0e+00 | 42/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.36×** | +13.9 | 2e-41 | 27/37 (LS 180, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.28×** | +12.8 | 3e-35 | 13/17 (NCI-H460, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +11.3 | 3e-27 | 32/44 (Hs 766T, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.00×** | +10.8 | 4e-25 | 34/46 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.93×** | +10.7 | 1e-24 | 29/44 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +10.3 | 9e-23 | 16/23 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +7.4 | 1e-11 | 24/48 (NCI-H2347, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +7.0 | 2e-10 | 21/46 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.48×** | +6.1 | 8e-08 | 20/46 (HS-578T, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.46×** | +5.9 | 2e-07 | 16/46 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +5.9 | 2e-07 | 16/47 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +4.8 | 6e-05 | 14/38 (NCI-H1792, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.33×** | +4.6 | 2e-04 | 14/47 (A498, NCI-H23, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.34×** | +4.5 | 2e-04 | 12/40 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +4.4 | 3e-04 | 16/46 (NCI-H23, J82, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 9e-04 | 11/43 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.017 | 8/43 (LoVo, hTERT-HPNE, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.025 | 7/46 (LoVo, LOX-IMVI, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 1.14× | +3.0 | 0.072 | 5/48 (RKO, SHP-77, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.20× | +2.9 | 0.080 | 2/48 (LoVo, HEC-1-A) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8735.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.545×** | -9.8 | 5e-20 | 26/46 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.634×** | -7.4 | 4e-11 | 22/46 (C-33 A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.676×** | -6.4 | 4e-08 | 22/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.688×** | -6.1 | 2e-07 | 21/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.789×** | -3.8 | 0.014 | 8/48 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.850× | -3.8 | 0.016 | 8/48 (A-172, SW480, …) | top dose only |  |
| [[Cyclosporin A (drug)]] 5 µM |  | 0.821× | -3.2 | 0.10 | 7/47 (NCI-H2030, HS-578T, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.826× | -3.1 | 0.13 | 10/46 (NCI-H2030, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Afatinib (drug)]] 5 µM |  | 0.828× | -3.1 | 0.14 | 5/48 (AN3 CA, NCI-H23, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8735. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.4 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +13.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 14.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +12.2) | — |
| [[LS 180 (line)]] | wt | 14.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.74× (z +8.7) | — |
| [[A-427 (line)]] | wt | 15.9 | 0 | 2 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.102× (z -11.0) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.252× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 13.4 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 5.19× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 8.71 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.50× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Digitoxin (drug)]] 5 µM 0.209× (z -9.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0933× (z -11.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 9.67 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.101× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 10.4 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0668× (z -10.4) |
| [[Hs 766T (line)]] | wt | 9.01 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.139× (z -9.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 6.52 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0729× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 7.73 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.27× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[PANC-1 (line)]] | alt | 7.21 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.89× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[RPMI-7951 (line)]] | alt | 8.91 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0984× (z -9.1) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 12.9 | 0 | 1 | — | [[Bentamapimod (drug)]] 0.05 µM 0.169× (z -8.6) |
| [[SNU-1 (line)]] | wt | 8.39 | 0 | 1 (1 ⚠) | — | [[Trifluridine (drug)]] 0.5 µM 0.0761× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 6.99 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0921× (z -9.1) |
| [[A-172 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8735), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ICE2]] | +0.70 | +0.78 / +0.54 | both halves | 1e-05 |  |
| [[INTS2]] | +0.69 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[MAGOHB]] | +0.69 | +0.72 / +0.47 | both halves | 2e-05 |  |
| [[MCTS1]] | +0.69 | +0.74 / +0.44 | both halves | 3e-05 |  |
| [[CYREN]] | +0.68 | +0.81 / +0.45 | both halves | 3e-05 |  |
| [[MRPL30]] | +0.68 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[TASOR]] | +0.68 | +0.74 / +0.48 | both halves | 2e-05 |  |
| [[NEK9]] | +0.65 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[SNAPC5]] | +0.63 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[TIMMDC1]] | +0.62 | +0.77 / +0.28 | both halves | 3e-04 | same gene group; pathway: Aerobic respiration and respiratory electron transport |
| [[USP7]] | +0.62 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[DARS1]] | +0.62 | +0.65 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNN]] | -0.68 | -0.67 / -0.37 | both halves | 8e-05 |  |
| [[GNB2]] | -0.63 | -0.66 / -0.46 | both halves | 2e-05 |  |
| [[STRN]] | -0.61 | -0.75 / -0.24 | both halves | 5e-04 |  |
| [[COX6A1]] | -0.61 | -0.57 / -0.42 | both halves | 4e-05 | pathway: Aerobic respiration and respiratory electron transport; STRING 435 |
| [[NENF]] | -0.60 | -0.71 / -0.40 | both halves | 5e-05 |  |
| [[RPLP2]] | -0.60 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[CYTH3]] | -0.60 | -0.67 / -0.34 | both halves | 1e-04 |  |
| [[RNF149]] | -0.60 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[RPS21]] | -0.60 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[RPLP1]] | -0.59 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[FAM118A]] | -0.59 | -0.70 / -0.22 | both halves | 6e-04 |  |
| [[LMTK2]] | -0.58 | -0.56 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **+** arm (projection on the module's main direction 0.735). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-6.0, 1.8); signed map (15.3, -27.7). **Vector** length 70.7, 11.5% of its response variance represented; |z| ≥ 3 in 991 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.9 | +18.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +10.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.2 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +5.0 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +4.9 | +13.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +5.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +2.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.1 | -9.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.8 | -6.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.6 | -7.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.4 | -6.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -3.1 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -1.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +1.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase assembly factor COX18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:73,052,362-73,069,755 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38991, OXA1L2 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Complex IV assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N8Q8](https://www.uniprot.org/uniprotkb/Q8N8Q8) (Cytochrome c oxidase assembly protein COX18, mitochondrial):

> Mitochondrial membrane insertase required for the translocation of the C-terminus of cytochrome c oxidase subunit II (MT-CO2/COX2) across the mitochondrial inner membrane. Plays a role in MT-CO2/COX2 maturation following the COX20-mediated stabilization of newly synthesized MT-CO2/COX2 protein and before the action of the metallochaperones SCO1/2. Essential for the assembly and stability of the mitochondrial respiratory chain complex IV (also known as cytochrome c oxidase).

**Summary**, from NCBI Gene [285521](https://www.ncbi.nlm.nih.gov/gene/285521):

> This gene encodes a cytochrome c oxidase assembly protein. The encoded protein is essential for integral membrane protein insertion into the mitochondrial inner membrane. It is also required for cytochrome c oxidase assembly and activity. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:26801](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26801) · Entrez [285521](https://www.ncbi.nlm.nih.gov/gene/285521) · UniProt [Q8N8Q8](https://www.uniprot.org/uniprotkb/Q8N8Q8) · Ensembl [ENSG00000163626](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163626)

## Data

Gene col 8735: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8735); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8735, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8735]; `tensor/DDL_lfc|DDL_z.npy` [8735]; `embed/gene_vectors.npy` [8735]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8735 or target_col == 8735). Every well: [[COX18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COX18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
