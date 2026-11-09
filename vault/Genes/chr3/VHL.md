---
symbol: "VHL"
type: "gene"
col: 5509
ensembl_id: "ENSG00000134086"
name: "von Hippel-Lindau tumor suppressor"
location: "3p25.3"
module: 57
arm: "-"
pooled_cpm: 47.55
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# VHL

*von Hippel-Lindau tumor suppressor* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.85× (z +13.2, q 5e-37, up in 43 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.50× (z +9.1, q 3e-17, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.908× (z -7.6, q 2e-11, down in 0 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.822× (z -6.2, q 2e-07, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.551×, Hs 766T 0.477×); [[Bortezomib (drug)]] 5 µM in 1 line (SK-MEL-2 0.0825×; ⚠ toxic); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.248×; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.575×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GATD1]] (+0.60, fdr 2e-05), [[SPTY2D1OS]] (+0.51, fdr 1e-04), [[RAD51-AS1]] (+0.50, fdr 6e-05); moves opposite to [[SKP1]] (-0.47, fdr 4e-05), [[NDEL1]] (-0.46, fdr 5e-05), [[GLT8D1]] (-0.45, fdr 2e-04).
> It sits in the **-** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LIMCH1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5509.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +13.2 | 5e-37 | 43/47 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.50×** | +9.1 | 3e-17 | 35/48 (HS-578T, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +8.9 | 1e-16 | 37/47 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +7.3 | 3e-11 | 30/48 (LoVo, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +7.0 | 3e-10 | 31/48 (BT-474, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.32×** | +6.2 | 7e-08 | 28/48 (COLO 205, RKO, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +6.1 | 8e-08 | 28/47 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +6.0 | 1e-07 | 28/48 (SW480, HCT15, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +5.6 | 1e-06 | 23/48 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.18× | +5.2 | 1e-05 | 19/48 (SNU-423, A498, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.27×** | +4.9 | 5e-05 | 22/43 (A-427, LoVo, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +4.7 | 1e-04 | 22/48 (BT-474, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.21×** | +4.2 | 0.001 | 20/48 (NCI-H2347, NCI-H1792, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +4.2 | 0.001 | 8/48 (C32, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +3.8 | 0.006 | 15/48 (AsPC-1, A-172, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.013 | 14/48 (LS 180, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 1.11× | +3.4 | 0.020 | 7/48 (HOP62, A549, …) | rises with dose | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.034 | 3/48 (SW 1088, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5509.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.551×, Hs 766T 0.477×); [[Bortezomib (drug)]] 5 µM in 1 line (SK-MEL-2 0.0825×; ⚠ toxic); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.248×; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.575×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -7.6 | 2e-11 | 0/49 | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.822×** | -6.2 | 2e-07 | 27/48 (HEC-1-A, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.680×** | -4.5 | 0.001 | 20/48 (MIA PaCa-2, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.861× | -3.3 | 0.12 | 16/48 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | 0.756× | -3.3 | 0.13 | 9/47 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | 0.904× | -3.2 | 0.15 | 3/48 (Hs 766T, LOX-IMVI, …) | top dose only |  |
| [[Sonidegib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.868× | -3.1 | 0.15 | 3/48 (SNU-423, NCI-H23, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.873× | -3.0 | 0.18 | 18/48 (PANC-1, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5509. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 66.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.84× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 46.6 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.21× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +10.5) | — |
| [[KATO III (line)]] | alt | 48.3 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +9.3) | — |
| [[LoVo (line)]] | wt | 42.6 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.28× (z +9.9) | — |
| [[NCI-H460 (line)]] | wt | 35.9 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.40× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 48.4 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0825× (z -11.8) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 37.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -10.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 43.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.01× (z +10.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 24.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.58× (z +9.6) ⚠ toxic | — |
| [[COLO 205 (line)]] | alt | 31.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.06× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 87.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -11.9) |
| [[HOP62 (line)]] | alt | 56.5 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.575× (z -8.6) |
| [[Hs 766T (line)]] | wt | 81.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 50.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 68.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.542× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 44.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 57.1 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.02× (z +9.8) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5509), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATD1]] | +0.60 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[SPTY2D1OS]] | +0.51 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[RAD51-AS1]] | +0.50 | +0.54 / +0.38 | both halves | 6e-05 |  |
| [[PCCA-DT]] | +0.49 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[CDC42SE1]] | +0.49 | +0.47 / +0.38 | both halves | 6e-05 |  |
| [[TRIM13]] | +0.48 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[H6PD]] | +0.48 | +0.44 / +0.37 | both halves | 9e-05 |  |
| [[CROCCP2]] | +0.47 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[XIAP]] | +0.47 | +0.42 / +0.36 | both halves | 1e-04 |  |
| [[IRAK2]] | +0.47 | +0.47 / +0.47 | both halves | 2e-05 | pathway: SARS-CoV-1 Infection; ⚠ same locus (11.3 kb, same strand: neighbours can correlate without regulation) |
| [[VAMP2]] | +0.46 | +0.32 / +0.47 | both halves | 2e-04 |  |
| [[C5orf24]] | +0.45 | +0.24 / +0.59 | both halves | 5e-04 |  |
| [[HEXD]] | +0.44 | +0.40 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKP1]] | -0.47 | -0.41 / -0.51 | both halves | 4e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 620 |
| [[NDEL1]] | -0.46 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[GLT8D1]] | -0.45 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[TPI1]] | -0.44 | -0.32 / -0.51 | both halves | 2e-04 | pathway: HALLMARK_HYPOXIA |
| [[PRADC1]] | -0.42 | -0.25 / -0.39 | both halves | 4e-04 |  |
| [[BZW2]] | -0.42 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[CCNK]] | -0.41 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[CDKL5]] | -0.41 | -0.28 / -0.32 | both halves | 3e-04 |  |
| [[EIF2AK1]] | -0.40 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[RTRAF]] | -0.40 | -0.38 / -0.29 | both halves | 2e-04 |  |
| [[MED8]] | -0.40 | -0.47 / -0.20 | both halves | 7e-04 |  |
| [[CDKN2C]] | -0.40 | -0.34 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LIMCH1]] | B | LIMCH1 activity lowers VHL's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 1.13× higher at baseline in the lines without LIMCH1 | 0.078 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **-** arm (projection on the module's main direction -0.130). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-9.0, 9.8); signed map (32.0, -15.7). **Vector** length 98.0, 21.4% of its response variance represented; |z| ≥ 3 in 890 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.3 | +13.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +8.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.7 | +7.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +4.4 | +4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | +4.3 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +7.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.3 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +4.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -6.2 |
|  | [[NG25 (drug)]] 5 µM |  | -4.0 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | -4.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -0.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -3.0 | -2.9 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -2.0 | -1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -1.4 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | von Hippel-Lindau tumor suppressor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:10,141,778-10,153,667 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VHL1 |
| Gene groups (HGNC) | E3 ubiquitin ligases |
| Hallmark sets | HYPOXIA |
| Reactome | 22 pathways, smallest: Replication of the SARS-CoV-1 genome; Replication of the SARS-CoV-2 genome; SARS-CoV-1 Genome Replication and Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [P40337](https://www.uniprot.org/uniprotkb/P40337) (von Hippel-Lindau disease tumor suppressor):

> Involved in the ubiquitination and subsequent proteasomal degradation via the von Hippel-Lindau ubiquitination complex. Seems to act as a target recruitment subunit in the E3 ubiquitin ligase complex and recruits hydroxylated hypoxia-inducible factor (HIF) under normoxic conditions. Involved in transcriptional repression through interaction with HIF1A, HIF1AN and histone deacetylases. Ubiquitinates, in an oxygen-responsive manner, ADRB2. Acts as a negative regulator of mTORC1 by promoting …

**Summary**, from NCBI Gene [7428](https://www.ncbi.nlm.nih.gov/gene/7428):

> This gene encodes a component of a ubiquitination complex. The encoded protein is involved in the ubiquitination and degradation of hypoxia-inducible-factor (HIF), which is a transcription factor that plays a central role in the regulation of gene expression by oxygen. In addition to oxygen-related gene expression, this protein plays a role in many other cellular processes including cilia formation, cytokine signaling, regulation of senescence, and formation of the extracellular matrix. …

**Accessions** — [HGNC:12687](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12687) · Entrez [7428](https://www.ncbi.nlm.nih.gov/gene/7428) · UniProt [P40337](https://www.uniprot.org/uniprotkb/P40337) · Ensembl [ENSG00000134086](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134086)

## Data

Gene col 5509: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5509); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5509, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5509]; `tensor/DDL_lfc|DDL_z.npy` [5509]; `embed/gene_vectors.npy` [5509]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5509 or target_col == 5509). Every well: [[VHL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VHL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
