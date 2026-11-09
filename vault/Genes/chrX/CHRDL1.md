---
symbol: "CHRDL1"
type: "gene"
col: 2191
ensembl_id: "ENSG00000101938"
name: "chordin like 1"
location: "Xq23"
module: 66
arm: "+"
pooled_cpm: 2.76
n_lines_expressing: 13
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 12
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# CHRDL1

*chordin like 1* — Xq23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.38× (z +12.9, q 2e-35, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.64× (z +9.2, q 6e-18, up in 4 of 6 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adenosine (drug)]] 0.5 µM: 0.460× (z -5.3, q 8e-05, down in 1 of 8 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POSTN]] (+0.71, fdr 7e-06), [[COL3A1]] (+0.63, fdr 1e-05), [[MOXD1]] (+0.59, fdr 1e-05); moves opposite to [[DCLRE1C]] (-0.49, fdr 1e-04), [[TOE1]] (-0.45, fdr 2e-04), [[MRPS2]] (-0.44, fdr 1e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[COL3A1]] → it (grade C ⚠); 12 go from it, the strongest it → [[PIGT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2191.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.38×** | +12.9 | 2e-35 | 2/2 (SNU-423, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.82×** | +10.6 | 1e-23 | 3/5 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.64×** | +9.2 | 6e-18 | 4/6 (HOP62, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.58×** | +8.7 | 5e-16 | 2/3 (SNU-423, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.74×** | +6.5 | 8e-09 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.93×** | +6.2 | 4e-08 | 4/8 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.32×** | +5.8 | 7e-07 | 2/4 (NCI-H460, SNU-423) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.72×** | +5.5 | 3e-06 | 1/3 (SNU-423) | top dose only | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.74×** | +5.2 | 1e-05 | 1/7 (hTERT-HPNE) | top dose only | composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +4.6 | 2e-04 | 0/4 | top dose only |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.87×** | +4.2 | 0.001 | 0/4 | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.37×** | +4.1 | 0.002 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +4.1 | 0.002 | 0/4 | top dose only | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.74×** | +3.7 | 0.008 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.74×** | +3.7 | 0.008 | 0/9 | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +3.7 | 0.008 | 2/8 (SNU-423, HOP62) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.15×** | +3.7 | 0.008 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.014 | 1/9 (SNU-423) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.61×** | +3.2 | 0.040 | 0/4 | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.059 | 0/8 | top dose only |  |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.71×** | +3.1 | 0.059 | 0/4 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +3.0 | 0.063 | 2/8 (NCI-H460, RPMI-7951) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tolmetin (drug)]] 0.05 µM |  | **1.65×** | +2.8 | 0.094 | 2/10 (SNU-423, J82) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.65×** | +2.8 | 0.094 | 0/4 | inconsistent across doses | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.80×** | +2.8 | 0.098 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2191.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adenosine (drug)]] 0.5 µM |  | **0.460×** | -5.3 | 8e-05 | 1/8 (hTERT-HPNE) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.578× | -3.5 | 0.13 | 3/8 (NCI-H23, NCI-H661, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 5 µM |  | 0.707× | -3.3 | 0.16 | 2/10 (SNU-423, RPMI-7951) | top dose only | position effect removed |
| [[Bendamustine (drug)]] 0.5 µM |  | 0.621× | -3.2 | 0.17 | 0/10 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2191. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 68.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 0.330 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.257 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.248 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.271 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.535 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.262 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.298 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.254 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.545 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.279 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.944 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.294 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.266 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.396 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.752 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.764 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.487 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.317 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.250 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.242 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.891 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.239 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.253 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.370 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.709 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.310 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.364 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.300 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.266 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.294 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.286 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2191), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POSTN]] | +0.71 | +0.59 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[COL3A1]] | +0.63 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[MOXD1]] | +0.59 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[SUSD5]] | +0.59 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[ANXA8]] | +0.58 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[CCDC80]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[TGFBI]] | +0.55 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[NRK]] | +0.55 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[EFEMP1]] | +0.54 | +0.29 / +0.62 | both halves | 2e-04 |  |
| [[CDH6]] | +0.54 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[CPE]] | +0.53 | +0.28 / +0.53 | both halves | 3e-04 |  |
| [[OLFML2A]] | +0.53 | +0.30 / +0.56 | both halves | 2e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCLRE1C]] | -0.49 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[TOE1]] | -0.45 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[MRPS2]] | -0.44 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[ZNF595]] | -0.43 | -0.32 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL3A1]] | C | COL3A1 activity raises CHRDL1's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 1.95× lower at baseline in the lines without COL3A1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677; co-absent with the target |
| [[THY1]] | C | THY1 activity raises CHRDL1's level | lines that do not express THY1 (38) vs lines expressing it (12) | 1.48× lower at baseline in the lines without THY1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TMPRSS15, DCN, COL11A1; co-absent with the target |
| [[BCAT1]] | C | BCAT1 activity raises CHRDL1's level | lines that do not express BCAT1 (25) vs lines expressing it (25) | 1.94× lower at baseline in the lines without BCAT1 | 0.029 | ⚠ within organs, on part of the lines; also absent: C5orf46, LOX, TOX; co-absent with the target |
| [[COL1A2]] | C | COL1A2 activity raises CHRDL1's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 2.76× lower at baseline in the lines without COL1A2 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5; co-absent with the target |
| [[CDH6]] | C | CDH6 activity raises CHRDL1's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 1.95× lower at baseline in the lines without CDH6 | 0.094 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 5, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIGT]] | B | CHRDL1 activity raises PIGT's level | lines that do not express CHRDL1 (37) vs lines expressing it (13) | 1.43× lower at baseline in the lines without CHRDL1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01592, PAX3, LINC01035 |
| [[FKBP7]] | B | CHRDL1 activity raises FKBP7's level | lines that do not express CHRDL1 (37) vs lines expressing it (13) | 1.55× lower at baseline in the lines without CHRDL1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01592, PAX3, LINC01035 |
| cells under [[Docetaxel (Trihydrate) (drug)]] 5 µM | B | CHRDL1 activity lowers the cells' numbers under Docetaxel (Trihydrate) 5 µM (makes them more sensitive) | lines that do not express CHRDL1 (37) vs lines expressing it (11) | the lines without CHRDL1: 1.32× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01592, PAX3, LINC01035 |
| [[CUL4B]] | B | CHRDL1 activity raises CUL4B's level | lines that do not express CHRDL1 (37) vs lines expressing it (13) | 1.72× lower at baseline in the lines without CHRDL1 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01592, PAX3, LINC01035 |
| [[CD302]] | B | CHRDL1 activity raises CD302's level | lines that do not express CHRDL1 (37) vs lines expressing it (13) | 1.69× lower at baseline in the lines without CHRDL1 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01592, PAX3, LINC01035 |
| [[SULF1]] | C | CHRDL1 activity raises SULF1's level | lines that do not express CHRDL1 (37) vs lines expressing it (13) | 3.26× lower at baseline in the lines without CHRDL1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01592, PAX3, LINC01035; co-absent with the target |
| [[NID2]] | C | CHRDL1 activity raises NID2's level | lines that do not express CHRDL1 (37) vs lines expressing it (13) | 4.08× lower at baseline in the lines without CHRDL1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01592, PAX3, LINC01035; co-absent with the target |
| [[CDH6]] | C | CHRDL1 activity raises CDH6's level | lines that do not express CHRDL1 (37) vs lines expressing it (13) | 3.64× lower at baseline in the lines without CHRDL1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01592, PAX3, LINC01035; co-absent with the target |
| [[SPARC]] | C | CHRDL1 activity raises SPARC's level | lines that do not express CHRDL1 (37) vs lines expressing it (13) | 3.36× lower at baseline in the lines without CHRDL1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01592, PAX3, LINC01035; co-absent with the target |
| [[BCAT1]] | C | CHRDL1 activity raises BCAT1's level | lines that do not express CHRDL1 (37) vs lines expressing it (13) | 4.17× lower at baseline in the lines without CHRDL1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01592, PAX3, LINC01035; co-absent with the target |
| [[CREB3L1]] | C | CHRDL1 activity raises CREB3L1's level | lines that do not express CHRDL1 (37) vs lines expressing it (13) | 2.89× lower at baseline in the lines without CHRDL1 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01592, PAX3, LINC01035; co-absent with the target |
| [[PTN]] | C | CHRDL1 activity raises PTN's level | lines that do not express CHRDL1 (37) vs lines expressing it (13) | 2.07× lower at baseline in the lines without CHRDL1 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01592, PAX3, LINC01035; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.689). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (57.4, 22.3); signed map (43.3, 21.5). **Vector** length 13.4, 2.34% of its response variance represented; |z| ≥ 3 in 180 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.3 | +9.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.7 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.5 | +0.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.5 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.5 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.4 | -0.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.4 | -0.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.4 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.4 | +0.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.3 | -0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.3 | -0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.3 | -0.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.3 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | chordin like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq23 — chrX:110,673,856-110,795,819 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NRLN1, CHL; previously MGC1 |
| Gene groups (HGNC) | Chordin family |
| Reactome | 4 pathways, smallest: Signaling by BMP; Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BU40](https://www.uniprot.org/uniprotkb/Q9BU40) (Chordin-like protein 1):

> Antagonizes the function of BMP4 by binding to it and preventing its interaction with receptors. Alters the fate commitment of neural stem cells from gliogenesis to neurogenesis. Contributes to neuronal differentiation of neural stem cells in the brain by preventing the adoption of a glial fate. May play a crucial role in dorsoventral axis formation. May play a role in embryonic bone formation (By similarity). May also play an important role in regulating retinal angiogenesis through modulation …

**Summary**, from NCBI Gene [91851](https://www.ncbi.nlm.nih.gov/gene/91851):

> This gene encodes an antagonist of bone morphogenetic protein 4. The encoded protein may play a role in topographic retinotectal projection and in the regulation of retinal angiogenesis in response to hypoxia. Alternatively spliced transcript variants encoding different isoforms have been described. [provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:29861](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29861) · Entrez [91851](https://www.ncbi.nlm.nih.gov/gene/91851) · UniProt [Q9BU40](https://www.uniprot.org/uniprotkb/Q9BU40) · Ensembl [ENSG00000101938](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101938)

## Data

Gene col 2191: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2191); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2191, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2191]; `tensor/DDL_lfc|DDL_z.npy` [2191]; `embed/gene_vectors.npy` [2191]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2191 or target_col == 2191). Every well: [[CHRDL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHRDL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
