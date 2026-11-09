---
symbol: "LRMDA"
type: "gene"
col: 7300
ensembl_id: "ENSG00000148655"
name: "leucine rich melanocyte differentiation associated"
location: "10q22.2-q22.3"
module: 121
arm: "+"
pooled_cpm: 127.03
n_lines_expressing: 29
n_dd_up: 22
n_dd_down: 33
n_dd_up_clean: 21
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# LRMDA

*leucine rich melanocyte differentiation associated* — 10q22.2-q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.72× (z +7.1, q 8e-10, up in 24 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.448× (z -10.9, q 5e-25, down in 24 of 27 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.541× (z -8.3, q 6e-15, down in 24 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOX5]] (+0.57, fdr 4e-05), [[ARNT2-DT]] (+0.56, fdr 4e-05), [[LINC01239]] (+0.56, fdr 2e-05); moves opposite to [[SWI5]] (-0.48, fdr 8e-05), [[SDHAP4-1]] (-0.42, fdr 2e-04), [[DIP2A]] (-0.42, fdr 3e-04).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LOXL4]] → it (grade B ⚠); 5 go from it, the strongest it → [[LINC01239]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7300.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.72×** | +7.1 | 8e-10 | 24/26 (HepG2/C3A, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +6.4 | 5e-08 | 11/27 (HT-29, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +5.4 | 1e-05 | 11/28 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.4 | 0.002 | 3/28 (LS 180, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.42×** | +4.2 | 0.003 | 21/26 (HepG2/C3A, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.37×** | +4.1 | 0.004 | 20/29 (HepG2/C3A, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.010 | 10/27 (HepG2/C3A, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.019 | 4/27 (A549, NCI-H460, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.021 | 11/27 (HepG2/C3A, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.029 | 15/27 (J82, HOP62, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.029 | 13/27 (HepG2/C3A, HOP62, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.029 | 11/27 (SW480, NCI-H2347, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.044 | 17/27 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.051 | 6/28 (HepG2/C3A, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.34×** | +3.2 | 0.051 | 9/28 (PANC-1, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.33×** | +3.2 | 0.051 | 6/27 (SW1417, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7300.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.448×** | -10.9 | 5e-25 | 24/27 (HepG2/C3A, A-427, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.458×** | -10.6 | 7e-24 | 24/27 (Panc 03.27, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.470×** | -10.3 | 2e-22 | 23/27 (HepG2/C3A, A-427, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.474×** | -10.2 | 4e-22 | 25/27 (SHP-77, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.483×** | -9.5 | 2e-19 | 24/26 (HepG2/C3A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.528×** | -8.7 | 4e-16 | 25/27 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.541×** | -8.3 | 6e-15 | 24/27 (Panc 03.27, A-427, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.344×** | -7.6 | 2e-12 | 25/28 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.583×** | -7.3 | 1e-11 | 24/27 (SW480, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.567×** | -6.8 | 8e-10 | 22/27 (HepG2/C3A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.392×** | -6.7 | 1e-09 | 23/27 (RKO, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.628×** | -6.3 | 1e-08 | 24/27 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.631×** | -6.3 | 2e-08 | 23/27 (SHP-77, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.622×** | -6.2 | 2e-08 | 20/27 (NCI-H1792, C32, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.639×** | -6.1 | 4e-08 | 24/27 (SW480, RKO, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.697×** | -4.7 | 9e-05 | 14/27 (HepG2/C3A, SW 900, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.518×** | -4.7 | 1e-04 | 22/27 (SHP-77, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.553×** | -4.2 | 8e-04 | 21/28 (Panc 03.27, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.748×** | -3.9 | 0.002 | 17/27 (COLO 205, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.821×** | -3.8 | 0.004 | 19/28 (COLO 205, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.737×** | -3.6 | 0.007 | 21/27 (HepG2/C3A, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.602×** | -3.6 | 0.007 | 15/27 (HOP62, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.741×** | -3.6 | 0.007 | 13/26 (HT-29, RKO, …) | two highest doses |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **0.832×** | -3.5 | 0.009 | 18/28 (SW480, C32, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7300. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 255 | 0 | 22 (17 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.123× (z -19.6) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.306× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 1,339 | 1 | 14 (10 ⚠) | [[Cobimetinib (drug)]] 5 µM 3.08× (z +10.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0928× (z -21.1) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.209× (z -12.7) |
| [[C32 (line)]] | wt | 635 | 0 | 14 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -27.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -16.0) |
| [[SHP-77 (line)]] | alt | 181 | 0 | 13 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.139× (z -20.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 452 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -21.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -14.0) |
| [[A-427 (line)]] | wt | 226 | 0 | 11 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.195× (z -15.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.319× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 438 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -22.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -12.1) |
| [[RKO (line)]] | wt | 364 | 0 | 10 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0939× (z -19.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -11.7) |
| [[NCI-H460 (line)]] | wt | 90.7 | 0 | 9 (9 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.208× (z -12.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[RPMI-7951 (line)]] | alt | 261 | 0 | 9 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.145× (z -14.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -12.6) |
| [[SW1417 (line)]] | alt | 114 | 0 | 9 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.260× (z -9.4) |
| [[J82 (line)]] | alt | 259 | 0 | 6 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.244× (z -11.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 229 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.153× (z -13.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 110 | 0 | 6 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.115× (z -15.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.126× (z -14.8) |
| [[SW 900 (line)]] | alt | 341 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -12.7) |
| [[LS 180 (line)]] | wt | 44.4 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.226× (z -10.0) |
| [[A549 (line)]] | wt | 118 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 33.4 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -9.9) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.323× (z -8.7) |
| [[HT-29 (line)]] | alt | 42.5 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.11× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 188 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.287× (z -9.4) ⚠ toxic |
| [[NCI-H661 (line)]] | alt | 190 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -11.2) |
| [[A-172 (line)]] | wt | 13.8 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 22.7 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.2 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 15.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 24.1 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 22.7 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.3 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 22.5 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.36 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.1 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.9 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 16.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7300), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOX5]] | +0.57 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[ARNT2-DT]] | +0.56 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[LINC01239]] | +0.56 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[L3MBTL4]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 | same gene group |
| [[EYA4]] | +0.56 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[POU6F2]] | +0.54 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[STK33]] | +0.52 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[FGF13]] | +0.52 | +0.45 / +0.47 | both halves | 3e-05 | same gene group |
| [[NPAS3]] | +0.52 | +0.47 / +0.49 | both halves | 2e-05 | STRING 406 |
| [[SOX6]] | +0.52 | +0.56 / +0.39 | both halves | 5e-05 | same gene group |
| [[LINC00383]] | +0.52 | +0.36 / +0.48 | both halves | 1e-04 |  |
| [[DMRTA1]] | +0.51 | +0.49 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SWI5]] | -0.48 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[SDHAP4-1]] | -0.42 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[DIP2A]] | -0.42 | -0.40 / -0.29 | both halves | 3e-04 |  |
| [[LINC01881]] | -0.40 | -0.35 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LOXL4]] | B | LOXL4 activity raises LRMDA's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 1.77× lower at baseline in the lines without LOXL4 | 0.072 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3 |
| [[MAP2K1]] | B | MAP2K1 activity lowers LRMDA's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SHROOM4]] | C | SHROOM4 activity raises LRMDA's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 3.09× lower at baseline in the lines without SHROOM4 | 0.022 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01239]] | B | LRMDA activity raises LINC01239's level | lines that do not express LRMDA (21) vs lines expressing it (29) | 2.21× lower at baseline in the lines without LRMDA | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, CCL28, SMIM10 |
| [[DMRTA1]] | B | LRMDA activity raises DMRTA1's level | lines that do not express LRMDA (21) vs lines expressing it (29) | 1.58× lower at baseline in the lines without LRMDA | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, CCL28, SMIM10 |
| [[DIP2A]] | B | LRMDA activity lowers DIP2A's level | lines that do not express LRMDA (21) vs lines expressing it (29) | 1.27× higher at baseline in the lines without LRMDA | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, CCL28, SMIM10 |
| [[THSD7A]] | C | LRMDA activity raises THSD7A's level | lines that do not express LRMDA (21) vs lines expressing it (29) | 2.41× lower at baseline in the lines without LRMDA | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, CCL28, SMIM10; co-absent with the target |
| [[SHROOM4]] | C | LRMDA activity raises SHROOM4's level | lines that do not express LRMDA (21) vs lines expressing it (29) | 2.17× lower at baseline in the lines without LRMDA | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, CCL28, SMIM10; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.526). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.9, 28.1); signed map (46.6, 26.5). **Vector** length 92.4, 27.4% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +10.0 | +1.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +9.5 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +6.5 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | -0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +7.1 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.3 | -8.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.1 | -10.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -6.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.8 | -8.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | -2.4 | -3.3 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -2.3 | -2.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.2 | -4.7 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -2.1 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich melanocyte differentiation associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2-q22.3 — chr10:75,431,624-76,560,168 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDA017, OCA7; previously C10orf11 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2I8](https://www.uniprot.org/uniprotkb/Q9H2I8) (Leucine-rich melanocyte differentiation-associated protein):

> Required for melanocyte differentiation.

**Summary**, from NCBI Gene [83938](https://www.ncbi.nlm.nih.gov/gene/83938):

> This gene encodes a leucine-rich repeat protein. The encoded protein is thought to play a role in melanocyte differentiation. Mutations in this gene have been associated with autosomal recessive oculocutaneous albinism 7 (OCA7). Alternatively spliced transcript variants have been identified. [provided by RefSeq, Mar 2015]

**Accessions** — [HGNC:23405](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23405) · Entrez [83938](https://www.ncbi.nlm.nih.gov/gene/83938) · UniProt [Q9H2I8](https://www.uniprot.org/uniprotkb/Q9H2I8) · Ensembl [ENSG00000148655](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148655)

## Data

Gene col 7300: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7300); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7300, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7300]; `tensor/DDL_lfc|DDL_z.npy` [7300]; `embed/gene_vectors.npy` [7300]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7300 or target_col == 7300). Every well: [[LRMDA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRMDA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
