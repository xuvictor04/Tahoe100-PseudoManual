---
symbol: "TNNI3K"
type: "gene"
col: 3838
ensembl_id: "ENSG00000116783"
name: "TNNI3 interacting kinase"
location: "1p31.1"
module: 37
arm: "+"
pooled_cpm: 11.91
n_lines_expressing: 47
n_dd_up: 17
n_dd_down: 31
n_dd_up_clean: 16
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 6
direction_downstream: 10
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# TNNI3K

*TNNI3 interacting kinase* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.76× (z +5.5, q 3e-05, up in 27 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (14 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.240× (z -14.2, q 3e-43, down in 41 of 44 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.436× (z -8.3, q 9e-15, down in 31 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C21orf62-AS1]] (+0.60, fdr 7e-06), [[MGAM]] (+0.58, fdr 1e-05), [[LINC02680]] (+0.57, fdr 1e-05); moves opposite to [[FAM3C]] (-0.48, fdr 9e-05), [[SOX13]] (-0.44, fdr 4e-04), [[MMP15]] (-0.44, fdr 3e-04).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 10 go from it, the strongest it → [[FPGT]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3838.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.76×** | +5.5 | 3e-05 | 27/41 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +5.2 | 7e-05 | 17/41 (SK-MEL-2, HT-29, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.64×** | +5.1 | 7e-05 | 23/43 (HOP62, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.63×** | +4.9 | 1e-04 | 19/43 (SK-MEL-2, C-33 A, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.60×** | +4.7 | 3e-04 | 22/42 (HEC-1-A, NCI-H23, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.41×** | +4.3 | 0.001 | 17/44 (SK-MEL-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.47×** | +4.3 | 0.001 | 23/45 (SK-MEL-2, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.39×** | +4.1 | 0.003 | 13/44 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.42×** | +4.1 | 0.003 | 14/43 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.37×** | +3.9 | 0.005 | 16/45 (SK-MEL-2, NCI-H460, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.50×** | +3.9 | 0.005 | 16/42 (SW480, A498, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.45×** | +3.8 | 0.007 | 15/45 (SW480, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.49×** | +3.8 | 0.008 | 11/42 (NCI-H1792, HS-578T, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.87×** | +3.3 | 0.042 | 4/43 (HEC-1-A, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.40×** | +3.2 | 0.054 | 9/43 (SK-MEL-2, SW480, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.057 | 9/45 (HEC-1-A, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3838.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.240×** | -14.2 | 3e-43 | 41/44 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.272×** | -13.0 | 4e-36 | 36/40 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.475×** | -10.5 | 2e-23 | 28/41 (CFPAC-1, A498, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.325×** | -10.5 | 2e-23 | 33/42 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.350×** | -10.1 | 8e-22 | 32/43 (NCI-H460, LS 180, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.378×** | -9.1 | 1e-17 | 36/42 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.436×** | -8.3 | 9e-15 | 31/39 (Hs 766T, C32, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.220×** | -7.9 | 2e-13 | 31/42 (NCI-H1573, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.233×** | -7.6 | 2e-12 | 32/41 (NCI-H1573, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.454×** | -7.6 | 2e-12 | 29/37 (LoVo, COLO 205, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.495×** | -7.0 | 1e-10 | 26/43 (C32, A549, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.504×** | -6.8 | 4e-10 | 35/44 (NCI-H1792, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.531×** | -6.0 | 1e-07 | 22/42 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.685×** | -5.3 | 4e-06 | 23/43 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.634×** | -4.5 | 2e-04 | 18/44 (COLO 205, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.636×** | -4.5 | 2e-04 | 19/44 (H4, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.668×** | -3.7 | 0.006 | 19/41 (SNU-423, SW48, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.693×** | -3.6 | 0.007 | 14/41 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.699×** | -3.6 | 0.010 | 16/44 (NCI-H2030, SW48, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.510×** | -3.5 | 0.012 | 14/41 (RPMI-7951, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -3.4 | 0.016 | 11/45 (SW 1088, C32, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.638×** | -3.2 | 0.033 | 9/45 (LOX-IMVI, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **0.748×** | -2.9 | 0.082 | 7/41 (SHP-77, LS 180, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.741×** | -2.9 | 0.086 | 13/41 (HT-29, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3838. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.4 | 0 | 12 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0326× (z -23.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -12.1) |
| [[C32 (line)]] | wt | 39.0 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -16.1) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0646× (z -14.6) |
| [[COLO 205 (line)]] | alt | 35.0 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -15.0) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.184× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 22.0 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0819× (z -19.1) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -11.1) |
| [[HOP62 (line)]] | alt | 11.3 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0567× (z -12.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0652× (z -11.6) |
| [[LS 180 (line)]] | wt | 11.7 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0520× (z -13.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H1573 (line)]] | alt | 23.8 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0889× (z -14.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0138× (z -13.5) |
| [[SW 900 (line)]] | alt | 12.0 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0782× (z -14.7) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0890× (z -9.8) |
| [[A498 (line)]] | wt | 32.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -18.6) ⚠ cell-cycle shift, explains ~66% of this change |
| [[A549 (line)]] | wt | 6.42 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0379× (z -12.5) |
| [[BT-474 (line)]] | alt | 25.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 14.7 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0381× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.117× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 12.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0561× (z -12.3) |
| [[RPMI-7951 (line)]] | alt | 6.47 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0338× (z -11.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0734× (z -8.5) |
| [[SNU-1 (line)]] | wt | 16.2 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0506× (z -10.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 10.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -10.5) ⚠ cell-cycle shift, explains ~66% of this change |
| [[HEC-1-A (line)]] | alt | 21.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -10.6) ⚠ cell-cycle shift, explains ~66% of this change |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0307× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0863× (z -13.9) ⚠ cell-cycle shift, explains ~66% of this change |
| [[LoVo (line)]] | wt | 11.3 | 0 | 2 (1 ⚠) | — | [[Belumosudil (drug)]] 5 µM 0.0756× (z -13.3) |
| [[NCI-H23 (line)]] | alt | 8.29 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0510× (z -10.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0694× (z -9.6) |
| [[SW480 (line)]] | alt | 6.41 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0626× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HT-29 (line)]] | alt | 5.88 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0826× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[PANC-1 (line)]] | alt | 3.72 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0866× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 9.59 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0440× (z -12.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-427 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3838), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C21orf62-AS1]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[MGAM]] | +0.58 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[LINC02680]] | +0.57 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[FRZB]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[LINC02641]] | +0.55 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[CCDC146]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ADAM20P1]] | +0.54 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[FLJ46284]] | +0.54 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[ADAM20]] | +0.54 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[CCDC30]] | +0.54 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[TNFSF13B]] | +0.53 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[RPL34-DT]] | +0.53 | +0.49 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM3C]] | -0.48 | -0.44 / -0.37 | both halves | 9e-05 |  |
| [[SOX13]] | -0.44 | -0.47 / -0.25 | both halves | 4e-04 |  |
| [[MMP15]] | -0.44 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[ACP7]] | -0.43 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[UNC5A]] | -0.42 | -0.42 / -0.25 | both halves | 4e-04 |  |
| [[TIAM1]] | -0.42 | -0.32 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers TNNI3K's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises TNNI3K's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 2.40× lower at baseline in the lines without FSIP2-AS1 | 0.054 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[ANKFN1]] | B | ANKFN1 activity raises TNNI3K's level | lines that do not express ANKFN1 (8) vs lines expressing it (42) | 1.82× lower at baseline in the lines without ANKFN1 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000214803, LINC00298; maybe low, not absent |
| [[LINC02112]] | B | LINC02112 activity raises TNNI3K's level | lines that do not express LINC02112 (6) vs lines expressing it (44) | 2.22× lower at baseline in the lines without LINC02112 | 0.066 | ⚠ within organs, on part of the lines; also absent: DNAH6, IQCM, LINC02932; maybe low, not absent |
| [[CORIN]] | C | CORIN activity raises TNNI3K's level | lines that do not express CORIN (5) vs lines expressing it (45) | 3.23× lower at baseline in the lines without CORIN | 0.060 | ⚠ within organs, on part of the lines; also absent: TNNI3K, WDR49, ENSG00000229195; maybe low, not absent; co-absent with the target; its own permutation p |
| [[C1QTNF7-AS1]] | C | C1QTNF7-AS1 activity raises TNNI3K's level | lines that do not express C1QTNF7-AS1 (3) vs lines expressing it (47) | 3.16× lower at baseline in the lines without C1QTNF7-AS1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IMPG2, ENSG00000251379, ENSG00000273184; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FPGT]] | C | TNNI3K activity raises FPGT's level | lines that do not express TNNI3K (3) vs lines expressing it (47) | 1.93× lower at baseline in the lines without TNNI3K | 0.018 | ⚠ few lines (3 vs 47); across organs; also absent: CORIN, CLEC2D, CFAP58; maybe low, not absent |
| [[NOXRED1]] | C | TNNI3K activity raises NOXRED1's level | lines that do not express TNNI3K (3) vs lines expressing it (47) | 1.85× lower at baseline in the lines without TNNI3K | 0.028 | ⚠ few lines (3 vs 47); across organs; also absent: CORIN, CLEC2D, CFAP58; maybe low, not absent |
| [[GPR135]] | C | TNNI3K activity raises GPR135's level | lines that do not express TNNI3K (3) vs lines expressing it (47) | 3.09× lower at baseline in the lines without TNNI3K | 0.041 | ⚠ few lines (3 vs 47); across organs; also absent: CORIN, CLEC2D, CFAP58; maybe low, not absent; co-absent with the target |
| [[ARMCX5-GPRASP2]] | C | TNNI3K activity weakens ARMCX5-GPRASP2's drug response | lines that do not express TNNI3K (3) vs lines expressing it (45) | the lines without TNNI3K respond 1.31× as strongly (z diff -0.70); strongest at Homoharringtonine 5 µM: 2.97x vs 1.30x (z diff -6.3) | 0.057 | ⚠ few lines (3 vs 47); across organs; also absent: CORIN, CLEC2D, CFAP58; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[ZRANB2-DT]] | C | TNNI3K activity raises ZRANB2-DT's level | lines that do not express TNNI3K (3) vs lines expressing it (47) | 2.31× lower at baseline in the lines without TNNI3K | 0.072 | ⚠ few lines (3 vs 47); across organs; also absent: CORIN, CLEC2D, CFAP58; maybe low, not absent |
| [[ECT2L]] | C | TNNI3K activity raises ECT2L's level | lines that do not express TNNI3K (3) vs lines expressing it (47) | 1.99× lower at baseline in the lines without TNNI3K | 0.088 | ⚠ few lines (3 vs 47); across organs; also absent: CORIN, CLEC2D, CFAP58; maybe low, not absent |
| [[C21orf62-AS1]] | C | TNNI3K activity raises C21orf62-AS1's level | lines that do not express TNNI3K (3) vs lines expressing it (47) | 2.68× lower at baseline in the lines without TNNI3K | 0.088 | ⚠ few lines (3 vs 47); across organs; also absent: CORIN, CLEC2D, CFAP58; maybe low, not absent |
| [[CCDC30]] | C | TNNI3K activity raises CCDC30's level | lines that do not express TNNI3K (3) vs lines expressing it (47) | 2.29× lower at baseline in the lines without TNNI3K | 0.092 | ⚠ few lines (3 vs 47); across organs; also absent: CORIN, CLEC2D, CFAP58; maybe low, not absent |
| [[SH3BGR]] | C | TNNI3K activity raises SH3BGR's level | lines that do not express TNNI3K (3) vs lines expressing it (47) | 2.14× lower at baseline in the lines without TNNI3K | 0.098 | ⚠ few lines (3 vs 47); across organs; also absent: CORIN, CLEC2D, CFAP58; maybe low, not absent |
| [[LRRC39]] | C | TNNI3K activity raises LRRC39's level | lines that do not express TNNI3K (3) vs lines expressing it (47) | 1.90× lower at baseline in the lines without TNNI3K | 0.098 | ⚠ few lines (3 vs 47); across organs; also absent: CORIN, CLEC2D, CFAP58; maybe low, not absent |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.541). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.1, -18.1); signed map (9.2, 4.4). **Vector** length 67.8, 13.2% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.5 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.5 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +5.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.3 | +4.3 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -2.2 | -3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.3 |
|  | [[vincristine (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -0.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.3 | -0.9 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.2 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | TNNI3 interacting kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:74,235,387-74,544,428 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CARK |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Mixed lineage kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q59H18](https://www.uniprot.org/uniprotkb/Q59H18) (Serine/threonine-protein kinase TNNI3K):

> May play a role in cardiac physiology.

**Summary**, from NCBI Gene [51086](https://www.ncbi.nlm.nih.gov/gene/51086):

> This gene encodes a protein that belongs to the MAP kinase kinase kinase (MAPKKK) family of protein kinases. The protein contains ankyrin repeat, protein kinase and serine-rich domains and is thought to play a role in cardiac physiology. [provided by RefSeq, Sep 2012]

**Accessions** — [HGNC:19661](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19661) · Entrez [51086](https://www.ncbi.nlm.nih.gov/gene/51086) · UniProt [Q59H18](https://www.uniprot.org/uniprotkb/Q59H18) · Ensembl [ENSG00000116783](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116783)

## Data

Gene col 3838: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3838); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3838, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3838]; `tensor/DDL_lfc|DDL_z.npy` [3838]; `embed/gene_vectors.npy` [3838]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3838 or target_col == 3838). Every well: [[TNNI3K — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNNI3K.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
