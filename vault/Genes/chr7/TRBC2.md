---
symbol: "TRBC2"
type: "gene"
col: 13067
ensembl_id: "ENSG00000211772"
name: "T cell receptor beta constant 2"
location: "7q34"
module: 92
arm: "+"
pooled_cpm: 2.86
n_lines_expressing: 11
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 9
direction_downstream: 20
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# TRBC2

*T cell receptor beta constant 2* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 9.41× (z +10.9, q 1e-24, up in 5 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.83× (z +4.3, q 0.001, up in 0 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 5 µM: 0.454× (z -4.0, q 0.032, down in 9 of 9 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RASGRF2]] (+0.69, fdr 7e-06), [[EPHB6]] (+0.69, fdr 7e-06), [[MANCR]] (+0.66, fdr 1e-05); moves opposite to [[TSC22D3]] (-0.48, fdr 5e-05), [[RNF144B]] (-0.48, fdr 6e-05), [[ACSL1]] (-0.47, fdr 1e-04).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[IRAK3]] → it (grade C ⚠); 20 go from it, the strongest it → [[PTPRE]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 12 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13067.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **9.41×** | +10.9 | 1e-24 | 5/5 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.69×** | +10.3 | 3e-22 | 7/8 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.67×** | +8.1 | 1e-13 | 6/6 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.27×** | +6.0 | 4e-07 | 6/8 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.04×** | +5.4 | 9e-06 | 2/8 (CFPAC-1, SW 900) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.57×** | +4.7 | 2e-04 | 3/8 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.58×** | +4.6 | 4e-04 | 5/7 (NCI-H1792, SW 900, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **2.38×** | +4.3 | 0.001 | 5/7 (CFPAC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.83×** | +4.3 | 0.001 | 0/9 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **2.32×** | +4.2 | 0.001 | 0/9 | top dose only |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +4.0 | 0.003 | 1/9 (HOP62) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.06×** | +3.6 | 0.015 | 0/8 | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.73×** | +3.4 | 0.026 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.85×** | +3.1 | 0.090 | 2/8 (CFPAC-1, LS 180) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13067.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.454×** | -4.0 | 0.032 | 9/9 (SW480, SW 900, …) | top dose only | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.477×** | -3.5 | 0.090 | 7/9 (SW480, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.492×** | -3.5 | 0.090 | 1/9 (Panc 03.27) | inconsistent across doses | position effect removed |
| [[Encorafenib (drug)]] 5 µM |  | 0.285× | -3.3 | 0.12 | 3/9 (SW480, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | 0.302× | -3.2 | 0.16 | 7/8 (SW480, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13067. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 16.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0686× (z -12.4) |
| [[LS 180 (line)]] | wt | 5.15 | 0 | 2 (1 ⚠) | — | [[Cobimetinib (drug)]] 0.5 µM 0.0457× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 15.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0966× (z -9.3) |
| [[SW 900 (line)]] | alt | 26.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.234 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.189 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.193 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.168 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.511 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.213 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.218 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.288 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.222 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.235 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.254 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.252 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.198 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.631 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.202 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.204 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.214 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.328 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.174 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.220 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.210 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.214 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.213 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.202 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.234 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.201 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.228 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.229 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.266 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13067), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASGRF2]] | +0.69 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[EPHB6]] | +0.69 | +0.76 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[MANCR]] | +0.66 | +0.56 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[CNIH3]] | +0.62 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[LINC00973]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[PRDM8]] | +0.56 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[ADAM19]] | +0.56 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[ANTXR2]] | +0.56 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[TGFA]] | +0.55 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[DUSP4]] | +0.55 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[S100A16]] | +0.55 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[ANXA10]] | +0.54 | +0.47 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D3]] | -0.48 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[RNF144B]] | -0.48 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[ACSL1]] | -0.47 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[C1R]] | -0.47 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[NFIL3]] | -0.47 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[CNTNAP1]] | -0.46 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[PDLIM1]] | -0.46 | -0.37 / -0.39 | both halves | 9e-05 |  |
| [[IRAK3]] | -0.44 | -0.25 / -0.56 | both halves | 4e-04 |  |
| [[SLC39A14]] | -0.44 | -0.35 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRAK3]] | C | IRAK3 activity raises TRBC2's level | lines that do not express IRAK3 (36) vs lines expressing it (14) | 2.85× lower at baseline in the lines without IRAK3 | 0.016 | ⚠ within organs, on part of the lines; also absent: IRAG2, TRBC2, CXCL5; co-absent with the target |
| [[TINAGL1]] | C | TINAGL1 activity raises TRBC2's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 2.14× lower at baseline in the lines without TINAGL1 | 0.021 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19; co-absent with the target |
| [[EPHB6]] | C | EPHB6 activity raises TRBC2's level | lines that do not express EPHB6 (27) vs lines expressing it (23) | 2.11× lower at baseline in the lines without EPHB6 | 0.022 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000213981, ARHGEF38; co-absent with the target |
| [[LINC02813]] | C | LINC02813 activity raises TRBC2's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 1.97× lower at baseline in the lines without LINC02813 | 0.027 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN; co-absent with the target |
| [[SHC3]] | C | SHC3 activity raises TRBC2's level | lines that do not express SHC3 (22) vs lines expressing it (28) | 2.13× lower at baseline in the lines without SHC3 | 0.029 | ⚠ within organs, on part of the lines; also absent: CCDC33, CCR3, RFX8; maybe low, not absent; co-absent with the target |
| [[MANCR]] | C | MANCR activity raises TRBC2's level | lines that do not express MANCR (20) vs lines expressing it (30) | 2.00× lower at baseline in the lines without MANCR | 0.036 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2; co-absent with the target |
| [[IL11]] | C | IL11 activity raises TRBC2's level | lines that do not express IL11 (27) vs lines expressing it (23) | 1.71× lower at baseline in the lines without IL11 | 0.036 | ⚠ within organs, on part of the lines; also absent: EDNRA, LINC00973, LINC01583; co-absent with the target |
| [[PAEP]] | C | PAEP activity raises TRBC2's level | lines that do not express PAEP (33) vs lines expressing it (17) | 1.89× lower at baseline in the lines without PAEP | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GREM2, UNC5D; co-absent with the target |
| [[SLC16A6]] | C | SLC16A6 activity raises TRBC2's level | lines that do not express SLC16A6 (27) vs lines expressing it (23) | 1.69× lower at baseline in the lines without SLC16A6 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENPP2, TMEM47, IGFBP7; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 11, C 9. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRE]] | B | TRBC2 activity raises PTPRE's level | lines that do not express TRBC2 (39) vs lines expressing it (11) | 2.79× lower at baseline in the lines without TRBC2 | 0.030 | ⚠ within organs, on part of the lines; also absent: PIGR, MUC6, PSG1 |
| [[GCNT1]] | B | TRBC2 activity raises GCNT1's level | lines that do not express TRBC2 (39) vs lines expressing it (11) | 1.35× lower at baseline in the lines without TRBC2 | 0.032 | ⚠ within organs, on part of the lines; also absent: PIGR, MUC6, PSG1 |
| [[LIMD2]] | B | TRBC2 activity strengthens LIMD2's drug response | lines that do not express TRBC2 (33) vs lines expressing it (8) | the lines without TRBC2 respond 0.69× as strongly (z diff +0.51); rises at some drug-doses, falls at others (44% from rises): Panobinostat 0.5 µM: 0.52x vs 0.30x (z diff +1.9); Panobinostat 5 µM: 0.63x vs 0.39x (z diff +1.7); Selinexor 5 µM: 1.52x vs 1.92x (z diff +1.7) | 0.033 | ⚠ within organs, on part of the lines; also absent: PIGR, MUC6, PSG1; target measured in part of the lines; both ways; rises at some drug-doses, falls at others; artifact flags |
| [[ACSL1]] | B | TRBC2 activity raises ACSL1's level | lines that do not express TRBC2 (39) vs lines expressing it (11) | 1.38× lower at baseline in the lines without TRBC2 | 0.049 | ⚠ within organs, on part of the lines; also absent: PIGR, MUC6, PSG1 |
| [[GPR68]] | B | TRBC2 activity raises GPR68's level | lines that do not express TRBC2 (39) vs lines expressing it (11) | 1.71× lower at baseline in the lines without TRBC2 | 0.057 | ⚠ within organs, on part of the lines; also absent: PIGR, MUC6, PSG1 |
| [[ALDH1A3]] | B | TRBC2 activity raises ALDH1A3's level | lines that do not express TRBC2 (39) vs lines expressing it (11) | 3.07× lower at baseline in the lines without TRBC2 | 0.059 | ⚠ within organs, on part of the lines; also absent: PIGR, MUC6, PSG1 |
| [[RAC2]] | B | TRBC2 activity raises RAC2's level | lines that do not express TRBC2 (39) vs lines expressing it (11) | 3.27× lower at baseline in the lines without TRBC2 | 0.064 | ⚠ within organs, on part of the lines; also absent: PIGR, MUC6, PSG1 |
| [[FUT8]] | B | TRBC2 activity raises FUT8's level | lines that do not express TRBC2 (39) vs lines expressing it (11) | 2.01× lower at baseline in the lines without TRBC2 | 0.067 | ⚠ within organs, on part of the lines; also absent: PIGR, MUC6, PSG1 |
| [[ADAM19]] | B | TRBC2 activity raises ADAM19's level | lines that do not express TRBC2 (39) vs lines expressing it (11) | 1.92× lower at baseline in the lines without TRBC2 | 0.078 | ⚠ within organs, on part of the lines; also absent: PIGR, MUC6, PSG1 |
| [[IL19]] | B | TRBC2 activity raises IL19's level | lines that do not express TRBC2 (39) vs lines expressing it (11) | 1.66× lower at baseline in the lines without TRBC2 | 0.088 | ⚠ within organs, on part of the lines; also absent: PIGR, MUC6, PSG1 |
| [[TGFA]] | B | TRBC2 activity raises TGFA's level | lines that do not express TRBC2 (39) vs lines expressing it (11) | 2.55× lower at baseline in the lines without TRBC2 | 0.092 | ⚠ within organs, on part of the lines; also absent: PIGR, MUC6, PSG1 |
| [[EPHB6]] | C | TRBC2 activity raises EPHB6's level | lines that do not express TRBC2 (39) vs lines expressing it (11) | 4.20× lower at baseline in the lines without TRBC2 | 0.004 | ⚠ within organs, on part of the lines; also absent: PIGR, MUC6, PSG1; co-absent with the target |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.644). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.4, 8.9); signed map (11.9, 51.3). **Vector** length 31.4, 10.2% of its response variance represented; |z| ≥ 3 in 275 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.4 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.9 | +1.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +0.8 | -0.2 |
| fall | [[Trametinib (drug)]] 5 µM |  | -1.8 | -4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -1.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.4 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | T cell receptor beta constant 2 |
| Locus type | T cell receptor gene (other) |
| Location | 7q34 — chr7:142,801,041-142,802,748 (+) |
| Ensembl biotype | TR_C_gene |
| Also known as | TCRBC2 |
| Gene groups (HGNC) | T cell receptor beta locus at 7q34 |
| Matched by | ensembl_id |

