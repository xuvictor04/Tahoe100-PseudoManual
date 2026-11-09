---
symbol: "GZF1"
type: "gene"
col: 4664
ensembl_id: "ENSG00000125812"
name: "GDNF inducible zinc finger protein 1"
location: "20p11.21"
module: 7
arm: "+"
pooled_cpm: 14.52
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 11
n_dd_up_clean: 24
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# GZF1

*GDNF inducible zinc finger protein 1* — 20p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.16× (z +25.9, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.432× (z -13.3, q 8e-38, down in 33 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.771× (z -4.1, q 0.003, down in 19 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GCC1]] (+0.69, fdr 1e-05), [[CREB3]] (+0.65, fdr 1e-05), [[TBL2]] (+0.63, fdr 2e-05); moves opposite to [[PAN3]] (-0.51, fdr 4e-05), [[NBL1]] (-0.48, fdr 7e-05), [[MARCHF6]] (-0.47, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 3 with an alert ⚠; shown: the 15 strongest. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4664.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.16×** | +25.9 | 0e+00 | 43/47 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.71×** | +20.8 | 0e+00 | 44/47 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **3.54×** | +20.1 | 0e+00 | 42/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.05×** | +17.7 | 0e+00 | 41/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.01×** | +16.8 | 0e+00 | 42/46 (SW1417, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.75×** | +16.1 | 0e+00 | 40/46 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +14.4 | 7e-45 | 36/45 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.14×** | +12.1 | 9e-32 | 38/47 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.01×** | +11.1 | 9e-27 | 36/48 (NCI-H1573, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.62×** | +10.8 | 1e-25 | 30/48 (SNU-1, SW1417, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.82×** | +9.5 | 9e-20 | 32/48 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.76×** | +9.0 | 2e-17 | 29/46 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.75×** | +8.9 | 2e-17 | 32/46 (SW1417, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.55×** | +7.8 | 3e-13 | 27/48 (SW1417, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.53×** | +7.7 | 4e-13 | 33/48 (NCI-H1573, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4664.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.432×** | -13.3 | 8e-38 | 33/46 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.670×** | -6.1 | 3e-07 | 22/42 (hTERT-HPNE, A498, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.720×** | -5.2 | 4e-05 | 21/39 (A498, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.729×** | -4.6 | 5e-04 | 15/28 (Hs 766T, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.749×** | -4.4 | 0.001 | 13/25 (KATO III, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.771×** | -4.1 | 0.003 | 19/47 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.771×** | -4.1 | 0.003 | 17/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Fumaric acid (drug)]] 0.5 µM |  | **0.786×** | -3.8 | 0.009 | 2/48 (A498, SW 1088) | inconsistent across doses | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **0.804×** | -3.3 | 0.054 | 8/47 (SW1417, AsPC-1, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.749×** | -3.3 | 0.061 | 12/43 (H4, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.813×** | -3.2 | 0.082 | 6/47 (A498, J82, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4664. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 14.7 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +19.3) | [[Digitoxin (drug)]] 5 µM 0.291× (z -9.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 17.0 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.162× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 68.0 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.85× (z +11.2) | [[Digitoxin (drug)]] 5 µM 0.229× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 11.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +14.8) | — |
| [[A-172 (line)]] | wt | 14.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +12.8) | — |
| [[NCI-H2347 (line)]] | alt | 7.01 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.48× (z +14.2) | [[Bosentan (hydrate) (drug)]] 5 µM 0.150× (z -9.9) |
| [[RKO (line)]] | wt | 16.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.54× (z +13.7) | — |
| [[SW1417 (line)]] | alt | 43.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.97× (z +23.2) | — |
| [[Hs 766T (line)]] | wt | 11.7 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 6.19× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -9.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 12.3 | 2 | 1 | [[Auranofin (drug)]] 5 µM 6.48× (z +10.2) | [[Bentamapimod (drug)]] 0.05 µM 0.180× (z -8.9) |
| [[A498 (line)]] | wt | 21.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -15.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 11.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.06× (z +11.2) | — |
| [[AsPC-1 (line)]] | alt | 10.1 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 8.15× (z +10.5) | — |
| [[C32 (line)]] | wt | 9.53 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +9.9) | [[Canagliflozin (drug)]] 0.05 µM 0.129× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 9.06 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.32× (z +13.2) | — |
| [[COLO 205 (line)]] | alt | 12.0 | 0 | 2 (1 ⚠) | — | [[Resveratrol (drug)]] 0.5 µM 0.0602× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 7.39 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +12.1) | — |
| [[HepG2_C3A (line)]] | wt | 11.8 | 0 | 2 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.104× (z -9.7) |
| [[HOP62 (line)]] | alt | 10.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +13.3) | — |
| [[PANC-1 (line)]] | alt | 13.1 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.41× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 13.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.49× (z +12.1) | — |
| [[BT-474 (line)]] | alt | 8.53 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.118× (z -8.5) |
| [[H4 (line)]] | wt | 12.0 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM 0.0838× (z -9.7) |
| [[HS-578T (line)]] | alt | 19.3 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 4.33× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 10.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +8.7) | — |
| [[J82 (line)]] | alt | 18.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +14.6) | — |
| [[LS 180 (line)]] | wt | 6.30 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 4.81 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.113× (z -9.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 8.92 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.31× (z +12.6) | — |
| [[SK-MEL-2 (line)]] | alt | 21.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +14.1) | — |
| [[A-427 (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4664), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCC1]] | +0.69 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[CREB3]] | +0.65 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[TBL2]] | +0.63 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[MSANTD4]] | +0.62 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[RBAK]] | +0.58 | +0.59 / +0.47 | both halves | 2e-05 | same gene group |
| [[EXOC8]] | +0.58 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[GTF2E1]] | +0.57 | +0.59 / +0.40 | both halves | 4e-05 |  |
| [[VCPIP1]] | +0.56 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[PCBP1]] | +0.56 | +0.67 / +0.33 | both halves | 1e-04 |  |
| [[STK16]] | +0.56 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[RTL6]] | +0.56 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[EMD]] | +0.55 | +0.53 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAN3]] | -0.51 | -0.67 / -0.41 | both halves | 4e-05 |  |
| [[NBL1]] | -0.48 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[MARCHF6]] | -0.47 | -0.50 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.537). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-32.8, 0.9); signed map (-6.1, -22.0). **Vector** length 81.3, 16.9% of its response variance represented; |z| ≥ 3 in 1,241 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.5 | +8.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.6 | +16.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +16.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +12.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +3.7 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.8 | -13.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.6 | -5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.3 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | -4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.7 | -3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | +0.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | GDNF inducible zinc finger protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.21 — chr20:23,362,182-23,373,062 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ322G13.2, ZBTB23; previously ZNF336 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H116](https://www.uniprot.org/uniprotkb/Q9H116) (GDNF-inducible zinc finger protein 1):

> Transcriptional repressor that binds the GZF1 responsive element (GRE) (consensus: 5'-TGCGCN[TG][CA]TATA-3'). May be regulating VSX2/HOX10 expression.

**Summary**, from NCBI Gene [64412](https://www.ncbi.nlm.nih.gov/gene/64412):

> Enables DNA-binding transcription repressor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Involved in negative regulation of transcription by RNA polymerase II. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15808](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15808) · Entrez [64412](https://www.ncbi.nlm.nih.gov/gene/64412) · UniProt [Q9H116](https://www.uniprot.org/uniprotkb/Q9H116) · Ensembl [ENSG00000125812](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125812)

## Data

Gene col 4664: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4664); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4664, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4664]; `tensor/DDL_lfc|DDL_z.npy` [4664]; `embed/gene_vectors.npy` [4664]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4664 or target_col == 4664). Every well: [[GZF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GZF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
