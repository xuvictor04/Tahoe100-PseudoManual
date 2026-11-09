---
symbol: "MFSD2A"
type: "gene"
col: 9639
ensembl_id: "ENSG00000168389"
name: "MFSD2 lysolipid transporter A, lysophospholipid"
location: "1p34.2"
module: 141
arm: "+"
pooled_cpm: 9.48
n_lines_expressing: 48
n_dd_up: 32
n_dd_down: 23
n_dd_up_clean: 15
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# MFSD2A

*MFSD2 lysolipid transporter A, lysophospholipid* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.08× (z +24.1, q 0e+00, up in 38 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.488× (z -6.0, q 1e-06, down in 26 of 46 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.546× (z -5.5, q 1e-05, down in 24 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGR3]] (+0.60, fdr 1e-05), [[PLK3]] (+0.58, fdr 1e-05), [[EGR2]] (+0.57, fdr 1e-05); moves opposite to [[PAIP1]] (-0.56, fdr 2e-05), [[NCKAP1]] (-0.56, fdr 3e-05), [[ZNF148]] (-0.56, fdr 1e-05).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[G0S2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9639.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.08×** | +24.1 | 0e+00 | 38/39 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.56×** | +17.8 | 0e+00 | 37/40 (HS-578T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.76×** | +13.6 | 1e-39 | 35/41 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.16×** | +13.0 | 3e-36 | 31/43 (NCI-H1792, SNU-423, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **3.59×** | +12.1 | 2e-31 | 43/46 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **3.10×** | +10.7 | 1e-24 | 40/45 (SW480, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **2.96×** | +10.2 | 1e-22 | 39/44 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.93×** | +10.2 | 2e-22 | 31/39 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.61×** | +9.1 | 7e-18 | 35/46 (HOP62, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.18×** | +7.4 | 1e-11 | 31/44 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **2.12×** | +7.1 | 6e-11 | 31/43 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **2.06×** | +6.6 | 2e-09 | 21/32 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +6.1 | 4e-08 | 23/44 (SW480, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | **1.90×** | +5.8 | 2e-07 | 24/37 (SNU-423, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.81×** | +5.6 | 7e-07 | 26/46 (SNU-423, SW480, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **2.33×** | +4.1 | 0.001 | 15/40 (J82, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +3.9 | 0.003 | 18/45 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[EX229 (drug)]] 0.05 µM |  | **1.53×** | +3.8 | 0.003 | 13/44 (NCI-H2347, LoVo, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.14×** | +3.6 | 0.006 | 12/42 (NCI-H23, J82, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.05×** | +3.4 | 0.013 | 14/40 (RPMI-7951, NCI-H2347, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.035 | 13/45 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.57×** | +3.1 | 0.042 | 7/43 (NCI-H460, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.57×** | +3.0 | 0.044 | 7/46 (LoVo, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.53×** | +2.9 | 0.076 | 4/43 (SW480, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9639.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.488×** | -6.0 | 1e-06 | 26/46 (NCI-H1792, RPMI-7951, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.546×** | -5.5 | 1e-05 | 24/42 (A-172, NCI-H2030, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.551×** | -5.4 | 1e-05 | 23/42 (NCI-H2347, HOP62, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.577×** | -5.2 | 3e-05 | 25/42 (AsPC-1, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.680×** | -5.1 | 4e-05 | 24/43 (AsPC-1, NCI-H23, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.586×** | -5.1 | 4e-05 | 21/46 (Hs 766T, KATO III, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.601×** | -4.8 | 1e-04 | 21/45 (AsPC-1, RKO, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.595×** | -4.5 | 4e-04 | 18/45 (RKO, NCI-H2030, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.396×** | -4.4 | 5e-04 | 19/42 (LS 180, HCT15, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.664×** | -4.4 | 5e-04 | 19/43 (AsPC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.619×** | -4.4 | 7e-04 | 11/15 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Afatinib (drug)]] 5 µM |  | **0.594×** | -4.0 | 0.003 | 16/45 (NCI-H2030, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.436×** | -4.0 | 0.003 | 19/45 (NCI-H1792, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.661×** | -3.9 | 0.004 | 16/45 (H4, A498, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.712×** | -3.9 | 0.004 | 15/43 (AsPC-1, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **0.776×** | -3.4 | 0.025 | 14/44 (H4, NCI-H2347, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.495×** | -3.4 | 0.025 | 11/44 (NCI-H23, RPMI-7951, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.98 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9639. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 17.0 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 23.8× (z +20.2) | — |
| [[NCI-H460 (line)]] | wt | 6.36 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 27.4× (z +12.4) | — |
| [[NCI-H2347 (line)]] | alt | 9.85 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.76× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -9.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 27.2 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.0590× (z -16.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 8.38 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 73.5× (z +22.2) | — |
| [[HS-578T (line)]] | alt | 18.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 17.2× (z +13.9) | — |
| [[RPMI-7951 (line)]] | alt | 21.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.133× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 18.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.58× (z +13.0) | — |
| [[SW480 (line)]] | alt | 5.21 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.89× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -9.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 12.1 | 0 | 3 (1 ⚠) | — | [[Cobimetinib (drug)]] 0.5 µM 0.0640× (z -11.3) |
| [[BT-474 (line)]] | alt | 12.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +10.7) | — |
| [[HEC-1-A (line)]] | alt | 2.42 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 29.3× (z +9.6) | — |
| [[J82 (line)]] | alt | 29.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.28× (z +18.5) | [[Dinaciclib (drug)]] 5 µM 0.0334× (z -19.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 22.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.31× (z +12.7) | — |
| [[Panc 03.27 (line)]] | alt | 4.28 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 50.8× (z +16.1) | — |
| [[PANC-1 (line)]] | alt | 2.65 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +10.8) | [[Rapamycin (drug)]] 0.5 µM 0.0723× (z -8.5) |
| [[A-172 (line)]] | wt | 5.98 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 14.9× (z +10.6) | [[Cobimetinib (drug)]] 5 µM 0.0636× (z -10.4) |
| [[H4 (line)]] | wt | 15.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.85× (z +8.9) | [[Busulfan (drug)]] 0.05 µM 0.0414× (z -10.3) |
| [[hTERT-HPNE (line)]] | wt | 7.12 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 55.7× (z +15.2) | — |
| [[SNU-423 (line)]] | alt | 7.79 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.2× (z +18.6) | — |
| [[A549 (line)]] | wt | 6.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +12.8) | — |
| [[COLO 205 (line)]] | alt | 4.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 4.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +10.6) | — |
| [[LoVo (line)]] | wt | 9.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +11.5) | — |
| [[LS 180 (line)]] | wt | 9.41 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -10.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 6.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.14× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 2.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +9.6) | — |
| [[A-427 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9639), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGR3]] | +0.60 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[PLK3]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[EGR2]] | +0.57 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[DUSP6]] | +0.57 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[ATG101]] | +0.57 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[SRA1]] | +0.56 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[OSBPL5]] | +0.56 | +0.50 / +0.53 | both halves | 1e-05 | pathway: Glycerophospholipid biosynthesis |
| [[MCL1]] | +0.56 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[DUSP7]] | +0.55 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[SPRY4]] | +0.54 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[FSCN1]] | +0.54 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[ST3GAL1]] | +0.54 | +0.36 / +0.57 | both halves | 1e-04 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAIP1]] | -0.56 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[NCKAP1]] | -0.56 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[ZNF148]] | -0.56 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[ZNF326]] | -0.52 | -0.29 / -0.60 | both halves | 2e-04 |  |
| [[RAD23B]] | -0.52 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[ATP6V1C1]] | -0.52 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[SMARCC2]] | -0.52 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ADD1]] | -0.51 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[FAM204A]] | -0.51 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[VPS41]] | -0.51 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[HINT3]] | -0.50 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[DNAJC13]] | -0.50 | -0.39 / -0.54 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[G0S2]] | B | G0S2 activity raises MFSD2A's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 1.85× lower at baseline in the lines without G0S2 | 0.011 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD |
| [[TOP2A]] | B | TOP2A activity lowers MFSD2A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RGS2]] | B | RGS2 activity raises MFSD2A's level | lines that do not express RGS2 (17) vs lines expressing it (33) | 1.12× lower at baseline in the lines without RGS2 | 0.069 | ⚠ within organs, on part of the lines; also absent: LINC01393, P2RY1, MEF2C-AS1; maybe low, not absent |
| [[HS3ST3B1]] | B | HS3ST3B1 activity raises MFSD2A's level | lines that do not express HS3ST3B1 (18) vs lines expressing it (32) | 1.62× lower at baseline in the lines without HS3ST3B1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| [[HAP1]] | B | HAP1 activity lowers MFSD2A's level | lines that do not express HAP1 (12) vs lines expressing it (38) | 1.64× higher at baseline in the lines without HAP1 | 0.083 | ⚠ within organs, on part of the lines; also absent: HID1, NRARP, PDE9A |
| [[KRAS]] | B | KRAS activity raises MFSD2A's level | compounds that target KRAS: 3 of 4 lower it (BI-3406, Lonafarnib, RMC-6236) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[MAP2K1]] | B | MAP2K1 activity raises MFSD2A's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SLC43A3]] | B | SLC43A3 activity strengthens MFSD2A's drug response | lines that do not express SLC43A3 (27) vs lines expressing it (19) | the lines without SLC43A3 respond 0.75× as strongly (z diff +1.03); strongest at Homoharringtonine 0.5 µM: 4.16x vs 10x (z diff +2.6) | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.503). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.3, -1.1); signed map (6.3, 32.1). **Vector** length 80.1, 17.8% of its response variance represented; |z| ≥ 3 in 1,263 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +13.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +24.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.3 | +13.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.3 | +17.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +6.1 |
|  | [[SBI-0640756 (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.5 | +2.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.5 | -2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.8 | -5.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.6 | -6.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.2 | -4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | +1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.9 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | MFSD2 lysolipid transporter A, lysophospholipid |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:39,955,112-39,969,968 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14490, SLC59A1; previously MFSD2 |
| Gene groups (HGNC) | Solute carrier family 59 |
| Reactome | 4 pathways, smallest: Synthesis of PC; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NA29](https://www.uniprot.org/uniprotkb/Q8NA29) (Sodium-dependent lysophosphatidylcholine symporter 1):

> Sodium-dependent lysophosphatidylcholine (LPC) symporter, which plays an essential role for blood-brain barrier formation and function. Specifically expressed in endothelium of the blood-brain barrier of micro-vessels and transports LPC into the brain (By similarity). Transport of LPC is essential because it constitutes the major mechanism by which docosahexaenoic acid (DHA), an omega-3 fatty acid that is essential for normal brain growth and cognitive function, enters the brain. Transports LPC …

**Summary**, from NCBI Gene [84879](https://www.ncbi.nlm.nih.gov/gene/84879):

> The protein encoded by this gene is a transmembrane protein and sodium-dependent lysophosphatidylcholine transporter. The encoded protein is involved in the establishment of the blood-brain barrier and is required for brain growth and function. Defects in this gene are a cause of a progressive microcephaly syndrome. [provided by RefSeq, Mar 2017]

**Accessions** — [HGNC:25897](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25897) · Entrez [84879](https://www.ncbi.nlm.nih.gov/gene/84879) · UniProt [Q8NA29](https://www.uniprot.org/uniprotkb/Q8NA29) · Ensembl [ENSG00000168389](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168389)

## Data

Gene col 9639: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9639); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9639, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9639]; `tensor/DDL_lfc|DDL_z.npy` [9639]; `embed/gene_vectors.npy` [9639]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9639 or target_col == 9639). Every well: [[MFSD2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFSD2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
