---
symbol: "YWHAQ"
type: "gene"
col: 5542
ensembl_id: "ENSG00000134308"
name: "tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein theta"
location: "2p25.1"
module: 20
arm: "+"
pooled_cpm: 183.34
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# YWHAQ

*tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein theta* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.23× (z +13.5, q 1e-38, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.81× (z +10.0, q 3e-21, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.730× (z -5.3, q 6e-05, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-427 0.413×, LS 180 0.408×, MIA PaCa-2 0.403×, C-33 A 0.465×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (MIA PaCa-2 0.401×, NCI-H1792 0.544×, RKO 0.549×, LS 180 0.557×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (SNU-1 0.137×, MIA PaCa-2 0.293×, A-427 0.431×, LS 180 0.398×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPK9]] (+0.69, fdr 7e-06), [[RBBP7]] (+0.68, fdr 7e-06), [[SPTBN1]] (+0.67, fdr 7e-06); moves opposite to [[TMEM258]] (-0.73, fdr 7e-06), [[NKAP]] (-0.73, fdr 7e-06), [[ALG2]] (-0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[L1CAM]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5542.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.23×** | +13.5 | 1e-38 | 47/49 (LoVo, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +12.4 | 1e-32 | 42/44 (LoVo, C32, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +11.5 | 2e-28 | 44/45 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.81×** | +10.0 | 3e-21 | 42/48 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.72×** | +9.1 | 8e-18 | 43/48 (HT-29, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.60×** | +8.4 | 5e-15 | 46/48 (SW480, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.53×** | +8.1 | 3e-14 | 47/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +8.1 | 4e-14 | 42/47 (NCI-H1792, LoVo, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +6.1 | 6e-08 | 37/48 (HT-29, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +5.4 | 3e-06 | 32/48 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.29×** | +4.2 | 0.001 | 28/48 (LoVo, NCI-H460, …) | rises with dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.7 | 0.009 | 19/38 (NCI-H2347, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.4 | 0.028 | 17/48 (RPMI-7951, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.23×** | +3.4 | 0.028 | 24/48 (NCI-H1573, LOX-IMVI, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.2 | 0.044 | 19/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5542.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-427 0.413×, LS 180 0.408×, MIA PaCa-2 0.403×, C-33 A 0.465×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (MIA PaCa-2 0.401×, NCI-H1792 0.544×, RKO 0.549×, LS 180 0.557×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (SNU-1 0.137×, MIA PaCa-2 0.293×, A-427 0.431×, LS 180 0.398×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.730×** | -5.3 | 6e-05 | 29/48 (SNU-1, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -4.2 | 0.007 | 24/48 (A-427, LS 180, …) | two highest doses | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.710×** | -4.1 | 0.007 | 34/48 (Hs 766T, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.864× | -3.5 | 0.064 | 22/49 (MIA PaCa-2, NCI-H1792, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.876× | -3.2 | 0.16 | 14/48 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.832× | -3.1 | 0.17 | 23/48 (Panc 03.27, HOP62, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 0.835× | -3.1 | 0.18 | 21/48 (NCI-H661, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5542. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 150 | 11 (7 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.87× (z +13.4) | — |
| [[NCI-H1573 (line)]] | alt | 83.7 | 8 (6 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.80× (z +10.9) | — |
| [[NCI-H1792 (line)]] | alt | 123 | 7 (6 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +14.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.26× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 98.0 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.81× (z +18.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.15× (z +12.7) | — |
| [[LS 180 (line)]] | wt | 124 | 4 (2 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.99× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.398× (z -10.0) |
| [[SW480 (line)]] | alt | 212 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 4.12× (z +9.9) | — |
| [[C32 (line)]] | wt | 47.3 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.36× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 6.83× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 94.5 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 4.65× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 282 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.40× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 99.7 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.49× (z +13.8) | — |
| [[KATO III (line)]] | alt | 129 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.21× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 100 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +12.4) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 183 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.19× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -15.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.431× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 152 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.30× (z +9.9) | — |
| [[COLO 205 (line)]] | alt | 81.4 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.58× (z +11.7) | — |
| [[HEC-1-A (line)]] | alt | 104 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.39× (z +10.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 222 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +11.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 409 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.293× (z -12.5) |
| [[RKO (line)]] | wt | 134 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +10.4) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.350× (z -10.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 101 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -17.0) |
| [[SW 900 (line)]] | alt | 157 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.78× (z +13.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 226 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +13.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 111 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.68× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 130 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +12.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 133 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +8.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 133 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 4.37× (z +9.0) | — |
| [[SK-MEL-2 (line)]] | alt | 166 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +8.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 205 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 419 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C-33 A (line)]] | alt | 166 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 179 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.47× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.588× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 162 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.81× (z +9.0) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 273 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 228 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 143 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 131 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 185 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 273 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 315 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 269 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 185 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5542), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK9]] | +0.69 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[RBBP7]] | +0.68 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[SPTBN1]] | +0.67 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[TCP1]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[RPSA]] | +0.66 | +0.62 / +0.67 | both halves | 7e-06 | pathway: SARS-CoV-1 Infection; STRING 599 |
| [[ARPP19]] | +0.66 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[DHFR]] | +0.64 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[API5]] | +0.64 | +0.46 / +0.70 | both halves | 3e-05 |  |
| [[GLO1]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[APP]] | +0.63 | +0.58 / +0.67 | both halves | 7e-06 | STRING 854 |
| [[CDC42]] | +0.63 | +0.53 / +0.70 | both halves | 1e-05 | pathway: RHO GTPase Effectors |
| [[FKBP9]] | +0.63 | +0.57 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM258]] | -0.73 | -0.58 / -0.81 | both halves | 7e-06 | pathway: SARS-CoV-2 Infection |
| [[NKAP]] | -0.73 | -0.67 / -0.77 | both halves | 7e-06 |  |
| [[ALG2]] | -0.71 | -0.67 / -0.72 | both halves | 7e-06 |  |
| [[MRPS18C]] | -0.71 | -0.68 / -0.70 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | -0.70 | -0.64 / -0.77 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[CROCCP2-1]] | -0.69 | -0.72 / -0.69 | both halves | 7e-06 |  |
| [[TERF2IP]] | -0.69 | -0.71 / -0.65 | both halves | 7e-06 |  |
| [[ZNF593]] | -0.68 | -0.53 / -0.75 | both halves | 1e-05 |  |
| [[ADPRM]] | -0.67 | -0.57 / -0.73 | both halves | 1e-05 |  |
| [[PDCD7]] | -0.66 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[SNHG9]] | -0.65 | -0.59 / -0.70 | both halves | 7e-06 |  |
| [[CCDC174]] | -0.65 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[KRTCAP2]] | -0.65 | -0.66 / -0.70 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[L1CAM]] | B | L1CAM activity raises YWHAQ's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 1.39× lower at baseline in the lines without L1CAM | 0.032 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |
| [[CRTAP]] | C | CRTAP activity raises YWHAQ's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.57× lower at baseline in the lines without CRTAP | 0.025 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.707). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.0, -11.7); signed map (-20.0, -36.7). **Vector** length 148, 52.1% of its response variance represented; |z| ≥ 3 in 1,228 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.3 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +13.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.0 | +9.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.9 | +10.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.6 | +8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +3.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.5 | +2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +4.1 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.2 | -5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.9 | -4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | -3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.9 | -4.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.9 | -2.8 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -3.8 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -1.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein theta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:9,583,967-9,630,997 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HS1, 14-3-3 |
| Gene groups (HGNC) | 14-3-3 phospho-serine/phospho-threonine binding proteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 29 pathways, smallest: Regulation of localization of FOXO transcription factors; SARS-CoV-2 targets host intracellular signalling and regulatory pathways; Chk1/Chk2(Cds1) mediated inactivation of Cyclin B:Cdk1 complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P27348](https://www.uniprot.org/uniprotkb/P27348) (14-3-3 protein theta):

> Adapter protein implicated in the regulation of a large spectrum of both general and specialized signaling pathways. Binds to a large number of partners, usually by recognition of a phosphoserine or phosphothreonine motif. Binding generally results in the modulation of the activity of the binding partner. Negatively regulates the kinase activity of PDPK1.

**Summary**, from NCBI Gene [10971](https://www.ncbi.nlm.nih.gov/gene/10971):

> This gene product belongs to the 14-3-3 family of proteins which mediate signal transduction by binding to phosphoserine-containing proteins. This highly conserved protein family is found in both plants and mammals, and this protein is 99% identical to the mouse and rat orthologs. This gene is upregulated in patients with amyotrophic lateral sclerosis. It contains in its 5' UTR a 6 bp tandem repeat sequence which is polymorphic, however, there is no correlation between the repeat number and the …

**Accessions** — [HGNC:12854](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12854) · Entrez [10971](https://www.ncbi.nlm.nih.gov/gene/10971) · UniProt [P27348](https://www.uniprot.org/uniprotkb/P27348) · Ensembl [ENSG00000134308](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134308)

## Data

Gene col 5542: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5542); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5542, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5542]; `tensor/DDL_lfc|DDL_z.npy` [5542]; `embed/gene_vectors.npy` [5542]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5542 or target_col == 5542). Every well: [[YWHAQ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YWHAQ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
