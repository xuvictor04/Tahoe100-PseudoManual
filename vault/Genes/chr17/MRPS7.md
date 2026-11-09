---
symbol: "MRPS7"
type: "gene"
col: 4613
ensembl_id: "ENSG00000125445"
name: "mitochondrial ribosomal protein S7"
location: "17q25.1"
module: 1
arm: "+"
pooled_cpm: 16.58
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# MRPS7

*mitochondrial ribosomal protein S7* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.80× (z +14.6, q 1e-45, up in 29 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.41× (z +5.5, q 5e-06, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.718× (z -3.8, q 0.065, down in 18 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.258×; ⚠ cell-cycle shift, would explain all of this change); [[Ferulic acid (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.125×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (HS-578T 0.189×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AFG1L]] (+0.72, fdr 7e-06), [[FASTKD2]] (+0.71, fdr 7e-06), [[LANCL2]] (+0.70, fdr 7e-06); moves opposite to [[LINC01881]] (-0.66, fdr 1e-05), [[STK32C]] (-0.61, fdr 2e-05), [[GMCL1]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4613.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.80×** | +14.6 | 1e-45 | 29/31 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.59×** | +14.5 | 3e-45 | 38/41 (A498, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.04×** | +7.5 | 1e-11 | 27/36 (A549, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +5.5 | 5e-06 | 27/43 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.5 | 5e-06 | 30/48 (SNU-423, NCI-H23, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.55×** | +4.8 | 1e-04 | 26/46 (NCI-H1792, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.48×** | +4.4 | 8e-04 | 21/46 (A549, A498, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.31×** | +4.3 | 0.001 | 28/47 (A549, NCI-H1792, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +4.0 | 0.005 | 22/47 (HT-29, SK-MEL-2, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.42×** | +3.9 | 0.005 | 21/43 (J82, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.27×** | +3.8 | 0.006 | 19/48 (PANC-1, J82, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.031 | 15/48 (Panc 03.27, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.70×** | +3.1 | 0.076 | 15/48 (COLO 205, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.69×** | +3.1 | 0.077 | 7/45 (NCI-H2347, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4613.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.258×; ⚠ cell-cycle shift, would explain all of this change); [[Ferulic acid (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.125×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (HS-578T 0.189×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.718×** | -3.8 | 0.065 | 18/47 (SW480, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.796×** | -3.7 | 0.065 | 21/48 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.743× | -3.4 | 0.13 | 17/47 (A498, RKO, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | 0.748× | -3.3 | 0.13 | 15/47 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | 0.592× | -3.1 | 0.21 | 16/48 (SNU-1, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4613. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 18.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A498 (line)]] | wt | 18.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.53× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[KATO III (line)]] | alt | 25.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.03× (z +10.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 12.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.39× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 27.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HEC-1-A (line)]] | alt | 23.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.29× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 15.6 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.5 µM 0.125× (z -9.2) |
| [[HS-578T (line)]] | alt | 12.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.189× (z -8.5) |
| [[J82 (line)]] | alt | 17.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[LoVo (line)]] | wt | 13.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 16.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2030 (line)]] | alt | 17.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H460 (line)]] | wt | 16.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.54× (z +11.5) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 19.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[PANC-1 (line)]] | alt | 17.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 22.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[AN3 CA (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4613), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AFG1L]] | +0.72 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[FASTKD2]] | +0.71 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[LANCL2]] | +0.70 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[GTF3C6]] | +0.70 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[VPS52]] | +0.70 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[ZNF629]] | +0.69 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[SNAPC5]] | +0.68 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[GATB]] | +0.67 | +0.75 / +0.53 | both halves | 1e-05 | STRING 571 |
| [[TACO1]] | +0.66 | +0.69 / +0.53 | both halves | 1e-05 | STRING 613 |
| [[FUNDC1]] | +0.66 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[UTP20]] | +0.66 | +0.66 / +0.55 | both halves | 1e-05 | STRING 623 |
| [[DNAJC11]] | +0.66 | +0.70 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01881]] | -0.66 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[STK32C]] | -0.61 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[GMCL1]] | -0.60 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[PCMT1]] | -0.60 | -0.62 / -0.37 | both halves | 7e-05 |  |
| [[SGK3]] | -0.60 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[DNAAF3]] | -0.59 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[SERAC1]] | -0.58 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[SLC17A5]] | -0.58 | -0.64 / -0.38 | both halves | 6e-05 |  |
| [[BRI3]] | -0.58 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[MPST]] | -0.57 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[RPS21]] | -0.57 | -0.55 / -0.46 | both halves | 3e-05 | STRING 951 |
| [[CDKN2D]] | -0.57 | -0.51 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises MRPS7's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[VPS35L]] | B | VPS35L activity raises MRPS7's level | lines that do not express VPS35L (9) vs lines expressing it (41) | 1.24× lower at baseline in the lines without VPS35L | 0.032 | ⚠ within organs, on part of the lines; also absent: HDGFL3, CHST11, RNF150 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.529). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.0, 11.3); signed map (11.3, -30.9). **Vector** length 56.2, 10.0% of its response variance represented; |z| ≥ 3 in 600 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.6 | +3.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +3.4 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +2.8 | +14.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +2.7 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -3.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.9 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -2.8 | -3.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.4 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -0.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,261,674-75,266,376 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRP-S, RP-S7, RPMS7, uS7m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9Y2R9](https://www.uniprot.org/uniprotkb/Q9Y2R9) carries no function annotation.

**Summary**, from NCBI Gene [51081](https://www.ncbi.nlm.nih.gov/gene/51081):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14499](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14499) · Entrez [51081](https://www.ncbi.nlm.nih.gov/gene/51081) · UniProt [Q9Y2R9](https://www.uniprot.org/uniprotkb/Q9Y2R9) · Ensembl [ENSG00000125445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125445)

## Data

Gene col 4613: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4613); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4613, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4613]; `tensor/DDL_lfc|DDL_z.npy` [4613]; `embed/gene_vectors.npy` [4613]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4613 or target_col == 4613). Every well: [[MRPS7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
