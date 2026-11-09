---
symbol: "NYAP2"
type: "gene"
col: 6883
ensembl_id: "ENSG00000144460"
name: "neuronal tyrosine-phosphorylated phosphoinositide-3-kinase adaptor 2"
location: "2q36.3"
module: 87
arm: "+"
pooled_cpm: 4.41
n_lines_expressing: 34
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 11
direction_downstream: 11
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# NYAP2

*neuronal tyrosine-phosphorylated phosphoinositide-3-kinase adaptor 2* — 2q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.04× (z +14.1, q 2e-42, up in 8 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.627× (z -4.2, q 0.016, down in 10 of 29 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (C32 0.0722×, SHP-77 0.113×, LS 180 0.242×); [[Digitoxin (drug)]] 5 µM in 2 lines (C32 0.0666×, SHP-77 0.117×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (C32 0.0917×; ⚠ cell-cycle shift, explains ~32% of this change); [[Tofacitinib (drug)]] 5 µM in 1 line (C32 0.106×); [[Tofacitinib (citrate) (drug)]] 5 µM in 1 line (C32 0.157×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DGKB]] (+0.65, fdr 1e-05), [[CHRM3]] (+0.65, fdr 3e-05), [[NELL1]] (+0.63, fdr 1e-05); moves opposite to [[DHTKD1]] (-0.50, fdr 3e-05), [[ALDH6A1]] (-0.47, fdr 5e-04), [[RAB40B]] (-0.45, fdr 3e-04).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[SYTL5]] → it (grade B ⚠); 11 go from it, the strongest it → [[PYROXD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6883.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.04×** | +14.1 | 2e-42 | 8/22 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.36×** | +12.7 | 1e-34 | 3/8 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.26×** | +10.3 | 1e-22 | 22/30 (LS 180, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.95×** | +9.7 | 3e-20 | 6/16 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.95×** | +9.7 | 3e-20 | 22/29 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.43×** | +8.0 | 2e-13 | 16/28 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.35×** | +7.7 | 2e-12 | 17/25 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.39×** | +7.2 | 3e-11 | 3/10 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **4.25×** | +6.8 | 7e-10 | 12/19 (NCI-H460, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +5.1 | 2e-05 | 7/20 (SW 900, J82, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.0 | 3e-05 | 10/30 (SW 900, HT-29, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.78×** | +4.8 | 7e-05 | 10/19 (NCI-H1573, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +4.7 | 1e-04 | 6/22 (NCI-H460, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.95×** | +4.3 | 8e-04 | 6/24 (A498, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.64×** | +4.3 | 8e-04 | 5/24 (HOP62, J82, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **2.27×** | +3.8 | 0.004 | 10/20 (SW 900, A498, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.25×** | +3.8 | 0.005 | 9/20 (C32, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.66×** | +3.3 | 0.036 | 8/28 (A498, SNU-423, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.1 | 0.054 | 3/22 (NCI-H460, KATO III, …) | top dose only | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6883.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (C32 0.0722×, SHP-77 0.113×, LS 180 0.242×); [[Digitoxin (drug)]] 5 µM in 2 lines (C32 0.0666×, SHP-77 0.117×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (C32 0.0917×; ⚠ cell-cycle shift, explains ~32% of this change); [[Tofacitinib (drug)]] 5 µM in 1 line (C32 0.106×); [[Tofacitinib (citrate) (drug)]] 5 µM in 1 line (C32 0.157×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.627×** | -4.2 | 0.016 | 10/29 (SHP-77, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | 0.679× | -3.5 | 0.11 | 12/29 (SHP-77, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.682× | -3.4 | 0.11 | 14/30 (SHP-77, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | 0.691× | -3.3 | 0.13 | 3/22 (LoVo, MIA PaCa-2, …) | two highest doses | position effect removed |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | 0.697× | -3.3 | 0.13 | 3/22 (LOX-IMVI, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.705× | -3.1 | 0.16 | 11/28 (SHP-77, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6883. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 38.2 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0722× (z -14.3) |
| [[SHP-77 (line)]] | alt | 59.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -13.4) |
| [[LoVo (line)]] | wt | 4.61 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.104× (z -8.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LS 180 (line)]] | wt | 9.24 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 1.56 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 16.3× (z +8.6) ⚠ unreliable plate only | — |
| [[A-172 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.916 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.892 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.813 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.875 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.890 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.886 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.710 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.832 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.903 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.958 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.02 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6883), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DGKB]] | +0.65 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[CHRM3]] | +0.65 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[NELL1]] | +0.63 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[MIR3681HG]] | +0.63 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[XIRP2]] | +0.59 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[LINC01287]] | +0.59 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[ARNT2-DT]] | +0.57 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[LINC00578]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[TRPM8]] | +0.57 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[FKBP9P1-1]] | +0.57 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[GRIA4]] | +0.57 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[CD96]] | +0.56 | +0.39 / +0.47 | both halves | 6e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHTKD1]] | -0.50 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ALDH6A1]] | -0.47 | -0.24 / -0.55 | both halves | 5e-04 |  |
| [[RAB40B]] | -0.45 | -0.28 / -0.44 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYTL5]] | B | SYTL5 activity raises NYAP2's level | lines that do not express SYTL5 (20) vs lines expressing it (30) | 2.38× lower at baseline in the lines without SYTL5 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400 |
| [[CFI]] | B | CFI activity raises NYAP2's level | lines that do not express CFI (31) vs lines expressing it (19) | 2.41× lower at baseline in the lines without CFI | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1 |
| [[IGFBP5]] | B | IGFBP5 activity raises NYAP2's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 2.61× lower at baseline in the lines without IGFBP5 | 0.023 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2 |
| [[TOP2A]] | B | TOP2A activity lowers NYAP2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RNF17]] | B | RNF17 activity raises NYAP2's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 2.43× lower at baseline in the lines without RNF17 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD |
| [[CCDC152]] | B | CCDC152 activity raises NYAP2's level | lines that do not express CCDC152 (30) vs lines expressing it (20) | 2.06× lower at baseline in the lines without CCDC152 | 0.048 | ⚠ within organs, on part of the lines; also absent: PLAT, SNTG1, COL19A1; maybe low, not absent |
| [[HS6ST2]] | B | HS6ST2 activity raises NYAP2's level | lines that do not express HS6ST2 (28) vs lines expressing it (22) | 1.79× lower at baseline in the lines without HS6ST2 | 0.062 | ⚠ within organs, on part of the lines; also absent: VIPR2, CACNB2, ENSG00000257883 |
| [[KCTD8]] | B | KCTD8 activity raises NYAP2's level | lines that do not express KCTD8 (30) vs lines expressing it (20) | 2.09× lower at baseline in the lines without KCTD8 | 0.081 | ⚠ within organs, on part of the lines; also absent: NOL4, DSCAM, IQCA1 |
| [[LINC02055]] | B | LINC02055 activity raises NYAP2's level | lines that do not express LINC02055 (30) vs lines expressing it (20) | 2.01× lower at baseline in the lines without LINC02055 | 0.082 | ⚠ within organs, on part of the lines; also absent: BAGE2, LINC01446, ENSG00000234352; maybe low, not absent |
| [[SNTG1]] | B | SNTG1 activity raises NYAP2's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 2.84× lower at baseline in the lines without SNTG1 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent |
| [[AIM2]] | C | AIM2 activity raises NYAP2's level | lines that do not express AIM2 (26) vs lines expressing it (24) | 2.11× lower at baseline in the lines without AIM2 | 0.044 | ⚠ within organs, on part of the lines; also absent: PEX5L, PHACTR1, ARMCX2; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PYROXD2]] | B | NYAP2 activity raises PYROXD2's level | lines that do not express NYAP2 (16) vs lines expressing it (34) | 1.78× lower at baseline in the lines without NYAP2 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, CHSY3, AIM2; maybe low, not absent |
| [[SPOCK3]] | B | NYAP2 activity raises SPOCK3's level | lines that do not express NYAP2 (16) vs lines expressing it (34) | 1.82× lower at baseline in the lines without NYAP2 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, CHSY3, AIM2; maybe low, not absent |
| [[MIR3681HG]] | B | NYAP2 activity raises MIR3681HG's level | lines that do not express NYAP2 (16) vs lines expressing it (34) | 3.23× lower at baseline in the lines without NYAP2 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, CHSY3, AIM2; maybe low, not absent |
| [[ALDH6A1]] | B | NYAP2 activity weakens ALDH6A1's drug response | lines that do not express NYAP2 (16) vs lines expressing it (32) | the lines without NYAP2 respond 1.05× as strongly (z diff -0.20); strongest at Dinaciclib 5 µM: 2.66x vs 1.73x (z diff -3.0) | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, CHSY3, AIM2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ALDH6A1]] | B | NYAP2 activity raises ALDH6A1's level | lines that do not express NYAP2 (16) vs lines expressing it (34) | 1.19× lower at baseline in the lines without NYAP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, CHSY3, AIM2; maybe low, not absent |
| [[P2RY1]] | B | NYAP2 activity raises P2RY1's level | lines that do not express NYAP2 (16) vs lines expressing it (34) | 1.67× lower at baseline in the lines without NYAP2 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, CHSY3, AIM2; maybe low, not absent |
| [[OFCC1]] | B | NYAP2 activity raises OFCC1's level | lines that do not express NYAP2 (16) vs lines expressing it (34) | 2.16× lower at baseline in the lines without NYAP2 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, CHSY3, AIM2; maybe low, not absent |
| [[ARHGAP20]] | B | NYAP2 activity raises ARHGAP20's level | lines that do not express NYAP2 (16) vs lines expressing it (34) | 2.07× lower at baseline in the lines without NYAP2 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, CHSY3, AIM2; maybe low, not absent |
| [[LY96]] | B | NYAP2 activity raises LY96's level | lines that do not express NYAP2 (16) vs lines expressing it (34) | 2.15× lower at baseline in the lines without NYAP2 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, CHSY3, AIM2; maybe low, not absent |
| [[DIRC3]] | B | NYAP2 activity raises DIRC3's level | lines that do not express NYAP2 (16) vs lines expressing it (34) | 2.53× lower at baseline in the lines without NYAP2 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, CHSY3, AIM2; maybe low, not absent |
| [[AIM2]] | C | NYAP2 activity raises AIM2's level | lines that do not express NYAP2 (16) vs lines expressing it (34) | 3.52× lower at baseline in the lines without NYAP2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, CHSY3, AIM2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.637). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.8, 31.9); signed map (29.4, 36.3). **Vector** length 56.8, 10.7% of its response variance represented; |z| ≥ 3 in 779 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +14.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +2.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +6.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.8 | +3.8 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -1.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.7 | -4.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -0.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | neuronal tyrosine-phosphorylated phosphoinositide-3-kinase adaptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.3 — chr2:225,399,710-225,729,887 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1486 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P242](https://www.uniprot.org/uniprotkb/Q9P242) (Neuronal tyrosine-phosphorylated phosphoinositide-3-kinase adapter 2):

> Activates PI3K and concomitantly recruits the WAVE1 complex to the close vicinity of PI3K and regulates neuronal morphogenesis.

**Summary**, from NCBI Gene [57624](https://www.ncbi.nlm.nih.gov/gene/57624):

> Predicted to be involved in neuron projection morphogenesis and phosphatidylinositol 3-kinase/protein kinase B signal transduction. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29291](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29291) · Entrez [57624](https://www.ncbi.nlm.nih.gov/gene/57624) · UniProt [Q9P242](https://www.uniprot.org/uniprotkb/Q9P242) · Ensembl [ENSG00000144460](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144460)

## Data

Gene col 6883: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6883); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6883, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6883]; `tensor/DDL_lfc|DDL_z.npy` [6883]; `embed/gene_vectors.npy` [6883]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6883 or target_col == 6883). Every well: [[NYAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NYAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
