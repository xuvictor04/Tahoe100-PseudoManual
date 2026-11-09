---
symbol: "PCYOX1"
type: "gene"
col: 3750
ensembl_id: "ENSG00000116005"
name: "prenylcysteine oxidase 1"
location: "2p13.3"
module: 50
arm: "+"
pooled_cpm: 64.56
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 21
n_dd_up_clean: 10
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# PCYOX1

*prenylcysteine oxidase 1* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.67× (z +11.6, q 4e-28, up in 44 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.13× (z +8.9, q 1e-16, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.321× (z -18.9, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMED4]] (+0.76, fdr 7e-06), [[GRN]] (+0.75, fdr 7e-06), [[GM2A]] (+0.74, fdr 7e-06); moves opposite to [[GPATCH4]] (-0.59, fdr 3e-05), [[NSRP1]] (-0.59, fdr 2e-05), [[AFG3L1P]] (-0.57, fdr 2e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[P3H1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3750.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.67×** | +11.6 | 4e-28 | 44/48 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.35×** | +9.7 | 1e-19 | 36/40 (A-172, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.13×** | +8.9 | 1e-16 | 46/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.95×** | +7.8 | 6e-13 | 44/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +6.6 | 3e-09 | 35/48 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +5.9 | 2e-07 | 40/48 (SK-MEL-2, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.66×** | +5.9 | 2e-07 | 34/48 (PANC-1, A498, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.68×** | +5.7 | 1e-06 | 30/44 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.009 | 33/48 (A-172, J82, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.010 | 35/49 (KATO III, PANC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.020 | 28/48 (RKO, NCI-H23, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.36×** | +3.5 | 0.021 | 28/48 (SNU-423, A498, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.36×** | +3.5 | 0.021 | 25/49 (LS 180, A-427, …) | top dose only |  |
| [[Ixazomib (drug)]] 5 µM |  | **1.66×** | +3.1 | 0.072 | 25/48 (A-172, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.66×** | +3.1 | 0.072 | 24/47 (A498, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.095 | 20/48 (KATO III, A498, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3750.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.321×** | -18.9 | 0e+00 | 47/48 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.248×** | -15.8 | 0e+00 | 47/48 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.314×** | -13.6 | 5e-40 | 44/48 (H4, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.415×** | -10.3 | 6e-23 | 45/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.521×** | -7.7 | 2e-12 | 39/48 (NCI-H23, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.528×** | -7.5 | 5e-12 | 42/48 (NCI-H23, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.519×** | -7.4 | 1e-11 | 43/48 (hTERT-HPNE, SW 900, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.581×** | -6.4 | 1e-08 | 38/48 (LOX-IMVI, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.616×** | -5.7 | 7e-07 | 36/48 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.630×** | -5.4 | 3e-06 | 37/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.650×** | -5.1 | 2e-05 | 33/48 (HepG2/C3A, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.490×** | -4.4 | 5e-04 | 31/48 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.777×** | -4.2 | 0.001 | 32/49 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.721×** | -3.9 | 0.005 | 31/47 (HS-578T, A498, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.731×** | -3.7 | 0.008 | 26/48 (Hs 766T, SW 900, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.735×** | -3.6 | 0.010 | 25/48 (AN3 CA, NCI-H460, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.748×** | -3.4 | 0.021 | 26/48 (NCI-H460, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3750. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 70.3 | 2 (1 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -15.0) |
| [[NCI-H460 (line)]] | wt | 62.3 | 2 (2 ⚠) | 6 | [[Dinaciclib (drug)]] 5 µM 4.02× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -22.4) |
| [[A498 (line)]] | wt | 64.9 | 5 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -12.7) |
| [[A549 (line)]] | wt | 74.9 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +13.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -16.6) |
| [[PANC-1 (line)]] | alt | 43.6 | 3 (1 ⚠) | 4 | [[Panobinostat (drug)]] 0.5 µM 3.28× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -17.3) |
| [[SK-MEL-2 (line)]] | alt | 30.1 | 4 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 6.42× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 2.63× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -17.8) |
| [[A-172 (line)]] | wt | 105 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 4.81× (z +13.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -19.0) |
| [[A-427 (line)]] | wt | 102 | 0 | 6 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -19.5) |
| [[Hs 766T (line)]] | wt | 52.7 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -18.2) |
| [[SW 900 (line)]] | alt | 64.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -19.2) |
| [[HepG2_C3A (line)]] | wt | 102 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -16.6) |
| [[LS 180 (line)]] | wt | 64.0 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +11.2) | [[Harringtonine (drug)]] 5 µM 0.188× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 63.7 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -16.9) |
| [[RPMI-7951 (line)]] | alt | 58.9 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.155× (z -13.5) |
| [[SNU-423 (line)]] | alt | 72.7 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -15.6) |
| [[H4 (line)]] | wt | 57.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0399× (z -28.0) |
| [[HOP62 (line)]] | alt | 133 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -25.2) |
| [[HT-29 (line)]] | alt | 55.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -16.0) |
| [[hTERT-HPNE (line)]] | wt | 97.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -15.3) |
| [[NCI-H1792 (line)]] | alt | 67.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -12.8) |
| [[C32 (line)]] | wt | 46.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.67× (z +10.1) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 0.5 µM 0.263× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 60.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -17.3) |
| [[HS-578T (line)]] | alt | 54.9 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.296× (z -9.2) |
| [[KATO III (line)]] | alt | 80.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.30× (z +13.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 54.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -19.1) |
| [[Panc 03.27 (line)]] | alt | 74.0 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.201× (z -13.4) |
| [[RKO (line)]] | wt | 42.1 | 0 | 3 | — | [[Harringtonine (drug)]] 0.5 µM 0.135× (z -13.3) |
| [[SNU-1 (line)]] | wt | 56.3 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +8.8) | [[Harringtonine (drug)]] 5 µM 0.244× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 37.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.216× (z -10.3) |
| [[HCT15 (line)]] | alt | 95.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -17.6) |
| [[HEC-1-A (line)]] | alt | 78.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +10.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 36.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -12.5) |
| [[LoVo (line)]] | wt | 47.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.213× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 26.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 56.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -15.6) |
| [[SW48 (line)]] | wt | 72.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +9.3) | — |
| [[BT-474 (line)]] | alt | 44.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.253× (z -9.2) |
| [[C-33 A (line)]] | alt | 73.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 73.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.235× (z -10.8) |
| [[NCI-H661 (line)]] | alt | 110 | 0 | 1 | — | [[Peretinoin (drug)]] 5 µM 0.159× (z -9.1) |
| [[SHP-77 (line)]] | alt | 27.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 72.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.360× (z -8.8) |
| [[SW480 (line)]] | alt | 80.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.409× (z -8.9) |
| [[AN3 CA (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3750), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED4]] | +0.76 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[GRN]] | +0.75 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[GM2A]] | +0.74 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[LAMP2]] | +0.68 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[FAM210B]] | +0.67 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[GLG1]] | +0.66 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[CCNG1]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[RCN2]] | +0.64 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[MOSPD3]] | +0.63 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[MLEC]] | +0.63 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[BSG]] | +0.62 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[CD46]] | +0.62 | +0.54 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH4]] | -0.59 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[NSRP1]] | -0.59 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[AFG3L1P]] | -0.57 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[ZNF562]] | -0.57 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[EIF3J]] | -0.56 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[TP53RK]] | -0.55 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[GCFC2]] | -0.54 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[SHROOM1]] | -0.54 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[MRPS16]] | -0.54 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[TMA16]] | -0.53 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[RFFL]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[MRPS17]] | -0.53 | -0.43 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P3H1]] | C | P3H1 activity raises PCYOX1's level | lines that do not express P3H1 (4) vs lines expressing it (46) | 1.65× lower at baseline in the lines without P3H1 | 0.049 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CEP112, TIMP2, CNTNAP1; maybe low, not absent |
| [[CRTAP]] | C | CRTAP activity raises PCYOX1's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.71× lower at baseline in the lines without CRTAP | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.9, -19.3); signed map (-51.3, -8.1). **Vector** length 104, 38.5% of its response variance represented; |z| ≥ 3 in 1,254 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glycosphingolipid catabolism* (reactome, mean cos +0.53 to 5); *Glycosphingolipid metabolism* (reactome, mean cos +0.53 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.9 | +5.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.6 | +7.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.6 | +8.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.1 | +5.9 |
|  | [[NG25 (drug)]] 5 µM |  | +4.1 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +2.5 | +0.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.4 | +1.6 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.4 | +2.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.4 | +0.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -9.9 | -10.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.7 | -13.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.5 | -15.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.9 | -5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.7 | -18.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.7 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.4 | -3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.8 | -7.4 |

