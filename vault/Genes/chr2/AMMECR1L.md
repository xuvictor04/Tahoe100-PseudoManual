---
symbol: "AMMECR1L"
type: "gene"
col: 6859
ensembl_id: "ENSG00000144233"
name: "AMMECR1 like"
location: "2q14.3"
module: 7
arm: "+"
pooled_cpm: 36.98
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 10
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# AMMECR1L

*AMMECR1 like* — 2q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.89× (z +13.4, q 2e-38, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.447× (z -15.2, q 0e+00, down in 42 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.822× (z -3.7, q 0.013, down in 14 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SW480 0.246×, LS 180 0.139×, AsPC-1 0.192×, NCI-H460 0.237×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A549 0.0729×, SW480 0.278×, RKO 0.178×, LOX-IMVI 0.266×, …; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.202×; ⚠ cell-cycle shift, explains ~27% of this change); [[Ipatasertib (drug)]] 0.5 µM in 1 line (SHP-77 0.0819×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.363×); [[Allantoin (drug)]] 0.5 µM in 1 line (CHP-212 0.114×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB45]] (+0.65, fdr 2e-05), [[ZNF746]] (+0.63, fdr 7e-06), [[YTHDF2]] (+0.59, fdr 4e-05); moves opposite to [[SPICE1]] (-0.56, fdr 3e-05), [[HSP90B1]] (-0.51, fdr 4e-04), [[PIK3C2A]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6859.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.89×** | +13.4 | 2e-38 | 46/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +11.4 | 1e-27 | 41/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +11.3 | 2e-27 | 33/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.04×** | +11.0 | 6e-26 | 40/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +9.6 | 1e-19 | 34/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.63×** | +9.3 | 2e-18 | 39/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +8.4 | 5e-15 | 34/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +8.0 | 1e-13 | 33/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +7.1 | 1e-10 | 29/48 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +6.0 | 9e-08 | 29/48 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +5.8 | 3e-07 | 27/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.36×** | +5.7 | 4e-07 | 31/47 (SW480, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +5.4 | 3e-06 | 26/48 (LoVo, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +5.3 | 5e-06 | 24/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.68×** | +5.1 | 1e-05 | 19/35 (SK-MEL-2, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.20× | +4.9 | 4e-05 | 19/48 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.30×** | +4.8 | 6e-05 | 23/47 (HT-29, RPMI-7951, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +4.1 | 1e-03 | 18/48 (PANC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +4.1 | 0.001 | 15/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6859.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SW480 0.246×, LS 180 0.139×, AsPC-1 0.192×, NCI-H460 0.237×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A549 0.0729×, SW480 0.278×, RKO 0.178×, LOX-IMVI 0.266×, …; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.202×; ⚠ cell-cycle shift, explains ~27% of this change); [[Ipatasertib (drug)]] 0.5 µM in 1 line (SHP-77 0.0819×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.363×); [[Allantoin (drug)]] 0.5 µM in 1 line (CHP-212 0.114×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.447×** | -15.2 | 0e+00 | 42/45 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.453×** | -14.4 | 1e-44 | 31/37 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.684×** | -7.2 | 1e-10 | 30/48 (HOP62, A498, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.767×** | -7.1 | 2e-10 | 34/48 (LOX-IMVI, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.707×** | -6.6 | 5e-09 | 34/48 (BT-474, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.740×** | -5.7 | 1e-06 | 28/48 (HepG2/C3A, A-172, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.772×** | -4.7 | 2e-04 | 21/47 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.774×** | -4.7 | 2e-04 | 19/48 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.822×** | -3.7 | 0.013 | 14/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.872× | -3.7 | 0.013 | 14/48 (NCI-H661, RKO, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.882× | -3.4 | 0.039 | 14/48 (CHP-212, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.826×** | -3.3 | 0.048 | 19/44 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 0.850× | -3.1 | 0.090 | 12/48 (AN3 CA, NCI-H23, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.05 µM |  | 0.852× | -3.0 | 0.095 | 8/48 (NCI-H23, NCI-H1573, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.894× | -3.0 | 0.095 | 13/48 (SNU-1, A-172, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.849× | -3.0 | 0.100 | 13/48 (RKO, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6859. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 41.9 | 6 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.07× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -16.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 36.7 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.364× (z -11.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 33.9 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +11.8) | — |
| [[LOX-IMVI (line)]] | wt | 55.9 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.65× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 43.9 | 4 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.70× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -13.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 56.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -15.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 44.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[A-427 (line)]] | wt | 35.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.99× (z +8.5) | — |
| [[AsPC-1 (line)]] | alt | 39.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -14.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 43.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -11.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 29.1 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.139× (z -15.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 49.7 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.70× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -9.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 43.6 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.363× (z -9.3) |
| [[A549 (line)]] | wt | 45.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0729× (z -26.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 32.8 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.114× (z -8.5) |
| [[H4 (line)]] | wt | 32.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -12.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 27.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -9.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 35.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -9.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 33.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -13.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 45.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 42.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -13.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[RPMI-7951 (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -8.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 25.3 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0819× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 38.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.34× (z +9.1) | — |
| [[A498 (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6859), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB45]] | +0.65 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[ZNF746]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[YTHDF2]] | +0.59 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[ZNF317]] | +0.57 | +0.36 / +0.55 | both halves | 1e-04 |  |
| [[FEM1B]] | +0.56 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[ZNF639]] | +0.56 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[DDX20]] | +0.56 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[URGCP]] | +0.55 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[ZBTB39]] | +0.55 | +0.37 / +0.63 | both halves | 9e-05 |  |
| [[RBM15B]] | +0.55 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[TMEM115]] | +0.54 | +0.36 / +0.53 | both halves | 1e-04 |  |
| [[HPS6]] | +0.54 | +0.36 / +0.47 | both halves | 1e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPICE1]] | -0.56 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[HSP90B1]] | -0.51 | -0.26 / -0.58 | both halves | 4e-04 |  |
| [[PIK3C2A]] | -0.49 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[PDIA4]] | -0.48 | -0.25 / -0.51 | both halves | 4e-04 |  |
| [[TPCN1]] | -0.47 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[TTC3]] | -0.47 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[LMAN1]] | -0.47 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[TMEM50B]] | -0.46 | -0.23 / -0.53 | both halves | 5e-04 |  |
| [[P4HA1]] | -0.45 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[BRWD3]] | -0.45 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[COPB2]] | -0.45 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[ADD3]] | -0.45 | -0.37 / -0.41 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises AMMECR1L's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ADD3]] | B | ADD3 activity lowers AMMECR1L's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.30× higher at baseline in the lines without ADD3 | 0.073 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |
| [[ZNF468]] | B | ZNF468 activity lowers AMMECR1L's level | lines that do not express ZNF468 (5) vs lines expressing it (45) | 1.37× higher at baseline in the lines without ZNF468 | 0.078 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF701, ZNF28, ZNF888 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises AMMECR1L's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises AMMECR1L's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.530). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-45.1, 5.0); signed map (-6.3, -24.9). **Vector** length 68.8, 13.9% of its response variance represented; |z| ≥ 3 in 1,110 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.1 | +4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +5.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.2 | +0.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +4.9 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.6 | -4.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.0 | -7.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -1.7 | -6.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.7 | -5.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.3 | +0.6 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.3 | +0.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | AMMECR1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.3 — chr2:127,861,630-127,885,967 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4268 |
| Matched by | ensembl_id |

UniProt [Q6DCA0](https://www.uniprot.org/uniprotkb/Q6DCA0) carries no function annotation.

**Summary**, from NCBI Gene [83607](https://www.ncbi.nlm.nih.gov/gene/83607):

> Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28658](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28658) · Entrez [83607](https://www.ncbi.nlm.nih.gov/gene/83607) · UniProt [Q6DCA0](https://www.uniprot.org/uniprotkb/Q6DCA0) · Ensembl [ENSG00000144233](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144233)

## Data

Gene col 6859: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6859); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6859, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6859]; `tensor/DDL_lfc|DDL_z.npy` [6859]; `embed/gene_vectors.npy` [6859]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6859 or target_col == 6859). Every well: [[AMMECR1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMMECR1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
