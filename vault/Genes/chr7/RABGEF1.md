---
symbol: "RABGEF1"
type: "gene"
col: 7828
ensembl_id: "ENSG00000154710"
name: "RAB guanine nucleotide exchange factor 1"
location: "7q11.21"
module: 41
arm: "+"
pooled_cpm: 453.92
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 29
n_dd_up_clean: 4
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# RABGEF1

*RAB guanine nucleotide exchange factor 1* — 7q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +10.5, q 8e-23, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.453× (z -12.8, q 5e-35, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.549× (z -9.7, q 4e-20, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTLL3]] (+0.76, fdr 7e-06), [[PHKG1]] (+0.73, fdr 7e-06), [[QPCTL]] (+0.72, fdr 7e-06); moves opposite to [[DLD]] (-0.68, fdr 7e-06), [[AIFM1]] (-0.67, fdr 7e-06), [[ZNF221]] (-0.65, fdr 9e-06).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF221]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7828.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +10.5 | 8e-23 | 48/49 (Panc 03.27, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +5.1 | 9e-05 | 33/48 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.023 | 27/48 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.023 | 41/48 (SHP-77, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.3 | 0.10 | 19/49 (LS 180, MIA PaCa-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.21× | +3.2 | 0.14 | 23/48 (LS 180, CHP-212, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7828.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.453×** | -12.8 | 5e-35 | 43/44 (A-172, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.549×** | -10.1 | 2e-21 | 41/49 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.549×** | -9.7 | 4e-20 | 44/48 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.642×** | -6.9 | 6e-10 | 31/45 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.653×** | -6.9 | 6e-10 | 42/48 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.715×** | -5.7 | 2e-06 | 37/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.694×** | -5.5 | 2e-06 | 44/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.721×** | -5.5 | 2e-06 | 30/48 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.725×** | -5.4 | 4e-06 | 36/48 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.804×** | -5.1 | 2e-05 | 34/48 (LoVo, Hs 766T, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.752×** | -4.6 | 2e-04 | 34/47 (C32, H4, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.831×** | -4.4 | 6e-04 | 24/48 (AsPC-1, RKO, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.832×** | -4.3 | 7e-04 | 28/48 (LoVo, SW480, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.768×** | -4.1 | 0.002 | 34/48 (AsPC-1, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.781×** | -4.0 | 0.002 | 29/48 (AsPC-1, RKO, …) | all doses, flat |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.635×** | -4.0 | 0.002 | 36/49 (A-172, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.784×** | -3.9 | 0.003 | 27/47 (AsPC-1, SW48, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.795×** | -3.9 | 0.004 | 27/48 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.800×** | -3.8 | 0.005 | 29/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.819×** | -3.4 | 0.022 | 26/49 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.825×** | -3.2 | 0.029 | 23/47 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7828. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 731 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -22.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.209× (z -21.0) |
| [[A498 (line)]] | wt | 638 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -20.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.238× (z -17.6) |
| [[PANC-1 (line)]] | alt | 404 | 1 | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +14.4) | [[Harringtonine (drug)]] 5 µM 0.433× (z -13.4) |
| [[H4 (line)]] | wt | 773 | 1 (1 ⚠) | 5 (3 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.50× (z +9.3) ⚠ cell-cycle shift, explains ~15% of this change | [[Harringtonine (drug)]] 5 µM 0.236× (z -14.7) |
| [[HS-578T (line)]] | alt | 525 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.272× (z -16.8) |
| [[AsPC-1 (line)]] | alt | 1,217 | 0 | 5 (2 ⚠) | — | [[Radotinib (drug)]] 5 µM 0.537× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 429 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.420× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.509× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 359 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -14.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.390× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 321 | 1 | 4 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.12× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.398× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.500× (z -8.6) |
| [[SW480 (line)]] | alt | 479 | 3 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.48× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.501× (z -11.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 397 | 2 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -10.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 452 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -18.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 426 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.370× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.613× (z -9.8) |
| [[SW1417 (line)]] | alt | 371 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.56× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.449× (z -11.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 477 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.07× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.01× (z +8.9) | [[Selinexor (drug)]] 5 µM 0.555× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 210 | 0 | 3 | — | [[Harringtonine (drug)]] 0.5 µM 0.469× (z -10.9) |
| [[A549 (line)]] | wt | 319 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.555× (z -10.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.487× (z -8.7) |
| [[C32 (line)]] | wt | 319 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +8.6) | [[Harringtonine (drug)]] 5 µM 0.341× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 427 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -12.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 348 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.325× (z -14.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 392 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -12.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 474 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Radotinib (drug)]] 5 µM 0.630× (z -8.6) |
| [[COLO 205 (line)]] | alt | 236 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +12.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 452 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.348× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.380× (z -10.0) |
| [[HOP62 (line)]] | alt | 438 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -11.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 493 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.313× (z -13.1) |
| [[LS 180 (line)]] | wt | 251 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 287 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.457× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 296 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 395 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -12.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 574 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.395× (z -9.8) ⚠ transcription drop |
| [[AN3 CA (line)]] | alt | 422 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.438× (z -8.7) |
| [[C-33 A (line)]] | alt | 343 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +10.6) | — |
| [[LOX-IMVI (line)]] | wt | 423 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 722 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.658× (z -16.4) ⚠ position not correctable |
| [[NCI-H1573 (line)]] | alt | 517 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 740 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.398× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 237 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -9.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 279 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +15.6) | — |
| [[RPMI-7951 (line)]] | alt | 542 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -10.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 428 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.43× (z +9.3) | — |
| [[SW 1271 (line)]] | alt | 450 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -8.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 396 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 255 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 305 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 510 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 478 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 475 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 339 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 836 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7828), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTLL3]] | +0.76 | +0.63 / +0.79 | both halves | 7e-06 |  |
| [[PHKG1]] | +0.73 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[QPCTL]] | +0.72 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[SENP5]] | +0.71 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[TPTEP2-CSNK1E]] | +0.71 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[MYO9B]] | +0.71 | +0.71 / +0.81 | both halves | 7e-06 |  |
| [[TPT1-AS1]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[ZFC3H1]] | +0.68 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[SLC35E1]] | +0.67 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[BLZF1]] | +0.67 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[SPSB1]] | +0.67 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[STX5-DT]] | +0.66 | +0.48 / +0.69 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLD]] | -0.68 | -0.58 / -0.75 | both halves | 7e-06 |  |
| [[AIFM1]] | -0.67 | -0.67 / -0.66 | both halves | 7e-06 |  |
| [[ZNF221]] | -0.65 | -0.57 / -0.67 | both halves | 9e-06 |  |
| [[DHX9]] | -0.65 | -0.54 / -0.67 | both halves | 1e-05 |  |
| [[C2CD5]] | -0.64 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[NBN]] | -0.64 | -0.53 / -0.72 | both halves | 1e-05 |  |
| [[SMG7]] | -0.64 | -0.50 / -0.71 | both halves | 1e-05 |  |
| [[NHLRC2]] | -0.64 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[ZNF280D]] | -0.64 | -0.60 / -0.68 | both halves | 7e-06 |  |
| [[NELFCD]] | -0.64 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[TRUB1]] | -0.64 | -0.58 / -0.73 | both halves | 7e-06 |  |
| [[MBTPS2]] | -0.63 | -0.65 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF221]] | B | ZNF221 activity lowers RABGEF1's level | lines that do not express ZNF221 (5) vs lines expressing it (45) | 1.29× higher at baseline in the lines without ZNF221 | 0.075 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF540, ZNF529-AS1, AGK |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.458). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-16.6, -0.4); signed map (-17.3, 17.1). **Vector** length 170, 68.2% of its response variance represented; |z| ≥ 3 in 1,648 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +15.3 | +10.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.9 | +5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.0 | +1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +5.9 | +3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.9 | +3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.3 | +3.0 |
|  | [[Vilanterol (drug)]] 5 µM |  | +4.3 | +2.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -11.1 | -9.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -9.5 | -5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -7.1 | -6.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.0 | -5.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.5 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.5 | -4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.4 | -4.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -5.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | RAB guanine nucleotide exchange factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.21 — chr7:66,682,164-66,811,464 (+) |
| Ensembl biotype | protein_coding |
| Also known as | rabex-5, RABEX5 |
| Gene groups (HGNC) | VPS9 domain containing; Zinc fingers A20-type; Atypical E3 ubiquitin ligases |
| Reactome | 5 pathways, smallest: TBC/RABGAPs; RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJ41](https://www.uniprot.org/uniprotkb/Q9UJ41) (Rab5 GDP/GTP exchange factor):

> Acts as a guanine-nucleotide releasing factor (GEF) for RAB5A by promoting the conversion of inactive RAB-GDP to the active form RAB-GTP. Forms a complex with RABEP1 that acts as Rab4/Rab5 effector regulating endosome fusion. Involved in endocytic membrane fusion and membrane trafficking of recycling endosomes. Also functions as a ubiquitin ligase (By similarity).

**Summary**, from NCBI Gene [27342](https://www.ncbi.nlm.nih.gov/gene/27342):

> RABGEF1 forms a complex with rabaptin-5 (RABPT5; MIM 603616) that is required for endocytic membrane fusion, and it serves as a specific guanine nucleotide exchange factor (GEF) for RAB5 (RAB5A; MIM 179512) (Horiuchi et al., 1997 [PubMed 9323142]).[supplied by OMIM, Mar 2010]

**Accessions** — [HGNC:17676](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17676) · Entrez [27342](https://www.ncbi.nlm.nih.gov/gene/27342) · UniProt [Q9UJ41](https://www.uniprot.org/uniprotkb/Q9UJ41) · Ensembl [ENSG00000154710](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154710)

## Data

Gene col 7828: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7828); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7828, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7828]; `tensor/DDL_lfc|DDL_z.npy` [7828]; `embed/gene_vectors.npy` [7828]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7828 or target_col == 7828). Every well: [[RABGEF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RABGEF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