**Function**, from UniProt [A0A5B9](https://www.uniprot.org/uniprotkb/A0A5B9) (T cell receptor beta constant 2):

> Constant region of T cell receptor (TR) beta chain. Alpha-beta T cell receptors are antigen specific receptors which are essential to the immune response and are present on the cell surface of T lymphocytes. Recognize peptide-major histocompatibility (MH) (pMH) complexes that are displayed by antigen presenting cells (APC), a prerequisite for efficient T cell adaptive immunity against pathogens. Binding of alpha-beta TR to pMH complex initiates TR-CD3 clustering on the cell surface and …

**Summary**, from NCBI Gene [28638](https://www.ncbi.nlm.nih.gov/gene/28638):

> Predicted to be involved in T cell receptor signaling pathway; adaptive immune response; and alpha-beta T cell activation. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:12157](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12157) · Entrez [28638](https://www.ncbi.nlm.nih.gov/gene/28638) · UniProt [A0A5B9](https://www.uniprot.org/uniprotkb/A0A5B9) · Ensembl [ENSG00000211772](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000211772)

## Data

Gene col 13067: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13067); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13067, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13067]; `tensor/DDL_lfc|DDL_z.npy` [13067]; `embed/gene_vectors.npy` [13067]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13067 or target_col == 13067). Every well: [[TRBC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRBC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
