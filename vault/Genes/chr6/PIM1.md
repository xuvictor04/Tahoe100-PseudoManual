---
symbol: "PIM1"
type: "gene"
col: 5982
ensembl_id: "ENSG00000137193"
name: "Pim-1 proto-oncogene, serine/threonine kinase"
location: "6p21.2"
module: 31
arm: "+"
pooled_cpm: 30.62
n_lines_expressing: 46
n_dd_up: 6
n_dd_down: 32
n_dd_up_clean: 3
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# PIM1

*Pim-1 proto-oncogene, serine/threonine kinase* — 6p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.83× (z +6.0, q 1e-06, up in 25 of 39 measured lines) ⚠ toxic. The strongest without an alert is [[Gallic acid (hydrate) (drug)]] 0.5 µM: 1.62× (z +5.0, q 1e-04, up in 27 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.417× (z -12.7, q 2e-34, down in 36 of 41 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPRC5A]] (+0.61, fdr 1e-05), [[GRB7]] (+0.60, fdr 1e-05), [[IFFO2]] (+0.59, fdr 1e-05); moves opposite to [[RCC1L]] (-0.58, fdr 8e-05), [[MTREX]] (-0.56, fdr 4e-05), [[COX10]] (-0.54, fdr 4e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[CAMK1D]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5982.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +6.0 | 1e-06 | 25/39 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.70×** | +5.5 | 9e-06 | 31/39 (AsPC-1, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **1.62×** | +5.0 | 1e-04 | 27/43 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.45×** | +4.8 | 2e-04 | 21/44 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.28×** | +3.6 | 0.034 | 19/43 (hTERT-HPNE, A498, …) | top dose only | composition shift |
| [[Pioglitazone (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.081 | 16/44 (PANC-1, NCI-H2347, …) | top dose only | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.35× | +3.1 | 0.16 | 15/44 (NCI-H1573, HT-29, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | 1.35× | +3.0 | 0.17 | 13/44 (PANC-1, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5982.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.417×** | -12.7 | 2e-34 | 36/41 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.351×** | -10.8 | 1e-24 | 40/44 (LoVo, NCI-H2347, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.259×** | -7.3 | 6e-11 | 34/42 (A498, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.270×** | -7.1 | 2e-10 | 34/42 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.499×** | -6.9 | 7e-10 | 33/42 (C-33 A, LS 180, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.503×** | -6.8 | 1e-09 | 22/31 (Panc 03.27, LS 180, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Belzutifan (drug)]] 5 µM |  | **0.295×** | -6.6 | 4e-09 | 29/39 (PANC-1, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.332×** | -5.9 | 2e-07 | 33/43 (A498, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.670×** | -5.8 | 4e-07 | 27/44 (NCI-H2347, NCI-H2030, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.589×** | -5.4 | 3e-06 | 25/43 (NCI-H1792, A549, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.392×** | -5.0 | 2e-05 | 27/42 (NCI-H2347, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.709×** | -5.0 | 3e-05 | 24/44 (NCI-H23, LoVo, …) | rises with dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.613×** | -4.8 | 6e-05 | 28/44 (LS 180, LoVo, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.631×** | -4.7 | 9e-05 | 24/43 (NCI-H2347, CFPAC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.660×** | -4.3 | 8e-04 | 22/43 (MIA PaCa-2, C-33 A, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.586×** | -3.9 | 0.003 | 20/44 (LoVo, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.770×** | -3.8 | 0.005 | 16/44 (AsPC-1, C-33 A, …) | all doses, stronger at high dose | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.500×** | -3.7 | 0.006 | 18/39 (LoVo, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.701×** | -3.6 | 0.007 | 21/44 (NCI-H1792, NCI-H2347, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.781×** | -3.6 | 0.010 | 24/44 (SW 900, H4, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5982. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 82.6 | 3 (3 ⚠) | 7 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.22× (z +9.4) ⚠ cell-cycle shift, explains ~17% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -21.8) |
| [[A498 (line)]] | wt | 50.0 | 2 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +12.5) ⚠ cell-cycle shift, would explain all of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.137× (z -13.2) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -11.7) |
| [[LS 180 (line)]] | wt | 84.2 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -20.0) |
| [[NCI-H2347 (line)]] | alt | 84.5 | 0 | 6 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.178× (z -14.6) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -11.5) |
| [[AsPC-1 (line)]] | alt | 54.7 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -15.7) |
| [[C-33 A (line)]] | alt | 55.2 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0657× (z -21.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -15.5) |
| [[KATO III (line)]] | alt | 36.1 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0620× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -14.9) |
| [[MIA PaCa-2 (line)]] | alt | 43.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -13.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 124 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0501× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -15.1) |
| [[HOP62 (line)]] | alt | 15.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HS-578T (line)]] | alt | 39.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-423 (line)]] | alt | 37.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.209× (z -9.2) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 48.0 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.122× (z -10.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -9.4) |
| [[SW480 (line)]] | alt | 14.2 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.188× (z -10.3) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0610× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.68× (z +12.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[J82 (line)]] | alt | 33.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 28.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 27.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -14.8) |
| [[PANC-1 (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 30.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0718× (z -10.3) |
| [[SW1417 (line)]] | alt | 43.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -9.2) |
| [[A-172 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.59 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.25 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.59 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5982), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRC5A]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[GRB7]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[IFFO2]] | +0.59 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[FGD6]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RHOF]] | +0.58 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[HDAC5]] | +0.58 | +0.33 / +0.59 | both halves | 1e-04 |  |
| [[YPEL2]] | +0.57 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[ZMIZ1]] | +0.56 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[JUP]] | +0.56 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[CYP2S1]] | +0.56 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[FOXK1]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[PARD6B]] | +0.56 | +0.38 / +0.55 | both halves | 7e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCC1L]] | -0.58 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[MTREX]] | -0.56 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[COX10]] | -0.54 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[UQCC1]] | -0.52 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[MCM3AP]] | -0.51 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[TAF2]] | -0.51 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[ERCC8]] | -0.50 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[MSANTD2]] | -0.49 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[ZCCHC4]] | -0.49 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[MRPS15]] | -0.49 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[STXBP5-AS1]] | -0.49 | -0.52 / -0.28 | both halves | 3e-04 |  |
| [[RCBTB2]] | -0.48 | -0.43 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PIM1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAMK1D]] | C | PIM1 activity raises CAMK1D's level | lines that do not express PIM1 (4) vs lines expressing it (46) | 3.85× lower at baseline in the lines without PIM1 | 0.054 | ⚠ few lines (4 vs 46); across organs; also absent: CLSTN3, HFE, HACD1; maybe low, not absent |
| [[TRIP10]] | C | PIM1 activity raises TRIP10's level | lines that do not express PIM1 (4) vs lines expressing it (46) | 1.88× lower at baseline in the lines without PIM1 | 0.060 | ⚠ few lines (4 vs 46); across organs; also absent: CLSTN3, HFE, HACD1; maybe low, not absent |
| [[IFFO2]] | C | PIM1 activity strengthens IFFO2's drug response | lines that do not express PIM1 (4) vs lines expressing it (43) | the lines without PIM1 respond 0.75× as strongly (z diff +1.25); strongest at Panobinostat 0.5 µM: 1.98x vs 3.77x (z diff +3.7) | 0.072 | ⚠ few lines (4 vs 46); across organs; also absent: CLSTN3, HFE, HACD1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SOX13]] | C | PIM1 activity lowers SOX13's level | lines that do not express PIM1 (4) vs lines expressing it (46) | 2.71× higher at baseline in the lines without PIM1 | 0.085 | ⚠ few lines (4 vs 46); across organs; also absent: CLSTN3, HFE, HACD1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.444). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-5.9, 32.8); signed map (-5.1, 27.6). **Vector** length 121, 34.4% of its response variance represented; |z| ≥ 3 in 1,292 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | +2.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | +1.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.5 | +0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.3 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | -0.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | +1.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.7 | -10.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.7 | -7.3 |
|  | [[EX229 (drug)]] 5 µM |  | -6.7 | -7.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.8 | -5.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.7 | -5.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.4 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | Pim-1 proto-oncogene, serine/threonine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.2 — chr6:37,170,152-37,175,428 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PIM |
| Gene groups (HGNC) | PIM kinase family |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, COMPLEMENT, IL2_STAT5_SIGNALING, INTERFERON_GAMMA_RESPONSE, HYPOXIA |
| Reactome | 12 pathways, smallest: Regulation of GBP-mediated host defense; STAT5 activation downstream of FLT3 ITD mutants; GBP-mediated host defense |
| Matched by | ensembl_id |

