---
symbol: "SLX4IP"
type: "gene"
col: 7368
ensembl_id: "ENSG00000149346"
name: "SLX4 interacting protein"
location: "20p12.2"
module: 1
arm: "+"
pooled_cpm: 50.77
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 27
n_dd_up_clean: 7
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SLX4IP

*SLX4 interacting protein* — 20p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 1.34× (z +3.7, q 0.069, up in 18 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.212× (z -20.7, q 0e+00, down in 46 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP41]] (+0.70, fdr 7e-06), [[AFG1L]] (+0.68, fdr 7e-06), [[SF3B3]] (+0.67, fdr 7e-06); moves opposite to [[TMEM165]] (-0.67, fdr 7e-06), [[TPTEP2-CSNK1E]] (-0.66, fdr 7e-06), [[CCDC168]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7368.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.34×** | +3.7 | 0.069 | 18/46 (HOP62, A-172, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.069 | 18/46 (RKO, LoVo, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.32×** | +3.4 | 0.095 | 20/47 (KATO III, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.095 | 19/45 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.095 | 14/46 (CFPAC-1, NCI-H1573, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.095 | 20/46 (AsPC-1, KATO III, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.095 | 21/46 (BT-474, hTERT-HPNE, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.095 | 11/46 (RKO, NCI-H1573, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.26× | +3.1 | 0.13 | 13/46 (LS 180, A-172, …) | inconsistent across doses |  |
| [[Brimonidine (drug)]] 5 µM |  | 1.26× | +3.0 | 0.13 | 11/46 (NCI-H1573, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7368.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.212×** | -20.7 | 0e+00 | 46/46 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.244×** | -18.8 | 0e+00 | 45/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.275×** | -17.2 | 0e+00 | 46/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.298×** | -16.1 | 0e+00 | 45/46 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.541×** | -11.3 | 2e-27 | 40/46 (SW480, COLO 205, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.488×** | -9.6 | 1e-19 | 38/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.561×** | -7.7 | 9e-13 | 35/46 (PANC-1, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.562×** | -7.4 | 1e-11 | 36/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.582×** | -7.2 | 3e-11 | 29/46 (NCI-H23, A-427, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.574×** | -7.1 | 6e-11 | 33/45 (RKO, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.632×** | -5.8 | 4e-07 | 36/46 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.637×** | -5.6 | 1e-06 | 27/43 (A-172, KATO III, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.661×** | -5.3 | 5e-06 | 28/45 (NCI-H23, SNU-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.664×** | -5.3 | 6e-06 | 30/47 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.492×** | -4.9 | 3e-05 | 29/42 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -4.9 | 3e-05 | 26/46 (A-427, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.780×** | -4.6 | 2e-04 | 30/47 (CFPAC-1, NCI-H2030, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.583×** | -3.8 | 0.004 | 23/46 (RKO, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.751×** | -3.3 | 0.022 | 18/45 (NCI-H23, CFPAC-1, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.715×** | -3.2 | 0.032 | 14/47 (SW480, KATO III, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7368. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 171 | 0 | 16 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0719× (z -26.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0945× (z -24.1) |
| [[PANC-1 (line)]] | alt | 49.0 | 0 | 12 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.121× (z -19.8) |
| [[NCI-H23 (line)]] | alt | 80.9 | 0 | 10 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -18.6) |
| [[KATO III (line)]] | alt | 109 | 0 | 8 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.218× (z -13.9) |
| [[NCI-H460 (line)]] | wt | 50.6 | 0 | 8 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.209× (z -13.0) |
| [[SHP-77 (line)]] | alt | 106 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.146× (z -18.1) |
| [[LS 180 (line)]] | wt | 62.8 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0986× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.168× (z -14.5) |
| [[SNU-1 (line)]] | wt | 60.0 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0937× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.132× (z -12.5) |
| [[A-427 (line)]] | wt | 42.8 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.157× (z -16.9) |
| [[COLO 205 (line)]] | alt | 114 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0864× (z -20.4) |
| [[HCT15 (line)]] | alt | 56.4 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -12.9) |
| [[LoVo (line)]] | wt | 52.4 | 1 (1 ⚠) | 5 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.72× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 5 µM 0.148× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.185× (z -17.0) |
| [[RKO (line)]] | wt | 54.0 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0631× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.127× (z -13.8) |
| [[H4 (line)]] | wt | 44.8 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0873× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 54.0 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.156× (z -15.2) |
| [[MIA PaCa-2 (line)]] | alt | 49.8 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.156× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.190× (z -11.8) |
| [[SW48 (line)]] | wt | 62.3 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.139× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.140× (z -11.7) |
| [[HOP62 (line)]] | alt | 31.1 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.223× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.233× (z -11.6) |
| [[J82 (line)]] | alt | 32.7 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.145× (z -14.3) |
| [[A-172 (line)]] | wt | 31.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.159× (z -12.4) |
| [[C-33 A (line)]] | alt | 44.1 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.178× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 46.6 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.140× (z -12.1) |
| [[SNU-423 (line)]] | alt | 35.6 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.194× (z -10.9) |
| [[AN3 CA (line)]] | alt | 52.7 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.138× (z -9.0) |
| [[C32 (line)]] | wt | 28.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 81.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.232× (z -10.8) |
| [[HT-29 (line)]] | alt | 24.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0637× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -10.3) |
| [[SW1417 (line)]] | alt | 32.2 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.222× (z -11.0) |
| [[A549 (line)]] | wt | 54.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.286× (z -8.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 44.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[hTERT-HPNE (line)]] | wt | 22.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.151× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 37.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.329× (z -8.6) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.106× (z -8.8) ⚠ toxic |
| [[NCI-H661 (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0652× (z -8.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 54.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[SW 900 (line)]] | alt | 37.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.253× (z -8.6) ⚠ toxic |
| [[A498 (line)]] | wt | 4.43 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.71 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7368), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP41]] | +0.70 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[AFG1L]] | +0.68 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[SF3B3]] | +0.67 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[LDAH]] | +0.67 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[AASDHPPT]] | +0.66 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[ZNF252P-1]] | +0.66 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[MRPL24]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[NUBPL]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[PABIR1]] | +0.65 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[USP40]] | +0.65 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[DCLRE1A]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[C2CD5]] | +0.64 | +0.66 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM165]] | -0.67 | -0.68 / -0.66 | both halves | 7e-06 |  |
| [[TPTEP2-CSNK1E]] | -0.66 | -0.64 / -0.66 | both halves | 7e-06 |  |
| [[CCDC168]] | -0.62 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[GNRH1]] | -0.61 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[RABGEF1]] | -0.61 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[HIC2]] | -0.61 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[ZNF250]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[PPP1R32]] | -0.60 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[SDHAP4-1]] | -0.60 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[GET1-SH3BGR]] | -0.60 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[APTR]] | -0.60 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[MXD4]] | -0.59 | -0.53 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.631). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.3, 6.5); signed map (5.0, -37.7). **Vector** length 94.2, 27.8% of its response variance represented; |z| ≥ 3 in 1,044 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +8.0 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.2 | -0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | +0.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +6.1 | -3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.1 | -3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.1 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +0.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.0 | +2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +0.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -1.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.2 | -17.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.1 | -7.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -4.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | SLX4 interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.2 — chr20:10,435,305-10,636,829 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1099D15.3; previously C20orf94 |
| Matched by | ensembl_id |

UniProt [Q5VYV7](https://www.uniprot.org/uniprotkb/Q5VYV7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:16225](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16225) · Entrez [128710](https://www.ncbi.nlm.nih.gov/gene/128710) · UniProt [Q5VYV7](https://www.uniprot.org/uniprotkb/Q5VYV7) · Ensembl [ENSG00000149346](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149346)

## Data

Gene col 7368: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7368); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7368, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7368]; `tensor/DDL_lfc|DDL_z.npy` [7368]; `embed/gene_vectors.npy` [7368]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7368 or target_col == 7368). Every well: [[SLX4IP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLX4IP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
