---
symbol: "GCC1"
type: "gene"
col: 11043
ensembl_id: "ENSG00000179562"
name: "GRIP and coiled-coil domain containing 1"
location: "7q32.1"
module: 7
arm: "+"
pooled_cpm: 17.65
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 9
n_dd_up_clean: 19
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# GCC1

*GRIP and coiled-coil domain containing 1* — 7q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.96× (z +14.7, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Carbidopa (monohydrate) (drug)]] 0.05 µM: 0.662× (z -6.3, q 7e-08, down in 29 of 48 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Anethole trithione (drug)]] 5 µM: 0.796× (z -4.9, q 1e-04, down in 18 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GZF1]] (+0.69, fdr 1e-05), [[TADA2B]] (+0.68, fdr 1e-05), [[CCDC174]] (+0.68, fdr 7e-06); moves opposite to [[CPSF6]] (-0.57, fdr 1e-05), [[PHTF2]] (-0.55, fdr 2e-05), [[DPY19L1]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11043.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +14.7 | 0e+00 | 42/47 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +12.0 | 6e-31 | 37/46 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +10.9 | 4e-25 | 37/45 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.00×** | +10.8 | 6e-25 | 42/48 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.93×** | +10.1 | 4e-22 | 40/48 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.88×** | +9.8 | 9e-21 | 42/48 (C32, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.12×** | +9.2 | 3e-18 | 34/48 (SW480, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.76×** | +8.8 | 1e-16 | 34/48 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.80×** | +8.7 | 1e-16 | 35/47 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +8.2 | 1e-14 | 37/48 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.61×** | +7.0 | 1e-10 | 28/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +6.9 | 2e-10 | 26/48 (PANC-1, NCI-H2030, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.53×** | +6.1 | 6e-08 | 25/46 (C32, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +5.7 | 5e-07 | 24/44 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +5.5 | 1e-06 | 22/42 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.40×** | +5.3 | 4e-06 | 21/47 (A-427, NCI-H460, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.33×** | +4.4 | 3e-04 | 19/46 (CFPAC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11043.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.662×** | -6.3 | 7e-08 | 29/48 (A498, HEC-1-A, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.651×** | -6.3 | 7e-08 | 16/30 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.689×** | -5.7 | 2e-06 | 21/39 (KATO III, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.711×** | -5.2 | 2e-05 | 23/46 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Anethole trithione (drug)]] 5 µM |  | **0.796×** | -4.9 | 1e-04 | 18/48 (A498, H4, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.746×** | -4.5 | 7e-04 | 21/47 (NCI-H1573, KATO III, …) | two highest doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.757×** | -4.3 | 0.002 | 18/48 (HT-29, NCI-H1792, …) | inconsistent across doses |  |
| [[Clonidine (hydrochloride) (drug)]] 5 µM |  | **0.833×** | -3.9 | 0.006 | 7/48 (J82, SW480, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.775×** | -3.6 | 0.019 | 13/34 (SNU-423, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.820× | -3.0 | 0.13 | 16/46 (H4, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.821× | -3.0 | 0.13 | 14/48 (HT-29, SW 1271, …) | two highest doses | composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11043. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 16.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 27.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.287× (z -9.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 27.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.287× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 20.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +9.0) | [[AZD2858 (drug)]] 0.5 µM 0.117× (z -8.8) ⚠ toxic |
| [[A498 (line)]] | wt | 43.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.8) | — |
| [[A549 (line)]] | wt | 14.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -9.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -9.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 25.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +10.7) | — |
| [[H4 (line)]] | wt | 18.7 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.106× (z -9.5) |
| [[HCT15 (line)]] | alt | 14.7 | 0 | 1 | — | [[Resveratrol (drug)]] 0.5 µM 0.0694× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 10.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 8.80 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.190× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 11.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.91× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -13.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -11.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.00 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11043), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GZF1]] | +0.69 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[TADA2B]] | +0.68 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[CCDC174]] | +0.68 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[ZNF408]] | +0.67 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[NRBF2]] | +0.67 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[ZNF646]] | +0.67 | +0.77 / +0.52 | both halves | 1e-05 |  |
| [[TSSC4]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[VCPIP1]] | +0.66 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[CBLL1]] | +0.66 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[XBP1]] | +0.65 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[EXOC8]] | +0.65 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[BRMS1]] | +0.65 | +0.71 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPSF6]] | -0.57 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[PHTF2]] | -0.55 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[DPY19L1]] | -0.55 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[ATP1B3]] | -0.55 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[UXS1]] | -0.55 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[BRI3BP]] | -0.54 | -0.58 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.694). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-37.5, -1.3); signed map (-5.9, -23.3). **Vector** length 86.9, 17.7% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.5 | +9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.9 | +10.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.7 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +8.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +9.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +3.9 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +2.3 | +1.7 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.2 | -5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.1 | -6.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.8 | -5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.2 | -3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +1.4 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Acetohexamide (drug)]] 5 µM |  | -1.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | GRIP and coiled-coil domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.1 — chr7:127,580,628-127,593,611 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22035, GCC88, GCC1P, MGC20706 |
| Gene groups (HGNC) | Golgins |
| Reactome | 4 pathways, smallest: Retrograde transport at the Trans-Golgi-Network; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CN9](https://www.uniprot.org/uniprotkb/Q96CN9) (GRIP and coiled-coil domain-containing protein 1):

> Probably involved in maintaining Golgi structure.

**Summary**, from NCBI Gene [79571](https://www.ncbi.nlm.nih.gov/gene/79571):

> The protein encoded by this gene is a peripheral membrane protein. It is sensitive to brefeldin A. This encoded protein contains a GRIP domain which is thought to be used in targeting. It may play a role in the organization of trans-Golgi network subcompartment involved with membrane transport. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19095](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19095) · Entrez [79571](https://www.ncbi.nlm.nih.gov/gene/79571) · UniProt [Q96CN9](https://www.uniprot.org/uniprotkb/Q96CN9) · Ensembl [ENSG00000179562](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179562)

## Data

Gene col 11043: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11043); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11043, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11043]; `tensor/DDL_lfc|DDL_z.npy` [11043]; `embed/gene_vectors.npy` [11043]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11043 or target_col == 11043). Every well: [[GCC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
