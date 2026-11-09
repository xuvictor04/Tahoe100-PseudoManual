---
symbol: "SIAE"
type: "gene"
col: 3100
ensembl_id: "ENSG00000110013"
name: "sialic acid acetylesterase"
location: "11q24.2"
module: 50
arm: "+"
pooled_cpm: 17.51
n_lines_expressing: 48
n_dd_up: 21
n_dd_down: 18
n_dd_up_clean: 14
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# SIAE

*sialic acid acetylesterase* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.74× (z +14.2, q 3e-43, up in 34 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +10.6, q 8e-24, up in 35 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.448× (z -15.9, q 0e+00, down in 37 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUMF2]] (+0.67, fdr 7e-06), [[MATN3]] (+0.57, fdr 6e-05), [[CST3]] (+0.56, fdr 3e-05); moves opposite to [[SDHAF2]] (-0.57, fdr 4e-05), [[UBXN4]] (-0.53, fdr 1e-05), [[ZNF222]] (-0.53, fdr 4e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3100.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.74×** | +14.2 | 3e-43 | 34/37 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.81×** | +14.0 | 4e-42 | 28/30 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +10.6 | 8e-24 | 35/43 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +10.5 | 2e-23 | 27/35 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +6.9 | 6e-10 | 32/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +6.8 | 1e-09 | 21/44 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +6.3 | 3e-08 | 21/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +5.2 | 1e-05 | 23/46 (SW1417, PANC-1, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.56×** | +4.5 | 5e-04 | 15/42 (A498, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.3 | 0.001 | 20/46 (A498, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.36×** | +4.2 | 0.001 | 17/46 (LOX-IMVI, A498, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.31×** | +3.9 | 0.005 | 15/46 (PANC-1, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +3.8 | 0.006 | 16/46 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.30×** | +3.6 | 0.014 | 13/41 (NCI-H1573, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.016 | 11/45 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.021 | 12/46 (PANC-1, KATO III, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.021 | 8/43 (J82, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.022 | 10/45 (A498, HT-29, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +3.1 | 0.060 | 5/46 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +2.9 | 0.091 | 9/46 (AsPC-1, NCI-H23, …) | top dose only |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.24×** | +2.9 | 0.091 | 2/45 (KATO III, A498) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3100.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.448×** | -15.9 | 0e+00 | 37/45 (Hs 766T, HT-29, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.532×** | -8.8 | 3e-16 | 31/45 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.567×** | -7.9 | 4e-13 | 29/44 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.588×** | -7.0 | 3e-10 | 31/45 (HT-29, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.609×** | -6.7 | 3e-09 | 28/45 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.706×** | -4.9 | 1e-04 | 22/45 (PANC-1, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.722×** | -4.5 | 5e-04 | 22/46 (KATO III, C-33 A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.562×** | -4.2 | 0.002 | 17/37 (SHP-77, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.741×** | -4.2 | 0.002 | 20/46 (HOP62, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.810×** | -4.1 | 0.002 | 19/46 (Panc 03.27, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.747×** | -4.1 | 0.002 | 20/46 (LOX-IMVI, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.585×** | -3.9 | 0.004 | 16/42 (NCI-H1573, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.760×** | -3.8 | 0.006 | 11/46 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.762×** | -3.8 | 0.006 | 18/43 (HT-29, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.764×** | -3.7 | 0.007 | 20/45 (HS-578T, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.796×** | -3.2 | 0.046 | 10/45 (A549, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3100. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 59.2 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 20.2 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -15.6) |
| [[LS 180 (line)]] | wt | 50.3 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -16.6) |
| [[PANC-1 (line)]] | alt | 17.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -13.8) |
| [[HT-29 (line)]] | alt | 19.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -19.7) |
| [[NCI-H1573 (line)]] | alt | 12.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 8.19× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -8.5) |
| [[A498 (line)]] | wt | 10.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +11.5) | — |
| [[A549 (line)]] | wt | 13.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 15.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.81× (z +11.7) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 31.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -23.8) |
| [[MIA PaCa-2 (line)]] | alt | 21.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.24× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 14.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.86× (z +9.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 8.00 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -9.2) |
| [[C-33 A (line)]] | alt | 14.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.122× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 16.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -14.8) |
| [[H4 (line)]] | wt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -8.8) |
| [[HOP62 (line)]] | alt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -12.6) |
| [[LoVo (line)]] | wt | 28.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 16.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.12× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 15.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.134× (z -10.2) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -9.6) |
| [[RKO (line)]] | wt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -11.3) |
| [[SHP-77 (line)]] | alt | 28.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.99× (z +9.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.95 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3100), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUMF2]] | +0.67 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[MATN3]] | +0.57 | +0.58 / +0.38 | both halves | 6e-05 |  |
| [[CST3]] | +0.56 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[SELENON]] | +0.56 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[ATP6AP2]] | +0.55 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[BSG]] | +0.54 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[GAA]] | +0.54 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[ITM2B]] | +0.54 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[CTSZ]] | +0.54 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[GM2A]] | +0.54 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[ARSA]] | +0.54 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[FAM210B]] | +0.53 | +0.58 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAF2]] | -0.57 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[UBXN4]] | -0.53 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ZNF222]] | -0.53 | -0.52 / -0.40 | both halves | 4e-05 |  |
| [[NSRP1]] | -0.52 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[GLRX2]] | -0.51 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[NME6]] | -0.50 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[ZNF761]] | -0.49 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[DNTTIP2]] | -0.49 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[PSMB6]] | -0.49 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[PSMD7]] | -0.49 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[OSGIN1]] | -0.49 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[DAXX]] | -0.49 | -0.39 / -0.45 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SIAE's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CTSF]] | B | CTSF activity raises SIAE's level | lines that do not express CTSF (16) vs lines expressing it (34) | 1.19× lower at baseline in the lines without CTSF | 0.087 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, LINC01725, BVES |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.615). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.0, -19.2); signed map (-26.0, -37.3). **Vector** length 72.1, 13.7% of its response variance represented; |z| ≥ 3 in 918 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +14.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +14.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +6.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +3.5 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +4.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.3 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.3 | -15.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.0 | -6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -7.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.3 | -7.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.0 | -8.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -4.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.8 | -1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | sialic acid acetylesterase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:124,633,113-124,695,707 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CSE-C, MGC87009, LSE; previously YSG2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAT2](https://www.uniprot.org/uniprotkb/Q9HAT2) (Sialate O-acetylesterase):

> Catalyzes the removal of O-acetyl ester groups from position 9 of the free diacetylated sialate N-acetyl-9-O-acetylneuraminate (Neu5,9Ac2) in the cytosol and of the diacetylated sialate residues of sialylglycoconjugates in the lysosomes (Probable). Together with the sialate-O-acetyltransferase they regulate the balance of acetylated sialoglycoconjugates, key players in various processes such as cell-cell interactions, host-pathogen recognition, and tumor antigenicity.

**Summary**, from NCBI Gene [54414](https://www.ncbi.nlm.nih.gov/gene/54414):

> This gene encodes an enzyme which removes 9-O-acetylation modifications from sialic acids. Mutations in this gene are associated with susceptibility to autoimmune disease 6. Multiple transcript variants encoding different isoforms, found either in the cytosol or in the lysosome, have been found for this gene.[provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:18187](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18187) · Entrez [54414](https://www.ncbi.nlm.nih.gov/gene/54414) · UniProt [Q9HAT2](https://www.uniprot.org/uniprotkb/Q9HAT2) · Ensembl [ENSG00000110013](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110013)

## Data

Gene col 3100: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3100); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3100, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3100]; `tensor/DDL_lfc|DDL_z.npy` [3100]; `embed/gene_vectors.npy` [3100]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3100 or target_col == 3100). Every well: [[SIAE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIAE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
