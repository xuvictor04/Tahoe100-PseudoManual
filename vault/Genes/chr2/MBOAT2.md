---
symbol: "MBOAT2"
type: "gene"
col: 6805
ensembl_id: "ENSG00000143797"
name: "membrane bound glycerophospholipid O-acyltransferase 2"
location: "2p25.1"
module: 30
arm: "+"
pooled_cpm: 173.56
n_lines_expressing: 47
n_dd_up: 17
n_dd_down: 25
n_dd_up_clean: 15
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# MBOAT2

*membrane bound glycerophospholipid O-acyltransferase 2* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.92× (z +13.2, q 3e-37, up in 39 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.447× (z -23.1, q 0e+00, down in 37 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAPSS1]] (+0.64, fdr 1e-05), [[ANXA6]] (+0.64, fdr 2e-05), [[ATP13A2]] (+0.64, fdr 3e-05); moves opposite to [[LATS1]] (-0.67, fdr 2e-05), [[ERCC6L2]] (-0.65, fdr 3e-05), [[UNK]] (-0.65, fdr 3e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[IRF6]] → it (grade B ⚠); 3 go from it, the strongest it → [[PTCHD4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6805.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.92×** | +13.2 | 3e-37 | 39/45 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.83×** | +12.3 | 3e-32 | 37/45 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.64×** | +10.1 | 1e-21 | 37/45 (SW480, KATO III, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +9.9 | 7e-21 | 32/45 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.59×** | +9.5 | 2e-19 | 36/45 (KATO III, SW480, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +9.4 | 5e-19 | 28/45 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +8.2 | 2e-14 | 32/45 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.06×** | +7.7 | 1e-12 | 36/46 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +7.0 | 1e-10 | 37/45 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +6.9 | 2e-10 | 30/45 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +6.2 | 3e-08 | 25/45 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +5.3 | 5e-06 | 26/42 (A498, J82, …) | all doses, flat | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +5.1 | 1e-05 | 23/46 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.42×** | +4.9 | 4e-05 | 28/46 (SW480, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +4.7 | 9e-05 | 23/44 (hTERT-HPNE, SW48, …) | two highest doses | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.042 | 17/45 (SW480, Hs 766T, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6805.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.447×** | -23.1 | 0e+00 | 37/45 (HS-578T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.442×** | -16.6 | 0e+00 | 36/45 (SW48, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.566×** | -16.3 | 0e+00 | 37/46 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.511×** | -13.6 | 3e-40 | 34/45 (A549, SNU-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.570×** | -11.4 | 4e-28 | 35/45 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.571×** | -11.4 | 6e-28 | 35/45 (LOX-IMVI, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.621×** | -9.7 | 3e-20 | 32/45 (A549, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.721×** | -9.4 | 4e-19 | 31/45 (A549, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.630×** | -9.4 | 4e-19 | 33/45 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.622×** | -9.2 | 1e-18 | 28/45 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.643×** | -8.6 | 4e-16 | 33/44 (SNU-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.653×** | -8.3 | 5e-15 | 29/45 (HS-578T, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.689×** | -7.6 | 2e-12 | 27/45 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.530×** | -6.7 | 7e-10 | 28/46 (HEC-1-A, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **0.727×** | -6.5 | 4e-09 | 28/45 (NCI-H2347, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.729×** | -6.2 | 3e-08 | 32/47 (HS-578T, SW48, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.768×** | -5.0 | 1e-05 | 25/44 (A-172, SW48, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.786×** | -4.9 | 3e-05 | 26/45 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.774×** | -4.8 | 5e-05 | 25/44 (A549, RKO, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6805. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 1,141 | 0 | 21 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -23.8) |
| [[H4 (line)]] | wt | 78.3 | 16 (1 ⚠) | 1 | [[Budesonide (drug)]] 0.05 µM 6.13× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -11.0) |
| [[HS-578T (line)]] | alt | 242 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -24.5) |
| [[SHP-77 (line)]] | alt | 167 | 12 | 0 | [[Dexamethasone (drug)]] 5 µM 3.18× (z +10.9) | — |
| [[A549 (line)]] | wt | 129 | 0 | 11 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -19.8) |
| [[LS 180 (line)]] | wt | 92.9 | 8 (1 ⚠) | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.30× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -14.3) |
| [[LoVo (line)]] | wt | 145 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -23.3) |
| [[NCI-H460 (line)]] | wt | 52.2 | 7 (1 ⚠) | 3 | [[Panobinostat (drug)]] 0.5 µM 3.69× (z +14.6) | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -15.7) |
| [[HOP62 (line)]] | alt | 138 | 2 (1 ⚠) | 7 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.60× (z +10.7) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.19× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -22.1) |
| [[LOX-IMVI (line)]] | wt | 147 | 2 | 7 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.37× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -16.3) |
| [[CFPAC-1 (line)]] | alt | 286 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -15.8) |
| [[HEC-1-A (line)]] | alt | 107 | 0 | 8 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -20.0) |
| [[KATO III (line)]] | alt | 165 | 3 | 5 | [[Ixazomib citrate (drug)]] 0.5 µM 3.67× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 87.5 | 5 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.82× (z +17.7) | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -13.7) |
| [[NCI-H2347 (line)]] | alt | 639 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -17.2) |
| [[A498 (line)]] | wt | 82.2 | 5 | 2 | [[Panobinostat (drug)]] 5 µM 3.30× (z +15.4) | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -11.4) |
| [[COLO 205 (line)]] | alt | 258 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.67× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -14.2) |
| [[SW48 (line)]] | wt | 395 | 1 | 5 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.11× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -20.0) |
| [[SW480 (line)]] | alt | 183 | 5 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.65× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 94.7 | 2 | 3 | [[Belinostat (drug)]] 5 µM 2.44× (z +8.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.278× (z -12.2) |
| [[A-172 (line)]] | wt | 219 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -18.8) |
| [[MIA PaCa-2 (line)]] | alt | 67.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.228× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 166 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -23.5) |
| [[NCI-H23 (line)]] | alt | 62.5 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.257× (z -12.4) |
| [[RKO (line)]] | wt | 80.6 | 3 | 1 | [[Belinostat (drug)]] 5 µM 3.26× (z +11.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.402× (z -9.0) |
| [[HCT15 (line)]] | alt | 86.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -12.6) |
| [[hTERT-HPNE (line)]] | wt | 96.0 | 2 (1 ⚠) | 1 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.41× (z +10.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -10.7) |
| [[J82 (line)]] | alt | 121 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -17.9) |
| [[NCI-H1792 (line)]] | alt | 153 | 1 | 2 | [[Belinostat (drug)]] 5 µM 2.40× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -18.2) |
| [[PANC-1 (line)]] | alt | 77.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.72× (z +17.0) | — |
| [[SK-MEL-2 (line)]] | alt | 94.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -19.5) |
| [[SW 900 (line)]] | alt | 126 | 2 | 1 | [[Belinostat (drug)]] 5 µM 2.50× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -10.2) |
| [[A-427 (line)]] | wt | 190 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.563× (z -10.7) |
| [[Hs 766T (line)]] | wt | 252 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -17.3) |
| [[SNU-1 (line)]] | wt | 103 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.201× (z -14.5) |
| [[SNU-423 (line)]] | alt | 69.5 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.02× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -10.7) |
| [[SW1417 (line)]] | alt | 169 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.69× (z +10.9) | — |
| [[AN3 CA (line)]] | alt | 162 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -11.5) |
| [[BT-474 (line)]] | alt | 177 | 1 | 0 | [[Neratinib (maleate) (drug)]] 5 µM 2.01× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 341 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -9.8) |
| [[C-33 A (line)]] | alt | 145 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.2 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 20.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 115 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6805), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAPSS1]] | +0.64 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[ANXA6]] | +0.64 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[ATP13A2]] | +0.64 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[PPP2R2C]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[OSTF1]] | +0.63 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[FLNB]] | +0.63 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[USP35]] | +0.62 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[STAM]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[NTAN1]] | +0.62 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[FNBP1L]] | +0.62 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[RIMS3]] | +0.62 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[PIP4K2A]] | +0.61 | +0.65 / +0.42 | both halves | 4e-05 | pathway: Phospholipid metabolism |

