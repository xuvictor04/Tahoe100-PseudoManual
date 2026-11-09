---
symbol: "ATP10D"
type: "gene"
col: 6969
ensembl_id: "ENSG00000145246"
name: "ATPase phospholipid transporting 10D (putative)"
location: "4p12"
module: 32
arm: "+"
pooled_cpm: 26.09
n_lines_expressing: 45
n_dd_up: 39
n_dd_down: 14
n_dd_up_clean: 32
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 8
direction_downstream: 4
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# ATP10D

*ATPase phospholipid transporting 10D (putative)* — 4p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.56× (z +9.3, q 5e-18, up in 34 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.677× (z -5.8, q 4e-06, down in 21 of 41 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.779× (z -5.2, q 4e-05, down in 23 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERAP2]] (+0.64, fdr 2e-05), [[PSMA4]] (+0.63, fdr 1e-05), [[TLR6]] (+0.59, fdr 1e-05); moves opposite to [[MTMR12]] (-0.53, fdr 1e-04), [[FBXO31]] (-0.52, fdr 3e-05), [[SOCS7]] (-0.52, fdr 2e-04).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LINC02328]] → it (grade B ⚠); 4 go from it, the strongest it → [[CAPN10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6969.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +9.3 | 5e-18 | 34/43 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +8.0 | 3e-13 | 26/42 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +7.7 | 2e-12 | 20/42 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +7.2 | 8e-11 | 20/41 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.63×** | +7.1 | 1e-10 | 32/43 (CFPAC-1, NCI-H2347, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.59×** | +6.9 | 5e-10 | 27/43 (COLO 205, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.65×** | +6.7 | 2e-09 | 28/43 (COLO 205, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~25% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +6.4 | 1e-08 | 24/43 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.50×** | +6.0 | 1e-07 | 23/43 (J82, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.49×** | +5.9 | 2e-07 | 22/43 (NCI-H23, J82, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +5.8 | 4e-07 | 26/42 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.2 | 1e-05 | 21/43 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +5.1 | 1e-05 | 20/43 (HOP62, COLO 205, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +5.0 | 2e-05 | 24/43 (J82, HEC-1-A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.40×** | +5.0 | 2e-05 | 24/43 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +4.2 | 8e-04 | 14/43 (HEC-1-A, A-427, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.2 | 8e-04 | 16/43 (NCI-H460, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +4.0 | 0.002 | 14/42 (HEC-1-A, A-427, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.003 | 17/42 (HEC-1-A, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.003 | 18/43 (HEC-1-A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6969.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **0.677×** | -5.8 | 4e-06 | 21/41 (Hs 766T, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.779×** | -5.2 | 4e-05 | 23/43 (CHP-212, CFPAC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.706×** | -5.0 | 1e-04 | 19/40 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.531×** | -4.9 | 1e-04 | 22/43 (PANC-1, CHP-212, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.732×** | -4.6 | 4e-04 | 21/43 (H4, CHP-212, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.730×** | -4.6 | 5e-04 | 23/42 (RKO, H4, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.732×** | -4.4 | 7e-04 | 20/42 (H4, NCI-H2030, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.756×** | -4.1 | 0.002 | 21/42 (NCI-H23, SW 1271, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.758×** | -4.1 | 0.003 | 21/43 (COLO 205, Hs 766T, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.605×** | -3.9 | 0.006 | 18/41 (NCI-H1573, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.642×** | -3.4 | 0.031 | 15/30 (SW 900, A549, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.726×** | -3.4 | 0.034 | 16/43 (C-33 A, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.857× | -3.2 | 0.050 | 15/42 (A498, CHP-212, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **0.659×** | -3.2 | 0.050 | 12/39 (LoVo, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.808×** | -3.1 | 0.075 | 11/43 (hTERT-HPNE, SW48, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6969. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 27.2 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.402× (z -9.4) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.191× (z -9.0) |
| [[A-427 (line)]] | wt | 36.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.41× (z +10.0) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 34.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.242× (z -9.5) |
| [[H4 (line)]] | wt | 91.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.175× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 20.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +8.8) | [[Docetaxel (drug)]] 0.05 µM 0.186× (z -9.6) ⚠ transcription drop; cell-cycle shift, explains ~41% of this change |
| [[NCI-H460 (line)]] | wt | 29.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.8) | — |
| [[RKO (line)]] | wt | 21.5 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -11.6) |
| [[A498 (line)]] | wt | 69.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 22.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0784× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 27.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +10.5) | — |
| [[CHP-212 (line)]] | wt | 91.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.269× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[NCI-H2347 (line)]] | alt | 13.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.02× (z +10.9) | — |
| [[SW 1271 (line)]] | alt | 63.1 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0913× (z -8.6) |
| [[SW 900 (line)]] | alt | 42.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0846× (z -8.9) ⚠ toxic |
| [[SW480 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.278× (z -9.0) ⚠ cell-cycle shift, explains ~56% of this change |
| [[A-172 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.91 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.90 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.37 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.72 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 15.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6969), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERAP2]] | +0.64 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[PSMA4]] | +0.63 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[TLR6]] | +0.59 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[LINC02328]] | +0.59 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[CASP7]] | +0.58 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[HTATIP2]] | +0.58 | +0.69 / +0.35 | both halves | 1e-04 |  |
| [[HDX]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[EGF]] | +0.57 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[PARP14]] | +0.57 | +0.66 / +0.36 | both halves | 1e-04 |  |
| [[NMI]] | +0.57 | +0.60 / +0.38 | both halves | 6e-05 |  |
| [[RBM43]] | +0.57 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[BTN3A3]] | +0.56 | +0.54 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTMR12]] | -0.53 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[FBXO31]] | -0.52 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[SOCS7]] | -0.52 | -0.56 / -0.32 | both halves | 2e-04 |  |
| [[AXIN1]] | -0.52 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[TSEN54]] | -0.51 | -0.51 / -0.25 | both halves | 4e-04 |  |
| [[CAPN10]] | -0.50 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[GLRX5]] | -0.48 | -0.39 / -0.31 | both halves | 2e-04 |  |
| [[SPATA33]] | -0.48 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[SH2B2]] | -0.48 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[CORO7]] | -0.47 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[SFXN2]] | -0.47 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[KLF13]] | -0.47 | -0.52 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02328]] | B | LINC02328 activity raises ATP10D's level | lines that do not express LINC02328 (14) vs lines expressing it (36) | 2.17× lower at baseline in the lines without LINC02328 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000253471, PDE4B; maybe low, not absent |
| [[IL7R]] | B | IL7R activity raises ATP10D's level | lines that do not express IL7R (30) vs lines expressing it (20) | 2.40× lower at baseline in the lines without IL7R | 0.024 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1 |
| [[CACNA2D1]] | B | CACNA2D1 activity raises ATP10D's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 2.59× lower at baseline in the lines without CACNA2D1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169 |
| [[TOP2A]] | B | TOP2A activity lowers ATP10D's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SPART]] | B | SPART activity raises ATP10D's level | lines that do not express SPART (15) vs lines expressing it (35) | 2.65× lower at baseline in the lines without SPART | 0.071 | ⚠ within organs, on part of the lines; also absent: CCDC169, SPART-AS1, FIGN |
| [[TLR1]] | B | TLR1 activity raises ATP10D's level | lines that do not express TLR1 (15) vs lines expressing it (35) | 2.22× lower at baseline in the lines without TLR1 | 0.081 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |
| [[TDO2]] | B | TDO2 activity raises ATP10D's level | lines that do not express TDO2 (27) vs lines expressing it (23) | 1.98× lower at baseline in the lines without TDO2 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LAMA1, SCN3A, MSC-AS1 |
| [[VPS35L]] | C | VPS35L activity raises ATP10D's level | lines that do not express VPS35L (9) vs lines expressing it (41) | 3.37× lower at baseline in the lines without VPS35L | 0.061 | ⚠ within organs, on part of the lines; also absent: HDGFL3, CHST11, RNF150; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAPN10]] | B | ATP10D activity lowers CAPN10's level | lines that do not express ATP10D (5) vs lines expressing it (45) | 1.81× higher at baseline in the lines without ATP10D | 0.086 | ⚠ within organs, on part of the lines; also absent: DUBR, CLEC2D, VPS35L |
| [[AXIN1]] | B | ATP10D activity lowers AXIN1's level | lines that do not express ATP10D (5) vs lines expressing it (45) | 1.58× higher at baseline in the lines without ATP10D | 0.088 | ⚠ within organs, on part of the lines; also absent: DUBR, CLEC2D, VPS35L |
| [[BTN3A2]] | B | ATP10D activity raises BTN3A2's level | lines that do not express ATP10D (5) vs lines expressing it (45) | 2.10× lower at baseline in the lines without ATP10D | 0.089 | ⚠ within organs, on part of the lines; also absent: DUBR, CLEC2D, VPS35L |
| [[VPS35L]] | C | ATP10D activity raises VPS35L's level | lines that do not express ATP10D (5) vs lines expressing it (45) | 4.75× lower at baseline in the lines without ATP10D | 0.078 | ⚠ within organs, on part of the lines; also absent: DUBR, CLEC2D, VPS35L; co-absent with the target |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.502). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.6, 54.6); signed map (49.3, -8.6). **Vector** length 91.3, 20.3% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +5.9 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +5.8 | +6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.8 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | +5.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +1.1 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | -5.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.3 | -4.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.1 | +5.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.9 | -4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -4.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.9 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | ATPase phospholipid transporting 10D (putative) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p12 — chr4:47,485,275-47,593,486 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ATPVD, KIAA1487 |
| Gene groups (HGNC) | ATPase phospholipid transporting |
| Reactome | 3 pathways, smallest: Ion transport by P-type ATPases; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P241](https://www.uniprot.org/uniprotkb/Q9P241) (Phospholipid-transporting ATPase VD):

> Catalytic component of a P4-ATPase flippase complex, which catalyzes the hydrolysis of ATP coupled to the transport of glucosylceramide (GlcCer) from the outer to the inner leaflet of the plasma membrane.

**Summary**, from NCBI Gene [57205](https://www.ncbi.nlm.nih.gov/gene/57205):

> Enables glycosylceramide flippase activity. Predicted to be involved in phospholipid translocation. Located in endoplasmic reticulum and plasma membrane. Part of phospholipid-translocating ATPase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13549](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13549) · Entrez [57205](https://www.ncbi.nlm.nih.gov/gene/57205) · UniProt [Q9P241](https://www.uniprot.org/uniprotkb/Q9P241) · Ensembl [ENSG00000145246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145246)

## Data

Gene col 6969: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6969); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6969, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6969]; `tensor/DDL_lfc|DDL_z.npy` [6969]; `embed/gene_vectors.npy` [6969]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6969 or target_col == 6969). Every well: [[ATP10D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP10D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
