---
symbol: "TRAPPC11"
type: "gene"
col: 9666
ensembl_id: "ENSG00000168538"
name: "trafficking protein particle complex subunit 11"
location: "4q35.1"
module: 17
arm: "+"
pooled_cpm: 39.8
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 16
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# TRAPPC11

*trafficking protein particle complex subunit 11* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.40× (z +9.0, q 1e-16, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.644× (z -11.7, q 6e-29, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DYNC2LI1]] (+0.73, fdr 7e-06), [[NIPSNAP2]] (+0.73, fdr 7e-06), [[ABITRAM]] (+0.70, fdr 7e-06); moves opposite to [[SLC23A3]] (-0.63, fdr 9e-06), [[LINC02798]] (-0.62, fdr 1e-05), [[LINC01588]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF569]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9666.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +9.0 | 1e-16 | 38/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.41×** | +6.4 | 3e-08 | 35/48 (RKO, PANC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.35×** | +5.7 | 2e-06 | 29/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.24×** | +3.8 | 0.020 | 15/48 (SW480, NCI-H2030, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.023 | 15/48 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.042 | 12/48 (C-33 A, SW48, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.21×** | +3.4 | 0.060 | 16/48 (SW480, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.2 | 0.089 | 16/48 (HOP62, LS 180, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +3.0 | 0.15 | 18/47 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9666.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.644×** | -11.7 | 6e-29 | 38/48 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.585×** | -10.1 | 2e-21 | 37/48 (SNU-423, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.655×** | -8.0 | 3e-13 | 37/46 (LoVo, NCI-H23, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.643×** | -7.7 | 2e-12 | 28/43 (C-33 A, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.699×** | -6.7 | 2e-09 | 31/48 (hTERT-HPNE, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.690×** | -6.7 | 2e-09 | 30/47 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.735×** | -5.8 | 6e-07 | 28/48 (SW480, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.727×** | -5.8 | 6e-07 | 23/39 (H4, AN3 CA, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.736×** | -5.8 | 6e-07 | 26/48 (NCI-H460, HOP62, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -5.3 | 8e-06 | 25/48 (SK-MEL-2, C32, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -4.5 | 3e-04 | 0/49 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.795×** | -4.3 | 8e-04 | 20/48 (AsPC-1, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.791×** | -4.2 | 0.001 | 23/48 (C32, AN3 CA, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.716×** | -4.1 | 0.002 | 22/48 (H4, NCI-H460, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.875× | -3.5 | 0.017 | 18/48 (AN3 CA, J82, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.829×** | -3.4 | 0.025 | 14/47 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | 0.837× | -3.3 | 0.028 | 14/48 (LS 180, Panc 03.27, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.841× | -3.2 | 0.037 | 17/47 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.720×** | -3.2 | 0.037 | 20/48 (CFPAC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.785×** | -3.0 | 0.089 | 14/47 (H4, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9666. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 70.7 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SW480 (line)]] | alt | 50.0 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.411× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.448× (z -9.8) |
| [[A498 (line)]] | wt | 48.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.323× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -10.9) |
| [[C32 (line)]] | wt | 47.7 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -18.2) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -10.6) |
| [[A-427 (line)]] | wt | 29.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 40.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -11.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 44.9 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.369× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 45.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 42.8 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -12.5) |
| [[A-172 (line)]] | wt | 46.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 27.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -8.9) |
| [[C-33 A (line)]] | alt | 49.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -12.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 39.6 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.134× (z -8.6) |
| [[COLO 205 (line)]] | alt | 37.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[H4 (line)]] | wt | 49.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0848× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HCT15 (line)]] | alt | 51.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -9.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -11.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 42.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.368× (z -9.7) ⚠ toxic |
| [[J82 (line)]] | alt | 35.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -9.7) |
| [[KATO III (line)]] | alt | 37.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[LoVo (line)]] | wt | 40.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H2347 (line)]] | alt | 54.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -8.7) |
| [[PANC-1 (line)]] | alt | 37.9 | 1 | 0 | [[Selinexor (drug)]] 5 µM 1.70× (z +8.9) | — |
| [[RKO (line)]] | wt | 47.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -11.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 34.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.305× (z -10.1) |
| [[SW 1271 (line)]] | alt | 48.6 | 0 | 1 | — | [[Furosemide (drug)]] 0.05 µM 0.0447× (z -10.7) |
| [[A549 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9666), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYNC2LI1]] | +0.73 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[NIPSNAP2]] | +0.73 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[ABITRAM]] | +0.70 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[MRPS31P4]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[GEMIN2]] | +0.69 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[TTC8]] | +0.69 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[CEPT1]] | +0.68 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[TRUB1]] | +0.68 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[TATDN3]] | +0.67 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[METTL14]] | +0.65 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[RAD17]] | +0.65 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[UBA5]] | +0.65 | +0.70 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC23A3]] | -0.63 | -0.57 / -0.63 | both halves | 9e-06 |  |
| [[LINC02798]] | -0.62 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[LINC01588]] | -0.60 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[SPON1-AS1]] | -0.60 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[CHADL]] | -0.59 | -0.46 / -0.65 | both halves | 3e-05 |  |
| [[GATAD2A]] | -0.59 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[WNT2B]] | -0.58 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[ZDHHC11]] | -0.58 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[QRICH2]] | -0.57 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[SFXN5]] | -0.56 | -0.50 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF569]] | B | ZNF569 activity raises TRAPPC11's level | lines that do not express ZNF569 (14) vs lines expressing it (36) | 1.13× lower at baseline in the lines without ZNF569 | 0.063 | ⚠ within organs, on part of the lines; also absent: ZNF570, PEG10, DNAAF9 |
| [[MDGA1]] | B | MDGA1 activity raises TRAPPC11's level | lines that do not express MDGA1 (13) vs lines expressing it (37) | 1.25× lower at baseline in the lines without MDGA1 | 0.066 | ⚠ within organs, on part of the lines; also absent: TCF7L1, ZNF470, FBXL2 |
| [[TOP2A]] | B | TOP2A activity raises TRAPPC11's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.797). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.5, -1.9); signed map (-21.8, -14.4). **Vector** length 102, 24.7% of its response variance represented; |z| ≥ 3 in 1,014 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Intraflagellar transport* (reactome, mean cos +0.52 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.2 | +9.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.5 | +6.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +2.4 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +2.9 | +5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | -0.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.5 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.3 | +3.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.1 | -11.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.9 | -10.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -5.0 | -4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.0 | -3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | trafficking protein particle complex subunit 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:183,659,267-183,713,594 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12716, gry, foigr; previously C4orf41 |
| Gene groups (HGNC) | Trafficking protein particle complex subunits |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z392](https://www.uniprot.org/uniprotkb/Q7Z392) (Trafficking protein particle complex subunit 11):

> Involved in endoplasmic reticulum to Golgi apparatus trafficking at a very early stage.

**Summary**, from NCBI Gene [60684](https://www.ncbi.nlm.nih.gov/gene/60684):

> The protein encoded by this gene is a subunit of the TRAPP (transport protein particle) tethering complex, which functions in intracellular vesicle trafficking. This subunit is involved in early stage endoplasmic reticulum-to-Golgi vesicle transport. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Jan 2013]

**Accessions** — [HGNC:25751](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25751) · Entrez [60684](https://www.ncbi.nlm.nih.gov/gene/60684) · UniProt [Q7Z392](https://www.uniprot.org/uniprotkb/Q7Z392) · Ensembl [ENSG00000168538](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168538)

## Data

Gene col 9666: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9666); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9666, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9666]; `tensor/DDL_lfc|DDL_z.npy` [9666]; `embed/gene_vectors.npy` [9666]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9666 or target_col == 9666). Every well: [[TRAPPC11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAPPC11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
