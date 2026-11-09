---
symbol: "TMEM117"
type: "gene"
col: 6270
ensembl_id: "ENSG00000139173"
name: "transmembrane protein 117"
location: "12q12"
module: 124
arm: "+"
pooled_cpm: 61.76
n_lines_expressing: 47
n_dd_up: 13
n_dd_down: 13
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# TMEM117

*transmembrane protein 117* — 12q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.63× (z +15.9, q 0e+00, up in 40 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.525× (z -7.4, q 6e-11, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A21]] (+0.71, fdr 2e-05), [[CRPPA]] (+0.68, fdr 1e-05), [[GRIP1]] (+0.68, fdr 1e-05); moves opposite to [[IFT172]] (-0.62, fdr 5e-05), [[ALAD]] (-0.59, fdr 1e-04), [[ARNT]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[(S)-Crizotinib (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6270.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.63×** | +15.9 | 0e+00 | 40/46 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.28×** | +9.2 | 1e-17 | 36/44 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.95×** | +7.7 | 2e-12 | 32/45 (NCI-H2347, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.0 | 2e-07 | 35/45 (A549, HS-578T, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +6.0 | 3e-07 | 31/47 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.53×** | +4.7 | 2e-04 | 30/44 (C32, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +4.7 | 3e-04 | 23/45 (SK-MEL-2, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +4.6 | 4e-04 | 23/45 (HOP62, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.021 | 24/45 (RKO, NCI-H2030, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.38×** | +3.3 | 0.064 | 24/45 (SNU-423, NCI-H1573, …) | inconsistent across doses |  |
| [[Meloxicam (drug)]] 0.05 µM |  | **1.35×** | +3.1 | 0.094 | 14/45 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.094 | 21/45 (A549, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.65×** | +3.1 | 0.098 | 21/41 (HEC-1-A, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6270.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.525×** | -7.4 | 6e-11 | 30/45 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.582×** | -6.3 | 8e-08 | 24/45 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.582×** | -6.3 | 8e-08 | 29/45 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.364×** | -6.1 | 1e-07 | 33/46 (RKO, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM |  | **0.730×** | -5.1 | 3e-05 | 31/45 (KATO III, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **0.642×** | -5.1 | 3e-05 | 30/44 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.676×** | -4.2 | 0.002 | 29/45 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.705×** | -4.0 | 0.004 | 25/44 (RKO, HT-29, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.707×** | -4.0 | 0.004 | 21/44 (A549, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.570×** | -3.4 | 0.039 | 19/44 (A-427, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.759×** | -3.2 | 0.076 | 22/45 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.765×** | -3.1 | 0.089 | 18/45 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.765×** | -3.1 | 0.089 | 21/45 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6270. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 160 | 3 | 9 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.58× (z +18.7) | [[Panobinostat (drug)]] 5 µM 0.163× (z -19.0) |
| [[A498 (line)]] | wt | 44.6 | 2 | 5 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.57× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -15.1) |
| [[RKO (line)]] | wt | 174 | 1 | 6 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 45.5 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 9.70× (z +12.1) | [[Selinexor (drug)]] 5 µM 0.251× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 39.6 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.161× (z -10.4) |
| [[HT-29 (line)]] | alt | 49.5 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.227× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 48.6 | 2 | 3 | [[Auranofin (drug)]] 5 µM 4.59× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.164× (z -13.3) |
| [[SK-MEL-2 (line)]] | alt | 96.9 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +14.2) | — |
| [[NCI-H460 (line)]] | wt | 66.1 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.81× (z +18.7) | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.267× (z -8.8) ⚠ cell-cycle shift, explains ~64% of this change |
| [[SW1417 (line)]] | alt | 135 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.309× (z -11.4) |
| [[SW480 (line)]] | alt | 111 | 1 | 3 | [[Auranofin (drug)]] 5 µM 4.11× (z +13.6) | [[Panobinostat (drug)]] 5 µM 0.264× (z -12.8) |
| [[A549 (line)]] | wt | 23.6 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.65× (z +14.6) | [[Digitoxin (drug)]] 5 µM 0.141× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[BT-474 (line)]] | alt | 17.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.96× (z +14.2) | — |
| [[C-33 A (line)]] | alt | 160 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.204× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 61.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +13.2) | — |
| [[HOP62 (line)]] | alt | 29.8 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.79× (z +8.5) | [[Adagrasib (drug)]] 0.05 µM 0.379× (z -16.5) ⚠ position not correctable · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.126× (z -10.0) |
| [[KATO III (line)]] | alt | 82.5 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +10.1) | [[Belinostat (drug)]] 5 µM 0.212× (z -11.6) |
| [[LS 180 (line)]] | wt | 112 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.84× (z +16.7) | — |
| [[SHP-77 (line)]] | alt | 73.1 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.278× (z -10.2) |
| [[SNU-1 (line)]] | wt | 134 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +13.2) | — |
| [[A-172 (line)]] | wt | 24.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.225× (z -8.5) |
| [[C32 (line)]] | wt | 123 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +8.5) ⚠ cell-cycle shift, explains ~84% of this change | [[Lonafarnib (drug)]] 5 µM 0.0549× (z -10.8) ⚠ toxic |
| [[H4 (line)]] | wt | 20.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.65× (z +11.9) | — |
| [[HCT15 (line)]] | alt | 59.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +11.4) | — |
| [[hTERT-HPNE (line)]] | wt | 29.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.34× (z +14.7) | — |
| [[NCI-H23 (line)]] | alt | 29.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +10.0) | [[Digitoxin (drug)]] 0.5 µM 0.222× (z -9.5) ⚠ cell-cycle shift, explains ~66% of this change |
| [[NCI-H2347 (line)]] | alt | 53.4 | 1 | 1 | [[Auranofin (drug)]] 5 µM 6.86× (z +13.7) | [[Panobinostat (drug)]] 0.5 µM 0.308× (z -8.5) |
| [[SW 900 (line)]] | alt | 20.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +9.7) | [[Harringtonine (drug)]] 0.05 µM 0.0498× (z -14.3) |
| [[AN3 CA (line)]] | alt | 141 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0730× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 17.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +10.9) | — |
| [[LOX-IMVI (line)]] | wt | 44.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +10.4) | — |
| [[NCI-H1792 (line)]] | alt | 32.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 51.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 37.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.60× (z +8.8) | — |
| [[SW48 (line)]] | wt | 204 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.296× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~93% of this change |
| [[A-427 (line)]] | wt | 81.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.48 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 16.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6270), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A21]] | +0.71 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[CRPPA]] | +0.68 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[GRIP1]] | +0.68 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[ARSB]] | +0.67 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[MSRA]] | +0.66 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[AVEN]] | +0.63 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[KIF26B]] | +0.63 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[EPM2A]] | +0.62 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[ADCK1]] | +0.61 | +0.57 / +0.35 | both halves | 1e-04 |  |
| [[MMADHC-DT]] | +0.61 | +0.54 / +0.33 | both halves | 1e-04 |  |
| [[ST7]] | +0.60 | +0.60 / +0.27 | both halves | 3e-04 |  |
| [[ENOX2]] | +0.60 | +0.62 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT172]] | -0.62 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[ALAD]] | -0.59 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[ARNT]] | -0.58 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[POT1]] | -0.57 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[PCTP]] | -0.57 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[ETFB]] | -0.56 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[CHEK2]] | -0.56 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[RAB3A]] | -0.56 | -0.46 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[RAD17]] | -0.55 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[SLC27A1]] | -0.55 | -0.57 / -0.10 | ⚠ one half (not replicated) | 0.003 |  |
| [[HEATR5B]] | -0.55 | -0.54 / -0.23 | both halves | 5e-04 |  |
| [[RNF41]] | -0.55 | -0.46 / -0.24 | both halves | 5e-04 |  |
| [[KLHL26]] | -0.55 | -0.37 / -0.30 | both halves | 2e-04 |  |
| [[ARL3]] | -0.54 | -0.45 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TMEM117's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[(S)-Crizotinib (drug)]] 0.05 µM | C | TMEM117 activity raises the cells' numbers under (S)-Crizotinib 0.05 µM (protects the cells) | lines that do not express TMEM117 (3) vs lines expressing it (45) | the lines without TMEM117: 0.74× the cells of the other lines | 0.040 | ⚠ few lines (3 vs 47); across organs; also absent: KLHL9; maybe low, not absent |
| cells under [[Econazole (drug)]] 0.5 µM | C | TMEM117 activity raises the cells' numbers under Econazole 0.5 µM (protects the cells) | lines that do not express TMEM117 (3) vs lines expressing it (45) | the lines without TMEM117: 0.76× the cells of the other lines | 0.082 | ⚠ few lines (3 vs 47); across organs; also absent: KLHL9; maybe low, not absent |

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.691). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-3.9, 8.3); signed map (24.8, -31.0). **Vector** length 131, 40.7% of its response variance represented; |z| ≥ 3 in 1,274 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.7 | +15.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +11.1 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.7 | +6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.1 | +4.6 |
|  | [[Benztropine (mesylate) (drug)]] 0.05 µM |  | +2.9 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +4.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -8.8 | -6.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.8 | -7.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.5 | -6.3 |
|  | [[Artesunate (drug)]] 5 µM |  | -4.3 | -5.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.5 | -6.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.1 | -4.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.7 | -2.5 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -2.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 117 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q12 — chr12:43,835,967-44,389,762 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434K2435 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0C3](https://www.uniprot.org/uniprotkb/Q9H0C3) (Transmembrane protein 117):

> Involved in endoplasmic reticulum (ER) stress-induced cell death pathway.

**Summary**, from NCBI Gene [84216](https://www.ncbi.nlm.nih.gov/gene/84216):

> Involved in intrinsic apoptotic signaling pathway in response to endoplasmic reticulum stress. Located in endoplasmic reticulum and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25308](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25308) · Entrez [84216](https://www.ncbi.nlm.nih.gov/gene/84216) · UniProt [Q9H0C3](https://www.uniprot.org/uniprotkb/Q9H0C3) · Ensembl [ENSG00000139173](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139173)

## Data

Gene col 6270: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6270); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6270, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6270]; `tensor/DDL_lfc|DDL_z.npy` [6270]; `embed/gene_vectors.npy` [6270]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6270 or target_col == 6270). Every well: [[TMEM117 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM117.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
