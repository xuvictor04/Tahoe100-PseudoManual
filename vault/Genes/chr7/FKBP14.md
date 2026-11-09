---
symbol: "FKBP14"
type: "gene"
col: 2720
ensembl_id: "ENSG00000106080"
name: "FKBP prolyl isomerase 14"
location: "7p14.3"
module: 56
arm: "+"
pooled_cpm: 43.5
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 21
n_dd_up_clean: 18
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# FKBP14

*FKBP prolyl isomerase 14* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.06× (z +16.8, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 0.599× (z -7.9, q 2e-12, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC24D]] (+0.74, fdr 7e-06), [[SURF4]] (+0.71, fdr 7e-06), [[LMAN1]] (+0.70, fdr 7e-06).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2720.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +16.8 | 0e+00 | 46/48 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **2.04×** | +11.7 | 3e-29 | 43/48 (A-172, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.96×** | +11.1 | 2e-26 | 40/48 (A-172, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.81×** | +9.8 | 2e-20 | 42/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.78×** | +9.5 | 4e-19 | 37/48 (A-172, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.74×** | +9.1 | 9e-18 | 38/48 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.71×** | +8.8 | 9e-17 | 40/48 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +8.6 | 6e-16 | 38/48 (HS-578T, RPMI-7951, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.35×** | +7.3 | 1e-11 | 41/48 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +7.1 | 7e-11 | 28/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | **1.53×** | +7.0 | 1e-10 | 31/47 (HS-578T, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.62×** | +5.6 | 8e-07 | 36/48 (MIA PaCa-2, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.41×** | +5.5 | 2e-06 | 20/39 (A-172, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **1.41×** | +5.5 | 2e-06 | 25/46 (HepG2/C3A, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.88×** | +5.4 | 2e-06 | 31/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.86×** | +5.3 | 4e-06 | 32/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +5.1 | 1e-05 | 30/48 (SW1417, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.78×** | +5.0 | 2e-05 | 21/48 (A-172, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.76×** | +4.9 | 4e-05 | 24/48 (MIA PaCa-2, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.48×** | +4.6 | 1e-04 | 21/48 (MIA PaCa-2, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.70×** | +4.6 | 1e-04 | 27/48 (SW480, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.46×** | +4.5 | 2e-04 | 25/48 (MIA PaCa-2, NCI-H1792, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2720.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.599×** | -7.9 | 2e-12 | 36/48 (HOP62, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.702×** | -5.4 | 2e-05 | 25/47 (SW 900, C-33 A, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.727×** | -5.1 | 8e-05 | 28/47 (NCI-H460, H4, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.820×** | -4.7 | 5e-04 | 29/48 (Hs 766T, LoVo, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.763×** | -4.5 | 8e-04 | 23/48 (HOP62, SW 900, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.770×** | -4.3 | 0.001 | 20/48 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.760×** | -4.3 | 0.001 | 19/48 (NCI-H2030, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.775×** | -4.1 | 0.004 | 21/48 (A498, LoVo, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.634×** | -3.9 | 0.005 | 20/48 (Hs 766T, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | **0.781×** | -3.9 | 0.005 | 17/47 (SW1417, A549, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.789×** | -3.9 | 0.005 | 24/47 (NCI-H2030, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.640×** | -3.9 | 0.005 | 17/48 (J82, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.779×** | -3.8 | 0.005 | 20/48 (Panc 03.27, RPMI-7951, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.786×** | -3.8 | 0.005 | 23/48 (A498, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.794×** | -3.8 | 0.005 | 20/48 (A498, NCI-H2030, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.814×** | -3.4 | 0.022 | 22/48 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.685×** | -3.3 | 0.036 | 17/49 (SW480, SW1417, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.55 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2720. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 17.2 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.02× (z +13.8) | — |
| [[HS-578T (line)]] | alt | 46.5 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +10.1) | — |
| [[J82 (line)]] | alt | 22.9 | 3 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +11.5) | [[AZD2858 (drug)]] 0.5 µM 0.187× (z -9.3) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 27.8 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.08× (z +9.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +9.9) | — |
| [[PANC-1 (line)]] | alt | 39.4 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +14.0) | — |
| [[AsPC-1 (line)]] | alt | 25.7 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.79× (z +8.8) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[HOP62 (line)]] | alt | 34.1 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.2) | [[Homoharringtonine (drug)]] 0.05 µM 0.311× (z -9.6) |
| [[KATO III (line)]] | alt | 56.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 32.6 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.15× (z +17.8) | — |
| [[A498 (line)]] | wt | 85.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.410× (z -9.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.383× (z -9.5) |
| [[RKO (line)]] | wt | 54.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -17.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 66.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +10.7) | — |
| [[SHP-77 (line)]] | alt | 45.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -15.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 34.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 25.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +10.5) | — |
| [[BT-474 (line)]] | alt | 49.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 37.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 64.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 41.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 23.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +12.5) | — |
| [[SK-MEL-2 (line)]] | alt | 38.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 19.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.38× (z +12.2) | — |
| [[SW 900 (line)]] | alt | 62.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.304× (z -9.4) |
| [[SW480 (line)]] | alt | 61.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +15.4) | — |
| [[AN3 CA (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 97.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 76.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 66.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2720), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC24D]] | +0.74 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[SURF4]] | +0.71 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[LMAN1]] | +0.70 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[CALU]] | +0.70 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[PGM3]] | +0.69 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[SEC31A]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[KDELR2]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[SLC31A1]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[SEC22B]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[SEC61A1]] | +0.66 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[COG6]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity raises FKBP14's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 4.2% of all compounds | 0.005 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[P3H3]] | B | P3H3 activity raises FKBP14's level | lines that do not express P3H3 (10) vs lines expressing it (40) | 1.33× lower at baseline in the lines without P3H3 | 0.082 | ⚠ within organs, on part of the lines; also absent: STARD9, GSTA4, CTXN1 |
| [[MCTP2]] | B | MCTP2 activity weakens FKBP14's drug response | lines that do not express MCTP2 (20) vs lines expressing it (28) | the lines without MCTP2 respond 1.22× as strongly (z diff -1.08); strongest at Panobinostat 5 µM: 2.32x vs 1.57x (z diff -2.6) | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3; target measured in part of the lines; artifact flags |
| [[P3H1]] | C | P3H1 activity raises FKBP14's level | lines that do not express P3H1 (4) vs lines expressing it (46) | 1.14× lower at baseline in the lines without P3H1 | 0.094 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CEP112, TIMP2, CNTNAP1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | FKBP14's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | FKBP14's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.58 | 0.492 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.6, -31.6); signed map (-52.7, 8.0). **Vector** length 129, 40.6% of its response variance represented; |z| ≥ 3 in 1,300 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.58 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.59 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.59 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.9 | +8.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.0 | +9.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.3 | +9.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +5.0 | +7.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +4.8 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +7.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.3 | +5.3 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.6 | -7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.1 | -1.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.0 | -3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.4 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.4 | -2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.7 | -5.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.0 | -3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -4.0 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | FKBP prolyl isomerase 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:30,010,587-30,026,702 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20731, FKBP22 |
| Gene groups (HGNC) | EF-hand domain containing; FKBP prolyl isomerase family |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 5 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; Unfolded Protein Response (UPR) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWM8](https://www.uniprot.org/uniprotkb/Q9NWM8) (Peptidyl-prolyl cis-trans isomerase FKBP14):

> PPIase which accelerates the folding of proteins during protein synthesis. Has a preference for substrates containing 4-hydroxylproline modifications, including type III collagen. May also target type VI and type X collagens.

**Summary**, from NCBI Gene [55033](https://www.ncbi.nlm.nih.gov/gene/55033):

> The protein encoded by this gene is a member of the FK506-binding protein family of peptidyl-prolyl cis-trans isomerases. The encoded protein is found in the lumen of the endoplasmic reticulum, where it is thought to accelerate protein folding. Defects in this gene are a cause of a type of Ehlers-Danlos syndrome (EDS). Both a protein-coding variant and noncoding variants are transcribed from this gene. [provided by RefSeq, Mar 2012]

**Accessions** — [HGNC:18625](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18625) · Entrez [55033](https://www.ncbi.nlm.nih.gov/gene/55033) · UniProt [Q9NWM8](https://www.uniprot.org/uniprotkb/Q9NWM8) · Ensembl [ENSG00000106080](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106080)

## Data

Gene col 2720: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2720); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2720, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2720]; `tensor/DDL_lfc|DDL_z.npy` [2720]; `embed/gene_vectors.npy` [2720]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2720 or target_col == 2720). Every well: [[FKBP14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FKBP14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
