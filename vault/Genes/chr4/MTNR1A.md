---
symbol: "MTNR1A"
type: "gene"
col: 9648
ensembl_id: "ENSG00000168412"
name: "melatonin receptor 1A"
location: "4q35.2"
module: 47
arm: "+"
pooled_cpm: 2.84
n_lines_expressing: 43
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 8
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# MTNR1A

*melatonin receptor 1A* — 4q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 12.3× (z +24.6, q 0e+00, up in 30 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Benproperine (phosphate) (drug)]] 5 µM: 0.533× (z -4.1, q 0.019, down in 12 of 30 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (LoVo 0.0450×, KATO III 0.0448×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (LoVo 0.0460×); [[Digitoxin (drug)]] 5 µM in 1 line (LoVo 0.0617×; ⚠ toxic; transcription drop); [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0579×); [[Vandetanib (drug)]] 5 µM in 1 line (KATO III 0.0782×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCUBE2]] (+0.72, fdr 7e-06), [[SSUH2]] (+0.72, fdr 7e-06), [[C3orf20]] (+0.71, fdr 7e-06); moves opposite to [[CCZ1B]] (-0.65, fdr 7e-06), [[SEC11A]] (-0.62, fdr 1e-05), [[PMS2P3-1]] (-0.62, fdr 1e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PPP1R1C]] → it (grade B ⚠); 8 go from it, the strongest it → [[FAT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9648.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **12.3×** | +24.6 | 0e+00 | 30/31 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **7.72×** | +14.2 | 3e-43 | 28/32 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **4.63×** | +10.1 | 7e-22 | 27/34 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.04×** | +7.4 | 3e-11 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.92×** | +6.9 | 5e-10 | 21/35 (A498, KATO III, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.87×** | +6.2 | 7e-08 | 10/38 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Filgotinib (drug)]] 5 µM |  | **2.22×** | +5.6 | 2e-06 | 19/39 (LoVo, A498, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **2.11×** | +5.2 | 1e-05 | 10/33 (SW480, SW 900, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.45×** | +4.8 | 1e-04 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.79×** | +4.0 | 0.003 | 16/37 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.67×** | +3.6 | 0.019 | 5/39 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.022 | 6/38 (SW480, Panc 03.27, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.59×** | +3.2 | 0.052 | 12/37 (C-33 A, SW 900, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.55×** | +3.0 | 0.088 | 1/13 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.55×** | +3.0 | 0.088 | 8/36 (NCI-H460, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.090 | 5/39 (HCT15, A498, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **2.27×** | +3.0 | 0.095 | 1/25 (SW480) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9648.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (LoVo 0.0450×, KATO III 0.0448×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (LoVo 0.0460×); [[Digitoxin (drug)]] 5 µM in 1 line (LoVo 0.0617×; ⚠ toxic; transcription drop); [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0579×); [[Vandetanib (drug)]] 5 µM in 1 line (KATO III 0.0782×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Benproperine (phosphate) (drug)]] 5 µM |  | **0.533×** | -4.1 | 0.019 | 12/30 (HEC-1-A, J82, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.734× | -3.0 | 0.34 | 8/36 (SW 900, RPMI-7951, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.565× | -3.0 | 0.34 | 5/39 (A-427, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9648. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 9.70 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.89× (z +9.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0450× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Bosentan (hydrate) (drug)]] 5 µM 0.0460× (z -10.7) |
| [[KATO III (line)]] | alt | 10.2 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0448× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Vandetanib (drug)]] 5 µM 0.0782× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 4.52 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 85.3× (z +17.6) | — |
| [[PANC-1 (line)]] | alt | 1.01 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 89.3× (z +16.3) | — |
| [[A498 (line)]] | wt | 3.59 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.8× (z +12.5) | — |
| [[HS-578T (line)]] | alt | 4.92 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 38.9× (z +12.9) | — |
| [[NCI-H460 (line)]] | wt | 1.08 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 43.1× (z +12.5) | — |
| [[A-172 (line)]] | wt | 0.898 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 69.8× (z +10.0) | — |
| [[A549 (line)]] | wt | 1.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 62.0× (z +10.8) | — |
| [[CFPAC-1 (line)]] | alt | 4.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.8× (z +17.6) | — |
| [[COLO 205 (line)]] | alt | 4.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.8× (z +14.1) | — |
| [[HOP62 (line)]] | alt | 1.33 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 165× (z +13.1) | — |
| [[hTERT-HPNE (line)]] | wt | 2.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 65.8× (z +10.8) | — |
| [[J82 (line)]] | alt | 1.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.0× (z +9.9) | — |
| [[NCI-H2030 (line)]] | alt | 4.26 | 0 | 1 | — | [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM 0.0579× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 3.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.1× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 4.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.9× (z +9.7) | — |
| [[SW48 (line)]] | wt | 9.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +10.9) | — |
| [[A-427 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.916 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.725 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.801 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.668 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.867 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.724 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.843 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.980 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.429 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.773 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9648), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCUBE2]] | +0.72 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[SSUH2]] | +0.72 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.71 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[SLC22A1]] | +0.71 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[TIAM2]] | +0.70 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[LINC01934]] | +0.69 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[LINC00486]] | +0.69 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[MMP25]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[PHEX]] | +0.69 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[KRT86]] | +0.69 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[SLC2A9]] | +0.69 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[NANOS3]] | +0.68 | +0.73 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCZ1B]] | -0.65 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[SEC11A]] | -0.62 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | -0.62 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[CCZ1]] | -0.61 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[SLC9A6]] | -0.60 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[GINM1]] | -0.60 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[PRKRA]] | -0.59 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[WHAMMP1]] | -0.59 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[ATP6AP2]] | -0.59 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[SMARCD2]] | -0.58 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[NUDT2]] | -0.58 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[IFI27L1]] | -0.58 | -0.57 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R1C]] | B | PPP1R1C activity raises MTNR1A's level | lines that do not express PPP1R1C (13) vs lines expressing it (37) | 1.58× lower at baseline in the lines without PPP1R1C | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent |
| [[LMO7DN]] | B | LMO7DN activity raises MTNR1A's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 1.67× lower at baseline in the lines without LMO7DN | 0.023 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[LINC00960]] | B | LINC00960 activity raises MTNR1A's level | lines that do not express LINC00960 (21) vs lines expressing it (29) | 1.27× lower at baseline in the lines without LINC00960 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000282943, ENSG00000272297, ADAMTS3; maybe low, not absent |
| [[KRT86]] | B | KRT86 activity raises MTNR1A's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 1.58× lower at baseline in the lines without KRT86 | 0.082 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |
| [[LINC01290]] | C | LINC01290 activity lowers MTNR1A's level | lines that do not express LINC01290 (3) vs lines expressing it (47) | 1.94× higher at baseline in the lines without LINC01290 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: UGDH, IQSEC2, APOBEC3F; maybe low, not absent; its own permutation p |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAT1]] | B | MTNR1A activity raises FAT1's level | lines that do not express MTNR1A (7) vs lines expressing it (43) | 2.82× lower at baseline in the lines without MTNR1A | 0.006 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[KCNQ4]] | B | MTNR1A activity strengthens KCNQ4's drug response | lines that do not express MTNR1A (5) vs lines expressing it (34) | the lines without MTNR1A respond 0.57× as strongly (z diff +0.60); strongest at Homoharringtonine 5 µM: 0.31x vs 1.94x (z diff +11.5) | 0.010 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[LINC01204]] | B | MTNR1A activity lowers LINC01204's level | lines that do not express MTNR1A (7) vs lines expressing it (43) | 2.10× higher at baseline in the lines without MTNR1A | 0.023 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SEMA4A]] | B | MTNR1A activity raises SEMA4A's level | lines that do not express MTNR1A (7) vs lines expressing it (43) | 2.35× lower at baseline in the lines without MTNR1A | 0.048 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MLIP]] | B | MTNR1A activity raises MLIP's level | lines that do not express MTNR1A (7) vs lines expressing it (43) | 1.93× lower at baseline in the lines without MTNR1A | 0.076 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CFAP161]] | B | MTNR1A activity raises CFAP161's level | lines that do not express MTNR1A (7) vs lines expressing it (43) | 2.09× lower at baseline in the lines without MTNR1A | 0.077 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ILKAP]] | B | MTNR1A activity lowers ILKAP's level | lines that do not express MTNR1A (7) vs lines expressing it (43) | 1.21× higher at baseline in the lines without MTNR1A | 0.083 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TRPC4AP]] | B | MTNR1A activity lowers TRPC4AP's level | lines that do not express MTNR1A (7) vs lines expressing it (43) | 1.14× higher at baseline in the lines without MTNR1A | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.9, -10.8); signed map (20.2, 7.9). **Vector** length 78.9, 16.3% of its response variance represented; |z| ≥ 3 in 932 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.5 | +24.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.7 | +14.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.9 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +4.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.0 | +6.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.5 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +5.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +2.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | melatonin receptor 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.2 — chr4:186,526,792-186,555,567 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MEL-1A-R |
| Gene groups (HGNC) | Melatonin receptors |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 5 pathways, smallest: Class A/1 (Rhodopsin-like receptors); G alpha (i) signalling events; GPCR ligand binding |
| Matched by | ensembl_id |

