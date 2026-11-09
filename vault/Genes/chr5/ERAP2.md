---
symbol: "ERAP2"
type: "gene"
col: 8926
ensembl_id: "ENSG00000164308"
name: "endoplasmic reticulum aminopeptidase 2"
location: "5q15"
module: 32
arm: "+"
pooled_cpm: 41.48
n_lines_expressing: 43
n_dd_up: 26
n_dd_down: 18
n_dd_up_clean: 20
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 8
direction_downstream: 12
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# ERAP2

*endoplasmic reticulum aminopeptidase 2* — 5q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.54× (z +7.8, q 2e-12, up in 28 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.307× (z -21.2, q 0e+00, down in 41 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM43]] (+0.72, fdr 7e-06), [[GBP3]] (+0.71, fdr 7e-06), [[NMI]] (+0.71, fdr 7e-06); moves opposite to [[TBC1D16]] (-0.52, fdr 9e-05), [[RDH13]] (-0.51, fdr 2e-04), [[SLC66A2]] (-0.51, fdr 3e-04).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 12 go from it, the strongest it → [[RBM43]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8926.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +7.8 | 2e-12 | 28/41 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +7.8 | 2e-12 | 25/41 (NCI-H2347, RKO, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +7.7 | 2e-12 | 27/41 (NCI-H2347, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +6.3 | 6e-08 | 22/39 (LS 180, LoVo, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +6.2 | 7e-08 | 19/41 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.1 | 9e-08 | 26/41 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.1 | 9e-08 | 23/41 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +6.0 | 2e-07 | 25/41 (NCI-H1792, A498, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +5.5 | 3e-06 | 16/33 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +5.1 | 2e-05 | 21/40 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.21×** | +5.0 | 3e-05 | 19/41 (LoVo, LS 180, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +4.9 | 4e-05 | 14/41 (SW1417, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +4.9 | 4e-05 | 17/41 (AsPC-1, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | **1.31×** | +4.8 | 5e-05 | 18/39 (C32, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.30×** | +4.7 | 1e-04 | 17/40 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.28×** | +4.5 | 3e-04 | 16/41 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +4.5 | 3e-04 | 17/41 (NCI-H460, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.22×** | +4.4 | 4e-04 | 17/41 (SW1417, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.002 | 12/41 (PANC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8926.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.307×** | -21.2 | 0e+00 | 41/41 (Hs 766T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.378×** | -17.4 | 0e+00 | 40/41 (Hs 766T, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.510×** | -17.0 | 0e+00 | 30/40 (COLO 205, PANC-1, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.438×** | -14.8 | 0e+00 | 40/41 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.631×** | -8.2 | 2e-14 | 31/41 (HCT15, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.633×** | -8.2 | 3e-14 | 32/41 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.643×** | -7.9 | 2e-13 | 29/41 (LOX-IMVI, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.758×** | -7.0 | 2e-10 | 25/41 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.712×** | -6.1 | 8e-08 | 24/41 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.543×** | -5.7 | 6e-07 | 23/40 (LOX-IMVI, C32, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.555×** | -5.5 | 2e-06 | 20/41 (SNU-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.763×** | -4.8 | 7e-05 | 19/41 (LoVo, Panc 03.27, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.777×** | -4.5 | 3e-04 | 16/40 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.844× | -4.3 | 8e-04 | 18/41 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.790×** | -4.0 | 0.002 | 15/40 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.853× | -4.0 | 0.002 | 14/41 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8926. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 30.9 | 1 (1 ⚠) | 6 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.53× (z +8.5) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.0978× (z -19.1) |
| [[NCI-H2347 (line)]] | alt | 56.7 | 3 (1 ⚠) | 3 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.51× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.567× (z -8.8) |
| [[SW480 (line)]] | alt | 16.9 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.255× (z -14.6) |
| [[A-172 (line)]] | wt | 152 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.239× (z -14.7) |
| [[A549 (line)]] | wt | 20.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -12.8) |
| [[H4 (line)]] | wt | 41.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0914× (z -13.7) |
| [[HCT15 (line)]] | alt | 41.6 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.128× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 19.5 | 1 | 3 | [[Harringtonine (drug)]] 0.5 µM 3.59× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -11.8) |
| [[Hs 766T (line)]] | wt | 303 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -18.2) |
| [[LoVo (line)]] | wt | 21.1 | 3 (2 ⚠) | 1 | [[Harringtonine (drug)]] 0.5 µM 4.72× (z +11.2) | [[Auranofin (drug)]] 5 µM 0.293× (z -8.8) |
| [[PANC-1 (line)]] | alt | 31.6 | 1 | 3 | [[Harringtonine (drug)]] 0.5 µM 3.11× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -20.1) |
| [[CFPAC-1 (line)]] | alt | 25.8 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 3.35× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.324× (z -8.9) |
| [[COLO 205 (line)]] | alt | 61.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -20.2) |
| [[LOX-IMVI (line)]] | wt | 34.3 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.243× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 22.8 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.202× (z -13.1) |
| [[SNU-1 (line)]] | wt | 46.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -15.0) |
| [[SNU-423 (line)]] | alt | 67.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.307× (z -10.3) |
| [[A498 (line)]] | wt | 74.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -15.4) |
| [[AsPC-1 (line)]] | alt | 20.2 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.77× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.117× (z -11.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 59.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -8.6) |
| [[HT-29 (line)]] | alt | 43.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -16.2) |
| [[NCI-H2030 (line)]] | alt | 25.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 77.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -13.4) |
| [[SK-MEL-2 (line)]] | alt | 60.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.274× (z -11.0) |
| [[SW1417 (line)]] | alt | 32.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -18.7) |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0998× (z -14.3) ⚠ cell-cycle shift, explains ~22% of this change |
| [[C32 (line)]] | wt | 40.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | — |
| [[HS-578T (line)]] | alt | 123 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -14.0) |
| [[NCI-H1573 (line)]] | alt | 15.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -12.0) |
| [[RKO (line)]] | wt | 27.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -11.7) |
| [[SW 900 (line)]] | alt | 33.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -15.1) |
| [[A-427 (line)]] | wt | 8.89 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.18 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.84 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 62.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.63 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.17 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.06 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8926), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM43]] | +0.72 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[GBP3]] | +0.71 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[NMI]] | +0.71 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[BTN3A3]] | +0.70 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[LINC02100]] | +0.68 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[CASP7]] | +0.68 | +0.62 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT |
| [[APOBEC3F]] | +0.67 | +0.57 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT |
| [[MOV10]] | +0.67 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[APOL6]] | +0.67 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[ERAP1]] | +0.65 | +0.55 / +0.52 | both halves | 1e-05 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 607 |
| [[TRIM21]] | +0.65 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[PHF11]] | +0.65 | +0.52 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D16]] | -0.52 | -0.36 / -0.38 | both halves | 9e-05 |  |
| [[RDH13]] | -0.51 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[SLC66A2]] | -0.51 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[MEX3D]] | -0.50 | -0.39 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ERAP2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IL15RA]] | B | IL15RA activity raises ERAP2's level | lines that do not express IL15RA (7) vs lines expressing it (43) | 1.79× lower at baseline in the lines without IL15RA | 0.042 | ⚠ within organs, on part of the lines; also absent: CLCF1, SGMS2 |
| [[APOL6]] | B | APOL6 activity raises ERAP2's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 2.49× lower at baseline in the lines without APOL6 | 0.069 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |
| [[LINC00944]] | B | LINC00944 activity raises ERAP2's level | lines that do not express LINC00944 (20) vs lines expressing it (30) | 2.12× lower at baseline in the lines without LINC00944 | 0.078 | ⚠ within organs, on part of the lines; also absent: RDUR, ENSG00000289600, LINC02405 |
| [[IFIT2]] | C | IFIT2 activity raises ERAP2's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 2.77× lower at baseline in the lines without IFIT2 | 0.018 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38; co-absent with the target |
| [[RNASEL]] | C | RNASEL activity raises ERAP2's level | lines that do not express RNASEL (5) vs lines expressing it (45) | 3.34× lower at baseline in the lines without RNASEL | 0.081 | ⚠ within organs, on part of the lines; also absent: SP140L, KIFC3, DDX60; maybe low, not absent; co-absent with the target |
| [[RBM43]] | C | RBM43 activity raises ERAP2's level | lines that do not express RBM43 (4) vs lines expressing it (46) | 3.12× lower at baseline in the lines without RBM43 | 0.083 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALPK1, RNASEL, TFAP2A |
| [[NMI]] | C | NMI activity raises ERAP2's level | lines that do not express NMI (4) vs lines expressing it (46) | 2.38× lower at baseline in the lines without NMI | 0.097 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NABP1, LGI4, C21orf91 |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 10, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBM43]] | B | ERAP2 activity raises RBM43's level | lines that do not express ERAP2 (7) vs lines expressing it (43) | 2.67× lower at baseline in the lines without ERAP2 | 0.012 | ⚠ within organs, on part of the lines; also absent: COL13A1, SMOX, TRIM38; maybe low, not absent |
| [[IFIT3]] | B | ERAP2 activity raises IFIT3's level | lines that do not express ERAP2 (7) vs lines expressing it (43) | 3.48× lower at baseline in the lines without ERAP2 | 0.046 | ⚠ within organs, on part of the lines; also absent: COL13A1, SMOX, TRIM38; maybe low, not absent |
| [[MR1]] | B | ERAP2 activity raises MR1's level | lines that do not express ERAP2 (7) vs lines expressing it (43) | 1.89× lower at baseline in the lines without ERAP2 | 0.047 | ⚠ within organs, on part of the lines; also absent: COL13A1, SMOX, TRIM38; maybe low, not absent |
| [[TRIM5]] | B | ERAP2 activity raises TRIM5's level | lines that do not express ERAP2 (7) vs lines expressing it (43) | 1.95× lower at baseline in the lines without ERAP2 | 0.048 | ⚠ within organs, on part of the lines; also absent: COL13A1, SMOX, TRIM38; maybe low, not absent |
| [[TRANK1]] | B | ERAP2 activity raises TRANK1's level | lines that do not express ERAP2 (7) vs lines expressing it (43) | 2.29× lower at baseline in the lines without ERAP2 | 0.052 | ⚠ within organs, on part of the lines; also absent: COL13A1, SMOX, TRIM38; maybe low, not absent |
| [[LINC02605]] | B | ERAP2 activity raises LINC02605's level | lines that do not express ERAP2 (7) vs lines expressing it (43) | 2.65× lower at baseline in the lines without ERAP2 | 0.056 | ⚠ within organs, on part of the lines; also absent: COL13A1, SMOX, TRIM38; maybe low, not absent |
| [[FAS]] | B | ERAP2 activity raises FAS's level | lines that do not express ERAP2 (7) vs lines expressing it (43) | 3.01× lower at baseline in the lines without ERAP2 | 0.066 | ⚠ within organs, on part of the lines; also absent: COL13A1, SMOX, TRIM38; maybe low, not absent |
| [[LINC00944]] | B | ERAP2 activity raises LINC00944's level | lines that do not express ERAP2 (7) vs lines expressing it (43) | 3.48× lower at baseline in the lines without ERAP2 | 0.085 | ⚠ within organs, on part of the lines; also absent: COL13A1, SMOX, TRIM38; maybe low, not absent |
| [[IL15RA]] | B | ERAP2 activity raises IL15RA's level | lines that do not express ERAP2 (7) vs lines expressing it (43) | 2.77× lower at baseline in the lines without ERAP2 | 0.092 | ⚠ within organs, on part of the lines; also absent: COL13A1, SMOX, TRIM38; maybe low, not absent |
| [[CTSO]] | B | ERAP2 activity raises CTSO's level | lines that do not express ERAP2 (7) vs lines expressing it (43) | 2.15× lower at baseline in the lines without ERAP2 | 0.093 | ⚠ within organs, on part of the lines; also absent: COL13A1, SMOX, TRIM38; maybe low, not absent |
| [[IL15]] | C | ERAP2 activity raises IL15's level | lines that do not express ERAP2 (7) vs lines expressing it (43) | 4.14× lower at baseline in the lines without ERAP2 | 0.008 | ⚠ within organs, on part of the lines; also absent: COL13A1, SMOX, TRIM38; maybe low, not absent; co-absent with the target |
| [[IFIT2]] | C | ERAP2 activity raises IFIT2's level | lines that do not express ERAP2 (7) vs lines expressing it (43) | 4.71× lower at baseline in the lines without ERAP2 | 0.010 | ⚠ within organs, on part of the lines; also absent: COL13A1, SMOX, TRIM38; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.599). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.8, 53.0); signed map (60.9, 31.2). **Vector** length 122, 33.7% of its response variance represented; |z| ≥ 3 in 1,213 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antimicrobial mechanism of IFN-stimulated genes* (reactome, mean cos +0.52 to 21); *IFIT antiviral response* (reactome, mean cos +0.52 to 9); *DDX58/IFIH1-mediated induction of interferon-alpha/beta* (reactome, mean cos +0.50 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +6.8 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.8 | +7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +6.0 | +6.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +7.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +6.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.6 | +4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.3 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +6.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.4 | +4.4 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -6.0 | -21.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.9 | -14.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.6 | -17.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.5 | -8.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -5.1 | -8.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.1 | -7.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.7 | -2.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.5 | -4.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.3 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | endoplasmic reticulum aminopeptidase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q15 — chr5:96,875,986-96,919,703 (+) |
| Ensembl biotype | protein_coding |
| Also known as | L-RAP, LRAP |
| Gene groups (HGNC) | Aminopeptidases; M1 metallopeptidases |
| Hallmark sets | COMPLEMENT |
| Reactome | 3 pathways, smallest: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P179](https://www.uniprot.org/uniprotkb/Q6P179) (Endoplasmic reticulum aminopeptidase 2):

> Aminopeptidase that plays a central role in peptide trimming, a step required for the generation of most HLA class I-binding peptides. Peptide trimming is essential to customize longer precursor peptides to fit them to the correct length required for presentation on MHC class I molecules. Preferentially hydrolyzes the basic residues Arg and Lys.

**Summary**, from NCBI Gene [64167](https://www.ncbi.nlm.nih.gov/gene/64167):

> This gene encodes a zinc metalloaminopeptidase of the M1 protease family that resides in the endoplasmic reticulum and functions in N-terminal trimming antigenic epitopes for presentation by major histocompatibility complex (MHC) class I molecules. Certain mutations in this gene are associated with the inflammatory arthritis syndrome ankylosing spondylitis and pre-eclampsia. This gene is located adjacent to a closely related aminopeptidase gene on chromosome 5. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:29499](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29499) · Entrez [64167](https://www.ncbi.nlm.nih.gov/gene/64167) · UniProt [Q6P179](https://www.uniprot.org/uniprotkb/Q6P179) · Ensembl [ENSG00000164308](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164308)

## Data

Gene col 8926: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8926); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8926, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8926]; `tensor/DDL_lfc|DDL_z.npy` [8926]; `embed/gene_vectors.npy` [8926]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8926 or target_col == 8926). Every well: [[ERAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
