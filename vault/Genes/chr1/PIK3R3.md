---
symbol: "PIK3R3"
type: "gene"
col: 3910
ensembl_id: "ENSG00000117461"
name: "phosphoinositide-3-kinase regulatory subunit 3"
location: "1p34.1"
module: 93
arm: "+"
pooled_cpm: 56.19
n_lines_expressing: 48
n_dd_up: 32
n_dd_down: 2
n_dd_up_clean: 22
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# PIK3R3

*phosphoinositide-3-kinase regulatory subunit 3* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.38× (z +32.7, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.766× (z -4.4, q 0.006, down in 28 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (RPMI-7951 0.0752×, A-427 0.161×, C-33 A 0.251×, NCI-H2030 0.239×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.336×, C-33 A 0.307×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 0.286×; ⚠ cell-cycle shift, explains ~49% of this change); [[Nevirapine (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0939×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLE4]] (+0.64, fdr 7e-06), [[HEXIM1]] (+0.59, fdr 1e-05), [[TEX14]] (+0.55, fdr 2e-05); moves opposite to [[PSMF1]] (-0.57, fdr 1e-05), [[NUDCD3]] (-0.55, fdr 3e-05), [[FAHD2CP]] (-0.51, fdr 4e-04).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3910.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.38×** | +32.7 | 0e+00 | 45/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **3.91×** | +15.8 | 0e+00 | 43/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.80×** | +14.8 | 0e+00 | 41/46 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.43×** | +14.5 | 3e-45 | 39/46 (CFPAC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.11×** | +13.1 | 3e-37 | 45/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.87×** | +12.2 | 4e-32 | 42/46 (NCI-H460, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.86×** | +11.7 | 1e-29 | 39/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.85×** | +10.0 | 7e-22 | 39/46 (A-172, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.43×** | +9.9 | 4e-21 | 37/46 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.80×** | +9.6 | 6e-20 | 38/46 (C32, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **3.08×** | +8.7 | 2e-16 | 36/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.97×** | +7.8 | 2e-13 | 33/45 (J82, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.56×** | +7.2 | 3e-11 | 33/46 (J82, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.84×** | +7.1 | 7e-11 | 34/47 (BT-474, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +6.6 | 1e-09 | 31/46 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.97×** | +5.2 | 6e-06 | 33/46 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +4.4 | 3e-04 | 23/45 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +4.1 | 0.001 | 19/46 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.002 | 19/47 (NCI-H1573, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3910.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (RPMI-7951 0.0752×, A-427 0.161×, C-33 A 0.251×, NCI-H2030 0.239×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.336×, C-33 A 0.307×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 0.286×; ⚠ cell-cycle shift, explains ~49% of this change); [[Nevirapine (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0939×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.766×** | -4.4 | 0.006 | 28/47 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.793×** | -3.9 | 0.033 | 25/46 (LS 180, C32, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.747× | -3.4 | 0.11 | 20/46 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.817× | -3.4 | 0.11 | 20/47 (A-172, LOX-IMVI, …) | all doses, flat |  |
| [[Pralsetinib (drug)]] 5 µM |  | 0.593× | -3.2 | 0.16 | 16/46 (NCI-H1573, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Larotrectinib sulfate (drug)]] 5 µM | ⚠ unreliable plate only | 0.774× | -3.0 | 0.24 | 12/46 (KATO III, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.83 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3910. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 25.2 | 10 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +27.5) | — |
| [[SW480 (line)]] | alt | 19.0 | 10 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.1× (z +25.4) | — |
| [[J82 (line)]] | alt | 39.8 | 9 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +19.1) | — |
| [[HOP62 (line)]] | alt | 31.4 | 8 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +21.2) | — |
| [[LOX-IMVI (line)]] | wt | 19.2 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.8× (z +21.6) | — |
| [[C32 (line)]] | wt | 72.9 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.45× (z +17.7) | — |
| [[CFPAC-1 (line)]] | alt | 32.0 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.0× (z +20.1) | — |
| [[H4 (line)]] | wt | 44.2 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.11× (z +15.8) | — |
| [[NCI-H1573 (line)]] | alt | 169 | 2 | 3 (3 ⚠) | [[Selinexor (drug)]] 5 µM 2.63× (z +10.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.286× (z -9.6) ⚠ cell-cycle shift, explains ~49% of this change |
| [[SW1417 (line)]] | alt | 65.8 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.08× (z +15.2) | — |
| [[A-172 (line)]] | wt | 32.6 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.78× (z +20.8) | — |
| [[A498 (line)]] | wt | 44.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +15.7) | — |
| [[HS-578T (line)]] | alt | 89.4 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.42× (z +17.1) | — |
| [[LS 180 (line)]] | wt | 38.6 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.22× (z +16.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 39.4 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.8× (z +22.4) | — |
| [[NCI-H2030 (line)]] | alt | 103 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +14.1) | [[Dinaciclib (drug)]] 0.05 µM 0.239× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 54.1 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +19.3) | — |
| [[RKO (line)]] | wt | 36.0 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.5× (z +20.0) | — |
| [[SNU-423 (line)]] | alt | 36.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.80× (z +16.5) | — |
| [[C-33 A (line)]] | alt | 127 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 21.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.9× (z +21.0) | — |
| [[NCI-H23 (line)]] | alt | 36.4 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +21.3) | — |
| [[A-427 (line)]] | wt | 82.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.96× (z +10.4) ⚠ cell-cycle shift, explains ~37% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 15.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.9× (z +14.4) | [[Nevirapine (drug)]] 0.05 µM 0.0939× (z -8.5) |
| [[Hs 766T (line)]] | wt | 50.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.84× (z +17.9) | — |
| [[KATO III (line)]] | alt | 18.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +18.7) | — |
| [[LoVo (line)]] | wt | 76.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.90× (z +20.2) | — |
| [[NCI-H1792 (line)]] | alt | 32.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.95× (z +14.9) | — |
| [[NCI-H2347 (line)]] | alt | 30.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.39× (z +15.3) | — |
| [[PANC-1 (line)]] | alt | 101 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.28× (z +18.5) | — |
| [[RPMI-7951 (line)]] | alt | 65.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.74× (z +13.2) | [[Dinaciclib (drug)]] 0.05 µM 0.0752× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 109 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +8.9) | — |
| [[SW48 (line)]] | wt | 22.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +15.7) | — |
| [[A549 (line)]] | wt | 15.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.10× (z +11.1) | — |
| [[COLO 205 (line)]] | alt | 35.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.63× (z +10.6) | — |
| [[HCT15 (line)]] | alt | 50.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +14.6) | — |
| [[HT-29 (line)]] | alt | 107 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +17.1) | — |
| [[hTERT-HPNE (line)]] | wt | 91.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.11× (z +13.3) | — |
| [[SHP-77 (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 1271 (line)]] | alt | 44.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.49× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 60.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.78× (z +16.1) | — |
| [[AN3 CA (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.3 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 142 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3910), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLE4]] | +0.64 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[HEXIM1]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[TEX14]] | +0.55 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[LINC01285]] | +0.55 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[KLHL15]] | +0.55 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[FAM222A]] | +0.54 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[TENT5A]] | +0.54 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[PTPN6]] | +0.54 | +0.52 / +0.47 | both halves | 2e-05 | same gene group; pathway: GPVI-mediated activation cascade; STRING 910 |
| [[TRIM72]] | +0.54 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[FAM151B]] | +0.53 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[LGMN]] | +0.53 | +0.46 / +0.60 | both halves | 3e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[LRRC23]] | +0.52 | +0.56 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMF1]] | -0.57 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[NUDCD3]] | -0.55 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[FAHD2CP]] | -0.51 | -0.25 / -0.35 | both halves | 4e-04 |  |
| [[TAMM41]] | -0.50 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[SIN3B]] | -0.50 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[MECR]] | -0.50 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[TBC1D13]] | -0.50 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[RFT1]] | -0.49 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[POFUT1]] | -0.49 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[MEAF6]] | -0.48 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[THOC1]] | -0.48 | -0.57 / -0.26 | both halves | 3e-04 |  |
| [[NLE1]] | -0.48 | -0.54 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PIK3R3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ECHDC3]] | B | ECHDC3 activity raises PIK3R3's level | lines that do not express ECHDC3 (23) vs lines expressing it (27) | 1.60× lower at baseline in the lines without ECHDC3 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: CACNA2D1, ZNF229, LRRIQ1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.660). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.4, -27.1); signed map (4.5, 16.0). **Vector** length 111, 34.5% of its response variance represented; |z| ≥ 3 in 1,453 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.2 | +11.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +9.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +7.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +14.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +10.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.3 | +2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +4.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -5.1 | +8.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.6 | +15.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.5 | -4.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.1 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.8 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.4 | -1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | phosphoinositide-3-kinase regulatory subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:46,040,140-46,133,036 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p55 |
| Gene groups (HGNC) | SH2 domain containing |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, UV_RESPONSE_DN, APICAL_JUNCTION, MTORC1_SIGNALING |
| Reactome | 44 pathways, smallest: Co-stimulation by ICOS; Interleukin-7 signaling; Signaling by KIT in disease |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92569](https://www.uniprot.org/uniprotkb/Q92569) (Phosphatidylinositol 3-kinase regulatory subunit gamma):

> Binds to activated (phosphorylated) protein-tyrosine kinases through its SH2 domain and regulates their kinase activity. During insulin stimulation, it also binds to IRS-1.

**Summary**, from NCBI Gene [8503](https://www.ncbi.nlm.nih.gov/gene/8503):

> Phosphatidylinositol 3-kinase (PI3K) phosphorylates phosphatidylinositol and similar compounds, which then serve as second messengers in growth signaling pathways. PI3K is composed of a catalytic and a regulatory subunit. The protein encoded by this gene represents a regulatory subunit of PI3K. The encoded protein contains two SH2 domains through which it binds activated protein tyrosine kinases to regulate their activity. [provided by RefSeq, Jun 2016]

**Accessions** — [HGNC:8981](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8981) · Entrez [8503](https://www.ncbi.nlm.nih.gov/gene/8503) · UniProt [Q92569](https://www.uniprot.org/uniprotkb/Q92569) · Ensembl [ENSG00000117461](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117461)

## Data

Gene col 3910: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3910); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3910, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3910]; `tensor/DDL_lfc|DDL_z.npy` [3910]; `embed/gene_vectors.npy` [3910]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3910 or target_col == 3910). Every well: [[PIK3R3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIK3R3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
