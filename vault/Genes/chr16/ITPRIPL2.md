---
symbol: "ITPRIPL2"
type: "gene"
col: 13005
ensembl_id: "ENSG00000205730"
name: "ITPRIP like 2"
location: "16p12.3"
module: 88
arm: "+"
pooled_cpm: 38.43
n_lines_expressing: 48
n_dd_up: 25
n_dd_down: 26
n_dd_up_clean: 21
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# ITPRIPL2

*ITPRIP like 2* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 1.69× (z +6.5, q 3e-08, up in 36 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.129× (z -25.4, q 0e+00, down in 46 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AVEN]] (+0.73, fdr 1e-05), [[ST7L]] (+0.72, fdr 1e-05), [[RXYLT1]] (+0.71, fdr 1e-04); moves opposite to [[CDON]] (-0.68, fdr 1e-05), [[HACE1]] (-0.67, fdr 1e-05), [[KANTR]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GPR160]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13005.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.69×** | +6.5 | 3e-08 | 36/46 (SNU-1, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +6.5 | 3e-08 | 25/43 (NCI-H1792, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.64×** | +6.1 | 2e-07 | 33/46 (BT-474, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.8 | 2e-04 | 26/46 (NCI-H460, SW480, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.45×** | +4.6 | 4e-04 | 31/46 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +4.4 | 0.001 | 22/45 (SNU-423, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.43×** | +4.2 | 0.003 | 23/45 (MIA PaCa-2, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +4.0 | 0.004 | 20/36 (NCI-H1792, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +3.9 | 0.005 | 23/40 (NCI-H1573, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.9 | 0.005 | 1/46 (NCI-H661) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.37×** | +3.9 | 0.005 | 19/46 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.36×** | +3.9 | 0.005 | 20/46 (A549, C32, …) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.32×** | +3.5 | 0.020 | 16/46 (SW 900, A-172, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.027 | 16/46 (NCI-H2030, LoVo, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.027 | 20/46 (NCI-H2030, NCI-H2347, …) | top dose only |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.039 | 12/46 (RKO, NCI-H23, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.042 | 16/46 (PANC-1, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.042 | 13/46 (SNU-423, LOX-IMVI, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.056 | 18/46 (A549, LOX-IMVI, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.061 | 12/46 (PANC-1, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13005.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.129×** | -25.4 | 0e+00 | 46/46 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.141×** | -24.2 | 0e+00 | 46/46 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.158×** | -23.0 | 0e+00 | 44/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.331×** | -13.7 | 9e-41 | 44/46 (KATO III, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.481×** | -9.0 | 2e-17 | 40/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.485×** | -9.0 | 2e-17 | 38/46 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.483×** | -9.0 | 2e-17 | 37/46 (PANC-1, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.478×** | -8.7 | 4e-16 | 38/46 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.528×** | -7.9 | 1e-13 | 37/46 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.648×** | -7.6 | 2e-12 | 36/45 (SK-MEL-2, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.331×** | -7.2 | 3e-11 | 40/46 (LoVo, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.342×** | -7.0 | 1e-10 | 37/46 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.616×** | -6.0 | 1e-07 | 29/46 (SNU-1, LoVo, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.424×** | -5.6 | 1e-06 | 29/41 (HS-578T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.464×** | -5.0 | 2e-05 | 30/45 (BT-474, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.676×** | -4.8 | 5e-05 | 24/46 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13005. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 63.9 | 0 | 12 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0594× (z -23.6) |
| [[LoVo (line)]] | wt | 50.1 | 0 | 11 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0843× (z -21.3) |
| [[A-427 (line)]] | wt | 23.3 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -12.6) |
| [[NCI-H1792 (line)]] | alt | 37.9 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 6.63× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -16.7) |
| [[SK-MEL-2 (line)]] | alt | 25.7 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -17.0) |
| [[SW480 (line)]] | alt | 21.4 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +9.2) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.0724× (z -22.0) |
| [[KATO III (line)]] | alt | 48.3 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.0437× (z -24.5) |
| [[LOX-IMVI (line)]] | wt | 29.9 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.117× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 33.3 | 1 | 4 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.03× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.0914× (z -21.6) |
| [[SNU-1 (line)]] | wt | 43.3 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.0717× (z -15.6) |
| [[SW1417 (line)]] | alt | 27.8 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +9.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -13.1) |
| [[A-172 (line)]] | wt | 93.0 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0773× (z -21.1) |
| [[A498 (line)]] | wt | 62.2 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -20.1) |
| [[AsPC-1 (line)]] | alt | 36.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.109× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 41.1 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -18.1) |
| [[HOP62 (line)]] | alt | 31.5 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.0948× (z -14.8) |
| [[Hs 766T (line)]] | wt | 94.7 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0761× (z -21.3) |
| [[HS-578T (line)]] | alt | 24.6 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.125× (z -11.6) |
| [[J82 (line)]] | alt | 49.0 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0846× (z -18.8) |
| [[NCI-H23 (line)]] | alt | 36.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -13.4) |
| [[Panc 03.27 (line)]] | alt | 37.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.125× (z -14.5) |
| [[RPMI-7951 (line)]] | alt | 55.2 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -11.9) |
| [[A549 (line)]] | wt | 27.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -12.5) |
| [[BT-474 (line)]] | alt | 61.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.128× (z -15.5) |
| [[C32 (line)]] | wt | 32.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -12.1) |
| [[CFPAC-1 (line)]] | alt | 26.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -11.1) |
| [[H4 (line)]] | wt | 40.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -11.7) |
| [[HCT15 (line)]] | alt | 49.2 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.145× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 85.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0391× (z -14.8) |
| [[LS 180 (line)]] | wt | 37.3 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0618× (z -19.0) |
| [[MIA PaCa-2 (line)]] | alt | 29.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0719× (z -19.0) |
| [[NCI-H1573 (line)]] | alt | 37.5 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.153× (z -13.3) |
| [[NCI-H2030 (line)]] | alt | 40.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.123× (z -13.9) |
| [[SW 900 (line)]] | alt | 21.2 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.189× (z -9.1) |
| [[CHP-212 (line)]] | wt | 41.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0662× (z -11.1) |
| [[RKO (line)]] | wt | 21.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.142× (z -10.8) |
| [[SNU-423 (line)]] | alt | 27.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.108× (z -12.2) |
| [[SW48 (line)]] | wt | 27.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.102× (z -10.9) |
| [[COLO 205 (line)]] | alt | 12.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0270× (z -13.9) |
| [[HepG2_C3A (line)]] | wt | 20.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.143× (z -8.7) |
| [[HT-29 (line)]] | alt | 14.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.189× (z -8.8) |
| [[AN3 CA (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.57 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13005), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AVEN]] | +0.73 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[ST7L]] | +0.72 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[RXYLT1]] | +0.71 | +0.70 / +0.35 | both halves | 1e-04 |  |
| [[MAD2L1-DT]] | +0.70 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[UBTF]] | +0.69 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[EXOSC6]] | +0.69 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.69 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[RPL7L1]] | +0.67 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[SLC16A1-AS1]] | +0.67 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[INO80D]] | +0.67 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[MCPH1]] | +0.66 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[ANKRD18B]] | +0.66 | +0.55 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDON]] | -0.68 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[HACE1]] | -0.67 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[KANTR]] | -0.65 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[CEP70]] | -0.64 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[SNAPC3]] | -0.64 | -0.64 / -0.37 | both halves | 7e-05 |  |
| [[PHKA2]] | -0.64 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[PDK3]] | -0.63 | -0.63 / -0.49 | both halves | 2e-05 |  |
| [[IGSF8]] | -0.63 | -0.51 / -0.40 | both halves | 4e-05 |  |
| [[RAB3A]] | -0.63 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[SLC9A6]] | -0.63 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[L2HGDH]] | -0.63 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[GPR160]] | -0.63 | -0.59 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR160]] | B | GPR160 activity lowers ITPRIPL2's level | lines that do not express GPR160 (8) vs lines expressing it (42) | 2.17× higher at baseline in the lines without GPR160 | 0.009 | ⚠ within organs, on part of the lines; also absent: PNPLA4, PRKCZ; maybe low, not absent |
| [[GPR155]] | B | GPR155 activity raises ITPRIPL2's level | lines that do not express GPR155 (6) vs lines expressing it (44) | 1.56× lower at baseline in the lines without GPR155 | 0.075 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PKIG, TBC1D19; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.703). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (7.0, -9.5); signed map (22.2, -26.9). **Vector** length 105, 32.4% of its response variance represented; |z| ≥ 3 in 1,218 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.1 | +4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.2 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.2 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.9 | +4.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.1 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.3 | +4.6 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -5.2 | -8.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.2 | -9.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.0 | -9.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.9 | -9.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.7 | -23.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -7.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.6 | -2.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.4 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | ITPRIP like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:19,113,932-19,121,629 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22994, MGC126798, MGC126800, LOC162073, D1C |
| Matched by | ensembl_id |

UniProt [Q3MIP1](https://www.uniprot.org/uniprotkb/Q3MIP1) carries no function annotation.

**Summary**, from NCBI Gene [162073](https://www.ncbi.nlm.nih.gov/gene/162073):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27257](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27257) · Entrez [162073](https://www.ncbi.nlm.nih.gov/gene/162073) · UniProt [Q3MIP1](https://www.uniprot.org/uniprotkb/Q3MIP1) · Ensembl [ENSG00000205730](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205730)

## Data

Gene col 13005: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13005); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13005, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13005]; `tensor/DDL_lfc|DDL_z.npy` [13005]; `embed/gene_vectors.npy` [13005]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13005 or target_col == 13005). Every well: [[ITPRIPL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITPRIPL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
