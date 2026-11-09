---
symbol: "NDUFAF1"
type: "gene"
col: 6068
ensembl_id: "ENSG00000137806"
name: "NADH:ubiquinone oxidoreductase complex assembly factor 1"
location: "15q15.1"
module: 170
arm: "+"
pooled_cpm: 8.64
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 8
n_dd_up_clean: 16
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/170"]
generated_by: "tahoemap"
---

# NDUFAF1

*NADH:ubiquinone oxidoreductase complex assembly factor 1* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.51× (z +16.2, q 0e+00, up in 42 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.549× (z -7.5, q 5e-11, down in 24 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF425]] (+0.74, fdr 7e-06), [[MDP1]] (+0.70, fdr 7e-06), [[HARBI1]] (+0.70, fdr 1e-05); moves opposite to [[LDHB]] (-0.64, fdr 1e-05), [[TBCD]] (-0.59, fdr 4e-05), [[PARP1]] (-0.58, fdr 1e-04).
> It sits in the **+** arm of [[Module 170]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6068.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.51×** | +16.2 | 0e+00 | 42/43 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.10×** | +13.5 | 3e-39 | 9/17 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.53×** | +11.5 | 2e-28 | 30/34 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +9.6 | 1e-19 | 33/47 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +8.5 | 2e-15 | 30/37 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.83×** | +7.5 | 5e-12 | 27/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.78×** | +6.9 | 5e-10 | 25/46 (KATO III, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +6.2 | 5e-08 | 29/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +6.1 | 6e-08 | 11/23 (SW1417, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +6.0 | 8e-08 | 23/41 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +6.0 | 9e-08 | 21/43 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +5.8 | 3e-07 | 23/44 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 4e-04 | 6/46 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +4.3 | 8e-04 | 18/48 (A498, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.59×** | +4.1 | 0.002 | 14/42 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.009 | 10/47 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.018 | 10/46 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.041 | 6/47 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.042 | 5/43 (LOX-IMVI, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6068.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.549×** | -7.5 | 5e-11 | 24/46 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.606×** | -6.2 | 1e-07 | 21/45 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.678×** | -4.8 | 3e-04 | 18/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.695×** | -4.3 | 0.002 | 17/38 (NCI-H23, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.714×** | -4.2 | 0.003 | 16/47 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Roxadustat (drug)]] 5 µM |  | **0.750×** | -3.4 | 0.055 | 11/45 (A549, C-33 A, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.602×** | -3.3 | 0.079 | 12/42 (SNU-423, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.770×** | -3.2 | 0.084 | 13/46 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tadalafil (drug)]] 5 µM |  | 0.776× | -3.0 | 0.14 | 11/45 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.784× | -3.0 | 0.14 | 12/46 (CHP-212, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.785× | -3.0 | 0.14 | 5/48 (NCI-H2030, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6068. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 10.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.85× (z +9.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.73× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -8.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 6.90 | 0 | 2 (1 ⚠) | — | [[Arbutin (drug)]] 5 µM 0.0716× (z -9.9) |
| [[A498 (line)]] | wt | 9.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +11.1) | — |
| [[BT-474 (line)]] | alt | 7.28 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0827× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 8.31 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 7.97× (z +9.5) ⚠ toxic | — |
| [[HEC-1-A (line)]] | alt | 8.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +9.9) | — |
| [[LoVo (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 7.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 9.20 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 7.55× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 8.83 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.278× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6068), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF425]] | +0.74 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[MDP1]] | +0.70 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[HARBI1]] | +0.70 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[SMIM19]] | +0.69 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[ZSWIM3]] | +0.68 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[ZNF490]] | +0.68 | +0.76 / +0.51 | both halves | 1e-05 |  |
| [[ATE1OSP]] | +0.68 | +0.77 / +0.51 | both halves | 1e-05 |  |
| [[TSG101]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[ZSCAN21]] | +0.68 | +0.82 / +0.46 | both halves | 3e-05 |  |
| [[GOSR1]] | +0.68 | +0.71 / +0.46 | both halves | 3e-05 |  |
| [[GPAT4-AS1]] | +0.67 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[CYP20A1]] | +0.67 | +0.73 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LDHB]] | -0.64 | -0.55 / -0.52 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[TBCD]] | -0.59 | -0.66 / -0.42 | both halves | 4e-05 |  |
| [[PARP1]] | -0.58 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[METAP1]] | -0.58 | -0.76 / -0.25 | both halves | 4e-04 |  |
| [[ST6GALNAC4]] | -0.58 | -0.63 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 170]]; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.809). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-28.5, 8.0); signed map (2.3, -13.4). **Vector** length 58.7, 8.85% of its response variance represented; |z| ≥ 3 in 820 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +16.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.0 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.8 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.4 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +4.1 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.1 | +1.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.1 | +2.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.0 | -4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -0.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | +0.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | +0.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase complex assembly factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:41,387,218-41,409,403 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CIA30, CGI-65 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors; Mitochondrial complex I assembly complex |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y375](https://www.uniprot.org/uniprotkb/Q9Y375) (Complex I intermediate-associated protein 30, mitochondrial):

> As part of the MCIA complex, involved in the assembly of the mitochondrial complex I.

**Summary**, from NCBI Gene [51103](https://www.ncbi.nlm.nih.gov/gene/51103):

> This gene encodes a complex I assembly factor protein. Complex I (NADH-ubiquinone oxidoreductase) catalyzes the transfer of electrons from NADH to ubiquinone (coenzyme Q) in the first step of the mitochondrial respiratory chain, resulting in the translocation of protons across the inner mitochondrial membrane. The encoded protein is required for assembly of complex I, and mutations in this gene are a cause of mitochondrial complex I deficiency. Alternatively spliced transcript variants have …

**Accessions** — [HGNC:18828](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18828) · Entrez [51103](https://www.ncbi.nlm.nih.gov/gene/51103) · UniProt [Q9Y375](https://www.uniprot.org/uniprotkb/Q9Y375) · Ensembl [ENSG00000137806](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137806)

## Data

Gene col 6068: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6068); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6068, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6068]; `tensor/DDL_lfc|DDL_z.npy` [6068]; `embed/gene_vectors.npy` [6068]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6068 or target_col == 6068). Every well: [[NDUFAF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFAF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
