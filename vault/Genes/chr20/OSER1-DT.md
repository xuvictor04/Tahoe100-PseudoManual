---
symbol: "OSER1-DT"
type: "gene"
col: 13368
ensembl_id: "ENSG00000223891"
name: "OSER1 divergent transcript"
location: "20q13.12"
module: 69
arm: "+"
pooled_cpm: 5.3
n_lines_expressing: 50
n_dd_up: 50
n_dd_down: 23
n_dd_up_clean: 42
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# OSER1-DT

*OSER1 divergent transcript* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 50 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.57× (z +22.9, q 0e+00, up in 37 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.406× (z -11.5, q 1e-27, down in 31 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.607× (z -6.4, q 4e-08, down in 22 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFV2-AS1]] (+0.72, fdr 7e-06), [[CREBRF]] (+0.69, fdr 7e-06), [[RSRP1]] (+0.68, fdr 7e-06); moves opposite to [[TCOF1]] (-0.67, fdr 7e-06), [[EIF2B3]] (-0.64, fdr 2e-04), [[PPP5C]] (-0.63, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 50 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13368.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.57×** | +22.9 | 0e+00 | 37/38 (SW1417, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.24×** | +14.6 | 1e-45 | 29/40 (HOP62, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.20×** | +10.0 | 2e-21 | 29/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.13×** | +9.6 | 8e-20 | 30/45 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.67×** | +9.3 | 2e-18 | 24/46 (NCI-H2030, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +8.7 | 5e-16 | 23/36 (SNU-423, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +7.6 | 2e-12 | 3/16 (HT-29, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.72×** | +6.9 | 3e-10 | 23/46 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +6.7 | 2e-09 | 20/39 (Panc 03.27, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +5.5 | 2e-06 | 7/26 (NCI-H2347, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +4.9 | 5e-05 | 12/24 (NCI-H2030, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +4.6 | 2e-04 | 12/46 (KATO III, A-172, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.43×** | +4.5 | 2e-04 | 10/46 (KATO III, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +4.5 | 2e-04 | 9/47 (SK-MEL-2, SW1417, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.44×** | +4.5 | 3e-04 | 7/47 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.28×** | +4.3 | 6e-04 | 8/46 (SW480, Hs 766T, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.58×** | +4.1 | 0.001 | 6/40 (HEC-1-A, SW1417, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +4.1 | 0.001 | 11/43 (RPMI-7951, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13368.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.406×** | -11.5 | 1e-27 | 31/47 (KATO III, A498, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.519×** | -8.4 | 2e-14 | 21/35 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.607×** | -6.4 | 4e-08 | 22/44 (HepG2/C3A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.657×** | -5.3 | 1e-05 | 20/47 (HOP62, SNU-423, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.683×** | -4.9 | 1e-04 | 13/44 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.467×** | -4.6 | 4e-04 | 9/41 (Hs 766T, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.470×** | -4.6 | 4e-04 | 12/31 (A549, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.607×** | -4.5 | 4e-04 | 15/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.694×** | -4.4 | 7e-04 | 12/42 (Hs 766T, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.788×** | -4.3 | 0.001 | 9/48 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.497×** | -4.2 | 0.001 | 13/35 (A-427, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.727×** | -4.1 | 0.002 | 15/44 (SNU-423, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.541×** | -3.7 | 0.009 | 10/43 (Hs 766T, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.551×** | -3.6 | 0.013 | 8/36 (HOP62, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.556×** | -3.5 | 0.015 | 10/34 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.763×** | -3.4 | 0.021 | 6/44 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.568×** | -3.4 | 0.021 | 8/28 (A549, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Voriconazole (drug)]] 0.05 µM |  | **0.777×** | -3.2 | 0.043 | 5/45 (NCI-H1573, LoVo, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.717×** | -3.0 | 0.073 | 3/42 (SW 900, HT-29, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13368. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 7.31 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +8.7) | [[Bortezomib (drug)]] 0.05 µM 0.0698× (z -9.6) |
| [[A-172 (line)]] | wt | 5.16 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.01× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.0826× (z -10.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 5.43 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.27× (z +10.5) | — |
| [[KATO III (line)]] | alt | 15.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.184× (z -8.9) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 7.83 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +10.2) | [[Bortezomib (drug)]] 0.05 µM 0.226× (z -9.3) |
| [[SNU-423 (line)]] | alt | 7.33 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.42× (z +10.0) | — |
| [[SW480 (line)]] | alt | 5.64 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +10.1) | [[Ixazomib citrate (drug)]] 5 µM 0.189× (z -8.6) ⚠ cell-cycle shift, explains ~18% of this change |
| [[A498 (line)]] | wt | 2.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.01× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 3.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.43× (z +9.7) | — |
| [[HepG2_C3A (line)]] | wt | 5.94 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0494× (z -9.3) |
| [[HOP62 (line)]] | alt | 5.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.49× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 6.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.00× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 4.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.18× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.172× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~61% of this change |
| [[Panc 03.27 (line)]] | alt | 2.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.69× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 7.44 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0742× (z -9.1) ⚠ cell-cycle shift, explains ~18% of this change |
| [[SW1417 (line)]] | alt | 9.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +11.1) | — |
| [[A-427 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13368), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFV2-AS1]] | +0.72 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[CREBRF]] | +0.69 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[RSRP1]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[CCNG2]] | +0.68 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[C11orf71]] | +0.67 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[OSER1]] | +0.66 | +0.49 / +0.70 | both halves | 1e-05 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[HBP1]] | +0.66 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[CLK1]] | +0.66 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[WBP1]] | +0.66 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[EIF3J-DT]] | +0.65 | +0.69 / +0.63 | both halves | 7e-06 | same gene group |
| [[C14orf28]] | +0.64 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[TCP11L2]] | +0.63 | +0.38 / +0.65 | both halves | 6e-05 |  |
| [[CCDC115]] | +0.63 | +0.66 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCOF1]] | -0.67 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[EIF2B3]] | -0.64 | -0.29 / -0.63 | both halves | 2e-04 |  |
| [[PPP5C]] | -0.63 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[SNRPD1]] | -0.63 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[HEATR3]] | -0.63 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[TEX2]] | -0.62 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[PA2G4]] | -0.62 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.61 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[EIPR1]] | -0.61 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[INTS7]] | -0.61 | -0.42 / -0.64 | both halves | 4e-05 |  |
| [[URB2]] | -0.61 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[TOMM40]] | -0.61 | -0.64 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers OSER1-DT's level | compounds that target MTOR: 5 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Temsirolimus) | 62% of the class's compounds vs 9.8% of all compounds | 0.095 | ⚠ off-target possible; 5 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.735). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.3, -41.3); signed map (-11.5, 8.7). **Vector** length 69.0, 11.2% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +22.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +14.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.4 | +9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.2 | +2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +8.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.0 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.7 | +4.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +1.7 | +3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +2.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.9 | -11.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -2.8 | -3.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -4.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +0.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -4.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.2 | -3.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.2 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | OSER1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20q13.12 — chr20:44,210,907-44,226,027 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously OSER1-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48585](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48585) · Entrez [100505783](https://www.ncbi.nlm.nih.gov/gene/100505783) · Ensembl [ENSG00000223891](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000223891)

## Data

Gene col 13368: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13368); `tables/drug_effects.parquet` (75 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13368, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13368]; `tensor/DDL_lfc|DDL_z.npy` [13368]; `embed/gene_vectors.npy` [13368]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13368 or target_col == 13368). Every well: [[OSER1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSER1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
