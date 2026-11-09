---
symbol: "CRISPLD1"
type: "gene"
col: 4244
ensembl_id: "ENSG00000121005"
name: "cysteine rich secretory protein LCCL domain containing 1"
location: "8q21.13"
module: 9
arm: "+"
pooled_cpm: 9.2
n_lines_expressing: 22
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 1
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# CRISPLD1

*cysteine rich secretory protein LCCL domain containing 1* — 8q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.45× (z +12.1, q 9e-31, up in 10 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 5 µM: 0.641× (z -4.2, q 0.014, down in 11 of 19 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.179×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.05 µM in 1 line (SW480 0.113×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHA5-AS1]] (+0.75, fdr 7e-06), [[EPHA5]] (+0.72, fdr 7e-06), [[CDH10]] (+0.70, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[QPCT]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ELAPOR2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4244.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.45×** | +12.1 | 9e-31 | 10/17 (NCI-H2347, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.16×** | +10.3 | 1e-22 | 10/16 (NCI-H2347, J82, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.75×** | +9.2 | 5e-18 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.16×** | +7.3 | 4e-11 | 0/16 | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.71×** | +7.2 | 6e-11 | 15/20 (A-427, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +6.9 | 5e-10 | 11/20 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +6.0 | 1e-07 | 1/11 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.85×** | +5.6 | 2e-06 | 11/18 (C32, SW 900, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.80×** | +5.6 | 2e-06 | 13/19 (J82, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **2.57×** | +4.7 | 2e-04 | 7/16 (A-427, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.62×** | +4.6 | 2e-04 | 11/20 (A-427, J82, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.60×** | +4.5 | 4e-04 | 6/19 (A-427, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.0 | 0.003 | 6/15 (SHP-77, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.008 | 5/17 (SW 900, H4, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.72×** | +3.7 | 0.009 | 2/14 (HOP62, A-427) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.70×** | +3.6 | 0.012 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.46×** | +3.4 | 0.020 | 9/19 (A-427, NCI-H1573, …) | rises with dose |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.46×** | +3.3 | 0.029 | 2/18 (SK-MEL-2, CHP-212) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.029 | 0/18 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4244.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.179×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.05 µM in 1 line (SW480 0.113×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.641×** | -4.2 | 0.014 | 11/19 (H4, C32, …) | rises with dose |  |
| [[Resveratrol (drug)]] 5 µM |  | 0.775× | -3.4 | 0.18 | 6/20 (C-33 A, HOP62, …) | top dose only | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | 0.698× | -3.3 | 0.20 | 2/20 (NCI-H460, SHP-77) | top dose only |  |
| [[Fusidic acid (drug)]] 5 µM |  | 0.791× | -3.1 | 0.20 | 1/20 (SHP-77) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.722× | -3.1 | 0.20 | 4/19 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[4EGI-1 (drug)]] 0.5 µM |  | 0.635× | -3.1 | 0.20 | 0/20 | inconsistent across doses | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4244. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 193 | 4 (1 ⚠) | 1 (1 ⚠) | [[Binimetinib (drug)]] 5 µM 5.17× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -10.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +11.0) | — |
| [[NCI-H2347 (line)]] | alt | 3.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +12.5) | — |
| [[SW 900 (line)]] | alt | 4.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.96× (z +9.4) | — |
| [[SW480 (line)]] | alt | 2.93 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.113× (z -8.5) |
| [[A-172 (line)]] | wt | 0.838 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.724 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.885 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.785 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.924 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.732 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.818 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.787 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.725 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.935 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.677 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.686 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.617 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.603 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.763 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.785 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.817 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.779 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.657 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.899 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4244), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHA5-AS1]] | +0.75 | +0.69 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[EPHA5]] | +0.72 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[CDH10]] | +0.70 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[ADGRL3]] | +0.69 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[NKAIN2]] | +0.69 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[ARHGAP25]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[CSRNP3]] | +0.66 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[NCAM2]] | +0.66 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[SLITRK5]] | +0.66 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[BCHE]] | +0.65 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ASXL3]] | +0.65 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[FIGN]] | +0.64 | +0.60 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 2, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[QPCT]] | B | QPCT activity lowers CRISPLD1's level | lines that do not express QPCT (25) vs lines expressing it (25) | 1.57× higher at baseline in the lines without QPCT | 0.049 | ⚠ within organs, on part of the lines; also absent: WFDC10B, LRRN1, KRT81 |
| [[GASK1B]] | B | GASK1B activity raises CRISPLD1's level | lines that do not express GASK1B (34) vs lines expressing it (16) | 2.29× lower at baseline in the lines without GASK1B | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B-AS1, HCN1, ENSG00000238054 |
| [[BCHE]] | C | BCHE activity raises CRISPLD1's level | lines that do not express BCHE (35) vs lines expressing it (15) | 5.02× lower at baseline in the lines without BCHE | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[KCNH5]] | C | KCNH5 activity raises CRISPLD1's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 5.15× lower at baseline in the lines without KCNH5 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[FUT9]] | C | FUT9 activity raises CRISPLD1's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 6.58× lower at baseline in the lines without FUT9 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |
| [[CACNB2]] | C | CACNB2 activity raises CRISPLD1's level | lines that do not express CACNB2 (31) vs lines expressing it (19) | 3.79× lower at baseline in the lines without CACNB2 | 0.062 | ⚠ within organs, on part of the lines; also absent: SFTA3-1, DPP10, LINC01035; maybe low, not absent; co-absent with the target |
| [[EPHA5]] | C | EPHA5 activity raises CRISPLD1's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 4.79× lower at baseline in the lines without EPHA5 | 0.062 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[CDH10]] | C | CDH10 activity raises CRISPLD1's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 6.46× lower at baseline in the lines without CDH10 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[FAM133A]] | C | FAM133A activity raises CRISPLD1's level | lines that do not express FAM133A (29) vs lines expressing it (21) | 3.37× lower at baseline in the lines without FAM133A | 0.080 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, TRPC4; co-absent with the target |
| [[PCDH18]] | C | PCDH18 activity raises CRISPLD1's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 2.99× lower at baseline in the lines without PCDH18 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677; co-absent with the target |
| [[GABRG2]] | C | GABRG2 activity raises CRISPLD1's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 2.60× lower at baseline in the lines without GABRG2 | 0.0998 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELAPOR2]] | B | CRISPLD1 activity raises ELAPOR2's level | lines that do not express CRISPLD1 (28) vs lines expressing it (22) | 2.78× lower at baseline in the lines without CRISPLD1 | 0.066 | ⚠ within organs, on part of the lines; also absent: GALNT13, ADAM23, SNCA |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.9, 33.1); signed map (41.0, 35.0). **Vector** length 51.2, 13.2% of its response variance represented; |z| ≥ 3 in 468 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +6.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +4.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | +4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +3.3 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.1 | -3.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | cysteine rich secretory protein LCCL domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.13 — chr8:74,984,505-75,034,558 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Cocoacrisp, DKFZp762F133; previously LCRISP1 |
| Matched by | ensembl_id |

UniProt [Q9H336](https://www.uniprot.org/uniprotkb/Q9H336) carries no function annotation.

**Summary**, from NCBI Gene [83690](https://www.ncbi.nlm.nih.gov/gene/83690):

> Involved in face morphogenesis. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18206](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18206) · Entrez [83690](https://www.ncbi.nlm.nih.gov/gene/83690) · UniProt [Q9H336](https://www.uniprot.org/uniprotkb/Q9H336) · Ensembl [ENSG00000121005](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121005)

## Data

Gene col 4244: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4244); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4244, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4244]; `tensor/DDL_lfc|DDL_z.npy` [4244]; `embed/gene_vectors.npy` [4244]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4244 or target_col == 4244). Every well: [[CRISPLD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRISPLD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
