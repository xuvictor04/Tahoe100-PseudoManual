---
symbol: "CNTN6"
type: "gene"
col: 5513
ensembl_id: "ENSG00000134115"
name: "contactin 6"
location: "3p26.3"
module: 121
arm: "+"
pooled_cpm: 4.31
n_lines_expressing: 12
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 12
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# CNTN6

*contactin 6* — 3p26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.17× (z +17.3, q 0e+00, up in 1 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (SNU-423 0.0845×; ⚠ cell-cycle shift, explains ~93% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.194×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SNU-423 0.103×; ⚠ cell-cycle shift, explains ~18% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRIN2A]] (+0.72, fdr 7e-06), [[LINC01435]] (+0.72, fdr 7e-06), [[TEX41]] (+0.66, fdr 7e-06); moves opposite to [[SDC3]] (-0.46, fdr 4e-05), [[INPP5F]] (-0.46, fdr 7e-05).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02506]] → it (grade C ⚠); 12 go from it, the strongest it → [[RFTN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5513.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.17×** | +17.3 | 0e+00 | 1/6 (C32) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.65×** | +13.2 | 4e-37 | 1/5 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.89×** | +12.8 | 2e-35 | 3/6 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.30×** | +12.0 | 4e-31 | 1/5 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.95×** | +8.6 | 1e-15 | 1/5 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.97×** | +5.8 | 6e-07 | 2/9 (SK-MEL-2, C32) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.99×** | +4.9 | 7e-05 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +4.9 | 7e-05 | 0/6 | top dose only | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +4.5 | 4e-04 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.04×** | +4.4 | 8e-04 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +4.2 | 0.001 | 3/7 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.1 | 0.002 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.60×** | +3.7 | 0.009 | 0/6 | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.012 | 1/9 (SW1417) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.024 | 1/9 (C32) | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.051 | 0/6 | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 0.05 µM |  | **1.42×** | +3.0 | 0.083 | 0/8 | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +2.9 | 0.092 | 0/5 | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.61×** | +2.9 | 0.092 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +2.9 | 0.094 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.60×** | +2.9 | 0.099 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5513.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (SNU-423 0.0845×; ⚠ cell-cycle shift, explains ~93% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.194×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SNU-423 0.103×; ⚠ cell-cycle shift, explains ~18% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.681× | -3.3 | 0.25 | 3/9 (H4, HS-578T, …) | two highest doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.663× | -3.3 | 0.25 | 0/9 | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.677× | -3.2 | 0.25 | 2/9 (SK-MEL-2, C32) | top dose only | plate-row cell shift |
| [[Asciminib (drug)]] 0.5 µM |  | 0.698× | -3.1 | 0.28 | 2/9 (RPMI-7951, SW1417) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5513. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 81.7 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0845× (z -10.4) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -9.8) |
| [[A498 (line)]] | wt | 23.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +9.1) | — |
| [[A-172 (line)]] | wt | 0.681 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.973 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.604 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.889 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.735 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.678 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.857 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.602 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.682 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.770 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.737 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.747 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.670 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.647 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.576 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.633 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.647 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.656 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.818 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.683 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.782 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.880 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.676 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.643 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.707 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5513), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRIN2A]] | +0.72 | +0.66 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[LINC01435]] | +0.72 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[TEX41]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[LINC00536]] | +0.65 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[PTH2R]] | +0.65 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[MSR1]] | +0.61 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[FYB1]] | +0.61 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[FRMPD4]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[KCNIP1]] | +0.58 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[DOCK10]] | +0.58 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[NR1H4]] | +0.57 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[SYT14]] | +0.57 | +0.51 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDC3]] | -0.46 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[INPP5F]] | -0.46 | -0.41 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02506]] | C | LINC02506 activity raises CNTN6's level | lines that do not express LINC02506 (40) vs lines expressing it (10) | 2.39× lower at baseline in the lines without LINC02506 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OVAAL, LINC01610, ENSG00000241168; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 4, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RFTN2]] | B | CNTN6 activity raises RFTN2's level | lines that do not express CNTN6 (38) vs lines expressing it (12) | 1.81× lower at baseline in the lines without CNTN6 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC02476, SPARC; maybe low, not absent |
| [[LDB2]] | B | CNTN6 activity raises LDB2's level | lines that do not express CNTN6 (38) vs lines expressing it (12) | 3.16× lower at baseline in the lines without CNTN6 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC02476, SPARC; maybe low, not absent |
| [[P2RX7]] | B | CNTN6 activity raises P2RX7's level | lines that do not express CNTN6 (38) vs lines expressing it (12) | 3.10× lower at baseline in the lines without CNTN6 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC02476, SPARC; maybe low, not absent |
| [[GPR158]] | B | CNTN6 activity raises GPR158's level | lines that do not express CNTN6 (38) vs lines expressing it (12) | 2.46× lower at baseline in the lines without CNTN6 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC02476, SPARC; maybe low, not absent |
| [[LINC02476]] | C | CNTN6 activity raises LINC02476's level | lines that do not express CNTN6 (38) vs lines expressing it (12) | 9.66× lower at baseline in the lines without CNTN6 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC02476, SPARC; maybe low, not absent; co-absent with the target |
| [[LINC02055]] | C | CNTN6 activity raises LINC02055's level | lines that do not express CNTN6 (38) vs lines expressing it (12) | 5.30× lower at baseline in the lines without CNTN6 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC02476, SPARC; maybe low, not absent; co-absent with the target |
| [[PDZRN3]] | C | CNTN6 activity raises PDZRN3's level | lines that do not express CNTN6 (38) vs lines expressing it (12) | 5.24× lower at baseline in the lines without CNTN6 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC02476, SPARC; maybe low, not absent; co-absent with the target |
| [[PREX2]] | C | CNTN6 activity raises PREX2's level | lines that do not express CNTN6 (38) vs lines expressing it (12) | 1.77× lower at baseline in the lines without CNTN6 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC02476, SPARC; maybe low, not absent; co-absent with the target |
| [[TP63]] | C | CNTN6 activity raises TP63's level | lines that do not express CNTN6 (38) vs lines expressing it (12) | 2.23× lower at baseline in the lines without CNTN6 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC02476, SPARC; maybe low, not absent; co-absent with the target |
| [[LINC01320]] | C | CNTN6 activity raises LINC01320's level | lines that do not express CNTN6 (38) vs lines expressing it (12) | 4.36× lower at baseline in the lines without CNTN6 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC02476, SPARC; maybe low, not absent; co-absent with the target |
| [[TEX41]] | C | CNTN6 activity raises TEX41's level | lines that do not express CNTN6 (38) vs lines expressing it (12) | 4.75× lower at baseline in the lines without CNTN6 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC02476, SPARC; maybe low, not absent; co-absent with the target |
| [[LINC02882]] | C | CNTN6 activity raises LINC02882's level | lines that do not express CNTN6 (38) vs lines expressing it (12) | 3.49× lower at baseline in the lines without CNTN6 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC02476, SPARC; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.677). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.2, 24.1); signed map (39.9, 25.0). **Vector** length 24.2, 6.69% of its response variance represented; |z| ≥ 3 in 191 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.8 | +13.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +17.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.5 | +8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.2 | +12.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.7 | -0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.7 | +1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.7 | +2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.6 | +1.7 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -3.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.8 | -2.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | -1.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.6 | -1.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -0.6 | +0.2 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.6 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | contactin 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p26.3 — chr3:1,092,658-1,404,217 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NB-3 |
| Gene groups (HGNC) | I-set domain containing; Contactins |
| Reactome | 4 pathways, smallest: CHL1 interactions; L1CAM interactions; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQ52](https://www.uniprot.org/uniprotkb/Q9UQ52) (Contactin-6):

> Contactins mediate cell surface interactions during nervous system development. Participates in oligodendrocytes generation by acting as a ligand of NOTCH1. Its association with NOTCH1 promotes NOTCH1 activation through the released notch intracellular domain (NICD) and subsequent translocation to the nucleus. Involved in motor coordination (By similarity).

**Summary**, from NCBI Gene [27255](https://www.ncbi.nlm.nih.gov/gene/27255):

> The protein encoded by this gene is a member of the immunoglobulin superfamily. It is a glycosylphosphatidylinositol (GPI)-anchored neuronal membrane protein that functions as a cell adhesion molecule. It may play a role in the formation of axon connections in the developing nervous system. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2014]

**Accessions** — [HGNC:2176](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2176) · Entrez [27255](https://www.ncbi.nlm.nih.gov/gene/27255) · UniProt [Q9UQ52](https://www.uniprot.org/uniprotkb/Q9UQ52) · Ensembl [ENSG00000134115](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134115)

## Data

Gene col 5513: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5513); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5513, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5513]; `tensor/DDL_lfc|DDL_z.npy` [5513]; `embed/gene_vectors.npy` [5513]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5513 or target_col == 5513). Every well: [[CNTN6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNTN6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