**Function**, from UniProt [P48039](https://www.uniprot.org/uniprotkb/P48039) (Melatonin receptor type 1A):

> High affinity receptor for melatonin. Likely to mediate the reproductive and circadian actions of melatonin. The activity of this receptor is mediated by pertussis toxin sensitive G proteins that inhibit adenylate cyclase activity. Possibly involved in sleep induction, by melatonin activation of the potassium channel KCNMA1/BK and the dissociation of G-beta and G-gamma subunits, thereby decreasing synaptic transmission (By similarity).

**Summary**, from NCBI Gene [4543](https://www.ncbi.nlm.nih.gov/gene/4543):

> This gene encodes one of two high affinity forms of a receptor for melatonin, the primary hormone secreted by the pineal gland. This receptor is a G-protein coupled, 7-transmembrane receptor that is responsible for melatonin effects on mammalian circadian rhythm and reproductive alterations affected by day length. The receptor is an integral membrane protein that is readily detectable and localized to two specific regions of the brain. The hypothalamic suprachiasmatic nucleus appears to be …

**Accessions** — [HGNC:7463](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7463) · Entrez [4543](https://www.ncbi.nlm.nih.gov/gene/4543) · UniProt [P48039](https://www.uniprot.org/uniprotkb/P48039) · Ensembl [ENSG00000168412](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168412)

## Data

Gene col 9648: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9648); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9648, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9648]; `tensor/DDL_lfc|DDL_z.npy` [9648]; `embed/gene_vectors.npy` [9648]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9648 or target_col == 9648). Every well: [[MTNR1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTNR1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
