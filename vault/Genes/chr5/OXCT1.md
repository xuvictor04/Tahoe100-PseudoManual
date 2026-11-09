---
symbol: "OXCT1"
type: "gene"
col: 1377
ensembl_id: "ENSG00000083720"
name: "3-oxoacid CoA-transferase 1"
location: "5p13.1"
module: 3
arm: "-"
pooled_cpm: 41.58
n_lines_expressing: 42
n_dd_up: 14
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# OXCT1

*3-oxoacid CoA-transferase 1* — 5p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.07× (z +22.1, q 0e+00, up in 33 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.555× (z -12.7, q 3e-34, down in 33 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACADM]] (+0.71, fdr 7e-06), [[SEPTIN11]] (+0.70, fdr 7e-06), [[MCCC2]] (+0.69, fdr 1e-05); moves opposite to [[VRK3]] (-0.65, fdr 1e-05), [[CIAO2B]] (-0.63, fdr 1e-05), [[ATG4B]] (-0.63, fdr 3e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[VSIG10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1377.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.07×** | +22.1 | 0e+00 | 33/40 (NCI-H2030, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.84×** | +21.6 | 0e+00 | 31/33 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +17.4 | 0e+00 | 35/39 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +15.5 | 0e+00 | 29/36 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +11.6 | 5e-29 | 24/39 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +10.1 | 3e-22 | 28/39 (HOP62, SHP-77, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +7.5 | 4e-12 | 22/40 (HEC-1-A, Hs 766T, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +7.4 | 1e-11 | 23/40 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +7.3 | 2e-11 | 22/40 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +7.2 | 2e-11 | 23/40 (SNU-423, SW480, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +5.7 | 6e-07 | 19/40 (NCI-H2030, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.24×** | +4.4 | 4e-04 | 19/40 (SW480, A-172, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.003 | 16/40 (NCI-H2347, HOP62, …) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.13× | +3.5 | 0.017 | 7/40 (SW480, SW 900, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.019 | 11/39 (NCI-H460, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.055 | 2/40 (A-172, LoVo) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.15× | +3.1 | 0.073 | 12/40 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.16× | +3.0 | 0.078 | 12/40 (LS 180, C32, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.15× | +3.0 | 0.087 | 8/40 (LoVo, KATO III, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.15× | +2.9 | 0.092 | 7/40 (C32, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1377.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.555×** | -12.7 | 3e-34 | 33/40 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.596×** | -11.2 | 2e-26 | 31/40 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.616×** | -10.5 | 2e-23 | 30/40 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.682×** | -7.8 | 7e-13 | 25/40 (SW 900, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.796×** | -4.9 | 9e-05 | 17/40 (HEC-1-A, RKO, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.715×** | -3.8 | 0.014 | 16/35 (RPMI-7951, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.772×** | -3.7 | 0.018 | 8/40 (NCI-H661, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.732×** | -3.5 | 0.029 | 13/37 (KATO III, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.855× | -3.4 | 0.040 | 8/39 (C32, HOP62, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.856× | -3.4 | 0.040 | 15/40 (SW48, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.863× | -3.2 | 0.067 | 18/40 (A-172, LS 180, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.902× | -3.2 | 0.070 | 6/40 (Hs 766T, HOP62, …) | rises with dose |  |
| [[Hydroxyurea (drug)]] 0.05 µM |  | 0.861× | -3.0 | 0.11 | 5/39 (HCT15, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1377. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 71.3 | 3 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +14.3) | [[Panobinostat (drug)]] 0.5 µM 0.396× (z -12.2) |
| [[J82 (line)]] | alt | 144 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -16.0) |
| [[LoVo (line)]] | wt | 48.8 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.06× (z +15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +11.5) | — |
| [[SHP-77 (line)]] | alt | 176 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.462× (z -10.6) |
| [[SW480 (line)]] | alt | 57.8 | 2 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.94× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -14.1) |
| [[HOP62 (line)]] | alt | 39.8 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +12.8) | [[Panobinostat (drug)]] 0.5 µM 0.355× (z -9.6) |
| [[RKO (line)]] | wt | 91.2 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +11.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.318× (z -11.5) |
| [[C32 (line)]] | wt | 52.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +13.3) | — |
| [[CFPAC-1 (line)]] | alt | 24.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.82× (z +22.5) | — |
| [[NCI-H1573 (line)]] | alt | 32.0 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +17.5) | [[Panobinostat (drug)]] 0.5 µM 0.346× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 76.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.46× (z +27.8) | [[Docetaxel (drug)]] 0.05 µM 0.477× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~12% of this change |
| [[NCI-H460 (line)]] | wt | 30.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 28.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +13.5) | — |
| [[A-172 (line)]] | wt | 32.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +9.5) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.393× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 23.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +19.2) | — |
| [[KATO III (line)]] | alt | 25.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.30× (z +12.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 50.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.30× (z +11.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 42.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +15.0) | — |
| [[NCI-H1792 (line)]] | alt | 35.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.55× (z +12.3) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 33.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -11.0) |
| [[SW 900 (line)]] | alt | 80.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +14.8) | [[Bortezomib (drug)]] 0.05 µM 0.366× (z -8.8) |
| [[AN3 CA (line)]] | alt | 72.6 | 0 | 1 | — | [[Arbutin (drug)]] 0.05 µM 0.115× (z -10.8) |
| [[BT-474 (line)]] | alt | 64.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +16.4) | — |
| [[Hs 766T (line)]] | wt | 44.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 53.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.337× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 42.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.402× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 33.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +18.5) | — |
| [[PANC-1 (line)]] | alt | 36.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +9.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 42.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0741× (z -18.4) ⚠ transcription drop; cell-cycle shift, explains ~12% of this change |
| [[SNU-423 (line)]] | alt | 16.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 38.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -9.3) |
| [[A-427 (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.95 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.42 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.26 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.72 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1377), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACADM]] | +0.71 | +0.65 / +0.61 | both halves | 7e-06 | STRING 546 |
| [[SEPTIN11]] | +0.70 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[MCCC2]] | +0.69 | +0.69 / +0.54 | both halves | 1e-05 | STRING 450 |
| [[USP13]] | +0.69 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[SNX5]] | +0.68 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[RNASEH2B]] | +0.68 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[ZMYND11]] | +0.65 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[TMPO]] | +0.64 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[SEPTIN8]] | +0.64 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[TMX4]] | +0.64 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[HDGFL3]] | +0.64 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[FGD5-AS1]] | +0.63 | +0.55 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VRK3]] | -0.65 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[CIAO2B]] | -0.63 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[ATG4B]] | -0.63 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[RNF181]] | -0.62 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[MRPL55]] | -0.62 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[PRKD2]] | -0.61 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[BLVRB]] | -0.61 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[ENO2]] | -0.61 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[MIR210HG]] | -0.61 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[SIRT7]] | -0.60 | -0.37 / -0.56 | both halves | 8e-05 |  |
| [[PLIN3]] | -0.60 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[MED31]] | -0.60 | -0.55 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers OXCT1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[OGFRL1]] | B | OGFRL1 activity raises OXCT1's level | lines that do not express OGFRL1 (10) vs lines expressing it (40) | 2.48× lower at baseline in the lines without OGFRL1 | 0.035 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, HDGFL3, CYP46A1 |
| [[DZIP1L]] | B | DZIP1L activity raises OXCT1's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 2.14× lower at baseline in the lines without DZIP1L | 0.060 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises OXCT1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VSIG10]] | B | OXCT1 activity lowers VSIG10's level | lines that do not express OXCT1 (8) vs lines expressing it (42) | 1.63× higher at baseline in the lines without OXCT1 | 0.038 | ⚠ within organs, on part of the lines |
| [[PRKD2]] | B | OXCT1 activity lowers PRKD2's level | lines that do not express OXCT1 (8) vs lines expressing it (42) | 1.32× higher at baseline in the lines without OXCT1 | 0.050 | ⚠ within organs, on part of the lines |
| [[ENO2]] | B | OXCT1 activity raises ENO2's level | lines that do not express OXCT1 (8) vs lines expressing it (42) | 2.67× lower at baseline in the lines without OXCT1 | 0.062 | ⚠ within organs, on part of the lines |
| [[POGLUT3]] | B | OXCT1 activity raises POGLUT3's level | lines that do not express OXCT1 (8) vs lines expressing it (42) | 1.62× lower at baseline in the lines without OXCT1 | 0.074 | ⚠ within organs, on part of the lines |
| [[DZIP1L]] | B | OXCT1 activity raises DZIP1L's level | lines that do not express OXCT1 (8) vs lines expressing it (42) | 1.89× lower at baseline in the lines without OXCT1 | 0.086 | ⚠ within organs, on part of the lines |
| [[VSIG10]] | B | OXCT1 activity weakens VSIG10's drug response | lines that do not express OXCT1 (8) vs lines expressing it (39) | the lines without OXCT1 respond 1.30× as strongly (z diff -1.34); strongest at Digitoxin 5 µM: 0.38x vs 0.56x (z diff -3.2) | 0.094 | ⚠ within organs, on part of the lines; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.666). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-3.8, 4.9); signed map (21.2, -34.1). **Vector** length 118, 30.2% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.51 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +17.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +21.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +15.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +22.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +11.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +2.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.4 | +2.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.1 | +1.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.7 | -12.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.8 | -11.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.2 | -10.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.5 | -7.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.1 | -2.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | 3-oxoacid CoA-transferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.1 — chr5:41,730,065-41,870,425 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SCOT; previously OXCT |
| Reactome | 4 pathways, smallest: Utilization of Ketone Bodies; Ketone body metabolism; Mitochondrial protein degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P55809](https://www.uniprot.org/uniprotkb/P55809) (Succinyl-CoA:3-ketoacid coenzyme A transferase 1, mitochondrial):

> Key enzyme for ketone body catabolism. Catalyzes the first, rate-limiting step of ketone body utilization in extrahepatic tissues, by transferring coenzyme A (CoA) from a donor thiolester species (succinyl-CoA) to an acceptor carboxylate (acetoacetate), and produces acetoacetyl-CoA. Acetoacetyl-CoA is further metabolized by acetoacetyl-CoA thiolase into two acetyl-CoA molecules which enter the citric acid cycle for energy production. Forms a dimeric enzyme where both of the subunits are able to …

**Summary**, from NCBI Gene [5019](https://www.ncbi.nlm.nih.gov/gene/5019):

> This gene encodes a member of the 3-oxoacid CoA-transferase gene family. The encoded protein is a homodimeric mitochondrial matrix enzyme that plays a central role in extrahepatic ketone body catabolism by catalyzing the reversible transfer of coenzyme A from succinyl-CoA to acetoacetate. Mutations in this gene are associated with succinyl CoA:3-oxoacid CoA transferase deficiency. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8527](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8527) · Entrez [5019](https://www.ncbi.nlm.nih.gov/gene/5019) · UniProt [P55809](https://www.uniprot.org/uniprotkb/P55809) · Ensembl [ENSG00000083720](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083720)

## Data

Gene col 1377: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1377); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1377, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1377]; `tensor/DDL_lfc|DDL_z.npy` [1377]; `embed/gene_vectors.npy` [1377]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1377 or target_col == 1377). Every well: [[OXCT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OXCT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
