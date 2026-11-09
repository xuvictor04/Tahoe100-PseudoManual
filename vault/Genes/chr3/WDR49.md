---
symbol: "WDR49"
type: "gene"
col: 10524
ensembl_id: "ENSG00000174776"
name: "WD repeat domain 49"
location: "3q26.1"
module: 37
arm: "+"
pooled_cpm: 17.71
n_lines_expressing: 47
n_dd_up: 26
n_dd_down: 17
n_dd_up_clean: 21
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# WDR49

*WD repeat domain 49* — 3q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.83× (z +20.1, q 0e+00, up in 39 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Belumosudil (drug)]] 5 µM: 0.466× (z -6.7, q 1e-08, down in 25 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02680]] (+0.87, fdr 7e-06), [[C9orf153]] (+0.82, fdr 7e-06), [[SNX31]] (+0.80, fdr 7e-06).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CASC20]] → it (grade B ⚠); 5 go from it, the strongest it → [[TMEM269]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10524.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.83×** | +20.1 | 0e+00 | 39/41 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **7.04×** | +16.9 | 0e+00 | 37/41 (HS-578T, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **6.49×** | +16.2 | 0e+00 | 37/40 (Panc 03.27, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.76×** | +9.1 | 9e-18 | 34/42 (SW480, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.59×** | +8.6 | 1e-15 | 39/44 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **5.42×** | +8.0 | 2e-13 | 38/44 (A498, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.06×** | +6.5 | 7e-09 | 32/44 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +6.5 | 8e-09 | 23/41 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.01×** | +6.3 | 2e-08 | 29/44 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +5.7 | 9e-07 | 20/44 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +5.6 | 1e-06 | 20/41 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.85×** | +5.5 | 2e-06 | 26/42 (SW480, SW 900, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.76×** | +5.1 | 2e-05 | 25/44 (SHP-77, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.92×** | +5.1 | 2e-05 | 18/24 (SW480, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +4.7 | 9e-05 | 18/39 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **2.33×** | +4.0 | 0.002 | 16/45 (HEC-1-A, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +4.0 | 0.002 | 22/44 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.005 | 14/44 (NCI-H23, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~25% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10524.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.466×** | -6.7 | 1e-08 | 25/42 (NCI-H1573, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.590×** | -4.8 | 4e-04 | 21/33 (hTERT-HPNE, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Pralsetinib (drug)]] 5 µM |  | **0.375×** | -4.6 | 6e-04 | 24/38 (SHP-77, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.707×** | -4.5 | 0.001 | 24/45 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.633×** | -4.2 | 0.004 | 20/45 (A498, NCI-H1573, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.658×** | -3.8 | 0.011 | 17/45 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.660×** | -3.8 | 0.011 | 15/44 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.660×** | -3.8 | 0.011 | 15/44 (SW 1271, hTERT-HPNE, …) | rises with dose |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.667×** | -3.7 | 0.014 | 16/44 (LoVo, NCI-H460, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.465×** | -3.6 | 0.015 | 16/38 (LOX-IMVI, J82, …) | top dose only | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.674×** | -3.6 | 0.017 | 11/44 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.665×** | -3.6 | 0.017 | 16/23 (hTERT-HPNE, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.684×** | -3.5 | 0.023 | 15/43 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.693×** | -3.4 | 0.033 | 12/44 (SW48, NCI-H1573, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.699×** | -3.3 | 0.040 | 14/45 (HOP62, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.712×** | -3.1 | 0.068 | 13/44 (CHP-212, NCI-H1573, …) | inconsistent across doses |  |
| [[Posaconazole (drug)]] 5 µM |  | **0.710×** | -3.0 | 0.088 | 7/44 (SW480, A549, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10524. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 24.1 | 4 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.49× (z +13.4) | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -11.3) |
| [[SW480 (line)]] | alt | 11.2 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.00× (z +11.6) | — |
| [[HOP62 (line)]] | alt | 50.4 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 20.4 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -11.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 21.6 | 4 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.94× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 43.9 | 3 | 2 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.02× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.314× (z -10.0) |
| [[C32 (line)]] | wt | 20.7 | 3 | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 18.8× (z +10.2) | [[Belumosudil (drug)]] 5 µM 0.0815× (z -8.7) |
| [[LoVo (line)]] | wt | 7.51 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +12.2) | — |
| [[LOX-IMVI (line)]] | wt | 23.0 | 4 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +11.8) | — |
| [[Panc 03.27 (line)]] | alt | 7.41 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +12.7) | [[Radotinib (drug)]] 0.5 µM 0.0781× (z -9.0) |
| [[BT-474 (line)]] | alt | 26.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 7.17× (z +8.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 6.54× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -9.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 10.9 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.84× (z +10.0) | — |
| [[HS-578T (line)]] | alt | 11.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.0× (z +15.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.84 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.9× (z +12.7) | — |
| [[NCI-H1573 (line)]] | alt | 84.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0502× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.160× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 11.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.90× (z +10.9) | — |
| [[HEC-1-A (line)]] | alt | 49.3 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.51× (z +11.9) | — |
| [[HepG2_C3A (line)]] | wt | 11.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.76× (z +9.3) | [[Ponatinib (drug)]] 5 µM 0.0573× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 38.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0315× (z -16.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 13.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.39× (z +12.9) | — |
| [[RKO (line)]] | wt | 14.3 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 21.7× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 19.0 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +9.1) | [[Harringtonine (drug)]] 5 µM 0.0952× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 17.2 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 14.6× (z +10.6) | — |
| [[A498 (line)]] | wt | 19.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.34× (z +11.7) | — |
| [[CFPAC-1 (line)]] | alt | 15.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +11.0) | — |
| [[CHP-212 (line)]] | wt | 89.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -8.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 5.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.39× (z +9.6) | — |
| [[J82 (line)]] | alt | 13.1 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +10.3) | — |
| [[NCI-H1792 (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0651× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 6.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +11.1) | — |
| [[SNU-423 (line)]] | alt | 5.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +10.1) | — |
| [[A-427 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10524), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02680]] | +0.87 | +0.85 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[C9orf153]] | +0.82 | +0.82 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[SNX31]] | +0.80 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[DRC1]] | +0.76 | +0.75 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[LINC02936]] | +0.76 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[LINC00640]] | +0.76 | +0.74 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[TICAM2]] | +0.76 | +0.68 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[ADCY10]] | +0.75 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[CORIN]] | +0.75 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[TEX29]] | +0.74 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[CCDC62]] | +0.74 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[LVRN]] | +0.74 | +0.73 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASC20]] | B | CASC20 activity raises WDR49's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 2.32× lower at baseline in the lines without CASC20 | 0.003 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers WDR49's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NPR3]] | B | NPR3 activity raises WDR49's level | lines that do not express NPR3 (7) vs lines expressing it (43) | 2.39× lower at baseline in the lines without NPR3 | 0.071 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[IQCJ]] | C | IQCJ activity raises WDR49's level | lines that do not express IQCJ (6) vs lines expressing it (44) | 2.70× lower at baseline in the lines without IQCJ | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000222042, MR1, HECTD2; maybe low, not absent; co-absent with the target |
| [[CORIN]] | C | CORIN activity raises WDR49's level | lines that do not express CORIN (5) vs lines expressing it (45) | 2.70× lower at baseline in the lines without CORIN | 0.092 | ⚠ within organs, on part of the lines; also absent: TNNI3K, WDR49, ENSG00000229195; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM269]] | C | WDR49 activity raises TMEM269's level | lines that do not express WDR49 (3) vs lines expressing it (47) | 2.15× lower at baseline in the lines without WDR49 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FOXP1, ENSG00000286952, CORIN; maybe low, not absent; its own permutation p |
| [[PELO-AS1]] | C | WDR49 activity raises PELO-AS1's level | lines that do not express WDR49 (3) vs lines expressing it (47) | 1.82× lower at baseline in the lines without WDR49 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FOXP1, ENSG00000286952, CORIN; maybe low, not absent; its own permutation p |
| [[TPTE2]] | C | WDR49 activity raises TPTE2's level | lines that do not express WDR49 (3) vs lines expressing it (47) | 2.43× lower at baseline in the lines without WDR49 | 0.065 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FOXP1, ENSG00000286952, CORIN; maybe low, not absent |
| [[TEX29]] | C | WDR49 activity raises TEX29's level | lines that do not express WDR49 (3) vs lines expressing it (47) | 1.53× lower at baseline in the lines without WDR49 | 0.075 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FOXP1, ENSG00000286952, CORIN; maybe low, not absent |
| [[CCDC146]] | C | WDR49 activity raises CCDC146's level | lines that do not express WDR49 (3) vs lines expressing it (47) | 2.18× lower at baseline in the lines without WDR49 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FOXP1, ENSG00000286952, CORIN; maybe low, not absent |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.906). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.5, -18.0); signed map (10.9, 5.4). **Vector** length 110, 29.7% of its response variance represented; |z| ≥ 3 in 1,084 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +16.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +16.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +20.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +9.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +5.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.7 | +8.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +2.7 | +4.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.3 | -0.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.2 | -6.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.5 | +5.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -3.4 | -4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.7 | -4.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.4 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 49 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.1 — chr3:167,478,684-167,653,983 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33620 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IV35](https://www.uniprot.org/uniprotkb/Q8IV35) (Cilia- and flagella-associated protein 337):

> Associates with components of the nexin-dynein regulatory complex (N-DRC), a key regulator of ciliary/flagellar motility, and might act as an inner dynein arm (IDA) hub or linkage.

**Summary**, from NCBI Gene [151790](https://www.ncbi.nlm.nih.gov/gene/151790):

> This gene encodes a member of the WD repeat protein family with nine WD repeats. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:26587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26587) · Entrez [151790](https://www.ncbi.nlm.nih.gov/gene/151790) · UniProt [Q8IV35](https://www.uniprot.org/uniprotkb/Q8IV35) · Ensembl [ENSG00000174776](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174776)

## Data

Gene col 10524: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10524); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10524, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10524]; `tensor/DDL_lfc|DDL_z.npy` [10524]; `embed/gene_vectors.npy` [10524]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10524 or target_col == 10524). Every well: [[WDR49 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR49.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
