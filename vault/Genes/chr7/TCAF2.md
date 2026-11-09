---
symbol: "TCAF2"
type: "gene"
col: 9942
ensembl_id: "ENSG00000170379"
name: "TRPM8 channel associated factor 2"
location: "7q35"
module: 105
arm: "+"
pooled_cpm: 7.85
n_lines_expressing: 46
n_dd_up: 4
n_dd_down: 22
n_dd_up_clean: 3
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 5
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# TCAF2

*TRPM8 channel associated factor 2* — 7q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +6.1, q 6e-07, up in 16 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.348× (z -19.7, q 0e+00, down in 40 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AK2]] (+0.62, fdr 1e-05), [[FAM210A]] (+0.61, fdr 3e-05), [[GRPEL1]] (+0.61, fdr 1e-05); moves opposite to [[TACC2]] (-0.52, fdr 6e-05), [[FAM171A1]] (-0.46, fdr 1e-04), [[CPLANE1]] (-0.45, fdr 6e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[EPHA3]] → it (grade B ⚠); 5 go from it, the strongest it → [[CLCN5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9942.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.1 | 6e-07 | 16/40 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +4.4 | 0.003 | 9/43 (H4, A-172, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.005 | 13/44 (RKO, A498, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.34×** | +3.8 | 0.021 | 9/43 (LOX-IMVI, A498, …) | rises with dose |  |
| [[Roxadustat (drug)]] 5 µM |  | 1.28× | +3.1 | 0.17 | 9/41 (SNU-423, A-172, …) | rises with dose |  |
| [[Penfluridol (drug)]] 0.05 µM |  | 1.29× | +3.1 | 0.17 | 2/41 (RPMI-7951, HEC-1-A) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9942.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.348×** | -19.7 | 0e+00 | 40/42 (SK-MEL-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.318×** | -14.5 | 3e-45 | 30/35 (C32, SNU-423, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.451×** | -10.5 | 2e-23 | 27/37 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.518×** | -8.3 | 1e-14 | 26/43 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.534×** | -8.3 | 1e-14 | 24/44 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.605×** | -6.6 | 3e-09 | 19/42 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.609×** | -6.5 | 5e-09 | 21/42 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.710×** | -6.4 | 1e-08 | 16/44 (J82, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.619×** | -6.3 | 2e-08 | 21/42 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.627×** | -6.2 | 4e-08 | 17/44 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.677×** | -5.2 | 1e-05 | 16/41 (C32, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.680×** | -5.1 | 2e-05 | 11/43 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.680×** | -5.1 | 2e-05 | 14/42 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.717×** | -4.4 | 4e-04 | 17/30 (CFPAC-1, SK-MEL-2, …) | two highest doses | composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.539×** | -4.3 | 8e-04 | 9/38 (Panc 03.27, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[8-Hydroxyquinoline (drug)]] 5 µM |  | **0.815×** | -3.8 | 0.004 | 10/44 (KATO III, NCI-H1573, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.818×** | -3.8 | 0.005 | 13/44 (PANC-1, BT-474, …) | rises with dose | position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | 0.838× | -3.3 | 0.028 | 3/44 (HepG2/C3A, NCI-H460, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.621×** | -3.3 | 0.028 | 9/34 (NCI-H460, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9942. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 25.5 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.249× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 16.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0536× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.312× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 4.71 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -12.1) |
| [[SK-MEL-2 (line)]] | alt | 24.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0878× (z -20.5) |
| [[C32 (line)]] | wt | 52.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0696× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.355× (z -8.9) |
| [[A-172 (line)]] | wt | 5.52 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -9.0) |
| [[HCT15 (line)]] | alt | 12.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0784× (z -13.8) |
| [[J82 (line)]] | alt | 8.61 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.274× (z -9.3) |
| [[RKO (line)]] | wt | 5.56 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0523× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Canagliflozin (hemihydrate) (drug)]] 0.05 µM 0.0530× (z -10.3) |
| [[SNU-423 (line)]] | alt | 10.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0777× (z -16.9) |
| [[BT-474 (line)]] | alt | 9.79 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0579× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 6.91 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 7.68 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 5.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 10.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 6.33 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0467× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SW480 (line)]] | alt | 5.71 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0776× (z -14.2) |
| [[A-427 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9942), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AK2]] | +0.62 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[FAM210A]] | +0.61 | +0.72 / +0.46 | both halves | 3e-05 |  |
| [[GRPEL1]] | +0.61 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[IPMK]] | +0.57 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[USP37]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[BMT2]] | +0.56 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[PPFIA4]] | +0.56 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[AK4]] | +0.55 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[MAP2K1]] | +0.55 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[UBE2O]] | +0.54 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[POM121C]] | +0.54 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[SCAND2P]] | +0.54 | +0.55 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TACC2]] | -0.52 | -0.60 / -0.39 | both halves | 6e-05 |  |
| [[FAM171A1]] | -0.46 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[CPLANE1]] | -0.45 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[CLCN5]] | -0.44 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[DIP2B]] | -0.43 | -0.26 / -0.43 | both halves | 4e-04 |  |
| [[PPFIBP2]] | -0.43 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[PPP1R9A]] | -0.41 | -0.39 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA3]] | B | EPHA3 activity raises TCAF2's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 1.92× lower at baseline in the lines without EPHA3 | 0.010 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491 |
| [[MLLT3]] | B | MLLT3 activity raises TCAF2's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 2.16× lower at baseline in the lines without MLLT3 | 0.016 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |
| [[NRN1]] | B | NRN1 activity raises TCAF2's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.84× lower at baseline in the lines without NRN1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[LRAT]] | B | LRAT activity raises TCAF2's level | lines that do not express LRAT (30) vs lines expressing it (20) | 1.89× lower at baseline in the lines without LRAT | 0.042 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, NR0B1, IL6 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLCN5]] | C | TCAF2 activity lowers CLCN5's level | lines that do not express TCAF2 (4) vs lines expressing it (46) | 2.51× higher at baseline in the lines without TCAF2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[ANKZF1]] | C | TCAF2 activity raises ANKZF1's level | lines that do not express TCAF2 (4) vs lines expressing it (46) | 1.46× lower at baseline in the lines without TCAF2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[UBE2O]] | C | [[SLC2A1]], TCAF2 activity raises UBE2O's level | lines that do not express SLC2A1, TCAF2 (4) vs lines expressing them (46) | 1.67× lower at baseline in the lines without SLC2A1, TCAF2 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, NIBAN2, IER3; maybe low, not absent; co-absent genes |
| [[GLRX]] | C | TCAF2 activity raises GLRX's level | lines that do not express TCAF2 (4) vs lines expressing it (46) | 4.43× lower at baseline in the lines without TCAF2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[MAP2K1]] | C | TCAF2 activity raises MAP2K1's level | lines that do not express TCAF2 (4) vs lines expressing it (46) | 1.76× lower at baseline in the lines without TCAF2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.638). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.0, -19.7); signed map (-41.2, 26.3). **Vector** length 73.3, 13.1% of its response variance represented; |z| ≥ 3 in 933 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +1.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +6.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +2.4 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +4.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -19.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.4 | -14.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.2 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.0 | -8.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.2 | -3.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.6 | -3.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -5.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | TRPM8 channel associated factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q35 — chr7:143,620,952-143,730,410 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40722, GATD9B; previously FAM139A, FAM115C |
| Gene groups (HGNC) | Glutamine amidotransferase class 1 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NFQ2](https://www.uniprot.org/uniprotkb/A6NFQ2) (TRPM8 channel-associated factor 2):

> [Isoform 2]: Negatively regulates the plasma membrane cation channel TRPM8 activity. Involved in the recruitment of TRPM8 to the cell surface. Promotes prostate cancer cell migration stimulation in a TRPM8-dependent manner.

**Summary**, from NCBI Gene [285966](https://www.ncbi.nlm.nih.gov/gene/285966):

> Enables transmembrane transporter binding activity. Involved in negative regulation of anion channel activity; positive regulation of cell migration; and positive regulation of protein targeting to membrane. Located in cell junction and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26878](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26878) · Entrez [285966](https://www.ncbi.nlm.nih.gov/gene/285966) · UniProt [A6NFQ2](https://www.uniprot.org/uniprotkb/A6NFQ2) · Ensembl [ENSG00000170379](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170379)

## Data

Gene col 9942: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9942); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9942, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9942]; `tensor/DDL_lfc|DDL_z.npy` [9942]; `embed/gene_vectors.npy` [9942]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9942 or target_col == 9942). Every well: [[TCAF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCAF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
