---
symbol: "CDC42EP1"
type: "gene"
col: 4871
ensembl_id: "ENSG00000128283"
name: "CDC42 effector protein 1"
location: "22q13.1"
module: 43
arm: "-"
pooled_cpm: 13.73
n_lines_expressing: 45
n_dd_up: 16
n_dd_down: 26
n_dd_up_clean: 10
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# CDC42EP1

*CDC42 effector protein 1* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.78× (z +8.7, q 2e-15, up in 22 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.265× (z -20.1, q 0e+00, down in 38 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAF4]] (+0.64, fdr 7e-06), [[PLD6]] (+0.60, fdr 1e-05), [[LACC1]] (+0.60, fdr 1e-05); moves opposite to [[GLG1]] (-0.65, fdr 1e-05), [[TYW1]] (-0.63, fdr 2e-05), [[EIF3K]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HCP5]] → it (grade B ⚠); 3 go from it, the strongest it → [[ZC3H7B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4871.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.78×** | +8.7 | 2e-15 | 22/40 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +8.6 | 2e-15 | 26/41 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.67×** | +7.6 | 3e-12 | 24/42 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.66×** | +7.6 | 3e-12 | 20/34 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +7.4 | 1e-11 | 9/23 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +6.2 | 5e-08 | 23/42 (HS-578T, A498, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.33×** | +6.1 | 9e-08 | 21/39 (A498, HOP62, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.37×** | +4.7 | 2e-04 | 17/36 (NCI-H1792, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +4.4 | 6e-04 | 9/43 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.32×** | +4.1 | 0.002 | 15/41 (NCI-H460, C32, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.8 | 0.007 | 11/38 (HS-578T, HOP62, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.007 | 7/42 (NCI-H460, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.29×** | +3.8 | 0.007 | 8/43 (SW480, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.53×** | +3.3 | 0.033 | 7/39 (NCI-H460, COLO 205, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.051 | 7/41 (NCI-H460, NCI-H23, …) | two highest doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.067 | 3/40 (HCT15, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4871.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.265×** | -20.1 | 0e+00 | 38/42 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.265×** | -20.0 | 0e+00 | 41/43 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.398×** | -13.9 | 1e-41 | 36/43 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.575×** | -8.4 | 8e-15 | 28/43 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.560×** | -8.3 | 1e-14 | 28/41 (COLO 205, A-172, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.367×** | -7.9 | 2e-13 | 27/42 (A549, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.415×** | -6.9 | 3e-10 | 30/39 (LoVo, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.742×** | -6.4 | 1e-08 | 22/40 (CFPAC-1, Panc 03.27, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.669×** | -6.1 | 7e-08 | 24/42 (COLO 205, KATO III, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.482×** | -5.8 | 5e-07 | 19/42 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.492×** | -5.6 | 1e-06 | 19/33 (HepG2/C3A, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.730×** | -4.8 | 8e-05 | 17/42 (KATO III, COLO 205, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.745×** | -4.5 | 3e-04 | 16/39 (A-427, C32, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.738×** | -4.4 | 4e-04 | 14/40 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.575×** | -4.4 | 5e-04 | 17/38 (CFPAC-1, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.772×** | -3.7 | 0.007 | 12/41 (BT-474, SW480, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.638×** | -3.6 | 0.012 | 13/40 (PANC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.721×** | -3.5 | 0.012 | 8/42 (A498, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.793×** | -3.5 | 0.012 | 14/42 (NCI-H2347, A549, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4871. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 24.9 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -14.1) |
| [[Panc 03.27 (line)]] | alt | 24.8 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 37.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -14.4) |
| [[COLO 205 (line)]] | alt | 34.7 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0800× (z -13.7) |
| [[KATO III (line)]] | alt | 26.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -11.4) |
| [[PANC-1 (line)]] | alt | 16.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.168× (z -13.5) |
| [[LoVo (line)]] | wt | 19.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -16.2) |
| [[NCI-H1573 (line)]] | alt | 14.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0747× (z -15.9) |
| [[SW480 (line)]] | alt | 10.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -11.6) |
| [[A-172 (line)]] | wt | 15.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.204× (z -10.0) |
| [[A498 (line)]] | wt | 20.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +12.8) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.08× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 17.3 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 22.5 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +8.6) ⚠ cell-cycle shift, explains ~48% of this change | [[Bendamustine (drug)]] 5 µM 0.148× (z -9.2) |
| [[HOP62 (line)]] | alt | 8.96 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +9.9) ⚠ cell-cycle shift, explains ~48% of this change | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -9.2) |
| [[J82 (line)]] | alt | 17.1 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +9.7) ⚠ cell-cycle shift, explains ~48% of this change | [[Panobinostat (drug)]] 5 µM 0.201× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 19.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0957× (z -13.5) |
| [[SW48 (line)]] | wt | 18.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0892× (z -11.0) |
| [[A-427 (line)]] | wt | 8.01 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 4.27 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +8.9) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[HS-578T (line)]] | alt | 16.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +9.3) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[LS 180 (line)]] | wt | 14.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.238× (z -8.7) |
| [[SW1417 (line)]] | alt | 16.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +9.0) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[A549 (line)]] | wt | 9.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.995 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.24 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.875 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4871), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAF4]] | +0.64 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[PLD6]] | +0.60 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[LACC1]] | +0.60 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[TRIP6]] | +0.58 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[RAP2C]] | +0.57 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[PLXNB2]] | +0.57 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[GRINA]] | +0.56 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[ZNF641]] | +0.56 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[LGALSL-DT]] | +0.56 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[PNRC2]] | +0.56 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[ZNF681]] | +0.56 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[ZNF525]] | +0.55 | +0.46 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLG1]] | -0.65 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[TYW1]] | -0.63 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[EIF3K]] | -0.63 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[STRAP]] | -0.62 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[UQCRH]] | -0.61 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[SNRPD2]] | -0.61 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[RPL27A]] | -0.59 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[BIRC6]] | -0.59 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[RPLP0]] | -0.58 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[NME2]] | -0.58 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[RPS5]] | -0.58 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[COX6A1]] | -0.56 | -0.44 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HCP5]] | B | HCP5 activity raises CDC42EP1's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 1.81× lower at baseline in the lines without HCP5 | 0.073 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZC3H7B]] | B | CDC42EP1 activity lowers ZC3H7B's level | lines that do not express CDC42EP1 (5) vs lines expressing it (45) | 1.88× higher at baseline in the lines without CDC42EP1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZFP36, IQCN, SLC22A20P; its own permutation p |
| [[PHF19]] | B | CDC42EP1 activity lowers PHF19's level | lines that do not express CDC42EP1 (5) vs lines expressing it (45) | 1.60× higher at baseline in the lines without CDC42EP1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZFP36, IQCN, SLC22A20P; its own permutation p |
| [[BIRC6]] | B | CDC42EP1 activity raises BIRC6's level | lines that do not express CDC42EP1 (5) vs lines expressing it (45) | 1.19× lower at baseline in the lines without CDC42EP1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZFP36, IQCN, SLC22A20P |

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **-** arm (projection on the module's main direction -0.532). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (1.5, -22.8); signed map (19.0, -16.0). **Vector** length 89.3, 19.3% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.5 | +8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +6.1 | +6.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.5 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +8.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +6.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.2 | +3.2 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -4.2 | -6.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.2 | -7.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.2 | -8.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.9 | -6.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.1 | -3.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | CDC42 effector protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:37,560,480-37,569,405 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MSE55, CEP1, Borg5 |
| Gene groups (HGNC) | CDC42 effector proteins |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 10 pathways, smallest: RHOJ GTPase cycle; RHOQ GTPase cycle; RHOG GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00587](https://www.uniprot.org/uniprotkb/Q00587) (Cdc42 effector protein 1):

> Probably involved in the organization of the actin cytoskeleton. Induced membrane extensions in fibroblasts.

**Summary**, from NCBI Gene [11135](https://www.ncbi.nlm.nih.gov/gene/11135):

> CDC42 is a member of the Rho GTPase family that regulates multiple cellular activities, including actin polymerization. The protein encoded by this gene is a CDC42 binding protein that mediates actin cytoskeleton reorganization at the plasma membrane. This protein is secreted and is primarily found in bone marrow. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17014](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17014) · Entrez [11135](https://www.ncbi.nlm.nih.gov/gene/11135) · UniProt [Q00587](https://www.uniprot.org/uniprotkb/Q00587) · Ensembl [ENSG00000128283](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128283)

## Data

Gene col 4871: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4871); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4871, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4871]; `tensor/DDL_lfc|DDL_z.npy` [4871]; `embed/gene_vectors.npy` [4871]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4871 or target_col == 4871). Every well: [[CDC42EP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC42EP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
