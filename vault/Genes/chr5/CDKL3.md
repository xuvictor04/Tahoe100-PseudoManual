---
symbol: "CDKL3"
type: "gene"
col: 133
ensembl_id: "ENSG00000006837"
name: "cyclin dependent kinase like 3"
location: "5q31.1"
module: 23
arm: "+"
pooled_cpm: 30.42
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 8
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# CDKL3

*cyclin dependent kinase like 3* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.28× (z +26.3, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.603× (z -7.9, q 1e-12, down in 37 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.666× (z -6.4, q 4e-08, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (PANC-1 0.281×, HepG2/C3A 0.198×, C-33 A 0.264×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (HCT15 0.173×, A498 0.272×, hTERT-HPNE 0.138×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.243×, A-172 0.313×, PANC-1 0.415×; ⚠ toxic; cell-cycle shift, explains ~28% of this change); [[Canagliflozin (drug)]] 0.05 µM in 1 line (BT-474 0.101×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW48 0.109×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAS2R4]] (+0.80, fdr 7e-06), [[TBCE-1]] (+0.78, fdr 7e-06), [[CFAP53]] (+0.78, fdr 7e-06); moves opposite to [[METAP1]] (-0.65, fdr 2e-04), [[PARP1]] (-0.64, fdr 5e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZCWPW1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 133.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.28×** | +26.3 | 0e+00 | 46/48 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.31×** | +18.5 | 0e+00 | 42/47 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.32×** | +13.2 | 2e-37 | 44/48 (SK-MEL-2, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.28×** | +12.9 | 5e-36 | 39/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +9.6 | 8e-20 | 35/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.74×** | +8.7 | 3e-16 | 34/48 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +7.4 | 9e-12 | 36/46 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +7.4 | 1e-11 | 29/48 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +7.2 | 5e-11 | 25/42 (NCI-H460, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.33×** | +6.4 | 1e-08 | 30/48 (A498, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +6.1 | 6e-08 | 29/48 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +5.4 | 4e-06 | 31/48 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +5.3 | 6e-06 | 29/48 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.5 | 3e-04 | 21/48 (Panc 03.27, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 5e-04 | 23/48 (SW 1088, A-172, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.003 | 18/48 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.011 | 13/48 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.018 | 17/48 (AsPC-1, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 133.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (PANC-1 0.281×, HepG2/C3A 0.198×, C-33 A 0.264×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (HCT15 0.173×, A498 0.272×, hTERT-HPNE 0.138×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.243×, A-172 0.313×, PANC-1 0.415×; ⚠ toxic; cell-cycle shift, explains ~28% of this change); [[Canagliflozin (drug)]] 0.05 µM in 1 line (BT-474 0.101×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW48 0.109×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.603×** | -7.9 | 1e-12 | 37/48 (HT-29, Hs 766T, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.628×** | -7.0 | 7e-10 | 28/47 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.666×** | -6.4 | 4e-08 | 29/48 (HCT15, PANC-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.694×** | -5.7 | 1e-06 | 30/48 (A-427, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.694×** | -5.7 | 1e-06 | 28/48 (SW480, PANC-1, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.709×** | -5.4 | 8e-06 | 26/48 (PANC-1, SW480, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.717×** | -5.2 | 2e-05 | 28/48 (PANC-1, HepG2/C3A, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.805×** | -3.4 | 0.051 | 17/48 (PANC-1, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 133. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 39.2 | 2 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +12.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.260× (z -14.5) ⚠ cell-cycle shift, explains ~57% of this change |
| [[MIA PaCa-2 (line)]] | alt | 43.1 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +14.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.243× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 41.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +11.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.313× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 42.0 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +18.9) | — |
| [[NCI-H1573 (line)]] | alt | 59.3 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +18.6) | [[Digitoxin (drug)]] 5 µM 0.369× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[NCI-H460 (line)]] | wt | 27.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.94× (z +24.1) | — |
| [[A498 (line)]] | wt | 29.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 36.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.38× (z +18.5) | — |
| [[NCI-H1792 (line)]] | alt | 27.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +12.5) | — |
| [[NCI-H2030 (line)]] | alt | 24.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +18.8) | — |
| [[NCI-H2347 (line)]] | alt | 18.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +12.9) | — |
| [[SK-MEL-2 (line)]] | alt | 44.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +16.0) | — |
| [[BT-474 (line)]] | alt | 13.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +9.5) | [[Canagliflozin (drug)]] 0.05 µM 0.101× (z -10.6) |
| [[C-33 A (line)]] | alt | 51.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.219× (z -9.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 31.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.35× (z +15.7) | — |
| [[H4 (line)]] | wt | 29.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +9.8) | — |
| [[HCT15 (line)]] | alt | 47.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 32.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.198× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[HOP62 (line)]] | alt | 31.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +14.1) | — |
| [[Hs 766T (line)]] | wt | 27.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +12.6) | — |
| [[HS-578T (line)]] | alt | 30.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +12.2) | — |
| [[HT-29 (line)]] | alt | 26.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.27× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 25.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.138× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 19.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +13.9) | — |
| [[KATO III (line)]] | alt | 19.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +11.3) | — |
| [[LOX-IMVI (line)]] | wt | 15.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 36.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +16.9) | — |
| [[RKO (line)]] | wt | 27.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.83× (z +14.8) | — |
| [[RPMI-7951 (line)]] | alt | 35.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 23.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 32.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +14.0) | — |
| [[SW48 (line)]] | wt | 17.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +8.5) | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.109× (z -9.3) |
| [[A-427 (line)]] | wt | 56.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.65× (z +8.6) | — |
| [[A549 (line)]] | wt | 22.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.47× (z +14.7) | — |
| [[C32 (line)]] | wt | 35.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +12.0) | — |
| [[COLO 205 (line)]] | alt | 33.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 14.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.38× (z +12.6) | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.85× (z +14.6) | — |
| [[SHP-77 (line)]] | alt | 28.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 17.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.00× (z +11.8) | — |
| [[SW480 (line)]] | alt | 31.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +12.7) | — |
| [[AN3 CA (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 133), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAS2R4]] | +0.80 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[TBCE-1]] | +0.78 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[CFAP53]] | +0.78 | +0.79 / +0.62 | both halves | 7e-06 |  |
| [[HAVCR2]] | +0.77 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[ATE1OSP]] | +0.76 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[CHD1-DT]] | +0.76 | +0.79 / +0.57 | both halves | 9e-06 |  |
| [[THAP2]] | +0.76 | +0.80 / +0.52 | both halves | 1e-05 |  |
| [[LINC01004]] | +0.74 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[N4BP2L1]] | +0.74 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[ZCWPW2]] | +0.74 | +0.76 / +0.57 | both halves | 9e-06 |  |
| [[OXA1L-DT]] | +0.74 | +0.79 / +0.49 | both halves | 1e-05 |  |
| [[CELF6]] | +0.74 | +0.71 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METAP1]] | -0.65 | -0.77 / -0.31 | both halves | 2e-04 |  |
| [[PARP1]] | -0.64 | -0.51 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CDKL3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAGEA4-AS1]] | B | MAGEA4-AS1 activity raises CDKL3's level | lines that do not express MAGEA4-AS1 (41) vs lines expressing it (9) | 1.49× lower at baseline in the lines without MAGEA4-AS1 | 0.040 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |
| [[L3MBTL1]] | B | L3MBTL1 activity raises CDKL3's level | lines that do not express L3MBTL1 (7) vs lines expressing it (43) | 1.75× lower at baseline in the lines without L3MBTL1 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000277611, DNAJC18, COPZ2; maybe low, not absent |
| [[JAM3]] | B | JAM3 activity raises CDKL3's level | lines that do not express JAM3 (23) vs lines expressing it (27) | 1.39× lower at baseline in the lines without JAM3 | 0.088 | ⚠ within organs, on part of the lines; also absent: NPTX1, NOVA2, GDNF-AS1 |
| [[CAVIN4]] | C | CAVIN4 activity raises CDKL3's level | lines that do not express CAVIN4 (4) vs lines expressing it (46) | 2.00× lower at baseline in the lines without CAVIN4 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GPR135, SYCP2L, FAM229B; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZCWPW1]] | C | CDKL3's natural level strengthens ZCWPW1's drug response | CDKL3's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.70, reverse -0.14; direction not clear | 0.016 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.849). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (3.6, 16.9); signed map (25.6, -7.4). **Vector** length 99.9, 26.3% of its response variance represented; |z| ≥ 3 in 1,117 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.6 | +13.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +18.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +12.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +26.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.0 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +9.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +5.4 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +2.0 | +3.6 |
| fall | [[Belinostat (drug)]] 5 µM |  | -6.3 | +5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.2 | +6.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.9 | +8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | +0.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.8 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.5 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -6.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.0 | -0.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.9 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:134,286,350-134,371,047 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NKIAMRE |
| Gene groups (HGNC) | Cyclin dependent kinase like family |
| Matched by | ensembl_id |

UniProt [Q8IVW4](https://www.uniprot.org/uniprotkb/Q8IVW4) carries no function annotation.

**Summary**, from NCBI Gene [51265](https://www.ncbi.nlm.nih.gov/gene/51265):

> The protein encoded by this gene is a member of cyclin-dependent protein kinase (CDK) family. CDK family members are highly similar to the gene products of Saccharomyces cerevisiae cdc28, and Schizosaccharomyces pombe cdc2, and are known to be important regulators of cell cycle progression. This gene was identified as a gene absent in leukemic patients with chromosome 5q deletion. This loss may be an important determinant of dysmyelopoiesis. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:15483](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15483) · Entrez [51265](https://www.ncbi.nlm.nih.gov/gene/51265) · UniProt [Q8IVW4](https://www.uniprot.org/uniprotkb/Q8IVW4) · Ensembl [ENSG00000006837](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006837)

## Data

Gene col 133: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 133); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 133, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 133]; `tensor/DDL_lfc|DDL_z.npy` [133]; `embed/gene_vectors.npy` [133]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 133 or target_col == 133). Every well: [[CDKL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDKL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
