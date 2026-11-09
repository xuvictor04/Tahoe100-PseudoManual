---
symbol: "XRCC1"
type: "gene"
col: 1041
ensembl_id: "ENSG00000073050"
name: "X-ray repair cross complementing 1"
location: "19q13.31"
module: 12
arm: "+"
pooled_cpm: 24.98
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# XRCC1

*X-ray repair cross complementing 1* — 19q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.93× (z +19.2, q 0e+00, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.520× (z -13.5, q 9e-39, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COQ6]] (+0.65, fdr 1e-05), [[REXO5]] (+0.63, fdr 1e-05), [[SIX5]] (+0.62, fdr 1e-05); moves opposite to [[TXN]] (-0.62, fdr 1e-05), [[PROCR]] (-0.60, fdr 8e-06), [[NUTF2]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1041.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +19.2 | 0e+00 | 40/47 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.83×** | +12.0 | 7e-31 | 35/48 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~17% of this change | **1.30×** | +5.5 | 9e-06 | 19/45 (NCI-H460, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Larotrectinib (drug)]] 0.5 µM |  | 1.19× | +3.7 | 0.035 | 9/48 (SW1417, SW480, …) | inconsistent across doses | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.039 | 11/48 (SW480, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.13× | +3.5 | 0.046 | 4/48 (A-172, NCI-H1792, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.3 | 0.079 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.2 | 0.083 | 10/38 (HEC-1-A, HT-29, …) | all doses, flat | composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.083 | 9/48 (LoVo, LOX-IMVI, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1041.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.520×** | -13.5 | 9e-39 | 41/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.542×** | -12.7 | 3e-34 | 31/47 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.569×** | -11.6 | 6e-29 | 39/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.705×** | -10.2 | 2e-22 | 37/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.656×** | -8.7 | 4e-16 | 34/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.685×** | -7.8 | 6e-13 | 25/48 (RPMI-7951, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.687×** | -7.7 | 8e-13 | 25/47 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.708×** | -6.7 | 1e-09 | 25/48 (HOP62, SW 900, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.772×** | -5.4 | 6e-06 | 20/48 (HOP62, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.841× | -5.1 | 2e-05 | 17/48 (A498, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.808×** | -4.4 | 5e-04 | 16/47 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.666×** | -4.4 | 5e-04 | 18/41 (SW 900, HT-29, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.823×** | -4.0 | 0.003 | 16/48 (SW 1271, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.824×** | -4.0 | 0.003 | 16/48 (A-172, SW480, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.831×** | -3.8 | 0.005 | 18/48 (A498, SW 1088, …) | all doses, flat |  |
| [[Isocorydine (drug)]] 5 µM |  | 0.882× | -3.7 | 0.008 | 7/48 (HS-578T, PANC-1, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.840× | -3.4 | 0.023 | 15/47 (LOX-IMVI, RPMI-7951, …) | inconsistent across doses |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | 0.845× | -3.3 | 0.026 | 3/48 (HOP62, NCI-H460, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.894× | -3.3 | 0.030 | 8/48 (SW 900, A498, …) | rises with dose |  |
| [[Hydroxyurea (drug)]] 0.5 µM |  | 0.854× | -3.3 | 0.031 | 8/47 (AsPC-1, H4, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1041. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 28.3 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.338× (z -12.0) |
| [[A-172 (line)]] | wt | 34.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +18.0) | — |
| [[HEC-1-A (line)]] | alt | 38.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +22.8) | — |
| [[HOP62 (line)]] | alt | 40.9 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +10.9) | [[Digitoxin (drug)]] 5 µM 0.288× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.335× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 18.5 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.322× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.363× (z -9.3) |
| [[PANC-1 (line)]] | alt | 18.4 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +12.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.383× (z -9.6) |
| [[SHP-77 (line)]] | alt | 28.2 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 25.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +8.6) | [[Neratinib (maleate) (drug)]] 0.5 µM 0.299× (z -8.6) ⚠ cell-cycle shift, explains ~10% of this change |
| [[SW 900 (line)]] | alt | 38.2 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -9.4) |
| [[A498 (line)]] | wt | 32.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +13.9) | — |
| [[A549 (line)]] | wt | 35.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +15.2) | — |
| [[AN3 CA (line)]] | alt | 35.2 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0942× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.142× (z -10.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 18.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +9.5) | — |
| [[HepG2_C3A (line)]] | wt | 16.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 25.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +10.2) | — |
| [[J82 (line)]] | alt | 28.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +16.8) | — |
| [[LOX-IMVI (line)]] | wt | 22.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.312× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 19.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 29.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +8.7) | — |
| [[RKO (line)]] | wt | 21.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +11.1) | — |
| [[RPMI-7951 (line)]] | alt | 30.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +12.0) | — |
| [[SK-MEL-2 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 20.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +11.7) | — |
| [[A-427 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1041), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COQ6]] | +0.65 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[REXO5]] | +0.63 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[SIX5]] | +0.62 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[HIRIP3]] | +0.62 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[SUPT20H]] | +0.62 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[ZNF318]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[SEPSECS]] | +0.60 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[NABP2]] | +0.60 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[EMC9]] | +0.59 | +0.70 / +0.44 | both halves | 3e-05 |  |
| [[GORAB]] | +0.59 | +0.70 / +0.39 | both halves | 5e-05 |  |
| [[PBX2]] | +0.58 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[METTL25B]] | +0.58 | +0.63 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXN]] | -0.62 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[PROCR]] | -0.60 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[NUTF2]] | -0.54 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[GARNL3]] | -0.54 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[NME2]] | -0.53 | -0.64 / -0.31 | both halves | 2e-04 |  |
| [[CMTM8]] | -0.52 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[PRDX1]] | -0.51 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[PIP4K2A]] | -0.51 | -0.60 / -0.40 | both halves | 4e-05 |  |
| [[PRRG1]] | -0.51 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[HAGLR]] | -0.50 | -0.36 / -0.60 | both halves | 1e-04 |  |
| [[MIPOL1]] | -0.50 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[PACC1]] | -0.50 | -0.51 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.430). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-43.4, -43.9); signed map (7.3, -24.4). **Vector** length 99.5, 22.0% of its response variance represented; |z| ≥ 3 in 909 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.8 | +19.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.7 | +12.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.1 | +2.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~17% of this change | +2.4 | +5.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | -1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +3.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.2 | +1.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.2 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.4 | -10.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.2 | -7.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.9 | -11.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.4 | -12.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.1 | -13.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -5.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | X-ray repair cross complementing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.31 — chr19:43,543,311-43,580,473 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RCC |
| Reactome | 13 pathways, smallest: Resolution of AP sites via the single-nucleotide replacement pathway; APEX1-Independent Resolution of AP Sites via the Single Nucleotide Replacement Pathway; HDR through MMEJ (alt-NHEJ) |
| Matched by | ensembl_id |

