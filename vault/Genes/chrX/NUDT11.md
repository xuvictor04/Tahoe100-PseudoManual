---
symbol: "NUDT11"
type: "gene"
col: 12189
ensembl_id: "ENSG00000196368"
name: "nudix hydrolase 11"
location: "Xp11.22"
module: 54
arm: "+"
pooled_cpm: 3.2
n_lines_expressing: 26
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# NUDT11

*nudix hydrolase 11* — Xp11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.65× (z +8.4, q 2e-14, up in 7 of 12 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.79× (z +5.3, q 1e-05, up in 0 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SNU-423 0.0866×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H460 0.0993×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (A-427 0.0784×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (PANC-1 0.398×); [[Cobimetinib (drug)]] 5 µM in 1 line (SK-MEL-2 0.0671×).
> Its strongest partners by |cos| (74 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 26 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELOVL4]] (+0.61, fdr 7e-06), [[ARL4A]] (+0.56, fdr 3e-05), [[RETREG1]] (+0.54, fdr 1e-04); moves opposite to [[CYP27C1]] (-0.54, fdr 3e-05), [[SMG1P6]] (-0.52, fdr 3e-04), [[FBXL8]] (-0.51, fdr 3e-04).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[BIK]] → it (grade B ⚠); 4 go from it, the strongest it → [[DMAC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12189.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **3.65×** | +8.4 | 2e-14 | 7/12 (SNU-423, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.39×** | +7.6 | 7e-12 | 2/4 (PANC-1, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.63×** | +5.8 | 1e-06 | 2/5 (SNU-423, Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.44×** | +5.6 | 3e-06 | 8/12 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.79×** | +5.3 | 1e-05 | 0/21 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **2.13×** | +4.9 | 8e-05 | 5/11 (NCI-H2030, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.99×** | +4.5 | 6e-04 | 7/20 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +4.4 | 6e-04 | 9/12 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.94×** | +4.3 | 0.001 | 12/17 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +4.2 | 0.002 | 13/20 (A549, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.57×** | +4.2 | 0.002 | 7/17 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.81×** | +3.8 | 0.006 | 10/21 (NCI-H23, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.79×** | +3.8 | 0.007 | 11/19 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.37×** | +3.7 | 0.010 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.74×** | +3.6 | 0.012 | 9/21 (NCI-H2030, NCI-H1573, …) | rises with dose | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.16×** | +3.3 | 0.039 | 3/10 (HOP62, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.59×** | +3.0 | 0.081 | 3/19 (A-427, SW 900, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SNU-423 0.0866×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H460 0.0993×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (A-427 0.0784×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (PANC-1 0.398×); [[Cobimetinib (drug)]] 5 µM in 1 line (SK-MEL-2 0.0671×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12189. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 4.98 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0784× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[NCI-H460 (line)]] | wt | 9.02 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0993× (z -10.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 15.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 5.97 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0671× (z -8.6) |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0866× (z -10.9) |
| [[A-172 (line)]] | wt | 0.217 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.734 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.230 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.360 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.208 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.807 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.215 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.212 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.230 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.264 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.187 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.201 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.198 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.199 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.831 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.223 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.226 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.206 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.264 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.286 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12189), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELOVL4]] | +0.61 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ARL4A]] | +0.56 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[RETREG1]] | +0.54 | +0.35 / +0.63 | both halves | 1e-04 |  |
| [[C15orf61]] ⚠ | +0.54 | +0.10 / +0.62 | ⚠ one half (not replicated) | 0.003 | ⚠ in the vector space only through flagged drug-doses |
| [[TUBB2B]] | +0.53 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[CELF4]] | +0.52 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[SHROOM2]] | +0.52 | +0.40 / +0.48 | both halves | 4e-05 |  |
| [[CCDC112]] | +0.52 | +0.24 / +0.60 | both halves | 5e-04 |  |
| [[SLC25A4]] | +0.52 | +0.29 / +0.62 | both halves | 3e-04 |  |
| [[RP9]] | +0.51 | +0.30 / +0.56 | both halves | 2e-04 |  |
| [[NTHL1]] | +0.50 | +0.32 / +0.47 | both halves | 2e-04 |  |
| [[ZNF10]] | +0.50 | +0.31 / +0.50 | both halves | 2e-04 |  |
| [[TCAF1]] | +0.50 | +0.20 / +0.63 | both halves | 7e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 6 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP27C1]] | -0.54 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[SMG1P6]] | -0.52 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[FBXL8]] | -0.51 | -0.27 / -0.57 | both halves | 3e-04 |  |
| [[LENG8-AS1]] | -0.50 | -0.11 / -0.55 | ⚠ one half (not replicated) | 0.002 |  |
| [[BHLHE40-AS1]] | -0.48 | -0.09 / -0.50 | ⚠ one half (not replicated) | 0.003 |  |
| [[SECISBP2]] | -0.48 | -0.12 / -0.43 | ⚠ not reproduced | 0.002 |  |
| [[SUMO3]] | -0.47 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[ERVK13-1]] | -0.47 | +0.11 / -0.52 | ⚠ one half (not replicated) | 1.00 |  |
| [[VPS52]] | -0.47 | -0.03 / -0.59 | ⚠ one half (not replicated) | 0.006 |  |
| [[RABL2B]] | -0.47 | -0.08 / -0.39 | ⚠ not reproduced | 0.003 |  |
| [[PRDM10]] | -0.46 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[CTTN]] | -0.46 | -0.25 / -0.53 | both halves | 4e-04 |  |
| [[DHFR]] | -0.45 | -0.21 / -0.43 | both halves | 6e-04 |  |
| [[DZANK1]] | -0.45 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[OSMR-DT]] | -0.45 | -0.50 / -0.29 | both halves | 2e-04 |  |
| [[AP2B1]] | -0.45 | -0.29 / -0.55 | both halves | 2e-04 |  |
| [[KIAA0753]] | -0.44 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[HCFC1]] | -0.44 | -0.20 / -0.50 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BIK]] | B | BIK activity lowers NUDT11's level | lines that do not express BIK (15) vs lines expressing it (35) | 2.47× higher at baseline in the lines without BIK | 0.012 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |
| [[SNAP91]] | C | SNAP91 activity raises NUDT11's level | lines that do not express SNAP91 (26) vs lines expressing it (24) | 2.05× lower at baseline in the lines without SNAP91 | 0.077 | ⚠ within organs, on part of the lines; also absent: CHST8, PLEKHG4B, COLEC12; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DMAC1]] | B | NUDT11 activity raises DMAC1's level | lines that do not express NUDT11 (24) vs lines expressing it (26) | 1.07× lower at baseline in the lines without NUDT11 | 0.005 | ⚠ within organs, on part of the lines; also absent: RNF182, ADAMTS10, NPTX1 |
| [[DZANK1]] | B | NUDT11 activity raises DZANK1's level | lines that do not express NUDT11 (24) vs lines expressing it (26) | 1.62× lower at baseline in the lines without NUDT11 | 0.026 | ⚠ within organs, on part of the lines; also absent: RNF182, ADAMTS10, NPTX1 |
| [[KIAA0753]] | B | NUDT11 activity raises KIAA0753's level | lines that do not express NUDT11 (24) vs lines expressing it (26) | 1.19× lower at baseline in the lines without NUDT11 | 0.031 | ⚠ within organs, on part of the lines; also absent: RNF182, ADAMTS10, NPTX1 |
| [[ENTREP2]] | B | NUDT11 activity raises ENTREP2's level | lines that do not express NUDT11 (24) vs lines expressing it (26) | 1.12× lower at baseline in the lines without NUDT11 | 0.084 | ⚠ within organs, on part of the lines; also absent: RNF182, ADAMTS10, NPTX1 |

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.367). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (26.2, 11.7); signed map (12.5, 26.4). **Vector** length 28.4, 4.70% of its response variance represented; |z| ≥ 3 in 308 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.1 | +4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +1.7 | +4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +1.6 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +1.6 | +4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | +0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.8 | +0.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.7 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.7 | +1.3 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.9 | -0.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.8 | -2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | +0.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -0.8 | +2.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.6 | -1.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.5 | -2.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.5 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | nudix hydrolase 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.22 — chrX:51,490,011-51,496,592 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DIPP3b, FLJ10628, hDIPP3beta |
| Gene groups (HGNC) | Nudix hydrolase family |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 2 pathways, smallest: Synthesis of pyrophosphates in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96G61](https://www.uniprot.org/uniprotkb/Q96G61) (Diphosphoinositol polyphosphate phosphohydrolase 3-beta):

> Phosphohydrolase that cleaves the beta-phosphate from the diphosphate groups in diphosphoinositol polyphosphate including PP-InsP5 (diphosphoinositol pentakisphosphate) and (PP)2-InsP4 (bis-diphosphoinositol tetrakisphosphate), consistent with a role in signal transduction. With a lower efficiency, can also hydrolyze in vitro dinucleoside oligophosphates including P(1),P(6)-bis(5'-adenosyl) hexaphosphate (Ap6A) and P(1),P(5)-bis(5'-adenosyl) pentaphosphate (Ap5A). It can also hydrolyze …

**Summary**, from NCBI Gene [55190](https://www.ncbi.nlm.nih.gov/gene/55190):

> NUDT11 belongs to a subgroup of phosphohydrolases that preferentially attack diphosphoinositol polyphosphates (Hidaka et al., 2002 [PubMed 12105228]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:18011](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18011) · Entrez [55190](https://www.ncbi.nlm.nih.gov/gene/55190) · UniProt [Q96G61](https://www.uniprot.org/uniprotkb/Q96G61) · Ensembl [ENSG00000196368](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196368)

## Data

Gene col 12189: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12189); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12189, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12189]; `tensor/DDL_lfc|DDL_z.npy` [12189]; `embed/gene_vectors.npy` [12189]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12189 or target_col == 12189). Every well: [[NUDT11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDT11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
