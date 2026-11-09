---
symbol: "FSTL1"
type: "gene"
col: 8689
ensembl_id: "ENSG00000163430"
name: "follistatin like 1"
location: "3q13.33"
module: 29
arm: "+"
pooled_cpm: 68.35
n_lines_expressing: 29
n_dd_up: 22
n_dd_down: 18
n_dd_up_clean: 17
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 14
direction_downstream: 11
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# FSTL1

*follistatin like 1* — 3q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.14× (z +15.1, q 0e+00, up in 25 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.26× (z +4.4, q 0.001, up in 14 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.354× (z -20.1, q 0e+00, down in 25 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMP2]] (+0.67, fdr 1e-05), [[POSTN]] (+0.66, fdr 1e-05), [[CTSZ]] (+0.66, fdr 2e-05); moves opposite to [[SMIM26]] (-0.57, fdr 3e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[MPHOSPH10]] (-0.56, fdr 7e-05), [[ZNF593]] (-0.55, fdr 5e-05), [[MRPS18B]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 11 go from it, the strongest it → [[TARS2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8689.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.14×** | +15.1 | 0e+00 | 25/26 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.12×** | +15.0 | 0e+00 | 20/22 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.82×** | +13.2 | 3e-37 | 24/25 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.40×** | +4.6 | 5e-04 | 16/26 (NCI-H1573, NCI-H460, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.4 | 0.001 | 14/27 (A-172, HOP62, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.35×** | +4.1 | 0.004 | 14/27 (NCI-H1573, NCI-H460, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.005 | 10/27 (NCI-H1792, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.006 | 10/27 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.33×** | +3.8 | 0.009 | 14/26 (SK-MEL-2, A-172, …) | two highest doses | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.011 | 15/26 (NCI-H1573, NCI-H460, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.021 | 13/27 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.030 | 14/27 (BT-474, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.030 | 9/26 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.035 | 11/27 (SK-MEL-2, A-172, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.041 | 8/27 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.064 | 11/26 (A-172, SK-MEL-2, …) | two highest doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.064 | 12/27 (SK-MEL-2, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.064 | 6/26 (NCI-H460, HOP62, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.075 | 6/27 (Hs 766T, RPMI-7951, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.081 | 11/26 (NCI-H460, NCI-H1573, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, none with an alert; shown: the 15 strongest. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8689.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.354×** | -20.1 | 0e+00 | 25/27 (Hs 766T, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.381×** | -13.2 | 1e-37 | 25/27 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.368×** | -13.2 | 2e-37 | 24/27 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.440×** | -11.3 | 3e-27 | 24/27 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.453×** | -10.9 | 2e-25 | 23/27 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.513×** | -9.2 | 4e-18 | 21/27 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.557×** | -8.0 | 8e-14 | 23/27 (LOX-IMVI, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.581×** | -7.2 | 5e-11 | 21/27 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.615×** | -6.7 | 2e-09 | 20/27 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.730×** | -4.3 | 9e-04 | 13/27 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.596×** | -3.7 | 0.011 | 11/27 (NCI-H460, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.778×** | -3.5 | 0.026 | 15/27 (H4, HOP62, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.710×** | -3.4 | 0.035 | 14/26 (hTERT-HPNE, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.788×** | -3.3 | 0.042 | 10/27 (HOP62, NCI-H460, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.640×** | -3.2 | 0.051 | 12/27 (H4, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8689. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 98.4 | 1 (1 ⚠) | 7 | [[Dinaciclib (drug)]] 5 µM 3.12× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -19.7) |
| [[A-172 (line)]] | wt | 487 | 5 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.80× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -15.4) |
| [[H4 (line)]] | wt | 268 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -23.8) |
| [[NCI-H460 (line)]] | wt | 34.4 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -20.6) |
| [[HOP62 (line)]] | alt | 198 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.95× (z +14.2) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.189× (z -14.9) |
| [[SNU-423 (line)]] | alt | 108 | 5 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.32× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -11.5) |
| [[A498 (line)]] | wt | 181 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.97× (z +13.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -16.5) |
| [[Hs 766T (line)]] | wt | 166 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0907× (z -24.3) |
| [[J82 (line)]] | alt | 292 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.09× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -20.2) |
| [[Panc 03.27 (line)]] | alt | 62.2 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +9.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -11.9) |
| [[HS-578T (line)]] | alt | 213 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -12.4) |
| [[hTERT-HPNE (line)]] | wt | 250 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 40.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -13.1) |
| [[RPMI-7951 (line)]] | alt | 128 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.93× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -14.1) |
| [[A549 (line)]] | wt | 44.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -16.2) |
| [[SK-MEL-2 (line)]] | alt | 34.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -20.8) |
| [[SNU-1 (line)]] | wt | 46.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -10.6) |
| [[AN3 CA (line)]] | alt | 88.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -15.7) |
| [[C-33 A (line)]] | alt | 40.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 17.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -9.5) |
| [[SW 1088 (line)]] | alt | 133 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0274× (z -12.3) |
| [[BT-474 (line)]] | alt | 31.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.157× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 73.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 31.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -15.7) |
| [[NCI-H661 (line)]] | alt | 30.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -8.5) |
| [[A-427 (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.99 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.92 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.05 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.21 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.59 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.68 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.13 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.29 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.18 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.86 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.58 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.24 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8689), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMP2]] | +0.67 | +0.57 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 430 |
| [[POSTN]] | +0.66 | +0.64 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_ANGIOGENESIS; STRING 450 |
| [[CTSZ]] | +0.66 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[TMEM30A]] | +0.64 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[SELENON]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[PGRMC1]] | +0.63 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[ADAM9]] | +0.62 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[LAMC1]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 557 |
| [[COL3A1]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 | same gene group; pathway: HALLMARK_ANGIOGENESIS; STRING 605 |
| [[ANTXR1]] | +0.60 | +0.49 / +0.54 | both halves | 1e-05 | same gene group |
| [[ERAP1]] | +0.59 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[DHFR]] | +0.59 | +0.37 / +0.57 | both halves | 7e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | -0.57 | -0.43 / -0.56 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MPHOSPH10]] | -0.56 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[ZNF593]] | -0.55 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[MRPS18B]] | -0.55 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[RPP21]] | -0.54 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[RBMX2]] | -0.54 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[SNHG7]] | -0.53 | -0.37 / -0.53 | both halves | 9e-05 |  |
| [[MTLN]] ⚠ | -0.53 | -0.31 / -0.49 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[LEO1]] | -0.53 | -0.31 / -0.54 | both halves | 2e-04 |  |
| [[TARS2]] | -0.53 | -0.37 / -0.52 | both halves | 8e-05 | same gene group |
| [[RP9]] | -0.53 | -0.36 / -0.57 | both halves | 9e-05 |  |
| [[MT1X]] | -0.53 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[ATF4]] | -0.53 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[SIRT6]] | -0.52 | -0.39 / -0.49 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 1, C 13. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers FSTL1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DKK3]] | C | DKK3 activity raises FSTL1's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 5.54× lower at baseline in the lines without DKK3 | 0.005 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1; co-absent with the target |
| [[C5orf46]] | C | C5orf46 activity raises FSTL1's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 4.97× lower at baseline in the lines without C5orf46 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[POSTN]] | C | POSTN activity raises FSTL1's level | lines that do not express POSTN (38) vs lines expressing it (12) | 5.14× lower at baseline in the lines without POSTN | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1; co-absent with the target |
| [[PTN]] | C | PTN activity raises FSTL1's level | lines that do not express PTN (28) vs lines expressing it (22) | 5.22× lower at baseline in the lines without PTN | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC; co-absent with the target |
| [[NID2]] | C | NID2 activity raises FSTL1's level | lines that do not express NID2 (32) vs lines expressing it (18) | 4.27× lower at baseline in the lines without NID2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1; co-absent with the target |
| [[SPARC]] | C | SPARC activity raises FSTL1's level | lines that do not express SPARC (34) vs lines expressing it (16) | 5.74× lower at baseline in the lines without SPARC | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032; co-absent with the target |
| [[FBN1]] | C | FBN1 activity raises FSTL1's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 4.49× lower at baseline in the lines without FBN1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241; co-absent with the target |
| [[ITGA4]] | C | ITGA4 activity raises FSTL1's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 5.01× lower at baseline in the lines without ITGA4 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[THY1]] | C | THY1 activity raises FSTL1's level | lines that do not express THY1 (38) vs lines expressing it (12) | 5.19× lower at baseline in the lines without THY1 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TMPRSS15, DCN, COL11A1; co-absent with the target |
| [[MMP2]] | C | MMP2 activity raises FSTL1's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 4.59× lower at baseline in the lines without MMP2 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L; co-absent with the target |
| [[LDOC1]] | C | LDOC1 activity raises FSTL1's level | lines that do not express LDOC1 (21) vs lines expressing it (29) | 4.05× lower at baseline in the lines without LDOC1 | 0.070 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, S1PR3, SNAP91; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 5, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TARS2]] | B | FSTL1 activity lowers TARS2's level | lines that do not express FSTL1 (21) vs lines expressing it (29) | 1.17× higher at baseline in the lines without FSTL1 | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC8A1, ABI3BP, TFPI2 |
| [[CDK2AP1]] | B | FSTL1 activity raises CDK2AP1's level | lines that do not express FSTL1 (21) vs lines expressing it (29) | 1.00× lower at baseline in the lines without FSTL1 | 0.057 | ⚠ within organs, on part of the lines; also absent: SLC8A1, ABI3BP, TFPI2 |
| [[NTHL1]] | B | FSTL1 activity lowers NTHL1's level | lines that do not express FSTL1 (21) vs lines expressing it (29) | 1.34× higher at baseline in the lines without FSTL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC8A1, ABI3BP, TFPI2 |
| [[EPB41L4A-AS1]] | B | FSTL1 activity raises EPB41L4A-AS1's level | lines that do not express FSTL1 (21) vs lines expressing it (29) | 1.09× lower at baseline in the lines without FSTL1 | 0.075 | ⚠ within organs, on part of the lines; also absent: SLC8A1, ABI3BP, TFPI2 |
| [[ZNF593]] | B | FSTL1 activity lowers ZNF593's level | lines that do not express FSTL1 (21) vs lines expressing it (29) | 1.36× higher at baseline in the lines without FSTL1 | 0.084 | ⚠ within organs, on part of the lines; also absent: SLC8A1, ABI3BP, TFPI2 |
| [[NID2]] | C | FSTL1 activity raises NID2's level | lines that do not express FSTL1 (21) vs lines expressing it (29) | 2.95× lower at baseline in the lines without FSTL1 | 0.031 | ⚠ within organs, on part of the lines; also absent: SLC8A1, ABI3BP, TFPI2; co-absent with the target |
| [[DKK3]] | C | FSTL1 activity raises DKK3's level | lines that do not express FSTL1 (21) vs lines expressing it (29) | 4.42× lower at baseline in the lines without FSTL1 | 0.045 | ⚠ within organs, on part of the lines; also absent: SLC8A1, ABI3BP, TFPI2; co-absent with the target |
| [[COL12A1]] | C | FSTL1 activity raises COL12A1's level | lines that do not express FSTL1 (21) vs lines expressing it (29) | 5.58× lower at baseline in the lines without FSTL1 | 0.065 | ⚠ within organs, on part of the lines; also absent: SLC8A1, ABI3BP, TFPI2; co-absent with the target |
| [[PTN]] | C | FSTL1 activity raises PTN's level | lines that do not express FSTL1 (21) vs lines expressing it (29) | 3.67× lower at baseline in the lines without FSTL1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SLC8A1, ABI3BP, TFPI2; co-absent with the target |
| [[C5orf46]] | C | FSTL1 activity raises C5orf46's level | lines that do not express FSTL1 (21) vs lines expressing it (29) | 1.82× lower at baseline in the lines without FSTL1 | 0.079 | ⚠ within organs, on part of the lines; also absent: SLC8A1, ABI3BP, TFPI2; co-absent with the target |
| [[MMP2]] | C | FSTL1 activity raises MMP2's level | lines that do not express FSTL1 (21) vs lines expressing it (29) | 5.11× lower at baseline in the lines without FSTL1 | 0.083 | ⚠ within organs, on part of the lines; also absent: SLC8A1, ABI3BP, TFPI2; co-absent with the target |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.607). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (57.3, 23.0); signed map (44.9, -8.7). **Vector** length 104, 31.4% of its response variance represented; |z| ≥ 3 in 851 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +10.3 | +13.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.2 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.4 | +15.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +4.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.0 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +0.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.8 | +3.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.5 | -13.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -7.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.1 | -1.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.1 | -2.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | follistatin like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.33 — chr3:120,392,293-120,451,016 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FRP, FSL1, OCC1, OCC-1, tsc36 |
| Gene groups (HGNC) | SPARC family; MicroRNA protein coding host genes |
| Hallmark sets | ANGIOGENESIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 4 pathways, smallest: Signaling by BMP; Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12841](https://www.uniprot.org/uniprotkb/Q12841) (Follistatin-related protein 1):

> Secreted glycoprotein that is involved in various physiological processes, such as angiogenesis, regulation of the immune response, cell proliferation and differentiation. Plays a role in the development of the central nervous system, skeletal system, lungs, and ureter (By similarity). Promotes endothelial cell survival, migration and differentiation into network structures in an AKT-dependent manner. Also promotes survival of cardiac myocytes (By similarity). Initiates various signaling …

**Summary**, from NCBI Gene [11167](https://www.ncbi.nlm.nih.gov/gene/11167):

> This gene encodes a protein with similarity to follistatin, an activin-binding protein. It contains an FS module, a follistatin-like sequence containing 10 conserved cysteine residues. This gene product is thought to be an autoantigen associated with rheumatoid arthritis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3972](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3972) · Entrez [11167](https://www.ncbi.nlm.nih.gov/gene/11167) · UniProt [Q12841](https://www.uniprot.org/uniprotkb/Q12841) · Ensembl [ENSG00000163430](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163430)

## Data

Gene col 8689: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8689); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8689, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8689]; `tensor/DDL_lfc|DDL_z.npy` [8689]; `embed/gene_vectors.npy` [8689]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8689 or target_col == 8689). Every well: [[FSTL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FSTL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
