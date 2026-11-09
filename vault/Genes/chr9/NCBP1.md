---
symbol: "NCBP1"
type: "gene"
col: 5944
ensembl_id: "ENSG00000136937"
name: "nuclear cap binding protein subunit 1"
location: "9q22.33"
module: 4
arm: "+"
pooled_cpm: 42.04
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# NCBP1

*nuclear cap binding protein subunit 1* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.50× (z +10.4, q 1e-22, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[XRK3F2 (drug)]] 0.5 µM: 0.754× (z -3.7, q 0.100, down in 17 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF2S1]] (+0.70, fdr 7e-06), [[NUP155]] (+0.70, fdr 7e-06), [[GCN1]] (+0.69, fdr 1e-05); moves opposite to [[EIF1]] (-0.66, fdr 1e-05), [[SAT2]] (-0.65, fdr 1e-05), [[RPS19]] (-0.63, fdr 8e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5944.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +10.4 | 1e-22 | 35/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.63×** | +8.8 | 2e-16 | 36/48 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.52×** | +8.8 | 2e-16 | 39/49 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.60×** | +8.6 | 1e-15 | 35/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.58×** | +8.4 | 6e-15 | 33/47 (MIA PaCa-2, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.54×** | +7.8 | 5e-13 | 38/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.51×** | +7.2 | 4e-11 | 26/40 (MIA PaCa-2, NCI-H1792, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +7.1 | 9e-11 | 33/48 (BT-474, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.45×** | +6.3 | 3e-08 | 27/44 (MIA PaCa-2, LS 180, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +5.7 | 7e-07 | 32/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.81×** | +5.7 | 8e-07 | 29/48 (KATO III, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.35×** | +5.5 | 2e-06 | 25/47 (SNU-423, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.4 | 3e-06 | 27/48 (MIA PaCa-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.5 | 2e-04 | 1/48 (CHP-212) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.27×** | +4.3 | 6e-04 | 22/48 (NCI-H1792, RKO, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.2 | 8e-04 | 18/48 (MIA PaCa-2, NCI-H1792, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.042 | 6/48 (SNU-423, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.18× | +3.0 | 0.075 | 7/48 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.084 | 10/48 (NCI-H460, J82, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5944.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.754×** | -3.7 | 0.100 | 17/47 (CHP-212, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.764×** | -3.5 | 0.100 | 21/47 (NCI-H661, SW 1271, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.829×** | -3.4 | 0.100 | 18/48 (hTERT-HPNE, Hs 766T, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.772×** | -3.4 | 0.100 | 15/48 (SW 1088, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.837× | -3.3 | 0.12 | 18/48 (A498, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5944. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 39.4 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +12.7) | — |
| [[A-427 (line)]] | wt | 42.5 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.476× (z -9.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[COLO 205 (line)]] | alt | 41.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +10.6) | — |
| [[HCT15 (line)]] | alt | 50.2 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.236× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 63.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 38.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[LS 180 (line)]] | wt | 39.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 24.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.36× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[NCI-H460 (line)]] | wt | 37.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.8) | — |
| [[SNU-423 (line)]] | alt | 31.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[SW480 (line)]] | alt | 71.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.2) | — |
| [[A-172 (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 54.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 46.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 69.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5944), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2S1]] | +0.70 | +0.65 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[NUP155]] | +0.70 | +0.60 / +0.74 | both halves | 7e-06 | pathway: HIV Infection; STRING 624 |
| [[GCN1]] | +0.69 | +0.52 / +0.73 | both halves | 1e-05 |  |
| [[NUP188]] | +0.68 | +0.51 / +0.74 | both halves | 1e-05 | pathway: HIV Infection; STRING 589 |
| [[LAS1L]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[SYNCRIP]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 473 |
| [[FARSB]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[XRCC5]] | +0.65 | +0.50 / +0.72 | both halves | 1e-05 | pathway: HIV Infection |
| [[UGGT1]] | +0.65 | +0.44 / +0.73 | both halves | 3e-05 |  |
| [[COPS3]] | +0.65 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[TRIP13]] | +0.64 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[SUPT16H]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 | pathway: Formation of HIV elongation complex in the absence of HIV Tat; STRING 735 |

## Genes that move opposite

*54 of its nearest partners move opposite, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF1]] | -0.66 | -0.56 / -0.69 | both halves | 1e-05 |  |
| [[SAT2]] | -0.65 | -0.54 / -0.70 | both halves | 1e-05 |  |
| [[RPS19]] | -0.63 | -0.58 / -0.64 | both halves | 8e-06 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC) |
| [[NACA4P]] ⚠ | -0.63 | -0.52 / -0.65 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CEP164P1]] | -0.63 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[RPL15]] | -0.63 | -0.51 / -0.66 | both halves | 1e-05 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC) |
| [[RPS15]] ⚠ | -0.62 | -0.51 / -0.69 | both halves | 1e-05 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC); ⚠ in the vector space only through flagged drug-doses |
| [[UBE2Z]] | -0.62 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[RPS27A]] ⚠ | -0.62 | -0.59 / -0.64 | both halves | 7e-06 | pathway: HIV Infection; ⚠ in the vector space only through flagged drug-doses |
| [[SNHG7]] | -0.62 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[RPS13]] ⚠ | -0.62 | -0.55 / -0.66 | both halves | 1e-05 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC); ⚠ in the vector space only through flagged drug-doses |
| [[EIF1B]] | -0.62 | -0.45 / -0.67 | both halves | 3e-05 |  |
| [[RPS29]] | -0.62 | -0.57 / -0.65 | both halves | 1e-05 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC) |
| [[GABARAPL2]] | -0.62 | -0.54 / -0.69 | both halves | 1e-05 |  |
| [[ZFAS1]] | -0.62 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[AKAP1-DT]] | -0.61 | -0.41 / -0.57 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.569). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-32.2, -32.7); signed map (-14.2, -44.4). **Vector** length 103, 25.0% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.6 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +5.3 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +4.8 | +6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | +4.6 | +7.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +7.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.3 | +3.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.2 | +2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +1.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.3 | -1.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.9 | -3.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.9 | -2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -3.2 | +3.6 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -0.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.4 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | nuclear cap binding protein subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.33 — chr9:97,633,668-97,673,748 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CBP80, Sto1; previously NCBP |
| Gene groups (HGNC) | MIF4G domain containing proteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 56 pathways, smallest: SLBP independent Processing of Histone Pre-mRNAs; SLBP Dependent Processing of Replication-Dependent Histone Pre-mRNAs; Signaling by FGFR2 IIIa TM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q09161](https://www.uniprot.org/uniprotkb/Q09161) (Nuclear cap-binding protein subunit 1):

> Component of the cap-binding complex (CBC), which binds cotranscriptionally to the 5'-cap of pre-mRNAs and is involved in various processes such as pre-mRNA splicing, translation regulation, nonsense-mediated mRNA decay, RNA-mediated gene silencing (RNAi) by microRNAs (miRNAs) and mRNA export. The CBC complex is involved in mRNA export from the nucleus via its interaction with ALYREF/THOC4/ALY, leading to the recruitment of the mRNA export machinery to the 5'-end of mRNA and to mRNA export in a …

**Summary**, from NCBI Gene [4686](https://www.ncbi.nlm.nih.gov/gene/4686):

> The product of this gene is a component of the nuclear cap-binding protein complex (CBC), which binds to the monomethylated 5' cap of nascent pre-mRNA in the nucleoplasm. The encoded protein promotes high-affinity mRNA-cap binding and associates with the CTD of RNA polymerase II. The CBC promotes pre-mRNA splicing, 3'-end processing, RNA nuclear export, and nonsense-mediated mRNA decay. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7658](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7658) · Entrez [4686](https://www.ncbi.nlm.nih.gov/gene/4686) · UniProt [Q09161](https://www.uniprot.org/uniprotkb/Q09161) · Ensembl [ENSG00000136937](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136937)

## Data

Gene col 5944: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5944); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5944, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5944]; `tensor/DDL_lfc|DDL_z.npy` [5944]; `embed/gene_vectors.npy` [5944]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5944 or target_col == 5944). Every well: [[NCBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
