---
symbol: "SUZ12P1"
type: "gene"
col: 15441
ensembl_id: "ENSG00000264538"
name: "SUZ12 pseudogene 1"
location: "17q11.2"
module: 71
arm: "+"
pooled_cpm: 57.9
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 10
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# SUZ12P1

*SUZ12 pseudogene 1* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.09× (z +14.5, q 4e-45, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.486× (z -13.2, q 7e-37, down in 39 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 0.681× (z -4.1, q 0.005, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIN9]] (+0.64, fdr 7e-06), [[C2orf42]] (+0.63, fdr 1e-05), [[MZT2A]] (+0.62, fdr 1e-05); moves opposite to [[PRELID3B]] (-0.58, fdr 1e-05), [[CSRP1]] (-0.57, fdr 4e-05), [[ALAS1]] (-0.55, fdr 1e-04).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15441.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.09×** | +14.5 | 4e-45 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.83×** | +12.0 | 1e-30 | 43/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.81×** | +11.8 | 1e-29 | 44/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +10.1 | 7e-22 | 36/49 (AsPC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.66×** | +10.0 | 2e-21 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +9.0 | 3e-17 | 36/47 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +7.5 | 6e-12 | 27/48 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.42×** | +6.9 | 5e-10 | 34/47 (PANC-1, NCI-H460, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.00×** | +6.5 | 5e-09 | 34/49 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.1 | 8e-08 | 29/50 (C32, SW1417, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.31×** | +5.2 | 1e-05 | 27/47 (KATO III, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.27×** | +4.8 | 7e-05 | 26/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +4.5 | 3e-04 | 28/48 (HEC-1-A, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.003 | 24/48 (NCI-H1792, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.20×** | +3.7 | 0.010 | 19/48 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15441.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.486×** | -13.2 | 7e-37 | 39/45 (A549, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.518×** | -13.0 | 6e-36 | 42/48 (RKO, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.541×** | -11.7 | 4e-29 | 35/44 (MIA PaCa-2, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.705×** | -6.9 | 8e-10 | 33/47 (PANC-1, SNU-423, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.681×** | -4.1 | 0.005 | 22/47 (NCI-H460, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 0.05 µM |  | **0.810×** | -3.9 | 0.009 | 17/49 (SNU-1, NCI-H23, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.823×** | -3.8 | 0.010 | 20/48 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **0.825×** | -3.8 | 0.011 | 18/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.828×** | -3.7 | 0.013 | 20/48 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.823×** | -3.7 | 0.013 | 17/48 (NCI-H1573, SNU-423, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.886× | -3.3 | 0.047 | 14/48 (A-427, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.853× | -3.1 | 0.084 | 12/47 (SNU-423, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15441. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 64.5 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -11.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 63.0 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 59.4 | 5 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.11× (z +14.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.90× (z +13.6) | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -12.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 70.1 | 4 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.70× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.474× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 77.9 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.152× (z -18.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 53.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -11.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 119 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -19.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 38.8 | 0 | 3 (2 ⚠) | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.204× (z -11.0) |
| [[HS-578T (line)]] | alt | 43.3 | 2 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -9.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 75.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -15.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 42.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.27× (z +8.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -12.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 54.2 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.132× (z -20.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 72.9 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.224× (z -14.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 53.9 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.317× (z -11.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 91.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.311× (z -12.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 62.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.17× (z +8.6) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -15.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 81.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -10.9) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.301× (z -10.1) |
| [[H4 (line)]] | wt | 39.2 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.34× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.00× (z +8.8) | — |
| [[KATO III (line)]] | alt | 55.5 | 1 | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.31× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.386× (z -9.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 56.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.356× (z -9.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 42.9 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.38× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.266× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 41.8 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -13.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 64.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -17.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 57.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -14.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 23.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +13.1) | — |
| [[C-33 A (line)]] | alt | 89.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -11.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 30.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +11.2) | — |
| [[CHP-212 (line)]] | wt | 78.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -10.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 84.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -15.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 33.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0870× (z -17.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 44.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -17.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 60.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -11.3) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 66.6 | 0 | 1 | — | [[Everolimus (drug)]] 0.05 µM 0.196× (z -8.5) |
| [[A-172 (line)]] | wt | 52.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 77.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15441), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN9]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[C2orf42]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[MZT2A]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[EMSY]] | +0.60 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[ZBTB8OS]] | +0.60 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[WDR20]] | +0.59 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[ARHGEF11]] | +0.58 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[PKN3]] | +0.58 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[GATD1-DT]] | +0.57 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[LRR1]] | +0.57 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[TNPO2]] | +0.57 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[DBF4B]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRELID3B]] | -0.58 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[CSRP1]] | -0.57 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[ALAS1]] | -0.55 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[SPTAN1]] | -0.54 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[ANXA2]] | -0.52 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[HAPSTR1]] | -0.52 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[DMXL1]] | -0.52 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[KIFAP3]] | -0.51 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[NELFE]] | -0.51 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[SPTBN1]] | -0.51 | -0.31 / -0.58 | both halves | 2e-04 |  |
| [[DYNC1LI2]] | -0.50 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[CREB3]] | -0.50 | -0.54 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.541). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.4, -34.8); signed map (5.9, -2.8). **Vector** length 107, 30.6% of its response variance represented; |z| ≥ 3 in 1,027 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +9.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +12.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.4 | +11.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +10.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.3 | +14.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +1.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.0 | +1.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.0 | +2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.2 | -2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.2 | -13.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -4.4 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.4 | -3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -0.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | SUZ12 pseudogene 1 |
| Locus type | pseudogene |
| Location | 17q11.2 — chr17:30,731,886-30,776,402 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously SUZ12P |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:32421](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32421) · Entrez [440423](https://www.ncbi.nlm.nih.gov/gene/440423) · Ensembl [ENSG00000264538](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000264538)

## Data

Gene col 15441: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15441); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15441, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15441]; `tensor/DDL_lfc|DDL_z.npy` [15441]; `embed/gene_vectors.npy` [15441]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15441 or target_col == 15441). Every well: [[SUZ12P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUZ12P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
