---
symbol: "AGPAT1"
type: "gene"
col: 12849
ensembl_id: "ENSG00000204310"
name: "1-acylglycerol-3-phosphate O-acyltransferase 1"
location: "6p21.32"
module: 50
arm: "+"
pooled_cpm: 18.75
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 21
n_dd_up_clean: 3
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# AGPAT1

*1-acylglycerol-3-phosphate O-acyltransferase 1* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.10× (z +18.6, q 0e+00, up in 41 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.34× (z +5.5, q 5e-06, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.454× (z -10.4, q 8e-23, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITM2C]] (+0.73, fdr 7e-06), [[TMEM30A]] (+0.71, fdr 7e-06), [[ARF3]] (+0.70, fdr 7e-06); moves opposite to [[DNAJC2]] (-0.63, fdr 2e-05), [[ADRM1]] (-0.58, fdr 1e-05), [[ATF4]] (-0.57, fdr 3e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MYL9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12849.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.10×** | +18.6 | 0e+00 | 41/41 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.15×** | +18.1 | 0e+00 | 31/31 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.71×** | +12.2 | 8e-32 | 35/37 (MIA PaCa-2, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +5.5 | 5e-06 | 26/48 (J82, MIA PaCa-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.49×** | +5.3 | 1e-05 | 27/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.45×** | +4.9 | 7e-05 | 27/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.29×** | +4.8 | 1e-04 | 23/46 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +4.7 | 1e-04 | 21/45 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.45×** | +4.7 | 2e-04 | 24/48 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.003 | 18/48 (A-172, HOP62, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.34×** | +3.9 | 0.006 | 17/47 (KATO III, LS 180, …) | rises with dose |  |
| [[palbociclib (drug)]] 5 µM |  | **1.61×** | +3.3 | 0.049 | 5/46 (A-427, PANC-1, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12849.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.454×** | -10.4 | 8e-23 | 41/47 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.607×** | -9.3 | 3e-18 | 36/47 (SHP-77, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.501×** | -9.1 | 1e-17 | 37/46 (H4, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.507×** | -7.9 | 6e-13 | 35/48 (SK-MEL-2, J82, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.579×** | -7.2 | 5e-11 | 38/48 (A-427, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.605×** | -6.6 | 3e-09 | 34/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.635×** | -6.0 | 2e-07 | 27/48 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **0.737×** | -5.7 | 8e-07 | 34/48 (NCI-H2030, SW 900, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.467×** | -5.3 | 8e-06 | 26/38 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.672×** | -5.3 | 8e-06 | 26/47 (COLO 205, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.500×** | -4.8 | 9e-05 | 22/46 (SK-MEL-2, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Delamanid (drug)]] 0.05 µM |  | **0.733×** | -4.1 | 0.002 | 21/48 (C32, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.733×** | -4.0 | 0.003 | 18/48 (MIA PaCa-2, NCI-H23, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.734×** | -3.9 | 0.003 | 18/47 (CFPAC-1, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.749×** | -3.8 | 0.005 | 20/47 (SNU-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.667×** | -3.8 | 0.005 | 21/48 (H4, SHP-77, …) | all doses, flat | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12849. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 26.1 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +14.4) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.143× (z -9.8) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.410× (z -8.6) |
| [[HOP62 (line)]] | alt | 27.2 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.308× (z -9.2) |
| [[HS-578T (line)]] | alt | 22.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +10.7) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.293× (z -8.7) |
| [[J82 (line)]] | alt | 26.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.92× (z +11.6) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.263× (z -8.8) |
| [[KATO III (line)]] | alt | 14.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 6.10× (z +9.5) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.0521× (z -16.1) |
| [[MIA PaCa-2 (line)]] | alt | 32.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.49× (z +12.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 15.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.53× (z +10.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 17.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.55× (z +10.2) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 20.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -10.7) |
| [[H4 (line)]] | wt | 23.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.69× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0644× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 16.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.42× (z +12.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 21.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +10.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 14.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.31× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 32.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.308× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 15.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.80× (z +10.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 19.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.36× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 19.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.19× (z +9.0) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.0693× (z -12.6) |
| [[SNU-423 (line)]] | alt | 24.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 15.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.53× (z +11.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 31.0 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.332× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 13.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.91× (z +9.3) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 9.36 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 27.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.195× (z -9.1) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 8.75 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 16.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 29.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +10.6) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 14.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0945× (z -11.3) |
| [[SHP-77 (line)]] | alt | 17.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -10.0) |
| [[SW 900 (line)]] | alt | 24.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.46× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12849), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITM2C]] | +0.73 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[TMEM30A]] | +0.71 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[ARF3]] | +0.70 | +0.61 / +0.71 | both halves | 7e-06 | pathway: Phospholipid metabolism |
| [[BAG6]] | +0.70 | +0.71 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[PRKACA]] | +0.70 | +0.69 / +0.57 | both halves | 8e-06 | pathway: Integration of energy metabolism |
| [[BSG]] | +0.69 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[FAM234A]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[NAGA]] | +0.67 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[GANAB]] | +0.67 | +0.69 / +0.58 | both halves | 8e-06 |  |
| [[SELENON]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[LAMP1]] | +0.64 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[FKBP1A]] | +0.64 | +0.63 / +0.52 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC2]] | -0.63 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[ADRM1]] | -0.58 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[ATF4]] | -0.57 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[NDUFB9]] | -0.56 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[PSMA7]] | -0.56 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[TATDN1]] | -0.55 | -0.61 / -0.46 | both halves | 3e-05 | same gene group |
| [[TTC4]] | -0.55 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[DNTTIP2]] | -0.55 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[LRSAM1]] | -0.54 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[ZNF286B]] | -0.54 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[NME6]] | -0.53 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[ZNF593]] | -0.53 | -0.44 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYL9]] | B | MYL9 activity raises AGPAT1's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 1.39× lower at baseline in the lines without MYL9 | 0.039 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[LGALS3BP]] | B | LGALS3BP activity lowers AGPAT1's level | lines that do not express LGALS3BP (7) vs lines expressing it (43) | 1.40× higher at baseline in the lines without LGALS3BP | 0.047 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[TOP2A]] | B | TOP2A activity lowers AGPAT1's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.775). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.0, -22.1); signed map (-27.4, -38.8). **Vector** length 83.9, 17.9% of its response variance represented; |z| ≥ 3 in 1,015 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +18.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +18.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +12.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +0.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.7 | +5.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | -2.8 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +1.5 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +4.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.0 | -9.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.5 | -7.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.0 | -10.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.1 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | -6.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.2 | -3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | 1-acylglycerol-3-phosphate O-acyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:32,168,212-32,178,096 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LPAAT-alpha, LPLAT1 |
| Gene groups (HGNC) | 1-acylglycerol-3-phosphate O-acyltransferases; MicroRNA protein coding host genes; Lysophospholipid acyltransferases |
| Reactome | 6 pathways, smallest: ChREBP activates metabolic gene expression; Synthesis of PA; Integration of energy metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99943](https://www.uniprot.org/uniprotkb/Q99943) (1-acyl-sn-glycerol-3-phosphate acyltransferase alpha):

> Converts 1-acyl-sn-glycerol-3-phosphate (lysophosphatidic acid or LPA) into 1,2-diacyl-sn-glycerol-3-phosphate (phosphatidic acid or PA) by incorporating an acyl moiety at the sn-2 position of the glycerol backbone.

**Summary**, from NCBI Gene [10554](https://www.ncbi.nlm.nih.gov/gene/10554):

> This gene encodes an enzyme that converts lysophosphatidic acid (LPA) into phosphatidic acid (PA). LPA and PA are two phospholipids involved in signal transduction and in lipid biosynthesis in cells. This enzyme localizes to the endoplasmic reticulum. This gene is located in the class III region of the human major histocompatibility complex. Alternative splicing results in two transcript variants encoding the same protein. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:324](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:324) · Entrez [10554](https://www.ncbi.nlm.nih.gov/gene/10554) · UniProt [Q99943](https://www.uniprot.org/uniprotkb/Q99943) · Ensembl [ENSG00000204310](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204310)

## Data

Gene col 12849: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12849); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12849, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12849]; `tensor/DDL_lfc|DDL_z.npy` [12849]; `embed/gene_vectors.npy` [12849]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12849 or target_col == 12849). Every well: [[AGPAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGPAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
