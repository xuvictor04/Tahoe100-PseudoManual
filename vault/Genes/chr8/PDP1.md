---
symbol: "PDP1"
type: "gene"
col: 9041
ensembl_id: "ENSG00000164951"
name: "pyruvate dehydrogenase phosphatase catalytic subunit 1"
location: "8q22.1"
module: 34
arm: "+"
pooled_cpm: 78.08
n_lines_expressing: 45
n_dd_up: 8
n_dd_down: 17
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# PDP1

*pyruvate dehydrogenase phosphatase catalytic subunit 1* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.42× (z +9.7, q 2e-19, up in 29 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.691× (z -10.1, q 3e-21, down in 23 of 43 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FRMD5]] (+0.62, fdr 1e-05), [[OSBPL3]] (+0.56, fdr 3e-05), [[ARL4C]] (+0.54, fdr 4e-05); moves opposite to [[RCC1L]] (-0.50, fdr 9e-05), [[MED24]] (-0.50, fdr 2e-04), [[PAPOLA]] (-0.49, fdr 1e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FRMD5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9041.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +9.7 | 2e-19 | 29/43 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +6.2 | 1e-07 | 27/43 (HOP62, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +6.2 | 1e-07 | 27/43 (NCI-H2030, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +5.7 | 2e-06 | 25/44 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +4.1 | 0.004 | 16/42 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.9 | 0.009 | 11/44 (C32, KATO III, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.22×** | +3.8 | 0.011 | 15/43 (C32, A498, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.014 | 16/43 (A-172, C32, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.014 | 16/42 (C32, Panc 03.27, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.6 | 0.019 | 2/44 (MIA PaCa-2, C-33 A) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.4 | 0.029 | 19/43 (HOP62, NCI-H2030, …) | two highest doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.13× | +3.2 | 0.057 | 4/43 (HOP62, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.2 | 0.070 | 15/43 (HOP62, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9041.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.691×** | -10.1 | 3e-21 | 23/43 (RKO, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.609×** | -9.1 | 3e-17 | 32/43 (HEC-1-A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.692×** | -7.1 | 2e-10 | 27/43 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.707×** | -6.5 | 1e-08 | 28/43 (SNU-423, SW 900, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.727×** | -5.9 | 3e-07 | 26/45 (SNU-423, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.738×** | -5.9 | 4e-07 | 26/43 (SW480, SW 900, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.807×** | -5.9 | 4e-07 | 23/43 (J82, A498, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.820×** | -5.4 | 4e-06 | 25/44 (SNU-423, SW1417, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.750×** | -5.4 | 5e-06 | 24/38 (SW 900, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.578×** | -5.2 | 1e-05 | 22/39 (Panc 03.27, A498, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.854× | -4.3 | 8e-04 | 16/43 (SNU-423, Panc 03.27, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.814×** | -4.0 | 0.003 | 19/43 (SW 900, SW1417, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.656×** | -4.0 | 0.003 | 21/44 (Panc 03.27, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.871× | -3.8 | 0.006 | 12/43 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.819×** | -3.6 | 0.012 | 22/39 (Panc 03.27, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.831×** | -3.6 | 0.012 | 11/43 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.827×** | -3.5 | 0.012 | 15/42 (SW480, LS 180, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | **0.824×** | -3.5 | 0.017 | 14/44 (LoVo, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.848× | -3.2 | 0.040 | 12/43 (SNU-423, RPMI-7951, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.852× | -3.1 | 0.052 | 19/44 (SW1417, NCI-H2347, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.856× | -3.0 | 0.064 | 13/43 (KATO III, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9041. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 143 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.403× (z -11.7) |
| [[A498 (line)]] | wt | 88.4 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -18.0) |
| [[Panc 03.27 (line)]] | alt | 320 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -16.8) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.501× (z -11.9) |
| [[SNU-423 (line)]] | alt | 325 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.175× (z -24.5) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -19.4) |
| [[C32 (line)]] | wt | 88.7 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.31× (z +20.8) | — |
| [[SW480 (line)]] | alt | 99.2 | 0 | 6 | — | [[Ixazomib citrate (drug)]] 5 µM 0.395× (z -9.0) |
| [[A-172 (line)]] | wt | 83.7 | 2 (2 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.22× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.272× (z -14.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 77.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -18.2) |
| [[HEC-1-A (line)]] | alt | 112 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 39.7 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.262× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.389× (z -11.2) |
| [[A-427 (line)]] | wt | 47.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 56.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 109 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.78× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -14.2) |
| [[RKO (line)]] | wt | 75.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -18.4) |
| [[SW1417 (line)]] | alt | 191 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -21.9) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.497× (z -9.6) |
| [[HOP62 (line)]] | alt | 52.3 | 2 | 0 | [[Panobinostat (drug)]] 0.05 µM 2.91× (z +11.0) | — |
| [[J82 (line)]] | alt | 156 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.402× (z -15.4) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.454× (z -8.9) |
| [[LoVo (line)]] | wt | 51.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.563× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 26.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -12.6) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.418× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 104 | 1 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 2.70× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Auranofin (drug)]] 5 µM 0.425× (z -8.6) |
| [[A549 (line)]] | wt | 36.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -13.9) |
| [[BT-474 (line)]] | alt | 44.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 72.7 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.332× (z -10.1) |
| [[HS-578T (line)]] | alt | 78.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.398× (z -8.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 51.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -12.6) |
| [[NCI-H661 (line)]] | alt | 59.6 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0579× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 75.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -10.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 80.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -8.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.8 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.9 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 154 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 85.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.0 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9041), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRMD5]] | +0.62 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[OSBPL3]] | +0.56 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[ARL4C]] | +0.54 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[EML4]] | +0.53 | +0.49 / +0.37 | both halves | 8e-05 |  |
| [[WNT7B]] | +0.51 | +0.53 / +0.39 | both halves | 6e-05 |  |
| [[UGCG]] | +0.51 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[TSC22D2]] | +0.51 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[EIF5A2]] | +0.50 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[TIAM1]] | +0.50 | +0.44 / +0.38 | both halves | 7e-05 |  |
| [[NHS]] | +0.49 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[MRPL14]] | +0.48 | +0.37 / +0.38 | both halves | 8e-05 |  |
| [[FAM3C]] | +0.48 | +0.52 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCC1L]] | -0.50 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[MED24]] | -0.50 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[PAPOLA]] | -0.49 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[VPS52]] | -0.49 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[VDAC1P8]] | -0.48 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[PSMC2]] | -0.47 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[PNISR-AS1]] | -0.47 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[IPP]] | -0.46 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[GPALPP1]] | -0.46 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[MAIP1]] | -0.46 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[TXNDC15]] | -0.45 | -0.43 / -0.25 | both halves | 4e-04 |  |
| [[NNT]] | -0.45 | -0.30 / -0.32 | both halves | 2e-04 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMD5]] | B | FRMD5 activity raises PDP1's level | lines that do not express FRMD5 (10) vs lines expressing it (40) | 2.00× lower at baseline in the lines without FRMD5 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000291112; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers PDP1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers PDP1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[WNT7B]] | B | WNT7B activity raises PDP1's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 1.42× lower at baseline in the lines without WNT7B | 0.095 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.449). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.2, 19.4); signed map (1.5, 41.9). **Vector** length 122, 33.2% of its response variance represented; |z| ≥ 3 in 1,217 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM |  | +6.8 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +9.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.7 | +6.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.1 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +5.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +1.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.4 | +2.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.2 | +3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.2 | +3.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.9 | -3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.2 | -5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.0 | -9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.9 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.6 | -7.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -4.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.7 | -4.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.3 | -2.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.8 | -2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | pyruvate dehydrogenase phosphatase catalytic subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:93,857,807-93,926,068 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PDP, PDH, PPM2A; previously PPM2C |
| Gene groups (HGNC) | Protein phosphatases, Mg2+/Mn2+ dependent |
| Hallmark sets | COMPLEMENT, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 4 pathways, smallest: Regulation of pyruvate dehydrogenase (PDH) complex; Regulation of pyruvate metabolism; Pyruvate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0J1](https://www.uniprot.org/uniprotkb/Q9P0J1) ([Pyruvate dehydrogenase [acetyl-transferring]]-phosphatase 1, mitochondrial):

> Mitochondrial enzyme that catalyzes the dephosphorylation and concomitant reactivation of the alpha subunit of the E1 component of the pyruvate dehydrogenase complex (PDC), thereby stimulating the conversion of pyruvate into acetyl-CoA.

**Summary**, from NCBI Gene [54704](https://www.ncbi.nlm.nih.gov/gene/54704):

> Pyruvate dehydrogenase (E1) is one of the three components (E1, E2, and E3) of the large pyruvate dehydrogenase complex. Pyruvate dehydrogenase kinases catalyze phosphorylation of serine residues of E1 to inactivate the E1 component and inhibit the complex. Pyruvate dehydrogenase phosphatases catalyze the dephosphorylation and activation of the E1 component to reverse the effects of pyruvate dehydrogenase kinases. Pyruvate dehydrogenase phosphatase is a heterodimer consisting of catalytic and …

**Accessions** — [HGNC:9279](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9279) · Entrez [54704](https://www.ncbi.nlm.nih.gov/gene/54704) · UniProt [Q9P0J1](https://www.uniprot.org/uniprotkb/Q9P0J1) · Ensembl [ENSG00000164951](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164951)

## Data

Gene col 9041: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9041); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9041, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9041]; `tensor/DDL_lfc|DDL_z.npy` [9041]; `embed/gene_vectors.npy` [9041]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9041 or target_col == 9041). Every well: [[PDP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