**Function**, from UniProt [P11309](https://www.uniprot.org/uniprotkb/P11309) (Serine/threonine-protein kinase pim-1):

> Proto-oncogene with serine/threonine kinase activity involved in cell survival and cell proliferation and thus providing a selective advantage in tumorigenesis. Exerts its oncogenic activity through: the regulation of MYC transcriptional activity, the regulation of cell cycle progression and by phosphorylation and inhibition of pro-apoptotic proteins (BAD, MAP3K5, FOXO3). Phosphorylation of MYC leads to an increase of MYC protein stability and thereby an increase of transcriptional activity (By …

**Summary**, from NCBI Gene [5292](https://www.ncbi.nlm.nih.gov/gene/5292):

> The protein encoded by this gene belongs to the Ser/Thr protein kinase family, and PIM subfamily. This gene is expressed primarily in B-lymphoid and myeloid cell lines, and is overexpressed in hematopoietic malignancies and in prostate cancer. It plays a role in signal transduction in blood cells, contributing to both cell proliferation and survival, and thus provides a selective advantage in tumorigenesis. Both the human and orthologous mouse genes have been reported to encode two isoforms …

**Accessions** — [HGNC:8986](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8986) · Entrez [5292](https://www.ncbi.nlm.nih.gov/gene/5292) · UniProt [P11309](https://www.uniprot.org/uniprotkb/P11309) · Ensembl [ENSG00000137193](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137193)

## Data

Gene col 5982: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5982); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5982, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5982]; `tensor/DDL_lfc|DDL_z.npy` [5982]; `embed/gene_vectors.npy` [5982]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5982 or target_col == 5982). Every well: [[PIM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
