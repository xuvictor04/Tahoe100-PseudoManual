---
symbol: "CDH26"
type: "gene"
col: 4502
ensembl_id: "ENSG00000124215"
name: "cadherin 26"
location: "20q13.33"
module: 15
arm: "+"
pooled_cpm: 3.31
n_lines_expressing: 45
n_dd_up: 6
n_dd_down: 25
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# CDH26

*cadherin 26* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.82× (z +5.4, q 3e-05, up in 10 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (16 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.271× (z -11.8, q 1e-29, down in 29 of 42 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.282× (z -6.0, q 2e-07, down in 21 of 36 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGK2]] (+0.61, fdr 1e-05), [[DDX59-AS1]] (+0.57, fdr 1e-05), [[SYCP2]] (+0.56, fdr 3e-05, ⚠ same locus), [[BNIPL]] (+0.55, fdr 1e-05); moves opposite to [[PPFIBP1]] (-0.51, fdr 3e-05), [[DYNLT1]] (-0.49, fdr 1e-04), [[TXNDC17]] (-0.49, fdr 2e-04).
> It sits in the **+** arm of [[Module 015]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4502.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.82×** | +5.4 | 3e-05 | 10/41 (PANC-1, KATO III, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.38×** | +4.1 | 0.007 | 7/41 (SW480, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.007 | 7/30 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.56×** | +4.1 | 0.007 | 10/40 (KATO III, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +3.7 | 0.022 | 1/7 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.50×** | +3.7 | 0.022 | 5/41 (A498, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.44× | +3.2 | 0.11 | 0/4 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4502.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.271×** | -11.8 | 1e-29 | 29/42 (HT-29, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.375×** | -8.9 | 2e-16 | 27/39 (NCI-H1573, NCI-H23, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.400×** | -8.3 | 2e-14 | 21/26 (NCI-H23, NCI-H2030, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.491×** | -6.4 | 2e-08 | 22/38 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.282×** | -6.0 | 2e-07 | 21/36 (A498, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.539×** | -5.6 | 2e-06 | 21/41 (HCT15, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.549×** | -5.4 | 5e-06 | 17/41 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.540×** | -5.4 | 6e-06 | 19/38 (A549, A498, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.568×** | -5.1 | 2e-05 | 15/27 (HT-29, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.673×** | -5.1 | 2e-05 | 13/42 (NCI-H1573, SW480, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.573×** | -5.0 | 2e-05 | 15/41 (H4, NCI-H1573, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.573×** | -4.9 | 6e-05 | 16/36 (NCI-H23, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.597×** | -4.7 | 1e-04 | 11/41 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.613×** | -4.4 | 4e-04 | 14/41 (SW 900, Hs 766T, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **0.615×** | -4.2 | 9e-04 | 13/23 (A-427, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.655×** | -3.8 | 0.004 | 11/41 (hTERT-HPNE, NCI-H1573, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.745×** | -3.8 | 0.005 | 13/41 (H4, CFPAC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.467×** | -3.6 | 0.009 | 10/28 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.673×** | -3.6 | 0.009 | 10/39 (NCI-H23, A549, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.500×** | -3.3 | 0.025 | 7/33 (A549, COLO 205, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4502. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 9.55 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0680× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A498 (line)]] | wt | 3.37 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0365× (z -11.3) ⚠ cell-cycle shift, explains ~68% of this change |
| [[A549 (line)]] | wt | 4.28 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0244× (z -11.6) ⚠ cell-cycle shift, explains ~68% of this change |
| [[HT-29 (line)]] | alt | 6.52 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0382× (z -11.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H1573 (line)]] | alt | 4.49 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0610× (z -10.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 3.14 | 0 | 2 (1 ⚠) | — | [[Belumosudil (drug)]] 5 µM 0.0603× (z -10.7) |
| [[SW1417 (line)]] | alt | 5.65 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0602× (z -10.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0653× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 2.68 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.5× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Hs 766T (line)]] | wt | 7.89 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0749× (z -9.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[MIA PaCa-2 (line)]] | alt | 3.45 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0638× (z -8.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2030 (line)]] | alt | 8.33 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0721× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW 900 (line)]] | alt | 3.92 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0463× (z -9.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 0.771 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.664 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.750 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4502), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 7 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGK2]] | +0.61 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[DDX59-AS1]] | +0.57 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[SYCP2]] | +0.56 | +0.46 / +0.43 | both halves | 3e-05 | ⚠ same locus (24.8 kb: neighbours can correlate without regulation) |
| [[BNIPL]] | +0.55 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[MYL6B-AS1]] | +0.55 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[ZNF630]] | +0.52 | +0.54 / +0.30 | both halves | 2e-04 |  |
| [[SNED1-AS1]] | +0.51 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[LINC01355]] | +0.50 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[KLRA1P]] | +0.50 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[ADHFE1]] | +0.50 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[PPP1CB-DT]] | +0.50 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[NUDT13]] | +0.50 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[HYPK]] | +0.49 | +0.41 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPFIBP1]] | -0.51 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[DYNLT1]] | -0.49 | -0.32 / -0.39 | both halves | 1e-04 |  |
| [[TXNDC17]] | -0.49 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[KLF7]] | -0.49 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[RASA1]] | -0.48 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[ARL4C]] | -0.46 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[F3]] | -0.45 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[TIAM1]] | -0.44 | -0.28 / -0.34 | both halves | 3e-04 |  |
| [[PICALM]] | -0.44 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[PDLIM7]] | -0.44 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[RIC1]] | -0.44 | -0.39 / -0.25 | both halves | 4e-04 |  |
| [[CD59]] | -0.43 | -0.47 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.347). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (4.9, 27.2); signed map (37.1, -11.6). **Vector** length 52.0, 7.19% of its response variance represented; |z| ≥ 3 in 1,062 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.4 | +0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +2.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.5 | +4.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.3 | +2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.1 | +1.6 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -2.6 | -5.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.4 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.2 | -11.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | -1.8 | -3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.7 | -8.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -4.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.3 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.2 | -1.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | cadherin 26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:59,958,423-60,034,011 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VR20 |
| Gene groups (HGNC) | Major cadherins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXH8](https://www.uniprot.org/uniprotkb/Q8IXH8) (Cadherin-like protein 26):

> Cadherins are calcium-dependent cell adhesion proteins. They preferentially interact with themselves in a homophilic manner in connecting cells; cadherins may thus contribute to the sorting of heterogeneous cell types. Ligand for integrins alpha-E/beta-7, ITGAE:ITGAB7, alpha-4/beta-7, ITGA4:ITGAB7 and alpha-4/beta-1, ITGA4:ITGAB1 through which modulates CD4(+) T cells activation.

**Summary**, from NCBI Gene [60437](https://www.ncbi.nlm.nih.gov/gene/60437):

> This gene encodes a member of the cadherin protein family. Cadherins are a family of calcium-dependent adhesion molecules that mediate cell-cell adhesion in all solid tissues and modulate a wide variety of processes, including cell polarization, migration and differentiation. Cadherin domains occur as repeats in the extracellular region and are thought to contribute to the sorting of heterogeneous cell types and the maintenance of orderly structures such as epithelium. This protein is expressed …

**Accessions** — [HGNC:15902](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15902) · Entrez [60437](https://www.ncbi.nlm.nih.gov/gene/60437) · UniProt [Q8IXH8](https://www.uniprot.org/uniprotkb/Q8IXH8) · Ensembl [ENSG00000124215](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124215)

## Data

Gene col 4502: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4502); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4502, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4502]; `tensor/DDL_lfc|DDL_z.npy` [4502]; `embed/gene_vectors.npy` [4502]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4502 or target_col == 4502). Every well: [[CDH26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDH26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
