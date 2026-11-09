---
symbol: "AHRR"
type: "gene"
col: 728
ensembl_id: "ENSG00000063438"
name: "aryl hydrocarbon receptor repressor"
location: "5p15.33"
module: 47
arm: "+"
pooled_cpm: 55.11
n_lines_expressing: 47
n_dd_up: 13
n_dd_down: 19
n_dd_up_clean: 13
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# AHRR

*aryl hydrocarbon receptor repressor* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.83× (z +9.8, q 8e-20, up in 31 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.673× (z -6.4, q 1e-07, down in 25 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ORAI2]] (+0.64, fdr 7e-06), [[ZDHHC11]] (+0.63, fdr 1e-05), [[PDE2A]] (+0.63, fdr 1e-05); moves opposite to [[CHPT1]] (-0.56, fdr 1e-05), [[PIGB]] (-0.54, fdr 3e-05), [[PEX2]] (-0.51, fdr 2e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CFAP161]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SCART1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 728.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.83×** | +9.8 | 8e-20 | 31/45 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +7.4 | 3e-11 | 25/44 (HS-578T, H4, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +6.1 | 2e-07 | 23/45 (LOX-IMVI, RKO, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Menadione (drug)]] 5 µM |  | **1.40×** | +5.2 | 2e-05 | 23/44 (NCI-H460, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.38×** | +5.2 | 2e-05 | 23/45 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Gemcitabine (drug)]] 0.05 µM |  | **1.29×** | +4.8 | 2e-04 | 19/45 (HS-578T, NCI-H1792, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +4.7 | 2e-04 | 21/45 (COLO 205, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lucanthone (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.014 | 18/45 (SW480, RPMI-7951, …) | top dose only |  |
| [[Gemcitabine (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.050 | 12/45 (NCI-H1792, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.059 | 9/45 (SW480, NCI-H1792, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.066 | 7/45 (RPMI-7951, SW480, …) | all doses, flat |  |
| [[Meloxicam (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.078 | 7/45 (RPMI-7951, LS 180, …) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.085 | 13/45 (SW480, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 728.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.673×** | -6.4 | 1e-07 | 25/45 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.498×** | -5.9 | 1e-06 | 23/46 (A-427, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.700×** | -5.7 | 2e-06 | 27/45 (KATO III, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.703×** | -5.7 | 2e-06 | 25/45 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **0.717×** | -5.4 | 1e-05 | 23/44 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.728×** | -5.1 | 3e-05 | 23/43 (KATO III, J82, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.749×** | -4.6 | 3e-04 | 21/45 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.758×** | -4.4 | 6e-04 | 23/45 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.750×** | -4.4 | 6e-04 | 19/41 (KATO III, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.766×** | -4.3 | 0.001 | 22/45 (SW 900, KATO III, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.625×** | -4.0 | 0.004 | 15/44 (SW 900, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.847× | -3.8 | 0.008 | 18/45 (AsPC-1, SW1417, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.759×** | -3.7 | 0.010 | 17/45 (SW 900, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.765×** | -3.6 | 0.013 | 16/44 (A549, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.800×** | -3.6 | 0.013 | 16/45 (SW 900, HOP62, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.802×** | -3.4 | 0.024 | 15/45 (SW 900, HOP62, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.669×** | -3.4 | 0.024 | 18/44 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.812×** | -3.3 | 0.027 | 12/45 (SW 900, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 728. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 114 | 0 | 11 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0890× (z -25.0) |
| [[C32 (line)]] | wt | 50.4 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +12.3) | [[PH-797804 (drug)]] 5 µM 0.0907× (z -9.7) |
| [[SW 900 (line)]] | alt | 232 | 0 | 5 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.181× (z -10.6) |
| [[HS-578T (line)]] | alt | 66.6 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.86× (z +24.4) | — |
| [[J82 (line)]] | alt | 99.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.369× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.469× (z -8.5) |
| [[LoVo (line)]] | wt | 47.8 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.321× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.360× (z -9.4) |
| [[HOP62 (line)]] | alt | 108 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.305× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.359× (z -8.6) |
| [[HT-29 (line)]] | alt | 72.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.193× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.241× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 40.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +9.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.210× (z -11.9) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 40.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +16.9) | — |
| [[SW1417 (line)]] | alt | 42.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -12.0) |
| [[A498 (line)]] | wt | 43.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -12.8) |
| [[A549 (line)]] | wt | 26.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +9.6) | — |
| [[H4 (line)]] | wt | 108 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +21.4) | — |
| [[LS 180 (line)]] | wt | 37.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[RKO (line)]] | wt | 19.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +9.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 20.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +9.2) | — |
| [[A-427 (line)]] | wt | 104 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.152× (z -10.7) |
| [[BT-474 (line)]] | alt | 66.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 56.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.215× (z -11.4) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 99.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 47.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[LOX-IMVI (line)]] | wt | 27.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +11.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 24.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 23.1 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.99× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.202× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~21% of this change |
| [[RPMI-7951 (line)]] | alt | 116 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 86.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +8.9) | — |
| [[SW 1088 (line)]] | alt | 72.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +9.8) | — |
| [[SW48 (line)]] | wt | 47.1 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0420× (z -8.9) |
| [[AN3 CA (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 97.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.43 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 71.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 728), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ORAI2]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ZDHHC11]] | +0.63 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[PDE2A]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[POU2F2]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[UCKL1-AS1]] | +0.62 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[ASGR1]] | +0.61 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[HPX]] | +0.61 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[AMZ1]] | +0.61 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[SH2D4B]] | +0.60 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[PILRA]] | +0.59 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[CYP2E1]] | +0.59 | +0.64 / +0.51 | both halves | 1e-05 | pathway: Biological oxidations |
| [[GARIN1B]] | +0.59 | +0.60 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHPT1]] | -0.56 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[PIGB]] | -0.54 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[PEX2]] | -0.51 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[FBXO7]] | -0.49 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[DRAM2]] | -0.49 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[OSBPL1A]] | -0.49 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[TNRC6A]] | -0.49 | -0.53 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFAP161]] | B | CFAP161 activity raises AHRR's level | lines that do not express CFAP161 (6) vs lines expressing it (44) | 2.15× lower at baseline in the lines without CFAP161 | 0.060 | ⚠ within organs, on part of the lines; also absent: CRB1; maybe low, not absent; its own permutation p |
| [[CYP2E1]], [[SCART1]] | C | CYP2E1, SCART1 activity raises AHRR's level | lines that do not express CYP2E1, SCART1 (3) vs lines expressing them (47) | 3.53× lower at baseline in the lines without CYP2E1, SCART1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AHRR, ARHGAP15, FAT1; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCART1]] | C | AHRR activity raises SCART1's level | lines that do not express AHRR (3) vs lines expressing it (47) | 3.13× lower at baseline in the lines without AHRR | 0.035 | ⚠ few lines (3 vs 47); across organs; also absent: ZFP36, CYP2E1, BIVM; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.654). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.4, -13.1); signed map (18.1, 16.0). **Vector** length 100, 23.1% of its response variance represented; |z| ≥ 3 in 1,259 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +6.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +1.0 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.8 | +2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.9 | +2.5 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -5.0 | -3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.7 | -3.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.5 | -4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.2 | -4.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.4 | -3.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.1 | -1.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.7 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | aryl hydrocarbon receptor repressor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.33 — chr5:321,714-438,291 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1234, bHLHe77; previously AHH, AHHR |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; PAS domain containing |
| Reactome | 9 pathways, smallest: Aryl hydrocarbon receptor signalling; Xenobiotics; Endogenous sterols |
| Matched by | ensembl_id |

