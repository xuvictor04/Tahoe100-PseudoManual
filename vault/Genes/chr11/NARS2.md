---
symbol: "NARS2"
type: "gene"
col: 6030
ensembl_id: "ENSG00000137513"
name: "asparaginyl-tRNA synthetase 2, mitochondrial"
location: "11q14.1"
module: 33
arm: "+"
pooled_cpm: 58.37
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# NARS2

*asparaginyl-tRNA synthetase 2, mitochondrial* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.33× (z +19.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.563× (z -12.5, q 4e-33, down in 32 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.597× (z -12.1, q 3e-31, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR3]] (+0.75, fdr 7e-06), [[ORC5]] (+0.74, fdr 7e-06), [[TAMM41]] (+0.73, fdr 7e-06); moves opposite to [[UBE2A]] (-0.61, fdr 1e-04), [[ATXN1L]] (-0.58, fdr 3e-05), [[MICALL2]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAM78B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6030.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.33×** | +19.9 | 0e+00 | 47/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.10×** | +17.4 | 0e+00 | 48/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.06×** | +17.1 | 0e+00 | 47/48 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +6.6 | 5e-09 | 29/48 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.71×** | +6.6 | 6e-09 | 34/48 (NCI-H2347, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.21×** | +6.3 | 3e-08 | 22/48 (NCI-H2347, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.58×** | +5.6 | 2e-06 | 29/48 (LoVo, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.26×** | +5.5 | 3e-06 | 26/48 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.22×** | +4.8 | 1e-04 | 18/48 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +4.6 | 3e-04 | 20/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +4.0 | 0.003 | 14/48 (NCI-H2347, A-172, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.18× | +3.9 | 0.004 | 13/48 (NCI-H2347, A-172, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.7 | 0.010 | 11/48 (A-172, LS 180, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.15× | +3.2 | 0.048 | 12/48 (NCI-H1573, NCI-H23, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.059 | 15/49 (KATO III, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.069 | 11/48 (A-427, AsPC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6030.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.563×** | -12.5 | 4e-33 | 32/45 (A-427, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.597×** | -12.1 | 3e-31 | 40/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.613×** | -11.5 | 2e-28 | 40/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.617×** | -11.3 | 1e-27 | 38/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.634×** | -10.7 | 1e-24 | 36/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.706×** | -8.2 | 2e-14 | 32/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.711×** | -7.7 | 1e-12 | 25/42 (Panc 03.27, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.728×** | -7.5 | 6e-12 | 33/48 (SW48, CHP-212, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.752×** | -6.7 | 1e-09 | 25/47 (NCI-H2030, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.764×** | -6.3 | 1e-08 | 26/48 (HEC-1-A, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.861× | -5.0 | 4e-05 | 22/48 (CHP-212, NCI-H2030, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **0.814×** | -4.8 | 7e-05 | 26/47 (PANC-1, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -4.6 | 1e-04 | 0/49 | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.811×** | -4.6 | 1e-04 | 21/48 (LoVo, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Raltitrexed (drug)]] 0.5 µM |  | 0.879× | -3.0 | 0.092 | 9/48 (SW 1271, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6030. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 120 | 2 | 10 (7 ⚠) | [[Panobinostat (drug)]] 5 µM 1.87× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -19.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.335× (z -17.5) |
| [[KATO III (line)]] | alt | 72.1 | 3 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.32× (z +9.8) | [[Digitoxin (drug)]] 5 µM 0.260× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.416× (z -10.2) |
| [[SW480 (line)]] | alt | 92.4 | 2 | 6 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.08× (z +10.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -20.0) |
| [[SW 900 (line)]] | alt | 52.4 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.02× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.331× (z -10.0) |
| [[A-172 (line)]] | wt | 37.5 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +14.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.50× (z +12.3) | — |
| [[NCI-H2030 (line)]] | alt | 81.6 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -20.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 45.9 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.296× (z -15.6) |
| [[SNU-423 (line)]] | alt | 51.3 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.65× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.359× (z -10.8) |
| [[A-427 (line)]] | wt | 97.1 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0924× (z -27.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 47.8 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.73× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.267× (z -12.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 65.8 | 0 | 4 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0670× (z -12.6) ⚠ toxic |
| [[HT-29 (line)]] | alt | 40.5 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.15× (z +10.8) | [[Auranofin (drug)]] 5 µM 0.405× (z -8.5) |
| [[J82 (line)]] | alt | 58.5 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.33× (z +9.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.426× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 73.0 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 103 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.47× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.414× (z -10.4) |
| [[SW1417 (line)]] | alt | 60.9 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +9.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.290× (z -12.8) |
| [[AsPC-1 (line)]] | alt | 22.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.42× (z +10.8) | — |
| [[C32 (line)]] | wt | 45.0 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.59× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.347× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 34.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.04× (z +12.6) | — |
| [[CHP-212 (line)]] | wt | 110 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -18.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 37.1 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.37× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.385× (z -9.5) |
| [[Hs 766T (line)]] | wt | 55.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.43× (z +11.3) | — |
| [[HS-578T (line)]] | alt | 42.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.32× (z +11.0) | — |
| [[LoVo (line)]] | wt | 61.0 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.29× (z +9.5) | [[Auranofin (drug)]] 5 µM 0.321× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 25.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.49× (z +13.3) | — |
| [[RKO (line)]] | wt | 62.0 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.228× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.364× (z -8.8) |
| [[BT-474 (line)]] | alt | 25.4 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.173× (z -11.8) |
| [[C-33 A (line)]] | alt | 142 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -15.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 47.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.92× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 23.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.15× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 72.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -18.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 59.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -22.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 76.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.199× (z -11.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 77.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -9.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 53.7 | 0 | 1 | — | [[Belzutifan (drug)]] 5 µM 0.0829× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 44.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.436× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 85.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.469× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 41.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.81× (z +9.2) | — |
| [[NCI-H661 (line)]] | alt | 77.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0654× (z -11.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -8.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 30.9 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.10× (z +8.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change | — |
| [[SW 1271 (line)]] | alt | 70.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -9.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 60.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -13.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6030), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR3]] | +0.75 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[ORC5]] | +0.74 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[TAMM41]] | +0.73 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.72 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[NPM3]] | +0.71 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[CLYBL]] | +0.70 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[RIOK1]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.70 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[EXOSC5]] | +0.70 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[NUFIP1]] | +0.69 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[FXN]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[NUBPL]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2A]] | -0.61 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[ATXN1L]] | -0.58 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[MICALL2]] | -0.57 | -0.47 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM78B]] | B | FAM78B activity raises NARS2's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.31× lower at baseline in the lines without FAM78B | 0.018 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[PSMB5]] | B | PSMB5 activity raises NARS2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.780). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.6, -42.7); signed map (-7.7, -50.4). **Vector** length 109, 29.8% of its response variance represented; |z| ≥ 3 in 1,164 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.54 to 8); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.59 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.59 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +5.5 | +5.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.6 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +4.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.1 | +17.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +3.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +1.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.6 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.6 | -12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.3 | -12.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.3 | -2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | asparaginyl-tRNA synthetase 2, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:78,435,620-78,575,194 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23441, SLM5; previously DFNB94 |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class II |
| Reactome | 3 pathways, smallest: Mitochondrial tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96I59](https://www.uniprot.org/uniprotkb/Q96I59) (Asparaginyl-tRNA synthetase):

> Mitochondrial aminoacyl-tRNA synthetase that catalyzes the specific attachment of the asparagine amino acid (aa) to the homologous transfer RNA (tRNA), further participating in protein synthesis. The reaction occurs in a two steps: asparagine is first activated by ATP to form Asn-AMP and then transferred to the acceptor end of tRNA(Asn) (Probable).

**Summary**, from NCBI Gene [79731](https://www.ncbi.nlm.nih.gov/gene/79731):

> This gene encodes a putative member of the class II family of aminoacyl-tRNA synthetases. These enzymes play a critical role in protein biosynthesis by charging tRNAs with their cognate amino acids. This protein is encoded by the nuclear genome but is likely to be imported to the mitochondrion where it is thought to catalyze the ligation of asparagine to tRNA molecules. Mutations in this gene have been associated with combined oxidative phosphorylation deficiency 24 (COXPD24). [provided by …

**Accessions** — [HGNC:26274](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26274) · Entrez [79731](https://www.ncbi.nlm.nih.gov/gene/79731) · UniProt [Q96I59](https://www.uniprot.org/uniprotkb/Q96I59) · Ensembl [ENSG00000137513](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137513)

## Data

Gene col 6030: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6030); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6030, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6030]; `tensor/DDL_lfc|DDL_z.npy` [6030]; `embed/gene_vectors.npy` [6030]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6030 or target_col == 6030). Every well: [[NARS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NARS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
