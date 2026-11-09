---
symbol: "TMCO1"
type: "gene"
col: 6693
ensembl_id: "ENSG00000143183"
name: "transmembrane and coiled-coil domains 1"
location: "1q24.1"
module: 210
arm: "+"
pooled_cpm: 76.12
n_lines_expressing: 49
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/210"]
generated_by: "tahoemap"
---

# TMCO1

*transmembrane and coiled-coil domains 1* — 1q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.45× (z +17.9, q 0e+00, up in 47 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +15.3, q 0e+00, up in 44 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 0.508×; ⚠ cell-cycle shift, would explain all of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.275×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.409×; ⚠ toxic; cell-cycle shift, explains ~22% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RTF2]] (+0.69, fdr 1e-05), [[OS9]] (+0.62, fdr 2e-05), [[COPB2]] (+0.61, fdr 9e-06); moves opposite to [[MEMO1]] (-0.57, fdr 4e-05), [[ORAI1]] (-0.55, fdr 2e-05), [[PLEKHJ1]] (-0.51, fdr 2e-05).
> It is in [[Module 210]], a single-armed module (tRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6693.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.45×** | +17.9 | 0e+00 | 47/48 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.28×** | +15.9 | 0e+00 | 38/41 (HEC-1-A, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +15.3 | 0e+00 | 44/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +13.8 | 3e-41 | 41/44 (SHP-77, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.51×** | +13.2 | 1e-37 | 45/48 (PANC-1, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.88×** | +12.6 | 1e-34 | 45/47 (NCI-H460, A-427, …) | two highest doses | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.83×** | +12.1 | 9e-32 | 44/47 (NCI-H460, MIA PaCa-2, …) | two highest doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.78×** | +11.6 | 3e-29 | 43/47 (NCI-H460, A-427, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.86×** | +6.5 | 4e-09 | 32/47 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +6.3 | 2e-08 | 31/47 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.5 | 3e-06 | 24/47 (A-172, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +5.4 | 3e-06 | 25/46 (NCI-H1573, PANC-1, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.20×** | +5.3 | 6e-06 | 22/47 (A-427, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +5.3 | 6e-06 | 28/37 (HOP62, A-172, …) | top dose only | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.62×** | +5.0 | 2e-05 | 33/46 (NCI-H2347, C32, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +4.9 | 3e-05 | 26/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 2e-04 | 24/47 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +3.9 | 0.003 | 20/47 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6693.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 0.508×; ⚠ cell-cycle shift, would explain all of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.275×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.409×; ⚠ toxic; cell-cycle shift, explains ~22% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.838× | -3.5 | 0.23 | 17/47 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.841× | -3.3 | 0.25 | 17/48 (SW 900, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6693. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 64.4 | 8 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +13.5) | — |
| [[PANC-1 (line)]] | alt | 75.9 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.07× (z +12.5) | — |
| [[HOP62 (line)]] | alt | 69.4 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 89.8 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +12.0) | — |
| [[SW480 (line)]] | alt | 70.5 | 7 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +11.5) | — |
| [[HEC-1-A (line)]] | alt | 74.6 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +11.5) | — |
| [[NCI-H1573 (line)]] | alt | 63.7 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.28× (z +12.4) | — |
| [[A-427 (line)]] | wt | 58.8 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.46× (z +9.4) | — |
| [[A-172 (line)]] | wt | 80.7 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +10.6) | — |
| [[A549 (line)]] | wt | 67.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[J82 (line)]] | alt | 86.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.42× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +8.6) | — |
| [[LoVo (line)]] | wt | 64.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.67× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 63.7 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 53.4 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +10.6) | — |
| [[RKO (line)]] | wt | 78.0 | 3 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +9.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.409× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~22% of this change |
| [[SNU-423 (line)]] | alt | 56.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 94.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.56× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 52.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HS-578T (line)]] | alt | 59.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.32× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 78.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.31× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 98.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.96× (z +12.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 70.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +11.9) | — |
| [[A498 (line)]] | wt | 150 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[C-33 A (line)]] | alt | 47.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.43× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.29× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 68.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.27× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 65.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 75.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 1.90× (z +8.8) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 63.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.40× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 44.5 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.90× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 113 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.18× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 80.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.55× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 69.9 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.275× (z -10.9) |
| [[KATO III (line)]] | alt | 31.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.19× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[RPMI-7951 (line)]] | alt | 97.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.08× (z +9.3) | — |
| [[SNU-1 (line)]] | wt | 70.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.08× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SW1417 (line)]] | alt | 61.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.31 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 84.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 57.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 140 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6693), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTF2]] | +0.69 | +0.72 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[OS9]] | +0.62 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[COPB2]] | +0.61 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[PRPF18]] | +0.61 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[ARPC3]] | +0.60 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[C1D]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ERP44]] | +0.56 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[MIGA1]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[SUPT5H]] | +0.55 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[UBE4A]] | +0.55 | +0.67 / +0.38 | both halves | 6e-05 |  |
| [[DNAL1]] | +0.55 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[ASB3]] | +0.54 | +0.58 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEMO1]] | -0.57 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[ORAI1]] | -0.55 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[PLEKHJ1]] | -0.51 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[JPH1]] | -0.50 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[C2orf69]] | -0.50 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[CLN6]] | -0.49 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[GPR63]] | -0.49 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[CHD7]] | -0.48 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[SMC6]] | -0.47 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TMCO1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 210]] — tRNA processing; 13 genes; every member is in the + arm (projection on the module's main direction 0.666). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.3, -14.8); signed map (-57.0, 5.3). **Vector** length 93.6, 26.7% of its response variance represented; |z| ≥ 3 in 953 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +9.4 | +13.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.1 | +6.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.3 | +5.3 |
|  | [[NG25 (drug)]] 5 µM |  | +4.1 | +5.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +5.5 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | +1.4 | +0.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.2 | +0.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.1 | -1.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -0.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.9 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -0.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.8 | +0.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane and coiled-coil domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.1 — chr1:165,724,293-165,827,755 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HP10122; previously TMCC4 |
| Gene groups (HGNC) | GEL complex subunits |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UM00](https://www.uniprot.org/uniprotkb/Q9UM00) (Calcium load-activated calcium channel):

> Endoplasmic reticulum (ER) calcium-selective channel preventing intracellular Ca2(+) stores from overfilling and maintaining calcium homeostasis in the ER. In response to endoplasmic reticulum (ER) Ca2(+) overloading, assembles into a homotetramer, forming a functional calcium-selective channel facilitating Ca2(+) release. Mediates ER Ca2(+) homeostasis in osteoblasts and plays a key role in bone formation, via the CaMKII-HDAC4-RUNX2 signaling axis (By similarity). Component of the multi-pass …

**Summary**, from NCBI Gene [54499](https://www.ncbi.nlm.nih.gov/gene/54499):

> This locus encodes a transmembrane protein. Mutations at this locus have been associated with craniofacial dysmorphism, skeletal anomalies, and cognitive disability. Mutations at this locus have also been associated with open angle glaucoma blindness. Alternatively spliced transcript variants have been described. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:18188](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18188) · Entrez [54499](https://www.ncbi.nlm.nih.gov/gene/54499) · UniProt [Q9UM00](https://www.uniprot.org/uniprotkb/Q9UM00) · Ensembl [ENSG00000143183](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143183)

## Data

Gene col 6693: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6693); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6693, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6693]; `tensor/DDL_lfc|DDL_z.npy` [6693]; `embed/gene_vectors.npy` [6693]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6693 or target_col == 6693). Every well: [[TMCO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMCO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
