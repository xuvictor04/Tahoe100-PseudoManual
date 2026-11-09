---
symbol: "METTL3"
type: "gene"
col: 9195
ensembl_id: "ENSG00000165819"
name: "methyltransferase 3, N6-adenosine-methyltransferase complex catalytic subunit"
location: "14q11.2"
module: 18
arm: "+"
pooled_cpm: 17.89
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# METTL3

*methyltransferase 3, N6-adenosine-methyltransferase complex catalytic subunit* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.69× (z +10.3, q 5e-22, up in 36 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.65× (z +9.8, q 3e-20, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.710× (z -9.6, q 7e-19, down in 32 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.801× (z -4.4, q 0.003, down in 16 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.244×; ⚠ cell-cycle shift, explains ~25% of this change); [[Allantoin (drug)]] 0.5 µM in 1 line (Hs 766T 0.237×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.499×; ⚠ cell-cycle shift, explains ~26% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS25]] (+0.72, fdr 9e-06), [[RFT1]] (+0.70, fdr 7e-06), [[ANAPC1]] (+0.69, fdr 7e-06); moves opposite to [[HES1]] (-0.67, fdr 1e-05), [[TMEM205]] (-0.65, fdr 8e-06), [[GABARAP]] (-0.63, fdr 1e-05, ⚠ GABARAP in the vector space only through flagged drug-doses), [[KLF2]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DUXAP8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9195.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.69×** | +10.3 | 5e-22 | 36/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.65×** | +9.8 | 3e-20 | 37/47 (SW480, KATO III, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +7.4 | 2e-11 | 29/47 (NCI-H1573, LS 180, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +7.2 | 7e-11 | 17/29 (HS-578T, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +7.2 | 7e-11 | 23/43 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +5.8 | 6e-07 | 19/47 (Panc 03.27, SHP-77, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.33×** | +5.6 | 2e-06 | 15/46 (NCI-H2030, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +5.5 | 2e-06 | 18/45 (LoVo, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.33×** | +5.3 | 7e-06 | 21/46 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.30×** | +5.2 | 1e-05 | 15/46 (CFPAC-1, NCI-H1792, …) | two highest doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.62×** | +5.0 | 4e-05 | 12/46 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.31×** | +4.9 | 4e-05 | 15/37 (NCI-H2030, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.19× | +4.8 | 7e-05 | 18/47 (NCI-H1792, NCI-H2030, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.29×** | +4.6 | 1e-04 | 17/48 (HT-29, NCI-H2347, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.18× | +4.6 | 2e-04 | 16/48 (NCI-H1792, CFPAC-1, …) | top dose only | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.54×** | +4.4 | 4e-04 | 10/47 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.003 | 8/46 (LS 180, A-427, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.007 | 9/43 (PANC-1, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.008 | 9/45 (CFPAC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.016 | 6/48 (NCI-H1573, MIA PaCa-2, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.034 | 9/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.036 | 4/47 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.036 | 3/48 (SW480, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.32×** | +2.8 | 0.095 | 7/44 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9195.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.244×; ⚠ cell-cycle shift, explains ~25% of this change); [[Allantoin (drug)]] 0.5 µM in 1 line (Hs 766T 0.237×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.499×; ⚠ cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.710×** | -9.6 | 7e-19 | 32/47 (NCI-H460, J82, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.801×** | -4.4 | 0.003 | 16/46 (COLO 205, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.813×** | -3.9 | 0.016 | 19/47 (SW 1271, COLO 205, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.718×** | -3.4 | 0.088 | 6/48 (A-427, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.891× | -3.3 | 0.13 | 11/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.852× | -3.2 | 0.14 | 8/48 (RPMI-7951, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | 0.874× | -3.1 | 0.14 | 10/48 (CHP-212, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9195. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 17.6 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.237× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -9.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -12.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9195), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS25]] | +0.72 | +0.57 / +0.74 | both halves | 9e-06 |  |
| [[RFT1]] | +0.70 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[ANAPC1]] | +0.69 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[AHSA1]] | +0.67 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[UBE2G2]] | +0.66 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[C1orf216]] | +0.66 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[DTD2]] | +0.65 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[IRAK1]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ADAT2]] | +0.63 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[RPE]] | +0.63 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[SORD]] | +0.63 | +0.62 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[RPUSD4]] | +0.63 | +0.61 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HES1]] | -0.67 | -0.57 / -0.65 | both halves | 1e-05 |  |
| [[TMEM205]] | -0.65 | -0.60 / -0.57 | both halves | 8e-06 |  |
| [[GABARAP]] ⚠ | -0.63 | -0.62 / -0.56 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[KLF2]] | -0.61 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[ANKRD12]] | -0.61 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[DBP]] | -0.60 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[LMNA]] | -0.59 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[MTHFR]] | -0.58 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[HDAC5]] | -0.58 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[GPX4]] | -0.57 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[KDM5B]] | -0.56 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[CCDC148]] | -0.56 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[CDKN2D]] | -0.54 | -0.50 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUXAP8]] | B | DUXAP8 activity raises METTL3's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.36× lower at baseline in the lines without DUXAP8 | 0.047 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.648). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-11.9, -31.2); signed map (-2.7, -51.7). **Vector** length 77.6, 13.5% of its response variance represented; |z| ≥ 3 in 850 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.8 | +10.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.9 | +7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.9 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +5.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | +4.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.3 | -9.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.0 | -3.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.1 | -3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.7 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +0.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.5 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -0.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | methyltransferase 3, N6-adenosine-methyltransferase complex catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:21,498,133-21,511,342 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Spo8, M6A, MT-A70 |
| Gene groups (HGNC) | m6A methyltransferase complex; 7BS N6-adenosine DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 2 pathways, smallest: Processing of Capped Intron-Containing Pre-mRNA; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86U44](https://www.uniprot.org/uniprotkb/Q86U44) (N(6)-adenosine-methyltransferase catalytic subunit METTL3):

> The METTL3-METTL14 heterodimer forms a N6-methyltransferase complex that methylates adenosine residues at the N(6) position of some RNAs and regulates various processes such as the circadian clock, differentiation of embryonic and hematopoietic stem cells, cortical neurogenesis, response to DNA damage, differentiation of T-cells and primary miRNA processing. In the heterodimer formed with METTL14, METTL3 constitutes the catalytic core. N6-methyladenosine (m6A), which takes place at the …

**Summary**, from NCBI Gene [56339](https://www.ncbi.nlm.nih.gov/gene/56339):

> This gene encodes the 70 kDa subunit of MT-A which is part of N6-adenosine-methyltransferase. This enzyme is involved in the posttranscriptional methylation of internal adenosine residues in eukaryotic mRNAs, forming N6-methyladenosine. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17563](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17563) · Entrez [56339](https://www.ncbi.nlm.nih.gov/gene/56339) · UniProt [Q86U44](https://www.uniprot.org/uniprotkb/Q86U44) · Ensembl [ENSG00000165819](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165819)

## Data

Gene col 9195: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9195); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9195, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9195]; `tensor/DDL_lfc|DDL_z.npy` [9195]; `embed/gene_vectors.npy` [9195]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9195 or target_col == 9195). Every well: [[METTL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
