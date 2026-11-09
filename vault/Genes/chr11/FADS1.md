---
symbol: "FADS1"
type: "gene"
col: 7378
ensembl_id: "ENSG00000149485"
name: "fatty acid desaturase 1"
location: "11q12.2"
module: 86
arm: "+"
pooled_cpm: 51.28
n_lines_expressing: 43
n_dd_up: 14
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# FADS1

*fatty acid desaturase 1* — 11q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.03× (z +15.9, q 0e+00, up in 39 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cepharanthine (drug)]] 5 µM: 1.98× (z +11.0, q 5e-26, up in 37 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.406× (z -14.5, q 4e-45, down in 37 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FADS2]] (+0.78, fdr 7e-06, ⚠ same locus), [[DHCR24]] (+0.63, fdr 7e-06), [[DHCR7]] (+0.63, fdr 7e-06), [[SCD]] (+0.63, fdr 1e-05); moves opposite to [[R3HCC1]] (-0.43, fdr 9e-05), [[TAF1A]] (-0.42, fdr 2e-04), [[SNHG11]] (-0.41, fdr 1e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PCSK9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7378.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.03×** | +15.9 | 0e+00 | 39/39 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.86×** | +14.8 | 0e+00 | 35/35 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Cepharanthine (drug)]] 5 µM |  | **1.98×** | +11.0 | 5e-26 | 37/41 (A549, SW 900, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.47×** | +9.5 | 2e-19 | 36/38 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Berbamine (drug)]] 5 µM |  | **1.78×** | +9.3 | 1e-18 | 36/42 (SW 900, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +7.6 | 3e-12 | 29/41 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.80×** | +6.7 | 1e-09 | 37/40 (A549, SW 900, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.65×** | +5.5 | 3e-06 | 29/41 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +5.1 | 2e-05 | 24/40 (NCI-H1573, SNU-423, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.0 | 0.004 | 1/41 (SW 900) | inconsistent across doses |  |
| [[Posaconazole (drug)]] 5 µM |  | **1.43×** | +3.9 | 0.004 | 21/41 (A-172, Panc 03.27, …) | top dose only | plate-row cell shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.007 | 19/41 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.3 | 0.044 | 19/40 (hTERT-HPNE, NCI-H2030, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.069 | 18/41 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sulfatinib (drug)]] 5 µM |  | **1.32×** | +3.0 | 0.091 | 15/40 (HOP62, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7378.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.406×** | -14.5 | 4e-45 | 37/41 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.427×** | -9.7 | 8e-20 | 34/41 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.690×** | -6.0 | 4e-07 | 31/41 (SNU-1, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.636×** | -5.0 | 1e-04 | 25/41 (NCI-H23, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.706×** | -4.0 | 0.008 | 19/41 (A-427, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.527×** | -3.8 | 0.013 | 23/41 (A-427, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.659×** | -3.8 | 0.013 | 19/40 (BT-474, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.745×** | -3.3 | 0.058 | 22/41 (NCI-H661, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Rifaximin (drug)]] 5 µM |  | 0.754× | -3.1 | 0.12 | 18/40 (HOP62, A-172, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7378. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 73.7 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -16.7) |
| [[HOP62 (line)]] | alt | 60.8 | 6 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.49× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Cepharanthine (drug)]] 5 µM 3.00× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 91.3 | 4 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.43× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -17.2) |
| [[Panc 03.27 (line)]] | alt | 37.9 | 5 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.79× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Berbamine (drug)]] 5 µM 2.98× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -12.1) |
| [[A-427 (line)]] | wt | 102 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 5.16× (z +13.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -16.5) |
| [[A549 (line)]] | wt | 80.7 | 6 (2 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 4.63× (z +16.0) | — |
| [[NCI-H2030 (line)]] | alt | 105 | 4 (2 ⚠) | 1 | [[Cepharanthine (drug)]] 5 µM 3.43× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -12.7) |
| [[SW 900 (line)]] | alt | 53.5 | 3 | 2 | [[Cepharanthine (drug)]] 5 µM 5.48× (z +14.7) | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -14.6) |
| [[SW480 (line)]] | alt | 39.5 | 4 (3 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +15.2) | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -12.3) |
| [[A-172 (line)]] | wt | 64.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.93× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +10.9) | — |
| [[A498 (line)]] | wt | 69.4 | 4 (2 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 2.27× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 109 | 2 | 2 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 3.08× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -10.4) |
| [[J82 (line)]] | alt | 153 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -17.9) |
| [[LoVo (line)]] | wt | 28.3 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +15.2) | — |
| [[LOX-IMVI (line)]] | wt | 61.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -12.9) |
| [[PANC-1 (line)]] | alt | 83.0 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -12.9) |
| [[RPMI-7951 (line)]] | alt | 47.7 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -16.4) |
| [[SNU-1 (line)]] | wt | 87.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -20.9) |
| [[CFPAC-1 (line)]] | alt | 47.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Cepharanthine (drug)]] 5 µM 2.57× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 27.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +11.3) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 27.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.56× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -11.9) |
| [[HS-578T (line)]] | alt | 53.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.327× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 39.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0826× (z -25.5) |
| [[NCI-H2347 (line)]] | alt | 36.5 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 34.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.03× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Cepharanthine (drug)]] 5 µM 3.08× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 21.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 13.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.98× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 28.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.34× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 32.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -10.4) |
| [[SHP-77 (line)]] | alt | 105 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +13.5) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 83.6 | 1 | 1 | [[Cepharanthine (drug)]] 5 µM 5.34× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.0720× (z -13.9) |
| [[C32 (line)]] | wt | 26.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +8.5) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 54.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -9.6) |
| [[H4 (line)]] | wt | 33.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 50.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -13.9) |
| [[hTERT-HPNE (line)]] | wt | 63.5 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 3.38× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.94 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.06 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.03 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.64 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.40 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7378), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FADS2]] | +0.78 | +0.80 / +0.69 | both halves | 7e-06 | same gene group; pathway: HALLMARK_BILE_ACID_METABOLISM; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[DHCR24]] | +0.63 | +0.69 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[DHCR7]] | +0.63 | +0.70 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 492 |
| [[SCD]] | +0.63 | +0.69 / +0.51 | both halves | 1e-05 | same gene group; pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 959 |
| [[FASN]] | +0.62 | +0.61 / +0.58 | both halves | 7e-06 | pathway: Fatty acid metabolism; STRING 624 |
| [[CYP51A1]] | +0.62 | +0.63 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[IDI1]] | +0.58 | +0.56 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[MSMO1]] | +0.58 | +0.60 / +0.59 | both halves | 7e-06 | STRING 670 |
| [[FDPS]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_PEROXISOME; STRING 406 |
| [[ELOVL5]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 836 |
| [[ACAT2]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 | STRING 454 |
| [[HMGCR]] | +0.57 | +0.63 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 456 |
| [[FDFT1]] | +0.57 | +0.62 / +0.59 | both halves | 7e-06 | pathway: PPARA activates gene expression; STRING 475 |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[R3HCC1]] | -0.43 | -0.36 / -0.38 | both halves | 9e-05 |  |
| [[TAF1A]] | -0.42 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[SNHG11]] | -0.41 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[MRPS18C]] | -0.41 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[PDRG1]] | -0.41 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[ZNF23]] | -0.41 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[ESF1]] | -0.40 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[TTF1]] | -0.40 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[MAP1S]] | -0.40 | -0.27 / -0.38 | both halves | 3e-04 |  |
| [[SEC62]] | -0.40 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[ZC3H13]] | -0.40 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[MED18]] | -0.40 | -0.32 / -0.49 | both halves | 2e-04 | pathway: PPARA activates gene expression |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCSK9]] | B | PCSK9 activity lowers FADS1's level | lines that do not express PCSK9 (28) vs lines expressing it (22) | 2.83× higher at baseline in the lines without PCSK9 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: C6orf132, RNF223, CDH1 |
| [[ELOVL5]] | B | ELOVL5 activity raises FADS1's level | lines that do not express ELOVL5 (6) vs lines expressing it (44) | 5.59× lower at baseline in the lines without ELOVL5 | 0.074 | ⚠ within organs, on part of the lines; also absent: PDE4A, TCEA2, MPP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.652). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.7, -50.0); signed map (-51.7, 32.0). **Vector** length 109, 31.8% of its response variance represented; |z| ≥ 3 in 1,115 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *cholesterol homeostasis* (hallmark, mean cos +0.51 to 24); *Activation of gene expression by SREBF (SREBP)* (reactome, mean cos +0.50 to 16); *Cholesterol biosynthesis via desmosterol (Bloch pathway)* (reactome, mean cos +0.54 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +6.4 | +11.0 |
|  | [[Berbamine (drug)]] 5 µM |  | +5.9 | +9.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.4 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +7.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +2.9 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +3.5 | +2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.4 | +6.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.8 | -14.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.6 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.0 | -9.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -2.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.4 | -5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -2.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.2 | +0.3 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.1 | -0.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | fatty acid desaturase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.2 — chr11:61,799,627-61,829,318 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D5D, FADSD5, TU12, FADS6; previously LLCDL1 |
| Gene groups (HGNC) | Fatty acid desaturases; MicroRNA protein coding host genes; Cytochrome b5 domain containing |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME, ANDROGEN_RESPONSE, MTORC1_SIGNALING |
| Reactome | 7 pathways, smallest: Linoleic acid (LA) metabolism; alpha-linolenic (omega3) and linoleic (omega6) acid metabolism; alpha-linolenic acid (ALA) metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O60427](https://www.uniprot.org/uniprotkb/O60427) (Acyl-CoA):

> [Isoform 1]: Acts as a front-end fatty acyl-coenzyme A (CoA) desaturase that introduces a cis double bond at carbon 5 located between a preexisting double bond and the carboxyl end of the fatty acyl chain. Involved in biosynthesis of highly unsaturated fatty acids (HUFA) from the essential polyunsaturated fatty acids (PUFA) linoleic acid (LA) (18:2n-6) and alpha-linolenic acid (ALA) (18:3n-3) precursors. Specifically, desaturates dihomo-gamma-linoleoate (DGLA) (20:3n-6) and eicosatetraenoate …

**Summary**, from NCBI Gene [3992](https://www.ncbi.nlm.nih.gov/gene/3992):

> The protein encoded by this gene is a member of the fatty acid desaturase (FADS) gene family. Desaturase enzymes regulate unsaturation of fatty acids through the introduction of double bonds between defined carbons of the fatty acyl chain. FADS family members are considered fusion products composed of an N-terminal cytochrome b5-like domain and a C-terminal multiple membrane-spanning desaturase portion, both of which are characterized by conserved histidine motifs. This gene is clustered with …

**Accessions** — [HGNC:3574](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3574) · Entrez [3992](https://www.ncbi.nlm.nih.gov/gene/3992) · UniProt [O60427](https://www.uniprot.org/uniprotkb/O60427) · Ensembl [ENSG00000149485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149485)

## Data

Gene col 7378: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7378); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7378, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7378]; `tensor/DDL_lfc|DDL_z.npy` [7378]; `embed/gene_vectors.npy` [7378]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7378 or target_col == 7378). Every well: [[FADS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FADS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
