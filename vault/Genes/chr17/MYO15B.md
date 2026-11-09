---
symbol: "MYO15B"
type: "gene"
col: 15496
ensembl_id: "ENSG00000266714"
name: "myosin XVB"
location: "17q25.1"
module: 141
arm: "+"
pooled_cpm: 18.18
n_lines_expressing: 45
n_dd_up: 3
n_dd_down: 44
n_dd_up_clean: 1
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 11
direction_downstream: 5
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# MYO15B

*myosin XVB* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Neratinib (maleate) (drug)]] 5 µM: 1.27× (z +4.5, q 0.004, up in 12 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (AsPC-1 7.13×, SW1417 2.93×, LoVo 3.63×, HepG2/C3A 5.71×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 4 lines (AsPC-1 8.38×, LoVo 6.04×, SW1417 3.91×, KATO III 3.72×; ⚠ cell-cycle shift, explains ~44% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (COLO 205 5.40×, SW1417 3.38×, AsPC-1 4.00×); [[Tucidinostat (drug)]] 5 µM in 1 line (KATO III 3.80×); [[Harringtonine (drug)]] 0.5 µM in 1 line (KATO III 4.84×).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (18 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.316× (z -15.3, q 0e+00, down in 35 of 42 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.376× (z -13.0, q 4e-36, down in 33 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELFN2]] (+0.63, fdr 1e-05), [[ADAMTS13]] (+0.54, fdr 1e-05), [[PMEPA1]] (+0.53, fdr 3e-05); moves opposite to [[GAPVD1]] (-0.46, fdr 4e-05), [[PDSS2]] (-0.43, fdr 1e-04), [[ATP5PF]] (-0.42, fdr 2e-04).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[GOLT1A]] → it (grade B ⚠); 5 go from it, the strongest it → [[CCDC120]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15496.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (AsPC-1 7.13×, SW1417 2.93×, LoVo 3.63×, HepG2/C3A 5.71×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 4 lines (AsPC-1 8.38×, LoVo 6.04×, SW1417 3.91×, KATO III 3.72×; ⚠ cell-cycle shift, explains ~44% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (COLO 205 5.40×, SW1417 3.38×, AsPC-1 4.00×); [[Tucidinostat (drug)]] 5 µM in 1 line (KATO III 3.80×); [[Harringtonine (drug)]] 0.5 µM in 1 line (KATO III 4.84×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.27×** | +4.5 | 0.004 | 12/43 (A-172, Panc 03.27, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.33×** | +3.7 | 0.061 | 13/40 (NCI-H460, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +3.5 | 0.081 | 8/21 (BT-474, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.29× | +3.3 | 0.14 | 15/41 (NCI-H460, SW480, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.1 | 0.19 | 14/43 (KATO III, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 19 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15496.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.316×** | -15.3 | 0e+00 | 35/42 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.376×** | -13.0 | 4e-36 | 33/42 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.543×** | -11.4 | 5e-28 | 27/41 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.468×** | -10.1 | 1e-21 | 29/42 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.464×** | -9.6 | 7e-20 | 32/39 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.493×** | -9.4 | 6e-19 | 28/42 (NCI-H23, A-427, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.503×** | -9.1 | 7e-18 | 26/42 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.534×** | -8.3 | 6e-15 | 26/39 (A-427, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.521×** | -8.3 | 6e-15 | 22/41 (PANC-1, NCI-H23, …) | rises with dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.534×** | -8.3 | 6e-15 | 30/42 (PANC-1, A-427, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.554×** | -7.8 | 3e-13 | 28/41 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.575×** | -7.3 | 1e-11 | 24/41 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.579×** | -7.2 | 2e-11 | 24/41 (PANC-1, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.594×** | -6.9 | 2e-10 | 20/43 (CHP-212, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.375×** | -6.8 | 4e-10 | 23/42 (PANC-1, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.605×** | -6.7 | 1e-09 | 20/40 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.703×** | -6.6 | 2e-09 | 24/43 (H4, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.601×** | -6.5 | 3e-09 | 23/39 (MIA PaCa-2, C-33 A, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.608×** | -6.4 | 4e-09 | 19/41 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.462×** | -5.3 | 2e-06 | 22/39 (PANC-1, NCI-H1792, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.682×** | -5.1 | 9e-06 | 16/42 (NCI-H23, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~24% here); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.490×** | -4.9 | 2e-05 | 14/40 (MIA PaCa-2, PANC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.704×** | -4.5 | 2e-04 | 12/43 (MIA PaCa-2, NCI-H460, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15496. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 28.6 | 0 | 21 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -23.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0857× (z -19.1) |
| [[NCI-H23 (line)]] | alt | 28.2 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0775× (z -16.7) |
| [[MIA PaCa-2 (line)]] | alt | 15.4 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0903× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0902× (z -11.8) |
| [[SW480 (line)]] | alt | 59.5 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -14.1) |
| [[KATO III (line)]] | alt | 35.4 | 5 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.80× (z +12.9) | — |
| [[A-427 (line)]] | wt | 27.8 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.172× (z -11.6) |
| [[HT-29 (line)]] | alt | 39.2 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.175× (z -15.5) |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -9.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -8.7) |
| [[SW1417 (line)]] | alt | 44.6 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +11.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.38× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -11.1) |
| [[A-172 (line)]] | wt | 16.4 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.123× (z -10.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A549 (line)]] | wt | 25.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 37.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.13× (z +18.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.00× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 14.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -9.2) |
| [[LoVo (line)]] | wt | 15.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1573 (line)]] | alt | 17.9 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.156× (z -10.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 12.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0556× (z -10.8) |
| [[CHP-212 (line)]] | wt | 17.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.0335× (z -9.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[COLO 205 (line)]] | alt | 49.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.40× (z +9.9) | — |
| [[HCT15 (line)]] | alt | 18.1 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.129× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -11.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HepG2_C3A (line)]] | wt | 12.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HOP62 (line)]] | alt | 6.43 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0550× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[NCI-H1792 (line)]] | alt | 8.62 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0499× (z -13.1) |
| [[NCI-H2030 (line)]] | alt | 10.1 | 0 | 1 | — | [[Mozavaptan (drug)]] 5 µM 0.0579× (z -13.1) |
| [[NCI-H2347 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 7.03 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[SNU-1 (line)]] | wt | 15.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -9.0) |
| [[SNU-423 (line)]] | alt | 6.90 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0818× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[A498 (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.61 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.86 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15496), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELFN2]] | +0.63 | +0.62 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[ADAMTS13]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[PMEPA1]] | +0.53 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[RASGEF1A]] | +0.52 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[CDC42BPG]] | +0.51 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[CHD5]] | +0.50 | +0.41 / +0.39 | both halves | 5e-05 |  |
| [[PLEC]] | +0.50 | +0.46 / +0.44 | both halves | 3e-05 | same gene group |
| [[PTPRN2]] | +0.50 | +0.44 / +0.40 | both halves | 5e-05 |  |
| [[DHRS12]] | +0.49 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[IDUA]] | +0.49 | +0.39 / +0.47 | both halves | 6e-05 |  |
| [[ZNF385C]] | +0.49 | +0.46 / +0.38 | both halves | 7e-05 |  |
| [[NOXA1]] | +0.49 | +0.39 / +0.52 | both halves | 6e-05 | same gene group |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GAPVD1]] | -0.46 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[PDSS2]] | -0.43 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[ATP5PF]] | -0.42 | -0.38 / -0.29 | both halves | 2e-04 |  |
| [[RHOQ]] | -0.41 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[CLPP]] | -0.41 | -0.21 / -0.43 | both halves | 6e-04 |  |
| [[PLEKHA8]] | -0.40 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[CNPY2]] | -0.40 | -0.30 / -0.35 | both halves | 2e-04 |  |
| [[NBAS]] | -0.40 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[VPS37A]] | -0.40 | -0.26 / -0.47 | both halves | 4e-04 |  |
| [[COP1]] | -0.40 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[ZNF521]] | -0.40 | -0.36 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GOLT1A]] | B | GOLT1A activity raises MYO15B's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 2.14× lower at baseline in the lines without GOLT1A | 0.008 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[CDC42BPG]] | B | CDC42BPG activity raises MYO15B's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.95× lower at baseline in the lines without CDC42BPG | 0.018 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[CCDC120]] | B | CCDC120 activity raises MYO15B's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 1.91× lower at baseline in the lines without CCDC120 | 0.023 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[IRF6]] | B | IRF6 activity raises MYO15B's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 2.14× lower at baseline in the lines without IRF6 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[CD22]] | B | CD22 activity raises MYO15B's level | lines that do not express CD22 (21) vs lines expressing it (29) | 1.48× lower at baseline in the lines without CD22 | 0.064 | ⚠ within organs, on part of the lines; also absent: CX3CL1, SHROOM4, CFB; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises MYO15B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EPPK1]] | B | EPPK1 activity raises MYO15B's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 1.76× lower at baseline in the lines without EPPK1 | 0.073 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| [[PMEPA1]] | B | PMEPA1 activity raises MYO15B's level | lines that do not express PMEPA1 (6) vs lines expressing it (44) | 1.48× lower at baseline in the lines without PMEPA1 | 0.084 | ⚠ within organs, on part of the lines; also absent: SOX4, SLC2A1-DT, ENSG00000285253 |
| [[LINC02026]] | B | LINC02026 activity raises MYO15B's level | lines that do not express LINC02026 (8) vs lines expressing it (42) | 1.69× lower at baseline in the lines without LINC02026 | 0.086 | ⚠ within organs, on part of the lines; also absent: ASRGL1, ENSG00000256673 |
| [[RASGEF1A]] | B | RASGEF1A activity raises MYO15B's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 1.29× lower at baseline in the lines without RASGEF1A | 0.095 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[ZMAT1]] | B | ZMAT1 activity strengthens MYO15B's drug response | lines that do not express ZMAT1 (16) vs lines expressing it (27) | the lines without ZMAT1 respond 0.57× as strongly (z diff +1.79); strongest at Harringtonine 5 µM: 1.40x vs 0.41x (z diff +6.5) | 0.099 | ⚠ within organs, on part of the lines; also absent: NTN1, C19orf81, LMX1B; target measured in part of the lines; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC120]] | B | MYO15B activity raises CCDC120's level | lines that do not express MYO15B (5) vs lines expressing it (45) | 2.25× lower at baseline in the lines without MYO15B | 0.060 | ⚠ within organs, on part of the lines; also absent: ID2, ASRGL1, CTNNA3; maybe low, not absent; its own permutation p |
| [[BAIAP3]] | B | MYO15B activity raises BAIAP3's level | lines that do not express MYO15B (5) vs lines expressing it (45) | 2.02× lower at baseline in the lines without MYO15B | 0.060 | ⚠ within organs, on part of the lines; also absent: ID2, ASRGL1, CTNNA3; maybe low, not absent; its own permutation p |
| [[RHOQ]] | B | MYO15B activity lowers RHOQ's level | lines that do not express MYO15B (5) vs lines expressing it (45) | 1.61× higher at baseline in the lines without MYO15B | 0.060 | ⚠ within organs, on part of the lines; also absent: ID2, ASRGL1, CTNNA3; maybe low, not absent; its own permutation p |
| [[NOXA1]] | B | MYO15B activity raises NOXA1's level | lines that do not express MYO15B (5) vs lines expressing it (45) | 2.06× lower at baseline in the lines without MYO15B | 0.070 | ⚠ within organs, on part of the lines; also absent: ID2, ASRGL1, CTNNA3; maybe low, not absent |
| [[TRA2B]] | B | MYO15B activity raises TRA2B's level | lines that do not express MYO15B (5) vs lines expressing it (45) | 1.18× lower at baseline in the lines without MYO15B | 0.089 | ⚠ within organs, on part of the lines; also absent: ID2, ASRGL1, CTNNA3; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.482). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-3.9, 43.1); signed map (14.3, 23.4). **Vector** length 79.6, 16.6% of its response variance represented; |z| ≥ 3 in 1,197 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.0 | +0.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +2.3 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +0.1 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -4.2 | -9.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -13.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -9.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -7.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.9 | -10.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -6.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | myosin XVB |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,587,800-75,626,849 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MYO15BP |
| Gene groups (HGNC) | Myosin heavy chains, class XV; FERM domain containing; SH3 domain containing |
| Matched by | ensembl_id |

UniProt [Q96JP2](https://www.uniprot.org/uniprotkb/Q96JP2) carries no function annotation.

**Summary**, from NCBI Gene [80022](https://www.ncbi.nlm.nih.gov/gene/80022):

> Predicted to enable ATP binding activity; actin binding activity; and cytoskeletal motor activity. Predicted to be located in several cellular components, including brush border; cytoskeleton; and plasma membrane bounded cell projection. Predicted to be part of myosin complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14083](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14083) · Entrez [80022](https://www.ncbi.nlm.nih.gov/gene/80022) · UniProt [Q96JP2](https://www.uniprot.org/uniprotkb/Q96JP2) · Ensembl [ENSG00000266714](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000266714)

## Data

Gene col 15496: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15496); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15496, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15496]; `tensor/DDL_lfc|DDL_z.npy` [15496]; `embed/gene_vectors.npy` [15496]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15496 or target_col == 15496). Every well: [[MYO15B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYO15B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