**Function**, from UniProt [A9YTQ3](https://www.uniprot.org/uniprotkb/A9YTQ3) (Aryl hydrocarbon receptor repressor):

> Mediates dioxin toxicity and is involved in regulation of cell growth and differentiation. Represses the transcription activity of AHR by competing with AHR for heterodimer formation with ARNT and subsequently binding to the xenobiotic response element (XRE) sequence present in the promoter regulatory region of a variety of genes. Represses CYP1A1 by binding the XRE sequence and recruiting ANKRA2, HDAC4 and/or HDAC5. Autoregulates its expression by associating with its own XRE site.; [Isoform …

**Summary**, from NCBI Gene [57491](https://www.ncbi.nlm.nih.gov/gene/57491):

> The protein encoded by this gene participates in the aryl hydrocarbon receptor (AhR) signaling cascade, which mediates dioxin toxicity, and is involved in regulation of cell growth and differentiation. It functions as a feedback modulator by repressing AhR-dependent gene expression. Alternatively spliced transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:346](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:346) · Entrez [57491](https://www.ncbi.nlm.nih.gov/gene/57491) · UniProt [A9YTQ3](https://www.uniprot.org/uniprotkb/A9YTQ3) · Ensembl [ENSG00000063438](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000063438)

## Data

Gene col 728: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 728); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 728, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 728]; `tensor/DDL_lfc|DDL_z.npy` [728]; `embed/gene_vectors.npy` [728]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 728 or target_col == 728). Every well: [[AHRR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AHRR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
