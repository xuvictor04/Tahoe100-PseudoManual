---
symbol: "RAB5B"
type: "gene"
col: 3239
ensembl_id: "ENSG00000111540"
name: "RAB5B, member RAS oncogene family"
location: "12q13.2"
module: 1
arm: "-"
pooled_cpm: 50.63
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# RAB5B

*RAB5B, member RAS oncogene family* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +14.2, q 3e-43, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.641× (z -11.9, q 1e-29, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MXD4]] (+0.68, fdr 7e-06), [[MTCH1]] (+0.66, fdr 7e-06), [[ULK1]] (+0.65, fdr 7e-06); moves opposite to [[NOC3L]] (-0.65, fdr 7e-06), [[NAA15]] (-0.63, fdr 1e-05), [[CEP83]] (-0.62, fdr 7e-06).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3239.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +14.2 | 3e-43 | 45/49 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.3 | 9e-08 | 26/49 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.7 | 2e-06 | 27/48 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.20×** | +4.9 | 1e-04 | 21/48 (A549, NCI-H23, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.30×** | +4.7 | 4e-04 | 27/47 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.9 | 0.010 | 19/48 (SNU-1, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.8 | 0.014 | 23/47 (A-427, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.023 | 19/47 (SK-MEL-2, LoVo, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.025 | 19/48 (MIA PaCa-2, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Berbamine (drug)]] 5 µM |  | 1.14× | +3.5 | 0.028 | 13/49 (NCI-H23, LoVo, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.028 | 19/48 (KATO III, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.031 | 15/48 (LS 180, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.20× | +3.3 | 0.035 | 21/48 (PANC-1, HEC-1-A, …) | two highest doses | composition shift |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.054 | 16/48 (H4, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.070 | 8/49 (LoVo, Panc 03.27, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.074 | 14/48 (SW1417, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 1.18× | +3.0 | 0.084 | 12/48 (AsPC-1, LoVo, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3239.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.641×** | -11.9 | 1e-29 | 39/48 (NCI-H2347, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.553×** | -11.2 | 1e-26 | 41/47 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.540×** | -11.1 | 1e-26 | 40/48 (HCT15, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.682×** | -7.2 | 8e-11 | 37/48 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.691×** | -7.0 | 4e-10 | 35/48 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.840× | -4.6 | 3e-04 | 23/48 (RPMI-7951, NCI-H1573, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.793×** | -4.4 | 1e-03 | 21/48 (AsPC-1, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.800×** | -4.2 | 0.002 | 23/48 (SW480, NCI-H1792, …) | two highest doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.822×** | -3.6 | 0.023 | 18/49 (hTERT-HPNE, SNU-423, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.828×** | -3.4 | 0.034 | 17/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -3.3 | 0.044 | 17/48 (CHP-212, LoVo, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.889× | -3.2 | 0.075 | 5/48 (CFPAC-1, SW 900, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | 0.851× | -3.0 | 0.10 | 19/48 (RPMI-7951, AsPC-1, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3239. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 55.2 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.212× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.428× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 65.0 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -14.8) |
| [[PANC-1 (line)]] | alt | 50.7 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -13.6) |
| [[RKO (line)]] | wt | 47.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.296× (z -11.0) |
| [[A-172 (line)]] | wt | 52.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +9.2) | — |
| [[A549 (line)]] | wt | 41.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 41.5 | 0 | 2 (2 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0785× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 53.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.236× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 48.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.2) | [[Harringtonine (drug)]] 5 µM 0.392× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 74.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +11.2) | [[Lonafarnib (drug)]] 5 µM 0.170× (z -10.0) ⚠ toxic |
| [[A-427 (line)]] | wt | 77.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -14.1) |
| [[A498 (line)]] | wt | 46.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.3) | — |
| [[AsPC-1 (line)]] | alt | 78.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.367× (z -10.5) |
| [[BT-474 (line)]] | alt | 61.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 58.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -13.4) |
| [[H4 (line)]] | wt | 47.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -12.3) |
| [[HCT15 (line)]] | alt | 67.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.151× (z -15.4) |
| [[HEC-1-A (line)]] | alt | 37.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 44.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 65.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 43.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 40.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.311× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 41.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +11.9) | — |
| [[SHP-77 (line)]] | alt | 26.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 52.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +12.1) | — |
| [[SW480 (line)]] | alt | 53.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +12.1) | — |
| [[AN3 CA (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3239), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXD4]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[MTCH1]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ULK1]] | +0.65 | +0.65 / +0.69 | both halves | 7e-06 | pathway: RAB GEFs exchange GTP for GDP on RABs |
| [[WIPI2]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ADIPOR1]] | +0.63 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[ZFYVE21]] | +0.61 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[NLGN2]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[GUCD1]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[GPBP1L1]] | +0.60 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[WDR20]] | +0.59 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[PBXIP1]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[HINFP]] | +0.59 | +0.59 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOC3L]] | -0.65 | -0.64 / -0.66 | both halves | 7e-06 |  |
| [[NAA15]] | -0.63 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[CEP83]] | -0.62 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[ATIC]] | -0.62 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[RIF1]] | -0.61 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[ABCE1]] | -0.61 | -0.67 / -0.57 | both halves | 9e-06 |  |
| [[C12orf29]] | -0.61 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[SERBP1]] | -0.60 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[PCNX2]] | -0.59 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[TCERG1]] | -0.59 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[COA7]] | -0.59 | -0.60 / -0.57 | both halves | 9e-06 |  |
| [[PAK1IP1]] | -0.58 | -0.55 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RAB5B's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.608). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.6, -36.8); signed map (-22.2, 8.7). **Vector** length 118, 30.8% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.7 | +14.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +5.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +6.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +5.0 | +4.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.4 | +3.6 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +3.5 | +4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.5 | +3.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.3 | +3.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.5 | -11.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.5 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.1 | -11.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.0 | -11.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.4 | -2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | RAB5B, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.2 — chr12:55,973,913-55,996,683 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 12 pathways, smallest: Respiratory syncytial virus (RSV) attachment and entry; TBC/RABGAPs; RAB geranylgeranylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P61020](https://www.uniprot.org/uniprotkb/P61020) (Ras-related protein Rab-5B):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. Involved in early endocytic trafficking. Required for EEA1 recruitment to early endosomes. Required for EGF and …

**Summary**, from NCBI Gene [5869](https://www.ncbi.nlm.nih.gov/gene/5869):

> Enables G protein activity; GDP binding activity; and GTP-dependent protein binding activity. Involved in several processes, including endocytosis; endosomal transport; and plasma membrane to endosome transport. Located in endosome and extracellular exosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9784](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9784) · Entrez [5869](https://www.ncbi.nlm.nih.gov/gene/5869) · UniProt [P61020](https://www.uniprot.org/uniprotkb/P61020) · Ensembl [ENSG00000111540](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111540)

## Data

Gene col 3239: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3239); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3239, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3239]; `tensor/DDL_lfc|DDL_z.npy` [3239]; `embed/gene_vectors.npy` [3239]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3239 or target_col == 3239). Every well: [[RAB5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
