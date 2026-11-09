---
symbol: "SRSF6"
type: "gene"
col: 4495
ensembl_id: "ENSG00000124193"
name: "serine and arginine rich splicing factor 6"
location: "20q13.11"
module: 96
arm: "+"
pooled_cpm: 87.48
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# SRSF6

*serine and arginine rich splicing factor 6* — 20q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.76× (z +29.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.399× (z -14.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SFPQ]] (+0.74, fdr 7e-06), [[ATXN7L2]] (+0.74, fdr 7e-06), [[CELSR3]] (+0.72, fdr 7e-06); moves opposite to [[HEBP1]] (-0.70, fdr 7e-06), [[COX6A1]] (-0.69, fdr 1e-05), [[PDCD10]] (-0.68, fdr 1e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4495.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.76×** | +29.9 | 0e+00 | 48/48 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.98×** | +17.5 | 0e+00 | 47/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.27×** | +12.6 | 4e-34 | 45/48 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.80×** | +9.4 | 9e-19 | 44/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +5.3 | 1e-05 | 31/48 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +5.3 | 1e-05 | 30/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +5.0 | 6e-05 | 28/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.9 | 8e-05 | 25/44 (PANC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +4.4 | 6e-04 | 29/48 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.34×** | +4.3 | 8e-04 | 31/45 (A-172, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.007 | 28/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.6 | 0.018 | 22/47 (RKO, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.24×** | +3.4 | 0.028 | 23/49 (A-172, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.050 | 24/49 (KATO III, HepG2/C3A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.2 | 0.050 | 24/47 (AsPC-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.055 | 20/48 (A-427, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.071 | 17/48 (KATO III, AsPC-1, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.093 | 19/48 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.42×** | +2.9 | 0.097 | 20/49 (NCI-H1573, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4495.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.399×** | -14.7 | 0e+00 | 47/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.577×** | -12.5 | 2e-33 | 45/49 (NCI-H23, RKO, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.502×** | -11.1 | 4e-26 | 46/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.513×** | -10.7 | 1e-24 | 45/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.548×** | -9.7 | 5e-20 | 44/48 (Panc 03.27, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.606×** | -7.7 | 9e-13 | 41/48 (NCI-H23, SNU-423, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.618×** | -7.7 | 9e-13 | 42/48 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.661×** | -6.4 | 1e-08 | 36/50 (NCI-H23, COLO 205, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.537×** | -5.2 | 1e-05 | 43/49 (PANC-1, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.811×** | -3.4 | 0.041 | 26/48 (LoVo, NCI-H1792, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.811×** | -3.2 | 0.060 | 23/47 (C32, H4, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | 0.829× | -3.0 | 0.12 | 20/48 (A-172, SW 1088, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4495. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 79.5 | 8 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +22.3) | [[Belinostat (drug)]] 5 µM 0.357× (z -10.9) |
| [[KATO III (line)]] | alt | 113 | 5 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +23.0) | [[Belinostat (drug)]] 5 µM 0.372× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 96.6 | 4 | 4 | [[Homoharringtonine (drug)]] 5 µM 7.80× (z +32.9) | [[Belinostat (drug)]] 5 µM 0.304× (z -13.4) |
| [[SW480 (line)]] | alt | 109 | 6 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +23.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 98.2 | 5 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +26.5) | [[Panobinostat (drug)]] 5 µM 0.403× (z -9.4) |
| [[PANC-1 (line)]] | alt | 73.3 | 3 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +20.2) | [[Belinostat (drug)]] 5 µM 0.349× (z -12.8) |
| [[COLO 205 (line)]] | alt | 114 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +23.4) | [[Belinostat (drug)]] 5 µM 0.328× (z -10.0) |
| [[HOP62 (line)]] | alt | 66.2 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +26.7) | [[Belinostat (drug)]] 5 µM 0.356× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 81.0 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +20.3) | [[Belinostat (drug)]] 5 µM 0.348× (z -10.2) |
| [[LS 180 (line)]] | wt | 70.9 | 4 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +17.8) | [[Belinostat (drug)]] 5 µM 0.363× (z -10.2) |
| [[A498 (line)]] | wt | 65.3 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +22.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 81.5 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +20.2) | [[Belinostat (drug)]] 5 µM 0.330× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 144 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +14.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -15.0) |
| [[Panc 03.27 (line)]] | alt | 72.1 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +19.4) | [[Belinostat (drug)]] 5 µM 0.407× (z -8.9) |
| [[SNU-423 (line)]] | alt | 89.3 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +22.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 69.7 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +18.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 69.9 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +18.6) | [[Belinostat (drug)]] 5 µM 0.274× (z -10.7) |
| [[LoVo (line)]] | wt | 79.0 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +22.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 127 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +12.1) | [[Belinostat (drug)]] 5 µM 0.298× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 69.9 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +13.4) | [[Belinostat (drug)]] 5 µM 0.400× (z -10.0) |
| [[SW 900 (line)]] | alt | 75.9 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +16.4) | [[Belinostat (drug)]] 5 µM 0.335× (z -9.9) |
| [[SW1417 (line)]] | alt | 148 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +21.1) | — |
| [[A-172 (line)]] | wt | 58.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +18.1) | — |
| [[C32 (line)]] | wt | 51.6 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.52× (z +20.7) | [[Belinostat (drug)]] 5 µM 0.278× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 107 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +15.7) | [[Belinostat (drug)]] 5 µM 0.332× (z -10.4) |
| [[H4 (line)]] | wt | 73.9 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +14.1) | [[Belinostat (drug)]] 5 µM 0.213× (z -11.3) |
| [[HCT15 (line)]] | alt | 106 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.3) | [[Belinostat (drug)]] 5 µM 0.278× (z -11.1) |
| [[HS-578T (line)]] | alt | 65.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +20.3) | — |
| [[HT-29 (line)]] | alt | 131 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +16.5) | [[Belinostat (drug)]] 5 µM 0.348× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 75.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +18.0) | — |
| [[RKO (line)]] | wt | 87.1 | 1 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 2.88× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -14.0) |
| [[RPMI-7951 (line)]] | alt | 112 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +19.0) | — |
| [[SK-MEL-2 (line)]] | alt | 66.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +22.6) | — |
| [[SNU-1 (line)]] | wt | 121 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -10.8) |
| [[SW48 (line)]] | wt | 65.5 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +12.3) | [[Belinostat (drug)]] 5 µM 0.234× (z -10.4) |
| [[A549 (line)]] | wt | 66.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 111 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +17.7) | — |
| [[Hs 766T (line)]] | wt | 112 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +19.9) | — |
| [[J82 (line)]] | alt | 101 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +18.4) | [[Belinostat (drug)]] 5 µM 0.422× (z -8.8) |
| [[SHP-77 (line)]] | alt | 56.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +11.5) | — |
| [[A-427 (line)]] | wt | 98.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.458× (z -8.5) |
| [[AN3 CA (line)]] | alt | 68.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.32× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 76.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -10.8) |
| [[SW 1088 (line)]] | alt | 101 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 81.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4495), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFPQ]] | +0.74 | +0.68 / +0.75 | both halves | 7e-06 | same gene group; STRING 694 |
| [[ATXN7L2]] | +0.74 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[CELSR3]] | +0.72 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[FKRP]] | +0.70 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[SRRM2]] | +0.70 | +0.64 / +0.61 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 599 |
| [[SRSF3]] | +0.69 | +0.66 / +0.69 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 991 |
| [[PIGO]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[PMF1]] | +0.69 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[CHTOP]] | +0.69 | +0.66 / +0.62 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 544 |
| [[SRSF1]] | +0.69 | +0.57 / +0.65 | both halves | 8e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 987 |
| [[EIF2B5]] | +0.68 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[MEPCE]] | +0.68 | +0.74 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEBP1]] | -0.70 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[COX6A1]] | -0.69 | -0.57 / -0.67 | both halves | 1e-05 |  |
| [[PDCD10]] | -0.68 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[ATOX1]] | -0.67 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[PLEKHA8]] | -0.65 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[BBLN]] | -0.64 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[HDAC3]] | -0.64 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[UBL5]] | -0.64 | -0.48 / -0.66 | both halves | 2e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[RNF149]] | -0.64 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[MTM1]] | -0.64 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[LAMTOR2]] | -0.64 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[KLHL7]] | -0.64 | -0.56 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SRSF6's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.787). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-3.3, -20.7); signed map (8.8, -35.9). **Vector** length 124, 41.6% of its response variance represented; |z| ≥ 3 in 1,084 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.8 | +29.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.2 | +17.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.2 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +5.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.1 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.3 | +1.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.9 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +0.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -12.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.8 | -7.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.4 | -14.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.9 | -9.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -7.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.9 | -5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.2 | -1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -2.4 |
|  | [[Neratinib (drug)]] 5 µM |  | -2.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | serine and arginine rich splicing factor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.11 — chr20:43,457,893-43,466,046 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SRP55, B52; previously SFRS6 |
| Gene groups (HGNC) | RNA binding motif containing; Serine and arginine rich splicing factors |
| Hallmark sets | DNA_REPAIR |
| Reactome | 12 pathways, smallest: mRNA Splicing - Minor Pathway; Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13247](https://www.uniprot.org/uniprotkb/Q13247) (Serine/arginine-rich splicing factor 6):

> Plays a role in constitutive splicing and modulates the selection of alternative splice sites. Plays a role in the alternative splicing of MAPT/Tau exon 10. Binds to alternative exons of TNC pre-mRNA and promotes the expression of alternatively spliced TNC. Plays a role in wound healing and in the regulation of keratinocyte differentiation and proliferation via its role in alternative splicing.

**Summary**, from NCBI Gene [6431](https://www.ncbi.nlm.nih.gov/gene/6431):

> The protein encoded by this gene is involved in mRNA splicing and may play a role in the determination of alternative splicing. The encoded nuclear protein belongs to the splicing factor SR family and has been shown to bind with and modulate another member of the family, SFRS12. Alternative splicing results in multiple transcript variants. In addition, two pseudogenes, one on chromosome 17 and the other on the X chromosome, have been found for this gene.[provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:10788](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10788) · Entrez [6431](https://www.ncbi.nlm.nih.gov/gene/6431) · UniProt [Q13247](https://www.uniprot.org/uniprotkb/Q13247) · Ensembl [ENSG00000124193](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124193)

## Data

Gene col 4495: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4495); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4495, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4495]; `tensor/DDL_lfc|DDL_z.npy` [4495]; `embed/gene_vectors.npy` [4495]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4495 or target_col == 4495). Every well: [[SRSF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRSF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
