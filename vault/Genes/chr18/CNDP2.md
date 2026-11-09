---
symbol: "CNDP2"
type: "gene"
col: 5438
ensembl_id: "ENSG00000133313"
name: "carnosine dipeptidase 2"
location: "18q22.3"
module: 18
arm: "+"
pooled_cpm: 31.35
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# CNDP2

*carnosine dipeptidase 2* — 18q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.12× (z +17.1, q 0e+00, up in 36 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 1.55× (z +5.2, q 2e-05, up in 17 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.612× (z -15.8, q 0e+00, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2G2]] (+0.65, fdr 1e-05), [[ABCF2]] (+0.64, fdr 1e-05), [[LETM1]] (+0.63, fdr 7e-06); moves opposite to [[HOXA5]] (-0.62, fdr 1e-05), [[CTR9]] (-0.60, fdr 1e-05), [[KDM5B]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KCNMB4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5438.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +17.1 | 0e+00 | 36/45 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +15.6 | 0e+00 | 31/36 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +12.1 | 3e-31 | 31/41 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +7.2 | 8e-11 | 30/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.55×** | +5.2 | 2e-05 | 17/47 (A498, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.47×** | +4.6 | 5e-04 | 15/44 (NCI-H2030, A498, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.22×** | +4.5 | 5e-04 | 14/44 (NCI-H2347, A549, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.20× | +4.1 | 0.003 | 13/48 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.004 | 14/47 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | 1.13× | +4.0 | 0.004 | 8/48 (NCI-H2347, SW480, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.9 | 0.005 | 16/48 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +3.9 | 0.005 | 20/48 (NCI-H2030, SNU-423, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +3.4 | 0.029 | 11/48 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.033 | 9/48 (MIA PaCa-2, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +3.3 | 0.040 | 8/47 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.040 | 11/45 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.042 | 12/47 (BT-474, C32, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.046 | 12/47 (BT-474, NCI-H23, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.15× | +3.1 | 0.064 | 15/47 (AsPC-1, Hs 766T, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | 1.14× | +3.0 | 0.070 | 6/47 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | 1.14× | +2.9 | 0.093 | 4/47 (RKO, C-33 A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5438.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.612×** | -15.8 | 0e+00 | 36/47 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.502×** | -8.2 | 7e-14 | 32/48 (A-427, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.563×** | -6.8 | 2e-09 | 29/47 (HT-29, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.813×** | -6.7 | 4e-09 | 23/48 (A498, J82, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.821×** | -4.3 | 0.002 | 20/47 (RKO, HS-578T, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.829×** | -4.3 | 0.002 | 17/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | 0.835× | -4.1 | 0.003 | 15/47 (BT-474, LoVo, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.883× | -4.0 | 0.004 | 16/48 (A-427, PANC-1, …) | top dose only | low cells (technical?) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.851× | -3.7 | 0.015 | 9/48 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.893× | -3.7 | 0.015 | 16/47 (NCI-H23, SW48, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.861× | -3.4 | 0.035 | 15/48 (A498, NCI-H23, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.862× | -3.4 | 0.035 | 15/48 (SW1417, LoVo, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.869× | -3.2 | 0.061 | 17/48 (A498, J82, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.873× | -3.1 | 0.083 | 13/48 (A498, MIA PaCa-2, …) | top dose only |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | 0.865× | -3.1 | 0.083 | 7/47 (RPMI-7951, C-33 A, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.875× | -3.0 | 0.083 | 5/48 (hTERT-HPNE, LS 180, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5438. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 27.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -16.6) |
| [[LS 180 (line)]] | wt | 33.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -12.5) |
| [[PANC-1 (line)]] | alt | 69.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +12.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -16.7) |
| [[A498 (line)]] | wt | 59.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +13.8) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 30.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.189× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.421× (z -8.9) |
| [[COLO 205 (line)]] | alt | 42.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.349× (z -10.5) |
| [[HS-578T (line)]] | alt | 27.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -9.8) |
| [[J82 (line)]] | alt | 52.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +9.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 34.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.49× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 30.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +10.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 40.4 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.313× (z -9.4) ⚠ cell-cycle shift, explains ~22% of this change |
| [[SK-MEL-2 (line)]] | alt | 46.9 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0570× (z -13.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 36.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -19.5) ⚠ cell-cycle shift, explains ~14% of this change |
| [[HEC-1-A (line)]] | alt | 26.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +9.6) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 14.3 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.114× (z -10.1) |
| [[LoVo (line)]] | wt | 26.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 24.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 49.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.31× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 25.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +10.2) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 25.8 | 0 | 1 | — | [[DTP3 (drug)]] 5 µM 0.0675× (z -9.2) |
| [[SW1417 (line)]] | alt | 41.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -9.2) |
| [[SW48 (line)]] | wt | 25.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -9.7) |
| [[A-172 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5438), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2G2]] | +0.65 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[ABCF2]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[LETM1]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[TMEM33]] | +0.61 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[PUM3]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[PSME3]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[WDR77]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[PUS1]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[ARMC6]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[AGPAT3]] | +0.57 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[MRPS25]] | +0.57 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[METTL3]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA5]] | -0.62 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[CTR9]] | -0.60 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[KDM5B]] | -0.59 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[FBXO33]] | -0.58 | -0.46 / -0.67 | both halves | 2e-05 |  |
| [[TRIM7-AS2]] | -0.55 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[ARID4A]] | -0.53 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[ZNF10]] | -0.53 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[TCEAL8]] | -0.53 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[NOSIP]] | -0.52 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[TRA2A]] | -0.51 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[MYLIP]] | -0.51 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[ATP5IF1]] | -0.51 | -0.41 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNMB4]] | B | KCNMB4 activity lowers CNDP2's level | lines that do not express KCNMB4 (5) vs lines expressing it (45) | 1.64× higher at baseline in the lines without KCNMB4 | 0.043 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.491). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-18.3, -32.2); signed map (-7.2, -43.0). **Vector** length 84.9, 16.7% of its response variance represented; |z| ≥ 3 in 936 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.7 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +17.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +15.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +12.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.2 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +3.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.5 | +4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.4 | +5.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.2 | +3.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.0 | +3.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -15.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.5 | -4.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.0 | -8.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.8 | -1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | carnosine dipeptidase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q22.3 — chr18:74,495,816-74,523,454 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10830, CN2, HsT2298, CPGL; previously PEPA |
| Gene groups (HGNC) | M20 metallopeptidases |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 6 pathways, smallest: Glutathione synthesis and recycling; Paracetamol ADME; Glutathione conjugation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96KP4](https://www.uniprot.org/uniprotkb/Q96KP4) (Cytosolic non-specific dipeptidase):

> Cytosolic metallodipeptidase with broad substrate specificity that catalyzes the hydrolysis of amide bonds in dipeptides and pseudopeptides. Substrates include L-cysteinylglycine, an intermediate metabolite of the gamma-glutamyl cycle of glutathione metabolism. Can also hydrolyze threonyl-containing dipeptides (By similarity). Upon physiological conditions of amino acids and lactate excess can also catalyze a reverse proteolysis reaction, generating N-[(S)-lactoyl]-L-phenylalanine and possibly …

**Summary**, from NCBI Gene [55748](https://www.ncbi.nlm.nih.gov/gene/55748):

> CNDP2, also known as tissue carnosinase and peptidase A (EC 3.4.13.18), is a nonspecific dipeptidase rather than a selective carnosinase (Teufel et al., 2003 [PubMed 12473676]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:24437](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24437) · Entrez [55748](https://www.ncbi.nlm.nih.gov/gene/55748) · UniProt [Q96KP4](https://www.uniprot.org/uniprotkb/Q96KP4) · Ensembl [ENSG00000133313](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133313)

## Data

Gene col 5438: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5438); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5438, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5438]; `tensor/DDL_lfc|DDL_z.npy` [5438]; `embed/gene_vectors.npy` [5438]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5438 or target_col == 5438). Every well: [[CNDP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNDP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
