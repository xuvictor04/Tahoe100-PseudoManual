---
symbol: "PTGR3"
type: "gene"
col: 11076
ensembl_id: "ENSG00000180011"
name: "prostaglandin reductase 3"
location: "18q22.3"
module: 15
arm: "+"
pooled_cpm: 23.6
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 25
n_dd_up_clean: 5
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# PTGR3

*prostaglandin reductase 3* — 18q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.82× (z +14.0, q 8e-42, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.259× (z -22.3, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHC2-AS1]] (+0.66, fdr 1e-05), [[KCTD1]] (+0.62, fdr 3e-05), [[LEMD3]] (+0.62, fdr 1e-04); moves opposite to [[STX8]] (-0.57, fdr 7e-05), [[CYB5R1]] (-0.54, fdr 3e-04), [[HNRNPDL]] (-0.54, fdr 8e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11076.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +14.0 | 8e-42 | 37/46 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +5.9 | 1e-06 | 25/44 (KATO III, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.5 | 6e-06 | 24/46 (MIA PaCa-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.3 | 2e-05 | 22/47 (hTERT-HPNE, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +4.9 | 1e-04 | 20/46 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.004 | 13/47 (A549, MIA PaCa-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.22×** | +3.3 | 0.093 | 13/44 (HS-578T, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.2 | 0.097 | 10/47 (HS-578T, SW1417, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11076.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.259×** | -22.3 | 0e+00 | 45/47 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.281×** | -20.9 | 0e+00 | 45/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.470×** | -17.6 | 0e+00 | 41/46 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.421×** | -14.3 | 5e-44 | 38/46 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.519×** | -10.8 | 4e-25 | 36/46 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.343×** | -9.2 | 3e-18 | 37/47 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.585×** | -8.3 | 6e-15 | 36/46 (C32, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.610×** | -8.1 | 3e-14 | 31/46 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.419×** | -7.5 | 5e-12 | 29/44 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.636×** | -7.5 | 5e-12 | 29/46 (PANC-1, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.702×** | -5.6 | 1e-06 | 22/46 (SK-MEL-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.727×** | -5.2 | 8e-06 | 21/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.555×** | -5.0 | 2e-05 | 21/44 (PANC-1, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.738×** | -5.0 | 2e-05 | 21/45 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.673×** | -4.7 | 1e-04 | 18/47 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.591×** | -4.5 | 2e-04 | 20/45 (HCT15, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11076. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 61.6 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -23.5) |
| [[C32 (line)]] | wt | 51.4 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -17.3) |
| [[LOX-IMVI (line)]] | wt | 24.7 | 1 | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -23.0) |
| [[LoVo (line)]] | wt | 24.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -18.5) |
| [[SK-MEL-2 (line)]] | alt | 33.1 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.127× (z -15.9) |
| [[HS-578T (line)]] | alt | 17.6 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -14.3) |
| [[KATO III (line)]] | alt | 19.3 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.189× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 26.2 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.221× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 29.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.226× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 18.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -22.6) |
| [[SW480 (line)]] | alt | 19.1 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -17.3) |
| [[Hs 766T (line)]] | wt | 32.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.141× (z -14.1) |
| [[HT-29 (line)]] | alt | 22.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -10.8) |
| [[J82 (line)]] | alt | 22.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -12.6) |
| [[SHP-77 (line)]] | alt | 38.9 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.252× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~2% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.291× (z -9.3) |
| [[SNU-423 (line)]] | alt | 10.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -15.7) |
| [[A549 (line)]] | wt | 14.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 10.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.198× (z -8.6) |
| [[BT-474 (line)]] | alt | 31.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -10.5) |
| [[H4 (line)]] | wt | 31.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -13.0) |
| [[HEC-1-A (line)]] | alt | 33.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.179× (z -14.3) |
| [[LS 180 (line)]] | wt | 30.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.225× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 24.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -15.4) |
| [[NCI-H1792 (line)]] | alt | 25.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -17.4) |
| [[Panc 03.27 (line)]] | alt | 17.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.245× (z -8.8) |
| [[RKO (line)]] | wt | 29.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.280× (z -8.7) |
| [[A-427 (line)]] | wt | 34.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.313× (z -9.8) |
| [[A498 (line)]] | wt | 7.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +14.1) | — |
| [[AN3 CA (line)]] | alt | 25.5 | 0 | 1 | — | [[Irinotecan (hydrochloride) (drug)]] 0.05 µM 0.0630× (z -9.4) |
| [[C-33 A (line)]] | alt | 25.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.212× (z -8.7) |
| [[COLO 205 (line)]] | alt | 14.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -11.1) |
| [[HCT15 (line)]] | alt | 33.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.193× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 22.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.105× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~2% of this change |
| [[hTERT-HPNE (line)]] | wt | 14.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 21.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -15.8) |
| [[SNU-1 (line)]] | wt | 21.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -9.1) |
| [[SW1417 (line)]] | alt | 30.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -11.1) |
| [[A-172 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.93 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11076), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHC2-AS1]] | +0.66 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[KCTD1]] | +0.62 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[LEMD3]] | +0.62 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[MSANTD2]] | +0.61 | +0.53 / +0.36 | both halves | 1e-04 |  |
| [[SAP30L-AS1]] | +0.60 | +0.45 / +0.37 | both halves | 7e-05 |  |
| [[GNG12-AS1]] | +0.59 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[ANXA2R-OT1]] | +0.58 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[ING2-DT]] | +0.58 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[POC1B-AS1]] | +0.58 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[SETD1B]] | +0.58 | +0.28 / +0.51 | both halves | 3e-04 |  |
| [[TLCD3A]] | +0.58 | +0.36 / +0.45 | both halves | 1e-04 |  |
| [[NUP50-DT]] | +0.57 | +0.51 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX8]] | -0.57 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[CYB5R1]] | -0.54 | -0.45 / -0.27 | both halves | 3e-04 |  |
| [[HNRNPDL]] | -0.54 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[TBC1D19]] | -0.53 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[EXOC3]] | -0.53 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[LMTK3]] | -0.53 | -0.41 / -0.28 | both halves | 3e-04 |  |
| [[CLINT1]] | -0.53 | -0.48 / -0.37 | both halves | 9e-05 |  |
| [[BBS5]] | -0.52 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[MAGT1]] | -0.52 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[SKIC3]] | -0.52 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[MKNK1]] | -0.51 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[ERP44]] | -0.51 | -0.45 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PTGR3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.573). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-3.4, 20.2); signed map (17.7, -5.4). **Vector** length 98.7, 24.5% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.1 | +14.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +5.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.4 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +2.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.0 | +2.1 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -5.7 | -22.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -20.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.2 | -0.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | -4.1 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.8 | -10.8 |
|  | [[EX229 (drug)]] 5 µM |  | -3.7 | -4.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.5 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -4.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.0 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | prostaglandin reductase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q22.3 — chr18:75,195,113-75,209,139 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC45594, PTGR-3; previously ZADH2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4Q0](https://www.uniprot.org/uniprotkb/Q8N4Q0) (Prostaglandin reductase 3):

> Functions as 15-oxo-prostaglandin 13-reductase and acts on 15-keto-PGE1, 15-keto-PGE2, 15-keto-PGE1-alpha and 15-keto-PGE2-alpha with highest efficiency towards 15-keto-PGE2-alpha. Overexpression represses transcriptional activity of PPARG and inhibits adipocyte differentiation.

**Summary**, from NCBI Gene [284273](https://www.ncbi.nlm.nih.gov/gene/284273):

> Predicted to enable 15-oxoprostaglandin 13-reductase [NAD(P)+] activity. Predicted to be involved in negative regulation of fat cell differentiation. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28697](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28697) · Entrez [284273](https://www.ncbi.nlm.nih.gov/gene/284273) · UniProt [Q8N4Q0](https://www.uniprot.org/uniprotkb/Q8N4Q0) · Ensembl [ENSG00000180011](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180011)

## Data

Gene col 11076: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11076); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11076, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11076]; `tensor/DDL_lfc|DDL_z.npy` [11076]; `embed/gene_vectors.npy` [11076]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11076 or target_col == 11076). Every well: [[PTGR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTGR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
