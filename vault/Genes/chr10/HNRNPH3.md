---
symbol: "HNRNPH3"
type: "gene"
col: 1771
ensembl_id: "ENSG00000096746"
name: "heterogeneous nuclear ribonucleoprotein H3"
location: "10q21.3"
module: 3
arm: "-"
pooled_cpm: 139.11
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# HNRNPH3

*heterogeneous nuclear ribonucleoprotein H3* — 10q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.52× (z +34.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.551× (z -11.4, q 2e-27, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPU]] (+0.75, fdr 7e-06), [[HNRNPM]] (+0.72, fdr 7e-06), [[BCLAF1]] (+0.70, fdr 1e-05); moves opposite to [[MPG]] (-0.72, fdr 1e-05), [[EIF4EBP1]] (-0.70, fdr 7e-06), [[GPR89B]] (-0.68, fdr 3e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZMAT1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1771.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.52×** | +34.6 | 0e+00 | 48/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.66×** | +19.0 | 0e+00 | 48/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.46×** | +17.5 | 0e+00 | 48/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.39×** | +16.3 | 0e+00 | 46/48 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +15.5 | 0e+00 | 47/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.01×** | +13.3 | 1e-38 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.78×** | +11.1 | 1e-26 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +10.8 | 3e-25 | 44/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +10.7 | 7e-25 | 40/49 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.62×** | +9.4 | 5e-19 | 37/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.39×** | +8.9 | 4e-17 | 45/49 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +8.0 | 5e-14 | 31/44 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.20×** | +8.0 | 5e-14 | 42/48 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +6.7 | 7e-10 | 32/45 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.35×** | +5.9 | 1e-07 | 32/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +4.4 | 4e-04 | 28/48 (NCI-H460, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.5 | 0.013 | 9/48 (A-172, HOP62, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.016 | 8/49 (CFPAC-1, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.018 | 20/48 (PANC-1, SNU-423, …) | rises with dose |  |
| [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.023 | 19/48 (A-172, A549, …) | inconsistent across doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.056 | 14/48 (CFPAC-1, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1771.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.551×** | -11.4 | 2e-27 | 48/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.623×** | -9.2 | 9e-18 | 44/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.643×** | -8.6 | 1e-15 | 38/48 (SW480, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.754×** | -5.5 | 5e-06 | 33/48 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.865× | -4.0 | 0.007 | 17/48 (SW480, HOP62, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.699×** | -3.6 | 0.023 | 28/49 (SW480, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.830×** | -3.6 | 0.023 | 23/49 (NCI-H2347, LoVo, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.714×** | -3.4 | 0.043 | 25/47 (A-427, NCI-H23, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | 0.845× | -3.3 | 0.063 | 19/48 (HCT15, J82, …) | rises with dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.893× | -3.1 | 0.097 | 6/48 (hTERT-HPNE, J82, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | 0.854× | -3.1 | 0.11 | 15/48 (SNU-423, hTERT-HPNE, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.897× | -3.0 | 0.12 | 11/48 (RKO, J82, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1771. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 180 | 13 (5 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +18.6) | [[Panobinostat (drug)]] 5 µM 0.434× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 152 | 15 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +28.5) | — |
| [[NCI-H1573 (line)]] | alt | 112 | 11 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +32.6) | [[Panobinostat (drug)]] 0.5 µM 0.473× (z -8.8) |
| [[PANC-1 (line)]] | alt | 165 | 12 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +29.1) | — |
| [[A-172 (line)]] | wt | 120 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +25.2) | — |
| [[LoVo (line)]] | wt | 110 | 9 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +33.8) | [[Panobinostat (drug)]] 0.5 µM 0.537× (z -9.6) |
| [[A549 (line)]] | wt | 135 | 9 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +31.8) | [[Panobinostat (drug)]] 0.5 µM 0.502× (z -8.5) |
| [[HOP62 (line)]] | alt | 122 | 7 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +25.2) | [[Panobinostat (drug)]] 5 µM 0.405× (z -11.9) |
| [[KATO III (line)]] | alt | 103 | 10 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.17× (z +21.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 116 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +19.2) | — |
| [[A498 (line)]] | wt | 122 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +30.2) | — |
| [[HEC-1-A (line)]] | alt | 171 | 6 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +22.8) | [[Panobinostat (drug)]] 0.5 µM 0.384× (z -13.4) |
| [[LS 180 (line)]] | wt | 109 | 8 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.84× (z +18.0) | [[Panobinostat (drug)]] 0.5 µM 0.447× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 110 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +19.3) | — |
| [[hTERT-HPNE (line)]] | wt | 125 | 5 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +25.0) | [[Panobinostat (drug)]] 5 µM 0.406× (z -10.3) |
| [[J82 (line)]] | alt | 113 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +21.5) | — |
| [[NCI-H23 (line)]] | alt | 170 | 6 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +21.4) | [[Panobinostat (drug)]] 5 µM 0.432× (z -11.6) |
| [[SW 900 (line)]] | alt | 189 | 6 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +22.2) | [[Panobinostat (drug)]] 0.5 µM 0.420× (z -9.6) |
| [[SW48 (line)]] | wt | 179 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +19.0) | — |
| [[HS-578T (line)]] | alt | 84.9 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +20.8) | — |
| [[HT-29 (line)]] | alt | 95.2 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +22.9) | — |
| [[AsPC-1 (line)]] | alt | 128 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.54× (z +26.5) | — |
| [[BT-474 (line)]] | alt | 139 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +22.0) | — |
| [[CFPAC-1 (line)]] | alt | 144 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +25.0) | [[Panobinostat (drug)]] 0.5 µM 0.498× (z -8.6) |
| [[H4 (line)]] | wt | 135 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +14.3) | — |
| [[HCT15 (line)]] | alt | 163 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +16.9) | — |
| [[HepG2_C3A (line)]] | wt | 145 | 4 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +18.4) | [[Belinostat (drug)]] 5 µM 0.426× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 136 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +20.9) | [[Panobinostat (drug)]] 0.5 µM 0.436× (z -10.4) |
| [[SNU-423 (line)]] | alt | 129 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +25.6) | — |
| [[COLO 205 (line)]] | alt | 80.2 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +20.9) | — |
| [[LOX-IMVI (line)]] | wt | 128 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +18.4) | — |
| [[A-427 (line)]] | wt | 176 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.436× (z -10.7) |
| [[Hs 766T (line)]] | wt | 97.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +17.1) | — |
| [[SK-MEL-2 (line)]] | alt | 123 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +21.9) | — |
| [[SW1417 (line)]] | alt | 141 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +18.4) | — |
| [[NCI-H2347 (line)]] | alt | 174 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +14.6) | — |
| [[RKO (line)]] | wt | 142 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +21.0) | — |
| [[RPMI-7951 (line)]] | alt | 131 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +18.8) | — |
| [[C-33 A (line)]] | alt | 186 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +9.5) | — |
| [[C32 (line)]] | wt | 118 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +19.7) | — |
| [[NCI-H2030 (line)]] | alt | 228 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.0) | — |
| [[SNU-1 (line)]] | wt | 146 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +11.7) | — |
| [[AN3 CA (line)]] | alt | 213 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.1) | — |
| [[SW 1088 (line)]] | alt | 131 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +8.8) | — |
| [[CHP-212 (line)]] | wt | 156 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 88.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 127 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1771), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPU]] | +0.75 | +0.74 / +0.63 | both halves | 7e-06 | same gene group; STRING 826 |
| [[HNRNPM]] | +0.72 | +0.66 / +0.75 | both halves | 7e-06 | same gene group; STRING 945 |
| [[BCLAF1]] | +0.70 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[HNRNPK]] | +0.68 | +0.49 / +0.63 | both halves | 1e-05 | same gene group; STRING 809 |
| [[EWSR1]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 | same gene group; STRING 496 |
| [[HMGN2]] | +0.67 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[HNRNPD]] | +0.66 | +0.53 / +0.74 | both halves | 1e-05 | same gene group; STRING 918 |
| [[ACADM]] | +0.66 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[CYB5D2]] | +0.66 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[FUBP1]] | +0.65 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ZMYND11]] | +0.65 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[WAC-AS1]] | +0.65 | +0.58 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPG]] | -0.72 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[EIF4EBP1]] | -0.70 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[GPR89B]] | -0.68 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[MYO9B]] | -0.66 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[YIF1B]] | -0.63 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[SLC35E1]] | -0.62 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[TBC1D20]] | -0.62 | -0.42 / -0.66 | both halves | 4e-05 |  |
| [[GP6-AS1]] | -0.62 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[RBAK-RBAKDN]] | -0.61 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[MTF1]] | -0.61 | -0.34 / -0.67 | both halves | 1e-04 |  |
| [[GPR89A]] | -0.61 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[DHDDS]] | -0.61 | -0.52 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZMAT1]] | B | ZMAT1 activity raises HNRNPH3's level | lines that do not express ZMAT1 (18) vs lines expressing it (32) | 1.29× lower at baseline in the lines without ZMAT1 | 0.014 | ⚠ within organs, on part of the lines; also absent: NTN1, C19orf81, LMX1B |
| [[HDAC6]] | B | HDAC6 activity raises HNRNPH3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ARHGEF17]] | C | ARHGEF17 activity raises HNRNPH3's level | lines that do not express ARHGEF17 (4) vs lines expressing it (46) | 1.41× lower at baseline in the lines without ARHGEF17 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RGS10; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.671). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-3.0, 4.3); signed map (14.8, -37.3). **Vector** length 103, 35.8% of its response variance represented; |z| ≥ 3 in 1,317 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA 3'-end processing* (reactome, mean cos +0.58 to 12); *mRNA Polyadenylation* (reactome, mean cos +0.58 to 11); *mRNA Splicing - Major Pathway* (reactome, mean cos +0.57 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.9 | +10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.8 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.8 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +34.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +19.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.3 | +0.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.2 | -0.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -7.0 | -11.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.6 | -8.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.8 | -9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -1.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.9 | -0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.6 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | +3.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.9 | -3.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.8 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | heterogeneous nuclear ribonucleoprotein H3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.3 — chr10:68,331,174-68,343,193 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 2H9; previously HNRPH3 |
| Gene groups (HGNC) | RNA binding motif containing; Heterogeneous nuclear ribonucleoproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P31942](https://www.uniprot.org/uniprotkb/P31942) (Heterogeneous nuclear ribonucleoprotein H3):

> Involved in the splicing process and participates in early heat shock-induced splicing arrest. Due to their great structural variations the different isoforms may possess different functions in the splicing reaction.

**Summary**, from NCBI Gene [3189](https://www.ncbi.nlm.nih.gov/gene/3189):

> This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in the nucleus, some seem to shuttle between the nucleus and the cytoplasm. The hnRNP proteins have …

**Accessions** — [HGNC:5043](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5043) · Entrez [3189](https://www.ncbi.nlm.nih.gov/gene/3189) · UniProt [P31942](https://www.uniprot.org/uniprotkb/P31942) · Ensembl [ENSG00000096746](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000096746)

## Data

Gene col 1771: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1771); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1771, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1771]; `tensor/DDL_lfc|DDL_z.npy` [1771]; `embed/gene_vectors.npy` [1771]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1771 or target_col == 1771). Every well: [[HNRNPH3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPH3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
