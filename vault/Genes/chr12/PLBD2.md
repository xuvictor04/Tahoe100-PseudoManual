---
symbol: "PLBD2"
type: "gene"
col: 7494
ensembl_id: "ENSG00000151176"
name: "phospholipase B domain containing 2"
location: "12q24.13"
module: 50
arm: "+"
pooled_cpm: 31.01
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 16
n_dd_up_clean: 15
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# PLBD2

*phospholipase B domain containing 2* — 12q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.05× (z +13.9, q 3e-41, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.566× (z -11.1, q 8e-26, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAN2B2]] (+0.77, fdr 7e-06), [[ABCA2]] (+0.71, fdr 7e-06), [[ESYT1]] (+0.70, fdr 7e-06); moves opposite to [[TRIP11]] (-0.68, fdr 7e-06), [[HELQ]] (-0.63, fdr 9e-06), [[RBBP6]] (-0.59, fdr 1e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SNTA1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7494.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.05×** | +13.9 | 3e-41 | 44/48 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.91×** | +12.5 | 1e-33 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +12.4 | 3e-33 | 31/36 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.86×** | +12.1 | 3e-31 | 44/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.76×** | +11.0 | 5e-26 | 33/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.63×** | +8.8 | 1e-16 | 29/40 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.51×** | +8.0 | 9e-14 | 37/48 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +8.0 | 9e-14 | 35/48 (MIA PaCa-2, SW48, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +6.6 | 2e-09 | 31/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.38×** | +6.2 | 3e-08 | 25/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +5.9 | 2e-07 | 25/48 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.31×** | +4.9 | 5e-05 | 25/48 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +4.5 | 4e-04 | 24/48 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pentoxifylline (drug)]] 0.5 µM |  | **1.24×** | +4.1 | 0.001 | 15/48 (J82, PANC-1, …) | two highest doses | position effect removed |
| [[Estrone sulfate (potassium) (drug)]] 0.05 µM |  | **1.24×** | +4.1 | 0.002 | 14/48 (HOP62, C32, …) | inconsistent across doses | position effect removed |
| [[Tomivosertib (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.009 | 10/48 (AsPC-1, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.05 µM |  | 1.20× | +3.3 | 0.032 | 12/48 (LS 180, KATO III, …) | inconsistent across doses | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.035 | 11/48 (NCI-H460, HCT15, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[SBI-0640756 (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.042 | 5/48 (NCI-H2030, HepG2/C3A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.042 | 15/48 (MIA PaCa-2, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7494.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.566×** | -11.1 | 8e-26 | 34/48 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.700×** | -9.9 | 2e-20 | 30/48 (SK-MEL-2, C32, …) | all doses, stronger at high dose | composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.703×** | -6.6 | 6e-09 | 28/48 (A-172, LS 180, …) | rises with dose | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.735×** | -6.0 | 3e-07 | 30/48 (AN3 CA, A-172, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Pimozide (drug)]] 5 µM |  | **0.773×** | -5.0 | 5e-05 | 21/48 (PANC-1, KATO III, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.780×** | -4.9 | 1e-04 | 20/48 (PANC-1, C32, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.779×** | -4.5 | 5e-04 | 21/47 (SW48, C-33 A, …) | all doses, flat | low cells (technical?) |
| [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | 0.853× | -4.4 | 8e-04 | 14/48 (Hs 766T, SW1417, …) | inconsistent across doses | position effect removed |
| [[Thymol (drug)]] 0.05 µM |  | **0.804×** | -4.3 | 0.001 | 10/48 (PANC-1, SW 1271, …) | inconsistent across doses | position effect removed |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.815×** | -4.0 | 0.004 | 15/47 (CFPAC-1, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.818×** | -3.9 | 0.004 | 19/48 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.811×** | -3.9 | 0.004 | 20/48 (HOP62, HEC-1-A, …) | all doses, flat | composition shift |
| [[Captopril (drug)]] 5 µM |  | **0.818×** | -3.9 | 0.004 | 7/48 (HEC-1-A, SW480, …) | top dose only | position effect removed |
| [[Clofarabine (drug)]] 0.05 µM |  | **0.827×** | -3.4 | 0.023 | 15/48 (NCI-H1573, BT-474, …) | inconsistent across doses |  |
| [[Simotinib (drug)]] 0.5 µM |  | 0.844× | -3.3 | 0.033 | 9/47 (SW1417, SW480, …) | inconsistent across doses | position effect removed |
| [[AZD-7648 (drug)]] 0.5 µM |  | **0.790×** | -3.3 | 0.035 | 12/48 (A549, Hs 766T, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.890× | -3.3 | 0.038 | 9/48 (NCI-H460, C-33 A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7494. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 22.4 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.84× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.95× (z +9.3) | — |
| [[A498 (line)]] | wt | 50.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.40× (z +9.2) ⚠ cell-cycle shift, explains ~21% of this change | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -9.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[C32 (line)]] | wt | 48.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -12.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.313× (z -9.8) |
| [[PANC-1 (line)]] | alt | 33.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.22× (z +8.6) | — |
| [[SW480 (line)]] | alt | 19.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.46× (z +8.7) | — |
| [[AsPC-1 (line)]] | alt | 29.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.03× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -10.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HOP62 (line)]] | alt | 36.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.248× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 38.0 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.51× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 30.5 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 24.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.339× (z -8.5) |
| [[H4 (line)]] | wt | 41.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.213× (z -9.6) |
| [[HCT15 (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -9.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 20.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.90× (z +8.8) | — |
| [[KATO III (line)]] | alt | 18.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.71× (z +9.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 31.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -9.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H1792 (line)]] | alt | 28.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -9.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SHP-77 (line)]] | alt | 31.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -11.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 33.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -15.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW48 (line)]] | wt | 36.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.219× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7494), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAN2B2]] | +0.77 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[ABCA2]] | +0.71 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[ESYT1]] | +0.70 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[NOMO1]] | +0.69 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[GLB1]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[SELENON]] | +0.68 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[GALNS]] | +0.67 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[PPT1]] | +0.67 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[CTSD]] | +0.66 | +0.76 / +0.50 | both halves | 1e-05 |  |
| [[CAPN1]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ADAM15]] | +0.66 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[COLGALT1]] | +0.65 | +0.66 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIP11]] | -0.68 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[HELQ]] | -0.63 | -0.58 / -0.57 | both halves | 9e-06 |  |
| [[RBBP6]] | -0.59 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[CCDC174]] | -0.58 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[NSRP1]] | -0.58 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[PPIG]] | -0.57 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[PDCD7]] | -0.57 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[MFAP1]] | -0.57 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[ZC3H6]] | -0.56 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[KRCC1]] | -0.56 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[MED18]] | -0.56 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[NEPRO-AS1]] | -0.55 | -0.59 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNTA1]] | B | SNTA1 activity raises PLBD2's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.92× lower at baseline in the lines without SNTA1 | 0.010 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[SEPTIN5]] | B | SEPTIN5 activity raises PLBD2's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.36× lower at baseline in the lines without SEPTIN5 | 0.050 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[SOAT1]] | C | SOAT1 activity raises PLBD2's level | lines that do not express SOAT1 (3) vs lines expressing it (47) | 1.81× lower at baseline in the lines without SOAT1 | 0.024 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, CEP85L, CFL2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.782). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.9, -21.7); signed map (-46.3, -11.4). **Vector** length 101, 23.2% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Extracellular matrix organization* (reactome, mean cos +0.53 to 12); *Glycosphingolipid catabolism* (reactome, mean cos +0.52 to 5); *Degradation of the extracellular matrix* (reactome, mean cos +0.54 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +8.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.4 | +8.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +3.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.6 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +4.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.7 | -11.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -7.5 | -9.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -6.1 | -3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.0 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.2 | -6.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -4.5 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.8 | -2.8 |
|  | [[Ciclopirox (drug)]] 5 µM |  | -1.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase B domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.13 — chr12:113,358,566-113,391,629 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PLBL2, p76 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NHP8](https://www.uniprot.org/uniprotkb/Q8NHP8) (Putative aminopeptidase PLBD2):

> Putative aminopeptidase.

**Summary**, from NCBI Gene [196463](https://www.ncbi.nlm.nih.gov/gene/196463):

> Predicted to enable glycerophospholipase activity. Predicted to be involved in lipid catabolic process. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27283](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27283) · Entrez [196463](https://www.ncbi.nlm.nih.gov/gene/196463) · UniProt [Q8NHP8](https://www.uniprot.org/uniprotkb/Q8NHP8) · Ensembl [ENSG00000151176](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151176)

## Data

Gene col 7494: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7494); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7494, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7494]; `tensor/DDL_lfc|DDL_z.npy` [7494]; `embed/gene_vectors.npy` [7494]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7494 or target_col == 7494). Every well: [[PLBD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLBD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
