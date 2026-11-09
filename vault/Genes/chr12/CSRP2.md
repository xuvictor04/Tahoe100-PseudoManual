---
symbol: "CSRP2"
type: "gene"
col: 10576
ensembl_id: "ENSG00000175183"
name: "cysteine and glycine rich protein 2"
location: "12q21.2"
module: 1
arm: "-"
pooled_cpm: 16.48
n_lines_expressing: 44
n_dd_up: 26
n_dd_down: 10
n_dd_up_clean: 15
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# CSRP2

*cysteine and glycine rich protein 2* — 12q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.64× (z +19.2, q 0e+00, up in 41 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Belumosudil (drug)]] 5 µM: 0.505× (z -6.9, q 3e-09, down in 28 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC41A1]] (+0.63, fdr 1e-05), [[CRABP2]] (+0.60, fdr 6e-05), [[P4HA2]] (+0.59, fdr 1e-05); moves opposite to [[DIS3L2]] (-0.65, fdr 7e-06), [[RAD54L2]] (-0.64, fdr 1e-05), [[YLPM1]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[PPP4R4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10576.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.64×** | +19.2 | 0e+00 | 41/41 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.89×** | +11.2 | 2e-26 | 37/42 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.85×** | +11.0 | 6e-26 | 35/42 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +10.6 | 3e-24 | 31/41 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.03×** | +10.5 | 9e-24 | 40/42 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.64×** | +10.2 | 2e-22 | 34/41 (LoVo, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.47×** | +9.5 | 2e-19 | 32/42 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **2.09×** | +7.7 | 7e-13 | 27/41 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.02×** | +7.4 | 8e-12 | 36/41 (SW1417, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.03×** | +7.2 | 4e-11 | 28/41 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.83×** | +6.1 | 5e-08 | 29/40 (SW480, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +5.5 | 2e-06 | 21/42 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.57×** | +4.7 | 1e-04 | 20/40 (NCI-H460, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.55×** | +4.6 | 2e-04 | 19/41 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.3 | 5e-04 | 19/42 (PANC-1, BT-474, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.002 | 15/41 (SNU-423, NCI-H1792, …) | top dose only | plate-row cell shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.011 | 15/42 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.40×** | +3.5 | 0.012 | 14/42 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.013 | 16/41 (SW1417, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.39×** | +3.3 | 0.024 | 11/42 (NCI-H2347, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.70×** | +2.9 | 0.076 | 6/39 (SW480, C32, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Clopidogrel (drug)]] 0.05 µM |  | **1.31×** | +2.9 | 0.095 | 4/42 (NCI-H1792, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10576.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.505×** | -6.9 | 3e-09 | 28/40 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.704×** | -5.2 | 5e-05 | 27/42 (SNU-423, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.610×** | -5.0 | 1e-04 | 14/25 (NCI-H2347, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.626×** | -4.9 | 1e-04 | 19/36 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.670×** | -4.2 | 0.003 | 18/41 (NCI-H2347, HOP62, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.678×** | -4.1 | 0.004 | 18/42 (A-172, HOP62, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.699×** | -3.6 | 0.024 | 14/42 (CFPAC-1, SHP-77, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.699×** | -3.6 | 0.024 | 20/42 (C32, BT-474, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.720×** | -3.5 | 0.034 | 18/41 (A549, HOP62, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.638×** | -3.3 | 0.056 | 14/40 (SW1417, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.734× | -3.1 | 0.10 | 14/42 (SW480, H4, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.5 µM |  | 0.659× | -3.1 | 0.10 | 9/40 (Hs 766T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM |  | 0.738× | -3.0 | 0.10 | 11/42 (LoVo, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Berbamine (drug)]] 0.05 µM |  | 0.740× | -3.0 | 0.10 | 14/42 (RKO, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.60 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10576. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 15.2 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.69× (z +17.1) | — |
| [[PANC-1 (line)]] | alt | 4.74 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.26× (z +13.1) | — |
| [[NCI-H2347 (line)]] | alt | 44.1 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.129× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.191× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 18.4 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -10.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 17.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +16.6) | — |
| [[A-172 (line)]] | wt | 23.3 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.0997× (z -12.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 7.52 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.18× (z +9.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.57× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 18.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.80× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 14.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 9.04 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.37× (z +10.4) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[Panc 03.27 (line)]] | alt | 9.38 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.96× (z +10.2) | — |
| [[SK-MEL-2 (line)]] | alt | 9.89 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +10.0) | — |
| [[SW 900 (line)]] | alt | 14.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.77× (z +12.0) | — |
| [[A-427 (line)]] | wt | 17.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.43× (z +8.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A498 (line)]] | wt | 8.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.17× (z +11.6) | — |
| [[A549 (line)]] | wt | 16.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.20× (z +12.7) | — |
| [[BT-474 (line)]] | alt | 6.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.43× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 13.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +9.0) | — |
| [[HCT15 (line)]] | alt | 35.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -9.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 5.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.12× (z +14.1) | — |
| [[HOP62 (line)]] | alt | 28.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 7.57 | 0 | 1 | — | [[Balsalazide (sodium hydrate) (drug)]] 0.5 µM 0.0602× (z -10.0) |
| [[J82 (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -11.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 6.53 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0901× (z -9.7) |
| [[RKO (line)]] | wt | 20.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 36.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0671× (z -13.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 92.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.79 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10576), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*39 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC41A1]] | +0.63 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[CRABP2]] | +0.60 | +0.39 / +0.62 | both halves | 6e-05 |  |
| [[P4HA2]] | +0.59 | +0.50 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[PDK3]] | +0.58 | +0.56 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[VAMP1]] | +0.56 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[SNAI1]] | +0.56 | +0.38 / +0.65 | both halves | 6e-05 |  |
| [[RFX2]] | +0.56 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[P4HA1]] | +0.56 | +0.55 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[INSIG2]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[RELT]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[GRK3]] | +0.54 | +0.36 / +0.59 | both halves | 1e-04 |  |
| [[SAP30-DT]] | +0.54 | +0.45 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*61 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIS3L2]] | -0.65 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[RAD54L2]] | -0.64 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[YLPM1]] | -0.63 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[LTV1]] | -0.60 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[ZNF839]] | -0.59 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[COG2]] | -0.58 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[RRP15]] | -0.57 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[GPATCH8]] | -0.57 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[ZNF502]] | -0.57 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[MRPL15]] | -0.57 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[DDX10]] | -0.56 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[JPX]] | -0.56 | -0.52 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CSRP2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[WNK3]] | B | WNK3 activity raises CSRP2's level | lines that do not express WNK3 (28) vs lines expressing it (22) | 2.41× lower at baseline in the lines without WNK3 | 0.088 | ⚠ within organs, on part of the lines; also absent: PCDH17, ZNF667, PTPRN; maybe low, not absent |
| [[TFCP2]] | C | TFCP2's natural level strengthens CSRP2's drug response | TFCP2's natural level across 40 lines (lineage-adjusted; a glimpse) | r +0.71, reverse -0.42; direction not clear | 0.054 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP4R4]] | B | CSRP2 activity raises PPP4R4's level | lines that do not express CSRP2 (6) vs lines expressing it (44) | 4.59× lower at baseline in the lines without CSRP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: TPST1, TBKBP1, CYP46A1; maybe low, not absent; its own permutation p |
| [[ZNF839]] | B | CSRP2 activity raises ZNF839's level | lines that do not express CSRP2 (6) vs lines expressing it (44) | 1.78× lower at baseline in the lines without CSRP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: TPST1, TBKBP1, CYP46A1; maybe low, not absent; its own permutation p |
| [[DHX30]] | B | CSRP2 activity raises DHX30's level | lines that do not express CSRP2 (6) vs lines expressing it (44) | 1.46× lower at baseline in the lines without CSRP2 | 0.096 | ⚠ within organs, on part of the lines; also absent: TPST1, TBKBP1, CYP46A1; maybe low, not absent |
| [[NOL9]] | B | CSRP2 activity raises NOL9's level | lines that do not express CSRP2 (6) vs lines expressing it (44) | 1.13× lower at baseline in the lines without CSRP2 | 0.0998 | ⚠ within organs, on part of the lines; also absent: TPST1, TBKBP1, CYP46A1; maybe low, not absent |
| [[GPR155]] | C | CSRP2 activity raises GPR155's level | lines that do not express CSRP2 (6) vs lines expressing it (44) | 3.68× lower at baseline in the lines without CSRP2 | 0.064 | ⚠ within organs, on part of the lines; also absent: TPST1, TBKBP1, CYP46A1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.577). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-27.8, -8.2); signed map (1.2, 19.6). **Vector** length 104, 27.1% of its response variance represented; |z| ≥ 3 in 1,076 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.7 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +19.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.5 | +10.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.3 | +7.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.6 | +7.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +3.3 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -5.5 | -1.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -0.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.7 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | cysteine and glycine rich protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.2 — chr12:76,858,709-76,879,023 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SmLIM, CRP2, LMO5 |
| Gene groups (HGNC) | LIM domain containing |
| Hallmark sets | HYPOXIA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16527](https://www.uniprot.org/uniprotkb/Q16527) (Cysteine and glycine-rich protein 2):

> Drastically down-regulated in response to PDGF-BB or cell injury, that promote smooth muscle cell proliferation and dedifferentiation. Seems to play a role in the development of the embryonic vascular system.

**Summary**, from NCBI Gene [1466](https://www.ncbi.nlm.nih.gov/gene/1466):

> CSRP2 is a member of the CSRP family of genes, encoding a group of LIM domain proteins, which may be involved in regulatory processes important for development and cellular differentiation. CRP2 contains two copies of the cysteine-rich amino acid sequence motif (LIM) with putative zinc-binding activity, and may be involved in regulating ordered cell growth. Other genes in the family include CSRP1 and CSRP3. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul …

**Accessions** — [HGNC:2470](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2470) · Entrez [1466](https://www.ncbi.nlm.nih.gov/gene/1466) · UniProt [Q16527](https://www.uniprot.org/uniprotkb/Q16527) · Ensembl [ENSG00000175183](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175183)

## Data

Gene col 10576: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10576); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10576, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10576]; `tensor/DDL_lfc|DDL_z.npy` [10576]; `embed/gene_vectors.npy` [10576]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10576 or target_col == 10576). Every well: [[CSRP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSRP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