## What is on record

|  |  |
|---|---|
| Name | prenylcysteine oxidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:70,257,386-70,281,185 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0908, PCL1 |
| Gene groups (HGNC) | Flavoproteins; Prenylcysteine oxidase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHG3](https://www.uniprot.org/uniprotkb/Q9UHG3) (Prenylcysteine oxidase 1):

> Prenylcysteine oxidase that cleaves the thioether bond of prenyl-L-cysteines, such as farnesylcysteine and geranylgeranylcysteine. Only active against free prenylcysteines and not prenylcysteine residues within prenylated proteins or peptides (By similarity). Involved in the final step in the degradation of prenylated proteins, by degrading prenylcysteines after the protein has been degraded.

**Summary**, from NCBI Gene [51449](https://www.ncbi.nlm.nih.gov/gene/51449):

> Prenylcysteine is released during the degradation of prenylated proteins. PCYOX1 catalyzes the degradation of prenylcysteine to yield free cysteines and a hydrophobic isoprenoid product (Tschantz et al., 1999 [PubMed 10585463]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:20588](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20588) · Entrez [51449](https://www.ncbi.nlm.nih.gov/gene/51449) · UniProt [Q9UHG3](https://www.uniprot.org/uniprotkb/Q9UHG3) · Ensembl [ENSG00000116005](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116005)

## Data

Gene col 3750: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3750); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3750, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3750]; `tensor/DDL_lfc|DDL_z.npy` [3750]; `embed/gene_vectors.npy` [3750]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3750 or target_col == 3750). Every well: [[PCYOX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCYOX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