**Function**, from UniProt [P18887](https://www.uniprot.org/uniprotkb/P18887) (DNA repair protein XRCC1):

> Scaffold protein involved in DNA single-strand break repair by mediating the assembly of DNA break repair protein complexes. Negatively regulates ADP-ribosyltransferase activity of PARP1 during base-excision repair in order to prevent excessive PARP1 activity. Recognizes and binds poly-ADP-ribose chains: specifically binds auto-poly-ADP-ribosylated PARP1, limiting its activity.

**Summary**, from NCBI Gene [7515](https://www.ncbi.nlm.nih.gov/gene/7515):

> The protein encoded by this gene is involved in the efficient repair of DNA single-strand breaks formed by exposure to ionizing radiation and alkylating agents. This protein interacts with DNA ligase III, polymerase beta and poly (ADP-ribose) polymerase to participate in the base excision repair pathway. It may play a role in DNA processing during meiogenesis and recombination in germ cells. A rare microsatellite polymorphism in this gene is associated with cancer in patients of varying …

**Accessions** — [HGNC:12828](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12828) · Entrez [7515](https://www.ncbi.nlm.nih.gov/gene/7515) · UniProt [P18887](https://www.uniprot.org/uniprotkb/P18887) · Ensembl [ENSG00000073050](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073050)

## Data

Gene col 1041: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1041); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1041, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1041]; `tensor/DDL_lfc|DDL_z.npy` [1041]; `embed/gene_vectors.npy` [1041]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1041 or target_col == 1041). Every well: [[XRCC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XRCC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
