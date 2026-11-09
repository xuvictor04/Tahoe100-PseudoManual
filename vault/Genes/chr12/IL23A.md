---
symbol: "IL23A"
type: "gene"
col: 3183
ensembl_id: "ENSG00000110944"
name: "interleukin 23 subunit alpha"
location: "12q13.3"
module: 112
arm: "+"
pooled_cpm: 3.91
n_lines_expressing: 44
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 8
direction_downstream: 7
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# IL23A

*interleukin 23 subunit alpha* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.16× (z +16.7, q 0e+00, up in 25 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.563× (z -3.9, q 0.065, down in 8 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Binimetinib (drug)]] 0.5 µM in 1 line (SW480 0.249×); [[Budesonide (drug)]] 0.05 µM in 1 line (NCI-H2347 0.154×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LTB]] (+0.73, fdr 7e-06), [[TRAF1]] (+0.66, fdr 7e-06), [[ICAM2]] (+0.65, fdr 1e-05); moves opposite to [[ADAM15]] (-0.58, fdr 1e-05), [[CPD]] (-0.57, fdr 1e-05), [[LARP1]] (-0.52, fdr 2e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LINC00973]] → it (grade B ⚠); 7 go from it, the strongest it → [[PIK3CD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3183.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.16×** | +16.7 | 0e+00 | 25/25 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.59×** | +10.6 | 1e-23 | 27/31 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.52×** | +9.1 | 2e-17 | 19/23 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +8.2 | 3e-14 | 12/24 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.07×** | +7.5 | 9e-12 | 0/6 | all doses, flat | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.60×** | +6.9 | 5e-10 | 14/19 (CFPAC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.91×** | +6.6 | 3e-09 | 10/36 (SW1417, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.45×** | +6.4 | 8e-09 | 3/13 (SW1417, SW 900, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +5.9 | 2e-07 | 1/6 (SW1417) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.98×** | +4.9 | 5e-05 | 13/35 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.97×** | +4.9 | 5e-05 | 3/11 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +4.4 | 6e-04 | 3/13 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.10×** | +3.8 | 0.006 | 4/21 (NCI-H23, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +3.7 | 0.009 | 5/29 (SHP-77, J82, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.61×** | +3.4 | 0.022 | 13/30 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.033 | 5/36 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.046 | 11/33 (Panc 03.27, NCI-H2347, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.84×** | +3.1 | 0.047 | 3/18 (SNU-423, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.065 | 4/32 (SW1417, SW48, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3183.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Binimetinib (drug)]] 0.5 µM in 1 line (SW480 0.249×); [[Budesonide (drug)]] 0.05 µM in 1 line (NCI-H2347 0.154×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.563×** | -3.9 | 0.065 | 8/37 (SW480, NCI-H1573, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.605×** | -3.6 | 0.076 | 13/37 (NCI-H2347, KATO III, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.620× | -3.5 | 0.10 | 9/31 (NCI-H2347, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3183. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 10.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.3× (z +15.3) | — |
| [[A549 (line)]] | wt | 1.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 45.9× (z +11.5) | — |
| [[HEC-1-A (line)]] | alt | 1.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 1.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.7× (z +10.9) | — |
| [[HT-29 (line)]] | alt | 1.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.8× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 18.6 | 0 | 1 | — | [[Budesonide (drug)]] 0.05 µM 0.154× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 8.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 1.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.8× (z +11.5) | — |
| [[SNU-423 (line)]] | alt | 3.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.4× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 12.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.78× (z +10.8) | — |
| [[SW480 (line)]] | alt | 16.9 | 0 | 1 | — | [[Binimetinib (drug)]] 0.5 µM 0.249× (z -8.6) |
| [[A-172 (line)]] | wt | 0.834 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.979 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.967 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.855 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.898 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.788 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.842 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.983 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3183), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTB]] | +0.73 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[TRAF1]] | +0.66 | +0.67 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ICAM2]] | +0.65 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[PLAU]] | +0.65 | +0.58 / +0.62 | both halves | 8e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[RND1]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[NEURL3]] | +0.62 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[CSF2]] | +0.62 | +0.62 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 652 |
| [[LIF-AS2]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[ARL14]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[TRPV3]] | +0.61 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[GATM]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[GOLGA7B]] | +0.60 | +0.56 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM15]] | -0.58 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[CPD]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[LARP1]] | -0.52 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[CMPK1]] | -0.50 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[USP5]] | -0.48 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[FGA]] | -0.48 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00973]] | B | LINC00973 activity raises IL23A's level | lines that do not express LINC00973 (23) vs lines expressing it (27) | 1.54× lower at baseline in the lines without LINC00973 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000239462, IL11, BICC1 |
| [[S100A2]] | B | S100A2 activity raises IL23A's level | lines that do not express S100A2 (25) vs lines expressing it (25) | 1.51× lower at baseline in the lines without S100A2 | 0.026 | ⚠ within organs, on part of the lines; also absent: KRT81, LINC00408, FGFBP1; maybe low, not absent |
| [[MPZL3]] | B | MPZL3 activity raises IL23A's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.69× lower at baseline in the lines without MPZL3 | 0.033 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[CX3CL1]] | B | CX3CL1 activity raises IL23A's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 1.42× lower at baseline in the lines without CX3CL1 | 0.045 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[PLAU]] | B | PLAU activity raises IL23A's level | lines that do not express PLAU (26) vs lines expressing it (24) | 1.50× lower at baseline in the lines without PLAU | 0.046 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |
| [[CPAMD8]] | B | CPAMD8 activity raises IL23A's level | lines that do not express CPAMD8 (19) vs lines expressing it (31) | 1.32× lower at baseline in the lines without CPAMD8 | 0.073 | ⚠ within organs, on part of the lines; also absent: ZSCAN18, GNAO1, C11orf96; maybe low, not absent |
| [[LINC03042]] | B | LINC03042 activity raises IL23A's level | lines that do not express LINC03042 (16) vs lines expressing it (34) | 1.59× lower at baseline in the lines without LINC03042 | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC00960, CORO2B, DNAH17; maybe low, not absent |
| [[GOLT1A]] | B | GOLT1A activity raises IL23A's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 1.84× lower at baseline in the lines without GOLT1A | 0.089 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIK3CD]] | B | IL23A activity raises PIK3CD's level | lines that do not express IL23A (6) vs lines expressing it (44) | 1.73× lower at baseline in the lines without IL23A | 0.029 | ⚠ within organs, on part of the lines; also absent: MYRF; maybe low, not absent |
| [[ADAM15]] | B | IL23A activity lowers ADAM15's level | lines that do not express IL23A (6) vs lines expressing it (44) | 1.50× higher at baseline in the lines without IL23A | 0.053 | ⚠ within organs, on part of the lines; also absent: MYRF; maybe low, not absent |
| [[PLA2G4C]] | B | IL23A activity raises PLA2G4C's level | lines that do not express IL23A (6) vs lines expressing it (44) | 1.48× lower at baseline in the lines without IL23A | 0.068 | ⚠ within organs, on part of the lines; also absent: MYRF; maybe low, not absent |
| [[NFKBIE]] | B | IL23A activity raises NFKBIE's level | lines that do not express IL23A (6) vs lines expressing it (44) | 1.38× lower at baseline in the lines without IL23A | 0.071 | ⚠ within organs, on part of the lines; also absent: MYRF; maybe low, not absent |
| [[PLAU]] | B | IL23A activity raises PLAU's level | lines that do not express IL23A (6) vs lines expressing it (44) | 2.99× lower at baseline in the lines without IL23A | 0.076 | ⚠ within organs, on part of the lines; also absent: MYRF; maybe low, not absent |
| [[UPP1]] | B | IL23A activity strengthens UPP1's drug response | lines that do not express IL23A (5) vs lines expressing it (36) | the lines without IL23A respond 0.89× as strongly (z diff +1.35); strongest at Trametinib 5 µM: 0.63x vs 0.45x (z diff +3.8) | 0.081 | ⚠ within organs, on part of the lines; also absent: MYRF; maybe low, not absent; target measured in part of the lines; the reference differs; artifact flags |
| [[SLCO5A1]] | B | IL23A activity strengthens SLCO5A1's drug response | lines that do not express IL23A (6) vs lines expressing it (36) | the lines without IL23A respond 0.90× as strongly (z diff +1.21); strongest at Idarubicin (hydrochloride) 5 µM: 2.18x vs 3.18x (z diff +3.0) | 0.081 | ⚠ within organs, on part of the lines; also absent: MYRF; maybe low, not absent; target measured in part of the lines; the reference differs; artifact flags |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.9, 1.8); signed map (42.1, 11.3). **Vector** length 59.8, 11.0% of its response variance represented; |z| ≥ 3 in 908 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interleukin-10 signaling* (reactome, mean cos +0.50 to 5); *KRAS signaling up* (hallmark, mean cos +0.54 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +16.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.7 | +10.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +9.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.9 | +6.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +2.4 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.2 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +3.7 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -3.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -1.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 23 subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:56,334,174-56,340,410 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SGRF, IL23P19, IL-23, IL-23A, P19 |
| Gene groups (HGNC) | Interleukins; Interleukin 12 type subunits |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 5 pathways, smallest: Interleukin-23 signaling; Interleukin-12 family signaling; Interleukin-4 and Interleukin-13 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPF7](https://www.uniprot.org/uniprotkb/Q9NPF7) (Interleukin-23 subunit alpha):

> Associates with IL12B to form the pro-inflammatory cytokine IL-23 that plays different roles in innate and adaptive immunity. Released by antigen-presenting cells such as dendritic cells or macrophages, binds to a heterodimeric receptor complex composed of IL12RB1 and IL23R to activate JAK2 and TYK2 which then phosphorylate the receptor to form a docking site leading to the phosphorylation of STAT3 and STAT4. This process leads to activation of several pathways including p38 MAPK or NF-kappa-B …

**Summary**, from NCBI Gene [51561](https://www.ncbi.nlm.nih.gov/gene/51561):

> This gene encodes a subunit of the heterodimeric cytokine interleukin 23 (IL23). IL23 is composed of this protein and the p40 subunit of interleukin 12 (IL12B). The receptor of IL23 is formed by the beta 1 subunit of IL12 (IL12RB1) and an IL23 specific subunit, IL23R. Both IL23 and IL12 can activate the transcription activator STAT4, and stimulate the production of interferon-gamma (IFNG). In contrast to IL12, which acts mainly on naive CD4(+) T cells, IL23 preferentially acts on memory CD4(+) …

**Accessions** — [HGNC:15488](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15488) · Entrez [51561](https://www.ncbi.nlm.nih.gov/gene/51561) · UniProt [Q9NPF7](https://www.uniprot.org/uniprotkb/Q9NPF7) · Ensembl [ENSG00000110944](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110944)

## Data

Gene col 3183: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3183); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3183, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3183]; `tensor/DDL_lfc|DDL_z.npy` [3183]; `embed/gene_vectors.npy` [3183]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3183 or target_col == 3183). Every well: [[IL23A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL23A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
