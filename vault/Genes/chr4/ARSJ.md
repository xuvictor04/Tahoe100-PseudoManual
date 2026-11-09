---
symbol: "ARSJ"
type: "gene"
col: 11131
ensembl_id: "ENSG00000180801"
name: "arylsulfatase family member J"
location: "4q26"
module: 151
arm: "+"
pooled_cpm: 46.71
n_lines_expressing: 42
n_dd_up: 13
n_dd_down: 27
n_dd_up_clean: 10
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 10
direction_downstream: 1
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# ARSJ

*arylsulfatase family member J* — 4q26

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.78× (z +17.4, q 0e+00, up in 35 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.221× (z -32.1, q 0e+00, down in 40 of 40 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EVA1A]] (+0.52, fdr 4e-05), [[CDC42EP3]] (+0.52, fdr 7e-05), [[MIR100HG]] (+0.51, fdr 1e-05); moves opposite to [[MOB2]] (-0.42, fdr 1e-04), [[ARFGEF1]] (-0.42, fdr 1e-04), [[ASS1]] (-0.41, fdr 5e-04).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[PTGS2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZNF462]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11131.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.78×** | +17.4 | 0e+00 | 35/41 (HS-578T, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +9.4 | 1e-18 | 27/40 (Hs 766T, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +6.7 | 4e-09 | 25/40 (NCI-H1573, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.74×** | +6.2 | 1e-07 | 25/40 (hTERT-HPNE, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.29×** | +5.4 | 7e-06 | 19/40 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.59×** | +5.1 | 3e-05 | 19/40 (SHP-77, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +5.0 | 5e-05 | 18/39 (RKO, HOP62, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.24×** | +4.5 | 4e-04 | 16/39 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.23×** | +4.3 | 0.001 | 15/39 (NCI-H1573, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +4.2 | 0.001 | 15/40 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.004 | 12/40 (SW 900, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.20× | +3.8 | 0.007 | 15/40 (SW480, NCI-H460, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.007 | 8/38 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.5 | 0.017 | 15/40 (NCI-H1573, HS-578T, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.062 | 9/39 (A498, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.099 | 6/40 (Hs 766T, SW 900, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11131.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.221×** | -32.1 | 0e+00 | 40/40 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.230×** | -31.2 | 0e+00 | 38/40 (A549, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.347×** | -22.5 | 0e+00 | 38/40 (A549, H4, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.476×** | -15.8 | 0e+00 | 31/37 (SW48, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.596×** | -15.5 | 0e+00 | 30/40 (A549, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.474×** | -15.2 | 0e+00 | 25/31 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.629×** | -9.8 | 6e-21 | 26/40 (A-172, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.646×** | -8.6 | 6e-16 | 23/36 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.766×** | -8.0 | 7e-14 | 19/40 (RKO, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.695×** | -7.7 | 6e-13 | 28/40 (HT-29, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.708×** | -7.3 | 1e-11 | 22/38 (CHP-212, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.754×** | -6.0 | 7e-08 | 22/40 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.749×** | -5.9 | 2e-07 | 19/39 (SNU-1, C32, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.788×** | -5.8 | 2e-07 | 23/40 (A549, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **0.625×** | -5.2 | 6e-06 | 16/36 (H4, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.828×** | -4.5 | 3e-04 | 14/40 (NCI-H460, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.810×** | -4.3 | 5e-04 | 19/40 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.819×** | -4.2 | 7e-04 | 17/40 (RKO, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.825×** | -4.1 | 0.001 | 14/40 (C32, RPMI-7951, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.693×** | -4.1 | 0.001 | 14/40 (CHP-212, A549, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.818×** | -4.0 | 0.001 | 16/40 (HS-578T, A549, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11131. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 90.8 | 1 | 11 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 6.25× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -18.3) |
| [[HS-578T (line)]] | alt | 112 | 1 | 7 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.0× (z +13.6) | [[Panobinostat (drug)]] 5 µM 0.166× (z -20.2) |
| [[C32 (line)]] | wt | 79.6 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.246× (z -13.4) |
| [[NCI-H1573 (line)]] | alt | 126 | 2 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.24× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.177× (z -16.4) |
| [[RKO (line)]] | wt | 93.4 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -19.3) |
| [[H4 (line)]] | wt | 112 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -17.6) |
| [[Hs 766T (line)]] | wt | 70.9 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.61× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.124× (z -20.0) |
| [[hTERT-HPNE (line)]] | wt | 93.8 | 2 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.8× (z +10.7) | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -17.8) |
| [[NCI-H2030 (line)]] | alt | 60.6 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.37× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.251× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 22.8 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -12.8) |
| [[A549 (line)]] | wt | 52.2 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0970× (z -20.5) |
| [[HT-29 (line)]] | alt | 95.3 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -19.2) |
| [[LoVo (line)]] | wt | 39.2 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.13× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.193× (z -16.8) |
| [[NCI-H1792 (line)]] | alt | 117 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -19.3) |
| [[RPMI-7951 (line)]] | alt | 60.1 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.149× (z -15.9) |
| [[A498 (line)]] | wt | 77.1 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 79.6 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 5.36× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -17.3) |
| [[HOP62 (line)]] | alt | 36.8 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.193× (z -14.8) |
| [[NCI-H2347 (line)]] | alt | 29.7 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.338× (z -10.6) |
| [[PANC-1 (line)]] | alt | 64.4 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 10.1× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.135× (z -17.6) |
| [[SNU-1 (line)]] | wt | 173 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.34× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.296× (z -11.0) |
| [[SNU-423 (line)]] | alt | 45.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.121× (z -17.1) |
| [[SW 900 (line)]] | alt | 54.2 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -13.9) |
| [[J82 (line)]] | alt | 34.9 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 10.5× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.230× (z -13.2) |
| [[SHP-77 (line)]] | alt | 29.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -11.3) |
| [[SW48 (line)]] | wt | 29.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.138× (z -11.1) |
| [[SW480 (line)]] | alt | 12.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -11.2) |
| [[AsPC-1 (line)]] | alt | 26.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.265× (z -9.2) |
| [[BT-474 (line)]] | alt | 39.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.174× (z -12.8) |
| [[SW 1088 (line)]] | alt | 90.3 | 0 | 2 (2 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.0791× (z -8.9) ⚠ transcription drop |
| [[CHP-212 (line)]] | wt | 50.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -8.5) |
| [[KATO III (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -11.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 13.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.234× (z -8.5) |
| [[A-427 (line)]] | wt | 5.65 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.30 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.17 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.51 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.68 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.82 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.47 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11131), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EVA1A]] | +0.52 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[CDC42EP3]] | +0.52 | +0.38 / +0.46 | both halves | 7e-05 |  |
| [[MIR100HG]] | +0.51 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[PLPP3]] | +0.48 | +0.49 / +0.31 | both halves | 2e-04 | pathway: Sphingolipid metabolism |
| [[LRRC8C]] | +0.46 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[PALM2AKAP2]] | +0.46 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[PLPP4]] | +0.45 | +0.24 / +0.45 | both halves | 5e-04 |  |
| [[AMOTL1]] | +0.45 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[HTR7]] | +0.44 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[ABL1]] | +0.44 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[SPRED1]] | +0.44 | +0.39 / +0.43 | both halves | 5e-05 |  |
| [[LINC02454]] | +0.43 | +0.41 / +0.43 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB2]] | -0.42 | -0.32 / -0.40 | both halves | 1e-04 |  |
| [[ARFGEF1]] | -0.42 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[ASS1]] | -0.41 | -0.24 / -0.46 | both halves | 5e-04 |  |
| [[YPEL2]] | -0.40 | -0.28 / -0.39 | both halves | 3e-04 |  |
| [[EPS8L2]] | -0.40 | -0.24 / -0.40 | both halves | 5e-04 |  |
| [[ABHD4]] | -0.40 | -0.24 / -0.50 | both halves | 4e-04 |  |
| [[CALCOCO2]] | -0.39 | -0.20 / -0.39 | ⚠ not reproduced | 8e-04 |  |
| [[CCDC28A]] | -0.39 | -0.19 / -0.39 | ⚠ not reproduced | 8e-04 |  |
| [[INPP5K]] | -0.38 | -0.18 / -0.41 | ⚠ not reproduced | 9e-04 |  |
| [[KIF16B]] | -0.38 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[UBXN6]] | -0.37 | -0.22 / -0.34 | both halves | 6e-04 |  |
| [[KIAA1522]] | -0.37 | -0.29 / -0.34 | both halves | 2e-04 |  |
| [[CHP1]] | -0.37 | -0.27 / -0.36 | both halves | 3e-04 |  |
| [[PNPLA2]] | -0.37 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[SMG1]] | -0.37 | -0.37 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTGS2]] | B | PTGS2 activity raises ARSJ's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.92× lower at baseline in the lines without PTGS2 | 0.002 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[MIR100HG]] | B | MIR100HG activity raises ARSJ's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 2.59× lower at baseline in the lines without MIR100HG | 0.006 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[FRMD4A]] | B | FRMD4A activity raises ARSJ's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 2.70× lower at baseline in the lines without FRMD4A | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[TMEM158]] | B | TMEM158 activity raises ARSJ's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 3.15× lower at baseline in the lines without TMEM158 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[HTR7]] | B | HTR7 activity raises ARSJ's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 1.78× lower at baseline in the lines without HTR7 | 0.039 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[TSPAN5]] | B | TSPAN5 activity raises ARSJ's level | lines that do not express TSPAN5 (9) vs lines expressing it (41) | 3.42× lower at baseline in the lines without TSPAN5 | 0.055 | ⚠ within organs, on part of the lines; also absent: KLF12 |
| [[KCTD12]] | B | KCTD12 activity raises ARSJ's level | lines that do not express KCTD12 (16) vs lines expressing it (34) | 2.84× lower at baseline in the lines without KCTD12 | 0.060 | ⚠ within organs, on part of the lines; also absent: CACNA2D1, NALCN, LINC01828 |
| [[PTGS2]] | B | PTGS2 activity strengthens ARSJ's drug response | lines that do not express PTGS2 (20) vs lines expressing it (21) | the lines without PTGS2 respond 0.71× as strongly (z diff +1.90); strongest at Belinostat 5 µM: 0.44x vs 0.33x (z diff +2.7) | 0.060 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4; target measured in part of the lines; artifact flags |
| [[LRRC8C]] | B | LRRC8C activity raises ARSJ's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 2.25× lower at baseline in the lines without LRRC8C | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |
| [[PLPP4]] | B | PLPP4 activity raises ARSJ's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 1.92× lower at baseline in the lines without PLPP4 | 0.090 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF462]] | B | ARSJ activity raises ZNF462's level | lines that do not express ARSJ (8) vs lines expressing it (42) | 2.16× lower at baseline in the lines without ARSJ | 0.094 | ⚠ within organs, on part of the lines; also absent: ATP2B4, CFAP45, LAMB1 |

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.498). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.3, 13.2); signed map (13.0, 48.4). **Vector** length 89.3, 20.3% of its response variance represented; |z| ≥ 3 in 1,182 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.2 | -0.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +17.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.1 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +1.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | -1.7 |
|  | [[EX229 (drug)]] 5 µM |  | +3.4 | +5.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.2 | +2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +3.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.0 | -6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -9.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.1 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | arylsulfatase family member J |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q26 — chr4:113,900,284-113,979,727 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23548 |
| Gene groups (HGNC) | Sulfatases |
| Reactome | 6 pathways, smallest: The activation of arylsulfatases; Glycosphingolipid catabolism; Glycosphingolipid metabolism |
| Matched by | ensembl_id |

UniProt [Q5FYB0](https://www.uniprot.org/uniprotkb/Q5FYB0) carries no function annotation.

**Summary**, from NCBI Gene [79642](https://www.ncbi.nlm.nih.gov/gene/79642):

> Sulfatases (EC 3.1.5.6), such as ARSJ, hydrolyze sulfate esters from sulfated steroids, carbohydrates, proteoglycans, and glycolipids. They are involved in hormone biosynthesis, modulation of cell signaling, and degradation of macromolecules (Sardiello et al., 2005 [PubMed 16174644]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:26286](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26286) · Entrez [79642](https://www.ncbi.nlm.nih.gov/gene/79642) · UniProt [Q5FYB0](https://www.uniprot.org/uniprotkb/Q5FYB0) · Ensembl [ENSG00000180801](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180801)

## Data

Gene col 11131: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11131); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11131, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11131]; `tensor/DDL_lfc|DDL_z.npy` [11131]; `embed/gene_vectors.npy` [11131]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11131 or target_col == 11131). Every well: [[ARSJ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARSJ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
