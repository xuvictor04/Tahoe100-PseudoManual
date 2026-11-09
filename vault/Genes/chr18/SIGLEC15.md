---
symbol: "SIGLEC15"
type: "gene"
col: 12330
ensembl_id: "ENSG00000197046"
name: "sialic acid binding Ig like lectin 15"
location: "18q21.1"
module: 13
arm: "+"
pooled_cpm: 2.42
n_lines_expressing: 23
n_dd_up: 14
n_dd_down: 16
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 6
direction_downstream: 22
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# SIGLEC15

*sialic acid binding Ig like lectin 15* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.50× (z +11.3, q 7e-27, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 2.40× (z +3.8, q 0.011, up in 0 of 7 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.332× (z -6.4, q 7e-08, down in 14 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD3]] (+0.78, fdr 7e-06), [[TMEM200A]] (+0.75, fdr 7e-06), [[GPR68]] (+0.66, fdr 7e-06); moves opposite to [[TSC22D3]] (-0.56, fdr 2e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TMEM200A]] → it (grade C ⚠); 22 go from it, the strongest it → [[PDE4DIPP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12330.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.50×** | +11.3 | 7e-27 | 1/2 (LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.02×** | +8.1 | 2e-13 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.57×** | +8.0 | 2e-13 | 2/5 (LOX-IMVI, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.00×** | +4.4 | 0.002 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +4.1 | 0.006 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.40×** | +3.8 | 0.011 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.84×** | +3.8 | 0.011 | 4/7 (J82, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.19×** | +3.4 | 0.042 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.69×** | +3.3 | 0.061 | 4/16 (SNU-423, HOP62, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.3 | 0.061 | 1/9 (RPMI-7951) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Silodosin (drug)]] 5 µM |  | **1.71×** | +3.2 | 0.067 | 1/9 (RPMI-7951) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +3.2 | 0.074 | 0/11 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.67×** | +3.1 | 0.083 | 1/11 (LoVo) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.56×** | +3.1 | 0.083 | 0/3 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12330.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.332×** | -6.4 | 7e-08 | 14/19 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.466×** | -4.8 | 3e-04 | 13/20 (LOX-IMVI, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.565×** | -4.3 | 0.003 | 13/19 (J82, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.616×** | -4.1 | 0.005 | 15/20 (SNU-423, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.531×** | -4.0 | 0.007 | 9/19 (LoVo, LOX-IMVI, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.552×** | -3.8 | 0.016 | 12/19 (SNU-423, hTERT-HPNE, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.658×** | -3.7 | 0.019 | 11/19 (H4, LoVo, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.564×** | -3.6 | 0.020 | 7/20 (J82, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.567×** | -3.6 | 0.020 | 6/18 (H4, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.575×** | -3.5 | 0.026 | 11/18 (SNU-423, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.683×** | -3.4 | 0.032 | 6/17 (BT-474, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.595×** | -3.3 | 0.048 | 13/16 (LOX-IMVI, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.598×** | -3.3 | 0.048 | 11/18 (SNU-423, LoVo, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.389×** | -3.1 | 0.073 | 7/19 (H4, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.709×** | -3.1 | 0.073 | 7/20 (LOX-IMVI, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.603×** | -3.1 | 0.073 | 10/18 (LOX-IMVI, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12330. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 57.5 | 0 | 9 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0285× (z -17.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -12.9) |
| [[LOX-IMVI (line)]] | wt | 12.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0248× (z -13.0) |
| [[H4 (line)]] | wt | 7.85 | 0 | 3 (1 ⚠) | — | [[olaparib (drug)]] 0.05 µM 0.0327× (z -8.7) ⚠ unreliable plate only · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0332× (z -8.7) |
| [[LoVo (line)]] | wt | 2.86 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0415× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 8.43 | 0 | 1 | — | [[Mifepristone (drug)]] 0.05 µM 0.0518× (z -8.7) |
| [[A-172 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.217 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.271 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.477 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.270 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.290 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.979 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.323 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.707 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.282 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.638 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.290 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.289 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.304 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.292 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.277 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.264 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.307 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12330), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD3]] | +0.78 | +0.72 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[TMEM200A]] | +0.75 | +0.72 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[GPR68]] | +0.66 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[LAMA4]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[EVA1A]] | +0.63 | +0.53 / +0.76 | both halves | 1e-05 |  |
| [[SPOCD1]] | +0.63 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[IL1RAPL1]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[SHANK1]] | +0.62 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[ADAMTS12]] | +0.61 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[INSYN2B]] | +0.61 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[C13orf46]] | +0.61 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[MIR4280HG]] | +0.61 | +0.48 / +0.66 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D3]] | -0.56 | -0.48 / -0.63 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM200A]] | C | TMEM200A activity raises SIGLEC15's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 1.98× lower at baseline in the lines without TMEM200A | 0.024 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615; co-absent with the target |
| [[SAMD3]] | C | SAMD3 activity raises SIGLEC15's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 2.29× lower at baseline in the lines without SAMD3 | 0.034 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11; co-absent with the target |
| [[MANCR]] | C | MANCR activity raises SIGLEC15's level | lines that do not express MANCR (20) vs lines expressing it (30) | 1.80× lower at baseline in the lines without MANCR | 0.050 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2; co-absent with the target |
| [[NLRP1]] | C | NLRP1 activity raises SIGLEC15's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 2.12× lower at baseline in the lines without NLRP1 | 0.073 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12; co-absent with the target |
| [[IL33]] | C | IL33 activity raises SIGLEC15's level | lines that do not express IL33 (35) vs lines expressing it (15) | 1.60× lower at baseline in the lines without IL33 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01133, MUC2, LINC01411; co-absent with the target |
| [[IL1B]] | C | IL1B activity raises SIGLEC15's level | lines that do not express IL1B (30) vs lines expressing it (20) | 2.00× lower at baseline in the lines without IL1B | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 4, C 18. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE4DIPP2]] | B | SIGLEC15 activity raises PDE4DIPP2's level | lines that do not express SIGLEC15 (27) vs lines expressing it (23) | 2.28× lower at baseline in the lines without SIGLEC15 | 0.028 | ⚠ within organs, on part of the lines; also absent: LINC01615, ZNF257, NLRP1 |
| [[MIR4280HG]] | B | SIGLEC15 activity raises MIR4280HG's level | lines that do not express SIGLEC15 (27) vs lines expressing it (23) | 1.87× lower at baseline in the lines without SIGLEC15 | 0.042 | ⚠ within organs, on part of the lines; also absent: LINC01615, ZNF257, NLRP1 |
| [[RAC2]] | B | SIGLEC15 activity raises RAC2's level | lines that do not express SIGLEC15 (27) vs lines expressing it (23) | 3.32× lower at baseline in the lines without SIGLEC15 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC01615, ZNF257, NLRP1 |
| [[FHAD1]] | B | SIGLEC15 activity raises FHAD1's level | lines that do not express SIGLEC15 (27) vs lines expressing it (23) | 1.61× lower at baseline in the lines without SIGLEC15 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC01615, ZNF257, NLRP1 |
| [[NLRP1]] | C | SIGLEC15 activity raises NLRP1's level | lines that do not express SIGLEC15 (27) vs lines expressing it (23) | 5.56× lower at baseline in the lines without SIGLEC15 | 3e-04 | ⚠ within organs, on part of the lines; also absent: LINC01615, ZNF257, NLRP1; co-absent with the target |
| [[TMEM200A]] | C | SIGLEC15 activity raises TMEM200A's level | lines that do not express SIGLEC15 (27) vs lines expressing it (23) | 3.41× lower at baseline in the lines without SIGLEC15 | 0.015 | ⚠ within organs, on part of the lines; also absent: LINC01615, ZNF257, NLRP1; co-absent with the target |
| [[SAMD3]] | C | SIGLEC15 activity raises SAMD3's level | lines that do not express SIGLEC15 (27) vs lines expressing it (23) | 3.52× lower at baseline in the lines without SIGLEC15 | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC01615, ZNF257, NLRP1; co-absent with the target |
| [[LINC02899]] | C | SIGLEC15 activity raises LINC02899's level | lines that do not express SIGLEC15 (27) vs lines expressing it (23) | 3.33× lower at baseline in the lines without SIGLEC15 | 0.027 | ⚠ within organs, on part of the lines; also absent: LINC01615, ZNF257, NLRP1; co-absent with the target |
| [[LINC02970]] | C | SIGLEC15 activity raises LINC02970's level | lines that do not express SIGLEC15 (27) vs lines expressing it (23) | 2.53× lower at baseline in the lines without SIGLEC15 | 0.031 | ⚠ within organs, on part of the lines; also absent: LINC01615, ZNF257, NLRP1; co-absent with the target |
| [[APCDD1L]] | C | SIGLEC15 activity raises APCDD1L's level | lines that do not express SIGLEC15 (27) vs lines expressing it (23) | 3.31× lower at baseline in the lines without SIGLEC15 | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC01615, ZNF257, NLRP1; co-absent with the target |
| [[EVA1A]] | C | SIGLEC15 activity raises EVA1A's level | lines that do not express SIGLEC15 (27) vs lines expressing it (23) | 2.84× lower at baseline in the lines without SIGLEC15 | 0.042 | ⚠ within organs, on part of the lines; also absent: LINC01615, ZNF257, NLRP1; co-absent with the target |
| [[LINC02220]] | C | SIGLEC15 activity raises LINC02220's level | lines that do not express SIGLEC15 (27) vs lines expressing it (23) | 1.98× lower at baseline in the lines without SIGLEC15 | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC01615, ZNF257, NLRP1; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.574). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.2, 13.8); signed map (19.3, 47.8). **Vector** length 54.2, 14.2% of its response variance represented; |z| ≥ 3 in 666 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +0.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.0 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +3.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.0 | +2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +0.4 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.4 | -4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.1 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -6.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | sialic acid binding Ig like lectin 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1 — chr18:45,825,675-45,844,094 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HsT1361; previously CD33L3 |
| Gene groups (HGNC) | V-set domain containing; Sialic acid binding Ig like lectins |
| Reactome | 2 pathways, smallest: DAP12 interactions; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZMC9](https://www.uniprot.org/uniprotkb/Q6ZMC9) (Sialic acid-binding Ig-like lectin 15):

> Binds sialylated glycoproteins.

**Summary**, from NCBI Gene [284266](https://www.ncbi.nlm.nih.gov/gene/284266):

> Predicted to be involved in regulation of actin cytoskeleton organization; regulation of bone resorption; and regulation of osteoclast development. Predicted to be located in membrane. Predicted to be part of protein-containing complex. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27596](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27596) · Entrez [284266](https://www.ncbi.nlm.nih.gov/gene/284266) · UniProt [Q6ZMC9](https://www.uniprot.org/uniprotkb/Q6ZMC9) · Ensembl [ENSG00000197046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197046)

## Data

Gene col 12330: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12330); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12330, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12330]; `tensor/DDL_lfc|DDL_z.npy` [12330]; `embed/gene_vectors.npy` [12330]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12330 or target_col == 12330). Every well: [[SIGLEC15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIGLEC15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
