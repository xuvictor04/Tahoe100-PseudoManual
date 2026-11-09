---
symbol: "NECTIN3"
type: "gene"
col: 10858
ensembl_id: "ENSG00000177707"
name: "nectin cell adhesion molecule 3"
location: "3q13.13"
module: 111
arm: "+"
pooled_cpm: 88.35
n_lines_expressing: 39
n_dd_up: 2
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# NECTIN3

*nectin cell adhesion molecule 3* — 3q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.44× (z +9.1, q 4e-17, up in 23 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (A498 2.40×, RKO 2.66×, RPMI-7951 1.97×, SW 900 1.98×, …); [[Tucidinostat (drug)]] 5 µM in 3 lines (NCI-H2347 1.88×, PANC-1 2.04×, NCI-H23 2.20×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 3.06×, SW 900 2.70×).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.761× (z -4.5, q 0.003, down in 18 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Docetaxel (Trihydrate) (drug)]] 0.5 µM: 0.813× (z -3.4, q 0.089, down in 14 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H1792 0.428×, HOP62 0.484×, A-172 0.568×, SK-MEL-2 0.599×; ⚠ cell-cycle shift, explains ~69% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-427 0.428×, J82 0.433×, SHP-77 0.362×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (J82 0.351×, A-172 0.443×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW 1271 0.102×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (AN3 CA 0.145×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEPTIN11]] (+0.58, fdr 2e-05), [[ATP11C]] (+0.56, fdr 1e-05), [[LAMC1]] (+0.55, fdr 2e-05); moves opposite to [[GOLPH3L]] (-0.55, fdr 1e-05), [[DDX19B]] (-0.54, fdr 3e-05), [[NFKBIL1]] (-0.52, fdr 3e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RFTN1]] → it (grade B ⚠); 4 go from it, the strongest it → [[LTBP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10858.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (A498 2.40×, RKO 2.66×, RPMI-7951 1.97×, SW 900 1.98×, …); [[Tucidinostat (drug)]] 5 µM in 3 lines (NCI-H2347 1.88×, PANC-1 2.04×, NCI-H23 2.20×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 3.06×, SW 900 2.70×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +9.1 | 4e-17 | 23/38 (A498, RKO, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.6 | 0.001 | 21/37 (RKO, SW 900, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Filgotinib (drug)]] 5 µM |  | 1.20× | +3.3 | 0.16 | 11/37 (LOX-IMVI, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.2 | 0.16 | 14/37 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.2 | 0.16 | 12/36 (A-172, SW 900, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.1 | 0.21 | 12/37 (CFPAC-1, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10858.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H1792 0.428×, HOP62 0.484×, A-172 0.568×, SK-MEL-2 0.599×; ⚠ cell-cycle shift, explains ~69% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-427 0.428×, J82 0.433×, SHP-77 0.362×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (J82 0.351×, A-172 0.443×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW 1271 0.102×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (AN3 CA 0.145×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.761×** | -4.5 | 0.003 | 18/35 (J82, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **0.781×** | -4.4 | 0.003 | 22/37 (hTERT-HPNE, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 0.852× | -4.0 | 0.010 | 16/37 (NCI-H1792, HOP62, …) | inconsistent across doses | composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.813×** | -3.4 | 0.089 | 14/37 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | 0.829× | -3.1 | 0.22 | 17/38 (A-427, J82, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | 0.845× | -3.0 | 0.25 | 16/37 (LOX-IMVI, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10858. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 27.0 | 5 (4 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.88× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.04× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 38.1 | 4 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.20× (z +9.0) | — |
| [[A498 (line)]] | wt | 78.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.61× (z +16.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +15.7) | — |
| [[J82 (line)]] | alt | 212 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.351× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 164 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -9.4) ⚠ cell-cycle shift, explains ~69% of this change |
| [[RKO (line)]] | wt | 57.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +12.1) | — |
| [[SW 900 (line)]] | alt | 62.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +8.9) | — |
| [[A-427 (line)]] | wt | 353 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[AN3 CA (line)]] | alt | 58.7 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.145× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 100 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.5) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[HEC-1-A (line)]] | alt | 191 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.489× (z -8.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 234 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -10.2) ⚠ cell-cycle shift, explains ~69% of this change |
| [[NCI-H1792 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -14.5) ⚠ cell-cycle shift, explains ~69% of this change |
| [[NCI-H2347 (line)]] | alt | 78.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.88× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 85.6 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.197× (z -8.8) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 118 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 62.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[SK-MEL-2 (line)]] | alt | 159 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.599× (z -8.6) ⚠ cell-cycle shift, explains ~69% of this change |
| [[SW 1271 (line)]] | alt | 95.7 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.102× (z -10.6) |
| [[A549 (line)]] | wt | 158 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 52.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 68.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.73 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.68 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 99.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 83.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 196 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 187 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 46.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 177 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 94.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.27 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 19.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.53 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.70 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10858), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN11]] | +0.58 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[ATP11C]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[LAMC1]] | +0.55 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[GNG12]] | +0.52 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[FSTL1]] | +0.51 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[MOB1A]] | +0.49 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[KALRN]] | +0.48 | +0.47 / +0.40 | both halves | 5e-05 | same gene group |
| [[PRPS2]] | +0.48 | +0.45 / +0.38 | both halves | 7e-05 |  |
| [[GLI3]] | +0.48 | +0.46 / +0.34 | both halves | 1e-04 |  |
| [[SNX7]] | +0.47 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[PGRMC1]] | +0.47 | +0.38 / +0.44 | both halves | 7e-05 |  |
| [[RBMS1]] | +0.47 | +0.43 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLPH3L]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[DDX19B]] | -0.54 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[NFKBIL1]] | -0.52 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[PICK1]] | -0.51 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[TARS2]] | -0.49 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[MRPL54]] | -0.49 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[BCAS2]] | -0.49 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[PRPF6]] | -0.48 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[CRTC1]] | -0.47 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[RPAIN]] | -0.47 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[SMN1]] | -0.47 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[CLASRP]] | -0.45 | -0.43 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RFTN1]] | B | RFTN1 activity raises NECTIN3's level | lines that do not express RFTN1 (20) vs lines expressing it (30) | 3.64× lower at baseline in the lines without RFTN1 | 0.017 | ⚠ within organs, on part of the lines; also absent: GPR176, KIAA0408, COL12A1 |
| [[TOP2A]] | B | TOP2A activity lowers NECTIN3's level | compounds that target TOP2A: 2 of 5 raise it (Doxorubicin, Idarubicin) | 40% of the class's compounds vs 0.6% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LTBP1]] | B | NECTIN3 activity raises LTBP1's level | lines that do not express NECTIN3 (11) vs lines expressing it (39) | 2.13× lower at baseline in the lines without NECTIN3 | 0.052 | ⚠ within organs, on part of the lines; also absent: CD96, NECTIN3-AS1, GPR176 |
| [[RAB23]] | B | NECTIN3 activity raises RAB23's level | lines that do not express NECTIN3 (11) vs lines expressing it (39) | 1.76× lower at baseline in the lines without NECTIN3 | 0.060 | ⚠ within organs, on part of the lines; also absent: CD96, NECTIN3-AS1, GPR176 |
| [[RFTN1]] | B | NECTIN3 activity raises RFTN1's level | lines that do not express NECTIN3 (11) vs lines expressing it (39) | 3.37× lower at baseline in the lines without NECTIN3 | 0.061 | ⚠ within organs, on part of the lines; also absent: CD96, NECTIN3-AS1, GPR176 |
| [[CDH2]] | C | NECTIN3 activity raises CDH2's level | lines that do not express NECTIN3 (11) vs lines expressing it (39) | 6.23× lower at baseline in the lines without NECTIN3 | 0.020 | ⚠ within organs, on part of the lines; also absent: CD96, NECTIN3-AS1, GPR176; co-absent with the target |

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.352). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-55.3, -1.6); signed map (-5.8, 36.6). **Vector** length 79.4, 19.0% of its response variance represented; |z| ≥ 3 in 682 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +9.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | +3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +1.5 | +1.4 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | +1.4 | +2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +3.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.4 | -2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -2.4 | -4.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.4 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -2.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.6 | -3.4 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -1.4 | -1.4 |
|  | [[Oxaprozin (drug)]] 0.05 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | nectin cell adhesion molecule 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.13 — chr3:111,070,071-111,275,563 (+) |
| Ensembl biotype | protein_coding |
| Also known as | nectin-3, PPR3, PVRR3, DKFZP566B0846, CDw113, CD113; previously PVRL3 |
| Gene groups (HGNC) | CD molecules; V-set domain containing; C2-set domain containing; I-set domain containing; Nectins and nectin-like molecules |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 5 pathways, smallest: Nectin/Necl  trans heterodimerization; Adherens junctions interactions; Cell-cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQS3](https://www.uniprot.org/uniprotkb/Q9NQS3) (Nectin-3):

> Cell adhesion molecule that promotes cell-cell adhesion through heterophilic trans-interactions with nectins-like or other nectins, such as trans-interaction with NECTIN2 at Sertoli-spermatid junctions. Trans-interaction with PVR induces activation of CDC42 and RAC small G proteins through common signaling molecules such as SRC and RAP1. Induces endocytosis-mediated down-regulation of PVR from the cell surface, resulting in reduction of cell movement and proliferation. Involved in axon guidance …

**Summary**, from NCBI Gene [25945](https://www.ncbi.nlm.nih.gov/gene/25945):

> This gene encodes a member of the nectin family of proteins, which function as adhesion molecules at adherens junctions. This family member interacts with other nectin-like proteins and with afadin, a filamentous actin-binding protein involved in the regulation of directional motility, cell proliferation and survival. This gene plays a role in ocular development involving the ciliary body. Mutations in this gene are believed to result in congenital ocular defects. Alternative splicing results …

**Accessions** — [HGNC:17664](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17664) · Entrez [25945](https://www.ncbi.nlm.nih.gov/gene/25945) · UniProt [Q9NQS3](https://www.uniprot.org/uniprotkb/Q9NQS3) · Ensembl [ENSG00000177707](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177707)

## Data

Gene col 10858: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10858); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10858, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10858]; `tensor/DDL_lfc|DDL_z.npy` [10858]; `embed/gene_vectors.npy` [10858]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10858 or target_col == 10858). Every well: [[NECTIN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NECTIN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
