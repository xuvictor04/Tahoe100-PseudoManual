---
symbol: "CPNE8"
type: "gene"
col: 6260
ensembl_id: "ENSG00000139117"
name: "copine 8"
location: "12q12"
module: 14
arm: "+"
pooled_cpm: 97.05
n_lines_expressing: 33
n_dd_up: 20
n_dd_down: 13
n_dd_up_clean: 15
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# CPNE8

*copine 8* — 12q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.90× (z +10.7, q 8e-24, up in 24 of 30 measured lines) ⚠ toxic. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.73× (z +9.1, q 4e-17, up in 22 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.355× (z -17.9, q 0e+00, down in 30 of 31 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[QKI]] (+0.60, fdr 1e-05), [[DENND2B]] (+0.58, fdr 3e-05), [[UVRAG]] (+0.56, fdr 2e-05); moves opposite to [[SLC35E1]] (-0.58, fdr 2e-05), [[SIN3B]] (-0.57, fdr 4e-05), [[ATG4B]] (-0.52, fdr 1e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[CCN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6260.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +10.7 | 8e-24 | 24/30 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.73×** | +9.1 | 4e-17 | 22/31 (Hs 766T, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +8.1 | 1e-13 | 19/31 (Hs 766T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.59×** | +8.0 | 2e-13 | 23/31 (C32, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +7.3 | 2e-11 | 22/31 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +7.1 | 1e-10 | 23/31 (Hs 766T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +6.2 | 3e-08 | 18/31 (A-427, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +6.2 | 5e-08 | 18/31 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +5.7 | 7e-07 | 21/31 (C32, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +5.5 | 2e-06 | 18/31 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +5.4 | 4e-06 | 20/31 (Hs 766T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +5.1 | 2e-05 | 19/31 (Hs 766T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.69×** | +4.5 | 3e-04 | 17/32 (Hs 766T, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.19× | +4.3 | 8e-04 | 15/31 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.022 | 11/31 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.3 | 0.030 | 10/31 (NCI-H2347, SW 900, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.036 | 11/31 (SW 900, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.042 | 11/32 (C32, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6260.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.355×** | -17.9 | 0e+00 | 30/31 (A549, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.363×** | -17.5 | 0e+00 | 29/31 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.402×** | -15.2 | 0e+00 | 22/28 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.464×** | -13.3 | 5e-38 | 27/32 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.528×** | -11.0 | 2e-26 | 29/31 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.568×** | -9.4 | 6e-19 | 24/30 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.653×** | -7.4 | 1e-11 | 20/31 (NCI-H2030, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.783×** | -4.2 | 0.002 | 20/32 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.786×** | -4.2 | 0.002 | 17/31 (A549, CHP-212, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.845× | -4.1 | 0.002 | 10/31 (SW 1088, Panc 03.27, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.805×** | -3.7 | 0.009 | 13/31 (AsPC-1, HT-29, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.803×** | -3.5 | 0.021 | 13/31 (NCI-H23, A549, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.765×** | -3.3 | 0.041 | 12/31 (NCI-H2347, A549, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.820×** | -3.2 | 0.060 | 13/29 (NCI-H2347, AN3 CA, …) | all doses, stronger at high dose | composition shift |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.879× | -3.2 | 0.060 | 10/32 (C32, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6260. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 128 | 8 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +23.9) | [[Panobinostat (drug)]] 5 µM 0.144× (z -18.9) |
| [[C32 (line)]] | wt | 96.9 | 9 (4 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.82× (z +13.8) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.31× (z +11.9) | — |
| [[NCI-H2347 (line)]] | alt | 308 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -22.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.410× (z -11.5) |
| [[PANC-1 (line)]] | alt | 171 | 2 (1 ⚠) | 7 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.274× (z -18.9) |
| [[A498 (line)]] | wt | 169 | 4 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 167 | 4 (3 ⚠) | 4 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.09× (z +14.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.349× (z -14.2) |
| [[AsPC-1 (line)]] | alt | 146 | 1 | 6 (3 ⚠) | [[Radotinib (drug)]] 5 µM 1.86× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.296× (z -11.8) |
| [[HT-29 (line)]] | alt | 108 | 0 | 7 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.164× (z -16.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.181× (z -16.1) |
| [[NCI-H1573 (line)]] | alt | 173 | 1 (1 ⚠) | 6 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.57× (z +10.1) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.158× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.400× (z -14.6) |
| [[Panc 03.27 (line)]] | alt | 145 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.170× (z -18.7) |
| [[A-427 (line)]] | wt | 120 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.0718× (z -27.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.332× (z -12.0) |
| [[A549 (line)]] | wt | 163 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.127× (z -25.3) |
| [[CFPAC-1 (line)]] | alt | 214 | 2 (1 ⚠) | 4 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.51× (z +9.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.271× (z -13.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.398× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 80.6 | 3 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +20.8) | [[Panobinostat (drug)]] 5 µM 0.263× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 222 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.424× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 223 | 2 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.236× (z -16.5) |
| [[SNU-423 (line)]] | alt | 132 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +14.1) | [[Panobinostat (drug)]] 0.5 µM 0.152× (z -17.2) |
| [[SW 900 (line)]] | alt | 116 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -10.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 179 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.186× (z -10.6) |
| [[CHP-212 (line)]] | wt | 199 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.146× (z -11.5) |
| [[SHP-77 (line)]] | alt | 90.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.225× (z -14.5) |
| [[hTERT-HPNE (line)]] | wt | 58.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +17.2) | — |
| [[HEC-1-A (line)]] | alt | 47.3 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.116× (z -9.6) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 113 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.335× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 83.4 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.02× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 112 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.370× (z -9.8) |
| [[HS-578T (line)]] | alt | 44.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.202× (z -12.6) |
| [[NCI-H596 (line)]] | alt | 82.4 | 0 | 1 | — | [[Oxaprozin (drug)]] 5 µM 0.207× (z -14.2) |
| [[A-172 (line)]] | wt | 8.10 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.74 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.81 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.60 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.78 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.16 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.98 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.52 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.36 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.76 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.61 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.82 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.64 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.61 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.49 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6260), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QKI]] | +0.60 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[DENND2B]] | +0.58 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[UVRAG]] | +0.56 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[GALNT7]] | +0.55 | +0.51 / +0.35 | both halves | 1e-04 |  |
| [[WDFY3]] | +0.54 | +0.35 / +0.45 | both halves | 1e-04 |  |
| [[CDC14A]] | +0.54 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[CCN3]] | +0.52 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[ANXA2R-AS1]] | +0.52 | +0.30 / +0.33 | both halves | 2e-04 |  |
| [[FAS]] | +0.51 | +0.31 / +0.43 | both halves | 2e-04 |  |
| [[PELI2]] | +0.51 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[BMPR1B]] | +0.51 | +0.34 / +0.39 | both halves | 1e-04 |  |
| [[ANOS2P]] | +0.50 | +0.35 / +0.25 | both halves | 4e-04 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35E1]] | -0.58 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[SIN3B]] | -0.57 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[ATG4B]] | -0.52 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[WDR37]] | -0.52 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[P4HB]] | -0.52 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[ZNF404]] | -0.51 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[KCTD20]] | -0.51 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[DDX19A]] | -0.50 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ASCC2]] | -0.50 | -0.29 / -0.34 | both halves | 2e-04 |  |
| [[AP1M1]] | -0.50 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[UBE4A]] | -0.49 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[LTN1]] | -0.49 | -0.37 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCN3]] | B | CPNE8 activity raises CCN3's level | lines that do not express CPNE8 (17) vs lines expressing it (33) | 1.59× lower at baseline in the lines without CPNE8 | 0.038 | ⚠ within organs, on part of the lines; also absent: NALCN, NT5E, MAP9 |
| [[MLXIP]] | B | CPNE8 activity lowers MLXIP's level | lines that do not express CPNE8 (17) vs lines expressing it (33) | 1.33× higher at baseline in the lines without CPNE8 | 0.099 | ⚠ within organs, on part of the lines; also absent: NALCN, NT5E, MAP9 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.420). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.3, -25.3); signed map (43.7, -0.4). **Vector** length 90.7, 23.0% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.6 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +6.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +0.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.8 | +10.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +7.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | -0.4 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | +1.9 | +1.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.5 | -17.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.1 | -17.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.1 | -11.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | +2.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.3 | +4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.3 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -4.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | copine 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q12 — chr12:38,646,822-38,907,430 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Copines |
| Reactome | 7 pathways, smallest: RHOD GTPase cycle; RHOJ GTPase cycle; RHOQ GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YQ8](https://www.uniprot.org/uniprotkb/Q86YQ8) (Copine-8):

> Probable calcium-dependent phospholipid-binding protein that may play a role in calcium-mediated intracellular processes.

**Summary**, from NCBI Gene [144402](https://www.ncbi.nlm.nih.gov/gene/144402):

> Calcium-dependent membrane-binding proteins may regulate molecular events at the interface of the cell membrane and cytoplasm. This gene is one of several genes that encode a calcium-dependent protein containing two N-terminal type II C2 domains and an integrin A domain-like sequence in the C-terminus. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:23498](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23498) · Entrez [144402](https://www.ncbi.nlm.nih.gov/gene/144402) · UniProt [Q86YQ8](https://www.uniprot.org/uniprotkb/Q86YQ8) · Ensembl [ENSG00000139117](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139117)

## Data

Gene col 6260: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6260); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6260, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6260]; `tensor/DDL_lfc|DDL_z.npy` [6260]; `embed/gene_vectors.npy` [6260]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6260 or target_col == 6260). Every well: [[CPNE8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPNE8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
