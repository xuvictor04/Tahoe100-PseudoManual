---
symbol: "GAS6"
type: "gene"
col: 11367
ensembl_id: "ENSG00000183087"
name: "growth arrest specific 6"
location: "13q34"
module: 126
arm: "+"
pooled_cpm: 16.52
n_lines_expressing: 42
n_dd_up: 10
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# GAS6

*growth arrest specific 6* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.03× (z +10.7, q 8e-24, up in 21 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.40× (z +7.2, q 1e-10, up in 19 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.616× (z -7.3, q 2e-10, down in 21 of 39 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDUA]] (+0.54, fdr 3e-05), [[MAN2A2]] (+0.53, fdr 3e-05), [[RMRP]] (+0.52, fdr 8e-05); moves opposite to [[MRPS12]] (-0.52, fdr 2e-04), [[EMC6]] (-0.47, fdr 5e-04), [[C16orf91]] (-0.46, fdr 4e-04).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NCS1]] → it (grade B ⚠); 10 go from it, the strongest it → [[APLP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11367.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.03×** | +10.7 | 8e-24 | 21/28 (SNU-423, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +10.1 | 1e-21 | 20/24 (SNU-423, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +9.8 | 3e-20 | 15/20 (SNU-423, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +7.2 | 1e-10 | 19/38 (AsPC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.95×** | +5.2 | 2e-05 | 10/19 (SNU-423, HOP62, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +4.5 | 6e-04 | 9/34 (HS-578T, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.003 | 10/40 (NCI-H460, PANC-1, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.63×** | +3.8 | 0.009 | 13/38 (SW480, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.031 | 7/40 (Hs 766T, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.049 | 9/39 (LoVo, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +3.2 | 0.063 | 12/31 (NCI-H460, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (drug)]] 0.5 µM |  | 1.22× | +3.0 | 0.10 | 6/35 (NCI-H460, NCI-H2347, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.22× | +3.0 | 0.10 | 7/40 (SW480, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11367.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.616×** | -7.3 | 2e-10 | 21/39 (SNU-423, COLO 205, …) | two highest doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.895× | -5.6 | 6e-06 | 13/40 (A-172, AsPC-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.703×** | -5.3 | 2e-05 | 16/39 (SNU-423, RPMI-7951, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.780×** | -5.3 | 2e-05 | 18/40 (Hs 766T, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.748×** | -4.4 | 0.002 | 13/39 (SNU-1, SW 1088, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.750×** | -4.3 | 0.002 | 16/40 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.769×** | -3.9 | 0.006 | 14/38 (KATO III, HOP62, …) | inconsistent across doses | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **0.770×** | -3.9 | 0.006 | 15/40 (A-427, COLO 205, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.615×** | -3.8 | 0.009 | 10/38 (Hs 766T, HOP62, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 5 µM |  | 0.842× | -3.6 | 0.015 | 7/39 (CHP-212, HS-578T, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.634×** | -3.6 | 0.018 | 9/37 (SW1417, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -3.4 | 0.037 | 9/40 (HCT15, SW480, …) | two highest doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.811×** | -3.1 | 0.074 | 7/39 (SW 1271, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11367. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 49.5 | 6 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +15.2) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 55.5 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +13.1) | — |
| [[SNU-423 (line)]] | alt | 30.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.58× (z +11.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 31.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +14.1) | — |
| [[A498 (line)]] | wt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 5.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.2× (z +15.3) | — |
| [[C32 (line)]] | wt | 7.36 | 0 | 1 | — | [[Mifepristone (drug)]] 0.05 µM 0.0853× (z -8.7) |
| [[COLO 205 (line)]] | alt | 12.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +13.6) | — |
| [[Hs 766T (line)]] | wt | 15.4 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.251× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 32.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +8.5) | — |
| [[J82 (line)]] | alt | 29.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +10.5) | — |
| [[KATO III (line)]] | alt | 14.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +13.0) | — |
| [[LS 180 (line)]] | wt | 32.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +12.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.95 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0966× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 15.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -11.9) |
| [[SNU-1 (line)]] | wt | 27.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11367), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDUA]] | +0.54 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[MAN2A2]] | +0.53 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[RMRP]] | +0.52 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[TLE5]] | +0.51 | +0.26 / +0.44 | both halves | 4e-04 |  |
| [[USF2]] | +0.51 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[PLXNB2]] | +0.51 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[LENG8]] | +0.51 | +0.28 / +0.53 | both halves | 3e-04 |  |
| [[GAA]] | +0.51 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[ADGRA2]] | +0.50 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[AKT2]] | +0.49 | +0.24 / +0.46 | both halves | 4e-04 |  |
| [[PLXNB1]] | +0.48 | +0.29 / +0.50 | both halves | 2e-04 |  |
| [[CCNL2]] | +0.48 | +0.39 / +0.45 | both halves | 5e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS12]] | -0.52 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[EMC6]] | -0.47 | -0.23 / -0.42 | both halves | 5e-04 |  |
| [[C16orf91]] | -0.46 | -0.24 / -0.41 | both halves | 4e-04 |  |
| [[NDUFA7]] | -0.44 | -0.25 / -0.39 | both halves | 4e-04 |  |
| [[GEMIN6]] | -0.43 | -0.13 / -0.43 | ⚠ not reproduced | 0.002 |  |
| [[PRPF4]] | -0.43 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[EMC4]] | -0.41 | -0.41 / -0.39 | both halves | 5e-05 | pathway: Dengue Virus Attachment and Entry |
| [[MTF1]] | -0.41 | -0.29 / -0.35 | both halves | 3e-04 |  |
| [[USP8]] | -0.41 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[TMEM60]] | -0.41 | -0.09 / -0.43 | ⚠ not reproduced | 0.003 |  |
| [[DEPDC5]] | -0.41 | -0.43 / -0.29 | both halves | 3e-04 |  |
| [[BLOC1S5]] | -0.40 | -0.40 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCS1]] | B | NCS1 activity raises GAS6's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 2.94× lower at baseline in the lines without NCS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[ADGRA2]] | B | ADGRA2 activity raises GAS6's level | lines that do not express ADGRA2 (11) vs lines expressing it (39) | 1.32× lower at baseline in the lines without ADGRA2 | 0.036 | ⚠ within organs, on part of the lines; also absent: CERCAM, SPEG, STARD9; maybe low, not absent |
| [[ADAMTS7]] | B | ADAMTS7 activity raises GAS6's level | lines that do not express ADAMTS7 (17) vs lines expressing it (33) | 1.22× lower at baseline in the lines without ADAMTS7 | 0.087 | ⚠ within organs, on part of the lines; also absent: VASH1, FHL1, ANTXR1; maybe low, not absent |
| [[BIN1]] | C | BIN1 activity raises GAS6's level | lines that do not express BIN1 (4) vs lines expressing it (46) | 3.81× lower at baseline in the lines without BIN1 | 0.042 | ⚠ few lines (4 vs 46); across organs; also absent: PORCN |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APLP1]] | B | GAS6 activity raises APLP1's level | lines that do not express GAS6 (8) vs lines expressing it (42) | 2.62× lower at baseline in the lines without GAS6 | 0.013 | ⚠ within organs, on part of the lines |
| [[NCS1]] | B | GAS6 activity raises NCS1's level | lines that do not express GAS6 (8) vs lines expressing it (42) | 1.94× lower at baseline in the lines without GAS6 | 0.046 | ⚠ within organs, on part of the lines |
| [[SELENON]] | B | GAS6 activity raises SELENON's level | lines that do not express GAS6 (8) vs lines expressing it (42) | 1.32× lower at baseline in the lines without GAS6 | 0.048 | ⚠ within organs, on part of the lines |
| [[SCARF2]] | B | GAS6 activity raises SCARF2's level | lines that do not express GAS6 (8) vs lines expressing it (42) | 1.62× lower at baseline in the lines without GAS6 | 0.057 | ⚠ within organs, on part of the lines |
| [[PRPF4]] | B | GAS6 activity raises PRPF4's level | lines that do not express GAS6 (8) vs lines expressing it (42) | 1.37× lower at baseline in the lines without GAS6 | 0.068 | ⚠ within organs, on part of the lines |
| [[SEPTIN5]] | B | GAS6 activity raises SEPTIN5's level | lines that do not express GAS6 (8) vs lines expressing it (42) | 2.10× lower at baseline in the lines without GAS6 | 0.075 | ⚠ within organs, on part of the lines |
| [[ADGRA2]] | B | GAS6 activity raises ADGRA2's level | lines that do not express GAS6 (8) vs lines expressing it (42) | 1.83× lower at baseline in the lines without GAS6 | 0.083 | ⚠ within organs, on part of the lines |
| [[MTURN]] | B | GAS6 activity raises MTURN's level | lines that do not express GAS6 (8) vs lines expressing it (42) | 1.78× lower at baseline in the lines without GAS6 | 0.093 | ⚠ within organs, on part of the lines |
| [[DAZAP1]] | B | GAS6 activity raises DAZAP1's level | lines that do not express GAS6 (8) vs lines expressing it (42) | 1.18× lower at baseline in the lines without GAS6 | 0.094 | ⚠ within organs, on part of the lines |
| [[CDH24]] | B | GAS6 activity raises CDH24's level | lines that do not express GAS6 (8) vs lines expressing it (42) | 1.57× lower at baseline in the lines without GAS6 | 0.096 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.528). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.5, -48.3); signed map (-15.8, -32.1). **Vector** length 73.4, 13.6% of its response variance represented; |z| ≥ 3 in 863 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +3.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.8 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.3 | -7.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -3.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -3.6 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.3 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | growth arrest specific 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:113,820,549-113,864,076 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AXSF, FLJ34709, DKFZp666G247; previously AXLLG |
| Gene groups (HGNC) | Gla domain containing |
| Reactome | 15 pathways, smallest: Transport of gamma-carboxylated protein precursors from the endoplasmic reticulum to the Golgi apparatus; Gamma-carboxylation of protein precursors; Removal of aminoterminal propeptides from gamma-carboxylated proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14393](https://www.uniprot.org/uniprotkb/Q14393) (Growth arrest-specific protein 6):

> Ligand for tyrosine-protein kinase receptors AXL, TYRO3 and MER whose signaling is implicated in cell growth and survival, cell adhesion and cell migration. GAS6/AXL signaling plays a role in various processes such as endothelial cell survival during acidification by preventing apoptosis, optimal cytokine signaling during human natural killer cell development, hepatic regeneration, gonadotropin-releasing hormone neuron survival and migration, platelet activation, or regulation of thrombotic …

**Summary**, from NCBI Gene [2621](https://www.ncbi.nlm.nih.gov/gene/2621):

> This gene encodes a gamma-carboxyglutamic acid (Gla)-containing protein thought to be involved in the stimulation of cell proliferation. This gene is frequently overexpressed in many cancers and has been implicated as an adverse prognostic marker. Elevated protein levels are additionally associated with a variety of disease states, including venous thromboembolic disease, systemic lupus erythematosus, chronic renal failure, and preeclampsia. [provided by RefSeq, Aug 2014]

**Accessions** — [HGNC:4168](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4168) · Entrez [2621](https://www.ncbi.nlm.nih.gov/gene/2621) · UniProt [Q14393](https://www.uniprot.org/uniprotkb/Q14393) · Ensembl [ENSG00000183087](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183087)

## Data

Gene col 11367: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11367); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11367, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11367]; `tensor/DDL_lfc|DDL_z.npy` [11367]; `embed/gene_vectors.npy` [11367]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11367 or target_col == 11367). Every well: [[GAS6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAS6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
