---
symbol: "GLE1"
type: "gene"
col: 4058
ensembl_id: "ENSG00000119392"
name: "GLE1 RNA export mediator"
location: "9q34.11"
module: 207
arm: "+"
pooled_cpm: 36.7
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/207"]
generated_by: "tahoemap"
---

# GLE1

*GLE1 RNA export mediator* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.81× (z +23.0, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.561× (z -15.9, q 0e+00, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PMS2P4-1]] (+0.72, fdr 7e-06), [[TSNAX-DISC1]] (+0.66, fdr 7e-06), [[CWF19L1]] (+0.64, fdr 7e-06); moves opposite to [[PCNX2]] (-0.63, fdr 3e-05), [[AIG1]] (-0.59, fdr 4e-05), [[UBE2E2]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 207]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4058.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +23.0 | 0e+00 | 43/47 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +13.9 | 2e-41 | 40/48 (RKO, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +11.9 | 3e-30 | 36/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +8.3 | 1e-14 | 27/47 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.33×** | +7.8 | 8e-13 | 29/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +7.1 | 1e-10 | 25/47 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.26×** | +6.3 | 2e-08 | 23/48 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.25×** | +5.9 | 3e-07 | 23/48 (A-427, C32, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +5.4 | 3e-06 | 18/48 (KATO III, SW1417, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +4.8 | 9e-05 | 15/48 (KATO III, BT-474, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.16× | +4.1 | 0.002 | 15/48 (AsPC-1, KATO III, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.23×** | +4.0 | 0.003 | 8/48 (SHP-77, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.14× | +3.6 | 0.016 | 7/48 (SW1417, A-172, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.053 | 7/48 (J82, A498, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4058.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.561×** | -15.9 | 0e+00 | 36/48 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.602×** | -13.5 | 7e-39 | 35/48 (J82, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.632×** | -12.7 | 2e-34 | 35/48 (NCI-H460, HOP62, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.688×** | -10.3 | 8e-23 | 30/47 (HOP62, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.680×** | -10.2 | 2e-22 | 27/47 (J82, H4, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.518×** | -9.5 | 2e-19 | 34/48 (Hs 766T, BT-474, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.820×** | -7.8 | 7e-13 | 22/48 (MIA PaCa-2, J82, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.768×** | -7.3 | 2e-11 | 23/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.611×** | -7.1 | 8e-11 | 24/48 (A-427, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.784×** | -6.7 | 1e-09 | 25/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -6.2 | 3e-08 | 0/48 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.810×** | -5.8 | 3e-07 | 21/48 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 0.868× | -5.5 | 1e-06 | 21/48 (J82, AsPC-1, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.828×** | -5.2 | 8e-06 | 12/48 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.848× | -4.6 | 2e-04 | 19/47 (A549, AsPC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.882× | -3.4 | 0.016 | 11/48 (BT-474, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.885× | -3.4 | 0.021 | 9/48 (RKO, SHP-77, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.888× | -3.3 | 0.028 | 13/48 (SW1417, SW480, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.894× | -3.0 | 0.067 | 14/48 (SW 1088, NCI-H23, …) | top dose only |  |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 0.927× | -3.0 | 0.067 | 2/48 (KATO III, LS 180) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4058. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 45.5 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +9.9) | [[Digitoxin (drug)]] 0.5 µM 0.405× (z -12.7) |
| [[SW480 (line)]] | alt | 45.1 | 2 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +13.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.441× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 20.7 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -14.0) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.296× (z -9.2) |
| [[J82 (line)]] | alt | 53.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -21.7) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.345× (z -12.3) |
| [[A549 (line)]] | wt | 40.7 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -12.2) ⚠ cell-cycle shift, explains ~65% of this change |
| [[HOP62 (line)]] | alt | 29.0 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.265× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.346× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 33.4 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.162× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 33.1 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -10.8) ⚠ cell-cycle shift, explains ~65% of this change |
| [[BT-474 (line)]] | alt | 59.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +10.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.354× (z -10.8) |
| [[CHP-212 (line)]] | wt | 24.5 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0685× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 33.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +10.9) | [[Digitoxin (drug)]] 0.5 µM 0.381× (z -9.0) |
| [[LS 180 (line)]] | wt | 27.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 66.5 | 2 | 0 | [[Selinexor (drug)]] 5 µM 1.86× (z +9.5) | — |
| [[C32 (line)]] | wt | 36.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +10.0) | — |
| [[H4 (line)]] | wt | 46.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.226× (z -9.3) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 34.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 51.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.143× (z -8.8) ⚠ toxic |
| [[HT-29 (line)]] | alt | 25.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 32.5 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.282× (z -8.7) |
| [[KATO III (line)]] | alt | 44.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 25.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.7) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 40.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 31.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 36.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 30.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.468× (z -8.6) |
| [[SNU-423 (line)]] | alt | 40.2 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.325× (z -10.6) |
| [[SW 900 (line)]] | alt | 19.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +9.2) | — |
| [[SW48 (line)]] | wt | 30.9 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.226× (z -8.5) |
| [[A-172 (line)]] | wt | 60.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4058), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2P4-1]] | +0.72 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[TSNAX-DISC1]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[CWF19L1]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[IKZF4]] | +0.63 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[NUP133]] | +0.62 | +0.46 / +0.63 | both halves | 3e-05 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 933 |
| [[TMED8]] | +0.62 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[MFSD8]] | +0.62 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[RECQL5]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[BLOC1S5-TXNDC5]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[POMT1]] | +0.61 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[RARS2]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[CRLS1]] | +0.61 | +0.40 / +0.70 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNX2]] | -0.63 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[AIG1]] | -0.59 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[UBE2E2]] | -0.58 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[ALCAM]] | -0.57 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[PLCB4]] | -0.57 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[FAT1]] | -0.55 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[MPDZ]] | -0.55 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[TIGD2]] | -0.53 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[FOXP1]] | -0.53 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[RPS6KA6]] | -0.52 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[AKAP6]] | -0.52 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ABLIM1]] | -0.52 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GLE1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 207]]; 15 genes; this gene is in the **+** arm (projection on the module's main direction 0.855). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-15.0, 22.6); signed map (-20.2, -1.1). **Vector** length 91.5, 19.8% of its response variance represented; |z| ≥ 3 in 1,066 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +23.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.3 | +13.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.9 | +8.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +3.3 | +5.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.8 | +0.1 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +1.6 | +1.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.5 | +0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.4 | +2.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +1.4 | +0.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.4 | -7.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.5 | -5.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -13.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.1 | -3.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.0 | -10.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -0.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.3 | -3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | +1.3 |

## What is on record

|  |  |
|---|---|
| Name | GLE1 RNA export mediator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,504,655-128,543,874 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hGLE1; previously GLE1L, LCCS1 |
| Gene groups (HGNC) | Nucleoporins |
| Reactome | 4 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53GS7](https://www.uniprot.org/uniprotkb/Q53GS7) (mRNA export factor GLE1):

> Required for the export of mRNAs containing poly(A) tails from the nucleus into the cytoplasm. May be involved in the terminal step of the mRNA transport through the nuclear pore complex (NPC).

**Summary**, from NCBI Gene [2733](https://www.ncbi.nlm.nih.gov/gene/2733):

> This gene encodes a predicted 75-kDa polypeptide with high sequence and structure homology to yeast Gle1p, which is nuclear protein with a leucine-rich nuclear export sequence essential for poly(A)+RNA export. Inhibition of human GLE1L by microinjection of antibodies against GLE1L in HeLa cells resulted in inhibition of poly(A)+RNA export. Immunoflourescence studies show that GLE1L is localized at the nuclear pore complexes. This localization suggests that GLE1L may act at a terminal step in …

**Accessions** — [HGNC:4315](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4315) · Entrez [2733](https://www.ncbi.nlm.nih.gov/gene/2733) · UniProt [Q53GS7](https://www.uniprot.org/uniprotkb/Q53GS7) · Ensembl [ENSG00000119392](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119392)

## Data

Gene col 4058: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4058); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4058, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4058]; `tensor/DDL_lfc|DDL_z.npy` [4058]; `embed/gene_vectors.npy` [4058]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4058 or target_col == 4058). Every well: [[GLE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
