---
symbol: "SRC"
type: "gene"
col: 12347
ensembl_id: "ENSG00000197122"
name: "SRC proto-oncogene, non-receptor tyrosine kinase"
location: "20q11.23"
module: 102
arm: "+"
pooled_cpm: 33.84
n_lines_expressing: 48
n_dd_up: 1
n_dd_down: 16
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 12
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# SRC

*SRC proto-oncogene, non-receptor tyrosine kinase* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.26× (z +4.0, q 0.037, up in 16 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 2.94×; ⚠ cell-cycle shift, explains ~55% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A498 3.77×); [[Harringtonine (drug)]] 5 µM in 1 line (A498 2.74×; ⚠ cell-cycle shift, explains ~53% of this change).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.241× (z -24.4, q 0e+00, down in 44 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBPMS2]] (+0.57, fdr 4e-05), [[ZFTA]] (+0.57, fdr 6e-05), [[RAB15]] (+0.56, fdr 1e-05); moves opposite to [[DAD1]] (-0.53, fdr 9e-05), [[GPN3]] (-0.51, fdr 8e-05), [[UFSP2]] (-0.51, fdr 3e-05).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PCSK6]] → it (grade B ⚠); 12 go from it, the strongest it → [[NUP37]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12347.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 2.94×; ⚠ cell-cycle shift, explains ~55% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A498 3.77×); [[Harringtonine (drug)]] 5 µM in 1 line (A498 2.74×; ⚠ cell-cycle shift, explains ~53% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.037 | 16/45 (HEC-1-A, HCT15, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Cytarabine (drug)]] 5 µM |  | 1.23× | +3.4 | 0.13 | 9/45 (LoVo, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.23× | +3.4 | 0.13 | 14/45 (J82, NCI-H23, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.27 | 8/46 (RPMI-7951, A498, …) | inconsistent across doses |  |
| [[Naproxen (drug)]] 0.05 µM |  | 1.21× | +3.0 | 0.27 | 8/44 (RKO, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12347.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.241×** | -24.4 | 0e+00 | 44/46 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.249×** | -23.8 | 0e+00 | 45/46 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.275×** | -22.1 | 0e+00 | 44/45 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.469×** | -13.0 | 2e-36 | 41/46 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.574×** | -9.5 | 2e-19 | 32/41 (A-172, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.682×** | -9.3 | 2e-18 | 27/44 (HT-29, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.641×** | -7.6 | 2e-12 | 31/44 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.752×** | -6.9 | 3e-10 | 22/45 (NCI-H460, LS 180, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.481×** | -6.6 | 3e-09 | 30/46 (LS 180, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **0.682×** | -6.3 | 2e-08 | 18/32 (A-172, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.711×** | -5.8 | 3e-07 | 22/45 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.749×** | -4.8 | 9e-05 | 23/46 (LoVo, COLO 205, …) | rises with dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.617×** | -4.3 | 6e-04 | 17/45 (NCI-H1792, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.628×** | -4.2 | 0.001 | 19/44 (J82, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.805×** | -3.6 | 0.014 | 21/45 (A-427, C32, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.818×** | -3.4 | 0.020 | 13/46 (NCI-H2347, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12347. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 91.7 | 4 (3 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +18.5) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.77× (z +16.1) | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -17.8) |
| [[HT-29 (line)]] | alt | 77.0 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0928× (z -21.5) |
| [[NCI-H460 (line)]] | wt | 61.0 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -19.1) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.185× (z -16.2) |
| [[LoVo (line)]] | wt | 21.1 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -17.7) |
| [[A-172 (line)]] | wt | 29.3 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0997× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.241× (z -12.2) |
| [[COLO 205 (line)]] | alt | 49.0 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -12.1) |
| [[Hs 766T (line)]] | wt | 75.1 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.119× (z -16.8) |
| [[J82 (line)]] | alt | 30.6 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.224× (z -11.9) |
| [[LS 180 (line)]] | wt | 36.3 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -15.7) |
| [[A-427 (line)]] | wt | 20.8 | 0 | 4 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.240× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 39.4 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.243× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 33.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -12.4) |
| [[KATO III (line)]] | alt | 44.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.111× (z -18.8) |
| [[RKO (line)]] | wt | 44.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.162× (z -15.0) |
| [[SK-MEL-2 (line)]] | alt | 28.9 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.122× (z -13.4) |
| [[SW480 (line)]] | alt | 12.8 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.197× (z -13.1) |
| [[A549 (line)]] | wt | 75.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -15.6) |
| [[C32 (line)]] | wt | 47.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.112× (z -15.6) |
| [[HEC-1-A (line)]] | alt | 34.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -14.6) |
| [[HepG2_C3A (line)]] | wt | 57.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.251× (z -10.7) |
| [[HOP62 (line)]] | alt | 21.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 32.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.116× (z -16.6) |
| [[NCI-H1792 (line)]] | alt | 53.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.232× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 35.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -12.8) |
| [[NCI-H2347 (line)]] | alt | 26.6 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.276× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 32.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -12.9) |
| [[SW1417 (line)]] | alt | 43.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.245× (z -13.3) |
| [[C-33 A (line)]] | alt | 24.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -10.5) |
| [[HS-578T (line)]] | alt | 16.5 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.194× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 23.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.216× (z -10.7) |
| [[PANC-1 (line)]] | alt | 12.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.251× (z -11.4) |
| [[SNU-423 (line)]] | alt | 14.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -9.6) |
| [[AN3 CA (line)]] | alt | 42.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[CHP-212 (line)]] | wt | 22.7 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM 0.0741× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 17.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -8.9) |
| [[BT-474 (line)]] | alt | 6.83 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.04 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12347), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBPMS2]] | +0.57 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[ZFTA]] | +0.57 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[RAB15]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[MSI1]] | +0.55 | +0.33 / +0.58 | both halves | 1e-04 | pathway: Signaling by ROBO receptors |
| [[SHROOM1]] | +0.55 | +0.37 / +0.41 | both halves | 8e-05 |  |
| [[ELF4]] | +0.52 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[DTX2P1]] | +0.52 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[CCDC136]] | +0.51 | +0.40 / +0.37 | both halves | 7e-05 |  |
| [[TMCO4]] | +0.50 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[CPNE2]] | +0.50 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[STRN4]] | +0.48 | +0.45 / +0.32 | both halves | 2e-04 |  |
| [[HTR1D]] | +0.48 | +0.30 / +0.51 | both halves | 2e-04 | pathway: G alpha (i) signalling events; STRING 535 |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAD1]] | -0.53 | -0.48 / -0.36 | both halves | 9e-05 | pathway: Adherens junctions interactions |
| [[GPN3]] | -0.51 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[UFSP2]] | -0.51 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[POT1]] | -0.50 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[PIBF1]] | -0.50 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[WDPCP]] | -0.49 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[CFDP1]] | -0.48 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[PKN2]] | -0.47 | -0.49 / -0.37 | both halves | 7e-05 | pathway: RHO GTPase Effectors |
| [[TRIQK]] | -0.47 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[MBD5]] | -0.46 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[LTN1]] | -0.46 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[SKIC3]] | -0.46 | -0.26 / -0.43 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCSK6]] | B | PCSK6 activity raises SRC's level | lines that do not express PCSK6 (21) vs lines expressing it (29) | 1.46× lower at baseline in the lines without PCSK6 | 0.082 | ⚠ within organs, on part of the lines; also absent: BTNL9, CYP4F12, LINC02964 |
| [[C12orf56]] | B | C12orf56 activity lowers SRC's level | lines that do not express C12orf56 (11) vs lines expressing it (39) | 1.24× higher at baseline in the lines without C12orf56 | 0.084 | ⚠ within organs, on part of the lines; also absent: DOC2A, GPR63, STC2; maybe low, not absent |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUP37]] | B | SRC activity lowers NUP37's level | compounds that target SRC: 2 of 3 raise it (NG25, Ponatinib) | 67% of the class's compounds vs 0.8% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[SFN]] | B | SRC activity raises SFN's level | compounds that target SRC: 2 of 3 lower it (NG25, Ponatinib) | 67% of the class's compounds vs 0.8% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[ZC3H12A]] | B | SRC activity raises ZC3H12A's level | compounds that target SRC: 2 of 3 lower it (NG25, Ponatinib) | 67% of the class's compounds vs 0.8% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[CDKN2B]] | B | SRC activity raises CDKN2B's level | compounds that target SRC: 2 of 3 lower it (NG25, Ponatinib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[CTDSPL]] | B | SRC activity lowers CTDSPL's level | compounds that target SRC: 2 of 3 raise it (NG25, Ponatinib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[ERCC5]] | B | SRC activity lowers ERCC5's level | compounds that target SRC: 2 of 3 raise it (NG25, Ponatinib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[GCH1]] | B | SRC activity raises GCH1's level | compounds that target SRC: 2 of 3 lower it (NG25, Ponatinib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[GSG1L]] | B | SRC activity raises GSG1L's level | compounds that target SRC: 2 of 3 lower it (NG25, Ponatinib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[IRGQ]] | B | SRC activity raises IRGQ's level | compounds that target SRC: 2 of 3 lower it (NG25, Ponatinib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[KRTAP5-AS1]] | B | SRC activity raises KRTAP5-AS1's level | compounds that target SRC: 2 of 3 lower it (NG25, Ponatinib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[MDFIC]] | B | SRC activity lowers MDFIC's level | compounds that target SRC: 2 of 3 raise it (NG25, Ponatinib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[RBM41]] | B | SRC activity lowers RBM41's level | compounds that target SRC: 2 of 3 raise it (NG25, Ponatinib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.456). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (4.0, 33.4); signed map (41.5, -1.7). **Vector** length 80.1, 16.7% of its response variance represented; |z| ≥ 3 in 1,051 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.3 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.5 | +4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | -9.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +0.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | -1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +0.9 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.6 | -4.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.6 | -22.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.3 | -23.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | +1.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -0.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.2 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.6 | -1.2 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.6 | -0.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | SRC proto-oncogene, non-receptor tyrosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:37,344,685-37,406,050 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ASV, c-src; previously SRC1 |
| Gene groups (HGNC) | SH2 domain containing; Src family tyrosine kinases; SH3 domain containing |
| Hallmark sets | COMPLEMENT, APICAL_JUNCTION |
| Reactome | 162 pathways, smallest: Regulation of gap junction activity; Activated NTRK3 signals through PI3K; FCGR activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P12931](https://www.uniprot.org/uniprotkb/P12931) (Proto-oncogene tyrosine-protein kinase Src):

> Non-receptor protein tyrosine kinase which is activated following engagement of many different classes of cellular receptors including immune response receptors, integrins and other adhesion receptors, receptor protein tyrosine kinases, G protein-coupled receptors as well as cytokine receptors. Participates in signaling pathways that control a diverse spectrum of biological activities including gene transcription, immune response, cell adhesion, cell cycle progression, apoptosis, migration, and …

**Summary**, from NCBI Gene [6714](https://www.ncbi.nlm.nih.gov/gene/6714):

> This gene is highly similar to the v-src gene of Rous sarcoma virus. This proto-oncogene may play a role in the regulation of embryonic development and cell growth. The protein encoded by this gene is a tyrosine-protein kinase whose activity can be inhibited by phosphorylation by c-SRC kinase. Mutations in this gene could be involved in the malignant progression of colon cancer. Two transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11283](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11283) · Entrez [6714](https://www.ncbi.nlm.nih.gov/gene/6714) · UniProt [P12931](https://www.uniprot.org/uniprotkb/P12931) · Ensembl [ENSG00000197122](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197122)

## Data

Gene col 12347: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12347); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12347, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12347]; `tensor/DDL_lfc|DDL_z.npy` [12347]; `embed/gene_vectors.npy` [12347]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12347 or target_col == 12347). Every well: [[SRC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
