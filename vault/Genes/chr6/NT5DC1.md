---
symbol: "NT5DC1"
type: "gene"
col: 10927
ensembl_id: "ENSG00000178425"
name: "5'-nucleotidase domain containing 1"
location: "6q22.1"
module: 160
arm: "-"
pooled_cpm: 65.81
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 30
n_dd_up_clean: 5
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# NT5DC1

*5'-nucleotidase domain containing 1* — 6q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.24× (z +6.6, q 2e-08, up in 26 of 48 measured lines) ⚠ cell-cycle shift, explains ~69% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.33× (z +6.2, q 2e-07, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.400× (z -19.6, q 0e+00, down in 41 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.448× (z -17.2, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUCLG2]] (+0.62, fdr 1e-05), [[SCCPDH]] (+0.59, fdr 1e-05), [[CISD2]] (+0.57, fdr 1e-05); moves opposite to [[RTN2]] (-0.61, fdr 1e-05), [[NECTIN2]] (-0.60, fdr 7e-06), [[NUMBL]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 160]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10927.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.24×** | +6.6 | 2e-08 | 26/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +6.2 | 2e-07 | 33/48 (A-172, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +5.6 | 4e-06 | 25/47 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.27×** | +5.1 | 6e-05 | 24/48 (A498, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.26×** | +4.9 | 1e-04 | 24/49 (COLO 205, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +4.4 | 0.001 | 17/48 (LoVo, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +4.2 | 0.003 | 22/48 (A-172, NCI-H1792, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.004 | 19/49 (A-172, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +3.9 | 0.007 | 20/42 (HT-29, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.19× | +3.8 | 0.009 | 14/49 (HOP62, A549, …) | two highest doses |  |
| [[Afatinib (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.021 | 16/49 (C-33 A, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.5 | 0.021 | 7/48 (SW480, SK-MEL-2, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +3.4 | 0.026 | 15/44 (A-427, A-172, …) | all doses, flat | composition shift |
| [[Amsacrine (drug)]] 5 µM |  | 1.11× | +3.3 | 0.038 | 8/48 (A498, hTERT-HPNE, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.17× | +3.3 | 0.038 | 18/48 (LS 180, A498, …) | top dose only |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.12× | +3.1 | 0.074 | 6/49 (C-33 A, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.080 | 15/47 (SW480, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10927.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.400×** | -19.6 | 0e+00 | 41/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.448×** | -17.2 | 0e+00 | 44/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.273×** | -14.5 | 1e-45 | 44/49 (PANC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.630×** | -14.0 | 3e-42 | 36/48 (NCI-H23, NCI-H460, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.312×** | -13.0 | 8e-37 | 43/48 (SK-MEL-2, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.554×** | -12.6 | 2e-34 | 40/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.565×** | -12.2 | 2e-32 | 41/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.619×** | -9.9 | 4e-21 | 35/47 (NCI-H23, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.654×** | -9.1 | 8e-18 | 30/48 (HT-29, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.667×** | -8.6 | 3e-16 | 32/48 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.696×** | -7.7 | 5e-13 | 35/48 (BT-474, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.789×** | -7.2 | 3e-11 | 27/49 (PANC-1, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.718×** | -7.1 | 6e-11 | 31/48 (LS 180, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.716×** | -6.9 | 2e-10 | 26/48 (NCI-H460, PANC-1, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.728×** | -6.8 | 5e-10 | 30/48 (PANC-1, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.750×** | -6.1 | 3e-08 | 31/48 (SNU-1, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.754×** | -6.0 | 6e-08 | 27/48 (LS 180, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.777×** | -5.4 | 2e-06 | 28/47 (NCI-H23, AN3 CA, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.837× | -5.4 | 2e-06 | 24/49 (RKO, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10927. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 126 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -18.5) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.280× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 76.1 | 0 | 14 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.210× (z -21.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.314× (z -15.8) |
| [[PANC-1 (line)]] | alt | 102 | 0 | 14 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.141× (z -28.4) |
| [[MIA PaCa-2 (line)]] | alt | 72.4 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -11.8) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.376× (z -10.5) |
| [[LS 180 (line)]] | wt | 94.1 | 1 (1 ⚠) | 8 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.5) ⚠ cell-cycle shift, explains ~5% of this change | [[Digitoxin (drug)]] 5 µM 0.278× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.291× (z -14.6) |
| [[SW480 (line)]] | alt | 102 | 0 | 9 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.298× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 90.1 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.236× (z -17.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.236× (z -9.1) |
| [[A549 (line)]] | wt | 76.5 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -12.7) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.620× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 82.8 | 0 | 6 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.171× (z -12.8) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.247× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 78.9 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -21.1) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.362× (z -11.0) |
| [[HT-29 (line)]] | alt | 77.6 | 0 | 5 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.373× (z -11.7) |
| [[LoVo (line)]] | wt | 65.1 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.384× (z -13.4) |
| [[SNU-423 (line)]] | alt | 96.7 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -16.9) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.389× (z -12.4) |
| [[HOP62 (line)]] | alt | 52.8 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.200× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.332× (z -12.5) |
| [[J82 (line)]] | alt | 58.3 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.255× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.423× (z -9.4) |
| [[KATO III (line)]] | alt | 93.8 | 0 | 4 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.153× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 48.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -14.3) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.342× (z -10.1) |
| [[SNU-1 (line)]] | wt | 63.6 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.232× (z -11.1) |
| [[AN3 CA (line)]] | alt | 60.6 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0818× (z -12.9) ⚠ toxic |
| [[C-33 A (line)]] | alt | 74.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.301× (z -10.3) |
| [[RKO (line)]] | wt | 51.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.229× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.321× (z -9.4) |
| [[SHP-77 (line)]] | alt | 45.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.229× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.344× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 82.9 | 0 | 3 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0503× (z -15.1) |
| [[A-427 (line)]] | wt | 72.5 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.133× (z -11.6) |
| [[HCT15 (line)]] | alt | 68.3 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.345× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 55.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -13.4) ⚠ cell-cycle shift, explains ~49% of this change |
| [[Panc 03.27 (line)]] | alt | 50.8 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.109× (z -11.0) |
| [[SW 900 (line)]] | alt | 46.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -9.4) ⚠ cell-cycle shift, explains ~49% of this change |
| [[A498 (line)]] | wt | 36.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -14.0) ⚠ cell-cycle shift, explains ~49% of this change |
| [[BT-474 (line)]] | alt | 89.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +19.1) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[COLO 205 (line)]] | alt | 55.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.354× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 75.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.324× (z -10.1) |
| [[SW 1271 (line)]] | alt | 84.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0516× (z -12.5) |
| [[A-172 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 65.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10927), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUCLG2]] | +0.62 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[SCCPDH]] | +0.59 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[CISD2]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[SLC35G1]] | +0.55 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[TMEM35B]] | +0.54 | +0.48 / +0.35 | both halves | 1e-04 |  |
| [[RAB11FIP2]] | +0.54 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[DOCK7]] | +0.54 | +0.43 / +0.38 | both halves | 6e-05 |  |
| [[ISOC1]] | +0.54 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[GCFC2]] | +0.54 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[MBTPS2]] | +0.53 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[ENOSF1]] | +0.52 | +0.52 / +0.39 | both halves | 5e-05 |  |
| [[LRRC58]] | +0.52 | +0.51 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTN2]] | -0.61 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[NECTIN2]] | -0.60 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[NUMBL]] | -0.60 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[HYAL1]] | -0.58 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[PLIN3]] | -0.57 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[GRIN2D]] | -0.56 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[RAB43]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[FBXL18]] | -0.55 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[CPLX1]] | -0.55 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[RASA4B]] | -0.54 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[TBC1D10B]] | -0.54 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[SLC25A42]] | -0.53 | -0.54 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **-** arm (projection on the module's main direction -0.632). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (7.8, 0.4); signed map (-14.9, -40.3). **Vector** length 86.0, 23.2% of its response variance represented; |z| ≥ 3 in 1,306 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +4.5 | +6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +6.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.4 | +1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.3 | +2.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.9 | -7.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.3 | -7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.6 | +3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.1 | -7.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -13.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.3 | -2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.2 | -1.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.9 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | 5'-nucleotidase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.1 — chr6:116,100,851-116,249,497 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ486I3.1, MGC24302; previously NT5C2L1 |
| Matched by | ensembl_id |

UniProt [Q5TFE4](https://www.uniprot.org/uniprotkb/Q5TFE4) carries no function annotation.

**Summary**, from NCBI Gene [221294](https://www.ncbi.nlm.nih.gov/gene/221294):

> While the exact function of the protein encoded by this gene is not known, it belongs to the 5'(3')-deoxyribonucleotidase family. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:21556](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21556) · Entrez [221294](https://www.ncbi.nlm.nih.gov/gene/221294) · UniProt [Q5TFE4](https://www.uniprot.org/uniprotkb/Q5TFE4) · Ensembl [ENSG00000178425](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178425)

## Data

Gene col 10927: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10927); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10927, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10927]; `tensor/DDL_lfc|DDL_z.npy` [10927]; `embed/gene_vectors.npy` [10927]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10927 or target_col == 10927). Every well: [[NT5DC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NT5DC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
