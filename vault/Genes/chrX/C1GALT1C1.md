---
symbol: "C1GALT1C1"
type: "gene"
col: 10062
ensembl_id: "ENSG00000171155"
name: "C1GALT1 specific chaperone 1"
location: "Xq24"
module: 29
arm: "+"
pooled_cpm: 9.21
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# C1GALT1C1

*C1GALT1 specific chaperone 1* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.90× (z +7.5, q 3e-11, up in 11 of 17 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.33× (z +4.9, q 1e-04, up in 13 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.331× (z -18.8, q 0e+00, down in 40 of 42 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP5MC3]] (+0.67, fdr 7e-06, ⚠ ATP5MC3 in the vector space only through flagged drug-doses), [[PDHB]] (+0.60, fdr 1e-05), [[ICMT]] (+0.59, fdr 1e-05), [[CALM3]] (+0.59, fdr 2e-04); moves opposite to [[CIRBP]] (-0.66, fdr 1e-05), [[SNHG32]] (-0.64, fdr 4e-05), [[WASHC1]] (-0.59, fdr 7e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10062.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.90×** | +7.5 | 3e-11 | 11/17 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.74×** | +6.7 | 5e-09 | 17/31 (SNU-423, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.66×** | +5.7 | 3e-06 | 8/25 (SNU-423, J82, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +4.9 | 1e-04 | 13/47 (A498, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +4.3 | 0.002 | 13/46 (HOP62, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.27×** | +4.1 | 0.004 | 16/47 (CFPAC-1, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.37×** | +3.8 | 0.012 | 14/38 (PANC-1, HCT15, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.36×** | +3.7 | 0.014 | 11/47 (Hs 766T, KATO III, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.034 | 11/44 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.30×** | +3.2 | 0.081 | 5/47 (HOP62, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10062.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.331×** | -18.8 | 0e+00 | 40/42 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.359×** | -12.3 | 1e-32 | 35/40 (NCI-H2347, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.531×** | -7.6 | 5e-12 | 29/46 (SW48, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.626×** | -5.4 | 9e-06 | 25/43 (Panc 03.27, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 5 µM |  | **0.732×** | -5.3 | 1e-05 | 23/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.732×** | -5.3 | 1e-05 | 23/42 (Hs 766T, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.655×** | -5.1 | 3e-05 | 18/45 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.613×** | -4.8 | 1e-04 | 17/43 (SW480, J82, …) | all doses, flat | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.699×** | -4.1 | 0.002 | 16/43 (C-33 A, A498, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.535×** | -3.9 | 0.005 | 13/41 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **0.731×** | -3.8 | 0.009 | 12/43 (KATO III, SW 900, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.754×** | -3.4 | 0.034 | 10/47 (KATO III, SHP-77, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.600×** | -3.2 | 0.058 | 14/31 (PANC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.772×** | -3.1 | 0.088 | 17/44 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.618×** | -3.0 | 0.096 | 15/44 (A-427, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10062. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -17.3) |
| [[PANC-1 (line)]] | alt | 12.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -16.1) |
| [[C32 (line)]] | wt | 6.40 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0388× (z -11.6) |
| [[KATO III (line)]] | alt | 20.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -14.1) |
| [[NCI-H2030 (line)]] | alt | 11.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -16.2) |
| [[Panc 03.27 (line)]] | alt | 10.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -13.5) |
| [[SW 900 (line)]] | alt | 6.84 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0537× (z -11.3) |
| [[A498 (line)]] | wt | 6.33 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 7.02 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -9.4) |
| [[COLO 205 (line)]] | alt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 7.30 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -8.9) |
| [[Hs 766T (line)]] | wt | 28.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -20.0) |
| [[HS-578T (line)]] | alt | 5.93 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0993× (z -11.9) |
| [[HT-29 (line)]] | alt | 9.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -8.6) |
| [[J82 (line)]] | alt | 17.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -13.9) |
| [[LoVo (line)]] | wt | 6.59 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 7.18 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0661× (z -16.5) |
| [[NCI-H2347 (line)]] | alt | 4.90 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0271× (z -16.4) |
| [[RKO (line)]] | wt | 9.38 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 10.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 9.65 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -12.2) |
| [[SW1417 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW480 (line)]] | alt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -11.8) |
| [[A-172 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.862 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.39 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10062), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5MC3]] ⚠ | +0.67 | +0.65 / +0.65 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[PDHB]] | +0.60 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[ICMT]] | +0.59 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[CALM3]] | +0.59 | +0.72 / +0.29 | both halves | 2e-04 |  |
| [[TGOLN2]] | +0.58 | +0.73 / +0.30 | both halves | 2e-04 |  |
| [[APRT]] | +0.57 | +0.64 / +0.36 | both halves | 1e-04 | pathway: Diseases of metabolism |
| [[TMX1]] | +0.57 | +0.72 / +0.39 | both halves | 5e-05 |  |
| [[BANF1]] | +0.56 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[PPT1]] | +0.55 | +0.69 / +0.33 | both halves | 1e-04 |  |
| [[MDH2]] | +0.55 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[LSM4]] | +0.55 | +0.67 / +0.28 | both halves | 3e-04 |  |
| [[DCAF16]] | +0.55 | +0.71 / +0.27 | both halves | 3e-04 |  |
| [[ATP5F1B]] | +0.55 | +0.61 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIRBP]] | -0.66 | -0.70 / -0.52 | both halves | 1e-05 |  |
| [[SNHG32]] | -0.64 | -0.78 / -0.41 | both halves | 4e-05 |  |
| [[WASHC1]] | -0.59 | -0.68 / -0.38 | both halves | 7e-05 |  |
| [[TTC36-AS1]] | -0.56 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[EPB41L4A-AS1]] | -0.54 | -0.71 / -0.33 | both halves | 1e-04 |  |
| [[NOXRED1]] | -0.54 | -0.59 / -0.38 | both halves | 7e-05 |  |
| [[ZNF547]] | -0.54 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[MPHOSPH8]] | -0.54 | -0.65 / -0.36 | both halves | 1e-04 |  |
| [[FNBP4]] | -0.53 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[DNAJC2]] | -0.53 | -0.63 / -0.32 | both halves | 2e-04 |  |
| [[CCT6P3]] | -0.53 | -0.63 / -0.31 | both halves | 2e-04 |  |
| [[GATAD1]] | -0.53 | -0.56 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.528). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-37.9, -28.8); signed map (-31.0, -36.7). **Vector** length 72.2, 13.1% of its response variance represented; |z| ≥ 3 in 804 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +4.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.0 | +4.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.0 | +3.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.4 | +2.2 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +1.3 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.8 | -18.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | -12.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.7 | -5.4 |
|  | [[Artesunate (drug)]] 5 µM |  | -2.8 | -5.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.8 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.8 | -2.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | C1GALT1 specific chaperone 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq24 — chrX:120,625,674-120,630,054 (-) |
| Ensembl biotype | protein_coding |
| Also known as | COSMC, C1GALT2 |
| Reactome | 6 pathways, smallest: Defective C1GALT1C1 causes TNPS; O-linked glycosylation of mucins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EU7](https://www.uniprot.org/uniprotkb/Q96EU7) (C1GALT1-specific chaperone 1):

> Probable chaperone required for the generation of 1 O-glycan Gal-beta1-3GalNAc-alpha1-Ser/Thr (T antigen), which is a precursor for many extended O-glycans in glycoproteins. Probably acts as a specific molecular chaperone assisting the folding/stability of core 1 beta-3-galactosyltransferase (C1GALT1).

**Summary**, from NCBI Gene [29071](https://www.ncbi.nlm.nih.gov/gene/29071):

> This gene encodes a type II transmembrane protein that is similar to the core 1 beta1,3-galactosyltransferase 1, which catalyzes the synthesis of the core-1 structure, also known as Thomsen-Friedenreich antigen, on O-linked glycans. This gene product lacks the galactosyltransferase activity itself, but instead acts as a molecular chaperone required for the folding, stability and full activity of the core 1 beta1,3-galactosyltransferase 1. Mutations in this gene have been associated with Tn …

**Accessions** — [HGNC:24338](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24338) · Entrez [29071](https://www.ncbi.nlm.nih.gov/gene/29071) · UniProt [Q96EU7](https://www.uniprot.org/uniprotkb/Q96EU7) · Ensembl [ENSG00000171155](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171155)

## Data

Gene col 10062: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10062); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10062, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10062]; `tensor/DDL_lfc|DDL_z.npy` [10062]; `embed/gene_vectors.npy` [10062]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10062 or target_col == 10062). Every well: [[C1GALT1C1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1GALT1C1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