## Genes that move opposite

*40 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LATS1]] | -0.67 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[ERCC6L2]] | -0.65 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[UNK]] | -0.65 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[ASH1L]] | -0.64 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[ZCCHC3]] | -0.63 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[ANKRD17-DT]] | -0.61 | -0.67 / -0.28 | both halves | 3e-04 |  |
| [[NFYC]] | -0.61 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[CREBBP]] | -0.61 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[HELQ]] | -0.60 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[ZBED5]] | -0.60 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[ZNF764]] | -0.60 | -0.56 / -0.36 | both halves | 9e-05 |  |
| [[LINC01004]] | -0.60 | -0.61 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRF6]] | B | IRF6 activity raises MBOAT2's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 1.87× lower at baseline in the lines without IRF6 | 0.025 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[TOP2A]] | B | TOP2A activity raises MBOAT2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PLEKHH2]] | B | PLEKHH2 activity lowers MBOAT2's level | lines that do not express PLEKHH2 (14) vs lines expressing it (36) | 1.62× higher at baseline in the lines without PLEKHH2 | 0.036 | ⚠ within organs, on part of the lines; also absent: PDLIM3, ENSG00000259363, AKT3 |
| [[CDA]] | B | CDA activity raises MBOAT2's level | lines that do not express CDA (16) vs lines expressing it (34) | 1.61× lower at baseline in the lines without CDA | 0.045 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |
| [[IRF6]] | B | IRF6 activity weakens MBOAT2's drug response | lines that do not express IRF6 (29) vs lines expressing it (17) | the lines without IRF6 respond 1.14× as strongly (z diff -0.86); strongest at Panobinostat 5 µM: 2.03x vs 1.34x (z diff -3.4) | 0.090 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; target measured in part of the lines; artifact flags |
| [[TSPAN33]] | B | TSPAN33 activity lowers MBOAT2's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.65× higher at baseline in the lines without TSPAN33 | 0.091 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[WARS2-AS1]] | C | WARS2-AS1 activity lowers MBOAT2's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 4.58× higher at baseline in the lines without WARS2-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTCHD4]] | C | MBOAT2 activity lowers PTCHD4's level | lines that do not express MBOAT2 (3) vs lines expressing it (47) | 9.42× higher at baseline in the lines without MBOAT2 | 0.068 | ⚠ few lines (3 vs 47); across organs; also absent: ZXDA, TMEM132A, IL27RA |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | MBOAT2's natural level raises the cells' numbers under Fluvoxamine 0.5 µM (protects the cells) | MBOAT2's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.65 | 0.409 over the table, 0.052 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | MBOAT2's natural level raises the cells' numbers under Bendamustine 0.5 µM (protects the cells) | MBOAT2's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.63 | 0.460 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.519). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.9, 7.0); signed map (-19.1, 29.9). **Vector** length 151, 51.5% of its response variance represented; |z| ≥ 3 in 1,889 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +10.9 | +13.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +9.2 | +12.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +9.2 | +8.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.0 | +9.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +9.0 | +9.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.6 | +10.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +7.5 | +7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +6.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.4 | +4.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.6 | -16.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -9.6 | -9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.4 | -16.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.0 | -23.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.9 | -8.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.5 | -9.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -3.8 | -2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.2 | -5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | membrane bound glycerophospholipid O-acyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:8,852,690-9,003,709 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14415, FLJ90298, LPLAT13; previously OACT2 |
| Gene groups (HGNC) | Membrane bound O-acyltransferase family; Lysophospholipid acyltransferases |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 5 pathways, smallest: Acyl chain remodelling of PC; Acyl chain remodelling of PE; Glycerophospholipid biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZWT7](https://www.uniprot.org/uniprotkb/Q6ZWT7) (Membrane-bound glycerophospholipid O-acyltransferase 2):

> Acyltransferase which catalyzes the transfer of an acyl group from an acyl-CoA to a lysophospholipid leading to the production of a phospholipid and participates in the reacylation step of the phospholipid remodeling pathway also known as the Lands cycle. Catalyzes preferentially the acylation of lysophosphatidylethanolamine (1-acyl-sn-glycero-3-phosphoethanolamine or LPE) and lysophosphatidic acid (LPA) and to a lesser extend lysophosphatidylcholine (LPC) and lysophosphatidylserine (LPS). …

**Summary**, from NCBI Gene [129642](https://www.ncbi.nlm.nih.gov/gene/129642):

> Enables 1-acylglycerophosphocholine O-acyltransferase activity; 1-acylglycerophosphoethanolamine O-acyltransferase activity; and 1-acylglycerophosphoserine O-acyltransferase activity. Involved in phosphatidylcholine acyl-chain remodeling; phosphatidylethanolamine acyl-chain remodeling; and phosphatidylserine acyl-chain remodeling. Predicted to be located in endoplasmic reticulum membrane. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25193](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25193) · Entrez [129642](https://www.ncbi.nlm.nih.gov/gene/129642) · UniProt [Q6ZWT7](https://www.uniprot.org/uniprotkb/Q6ZWT7) · Ensembl [ENSG00000143797](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143797)

## Data

Gene col 6805: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6805); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6805, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6805]; `tensor/DDL_lfc|DDL_z.npy` [6805]; `embed/gene_vectors.npy` [6805]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6805 or target_col == 6805). Every well: [[MBOAT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MBOAT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
