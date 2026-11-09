---
symbol: "FAM120AOS"
type: "gene"
col: 12067
ensembl_id: "ENSG00000188938"
name: "family with sequence similarity 120 member A opposite strand"
location: "9q22.31"
module: 10
arm: "+"
pooled_cpm: 35.3
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 14
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# FAM120AOS

*family with sequence similarity 120 member A opposite strand* — 9q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.75× (z +25.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.674× (z -7.1, q 1e-09, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (78 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01135]] (+0.71, fdr 4e-05), [[PKN2-AS1]] (+0.71, fdr 1e-04), [[TSGA10]] (+0.70, fdr 6e-05); moves opposite to [[RSAD1]] (-0.67, fdr 5e-05), [[FAM118A]] (-0.64, fdr 6e-04), [[WRAP73]] (-0.63, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12067.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.75×** | +25.6 | 0e+00 | 47/48 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.54×** | +16.7 | 0e+00 | 47/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +16.1 | 0e+00 | 37/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +13.8 | 3e-41 | 36/39 (A-427, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +12.2 | 3e-32 | 38/44 (Panc 03.27, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +12.0 | 4e-31 | 38/48 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +11.6 | 6e-29 | 40/47 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +9.4 | 4e-19 | 36/47 (RKO, HT-29, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +8.7 | 3e-16 | 36/48 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +8.6 | 6e-16 | 35/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +8.0 | 9e-14 | 28/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.39×** | +5.9 | 2e-07 | 34/48 (SW480, KATO III, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.31×** | +4.9 | 4e-05 | 23/48 (A498, NCI-H460, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.21×** | +4.8 | 6e-05 | 24/48 (PANC-1, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +4.7 | 8e-05 | 21/48 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.002 | 19/47 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.46×** | +4.0 | 0.002 | 16/48 (NCI-H1792, A-427, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.028 | 12/47 (KATO III, A-172, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.036 | 17/48 (PANC-1, RKO, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.14× | +3.2 | 0.040 | 13/48 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.064 | 5/48 (SNU-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12067.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.674×** | -7.1 | 1e-09 | 34/48 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.700×** | -6.4 | 6e-08 | 26/47 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.772×** | -4.6 | 8e-04 | 22/48 (SK-MEL-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.775×** | -4.5 | 8e-04 | 24/47 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.779×** | -4.4 | 1e-03 | 21/47 (SW 900, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.629×** | -4.3 | 0.001 | 19/48 (MIA PaCa-2, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.810×** | -3.7 | 0.014 | 22/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -3.1 | 0.15 | 16/47 (PANC-1, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12067. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 45.7 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +14.6) | — |
| [[NCI-H460 (line)]] | wt | 35.6 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +18.5) | — |
| [[A498 (line)]] | wt | 30.6 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +13.8) | — |
| [[HEC-1-A (line)]] | alt | 77.5 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +13.5) | — |
| [[HOP62 (line)]] | alt | 31.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +14.2) | — |
| [[PANC-1 (line)]] | alt | 26.5 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +15.1) | — |
| [[HT-29 (line)]] | alt | 42.7 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +12.9) | — |
| [[LoVo (line)]] | wt | 41.5 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +12.9) | [[Digitoxin (drug)]] 5 µM 0.305× (z -11.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 26.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.34× (z +15.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 38.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.4) | — |
| [[NCI-H1792 (line)]] | alt | 25.9 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +12.8) | — |
| [[NCI-H2347 (line)]] | alt | 33.3 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 33.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +13.2) | — |
| [[RKO (line)]] | wt | 48.1 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +11.9) | — |
| [[SNU-423 (line)]] | alt | 35.1 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +10.8) | [[Verteporfin (drug)]] 5 µM 0.292× (z -8.8) |
| [[A549 (line)]] | wt | 43.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +11.2) | — |
| [[AsPC-1 (line)]] | alt | 17.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.30× (z +14.2) | — |
| [[C32 (line)]] | wt | 24.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +12.4) | — |
| [[CFPAC-1 (line)]] | alt | 20.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +12.6) | — |
| [[HCT15 (line)]] | alt | 55.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +13.0) | — |
| [[Hs 766T (line)]] | wt | 26.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +12.8) | — |
| [[HS-578T (line)]] | alt | 31.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +13.4) | — |
| [[J82 (line)]] | alt | 46.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +10.6) | — |
| [[LS 180 (line)]] | wt | 36.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +12.9) | — |
| [[NCI-H1573 (line)]] | alt | 29.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 17.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.70× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 29.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 45.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +9.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.323× (z -9.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 27.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +13.2) | — |
| [[A-427 (line)]] | wt | 34.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.02× (z +12.5) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 34.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +10.2) | — |
| [[C-33 A (line)]] | alt | 54.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 50.7 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.65× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 21.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 25.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0768× (z -14.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 29.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +12.1) | — |
| [[KATO III (line)]] | alt | 53.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 27.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +10.2) | — |
| [[SHP-77 (line)]] | alt | 34.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +10.4) | — |
| [[SW 900 (line)]] | alt | 19.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.52× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 34.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +14.8) | — |
| [[SW48 (line)]] | wt | 25.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +11.2) | — |
| [[AN3 CA (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12067), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 22 of them with an alert (⚠; 22 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01135]] | +0.71 | +0.74 / +0.42 | both halves | 4e-05 |  |
| [[PKN2-AS1]] | +0.71 | +0.80 / +0.33 | both halves | 1e-04 |  |
| [[TSGA10]] | +0.70 | +0.78 / +0.39 | both halves | 6e-05 |  |
| [[PDCL3P4]] | +0.70 | +0.82 / +0.30 | both halves | 2e-04 |  |
| [[PPP3CB-AS1]] | +0.69 | +0.75 / +0.34 | both halves | 1e-04 |  |
| [[F8]] | +0.68 | +0.79 / +0.29 | both halves | 2e-04 |  |
| [[IRAK4]] | +0.67 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[USP11]] | +0.67 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[TBCE-1]] | +0.67 | +0.70 / +0.37 | both halves | 9e-05 |  |
| [[AP4S1]] | +0.66 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[MMADHC-DT]] | +0.66 | +0.77 / +0.21 | both halves | 7e-04 |  |
| [[PPP1R12A-AS2]] | +0.66 | +0.77 / +0.22 | both halves | 6e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSAD1]] | -0.67 | -0.61 / -0.39 | both halves | 5e-05 |  |
| [[FAM118A]] | -0.64 | -0.69 / -0.22 | both halves | 6e-04 |  |
| [[WRAP73]] | -0.63 | -0.58 / -0.32 | both halves | 2e-04 |  |
| [[L2HGDH]] | -0.63 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[TOMM5]] | -0.63 | -0.66 / -0.36 | both halves | 1e-04 |  |
| [[ZNF692]] | -0.62 | -0.67 / -0.48 | both halves | 2e-05 |  |
| [[C20orf27]] | -0.62 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[TRABD]] | -0.62 | -0.64 / -0.35 | both halves | 1e-04 |  |
| [[NHP2]] | -0.62 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[KLHL8]] | -0.62 | -0.53 / -0.37 | both halves | 9e-05 |  |
| [[FAM24B]] | -0.61 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[BRF1]] | -0.61 | -0.64 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FAM120AOS's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.629). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.3, 13.7); signed map (24.6, -8.1). **Vector** length 88.3, 21.5% of its response variance represented; |z| ≥ 3 in 988 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +16.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +11.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +25.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | +8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +8.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.1 | +0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | +5.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.0 | +0.5 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | +2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -5.0 | +4.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | +1.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | -3.3 | +3.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 120 member A opposite strand |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.31 — chr9:93,431,441-93,453,581 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C9orf10OS |
| Matched by | ensembl_id |

UniProt [Q5T036](https://www.uniprot.org/uniprotkb/Q5T036) carries no function annotation.

**Summary**, from NCBI Gene [158293](https://www.ncbi.nlm.nih.gov/gene/158293):

> Differences in the expression level of this gene are associated with the survival rate of those with glioma. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:23389](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23389) · Entrez [158293](https://www.ncbi.nlm.nih.gov/gene/158293) · UniProt [Q5T036](https://www.uniprot.org/uniprotkb/Q5T036) · Ensembl [ENSG00000188938](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188938)

## Data

Gene col 12067: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12067); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12067, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12067]; `tensor/DDL_lfc|DDL_z.npy` [12067]; `embed/gene_vectors.npy` [12067]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12067 or target_col == 12067). Every well: [[FAM120AOS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM120AOS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
