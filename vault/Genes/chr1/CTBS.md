---
symbol: "CTBS"
type: "gene"
col: 3879
ensembl_id: "ENSG00000117151"
name: "chitobiase"
location: "1p22.3"
module: 5
arm: "-"
pooled_cpm: 30.63
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 18
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# CTBS

*chitobiase* — 1p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.70× (z +7.4, q 6e-11, up in 29 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.30× (z +5.1, q 5e-05, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.605× (z -9.8, q 5e-20, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DAD1]] (+0.47, fdr 9e-05), [[TMEM9]] (+0.46, fdr 2e-04), [[PDZD11]] (+0.46, fdr 2e-04); moves opposite to [[ASMTL-AS1]] (-0.48, fdr 1e-04), [[NCL]] (-0.47, fdr 2e-04), [[MYO19]] (-0.47, fdr 4e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3879.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +7.4 | 6e-11 | 29/41 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +6.2 | 2e-07 | 24/35 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +5.1 | 5e-05 | 25/47 (NCI-H2347, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.57×** | +4.5 | 0.001 | 28/45 (A-427, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +4.4 | 0.001 | 23/39 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.008 | 21/47 (SHP-77, HT-29, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.26×** | +3.2 | 0.094 | 15/47 (A549, BT-474, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.2 | 0.096 | 15/47 (SW480, BT-474, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.2 | 0.096 | 1/47 (NCI-H23) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.25× | +3.1 | 0.11 | 20/47 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.12 | 13/47 (KATO III, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3879.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.605×** | -9.8 | 5e-20 | 37/46 (NCI-H1792, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.638×** | -6.2 | 1e-07 | 29/47 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.640×** | -6.2 | 1e-07 | 31/47 (KATO III, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.649×** | -6.0 | 3e-07 | 31/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.651×** | -5.9 | 3e-07 | 31/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.648×** | -5.8 | 7e-07 | 33/45 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.727×** | -4.4 | 9e-04 | 27/47 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.552×** | -4.3 | 0.001 | 27/46 (A-427, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.814×** | -4.0 | 0.004 | 19/47 (Hs 766T, PANC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.765×** | -3.7 | 0.013 | 19/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.780×** | -3.4 | 0.031 | 18/47 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.773×** | -3.4 | 0.036 | 17/46 (LS 180, LOX-IMVI, …) | inconsistent across doses |  |
| [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | **0.785×** | -3.3 | 0.036 | 13/47 (KATO III, SW 1271, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.794×** | -3.2 | 0.061 | 17/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.651×** | -3.1 | 0.073 | 12/47 (KATO III, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[crizotinib (drug)]] 5 µM |  | **0.794×** | -3.1 | 0.079 | 17/47 (SNU-423, A-172, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.802×** | -3.0 | 0.081 | 15/47 (KATO III, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.664×** | -3.0 | 0.095 | 18/46 (A-427, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3879. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 30.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.70× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -12.2) |
| [[A498 (line)]] | wt | 40.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -11.6) |
| [[A-427 (line)]] | wt | 35.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.271× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 24.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +9.0) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 39.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 24.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 34.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -10.9) |
| [[HS-578T (line)]] | alt | 47.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 32.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 31.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -13.2) |
| [[NCI-H2347 (line)]] | alt | 36.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -8.8) |
| [[PANC-1 (line)]] | alt | 82.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 38.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -11.1) |
| [[SHP-77 (line)]] | alt | 18.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -9.8) |
| [[SNU-1 (line)]] | wt | 22.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 29.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -11.4) |
| [[SW 1088 (line)]] | alt | 76.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0784× (z -11.7) |
| [[SW480 (line)]] | alt | 15.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -8.9) |
| [[A-172 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.27 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3879), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAD1]] | +0.47 | +0.37 / +0.51 | both halves | 9e-05 |  |
| [[TMEM9]] | +0.46 | +0.31 / +0.43 | both halves | 2e-04 |  |
| [[PDZD11]] | +0.46 | +0.44 / +0.32 | both halves | 2e-04 |  |
| [[NKIRAS2]] | +0.46 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[RBM18]] | +0.45 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[CTSB]] | +0.44 | +0.36 / +0.39 | both halves | 1e-04 |  |
| [[CCNI]] | +0.44 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[TOX4]] | +0.44 | +0.43 / +0.39 | both halves | 6e-05 |  |
| [[TSPAN31]] | +0.44 | +0.37 / +0.54 | both halves | 9e-05 |  |
| [[SMIM20]] | +0.42 | +0.38 / +0.37 | both halves | 8e-05 |  |
| [[AGA]] | +0.42 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[PRAF2]] | +0.41 | +0.41 / +0.29 | both halves | 2e-04 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASMTL-AS1]] | -0.48 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[NCL]] | -0.47 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[MYO19]] | -0.47 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[TONSL]] | -0.46 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[CHAF1A]] | -0.44 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[C1orf159]] | -0.44 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[ALYREF]] | -0.44 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[UHRF1]] | -0.43 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[NASP]] | -0.42 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[MAD1L1]] | -0.42 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[NOM1]] | -0.41 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[DGCR8]] | -0.41 | -0.25 / -0.52 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.373). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-25.9, -40.2); signed map (-22.7, -5.7). **Vector** length 70.6, 13.5% of its response variance represented; |z| ≥ 3 in 792 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.7 | +5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.2 | +3.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.4 | +1.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +4.5 |
|  | [[Riluzole hydrochloride (drug)]] 0.05 µM |  | +1.4 | +1.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.2 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -4.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.1 | -5.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -3.4 |
|  | [[crizotinib (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | chitobiase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.3 — chr1:84,549,611-84,574,480 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CTB |
| Gene groups (HGNC) | Chitinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01459](https://www.uniprot.org/uniprotkb/Q01459) (Di-N-acetylchitobiase):

> Reducing-end exoglycosidase involved in glycan degradation. Hydrolyzes N,N'-diacetylchitobiose (GlnNAc2) and higher chitin-oligosaccharides (GlcNAc(n)) to monomeric GlcNAc acting on reducing-end residues. During N-linked glycoprotein degradation, it cleaves single GlcNAc molecules uniquely from the reducing end of N,N'-diacetylchitobiose units linking oligosaccharides to proteins, and therefore it functions after cleavage of the Asn-GlcNAc bond and asparagine removal by glycosylasparaginase (By …

**Summary**, from NCBI Gene [1486](https://www.ncbi.nlm.nih.gov/gene/1486):

> Chitobiase is a lysosomal glycosidase involved in degradation of asparagine-linked oligosaccharides on glycoproteins (Aronson and Kuranda, 1989 [PubMed 2531691]).[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:2496](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2496) · Entrez [1486](https://www.ncbi.nlm.nih.gov/gene/1486) · UniProt [Q01459](https://www.uniprot.org/uniprotkb/Q01459) · Ensembl [ENSG00000117151](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117151)

## Data

Gene col 3879: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3879); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3879, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3879]; `tensor/DDL_lfc|DDL_z.npy` [3879]; `embed/gene_vectors.npy` [3879]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3879 or target_col == 3879). Every well: [[CTBS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTBS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
