---
symbol: "BAG5"
type: "gene"
col: 9253
ensembl_id: "ENSG00000166170"
name: "BAG cochaperone 5"
location: "14q32.33"
module: 36
arm: "+"
pooled_cpm: 31.68
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# BAG5

*BAG cochaperone 5* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.59× (z +11.9, q 5e-30, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.847× (z -4.4, q 0.004, down in 18 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK9]] (+0.65, fdr 1e-05), [[FASTKD5]] (+0.65, fdr 1e-05), [[NIPA2]] (+0.61, fdr 1e-05); moves opposite to [[ABCA5]] (-0.58, fdr 1e-05), [[KMT2E]] (-0.56, fdr 1e-05), [[PNISR]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9253.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +11.9 | 5e-30 | 36/48 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.84×** | +11.1 | 3e-26 | 43/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +10.9 | 2e-25 | 41/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +9.9 | 5e-21 | 36/47 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.60×** | +9.1 | 8e-18 | 38/48 (LoVo, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.63×** | +9.0 | 3e-17 | 34/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.19×** | +7.5 | 5e-12 | 30/48 (KATO III, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.51×** | +7.5 | 5e-12 | 29/48 (SW480, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.53×** | +5.0 | 3e-05 | 24/41 (SW480, A-172, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +4.5 | 3e-04 | 20/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +4.4 | 6e-04 | 18/47 (NCI-H1792, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.27×** | +4.3 | 9e-04 | 19/47 (HOP62, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **1.26×** | +4.1 | 0.002 | 17/39 (LS 180, NCI-H460, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.6 | 0.010 | 13/48 (A549, SNU-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.23×** | +3.6 | 0.010 | 18/48 (HOP62, A-427, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.012 | 11/47 (NCI-H23, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Busulfan (drug)]] 5 µM |  | 1.15× | +3.5 | 0.014 | 14/48 (AN3 CA, C32, …) | inconsistent across doses | position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.13× | +3.2 | 0.033 | 11/48 (AsPC-1, SW480, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.045 | 14/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | 1.12× | +3.0 | 0.058 | 7/48 (CFPAC-1, LoVo, …) | top dose only | position effect removed |
| [[Busulfan (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.064 | 4/48 (Hs 766T, LS 180, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +2.9 | 0.066 | 14/48 (SK-MEL-2, NCI-H2347, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.35×** | +2.8 | 0.077 | 3/47 (Hs 766T, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9253.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.847× | -4.4 | 0.004 | 18/48 (COLO 205, KATO III, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.767×** | -4.3 | 0.004 | 20/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **0.753×** | -3.7 | 0.035 | 14/48 (SW48, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | **0.765×** | -3.5 | 0.059 | 21/48 (NCI-H460, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.771×** | -3.4 | 0.069 | 14/48 (NCI-H1573, C-33 A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.825× | -3.2 | 0.14 | 12/47 (C32, LoVo, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.844× | -3.1 | 0.14 | 13/46 (LoVo, C32, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9253. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 45.8 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.54× (z +11.0) | — |
| [[A-427 (line)]] | wt | 36.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 30.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.111× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[H4 (line)]] | wt | 22.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.131× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~42% of this change |
| [[KATO III (line)]] | alt | 44.5 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.40× (z +10.5) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 6.26× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 31.9 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.99× (z +9.0) | [[Torkinib (drug)]] 5 µM 0.0961× (z -10.0) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 30.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +10.2) | — |
| [[HOP62 (line)]] | alt | 24.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 29.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +8.5) | — |
| [[LoVo (line)]] | wt | 35.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.30× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 18.8 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.96× (z +9.3) ⚠ toxic | — |
| [[NCI-H1573 (line)]] | alt | 32.6 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.14× (z +11.6) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 23.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 27.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -9.9) ⚠ cell-cycle shift, explains ~54% of this change |
| [[NCI-H460 (line)]] | wt | 27.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 47.3 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.15× (z +9.8) ⚠ toxic | — |
| [[PANC-1 (line)]] | alt | 24.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 26.6 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0775× (z -12.2) |
| [[A-172 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9253), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK9]] | +0.65 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[FASTKD5]] | +0.65 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[NIPA2]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[EIF2S1]] | +0.61 | +0.70 / +0.46 | both halves | 2e-05 |  |
| [[NAA20]] | +0.61 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[SLC35C1]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[PRR14L]] | +0.60 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[ABCF2]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[MAGOH]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[VAMP3]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[ICE1]] | +0.59 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[ZNF460]] | +0.58 | +0.59 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCA5]] | -0.58 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[KMT2E]] | -0.56 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[PNISR]] | -0.53 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[PTBP2]] | -0.52 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[NBPF19]] | -0.51 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[CHMP2B]] | -0.51 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[TRA2A]] | -0.51 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[CTNNB1]] | -0.50 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[HNRNPH1]] | -0.50 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[VAMP2]] | -0.49 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[SRSF11]] ⚠ | -0.49 | -0.40 / -0.44 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TCAF1]] | -0.49 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[PIM3]] | -0.49 | -0.44 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.464). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-28.7, -11.3); signed map (-7.9, -27.3). **Vector** length 92.7, 20.4% of its response variance represented; |z| ≥ 3 in 897 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.6 | +9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +10.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | +7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +11.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.5 | +2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.9 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +3.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.7 | -1.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.8 | -4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -4.2 | -4.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.2 | -1.6 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.7 | -3.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -1.7 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | BAG cochaperone 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:103,556,545-103,562,657 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | BAG cochaperones |
| Reactome | 4 pathways, smallest: Regulation of HSF1-mediated heat shock response; Cellular response to heat stress; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UL15](https://www.uniprot.org/uniprotkb/Q9UL15) (BAG family molecular chaperone regulator 5):

> Co-chaperone for HSP/HSP70 proteins. It functions as a nucleotide-exchange factor promoting the release of ADP from HSP70, thereby activating HSP70-mediated protein refolding. Has an essential role in maintaining proteostasis at junctional membrane complexes (JMC), where it may function as a scaffold between the HSPA8 chaperone and JMC proteins enabling correct, HSPA8-dependent JMC protein folding (By similarity). Inhibits both auto-ubiquitination of PRKN and ubiquitination of target proteins …

**Summary**, from NCBI Gene [9529](https://www.ncbi.nlm.nih.gov/gene/9529):

> The protein encoded by this gene is a member of the BAG1-related protein family. BAG1 is an anti-apoptotic protein that functions through interactions with a variety of cell apoptosis and growth related proteins including BCL-2, Raf-protein kinase, steroid hormone receptors, growth factor receptors and members of the heat shock protein 70 kDa family. This protein contains a BAG domain near the C-terminus, which could bind and inhibit the chaperone activity of Hsc70/Hsp70. Three transcript …

**Accessions** — [HGNC:941](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:941) · Entrez [9529](https://www.ncbi.nlm.nih.gov/gene/9529) · UniProt [Q9UL15](https://www.uniprot.org/uniprotkb/Q9UL15) · Ensembl [ENSG00000166170](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166170)

## Data

Gene col 9253: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9253); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9253, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9253]; `tensor/DDL_lfc|DDL_z.npy` [9253]; `embed/gene_vectors.npy` [9253]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9253 or target_col == 9253). Every well: [[BAG5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAG5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
