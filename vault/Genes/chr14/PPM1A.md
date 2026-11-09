---
symbol: "PPM1A"
type: "gene"
col: 2002
ensembl_id: "ENSG00000100614"
name: "protein phosphatase, Mg2+/Mn2+ dependent 1A"
location: "14q23.1"
module: 29
arm: "+"
pooled_cpm: 75.59
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# PPM1A

*protein phosphatase, Mg2+/Mn2+ dependent 1A* — 14q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.36× (z +5.1, q 1e-04, up in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[PH-797804 (drug)]] 5 µM in 2 lines (C32 7.18×, SW48 7.00×); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 2.12×; ⚠ cell-cycle shift, explains ~74% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 1.83×; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 3.03×).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.707× (z -5.7, q 7e-06, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LDB1]] (+0.62, fdr 1e-05), [[CASTOR3P-1]] (+0.58, fdr 1e-04), [[MSL3]] (+0.56, fdr 1e-05); moves opposite to [[SCFD1]] (-0.58, fdr 1e-05), [[AASDH]] (-0.53, fdr 1e-05), [[ESF1]] (-0.51, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2002.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[PH-797804 (drug)]] 5 µM in 2 lines (C32 7.18×, SW48 7.00×); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 2.12×; ⚠ cell-cycle shift, explains ~74% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 1.83×; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 3.03×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.36×** | +5.1 | 1e-04 | 29/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +5.1 | 1e-04 | 31/48 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.0 | 0.012 | 0/50 | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.24× | +3.3 | 0.13 | 22/48 (J82, HT-29, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 1.21× | +3.1 | 0.21 | 18/48 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2002.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.707×** | -5.7 | 7e-06 | 34/48 (HOP62, SHP-77, …) | top dose only | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.623×** | -4.1 | 0.012 | 27/48 (SW48, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.784×** | -4.0 | 0.012 | 26/48 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | 0.852× | -3.7 | 0.030 | 23/48 (LOX-IMVI, AsPC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.804×** | -3.6 | 0.038 | 24/48 (LoVo, AsPC-1, …) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.663×** | -3.5 | 0.038 | 25/48 (NCI-H1792, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.707×** | -3.3 | 0.071 | 25/48 (hTERT-HPNE, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.687×** | -3.2 | 0.087 | 25/48 (Hs 766T, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.720×** | -3.2 | 0.092 | 21/48 (HCT15, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **0.693×** | -3.2 | 0.092 | 22/47 (LoVo, RKO, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.832× | -3.0 | 0.12 | 20/48 (NCI-H2347, SW48, …) | inconsistent across doses |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.878× | -3.0 | 0.12 | 11/49 (Hs 766T, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2002. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 98.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.353× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.399× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 91.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.2) ⚠ cell-cycle shift, explains ~74% of this change | [[Dinaciclib (drug)]] 5 µM 0.351× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[HOP62 (line)]] | alt | 66.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -10.3) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.464× (z -8.5) |
| [[SW 1271 (line)]] | alt | 90.2 | 0 | 2 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.105× (z -10.0) |
| [[SW48 (line)]] | wt | 114 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.03× (z +8.8) | — |
| [[A498 (line)]] | wt | 54.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AsPC-1 (line)]] | alt | 69.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -10.9) ⚠ cell-cycle shift, explains ~74% of this change |
| [[C32 (line)]] | wt | 66.4 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 7.18× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 81.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -11.0) ⚠ cell-cycle shift, explains ~74% of this change |
| [[LS 180 (line)]] | wt | 91.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[NCI-H2030 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.563× (z -9.1) ⚠ cell-cycle shift, explains ~74% of this change |
| [[NCI-H23 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.351× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[NCI-H2347 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.479× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~12% of this change |
| [[NCI-H460 (line)]] | wt | 76.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.483× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.426× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[A-172 (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 81.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 88.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 79.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 68.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 71.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 78.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 98.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 94.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 72.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2002), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LDB1]] | +0.62 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[CASTOR3P-1]] | +0.58 | +0.35 / +0.49 | both halves | 1e-04 |  |
| [[MSL3]] | +0.56 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[USF1]] | +0.56 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[HECA]] | +0.56 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[CTSZ]] | +0.55 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[CNPY3]] | +0.55 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[PPP2R5D]] | +0.55 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[HIPK1]] | +0.55 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[PCMTD1]] | +0.55 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[AMFR]] | +0.54 | +0.59 / +0.53 | both halves | 1e-05 | STRING 475 |
| [[ACTR1A]] | +0.54 | +0.51 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCFD1]] | -0.58 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[AASDH]] | -0.53 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[ESF1]] | -0.51 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[NOP58]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[CCDC28B]] | -0.50 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[RPF2]] | -0.50 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[ZNG1F]] | -0.49 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[BCAT2]] | -0.48 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[ISG20L2]] | -0.47 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[ASL]] | -0.47 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[CEBPZ]] | -0.47 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[GDF1]] | -0.46 | -0.43 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.533). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-18.2, -15.9); signed map (-19.1, -35.1). **Vector** length 104, 27.9% of its response variance represented; |z| ≥ 3 in 788 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.6 | +1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.3 | +1.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.9 | -1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | +4.7 | -2.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.6 | -0.1 |
|  | [[Erlotinib (drug)]] 5 µM |  | +2.5 | +2.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.3 | +2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +1.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.8 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -4.8 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -4.6 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -3.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.6 | -3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.4 | -3.5 |
|  | [[EX229 (drug)]] 5 µM |  | -3.3 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase, Mg2+/Mn2+ dependent 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.1 — chr14:60,245,752-60,299,087 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC9201, PP2Calpha, PP2CA |
| Gene groups (HGNC) | Protein phosphatases, Mg2+/Mn2+ dependent |
| Hallmark sets | TGF_BETA_SIGNALING |
| Reactome | 6 pathways, smallest: Energy dependent regulation of mTOR by LKB1-AMPK; Downregulation of SMAD2/3:SMAD4 transcriptional activity; MTOR signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [P35813](https://www.uniprot.org/uniprotkb/P35813) (Protein phosphatase 1A):

> Enzyme with a broad specificity. Negatively regulates TGF-beta signaling through dephosphorylating SMAD2 and SMAD3, resulting in their dissociation from SMAD4, nuclear export of the SMADs and termination of the TGF-beta-mediated signaling. Dephosphorylates PRKAA1 and PRKAA2. Plays an important role in the termination of TNF-mediated NF-kappa-B activation through dephosphorylating and inactivating IKBKB/IKKB.

**Summary**, from NCBI Gene [5494](https://www.ncbi.nlm.nih.gov/gene/5494):

> The protein encoded by this gene is a member of the PP2C family of Ser/Thr protein phosphatases. PP2C family members are known to be negative regulators of cell stress response pathways. This phosphatase dephosphorylates, and negatively regulates the activities of, MAP kinases and MAP kinase kinases. It has been shown to inhibit the activation of p38 and JNK kinase cascades induced by environmental stresses. This phosphatase can also dephosphorylate cyclin-dependent kinases, and thus may be …

**Accessions** — [HGNC:9275](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9275) · Entrez [5494](https://www.ncbi.nlm.nih.gov/gene/5494) · UniProt [P35813](https://www.uniprot.org/uniprotkb/P35813) · Ensembl [ENSG00000100614](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100614)

## Data

Gene col 2002: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2002); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2002, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2002]; `tensor/DDL_lfc|DDL_z.npy` [2002]; `embed/gene_vectors.npy` [2002]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2002 or target_col == 2002). Every well: [[PPM1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPM1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
