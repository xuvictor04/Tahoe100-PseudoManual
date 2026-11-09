---
symbol: "WDR5"
type: "gene"
col: 12186
ensembl_id: "ENSG00000196363"
name: "WD repeat domain 5"
location: "9q34.2"
module: 199
arm: "+"
pooled_cpm: 23.67
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/199"]
generated_by: "tahoemap"
---

# WDR5

*WD repeat domain 5* — 9q34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.66× (z +10.1, q 3e-21, up in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.78× (z +5.9, q 2e-07, up in 20 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.503× (z -19.5, q 0e+00, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INTS11]] (+0.73, fdr 7e-06), [[GTPBP3]] (+0.72, fdr 1e-05), [[ACTR5]] (+0.72, fdr 1e-05); moves opposite to [[NPHS1]] (-0.68, fdr 7e-06), [[RIPK2-DT]] (-0.66, fdr 1e-05), [[SGO1-AS1]] (-0.66, fdr 1e-05).
> It is in [[Module 199]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ANKRD20A5P]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 19 with an alert ⚠; shown: the 15 strongest and the 13 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12186.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.66×** | +10.1 | 3e-21 | 38/48 (SW480, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.66×** | +9.7 | 5e-20 | 25/36 (KATO III, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.63×** | +9.7 | 5e-20 | 41/48 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.53×** | +8.4 | 6e-15 | 34/47 (HT-29, COLO 205, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +7.7 | 2e-12 | 29/47 (A549, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.47×** | +7.6 | 3e-12 | 32/47 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.42×** | +6.9 | 4e-10 | 24/42 (KATO III, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.41×** | +6.5 | 5e-09 | 26/46 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.37×** | +6.2 | 4e-08 | 24/47 (SW48, NCI-H1573, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.81×** | +6.0 | 1e-07 | 12/29 (NCI-H1573, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +5.9 | 2e-07 | 20/47 (MIA PaCa-2, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +5.8 | 3e-07 | 1/48 (KATO III) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.27×** | +4.8 | 7e-05 | 22/45 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.26×** | +4.6 | 1e-04 | 17/45 (NCI-H23, AsPC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.26×** | +4.6 | 1e-04 | 15/47 (H4, SW480, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.38×** | +4.6 | 2e-04 | 18/46 (HCT15, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.003 | 6/46 (A498, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.004 | 11/47 (NCI-H1573, A549, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +3.7 | 0.006 | 12/48 (H4, HS-578T, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.007 | 10/47 (NCI-H460, CHP-212, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.20×** | +3.6 | 0.007 | 12/47 (NCI-H1573, BT-474, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.14× | +3.6 | 0.007 | 13/48 (SHP-77, HOP62, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.007 | 7/48 (NCI-H460, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.014 | 7/46 (CFPAC-1, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.015 | 11/48 (COLO 205, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.037 | 17/46 (CHP-212, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.055 | 6/48 (NCI-H1573, H4, …) | inconsistent across doses |  |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | 1.16× | +2.9 | 0.067 | 6/47 (SW480, CFPAC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12186.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.503×** | -19.5 | 0e+00 | 40/47 (HOP62, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.626×** | -9.0 | 5e-17 | 31/48 (J82, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.769×** | -7.5 | 1e-11 | 26/48 (NCI-H1573, A498, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.783×** | -7.0 | 4e-10 | 26/48 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.712×** | -6.8 | 1e-09 | 27/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.841× | -5.0 | 6e-05 | 21/48 (J82, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.817×** | -4.1 | 0.003 | 17/47 (SK-MEL-2, NCI-H1573, …) | top dose only |  |
| [[Pimozide (drug)]] 0.05 µM |  | **0.818×** | -4.0 | 0.004 | 14/46 (NCI-H2030, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | 0.837× | -3.6 | 0.020 | 14/47 (A498, KATO III, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.838× | -3.6 | 0.020 | 11/47 (SW 900, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.838× | -3.3 | 0.047 | 9/47 (BT-474, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.852× | -3.2 | 0.056 | 15/47 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.849× | -3.2 | 0.062 | 19/47 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.859× | -3.1 | 0.081 | 10/48 (MIA PaCa-2, COLO 205, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12186. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 24.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -11.8) |
| [[KATO III (line)]] | alt | 22.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.10× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | — |
| [[LoVo (line)]] | wt | 17.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -12.5) |
| [[NCI-H2030 (line)]] | alt | 14.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.47× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | — |
| [[C-33 A (line)]] | alt | 41.8 | 0 | 2 (2 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.217× (z -10.4) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 38.0 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.393× (z -9.0) |
| [[J82 (line)]] | alt | 41.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 14.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.253× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 20.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -9.9) |
| [[SW480 (line)]] | alt | 30.5 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 2.15× (z +9.0) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -10.8) |
| [[A498 (line)]] | wt | 28.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -10.6) |
| [[HOP62 (line)]] | alt | 25.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -16.9) |
| [[HS-578T (line)]] | alt | 17.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 23.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -8.7) |
| [[LS 180 (line)]] | wt | 21.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.54× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 33.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.288× (z -10.3) ⚠ cell-cycle shift, explains ~61% of this change |
| [[NCI-H23 (line)]] | alt | 27.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -12.6) |
| [[NCI-H2347 (line)]] | alt | 26.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 24.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 14.0 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.123× (z -9.9) |
| [[SNU-423 (line)]] | alt | 22.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -11.4) |
| [[SW 1271 (line)]] | alt | 29.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0796× (z -10.1) |
| [[A-427 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12186), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS11]] | +0.73 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[GTPBP3]] | +0.72 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[ACTR5]] | +0.72 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[NUP93]] | +0.70 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[ZDHHC8]] | +0.70 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[RPA1]] | +0.70 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[CPSF4]] | +0.69 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[TBCD]] | +0.69 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[TRABD]] | +0.68 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[FAR1]] | +0.68 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[POFUT1]] | +0.67 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[TELO2]] | +0.67 | +0.62 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPHS1]] | -0.68 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[RIPK2-DT]] | -0.66 | -0.68 / -0.51 | both halves | 1e-05 |  |
| [[SGO1-AS1]] | -0.66 | -0.69 / -0.56 | both halves | 1e-05 |  |
| [[RNF103-CHMP3]] | -0.66 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[LINC02307]] | -0.65 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[C21orf91]] | -0.65 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[CCDC148]] | -0.64 | -0.74 / -0.52 | both halves | 1e-05 |  |
| [[BAZ2B]] | -0.64 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[LPXN]] | -0.64 | -0.67 / -0.47 | both halves | 2e-05 |  |
| [[AK9]] | -0.64 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[PATL2]] | -0.63 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[DNAH12]] | -0.63 | -0.59 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD20A5P]] | B | ANKRD20A5P activity lowers WDR5's level | lines that do not express ANKRD20A5P (16) vs lines expressing it (34) | 1.15× higher at baseline in the lines without ANKRD20A5P | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000283294, SH3RF2 |
| [[KMO]] | B | KMO activity lowers WDR5's level | lines that do not express KMO (18) vs lines expressing it (32) | 1.36× higher at baseline in the lines without KMO | 0.038 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[HLA-V-1]] | B | HLA-V-1 activity lowers WDR5's level | lines that do not express HLA-V-1 (21) vs lines expressing it (29) | 1.28× higher at baseline in the lines without HLA-V-1 | 0.038 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MST1R, KIAA0040 |
| [[BMP2]] | B | BMP2 activity lowers WDR5's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 1.33× higher at baseline in the lines without BMP2 | 0.048 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[ATXN1]] | B | ATXN1 activity lowers WDR5's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 1.56× higher at baseline in the lines without ATXN1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| [[ABCA10]] | B | ABCA10 activity lowers WDR5's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 1.41× higher at baseline in the lines without ABCA10 | 0.070 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 199]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.768). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.0, -16.6); signed map (-41.8, -13.6). **Vector** length 102, 23.3% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +5.3 | +9.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +4.9 | +8.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.8 | +10.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +7.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +3.0 | +4.8 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.8 | +2.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.4 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +5.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.7 | -19.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.7 | -9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -7.9 | -1.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.1 | -6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.2 — chr9:134,135,365-134,159,968 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SWD3, CFAP89, BIG-3 |
| Gene groups (HGNC) | WD repeat domain containing; ATAC complex; NSL histone acetyltransferase complex; Cilia and flagella associated; WRAD complex |
| Reactome | 37 pathways, smallest: Loss of Function of KMT2D in Kabuki Syndrome; Loss of Function of KMT2D in MLL4 Complex Formation in Kabuki Syndrome; Cardiogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P61964](https://www.uniprot.org/uniprotkb/P61964) (WD repeat-containing protein 5):

> Contributes to histone modification. May position the N-terminus of histone H3 for efficient trimethylation at 'Lys-4'. As part of the MLL1/MLL complex it is involved in methylation and dimethylation at 'Lys-4' of histone H3. H3 'Lys-4' methylation represents a specific tag for epigenetic transcriptional activation. As part of the NSL complex it may be involved in acetylation of nucleosomal histone H4 on several lysine residues. May regulate osteoblasts differentiation (By similarity). In …

**Summary**, from NCBI Gene [11091](https://www.ncbi.nlm.nih.gov/gene/11091):

> This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. This protein contains 7 WD repeats. Alternatively spliced transcript variants …

**Accessions** — [HGNC:12757](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12757) · Entrez [11091](https://www.ncbi.nlm.nih.gov/gene/11091) · UniProt [P61964](https://www.uniprot.org/uniprotkb/P61964) · Ensembl [ENSG00000196363](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196363)

## Data

Gene col 12186: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12186); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12186, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12186]; `tensor/DDL_lfc|DDL_z.npy` [12186]; `embed/gene_vectors.npy` [12186]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12186 or target_col == 12186). Every well: [[WDR5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
