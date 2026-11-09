---
symbol: "SLC26A4"
type: "gene"
col: 1655
ensembl_id: "ENSG00000091137"
name: "solute carrier family 26 member 4"
location: "7q22.3"
module: 53
arm: "+"
pooled_cpm: 3.56
n_lines_expressing: 43
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 29
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# SLC26A4

*solute carrier family 26 member 4* — 7q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.01× (z +9.6, q 3e-19, up in 2 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.61× (z +8.7, q 8e-16, up in 21 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.639× (z -4.1, q 0.013, down in 13 of 40 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.474× (z -3.6, q 0.063, down in 11 of 20 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (A-427 0.158×, NCI-H23 0.0719×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HOP62 0.0564×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HOP62 0.0685×; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 5 µM in 1 line (A-427 0.0389×); [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM in 1 line (A-172 0.0479×); [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (NCI-H2030 0.0774×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01588]] (+0.71, fdr 7e-06), [[MEI1]] (+0.71, fdr 7e-06), [[PKD1L1]] (+0.71, fdr 7e-06); moves opposite to [[IFT172]] (-0.57, fdr 3e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 29 go from it, the strongest it → [[LINC01191]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1655.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.01×** | +9.6 | 3e-19 | 2/5 (HS-578T, A-427) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.61×** | +8.7 | 8e-16 | 21/34 (LoVo, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.53×** | +7.8 | 1e-12 | 2/6 (HS-578T, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +7.5 | 8e-12 | 12/28 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +6.9 | 6e-10 | 15/31 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.88×** | +5.7 | 1e-06 | 15/40 (RKO, A498, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +5.5 | 3e-06 | 9/39 (A498, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.51×** | +5.3 | 8e-06 | 3/39 (A498, NCI-H460, …) | top dose only | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.8 | 8e-05 | 3/12 (A498, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +4.8 | 1e-04 | 9/23 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +4.7 | 2e-04 | 3/12 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +4.6 | 2e-04 | 8/31 (HEC-1-A, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.50×** | +3.5 | 0.019 | 5/30 (LoVo, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.023 | 4/39 (A-427, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.030 | 7/33 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.042 | 1/37 (SW480) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.39×** | +2.9 | 0.097 | 2/38 (CFPAC-1, A498) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1655.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (A-427 0.158×, NCI-H23 0.0719×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HOP62 0.0564×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HOP62 0.0685×; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 5 µM in 1 line (A-427 0.0389×); [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM in 1 line (A-172 0.0479×); [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (NCI-H2030 0.0774×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.639×** | -4.1 | 0.013 | 13/40 (A-427, NCI-H23, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.643×** | -4.1 | 0.013 | 8/19 (A-427, NCI-H23, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.474×** | -3.6 | 0.063 | 11/20 (A-427, HOP62, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.694× | -3.4 | 0.10 | 4/36 (A-427, RKO, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.710× | -3.2 | 0.16 | 15/39 (NCI-H23, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Salicylic acid (drug)]] 5 µM |  | 0.787× | -3.1 | 0.16 | 5/39 (COLO 205, HEC-1-A, …) | top dose only |  |
| [[Quinestrol (drug)]] 5 µM |  | 0.793× | -3.1 | 0.17 | 3/39 (HCT15, SW 900, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.703× | -3.0 | 0.17 | 11/35 (HS-578T, NCI-H2030, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1655. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 42.3 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -11.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0389× (z -9.7) |
| [[HOP62 (line)]] | alt | 6.30 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0564× (z -12.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.35 | 0 | 1 | — | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM 0.0479× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 7.75 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0774× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0719× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A498 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.857 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.943 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.783 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.831 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.893 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.808 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.903 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.845 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1655), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01588]] | +0.71 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[MEI1]] | +0.71 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[PKD1L1]] | +0.71 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[ASGR1]] | +0.70 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[EFCAB8]] | +0.69 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[DPYS]] | +0.69 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[GRK4]] | +0.67 | +0.66 / +0.58 | both halves | 8e-06 |  |
| [[SLC6A13]] | +0.66 | +0.67 / +0.52 | both halves | 1e-05 | pathway: SLC-mediated transmembrane transport |
| [[NUP210L]] | +0.66 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[XG]] | +0.66 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[ZPLD1]] | +0.65 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[LINC00393]] | +0.65 | +0.50 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT172]] | -0.57 | -0.45 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC26A4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZPLD1]] | B | ZPLD1 activity lowers SLC26A4's level | lines that do not express ZPLD1 (7) vs lines expressing it (43) | 1.53× higher at baseline in the lines without ZPLD1 | 0.024 | ⚠ within organs, on part of the lines; also absent: STAT4, ABCA12, ANKRD7; maybe low, not absent |
| [[MRC2]] | B | MRC2 activity raises SLC26A4's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 1.74× lower at baseline in the lines without MRC2 | 0.049 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1 |
| [[MSRB3]] | B | MSRB3 activity raises SLC26A4's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 1.71× lower at baseline in the lines without MSRB3 | 0.058 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |

### Downstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 29, C 0. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01191]] | B | SLC26A4 activity raises LINC01191's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 2.02× lower at baseline in the lines without SLC26A4 | 0.003 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[SLC4A5]] | B | SLC26A4 activity raises SLC4A5's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.71× lower at baseline in the lines without SLC26A4 | 0.008 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[LINC01588]] | B | SLC26A4 activity raises LINC01588's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.88× lower at baseline in the lines without SLC26A4 | 0.009 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[MIRLET7IHG]] | B | SLC26A4 activity raises MIRLET7IHG's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.71× lower at baseline in the lines without SLC26A4 | 0.010 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[PPIEL-1]] | B | SLC26A4 activity raises PPIEL-1's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.66× lower at baseline in the lines without SLC26A4 | 0.011 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[USP50]] | B | SLC26A4 activity raises USP50's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.38× lower at baseline in the lines without SLC26A4 | 0.015 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[PILRA]] | B | SLC26A4 activity raises PILRA's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.80× lower at baseline in the lines without SLC26A4 | 0.016 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[WNK4]] | B | SLC26A4 activity raises WNK4's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 2.46× lower at baseline in the lines without SLC26A4 | 0.017 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[ALDH8A1]] | B | SLC26A4 activity raises ALDH8A1's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.63× lower at baseline in the lines without SLC26A4 | 0.019 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[ANKDD1B]] | B | SLC26A4 activity raises ANKDD1B's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.59× lower at baseline in the lines without SLC26A4 | 0.019 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[LINC02936]] | B | SLC26A4 activity raises LINC02936's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.83× lower at baseline in the lines without SLC26A4 | 0.020 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[ZDHHC11]] | B | SLC26A4 activity raises ZDHHC11's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.47× lower at baseline in the lines without SLC26A4 | 0.030 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.669). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.3, -12.2); signed map (21.6, 8.5). **Vector** length 49.4, 6.55% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.7 | +8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +0.2 |
| fall | [[Radotinib (drug)]] 5 µM |  | -2.5 | -2.5 |
|  | [[NG25 (drug)]] 5 µM |  | -2.0 | -3.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.6 | -3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -0.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -2.2 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 26 member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.3 — chr7:107,660,828-107,717,809 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PDS; previously DFNB4 |
| Gene groups (HGNC) | Solute carrier family 26 |
| Reactome | 6 pathways, smallest: Inorganic anion exchange by SLC26 transporters; SLC-mediated transport of inorganic anions; SLC transporter disorders |
| Matched by | ensembl_id |

**Function**, from UniProt [O43511](https://www.uniprot.org/uniprotkb/O43511) (Pendrin):

> Sodium-independent transporter of chloride and iodide. Mediates electroneutral chloride-bicarbonate, chloride-iodide and chloride-formate exchange with 1:1 stoichiometry. Mediates electroneutral iodide-bicarbonate exchange (By similarity).

**Summary**, from NCBI Gene [5172](https://www.ncbi.nlm.nih.gov/gene/5172):

> Mutations in this gene are associated with Pendred syndrome, the most common form of syndromic deafness, an autosomal-recessive disease. It is highly homologous to the SLC26A3 gene; they have similar genomic structures and this gene is located 3' of the SLC26A3 gene. The encoded protein has homology to sulfate transporters. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8818](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8818) · Entrez [5172](https://www.ncbi.nlm.nih.gov/gene/5172) · UniProt [O43511](https://www.uniprot.org/uniprotkb/O43511) · Ensembl [ENSG00000091137](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091137)

## Data

Gene col 1655: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1655); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1655, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1655]; `tensor/DDL_lfc|DDL_z.npy` [1655]; `embed/gene_vectors.npy` [1655]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1655 or target_col == 1655). Every well: [[SLC26A4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC26A4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
