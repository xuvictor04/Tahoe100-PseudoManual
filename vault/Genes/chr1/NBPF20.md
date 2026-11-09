---
symbol: "NBPF20"
type: "gene"
col: 8586
ensembl_id: "ENSG00000162825"
name: "NBPF member 20"
location: "1q21.1"
module: 59
arm: "-"
pooled_cpm: 14.07
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 2
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# NBPF20

*NBPF member 20* — 1q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.66× (z +7.2, q 4e-10, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 0.527× (z -4.8, q 9e-04, down in 17 of 42 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 0.770× (z -4.5, q 0.002, down in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H460 0.139×, A549 0.0732×, RKO 0.200×, NCI-H23 0.244×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H1573 0.148×, KATO III 0.179×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.186×, SW1417 0.176×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.169×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBPF9]] (+0.75, fdr 7e-06), [[NBPF8]] (+0.68, fdr 7e-06), [[NBPF15]] (+0.68, fdr 7e-06); moves opposite to [[CHASERR]] (-0.59, fdr 1e-05), [[CDKN1B]] (-0.58, fdr 1e-05), [[CDKN2C]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ZEB1]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Belzutifan (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8586.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +7.2 | 4e-10 | 30/47 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.60×** | +6.7 | 5e-09 | 26/47 (AsPC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +6.3 | 4e-08 | 25/47 (NCI-H2347, LS 180, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +6.2 | 8e-08 | 23/47 (NCI-H2347, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +6.0 | 3e-07 | 23/47 (CFPAC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.50×** | +5.8 | 5e-07 | 23/47 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +5.8 | 5e-07 | 22/47 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +5.1 | 2e-05 | 17/47 (SW480, A498, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +5.1 | 2e-05 | 21/47 (A-172, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.41×** | +4.9 | 7e-05 | 15/47 (NCI-H460, SW480, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.39×** | +4.7 | 1e-04 | 20/46 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +4.5 | 3e-04 | 16/48 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.33×** | +4.1 | 0.002 | 9/47 (NCI-H460, SW 900, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +4.0 | 0.002 | 13/45 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +3.9 | 0.004 | 5/48 (HOP62, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.004 | 17/47 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.009 | 13/47 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.63×** | +3.6 | 0.009 | 7/46 (A-427, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8586.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H460 0.139×, A549 0.0732×, RKO 0.200×, NCI-H23 0.244×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H1573 0.148×, KATO III 0.179×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.186×, SW1417 0.176×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.169×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.527×** | -4.8 | 9e-04 | 17/42 (SK-MEL-2, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.770×** | -4.5 | 0.002 | 16/48 (MIA PaCa-2, RKO, …) | two highest doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.783× | -3.4 | 0.14 | 15/47 (RKO, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.05 µM |  | 0.786× | -3.2 | 0.20 | 16/44 (AsPC-1, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8586. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 17.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.169× (z -10.4) |
| [[A-427 (line)]] | wt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[A549 (line)]] | wt | 15.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0732× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[KATO III (line)]] | alt | 8.78 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.179× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 7.29 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.138× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 9.57 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.186× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 35.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[NCI-H460 (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[RKO (line)]] | wt | 52.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[SW1417 (line)]] | alt | 9.03 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8586), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF9]] | +0.75 | +0.74 / +0.74 | both halves | 7e-06 | same gene group |
| [[NBPF8]] | +0.68 | +0.62 / +0.66 | both halves | 7e-06 | same gene group |
| [[NBPF15]] | +0.68 | +0.64 / +0.66 | both halves | 7e-06 | same gene group |
| [[TTL]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[ZNF8]] | +0.64 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[SMAGP]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[CUTC]] | +0.64 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[UGGT2]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[ANKS6]] | +0.62 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[RUSC2]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[PEA15]] | +0.61 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[PINX1]] | +0.61 | +0.60 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHASERR]] | -0.59 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[CDKN1B]] | -0.58 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[CDKN2C]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[EFNA1]] | -0.57 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[DBP]] | -0.57 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[TRA2A]] | -0.57 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[CCDC115]] | -0.56 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[HCFC1R1]] | -0.56 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[ATP5IF1]] | -0.56 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.56 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[CTNND1]] | -0.54 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[MBIP]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZEB1]] | B | ZEB1 activity raises NBPF20's level | lines that do not express ZEB1 (9) vs lines expressing it (41) | 2.02× lower at baseline in the lines without ZEB1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ITGA10, LIX1L, BRSK1 |
| [[RFLNB]] | B | RFLNB activity raises NBPF20's level | lines that do not express RFLNB (16) vs lines expressing it (34) | 1.69× lower at baseline in the lines without RFLNB | 0.024 | ⚠ within organs, on part of the lines; also absent: FSD1, B4GALNT1, ANTXR1 |
| [[PARVB]] | B | PARVB activity raises NBPF20's level | lines that do not express PARVB (13) vs lines expressing it (37) | 1.62× lower at baseline in the lines without PARVB | 0.037 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |
| [[CXXC5]] | B | CXXC5 activity lowers NBPF20's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 1.64× higher at baseline in the lines without CXXC5 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[ADAM23]] | B | ADAM23 activity raises NBPF20's level | lines that do not express ADAM23 (26) vs lines expressing it (24) | 1.52× lower at baseline in the lines without ADAM23 | 0.057 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, GALNT13, CNRIP1 |
| [[EFNA1]] | B | EFNA1 activity lowers NBPF20's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 1.60× higher at baseline in the lines without EFNA1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[LDLRAD3]] | B | LDLRAD3 activity raises NBPF20's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 1.56× lower at baseline in the lines without LDLRAD3 | 0.078 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Belzutifan (drug)]] 5 µM | C | NBPF20's natural level raises the cells' numbers under Belzutifan 5 µM (protects the cells) | NBPF20's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.60 | 0.461 over the table, 0.076 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **-** arm (projection on the module's main direction -0.575). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (20.9, -25.0); signed map (-17.4, 47.1). **Vector** length 80.7, 14.6% of its response variance represented; |z| ≥ 3 in 1,079 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.1 | +7.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +5.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.8 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | -1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.7 | +4.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.5 | +3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +4.9 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.9 | -4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +0.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -4.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | NBPF member 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.1 — chr1:145,289,900-145,425,603 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | NBPF members |
| Matched by | ensembl_id |

UniProt [P0DPF2](https://www.uniprot.org/uniprotkb/P0DPF2) carries no function annotation.

**Summary**, from NCBI Gene [100288142](https://www.ncbi.nlm.nih.gov/gene/100288142):

> This gene is a member of the neuroblastoma breakpoint family (NBPF) which consists of dozens of recently duplicated genes primarily located in segmental duplications on human chromosome 1. This gene family has experienced its greatest expansion within the human lineage and has expanded, to a lesser extent, among primates in general. Members of this gene family are characterized by tandemly repeated copies of DUF1220 protein domains. Gene copy number variations in the human chromosomal region …

**Accessions** — [HGNC:32000](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32000) · Entrez [100288142](https://www.ncbi.nlm.nih.gov/gene/100288142) · UniProt [P0DPF2](https://www.uniprot.org/uniprotkb/P0DPF2) · Ensembl [ENSG00000162825](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162825)

## Data

Gene col 8586: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8586); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8586, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8586]; `tensor/DDL_lfc|DDL_z.npy` [8586]; `embed/gene_vectors.npy` [8586]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8586 or target_col == 8586). Every well: [[NBPF20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NBPF20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
