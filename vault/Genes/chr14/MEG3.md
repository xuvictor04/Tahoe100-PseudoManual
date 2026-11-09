---
symbol: "MEG3"
type: "gene"
col: 13208
ensembl_id: "ENSG00000214548"
name: "maternally expressed 3"
location: "14q32.2"
module: 13
arm: "+"
pooled_cpm: 29.46
n_lines_expressing: 15
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 34
direction_downstream: 28
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# MEG3

*maternally expressed 3* — 14q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.02× (z +8.5, q 1e-14, up in 4 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.56× (z +4.8, q 2e-04, up in 8 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW 1088 0.142×, NCI-H23 0.182×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (PANC-1 0.380×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MEG8]] (+0.91, fdr 7e-06, ⚠ same locus), [[MIR493HG]] (+0.89, fdr 7e-06, ⚠ same locus), [[PLEKHG4B]] (+0.66, fdr 7e-06), [[VSTM4]] (+0.64, fdr 7e-06), [[LINC01411]] (+0.64, fdr 7e-06); moves opposite to [[SRGN]] (-0.49, fdr 7e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 34 arrows point to it, the strongest [[EPHB1]] → it (grade B ⚠); 28 go from it, the strongest it → [[EML1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13208.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.02×** | +8.5 | 1e-14 | 4/14 (NCI-H1573, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +6.4 | 5e-08 | 2/8 (PANC-1, SNU-423) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +5.7 | 2e-06 | 1/11 (NCI-H1573) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +4.8 | 2e-04 | 8/13 (CFPAC-1, SNU-423, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.7 | 0.023 | 2/12 (SNU-423, AN3 CA) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.028 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.57×** | +3.4 | 0.048 | 0/13 | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.49× | +3.1 | 0.15 | 6/13 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13208.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW 1088 0.142×, NCI-H23 0.182×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (PANC-1 0.380×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | 0.630× | -3.6 | 0.18 | 7/12 (NCI-H1573, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.655× | -3.3 | 0.18 | 6/13 (hTERT-HPNE, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.659× | -3.2 | 0.18 | 3/13 (NCI-H1573, HOP62, …) | inconsistent across doses | position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.637× | -3.2 | 0.18 | 1/13 (NCI-H23) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13208. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 7.49 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 11.1× (z +11.7) | — |
| [[HOP62 (line)]] | alt | 38.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.10× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 46.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -8.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 207 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -8.9) |
| [[SNU-423 (line)]] | alt | 26.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.53× (z +9.5) | — |
| [[SW 1088 (line)]] | alt | 837 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -8.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.44 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.88 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.52 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.51 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.79 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.74 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 680 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.34 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.41 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.41 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.66 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.39 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.57 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.95 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13208), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEG8]] | +0.91 | +0.88 / +0.90 | both halves | 7e-06 | same gene group; ⚠ same locus (22.0 kb, same strand: neighbours can correlate without regulation) |
| [[MIR493HG]] | +0.89 | +0.86 / +0.86 | both halves | 7e-06 | same gene group; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PLEKHG4B]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[VSTM4]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[LINC01411]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[AGPAT4]] | +0.63 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[INHBA]] | +0.63 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[KCNMA1]] | +0.63 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[ADAMTS16]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[INSYN2B]] | +0.60 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[ADAMTS6]] | +0.60 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[COL5A1]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[CSF1R]] | +0.59 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[FZD8]] | +0.58 | +0.63 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGN]] | -0.49 | -0.45 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 3, C 31. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHB1]] | B | EPHB1 activity raises MEG3's level | lines that do not express EPHB1 (16) vs lines expressing it (34) | 2.34× lower at baseline in the lines without EPHB1 | 0.027 | ⚠ within organs, on part of the lines; also absent: KCNG1, DOCK2, GLIS1; maybe low, not absent |
| [[CACNG7]] | B | CACNG7 activity raises MEG3's level | lines that do not express CACNG7 (21) vs lines expressing it (29) | 2.60× lower at baseline in the lines without CACNG7 | 0.061 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |
| [[COL5A3]] | B | COL5A3 activity raises MEG3's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 1.90× lower at baseline in the lines without COL5A3 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[MIR493HG]] | C | MIR493HG activity raises MEG3's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 13.62× lower at baseline in the lines without MIR493HG | 3e-05 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252; co-absent with the target |
| [[MEG8]] | C | MEG8 activity raises MEG3's level | lines that do not express MEG8 (32) vs lines expressing it (18) | 8.07× lower at baseline in the lines without MEG8 | 0.001 | ⚠ within organs, on part of the lines; also absent: MEG3, MIR493HG, MXRA8; co-absent with the target |
| [[EVC2]] | C | EVC2 activity raises MEG3's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 4.99× lower at baseline in the lines without EVC2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7; co-absent with the target |
| [[GDNF]] | C | GDNF activity raises MEG3's level | lines that do not express GDNF (38) vs lines expressing it (12) | 3.74× lower at baseline in the lines without GDNF | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9; co-absent with the target |
| [[GDNF-AS1]] | C | GDNF-AS1 activity raises MEG3's level | lines that do not express GDNF-AS1 (23) vs lines expressing it (27) | 3.02× lower at baseline in the lines without GDNF-AS1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent; co-absent with the target |
| [[INSYN2B]] | C | INSYN2B activity raises MEG3's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 4.13× lower at baseline in the lines without INSYN2B | 0.014 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |
| [[GREM1]] | C | GREM1 activity raises MEG3's level | lines that do not express GREM1 (38) vs lines expressing it (12) | 4.12× lower at baseline in the lines without GREM1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000203434, LINC01098, AFP; co-absent with the target |
| [[ADAMTS18]] | C | ADAMTS18 activity raises MEG3's level | lines that do not express ADAMTS18 (23) vs lines expressing it (27) | 4.19× lower at baseline in the lines without ADAMTS18 | 0.020 | ⚠ within organs, on part of the lines; also absent: TSHZ3, TWIST2, INSYN2B; maybe low, not absent; co-absent with the target |
| [[CRMP1]] | C | CRMP1 activity raises MEG3's level | lines that do not express CRMP1 (19) vs lines expressing it (31) | 3.30× lower at baseline in the lines without CRMP1 | 0.029 | ⚠ within organs, on part of the lines; also absent: JAM3, NHSL2, ENSG00000286033; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 10, C 18. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EML1]] | B | MEG3 activity raises EML1's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 2.99× lower at baseline in the lines without MEG3 | 0.025 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8 |
| [[LINC01119]] | B | MEG3 activity strengthens LINC01119's drug response | lines that do not express MEG3 (30) vs lines expressing it (13) | the lines without MEG3 respond 0.64× as strongly (z diff +1.20); strongest at Panobinostat 0.5 µM: 0.61x vs 0.21x (z diff +4.1) | 0.039 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8; target measured in part of the lines; artifact flags |
| [[SMTN]] | B | MEG3 activity raises SMTN's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 1.59× lower at baseline in the lines without MEG3 | 0.043 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8 |
| [[LINC01119]] | B | MEG3 activity raises LINC01119's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 1.97× lower at baseline in the lines without MEG3 | 0.043 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8 |
| [[COL5A3]] | B | MEG3 activity raises COL5A3's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 2.50× lower at baseline in the lines without MEG3 | 0.049 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8 |
| [[TRIM9]] | B | MEG3 activity raises TRIM9's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 2.69× lower at baseline in the lines without MEG3 | 0.067 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8 |
| cells under [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM | B | MEG3 activity lowers the cells' numbers under Dapagliflozin ((2S)-1,2-propanediol, hydrate) 0.5 µM (makes them more sensitive) | lines that do not express MEG3 (35) vs lines expressing it (13) | the lines without MEG3: 1.21× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8 |
| [[MYO10]] | B | MEG3 activity raises MYO10's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 1.61× lower at baseline in the lines without MEG3 | 0.092 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8 |
| [[LTBP4]] | B | MEG3 activity raises LTBP4's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 1.43× lower at baseline in the lines without MEG3 | 0.095 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8 |
| [[AFF3]] | B | MEG3 activity raises AFF3's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 3.39× lower at baseline in the lines without MEG3 | 0.098 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8 |
| [[MIR493HG]] | C | MEG3 activity raises MIR493HG's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 6.02× lower at baseline in the lines without MEG3 | 8e-04 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8; co-absent with the target |
| [[MEG8]] | C | MEG3 activity raises MEG8's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 10.13× lower at baseline in the lines without MEG3 | 8e-04 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.5, 15.8); signed map (22.6, 48.5). **Vector** length 42.0, 13.1% of its response variance represented; |z| ≥ 3 in 282 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective B3GALTL causes PpS* (reactome, mean cos +0.50 to 8); *O-glycosylation of TSR domain-containing proteins* (reactome, mean cos +0.50 to 8); *Diseases associated with O-glycosylation of proteins* (reactome, mean cos +0.50 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.2 | +1.9 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.2 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -3.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -3.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.5 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.3 | -1.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | maternally expressed 3 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q32.2 — chr14:100,779,410-100,861,031 (+) |
| Ensembl biotype | lncRNA |
| Also known as | Lnc-DLK1-35, GTL2, NCRNA00023, LINC00023, onco-lncRNA-83 |
| Gene groups (HGNC) | MicroRNA non-coding host genes; Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [55384](https://www.ncbi.nlm.nih.gov/gene/55384):

> This gene is a maternally expressed imprinted gene. Multiple alternatively spliced transcript variants have been transcribed from this gene and all of them are long non-coding RNAs (lncRNAs). This gene is expressed in many normal tissues, but its expression is lost in multiple cancer cell lines of various tissue origins. It inhibits tumor cell proliferation in vitro. It also interacts with the tumor suppressor p53, and regulates p53 target gene expression. Its deletion enhances angiogenesis in …

**Accessions** — [HGNC:14575](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14575) · Entrez [55384](https://www.ncbi.nlm.nih.gov/gene/55384) · Ensembl [ENSG00000214548](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214548)

## Data

Gene col 13208: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13208); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13208, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13208]; `tensor/DDL_lfc|DDL_z.npy` [13208]; `embed/gene_vectors.npy` [13208]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13208 or target_col == 13208). Every well: [[MEG3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEG3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
