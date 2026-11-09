---
symbol: "MRPS9"
type: "gene"
col: 5793
ensembl_id: "ENSG00000135972"
name: "mitochondrial ribosomal protein S9"
location: "2q12.1"
module: 213
arm: "+"
pooled_cpm: 43.43
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/213"]
generated_by: "tahoemap"
---

# MRPS9

*mitochondrial ribosomal protein S9* — 2q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (14 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.73× (z +12.9, q 4e-35, up in 40 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.39× (z +11.5, q 3e-28, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.784× (z -8.5, q 2e-14, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (MIA PaCa-2 0.424×, A-427 0.351×, HOP62 0.502×, A498 0.539×, …); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RKO 0.222×, A-172 0.280×, AN3 CA 0.148×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 0.117×, NCI-H1573 0.369×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMLHE]] (+0.69, fdr 3e-05), [[THUMPD2]] (+0.66, fdr 7e-06), [[ERCC8]] (+0.65, fdr 7e-06); moves opposite to [[GTPBP1]] (-0.58, fdr 1e-05), [[HECA]] (-0.54, fdr 9e-05), [[MAPKAPK2]] (-0.52, fdr 1e-05).
> It is in [[Module 213]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 18 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5793.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +12.9 | 4e-35 | 40/47 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.41×** | +11.9 | 5e-30 | 32/48 (HEC-1-A, A549, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +11.5 | 3e-28 | 33/48 (A-172, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +11.2 | 4e-27 | 37/48 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +10.5 | 1e-23 | 39/48 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +10.1 | 6e-22 | 37/48 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.49×** | +9.8 | 1e-20 | 31/48 (LoVo, LS 180, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +9.6 | 6e-20 | 34/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +8.0 | 1e-13 | 36/48 (HOP62, A-172, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +7.9 | 1e-13 | 30/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +7.4 | 5e-12 | 28/48 (HEC-1-A, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.33×** | +6.9 | 2e-10 | 25/48 (A-172, SW 900, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +6.8 | 5e-10 | 26/48 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +6.4 | 5e-09 | 30/43 (NCI-H1573, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.30×** | +6.2 | 2e-08 | 20/42 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.48×** | +5.0 | 2e-05 | 19/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.47×** | +4.9 | 3e-05 | 17/47 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.32×** | +4.8 | 4e-05 | 21/48 (HOP62, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.43×** | +4.6 | 1e-04 | 17/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.43×** | +4.5 | 1e-04 | 16/48 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.18× | +4.0 | 0.001 | 9/48 (C32, A-172, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.002 | 9/48 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5793.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (MIA PaCa-2 0.424×, A-427 0.351×, HOP62 0.502×, A498 0.539×, …); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RKO 0.222×, A-172 0.280×, AN3 CA 0.148×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 0.117×, NCI-H1573 0.369×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.784×** | -8.5 | 2e-14 | 28/48 (MIA PaCa-2, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.840× | -4.3 | 0.005 | 14/47 (hTERT-HPNE, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.844× | -4.0 | 0.011 | 14/47 (SNU-1, HOP62, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.764×** | -3.5 | 0.077 | 13/48 (CFPAC-1, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.777× | -3.2 | 0.13 | 10/48 (A-427, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5793. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 70.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +14.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.46× (z +12.4) | — |
| [[A-172 (line)]] | wt | 29.7 | 1 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.95× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 30.6 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +12.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 43.1 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +9.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 66.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -13.6) |
| [[RKO (line)]] | wt | 51.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.76× (z +9.3) ⚠ toxic | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 66.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.86× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.654× (z -9.4) |
| [[A-427 (line)]] | wt | 52.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -11.6) |
| [[A498 (line)]] | wt | 36.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -10.0) |
| [[A549 (line)]] | wt | 41.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[AN3 CA (line)]] | alt | 62.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 35.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 51.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[NCI-H23 (line)]] | alt | 77.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -24.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[NCI-H460 (line)]] | wt | 56.0 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 1.81× (z +8.7) ⚠ toxic | — |
| [[PANC-1 (line)]] | alt | 46.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +8.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SHP-77 (line)]] | alt | 46.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[SW 1271 (line)]] | alt | 62.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0628× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5793), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMLHE]] | +0.69 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[THUMPD2]] | +0.66 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[ERCC8]] | +0.65 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[CCDC43]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[MRPL1]] | +0.65 | +0.56 / +0.70 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 995 |
| [[JPX]] | +0.64 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[RBM26]] | +0.62 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[TYW3]] | +0.61 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[ACBD6]] | +0.61 | +0.42 / +0.68 | both halves | 4e-05 |  |
| [[SNRPF]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[PGGT1B]] | +0.60 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[CWC27]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTPBP1]] | -0.58 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[HECA]] | -0.54 | -0.37 / -0.60 | both halves | 9e-05 |  |
| [[MAPKAPK2]] | -0.52 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[INPP5K]] | -0.50 | -0.49 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 213]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.802). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-22.7, -1.0); signed map (-18.6, -23.1). **Vector** length 90.5, 20.0% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.1 | +11.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.3 | +9.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.2 | +12.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.7 | +10.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +6.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.0 | +2.0 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | +4.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.6 | -8.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +0.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.6 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -0.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | -4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | +3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q12.1 — chr2:105,038,069-105,099,960 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPMS9, MRP-S9, S9mt, uS9m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [P82933](https://www.uniprot.org/uniprotkb/P82933) carries no function annotation.

**Summary**, from NCBI Gene [64965](https://www.ncbi.nlm.nih.gov/gene/64965):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14501](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14501) · Entrez [64965](https://www.ncbi.nlm.nih.gov/gene/64965) · UniProt [P82933](https://www.uniprot.org/uniprotkb/P82933) · Ensembl [ENSG00000135972](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135972)

## Data

Gene col 5793: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5793); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5793, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5793]; `tensor/DDL_lfc|DDL_z.npy` [5793]; `embed/gene_vectors.npy` [5793]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5793 or target_col == 5793). Every well: [[MRPS9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
