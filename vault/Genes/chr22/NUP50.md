---
symbol: "NUP50"
type: "gene"
col: 1717
ensembl_id: "ENSG00000093000"
name: "nucleoporin 50"
location: "22q13.31"
module: 71
arm: "+"
pooled_cpm: 56.01
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# NUP50

*nucleoporin 50* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.74× (z +13.5, q 5e-39, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.800× (z -6.3, q 2e-07, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDOR1]] (+0.64, fdr 7e-06), [[ZNF718]] (+0.64, fdr 1e-05), [[SUV39H2]] (+0.64, fdr 1e-05); moves opposite to [[TMEM167B]] (-0.62, fdr 7e-06), [[GOLGA4]] (-0.61, fdr 1e-05), [[SEC11C]] (-0.60, fdr 1e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MDFI]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1717.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.74×** | +13.5 | 5e-39 | 47/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.31×** | +12.3 | 3e-32 | 45/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +9.8 | 2e-20 | 36/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +8.3 | 2e-14 | 37/47 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +8.0 | 2e-13 | 38/48 (HCT15, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +7.9 | 3e-13 | 36/47 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.45×** | +7.3 | 3e-11 | 33/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +7.3 | 3e-11 | 26/47 (MIA PaCa-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +7.2 | 3e-11 | 35/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.41×** | +6.7 | 1e-09 | 31/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.27×** | +6.5 | 5e-09 | 26/48 (NCI-H2030, SNU-423, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +5.8 | 4e-07 | 28/48 (NCI-H2030, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.64×** | +5.0 | 2e-05 | 20/34 (NCI-H1573, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.27×** | +4.7 | 1e-04 | 25/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +4.4 | 4e-04 | 24/48 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.3 | 7e-04 | 17/48 (SNU-423, SW1417, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.018 | 18/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.057 | 12/49 (CFPAC-1, HCT15, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1717.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.800×** | -6.3 | 2e-07 | 31/48 (LoVo, SW48, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.778×** | -5.0 | 2e-04 | 26/48 (LoVo, SHP-77, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.796×** | -4.6 | 1e-03 | 22/48 (SW48, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.811×** | -4.2 | 0.004 | 22/47 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.864× | -4.2 | 0.004 | 23/48 (SW48, LoVo, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.818×** | -4.0 | 0.006 | 22/49 (SW 1088, C32, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.820×** | -3.8 | 0.011 | 18/47 (SW48, C32, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.876× | -3.7 | 0.016 | 15/49 (C32, SW48, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.833×** | -3.7 | 0.016 | 19/49 (RKO, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -3.5 | 0.024 | 19/48 (SW48, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.845× | -3.4 | 0.029 | 16/49 (C32, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.865× | -3.4 | 0.032 | 15/48 (AsPC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | 0.833× | -3.4 | 0.032 | 17/47 (AsPC-1, C32, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.864× | -3.4 | 0.032 | 17/48 (SW48, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.849× | -3.3 | 0.041 | 19/48 (Hs 766T, A-427, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.861× | -3.0 | 0.080 | 13/47 (HS-578T, NCI-H2347, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.864× | -2.9 | 0.097 | 7/48 (CFPAC-1, SW48, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1717. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.9 | 7 (4 ⚠) | 0 | [[Digitoxin (drug)]] 0.05 µM 2.71× (z +10.5) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.54× (z +9.4) | — |
| [[SW48 (line)]] | wt | 343 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -17.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.251× (z -10.0) |
| [[PANC-1 (line)]] | alt | 39.0 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +13.1) | — |
| [[SW480 (line)]] | alt | 65.5 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.17× (z +12.1) | — |
| [[HEC-1-A (line)]] | alt | 69.5 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.40× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.208× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[A-427 (line)]] | wt | 44.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 85.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.383× (z -9.0) |
| [[HCT15 (line)]] | alt | 146 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.82× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 115 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -16.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 34.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.35× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 51.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +10.7) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.52× (z +9.1) | — |
| [[RKO (line)]] | wt | 67.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.90× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 60.4 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.155× (z -9.8) |
| [[C-33 A (line)]] | alt | 70.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 90.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 53.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 59.3 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.21× (z +8.9) ⚠ unreliable plate only | — |
| [[HS-578T (line)]] | alt | 73.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.55× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 79.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 36.7 | 0 | 1 | — | [[PF-06260933 (drug)]] 5 µM 0.114× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 43.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +8.9) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[SNU-423 (line)]] | alt | 35.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +10.3) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[A-172 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 63.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1717), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDOR1]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ZNF718]] | +0.64 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[SUV39H2]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[CENPO]] | +0.63 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[NUP155]] | +0.61 | +0.72 / +0.55 | both halves | 1e-05 | same gene group; pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 967 |
| [[DDIAS]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[TOR1A]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[UTP4]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[XRCC3]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[CDC25A]] | +0.59 | +0.56 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[XRCC2]] | +0.59 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[TRAPPC10]] | +0.59 | +0.66 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM167B]] | -0.62 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[GOLGA4]] | -0.61 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[SEC11C]] | -0.60 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[KRT10]] ⚠ | -0.59 | -0.61 / -0.54 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SLC41A2]] | -0.58 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[SAT2]] | -0.58 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[UBE2B]] | -0.57 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[CDKN1C]] | -0.57 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[PIM3]] | -0.57 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[MAK]] | -0.56 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[HADHB]] | -0.56 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[SNHG8]] | -0.56 | -0.59 / -0.57 | both halves | 9e-06 |  |
| [[ATF4]] | -0.55 | -0.58 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MDFI]] | B | MDFI activity raises NUP50's level | lines that do not express MDFI (25) vs lines expressing it (25) | 1.60× lower at baseline in the lines without MDFI | 0.026 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises NUP50's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.579). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.9, -43.5); signed map (-37.7, -49.3). **Vector** length 106, 28.2% of its response variance represented; |z| ≥ 3 in 1,227 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +5.9 | +6.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.3 | +4.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.3 | +13.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +12.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +8.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.4 | +1.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.2 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.0 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -6.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +1.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.5 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -2.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | nucleoporin 50 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:45,163,925-45,188,017 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously NPAP60L |
| Gene groups (HGNC) | Nucleoporins |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 69 pathways, smallest: IP3 and IP4 transport between cytosol and nucleus; IP6 and IP7 transport between cytosol and nucleus; IPs transport between nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKX7](https://www.uniprot.org/uniprotkb/Q9UKX7) (Nuclear pore complex protein Nup50):

> Component of the nuclear pore complex that has a direct role in nuclear protein import. Actively displaces NLSs from importin-alpha, and facilitates disassembly of the importin-alpha:beta-cargo complex and importin recycling. Interacts with regulatory proteins of cell cycle progression including CDKN1B (By similarity). This interaction is required for correct intracellular transport and degradation of CDKN1B (By similarity).

**Summary**, from NCBI Gene [10762](https://www.ncbi.nlm.nih.gov/gene/10762):

> The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. The protein encoded by this gene is a member of the FG-repeat containing nucleoporins that functions as a soluble cofactor in importin-alpha:beta-mediated nuclear protein import. Pseudogenes of this gene are found on …

**Accessions** — [HGNC:8065](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8065) · Entrez [10762](https://www.ncbi.nlm.nih.gov/gene/10762) · UniProt [Q9UKX7](https://www.uniprot.org/uniprotkb/Q9UKX7) · Ensembl [ENSG00000093000](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000093000)

## Data

Gene col 1717: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1717); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1717, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1717]; `tensor/DDL_lfc|DDL_z.npy` [1717]; `embed/gene_vectors.npy` [1717]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1717 or target_col == 1717). Every well: [[NUP50 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUP50.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
