---
symbol: "KIF26B"
type: "gene"
col: 8588
ensembl_id: "ENSG00000162849"
name: "kinesin family member 26B"
location: "1q44"
module: 26
arm: "+"
pooled_cpm: 36.64
n_lines_expressing: 40
n_dd_up: 21
n_dd_down: 9
n_dd_up_clean: 17
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# KIF26B

*kinesin family member 26B* — 1q44

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.85× (z +36.3, q 0e+00, up in 33 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.593× (z -8.5, q 1e-14, down in 25 of 37 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DKK2]] (+0.67, fdr 1e-05), [[GRM8]] (+0.64, fdr 4e-05), [[NPAS3]] (+0.63, fdr 1e-05); moves opposite to [[WRAP73]] (-0.58, fdr 4e-04), [[MAST3]] (-0.58, fdr 7e-04), [[PCTP]] (-0.57, fdr 6e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8588.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.85×** | +36.3 | 0e+00 | 33/37 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.74×** | +15.7 | 0e+00 | 28/36 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +11.2 | 4e-27 | 27/38 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.92×** | +10.6 | 5e-24 | 22/37 (A-172, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.76×** | +9.2 | 4e-18 | 23/38 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +8.3 | 1e-14 | 19/38 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +6.4 | 1e-08 | 10/34 (HOP62, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +5.9 | 2e-07 | 13/38 (COLO 205, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +4.5 | 4e-04 | 11/37 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.32×** | +4.5 | 4e-04 | 10/37 (SHP-77, RKO, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +4.5 | 4e-04 | 12/27 (HOP62, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Brimonidine (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.011 | 10/38 (RPMI-7951, SW1417, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +3.5 | 0.024 | 13/37 (H4, PANC-1, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.026 | 8/38 (SHP-77, NCI-H2347, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.041 | 6/38 (SW 1088, HOP62, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.15× | +3.2 | 0.047 | 7/38 (SHP-77, RPMI-7951, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.059 | 7/36 (SHP-77, LOX-IMVI, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.44×** | +3.1 | 0.059 | 4/34 (A498, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.063 | 8/37 (NCI-H1792, H4, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8588.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.593×** | -8.5 | 1e-14 | 25/37 (SHP-77, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.627×** | -7.6 | 8e-12 | 23/38 (SHP-77, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.646×** | -7.1 | 2e-10 | 25/38 (SHP-77, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.728×** | -5.2 | 3e-05 | 21/36 (SW48, hTERT-HPNE, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.755×** | -4.6 | 5e-04 | 22/38 (SHP-77, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **0.786×** | -3.9 | 0.008 | 19/35 (KATO III, SW480, …) | all doses, flat | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.859× | -3.5 | 0.035 | 13/39 (CHP-212, SW480, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.868× | -3.3 | 0.072 | 7/39 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.820×** | -3.2 | 0.072 | 11/38 (HT-29, SHP-77, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.821×** | -3.2 | 0.072 | 15/37 (COLO 205, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.827×** | -3.1 | 0.099 | 12/36 (CFPAC-1, C32, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.819× | -3.0 | 0.12 | 4/37 (HepG2/C3A, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8588. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 408 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0997× (z -24.4) |
| [[COLO 205 (line)]] | alt | 128 | 2 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.02× (z +21.8) | [[Panobinostat (drug)]] 0.5 µM 0.110× (z -17.5) |
| [[LoVo (line)]] | wt | 45.8 | 4 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.80× (z +26.8) | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -10.6) |
| [[SW480 (line)]] | alt | 118 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.132× (z -21.0) |
| [[A-172 (line)]] | wt | 12.2 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.4× (z +20.4) | — |
| [[NCI-H460 (line)]] | wt | 11.3 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.6× (z +24.9) | — |
| [[AN3 CA (line)]] | alt | 127 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -14.3) |
| [[A498 (line)]] | wt | 12.6 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 17.9× (z +16.3) | — |
| [[HepG2_C3A (line)]] | wt | 103 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -13.0) |
| [[HOP62 (line)]] | alt | 9.34 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +18.8) | — |
| [[C32 (line)]] | wt | 55.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.201× (z -9.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 111 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -11.0) |
| [[HCT15 (line)]] | alt | 17.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.24× (z +11.4) | — |
| [[LOX-IMVI (line)]] | wt | 49.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +14.7) | — |
| [[NCI-H1573 (line)]] | alt | 10.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.79× (z +13.0) | — |
| [[RKO (line)]] | wt | 55.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.204× (z -9.9) |
| [[SW1417 (line)]] | alt | 65.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.245× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.285× (z -8.5) |
| [[BT-474 (line)]] | alt | 9.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.7× (z +15.8) | — |
| [[C-33 A (line)]] | alt | 18.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.22× (z +13.5) | — |
| [[H4 (line)]] | wt | 53.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 25.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 21.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +9.9) | — |
| [[hTERT-HPNE (line)]] | wt | 70.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0561× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[KATO III (line)]] | alt | 71.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.150× (z -13.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 46.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +10.5) | — |
| [[NCI-H23 (line)]] | alt | 16.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 18.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.07× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 10.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +14.9) | — |
| [[RPMI-7951 (line)]] | alt | 53.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.19× (z +13.2) | — |
| [[SW 900 (line)]] | alt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.12× (z +10.9) | — |
| [[SW48 (line)]] | wt | 36.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.115× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.94 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.28 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.12 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.70 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.17 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.96 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.58 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.91 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8588), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DKK2]] | +0.67 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[GRM8]] | +0.64 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[NPAS3]] | +0.63 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[TMEM117]] | +0.63 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[ADAMTS19]] | +0.62 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[PITX1-AS1]] | +0.61 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[NINJ2]] | +0.60 | +0.57 / +0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[CRPPA]] | +0.59 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[LIX1-AS1]] | +0.59 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[HAS2-AS1]] | +0.59 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[LYPLAL1-AS1]] | +0.58 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[CIBAR1-DT]] | +0.58 | +0.51 / +0.29 | both halves | 3e-04 |  |
| [[LINC01340]] | +0.58 | +0.50 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WRAP73]] | -0.58 | -0.55 / -0.25 | both halves | 4e-04 |  |
| [[MAST3]] | -0.58 | -0.60 / -0.20 | both halves | 7e-04 |  |
| [[PCTP]] | -0.57 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[TTLL1]] | -0.57 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[SUFU]] | -0.55 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[PLD2]] | -0.54 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[CNEP1R1]] | -0.54 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[FN3KRP]] | -0.54 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[ARRB2]] | -0.53 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[DPY30]] | -0.53 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[YIF1B]] | -0.53 | -0.50 / -0.12 | ⚠ not reproduced | 0.002 |  |
| [[PCMT1]] | -0.52 | -0.49 / -0.18 | ⚠ not reproduced | 0.001 |  |
| [[CEP57L1]] | -0.52 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[ALAD]] | -0.52 | -0.30 / -0.33 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KIF26B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LGR5]] | B | LGR5 activity raises KIF26B's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 3.37× lower at baseline in the lines without LGR5 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573 |
| [[PROX1-AS1]] | B | PROX1-AS1 activity raises KIF26B's level | lines that do not express PROX1-AS1 (29) vs lines expressing it (21) | 3.09× lower at baseline in the lines without PROX1-AS1 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST18, AXIN2, PROX1 |
| [[HDAC6]] | B | HDAC6 activity raises KIF26B's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.510). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (25.4, 36.5); signed map (37.2, 18.3). **Vector** length 102, 24.0% of its response variance represented; |z| ≥ 3 in 1,023 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +14.8 | +36.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.0 | +6.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +11.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.6 | +8.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +15.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.4 | +10.6 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +2.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.4 | +3.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.1 | -7.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.4 | -4.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.4 | -8.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -3.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.9 | -0.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 26B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q44 — chr1:245,154,985-245,709,432 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10157 |
| Gene groups (HGNC) | Kinesins |
| Reactome | 8 pathways, smallest: Kinesins; COPI-dependent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2KJY2](https://www.uniprot.org/uniprotkb/Q2KJY2) (Kinesin-like protein KIF26B):

> Essential for embryonic kidney development. Plays an important role in the compact adhesion between mesenchymal cells adjacent to the ureteric buds, possibly by interacting with MYH10. This could lead to the establishment of the basolateral integrity of the mesenchyme and the polarized expression of ITGA8, which maintains the GDNF expression required for further ureteric bud attraction. Although it seems to lack ATPase activity it is constitutively associated with microtubules (By similarity).

**Summary**, from NCBI Gene [55083](https://www.ncbi.nlm.nih.gov/gene/55083):

> The protein encoded by this gene is an intracellular motor protein thought to transport organelles along microtubules. The encoded protein is required for kidney development. Elevated levels of this protein have been found in some breast and colorectal cancers. [provided by RefSeq, Mar 2017]

**Accessions** — [HGNC:25484](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25484) · Entrez [55083](https://www.ncbi.nlm.nih.gov/gene/55083) · UniProt [Q2KJY2](https://www.uniprot.org/uniprotkb/Q2KJY2) · Ensembl [ENSG00000162849](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162849)

## Data

Gene col 8588: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8588); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8588, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8588]; `tensor/DDL_lfc|DDL_z.npy` [8588]; `embed/gene_vectors.npy` [8588]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8588 or target_col == 8588). Every well: [[KIF26B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF26B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
