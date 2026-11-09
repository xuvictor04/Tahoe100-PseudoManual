---
symbol: "EPHA5-AS1"
type: "gene"
col: 14715
ensembl_id: "ENSG00000250846"
name: "EPHA5 antisense RNA 1"
location: "4q13.2"
module: 9
arm: "+"
pooled_cpm: 2.01
n_lines_expressing: 22
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 12
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# EPHA5-AS1

*EPHA5 antisense RNA 1* — 4q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.58× (z +9.7, q 2e-19, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.18× (z +9.6, q 4e-19, up in 2 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHA5]] (+0.78, fdr 7e-06, ⚠ same locus), [[CRISPLD1]] (+0.75, fdr 7e-06), [[CDH10]] (+0.71, fdr 7e-06), [[THSD7A]] (+0.69, fdr 7e-06); moves opposite to [[RECQL]] (-0.52, fdr 3e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[EPHA5]] → it (grade C ⚠); 12 go from it, the strongest it → [[RIMS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14715.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.58×** | +9.7 | 2e-19 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.18×** | +9.6 | 4e-19 | 2/9 (SNU-423, hTERT-HPNE) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.27×** | +7.9 | 8e-13 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.54×** | +7.7 | 2e-12 | 6/11 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.71×** | +7.7 | 2e-12 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.06×** | +6.0 | 2e-07 | 7/17 (A498, SW 900, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.43×** | +5.2 | 2e-05 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.51×** | +5.2 | 2e-05 | 2/6 (A-427, SHP-77) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.83×** | +5.0 | 4e-05 | 2/17 (A-427, NCI-H2030) | rises with dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.53×** | +4.8 | 9e-05 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.21×** | +4.6 | 2e-04 | 2/14 (A498, SHP-77) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +4.4 | 4e-04 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.93×** | +3.9 | 0.005 | 10/18 (A-427, SNU-423, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.58×** | +3.6 | 0.011 | 7/17 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.55×** | +3.6 | 0.011 | 0/11 | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +3.2 | 0.042 | 4/18 (J82, NCI-H2030, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.28×** | +3.1 | 0.053 | 1/4 (NCI-H2030) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.73×** | +3.1 | 0.057 | 6/9 (NCI-H460, A-427, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +3.1 | 0.058 | 2/10 (A-427, NCI-H23) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +3.0 | 0.075 | 4/14 (SNU-423, J82, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.42×** | +2.9 | 0.087 | 1/17 (SHP-77) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +2.9 | 0.087 | 2/17 (A498, hTERT-HPNE) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14715.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mebendazole (drug)]] 5 µM |  | 0.570× | -3.2 | 0.92 | 5/17 (C32, NCI-H460, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14715. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 0.184 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.533 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.590 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.199 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.191 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.558 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.634 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.212 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.668 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.192 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.201 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.270 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.210 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.174 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.776 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.240 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.186 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.183 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.847 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.179 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.159 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.182 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.229 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.142 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.293 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.220 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.224 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.214 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.183 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.246 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.183 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14715), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHA5]] | +0.78 | +0.74 / +0.78 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[CRISPLD1]] | +0.75 | +0.69 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[CDH10]] | +0.71 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[THSD7A]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[SCN2A]] | +0.67 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[NKAIN2]] | +0.65 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[MAPK10]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[MIR99AHG]] | +0.63 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[ZSCAN31]] | +0.63 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[IQCM]] | +0.62 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[BMP5]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[CDH18]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SEMA3E]] | +0.61 | +0.65 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RECQL]] | -0.52 | -0.54 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA5]] | C | EPHA5 activity raises EPHA5-AS1's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 3.30× lower at baseline in the lines without EPHA5 | 0.003 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[SCN3A]] | C | SCN3A activity raises EPHA5-AS1's level | lines that do not express SCN3A (34) vs lines expressing it (16) | 2.96× lower at baseline in the lines without SCN3A | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, TRPC4, ENSG00000224865; co-absent with the target |
| [[CDH10]] | C | CDH10 activity raises EPHA5-AS1's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 3.06× lower at baseline in the lines without CDH10 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[FAM133A]] | C | FAM133A activity raises EPHA5-AS1's level | lines that do not express FAM133A (29) vs lines expressing it (21) | 2.35× lower at baseline in the lines without FAM133A | 0.035 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, TRPC4; co-absent with the target |
| [[CACNB2]] | C | CACNB2 activity raises EPHA5-AS1's level | lines that do not express CACNB2 (31) vs lines expressing it (19) | 2.61× lower at baseline in the lines without CACNB2 | 0.036 | ⚠ within organs, on part of the lines; also absent: SFTA3-1, DPP10, LINC01035; maybe low, not absent; co-absent with the target |
| [[BCHE]] | C | BCHE activity raises EPHA5-AS1's level | lines that do not express BCHE (35) vs lines expressing it (15) | 2.28× lower at baseline in the lines without BCHE | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[FSTL5]] | C | FSTL5 activity raises EPHA5-AS1's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 2.18× lower at baseline in the lines without FSTL5 | 0.049 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2; co-absent with the target |
| [[FMN2]] | C | FMN2 activity raises EPHA5-AS1's level | lines that do not express FMN2 (26) vs lines expressing it (24) | 2.54× lower at baseline in the lines without FMN2 | 0.052 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent; co-absent with the target |
| [[PDE1A]] | C | PDE1A activity raises EPHA5-AS1's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 2.84× lower at baseline in the lines without PDE1A | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 2, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RIMS1]] | B | EPHA5-AS1 activity raises RIMS1's level | lines that do not express EPHA5-AS1 (28) vs lines expressing it (22) | 2.48× lower at baseline in the lines without EPHA5-AS1 | 0.059 | ⚠ within organs, on part of the lines; also absent: EPHA5, ADAM23, TRPC4 |
| cells under [[Vinblastine (sulfate) (drug)]] 5 µM | B | EPHA5-AS1 activity lowers the cells' numbers under Vinblastine (sulfate) 5 µM (makes them more sensitive) | lines that do not express EPHA5-AS1 (28) vs lines expressing it (20) | the lines without EPHA5-AS1: 1.15× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: EPHA5, ADAM23, TRPC4 |
| [[EPHA5]] | C | EPHA5-AS1 activity raises EPHA5's level | lines that do not express EPHA5-AS1 (28) vs lines expressing it (22) | 7.30× lower at baseline in the lines without EPHA5-AS1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: EPHA5, ADAM23, TRPC4; co-absent with the target |
| [[PCDH9]] | C | EPHA5-AS1 activity raises PCDH9's level | lines that do not express EPHA5-AS1 (28) vs lines expressing it (22) | 4.28× lower at baseline in the lines without EPHA5-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: EPHA5, ADAM23, TRPC4; co-absent with the target |
| [[PDE4B]] | C | EPHA5-AS1 activity raises PDE4B's level | lines that do not express EPHA5-AS1 (28) vs lines expressing it (22) | 2.42× lower at baseline in the lines without EPHA5-AS1 | 0.028 | ⚠ within organs, on part of the lines; also absent: EPHA5, ADAM23, TRPC4; co-absent with the target |
| [[BCHE]] | C | EPHA5-AS1 activity raises BCHE's level | lines that do not express EPHA5-AS1 (28) vs lines expressing it (22) | 3.38× lower at baseline in the lines without EPHA5-AS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: EPHA5, ADAM23, TRPC4; co-absent with the target |
| [[HECW2]] | C | EPHA5-AS1 activity raises HECW2's level | lines that do not express EPHA5-AS1 (28) vs lines expressing it (22) | 4.55× lower at baseline in the lines without EPHA5-AS1 | 0.041 | ⚠ within organs, on part of the lines; also absent: EPHA5, ADAM23, TRPC4; co-absent with the target |
| [[NKAIN3]] | C | EPHA5-AS1 activity raises NKAIN3's level | lines that do not express EPHA5-AS1 (28) vs lines expressing it (22) | 3.10× lower at baseline in the lines without EPHA5-AS1 | 0.062 | ⚠ within organs, on part of the lines; also absent: EPHA5, ADAM23, TRPC4; co-absent with the target |
| [[EBF1]] | C | EPHA5-AS1 activity raises EBF1's level | lines that do not express EPHA5-AS1 (28) vs lines expressing it (22) | 4.63× lower at baseline in the lines without EPHA5-AS1 | 0.071 | ⚠ within organs, on part of the lines; also absent: EPHA5, ADAM23, TRPC4; co-absent with the target |
| [[PDE7B]] | C | EPHA5-AS1 activity raises PDE7B's level | lines that do not express EPHA5-AS1 (28) vs lines expressing it (22) | 2.39× lower at baseline in the lines without EPHA5-AS1 | 0.075 | ⚠ within organs, on part of the lines; also absent: EPHA5, ADAM23, TRPC4; co-absent with the target |
| [[ZFHX4]] | C | EPHA5-AS1 activity raises ZFHX4's level | lines that do not express EPHA5-AS1 (28) vs lines expressing it (22) | 6.28× lower at baseline in the lines without EPHA5-AS1 | 0.079 | ⚠ within organs, on part of the lines; also absent: EPHA5, ADAM23, TRPC4; co-absent with the target |
| [[SCN3A]] | C | EPHA5-AS1 activity raises SCN3A's level | lines that do not express EPHA5-AS1 (28) vs lines expressing it (22) | 2.78× lower at baseline in the lines without EPHA5-AS1 | 0.082 | ⚠ within organs, on part of the lines; also absent: EPHA5, ADAM23, TRPC4; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.7, 32.8); signed map (40.9, 34.6). **Vector** length 31.5, 7.37% of its response variance represented; |z| ≥ 3 in 337 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.2 | +2.3 |
| fall | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -0.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -1.8 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | EPHA5 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q13.2 — chr4:65,669,961-65,698,029 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50602](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50602) · Entrez [100144602](https://www.ncbi.nlm.nih.gov/gene/100144602) · Ensembl [ENSG00000250846](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250846)

## Data

Gene col 14715: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14715); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14715, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14715]; `tensor/DDL_lfc|DDL_z.npy` [14715]; `embed/gene_vectors.npy` [14715]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14715 or target_col == 14715). Every well: [[EPHA5-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPHA5-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
