---
symbol: "GTPBP3"
type: "gene"
col: 5045
ensembl_id: "ENSG00000130299"
name: "GTP binding protein 3, mitochondrial"
location: "19p13.11"
module: 26
arm: "-"
pooled_cpm: 9.6
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 16
n_dd_up_clean: 13
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# GTPBP3

*GTP binding protein 3, mitochondrial* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.00× (z +16.8, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.489× (z -15.4, q 0e+00, down in 35 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELP1]] (+0.76, fdr 7e-06), [[ACTR5]] (+0.74, fdr 7e-06), [[BRAT1]] (+0.73, fdr 7e-06); moves opposite to [[CCDC90B-AS1]] (-0.71, fdr 3e-05), [[PPP1R12A-AS2]] (-0.70, fdr 4e-05), [[LINC02307]] (-0.69, fdr 3e-05).
> It sits in the **-** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PODXL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5045.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.00×** | +16.8 | 0e+00 | 44/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.85×** | +16.0 | 0e+00 | 42/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.35×** | +13.1 | 9e-37 | 43/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +12.3 | 7e-33 | 25/36 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.77×** | +8.4 | 6e-15 | 12/17 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +7.2 | 4e-11 | 26/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.60×** | +6.9 | 5e-10 | 22/37 (SW1417, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +6.4 | 9e-09 | 22/43 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +5.8 | 6e-07 | 2/48 (Hs 766T, HOP62) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.41×** | +5.2 | 1e-05 | 13/47 (HS-578T, HOP62, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +5.1 | 2e-05 | 18/48 (C32, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.43×** | +5.0 | 2e-05 | 14/26 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +4.9 | 3e-05 | 16/39 (A498, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.8 | 8e-05 | 14/39 (SNU-423, HS-578T, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.30×** | +4.0 | 0.002 | 3/47 (A498, C-33 A, …) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.004 | 11/44 (LS 180, NCI-H460, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.005 | 6/45 (LoVo, NCI-H2347, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.60×** | +3.8 | 0.005 | 4/47 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.040 | 3/43 (MIA PaCa-2, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Monocrotaline (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.048 | 6/42 (C32, NCI-H2030, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.078 | 4/45 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +2.9 | 0.099 | 9/46 (A549, AsPC-1, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +2.9 | 0.099 | 7/48 (SHP-77, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5045.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.489×** | -15.4 | 0e+00 | 35/45 (A-172, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.480×** | -11.2 | 8e-27 | 35/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.482×** | -11.1 | 2e-26 | 34/46 (RKO, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.507×** | -10.4 | 4e-23 | 33/46 (H4, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.520×** | -9.6 | 9e-20 | 28/46 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.550×** | -9.1 | 6e-18 | 30/46 (BT-474, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.638×** | -6.9 | 5e-10 | 23/46 (HCT15, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.645×** | -6.7 | 1e-09 | 25/44 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.553×** | -4.7 | 1e-04 | 16/46 (A-427, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 5 µM |  | **0.768×** | -3.9 | 0.006 | 6/47 (KATO III, NCI-H661, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.776×** | -3.9 | 0.006 | 12/46 (SW48, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.782×** | -3.8 | 0.008 | 14/46 (LS 180, A498, …) | rises with dose |  |
| [[Crizotinib (hydrochloride) (drug)]] 0.5 µM |  | **0.783×** | -3.7 | 0.008 | 11/44 (HepG2/C3A, HCT15, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.788×** | -3.7 | 0.011 | 13/47 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.810×** | -3.2 | 0.049 | 8/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5045. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 8.36 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -14.1) |
| [[SW480 (line)]] | alt | 12.6 | 3 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.40× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -10.5) |
| [[A-172 (line)]] | wt | 13.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -18.1) |
| [[A-427 (line)]] | wt | 12.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.204× (z -9.2) |
| [[A498 (line)]] | wt | 19.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -13.9) |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.101× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 11.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 7.58 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -11.0) |
| [[H4 (line)]] | wt | 12.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0329× (z -12.9) |
| [[Hs 766T (line)]] | wt | 6.87 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -8.8) |
| [[LoVo (line)]] | wt | 9.71 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.30× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 11.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -15.0) |
| [[RKO (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0721× (z -12.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 7.04 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.116× (z -8.9) ⚠ toxic |
| [[SW 900 (line)]] | alt | 6.78 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0755× (z -9.6) |
| [[SW48 (line)]] | wt | 19.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.160× (z -8.5) |
| [[A549 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5045), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELP1]] | +0.76 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ACTR5]] | +0.74 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[BRAT1]] | +0.73 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[WDR5]] | +0.72 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[SKP2]] | +0.71 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[RSAD1]] | +0.69 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[UTP18]] | +0.69 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[TAF5L]] | +0.68 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[ZDHHC8]] | +0.67 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[IMPDH1]] | +0.67 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[METAP1]] | +0.67 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[TRABD]] | +0.67 | +0.59 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC90B-AS1]] | -0.71 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[PPP1R12A-AS2]] | -0.70 | -0.55 / -0.40 | both halves | 4e-05 |  |
| [[LINC02307]] | -0.69 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[BAZ2B]] | -0.69 | -0.67 / -0.38 | both halves | 6e-05 |  |
| [[MMADHC-DT]] | -0.68 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[ANGPT2]] | -0.67 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[C11orf58]] | -0.67 | -0.63 / -0.43 | both halves | 4e-05 |  |
| [[AK9]] | -0.67 | -0.59 / -0.33 | both halves | 1e-04 |  |
| [[KANSL1L]] | -0.66 | -0.57 / -0.27 | both halves | 3e-04 |  |
| [[PCNX4-DT]] | -0.66 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[TMEM202-AS1]] | -0.66 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[ATE1OSP]] | -0.65 | -0.54 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PODXL2]] | B | PODXL2 activity raises GTPBP3's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.55× lower at baseline in the lines without PODXL2 | 0.020 | ⚠ within organs, on part of the lines |
| [[MCOLN2]] | B | MCOLN2 activity raises GTPBP3's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.42× lower at baseline in the lines without MCOLN2 | 0.049 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[GPD1L]] | C | GPD1L activity raises GTPBP3's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 2.02× lower at baseline in the lines without GPD1L | 0.035 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |
| [[HACE1]] | C | HACE1 activity raises GTPBP3's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 1.85× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **-** arm (projection on the module's main direction -0.679). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-1.2, -2.0); signed map (-40.6, -13.4). **Vector** length 73.0, 12.8% of its response variance represented; |z| ≥ 3 in 1,031 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.6 | +16.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +16.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.4 | +13.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.9 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.3 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | -2.9 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.2 | +2.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.2 | +0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.9 | -15.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.8 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -6.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.5 | -0.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.7 | -0.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | GTP binding protein 3, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,334,920-17,342,731 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MSS1, THDF1, GTPBG3, MTGP1, FLJ14700 |
| Reactome | 3 pathways, smallest: tRNA modification in the mitochondrion; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969Y2](https://www.uniprot.org/uniprotkb/Q969Y2) (5-taurinomethyluridine-[tRNA] synthase subunit GTPB3, mitochondrial):

> GTPase component of the GTPBP3-MTO1 complex that catalyzes the 5-taurinomethyluridine (taum(5)U) modification at the 34th wobble position (U34) of mitochondrial tRNAs (mt-tRNAs), which plays a role in mt-tRNA decoding and mitochondrial translation. Taum(5)U formation on mammalian mt-tRNA requires the presence of both GTPBP3-mediated GTPase activity and MTO1 catalytic activity.

**Summary**, from NCBI Gene [84705](https://www.ncbi.nlm.nih.gov/gene/84705):

> This locus encodes a GTP-binding protein. The encoded protein is localized to the mitochondria and may play a role in mitochondrial tRNA modification. Polymorphisms at this locus may be associated with severity of aminoglycoside-induced deafness, a disease associated with a mutation in the 12S rRNA. Alternatively spliced transcript variants encoding different isoforms have been described. [provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:14880](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14880) · Entrez [84705](https://www.ncbi.nlm.nih.gov/gene/84705) · UniProt [Q969Y2](https://www.uniprot.org/uniprotkb/Q969Y2) · Ensembl [ENSG00000130299](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130299)

## Data

Gene col 5045: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5045); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5045, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5045]; `tensor/DDL_lfc|DDL_z.npy` [5045]; `embed/gene_vectors.npy` [5045]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5045 or target_col == 5045). Every well: [[GTPBP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTPBP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
