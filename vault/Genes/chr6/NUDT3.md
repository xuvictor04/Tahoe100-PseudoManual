---
symbol: "NUDT3"
type: "gene"
col: 15716
ensembl_id: "ENSG00000272325"
name: "nudix hydrolase 3"
location: "6p21.31"
module: 18
arm: "+"
pooled_cpm: 104.08
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# NUDT3

*nudix hydrolase 3* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 1.71× (z +14.6, q 3e-45, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.714× (z -9.1, q 5e-17, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMTC4]] (+0.70, fdr 7e-06), [[UBE2G2]] (+0.66, fdr 7e-06), [[GART]] (+0.66, fdr 7e-06); moves opposite to [[NRBF2]] (-0.64, fdr 7e-06), [[MFAP1]] (-0.63, fdr 7e-06), [[CREB3]] (-0.62, fdr 7e-06).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ADCY3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15716.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **1.71×** | +14.6 | 3e-45 | 44/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +13.6 | 9e-40 | 41/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +13.0 | 2e-36 | 42/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +12.7 | 2e-34 | 42/47 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +11.6 | 8e-29 | 42/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +10.6 | 4e-24 | 33/45 (C32, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.00×** | +9.8 | 1e-20 | 37/48 (RKO, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.39×** | +8.8 | 8e-17 | 32/49 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.37×** | +8.6 | 5e-16 | 28/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +8.5 | 1e-15 | 32/48 (RPMI-7951, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +7.8 | 3e-13 | 29/44 (LoVo, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.57×** | +6.4 | 7e-09 | 31/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.25×** | +6.1 | 4e-08 | 25/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +6.0 | 1e-07 | 26/48 (KATO III, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +5.9 | 1e-07 | 23/38 (SNU-1, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +5.5 | 1e-06 | 24/48 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +4.8 | 5e-05 | 21/48 (MIA PaCa-2, A-427, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.40×** | +4.7 | 7e-05 | 18/49 (C-33 A, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.14× | +3.5 | 0.013 | 7/48 (NCI-H460, hTERT-HPNE, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.14× | +3.4 | 0.015 | 16/48 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.021 | 5/49 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15716.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.714×** | -9.1 | 5e-17 | 28/48 (PANC-1, A-427, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.758×** | -7.5 | 2e-11 | 27/48 (PANC-1, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.830×** | -7.1 | 2e-10 | 22/48 (SW1417, LS 180, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.791×** | -6.3 | 3e-08 | 24/48 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.818×** | -3.9 | 0.011 | 16/48 (A498, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.905× | -3.8 | 0.013 | 17/48 (PANC-1, J82, …) | rises with dose | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.879× | -3.5 | 0.038 | 14/49 (KATO III, RKO, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.877× | -3.4 | 0.041 | 11/48 (SW 1088, SW480, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.915× | -3.4 | 0.041 | 3/48 (hTERT-HPNE, Hs 766T, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.918× | -3.3 | 0.054 | 12/48 (A-427, PANC-1, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains <1% of this change | 0.886× | -3.3 | 0.054 | 12/48 (SW 1088, RKO, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.888× | -3.2 | 0.065 | 17/48 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.889× | -3.2 | 0.067 | 13/49 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.893× | -3.1 | 0.086 | 12/47 (Hs 766T, LoVo, …) | rises with dose |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.894× | -3.0 | 0.094 | 5/48 (SW 900, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15716. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 91.1 | 8 (3 ⚠) | 2 | [[Digitoxin (drug)]] 0.5 µM 2.19× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.547× (z -9.4) |
| [[PANC-1 (line)]] | alt | 175 | 3 | 6 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 2.57× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.379× (z -19.6) |
| [[SW480 (line)]] | alt | 130 | 9 (4 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.18× (z +12.3) | — |
| [[LoVo (line)]] | wt | 75.7 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +13.4) | — |
| [[A-427 (line)]] | wt | 154 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.459× (z -12.8) |
| [[LS 180 (line)]] | wt | 71.5 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.90× (z +14.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 159 | 1 | 3 | [[PH-797804 (drug)]] 5 µM 4.17× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.373× (z -12.3) |
| [[SW1417 (line)]] | alt | 96.1 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.428× (z -11.5) |
| [[COLO 205 (line)]] | alt | 41.3 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.45× (z +11.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.97× (z +11.2) | — |
| [[KATO III (line)]] | alt | 73.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.33× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 162 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.412× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 89.3 | 3 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.45× (z +9.6) ⚠ toxic | — |
| [[NCI-H2030 (line)]] | alt | 184 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.423× (z -9.9) |
| [[RKO (line)]] | wt | 165 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.91× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -15.5) ⚠ cell-cycle shift, explains ~10% of this change |
| [[SNU-423 (line)]] | alt | 99.1 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 61.8 | 2 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C32 (line)]] | wt | 103 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.71× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 95.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 46.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 115 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.433× (z -11.0) |
| [[A498 (line)]] | wt | 64.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 52.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +8.9) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 73.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.88× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 116 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HT-29 (line)]] | alt | 72.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +10.4) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 74.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 159 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.528× (z -9.5) |
| [[SNU-1 (line)]] | wt | 196 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -15.0) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 89.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.132× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~6% of this change |
| [[SW48 (line)]] | wt | 140 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.374× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 71.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 215 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 194 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 114 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 71.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 60.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15716), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMTC4]] | +0.70 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[UBE2G2]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[GART]] | +0.66 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[LARP1]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[SENP3]] | +0.64 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[ABCC4]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[USP45]] | +0.63 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[PEMT]] | +0.63 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[MDN1]] | +0.63 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[CPSF6]] | +0.63 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[HACD3]] | +0.62 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[UCK2]] | +0.62 | +0.75 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRBF2]] | -0.64 | -0.58 / -0.69 | both halves | 7e-06 |  |
| [[MFAP1]] | -0.63 | -0.58 / -0.68 | both halves | 7e-06 |  |
| [[CREB3]] | -0.62 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[NOSIP]] | -0.61 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[CTR9]] | -0.61 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[TRAPPC2B]] | -0.61 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[TMF1]] | -0.59 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[IL10RB]] | -0.58 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[SPTY2D1]] | -0.58 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[SELENOM]] | -0.58 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[BTG1]] | -0.58 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[TCEAL8]] | -0.58 | -0.47 / -0.64 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY3]] | B | ADCY3 activity raises NUDT3's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.36× lower at baseline in the lines without ADCY3 | 0.027 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[HDAC6]] | B | HDAC6 activity raises NUDT3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LAMB1]] | B | LAMB1 activity lowers NUDT3's level | lines that do not express LAMB1 (7) vs lines expressing it (43) | 1.88× higher at baseline in the lines without LAMB1 | 0.079 | ⚠ within organs, on part of the lines; also absent: TGFBR2, SDC4, VDR |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.735). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.0, -35.0); signed map (-10.5, -42.4). **Vector** length 119, 35.9% of its response variance represented; |z| ≥ 3 in 1,218 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +10.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.9 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +8.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.9 | +5.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +0.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.2 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +3.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.6 | +0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +9.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.2 | -3.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | -2.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.5 | -7.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.4 | -1.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.7 | -3.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.5 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -0.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | nudix hydrolase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:34,279,679-34,392,669 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DIPP |
| Gene groups (HGNC) | Nudix hydrolase family |
| Reactome | 2 pathways, smallest: Synthesis of pyrophosphates in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O95989](https://www.uniprot.org/uniprotkb/O95989) (Diphosphoinositol polyphosphate phosphohydrolase 1):

> Cleaves a beta-phosphate from the diphosphate groups in PP-InsP5 (diphosphoinositol pentakisphosphate) and [PP]2-InsP4 (bisdiphosphoinositol tetrakisphosphate), suggesting that it may play a role in signal transduction. InsP6 (inositol hexakisphosphate) is not a substrate. Acts as a negative regulator of the ERK1/2 pathway (By similarity). Also able to catalyze the hydrolysis of dinucleoside oligophosphates, with diadenosine 5',5'''-P1,P6-hexaphosphate (Ap6A) and diadenosine 5',5'''- …

**Summary**, from NCBI Gene [11165](https://www.ncbi.nlm.nih.gov/gene/11165):

> NUDT3 belongs to the MutT, or Nudix, protein family. Nudix proteins act as homeostatic checkpoints at important stages in nucleoside phosphate metabolic pathways, guarding against elevated levels of potentially dangerous intermediates, like 8-oxo-dGTP, which promotes AT-to-CG transversions (Safrany et al., 1998 [PubMed 9822604]).[supplied by OMIM, Feb 2011]

**Accessions** — [HGNC:8050](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8050) · Entrez [11165](https://www.ncbi.nlm.nih.gov/gene/11165) · UniProt [O95989](https://www.uniprot.org/uniprotkb/O95989) · Ensembl [ENSG00000272325](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000272325)

## Data

Gene col 15716: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15716); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15716, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15716]; `tensor/DDL_lfc|DDL_z.npy` [15716]; `embed/gene_vectors.npy` [15716]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15716 or target_col == 15716). Every well: [[NUDT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
