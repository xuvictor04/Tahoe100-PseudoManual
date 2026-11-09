---
symbol: "UBE2J1"
type: "gene"
col: 12698
ensembl_id: "ENSG00000198833"
name: "ubiquitin conjugating enzyme E2 J1"
location: "6q15"
module: 49
arm: "+"
pooled_cpm: 57.79
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 24
n_dd_up_clean: 1
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# UBE2J1

*ubiquitin conjugating enzyme E2 J1* — 6q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.32× (z +7.3, q 2e-10, up in 25 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Retinoic acid (drug)]] 5 µM: 1.13× (z +4.1, q 0.007, up in 8 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 2.38×, NCI-H23 3.23×, SW480 1.89×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 2.60×; ⚠ toxic; transcription drop); [[Selinexor (drug)]] 5 µM in 1 line (PANC-1 1.68×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.242× (z -36.9, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAM1]] (+0.66, fdr 1e-05), [[SLC35B1]] (+0.62, fdr 1e-05), [[ARL1]] (+0.59, fdr 1e-05); moves opposite to [[SNRPB]] (-0.48, fdr 9e-05), [[LARS2]] (-0.46, fdr 2e-04).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12698.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 2.38×, NCI-H23 3.23×, SW480 1.89×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 2.60×; ⚠ toxic; transcription drop); [[Selinexor (drug)]] 5 µM in 1 line (PANC-1 1.68×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.32×** | +7.3 | 2e-10 | 25/49 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +5.5 | 1e-05 | 19/40 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Retinoic acid (drug)]] 5 µM |  | 1.13× | +4.1 | 0.007 | 8/49 (Hs 766T, SW 900, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.17× | +4.1 | 0.007 | 16/48 (H4, BT-474, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.011 | 12/48 (NCI-H1573, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.16× | +3.8 | 0.013 | 16/48 (HOP62, NCI-H23, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.14× | +3.2 | 0.11 | 20/44 (A-427, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Bexarotene (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.12 | 8/48 (RPMI-7951, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12698.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.242×** | -36.9 | 0e+00 | 48/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.285×** | -32.7 | 0e+00 | 48/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.316×** | -30.0 | 0e+00 | 48/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.543×** | -21.0 | 0e+00 | 44/49 (NCI-H1792, HT-29, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.522×** | -16.9 | 0e+00 | 46/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.542×** | -15.3 | 0e+00 | 41/48 (HOP62, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.694×** | -12.6 | 2e-34 | 32/48 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.708×** | -12.1 | 1e-31 | 37/48 (SW1417, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.734×** | -11.1 | 5e-27 | 39/48 (HS-578T, RKO, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.653×** | -10.7 | 7e-25 | 35/50 (SW480, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.665×** | -10.6 | 1e-24 | 36/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.459×** | -10.6 | 1e-24 | 41/49 (HT-29, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.659×** | -10.4 | 7e-24 | 30/47 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.716×** | -8.7 | 1e-16 | 32/48 (A-172, SW 900, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.736×** | -8.0 | 6e-14 | 29/48 (HS-578T, HT-29, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.758×** | -6.9 | 1e-10 | 28/48 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.772×** | -6.7 | 6e-10 | 27/48 (HT-29, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.626×** | -6.4 | 6e-09 | 27/49 (HS-578T, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.785×** | -6.3 | 9e-09 | 22/48 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.867× | -3.7 | 0.004 | 10/48 (BT-474, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12698. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 88.9 | 0 | 11 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.169× (z -19.5) |
| [[SW480 (line)]] | alt | 69.8 | 1 (1 ⚠) | 9 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.89× (z +8.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -27.0) |
| [[HS-578T (line)]] | alt | 68.8 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.206× (z -17.2) |
| [[LoVo (line)]] | wt | 87.6 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.134× (z -24.3) |
| [[SW 900 (line)]] | alt | 74.6 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.178× (z -18.6) |
| [[HOP62 (line)]] | alt | 43.7 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -17.1) |
| [[J82 (line)]] | alt | 72.7 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.346× (z -13.0) |
| [[NCI-H1792 (line)]] | alt | 97.9 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.126× (z -23.3) |
| [[NCI-H2347 (line)]] | alt | 66.3 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -18.1) |
| [[PANC-1 (line)]] | alt | 34.5 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.60× (z +11.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.416× (z -10.9) |
| [[RKO (line)]] | wt | 70.2 | 0 | 7 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.238× (z -15.6) |
| [[A-172 (line)]] | wt | 68.3 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.171× (z -21.2) |
| [[NCI-H1573 (line)]] | alt | 36.6 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -14.1) |
| [[SW1417 (line)]] | alt | 62.6 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.153× (z -21.9) |
| [[A498 (line)]] | wt | 43.6 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.368× (z -12.8) |
| [[KATO III (line)]] | alt | 77.3 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.100× (z -24.6) |
| [[Panc 03.27 (line)]] | alt | 73.9 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -21.8) |
| [[A-427 (line)]] | wt | 40.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -20.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.317× (z -10.6) |
| [[A549 (line)]] | wt | 34.7 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -15.5) |
| [[AsPC-1 (line)]] | alt | 62.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.219× (z -15.2) |
| [[CFPAC-1 (line)]] | alt | 45.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.261× (z -13.8) |
| [[COLO 205 (line)]] | alt | 62.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.169× (z -13.7) |
| [[Hs 766T (line)]] | wt | 71.2 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.193× (z -16.8) |
| [[LS 180 (line)]] | wt | 85.6 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -18.5) |
| [[NCI-H460 (line)]] | wt | 40.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -17.2) |
| [[RPMI-7951 (line)]] | alt | 75.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.270× (z -12.1) |
| [[SHP-77 (line)]] | alt | 53.7 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.280× (z -11.6) |
| [[SW48 (line)]] | wt | 61.5 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.152× (z -14.1) |
| [[C32 (line)]] | wt | 66.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -15.1) |
| [[HEC-1-A (line)]] | alt | 42.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.373× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 59.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.241× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 60.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.260× (z -12.2) |
| [[SNU-423 (line)]] | alt | 62.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -15.7) |
| [[AN3 CA (line)]] | alt | 82.6 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.165× (z -11.0) |
| [[HCT15 (line)]] | alt | 59.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.231× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 61.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.449× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 56.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.274× (z -11.9) |
| [[SNU-1 (line)]] | wt | 58.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.185× (z -12.5) |
| [[BT-474 (line)]] | alt | 41.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -12.1) |
| [[C-33 A (line)]] | alt | 45.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -9.8) |
| [[H4 (line)]] | wt | 36.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.159× (z -12.3) |
| [[HepG2_C3A (line)]] | wt | 49.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.311× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 29.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +9.5) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12698), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAM1]] | +0.66 | +0.56 / +0.72 | both halves | 1e-05 | **novel candidate** |
| [[SLC35B1]] | +0.62 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ARL1]] | +0.59 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[SRP72]] | +0.59 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[GFPT1]] | +0.58 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[SEC63]] | +0.58 | +0.63 / +0.49 | both halves | 1e-05 | STRING 538 |
| [[COPG1]] | +0.57 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ARL2BP]] | +0.57 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[MPC1]] | +0.57 | +0.44 / +0.42 | both halves | 4e-05 | **novel candidate** |
| [[NANS]] | +0.55 | +0.66 / +0.35 | both halves | 1e-04 |  |
| [[EPRS1]] | +0.54 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[OSTC]] | +0.54 | +0.59 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPB]] | -0.48 | -0.45 / -0.37 | both halves | 9e-05 |  |
| [[LARS2]] | -0.46 | -0.49 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises UBE2J1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.7, -39.2); signed map (-56.9, 12.1). **Vector** length 89.3, 23.3% of its response variance represented; |z| ≥ 3 in 1,288 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | -3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.5 | +3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +1.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.0 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.9 | +2.6 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -5.3 | -8.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -4.5 | -8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -11.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.9 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.9 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -12.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -0.5 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 J1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q15 — chr6:89,326,625-89,352,722 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC153, CGI-76, NCUBE1, UBC6 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y385](https://www.uniprot.org/uniprotkb/Q9Y385) (Ubiquitin-conjugating enzyme E2 J1):

> Catalyzes the covalent attachment of ubiquitin to other proteins. Functions in the selective degradation of misfolded membrane proteins from the endoplasmic reticulum (ERAD) and is essential for cells to recover from ER stress. Plays a role in MAPKAPK2-dependent translational control of TNF synthesis. Also acts as a platform for perinuclear positioning of the endosomal system by mediating ubiquitination of SQSTM1 through interaction with the E3 ubiquitin-protein ligase RNF26. Plays a role in …

**Summary**, from NCBI Gene [51465](https://www.ncbi.nlm.nih.gov/gene/51465):

> The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, or E1s, ubiquitin-conjugating enzymes, or E2s, and ubiquitin-protein ligases, or E3s. This gene encodes a member of the E2 ubiquitin-conjugating enzyme family. This enzyme is located in the membrane of the endoplasmic reticulum (ER) and may contribute to quality …

**Accessions** — [HGNC:17598](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17598) · Entrez [51465](https://www.ncbi.nlm.nih.gov/gene/51465) · UniProt [Q9Y385](https://www.uniprot.org/uniprotkb/Q9Y385) · Ensembl [ENSG00000198833](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198833)

## Data

Gene col 12698: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12698); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12698, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12698]; `tensor/DDL_lfc|DDL_z.npy` [12698]; `embed/gene_vectors.npy` [12698]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12698 or target_col == 12698). Every well: [[UBE2J1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2J1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
