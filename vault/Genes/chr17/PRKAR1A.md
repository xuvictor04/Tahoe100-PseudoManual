---
symbol: "PRKAR1A"
type: "gene"
col: 3011
ensembl_id: "ENSG00000108946"
name: "protein kinase cAMP-dependent type I regulatory subunit alpha"
location: "17q24.2"
module: 3
arm: "-"
pooled_cpm: 150.15
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 9
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PRKAR1A

*protein kinase cAMP-dependent type I regulatory subunit alpha* — 17q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.35× (z +16.0, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.65× (z +9.3, q 1e-18, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.698× (z -6.7, q 1e-08, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERLIN2]] (+0.73, fdr 7e-06), [[EIF4G2]] (+0.73, fdr 1e-05), [[ELK4]] (+0.70, fdr 1e-05); moves opposite to [[POP7]] (-0.68, fdr 6e-05), [[USP42]] (-0.68, fdr 1e-05), [[TSEN54]] (-0.65, fdr 3e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3011.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.35×** | +16.0 | 0e+00 | 48/49 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.35×** | +15.4 | 0e+00 | 44/44 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +11.7 | 3e-29 | 40/45 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +9.3 | 1e-18 | 43/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +8.6 | 7e-16 | 33/48 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +7.9 | 3e-13 | 38/48 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +7.4 | 1e-11 | 39/48 (HOP62, BT-474, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +6.7 | 1e-09 | 42/48 (SK-MEL-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +6.2 | 4e-08 | 42/48 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +6.1 | 5e-08 | 28/49 (SW1417, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +5.6 | 1e-06 | 30/48 (LoVo, LS 180, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +4.9 | 5e-05 | 31/48 (HOP62, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.5 | 3e-04 | 28/48 (MIA PaCa-2, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.4 | 4e-04 | 27/50 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.8 | 0.006 | 18/48 (MIA PaCa-2, CFPAC-1, …) | top dose only | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.6 | 0.009 | 11/48 (SW1417, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.23×** | +3.6 | 0.009 | 25/47 (A549, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3011.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.698×** | -6.7 | 1e-08 | 40/48 (LOX-IMVI, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.720×** | -6.1 | 3e-07 | 36/48 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.738×** | -5.7 | 2e-06 | 33/48 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.775×** | -4.8 | 3e-04 | 36/48 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.782×** | -4.6 | 5e-04 | 33/48 (SW 900, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.777×** | -4.4 | 8e-04 | 31/48 (SW 900, NCI-H460, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.812×** | -3.9 | 0.008 | 27/48 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.720×** | -3.2 | 0.089 | 25/48 (NCI-H460, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.780×** | -3.2 | 0.089 | 24/48 (SHP-77, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | 0.848× | -3.1 | 0.12 | 20/48 (NCI-H661, AN3 CA, …) | two highest doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.892× | -3.0 | 0.13 | 11/48 (A-427, NCI-H2030, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3011. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 155 | 6 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +16.0) | [[Belinostat (drug)]] 5 µM 0.488× (z -9.3) |
| [[HOP62 (line)]] | alt | 216 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.01× (z +13.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.9) | — |
| [[LoVo (line)]] | wt | 69.9 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +16.9) | — |
| [[LS 180 (line)]] | wt | 116 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +10.9) | — |
| [[A549 (line)]] | wt | 180 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +13.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.505× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 85.3 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +15.7) | [[Panobinostat (drug)]] 5 µM 0.491× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 213 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +16.8) | — |
| [[A-172 (line)]] | wt | 154 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 221 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.60× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.57× (z +10.4) | — |
| [[HS-578T (line)]] | alt | 127 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 117 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.40× (z +15.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 194 | 2 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.424× (z -9.9) |
| [[PANC-1 (line)]] | alt | 87.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.62× (z +18.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 103 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +10.6) | — |
| [[A498 (line)]] | wt | 147 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +13.1) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 103 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +10.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 96.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +9.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 97.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +14.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 128 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 165 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +13.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 231 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.40× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 129 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +13.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 154 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.46× (z +11.1) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 93.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +12.1) | — |
| [[CFPAC-1 (line)]] | alt | 131 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 188 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.86× (z +11.3) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 114 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.52× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 168 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +10.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 130 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +10.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.239× (z -15.2) ⚠ toxic; cell-cycle shift, explains ~96% of this change |
| [[SW 900 (line)]] | alt | 241 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.92× (z +8.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.514× (z -8.7) |
| [[SW480 (line)]] | alt | 148 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +11.4) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 152 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +12.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 251 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +10.2) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 89.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +14.8) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 166 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +8.6) | — |
| [[KATO III (line)]] | alt | 131 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +8.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 164 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.22× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 152 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.95× (z +11.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 123 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 185 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.229× (z -9.2) |
| [[AN3 CA (line)]] | alt | 145 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 398 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 290 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 128 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3011), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERLIN2]] | +0.73 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[EIF4G2]] | +0.73 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[ELK4]] | +0.70 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[HNRNPK]] | +0.70 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[LIN7C]] | +0.69 | +0.57 / +0.71 | both halves | 8e-06 | pathway: Activation of NMDA receptors and postsynaptic events |
| [[BAG6]] | +0.68 | +0.57 / +0.74 | both halves | 1e-05 |  |
| [[CHRAC1]] | +0.67 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[TMX4]] | +0.67 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[CGGBP1]] | +0.67 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[TUG1]] | +0.66 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[DDX6]] | +0.66 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[MOB1A]] | +0.66 | +0.44 / +0.66 | both halves | 3e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 8 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POP7]] | -0.68 | -0.38 / -0.67 | both halves | 6e-05 |  |
| [[USP42]] | -0.68 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[TSEN54]] | -0.65 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[ATP5MJ]] | -0.64 | -0.34 / -0.64 | both halves | 1e-04 |  |
| [[RPP21]] | -0.64 | -0.40 / -0.57 | both halves | 4e-05 |  |
| [[TMEM120B]] | -0.63 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[C15orf61]] ⚠ | -0.63 | -0.37 / -0.65 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[DHX57]] | -0.63 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[MRPS26]] | -0.63 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[UBE2R2]] | -0.63 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[DTX2P1-UPK3BP1-PMS2P11]] | -0.62 | -0.57 / -0.61 | both halves | 9e-06 |  |
| [[PUS3]] | -0.62 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[TOMM5]] | -0.62 | -0.51 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PRKAR1A's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises PRKAR1A's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises PRKAR1A's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.662). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.1, -22.1); signed map (17.4, -33.5). **Vector** length 147, 49.8% of its response variance represented; |z| ≥ 3 in 1,225 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +12.8 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +12.3 | +16.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +11.0 | +11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.7 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.5 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +3.6 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +2.8 | +2.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -8.9 | -3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | -7.4 | -4.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.0 | -6.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.6 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.9 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.6 | -2.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.1 | -3.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.9 | -2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase cAMP-dependent type I regulatory subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.2 — chr17:68,511,780-68,551,319 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CNC1; previously PRKAR1, TSE1, PKR1, Prkar1alpha |
| Gene groups (HGNC) | Protein kinase A subunits |
| Reactome | 48 pathways, smallest: CREB1 phosphorylation through the activation of Adenylate Cyclase; ALK mutants bind TKIs; PKA activation in glucagon signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [P10644](https://www.uniprot.org/uniprotkb/P10644) (cAMP-dependent protein kinase type I-alpha regulatory subunit):

> Regulatory subunit of the cAMP-dependent protein kinases involved in cAMP signaling in cells.

**Summary**, from NCBI Gene [5573](https://www.ncbi.nlm.nih.gov/gene/5573):

> cAMP is a signaling molecule important for a variety of cellular functions. cAMP exerts its effects by activating the cAMP-dependent protein kinase, which transduces the signal through phosphorylation of different target proteins. The inactive kinase holoenzyme is a tetramer composed of two regulatory and two catalytic subunits. cAMP causes the dissociation of the inactive holoenzyme into a dimer of regulatory subunits bound to four cAMP and two free monomeric catalytic subunits. Four different …

**Accessions** — [HGNC:9388](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9388) · Entrez [5573](https://www.ncbi.nlm.nih.gov/gene/5573) · UniProt [P10644](https://www.uniprot.org/uniprotkb/P10644) · Ensembl [ENSG00000108946](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108946)

## Data

Gene col 3011: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3011); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3011, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3011]; `tensor/DDL_lfc|DDL_z.npy` [3011]; `embed/gene_vectors.npy` [3011]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3011 or target_col == 3011). Every well: [[PRKAR1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKAR1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
