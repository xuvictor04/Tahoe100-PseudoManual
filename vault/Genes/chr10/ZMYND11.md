---
symbol: "ZMYND11"
type: "gene"
col: 293
ensembl_id: "ENSG00000015171"
name: "zinc finger MYND-type containing 11"
location: "10p15.3"
module: 194
arm: "+"
pooled_cpm: 62.01
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 11
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/194"]
generated_by: "tahoemap"
---

# ZMYND11

*zinc finger MYND-type containing 11* — 10p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.10× (z +14.3, q 2e-43, up in 40 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.49× (z +7.7, q 3e-12, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.168× (z -34.4, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPSF2]] (+0.75, fdr 7e-06), [[ZMPSTE24]] (+0.75, fdr 7e-06), [[PSME3IP1]] (+0.74, fdr 9e-06); moves opposite to [[CIB1]] (-0.77, fdr 7e-06), [[CIAO2B]] (-0.74, fdr 7e-06), [[ABCB9]] (-0.72, fdr 9e-06).
> It sits in the **+** arm of [[Module 194]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[C7orf57]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 293.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.10×** | +14.3 | 2e-43 | 40/49 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +13.6 | 1e-39 | 37/44 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +9.2 | 7e-18 | 33/45 (RPMI-7951, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +7.7 | 3e-12 | 31/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +7.5 | 8e-12 | 35/48 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +5.9 | 3e-07 | 30/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.23×** | +5.6 | 2e-06 | 25/48 (AsPC-1, NCI-H2030, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.32×** | +5.0 | 4e-05 | 26/47 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +4.7 | 1e-04 | 30/48 (NCI-H1573, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +4.6 | 3e-04 | 27/48 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +4.3 | 1e-03 | 19/48 (RKO, PANC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.48×** | +4.0 | 0.003 | 22/49 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.013 | 19/47 (NCI-H23, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 1.14× | +3.6 | 0.014 | 9/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.014 | 17/47 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.015 | 16/47 (NCI-H460, RKO, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.19× | +3.4 | 0.024 | 17/47 (AsPC-1, NCI-H1792, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.13× | +3.2 | 0.035 | 10/48 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.035 | 13/47 (NCI-H2347, NCI-H2030, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 293.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.168×** | -34.4 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.181×** | -33.0 | 0e+00 | 48/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.201×** | -30.9 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.396×** | -17.9 | 0e+00 | 46/48 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.618×** | -13.1 | 2e-37 | 44/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.525×** | -12.4 | 2e-33 | 44/48 (NCI-H661, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.675×** | -7.6 | 2e-12 | 38/48 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.472×** | -7.6 | 3e-12 | 44/49 (A-172, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.778×** | -4.8 | 8e-05 | 25/48 (LOX-IMVI, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.787×** | -4.6 | 2e-04 | 24/48 (KATO III, SW48, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.737×** | -4.2 | 0.001 | 21/48 (RPMI-7951, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.824×** | -3.7 | 0.009 | 19/48 (HepG2/C3A, HEC-1-A, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.796×** | -3.1 | 0.072 | 13/48 (RKO, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 293. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 37.3 | 5 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +11.2) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.49× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.125× (z -17.2) |
| [[MIA PaCa-2 (line)]] | alt | 55.0 | 2 (2 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +9.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.0972× (z -24.6) |
| [[A549 (line)]] | wt | 69.8 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +9.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.119× (z -19.9) |
| [[LoVo (line)]] | wt | 47.3 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +12.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.175× (z -19.0) |
| [[NCI-H1792 (line)]] | alt | 137 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -20.3) |
| [[RKO (line)]] | wt | 92.8 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 0.05 µM 2.50× (z +8.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.128× (z -20.7) |
| [[SNU-423 (line)]] | alt | 49.6 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +8.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.141× (z -17.0) |
| [[SW1417 (line)]] | alt | 84.5 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 5 µM 2.42× (z +9.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -20.6) |
| [[SW480 (line)]] | alt | 48.5 | 1 (1 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.5) ⚠ cell-cycle shift, explains ~8% of this change | [[Panobinostat (drug)]] 5 µM 0.103× (z -24.9) |
| [[A-427 (line)]] | wt | 69.1 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +9.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -18.8) |
| [[C-33 A (line)]] | alt | 130 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.113× (z -23.5) |
| [[HEC-1-A (line)]] | alt | 92.3 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.88× (z +14.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -21.1) |
| [[HOP62 (line)]] | alt | 48.4 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +9.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.145× (z -20.5) |
| [[HT-29 (line)]] | alt | 50.1 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.172× (z -17.5) |
| [[KATO III (line)]] | alt | 54.6 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +11.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.0837× (z -24.1) |
| [[LOX-IMVI (line)]] | wt | 58.7 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 2.51× (z +8.7) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.185× (z -16.8) |
| [[NCI-H2030 (line)]] | alt | 100 | 2 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.9) ⚠ cell-cycle shift, explains ~8% of this change | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -15.1) |
| [[PANC-1 (line)]] | alt | 46.4 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.63× (z +11.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.207× (z -18.8) |
| [[RPMI-7951 (line)]] | alt | 65.9 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.00× (z +11.8) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.285× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 63.6 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +9.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.141× (z -20.3) |
| [[A498 (line)]] | wt | 33.5 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +9.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -14.6) |
| [[HepG2_C3A (line)]] | wt | 91.2 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -19.6) |
| [[HS-578T (line)]] | alt | 50.0 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +9.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.188× (z -14.9) |
| [[J82 (line)]] | alt | 58.2 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -19.3) |
| [[LS 180 (line)]] | wt | 66.0 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +9.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.114× (z -21.7) |
| [[NCI-H460 (line)]] | wt | 58.1 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.117× (z -27.9) |
| [[Panc 03.27 (line)]] | alt | 36.1 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +9.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.0973× (z -19.4) |
| [[A-172 (line)]] | wt | 114 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -21.2) |
| [[AN3 CA (line)]] | alt | 111 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -13.8) |
| [[Hs 766T (line)]] | wt | 31.3 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.185× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 65.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.148× (z -22.7) |
| [[NCI-H23 (line)]] | alt | 89.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.171× (z -21.0) |
| [[NCI-H2347 (line)]] | alt | 35.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +10.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.321× (z -11.7) |
| [[SW48 (line)]] | wt | 84.1 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -17.0) |
| [[C32 (line)]] | wt | 50.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -14.7) |
| [[H4 (line)]] | wt | 37.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -10.0) |
| [[HCT15 (line)]] | alt | 60.6 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.167× (z -13.3) |
| [[hTERT-HPNE (line)]] | wt | 65.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.148× (z -14.2) |
| [[SHP-77 (line)]] | alt | 60.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.142× (z -18.7) |
| [[SNU-1 (line)]] | wt | 122 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0903× (z -20.9) |
| [[SW 900 (line)]] | alt | 47.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.170× (z -15.1) |
| [[CFPAC-1 (line)]] | alt | 35.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +9.4) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 69.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.121× (z -10.9) |
| [[COLO 205 (line)]] | alt | 33.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.141× (z -13.5) |
| [[BT-474 (line)]] | alt | 82.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -17.5) |
| [[NCI-H661 (line)]] | alt | 65.8 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0570× (z -13.0) |
| [[NCI-H2122 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 293), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPSF2]] | +0.75 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ZMPSTE24]] | +0.75 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[PSME3IP1]] | +0.74 | +0.57 / +0.71 | both halves | 9e-06 |  |
| [[UBTF]] | +0.74 | +0.75 / +0.50 | both halves | 1e-05 |  |
| [[ANKRD40]] | +0.73 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[EFCAB2]] | +0.73 | +0.66 / +0.57 | both halves | 8e-06 |  |
| [[DDX6]] | +0.73 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ZFX]] | +0.72 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[NSD1]] | +0.72 | +0.68 / +0.57 | both halves | 1e-05 | same gene group |
| [[ZNF507]] | +0.70 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[ZFP91]] | +0.70 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[IQCH-AS1]] | +0.70 | +0.61 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIB1]] | -0.77 | -0.72 / -0.59 | both halves | 7e-06 |  |
| [[CIAO2B]] | -0.74 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[ABCB9]] | -0.72 | -0.57 / -0.65 | both halves | 9e-06 |  |
| [[DPM1]] | -0.72 | -0.59 / -0.73 | both halves | 7e-06 |  |
| [[ANKRD37]] | -0.72 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[TNNI3]] | -0.71 | -0.45 / -0.75 | both halves | 3e-05 |  |
| [[AHDC1]] | -0.71 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[SLC27A1]] | -0.71 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[CARHSP1]] | -0.71 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[MPG]] | -0.70 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[UBA6]] | -0.70 | -0.68 / -0.43 | both halves | 3e-05 |  |
| [[CARD19]] | -0.70 | -0.54 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C7orf57]] | B | C7orf57 activity lowers ZMYND11's level | lines that do not express C7orf57 (18) vs lines expressing it (32) | 1.26× higher at baseline in the lines without C7orf57 | 0.0995 | ⚠ within organs, on part of the lines; also absent: CACNG6, GNG11, PAPLN |
| [[TMEM92]] | C | TMEM92 activity weakens ZMYND11's drug response | lines that do not express TMEM92 (22) vs lines expressing it (27) | the lines without TMEM92 respond 0.94× as strongly (z diff -0.25); strongest at Tucidinostat 5 µM: 0.56x vs 0.64x (z diff -2.2) | 0.093 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10; target measured in part of the lines; rests on the correction; artifact flags |
| [[WWC3]] | C | WWC3 activity lowers ZMYND11's level | lines that do not express WWC3 (4) vs lines expressing it (46) | 1.71× higher at baseline in the lines without WWC3 | 0.096 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZMIZ1, ADD3, RASSF5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 194]]; 17 genes; this gene is in the **+** arm (projection on the module's main direction 0.879). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-5.6, 3.7); signed map (18.1, -29.9). **Vector** length 142, 45.4% of its response variance represented; |z| ≥ 3 in 1,316 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.9 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +11.3 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.9 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.8 | +7.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.5 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.5 | +4.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +6.5 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +4.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.4 | +3.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +4.2 | +3.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.7 | -13.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -8.3 | -17.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -8.0 | -30.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.7 | -7.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.0 | -12.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.0 | -7.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.7 | -3.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.3 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger MYND-type containing 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.3 — chr10:130,088-254,637 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BS69, BRAM1 |
| Gene groups (HGNC) | Zinc fingers MYND-type; PHD finger proteins; PWWP domain containing; Bromodomain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15326](https://www.uniprot.org/uniprotkb/Q15326) (Zinc finger MYND domain-containing protein 11):

> Chromatin reader that specifically recognizes and binds histone H3.3 trimethylated at 'Lys-36' (H3.3K36me3) and regulates RNA polymerase II elongation. Does not bind other histone H3 subtypes (H3.1 or H3.2) (By similarity). Colocalizes with highly expressed genes and functions as a transcription corepressor by modulating RNA polymerase II at the elongation stage. Binds non-specifically to dsDNA. Acts as a tumor-suppressor by repressing a transcriptional program essential for tumor cell growth.; …

**Summary**, from NCBI Gene [10771](https://www.ncbi.nlm.nih.gov/gene/10771):

> The protein encoded by this gene was first identified by its ability to bind the adenovirus E1A protein. The protein localizes to the nucleus. It functions as a transcriptional repressor, and expression of E1A inhibits this repression. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16966](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16966) · Entrez [10771](https://www.ncbi.nlm.nih.gov/gene/10771) · UniProt [Q15326](https://www.uniprot.org/uniprotkb/Q15326) · Ensembl [ENSG00000015171](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000015171)

## Data

Gene col 293: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 293); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 293, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 293]; `tensor/DDL_lfc|DDL_z.npy` [293]; `embed/gene_vectors.npy` [293]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 293 or target_col == 293). Every well: [[ZMYND11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZMYND11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
