---
symbol: "USF2"
type: "gene"
col: 2645
ensembl_id: "ENSG00000105698"
name: "upstream transcription factor 2, c-fos interacting"
location: "19q13.12"
module: 50
arm: "+"
pooled_cpm: 33.05
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 8
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# USF2

*upstream transcription factor 2, c-fos interacting* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.49× (z +14.7, q 0e+00, up in 43 of 43 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (HEC-1-A 5.51×, SW480 5.41×, HOP62 4.99×, PANC-1 3.82×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (SW480 7.30×, KATO III 9.09×, HEC-1-A 4.27×, HOP62 4.80×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 3.76×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.466× (z -9.0, q 1e-16, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERP29]] (+0.66, fdr 7e-06), [[TLE5]] (+0.58, fdr 1e-05), [[HOXB7]] (+0.58, fdr 1e-05); moves opposite to [[HAUS7]] (-0.57, fdr 4e-05), [[VPS25]] (-0.56, fdr 7e-05), [[EIF6]] (-0.55, fdr 3e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2645.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (HEC-1-A 5.51×, SW480 5.41×, HOP62 4.99×, PANC-1 3.82×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (SW480 7.30×, KATO III 9.09×, HEC-1-A 4.27×, HOP62 4.80×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 3.76×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.49×** | +14.7 | 0e+00 | 43/43 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.22×** | +13.3 | 1e-37 | 36/37 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.19×** | +8.5 | 3e-15 | 38/42 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.58×** | +5.4 | 8e-06 | 36/46 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.32× | +3.1 | 0.19 | 21/46 (SNU-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.31× | +3.0 | 0.23 | 22/46 (RKO, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2645.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.466×** | -9.0 | 1e-16 | 44/48 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.494×** | -8.3 | 3e-14 | 44/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.504×** | -8.1 | 1e-13 | 44/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.561×** | -6.8 | 1e-09 | 32/47 (SNU-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.674×** | -6.5 | 7e-09 | 28/47 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.628×** | -5.5 | 5e-06 | 31/48 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.700×** | -4.0 | 0.006 | 29/48 (J82, SW48, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.733×** | -3.6 | 0.019 | 27/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | 0.774× | -3.0 | 0.17 | 19/47 (A-427, SHP-77, …) | rises with dose | cell-cycle shift (explains ~12% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2645. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 33.7 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 7.30× (z +17.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.299× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 19.1 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.58× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 51.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +16.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 48.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +14.0) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 64.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -10.9) |
| [[KATO III (line)]] | alt | 31.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.09× (z +15.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 35.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.22× (z +11.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.320× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 37.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -11.7) |
| [[PANC-1 (line)]] | alt | 40.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +12.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -12.2) |
| [[A-172 (line)]] | wt | 31.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.88× (z +9.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.320× (z -8.6) |
| [[A498 (line)]] | wt | 22.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.22× (z +10.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 35.1 | 0 | 2 (1 ⚠) | — | [[Oxaprozin (drug)]] 0.5 µM 0.0774× (z -10.5) |
| [[HS-578T (line)]] | alt | 37.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 30.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 16.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.57× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 25.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.69× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 30.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +9.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 43.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +11.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 16.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +8.8) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 36.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +9.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 22.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +9.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 26.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 45.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +12.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 32.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 28.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 30.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +8.5) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 28.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.77× (z +8.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 36.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 43.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 29.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.93× (z +11.2) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 38.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0850× (z -13.9) |
| [[SW1417 (line)]] | alt | 46.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 44.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.251× (z -8.6) |
| [[A-427 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2645), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERP29]] | +0.66 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[TLE5]] | +0.58 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[HOXB7]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[CREBRF]] | +0.55 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[HOXC6]] | +0.54 | +0.40 / +0.56 | both halves | 4e-05 |  |
| [[STAG3L4-1]] | +0.54 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[LDB1]] | +0.54 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[MIRLET7BHG]] | +0.54 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[EMC10]] | +0.54 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[RPL41]] | +0.54 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[TXNDC16]] | +0.54 | +0.39 / +0.42 | both halves | 6e-05 |  |
| [[RBM33]] | +0.53 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HAUS7]] | -0.57 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[VPS25]] | -0.56 | -0.58 / -0.38 | both halves | 7e-05 |  |
| [[EIF6]] | -0.55 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[APEX2]] | -0.55 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[RRP7A]] | -0.54 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[ATP5MC1]] | -0.50 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[FADD]] | -0.49 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[PWP2]] | -0.49 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[DYNLT1]] | -0.48 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[DCTPP1]] | -0.47 | -0.29 / -0.43 | both halves | 2e-04 |  |
| [[UTP11]] | -0.46 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[SETX]] | -0.46 | -0.44 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises USF2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.270). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.4, -48.4); signed map (-24.0, -3.9). **Vector** length 72.3, 16.7% of its response variance represented; |z| ≥ 3 in 692 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +13.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +14.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | -0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +8.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | -0.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +2.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.9 | +0.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -6.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | upstream transcription factor 2, c-fos interacting |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:35,268,962-35,279,821 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FIP, bHLHb12 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Reactome | 3 pathways, smallest: Estrogen-dependent gene expression; ESR-mediated signaling; Signaling by Nuclear Receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15853](https://www.uniprot.org/uniprotkb/Q15853) (Upstream stimulatory factor 2):

> Transcription factor that binds to a symmetrical DNA sequence (E-boxes) (5'-CACGTG-3') that is found in a variety of viral and cellular promoters.

**Summary**, from NCBI Gene [7392](https://www.ncbi.nlm.nih.gov/gene/7392):

> This gene encodes a member of the basic helix-loop-helix leucine zipper family of transcription factors. The encoded protein can activate transcription through pyrimidine-rich initiator (Inr) elements and E-box motifs and is involved in regulating multiple cellular processes. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:12594](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12594) · Entrez [7392](https://www.ncbi.nlm.nih.gov/gene/7392) · UniProt [Q15853](https://www.uniprot.org/uniprotkb/Q15853) · Ensembl [ENSG00000105698](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105698)

## Data

Gene col 2645: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2645); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2645, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2645]; `tensor/DDL_lfc|DDL_z.npy` [2645]; `embed/gene_vectors.npy` [2645]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2645 or target_col == 2645). Every well: [[USF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
