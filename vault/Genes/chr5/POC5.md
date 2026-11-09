---
symbol: "POC5"
type: "gene"
col: 7617
ensembl_id: "ENSG00000152359"
name: "POC5 centriolar protein"
location: "5q13.3"
module: 11
arm: "+"
pooled_cpm: 20.82
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 9
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# POC5

*POC5 centriolar protein* — 5q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.19× (z +24.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.688× (z -7.8, q 5e-12, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SHP-77 0.0881×, KATO III 0.131×, HEC-1-A 0.244×, HCT15 0.122×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-427 0.163×, SW480 0.314×, NCI-H1573 0.128×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (KATO III 0.162×, PANC-1 0.365×, SW 900 0.148×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (SW480 0.403×, MIA PaCa-2 0.241×); [[Digitoxin (drug)]] 0.5 µM in 2 lines (SW480 0.413×, PANC-1 0.458×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZSCAN26]] (+0.66, fdr 7e-06), [[NUP37]] (+0.65, fdr 1e-05), [[ABRAXAS2]] (+0.59, fdr 7e-06); moves opposite to [[LINC01128]] (-0.45, fdr 4e-05), [[TFRC]] (-0.45, fdr 2e-04), [[SARM1]] (-0.44, fdr 0.007, ⚠ one half only (not replicated)), [[NRBP2]] (-0.44, fdr 6e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7617.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.19×** | +24.2 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.14×** | +23.9 | 0e+00 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +21.0 | 0e+00 | 38/47 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.64×** | +19.5 | 0e+00 | 44/48 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.45×** | +18.7 | 0e+00 | 45/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.00×** | +14.4 | 3e-45 | 34/46 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.01×** | +13.8 | 3e-41 | 37/48 (PANC-1, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.79×** | +12.1 | 5e-32 | 36/48 (HOP62, COLO 205, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.79×** | +12.1 | 5e-32 | 39/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +10.2 | 8e-23 | 29/46 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +8.8 | 1e-16 | 22/48 (RKO, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +8.1 | 2e-14 | 24/48 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +7.8 | 2e-13 | 24/48 (A549, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +7.5 | 2e-12 | 28/47 (LoVo, COLO 205, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.43×** | +7.2 | 2e-11 | 22/47 (SW480, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +7.1 | 4e-11 | 28/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7617.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SHP-77 0.0881×, KATO III 0.131×, HEC-1-A 0.244×, HCT15 0.122×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-427 0.163×, SW480 0.314×, NCI-H1573 0.128×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (KATO III 0.162×, PANC-1 0.365×, SW 900 0.148×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (SW480 0.403×, MIA PaCa-2 0.241×); [[Digitoxin (drug)]] 0.5 µM in 2 lines (SW480 0.413×, PANC-1 0.458×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.688×** | -7.8 | 5e-12 | 24/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.693×** | -7.3 | 7e-11 | 24/45 (COLO 205, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.695×** | -7.3 | 7e-11 | 19/34 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.733×** | -6.4 | 2e-08 | 22/42 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.766×** | -5.5 | 4e-06 | 18/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.780×** | -5.2 | 2e-05 | 16/48 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.808×** | -4.4 | 8e-04 | 14/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.801×** | -4.3 | 0.001 | 16/38 (SHP-77, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.812×** | -4.2 | 0.002 | 11/47 (NCI-H23, RPMI-7951, …) | rises with dose |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.879× | -3.8 | 0.010 | 9/48 (A-172, A498, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.845× | -3.4 | 0.040 | 9/46 (HS-578T, NCI-H460, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7617. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 34.7 | 6 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +20.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.356× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.458× (z -9.2) |
| [[SW480 (line)]] | alt | 38.0 | 3 | 7 (5 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.17× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.403× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 17.8 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +14.9) | — |
| [[NCI-H460 (line)]] | wt | 22.8 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.35× (z +11.0) | [[Digitoxin (drug)]] 5 µM 0.320× (z -10.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 22.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.88× (z +20.0) | — |
| [[HEC-1-A (line)]] | alt | 24.0 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.10× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -11.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 21.2 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.42× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -14.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 19.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.62× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 18.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 15.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.33× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -13.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 20.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +10.3) | — |
| [[A-427 (line)]] | wt | 32.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -14.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 21.2 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 4.06× (z +9.4) | [[Auranofin (drug)]] 5 µM 0.241× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 20.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -9.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 12.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +11.5) | — |
| [[HCT15 (line)]] | alt | 28.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -11.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 17.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +13.0) | — |
| [[A498 (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -10.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 10.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.20× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -8.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0546× (z -14.9) ⚠ toxic |
| [[HT-29 (line)]] | alt | 21.5 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.90× (z +9.2) | — |
| [[J82 (line)]] | alt | 18.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +11.6) | — |
| [[LOX-IMVI (line)]] | wt | 15.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +9.9) | — |
| [[NCI-H2030 (line)]] | alt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +13.3) | — |
| [[SHP-77 (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0881× (z -17.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.169× (z -11.2) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 17.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +10.2) | — |
| [[SW 1271 (line)]] | alt | 62.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0936× (z -8.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW 900 (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -11.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 12.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.12× (z +10.0) | — |
| [[AN3 CA (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7617), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN26]] | +0.66 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[NUP37]] | +0.65 | +0.69 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[ABRAXAS2]] | +0.59 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[CEP295]] | +0.59 | +0.63 / +0.59 | both halves | 7e-06 | STRING 660 |
| [[PSMD4]] | +0.56 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[HYLS1]] | +0.54 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[HMGXB4]] | +0.54 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[MARCHF7]] | +0.54 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[DBT]] | +0.54 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[MRPL38]] | +0.53 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[SMG9]] | +0.53 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[FADD]] | +0.52 | +0.49 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01128]] | -0.45 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[TFRC]] | -0.45 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[SARM1]] | -0.44 | -0.03 / -0.52 | ⚠ one half (not replicated) | 0.007 |  |
| [[NRBP2]] | -0.44 | -0.38 / -0.47 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers POC5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.426). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-42.4, -57.3); signed map (-43.1, -33.6). **Vector** length 85.2, 18.9% of its response variance represented; |z| ≥ 3 in 1,154 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.2 | +19.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.9 | +12.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.4 | +13.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.8 | +7.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.6 | +7.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +7.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +4.1 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.7 | +3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +1.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.8 | -7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.2 | -4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.6 | -6.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.3 | -7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | +10.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.2 | -2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | POC5 centriolar protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.3 — chr5:75,674,124-75,717,448 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35779, MGC120442, MGC120443, MGC120444, hPOC5; previously C5orf37 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NA72](https://www.uniprot.org/uniprotkb/Q8NA72) (Centrosomal protein POC5):

> Essential for the assembly of the distal half of centrioles, required for centriole elongation. Acts as a negative regulator of centriole elongation.

**Summary**, from NCBI Gene [134359](https://www.ncbi.nlm.nih.gov/gene/134359):

> Predicted to enable identical protein binding activity. Involved in centriole elongation and negative regulation of centriole elongation. Located in centriole and centrosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26658](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26658) · Entrez [134359](https://www.ncbi.nlm.nih.gov/gene/134359) · UniProt [Q8NA72](https://www.uniprot.org/uniprotkb/Q8NA72) · Ensembl [ENSG00000152359](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152359)

## Data

Gene col 7617: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7617); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7617, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7617]; `tensor/DDL_lfc|DDL_z.npy` [7617]; `embed/gene_vectors.npy` [7617]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7617 or target_col == 7617). Every well: [[POC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
