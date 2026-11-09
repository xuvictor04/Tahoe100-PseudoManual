---
symbol: "HYLS1"
type: "gene"
col: 12572
ensembl_id: "ENSG00000198331"
name: "HYLS1 centriolar and ciliogenesis associated"
location: "11q24.2"
module: 22
arm: "+"
pooled_cpm: 5.37
n_lines_expressing: 45
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 13
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# HYLS1

*HYLS1 centriolar and ciliogenesis associated* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.35× (z +13.6, q 3e-39, up in 28 of 33 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 2.56× (z +10.2, q 8e-22, up in 30 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HOP62 0.121×, NCI-H23 0.151×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (KATO III 0.0681×; ⚠ cell-cycle shift, explains ~14% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DEPDC1]] (+0.73, fdr 7e-06), [[ATF7IP]] (+0.68, fdr 7e-06), [[ASPM]] (+0.68, fdr 7e-06); moves opposite to [[QSOX1]] (-0.58, fdr 1e-05), [[DPM1]] (-0.57, fdr 2e-05), [[IGSF8]] (-0.56, fdr 3e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 13 go from it, the strongest it → [[KIF23]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12572.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.35×** | +13.6 | 3e-39 | 28/33 (NCI-H2030, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.56×** | +10.2 | 8e-22 | 30/40 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +6.5 | 2e-08 | 13/42 (KATO III, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.64×** | +5.5 | 4e-06 | 14/41 (C32, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.62×** | +5.4 | 7e-06 | 13/33 (NCI-H2030, A549, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +4.6 | 4e-04 | 14/42 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.9 | 0.007 | 6/25 (A-427, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +3.8 | 0.012 | 1/11 (HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.26×** | +3.7 | 0.012 | 3/41 (HOP62, HCT15, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.86×** | +3.7 | 0.015 | 4/30 (NCI-H23, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.36×** | +3.3 | 0.050 | 3/39 (A498, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.40×** | +3.3 | 0.054 | 7/40 (NCI-H23, HEC-1-A, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.70×** | +3.1 | 0.078 | 1/10 (NCI-H1573) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +3.1 | 0.080 | 1/6 (NCI-H2030) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.31×** | +3.0 | 0.087 | 5/41 (NCI-H1573, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12572.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HOP62 0.121×, NCI-H23 0.151×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (KATO III 0.0681×; ⚠ cell-cycle shift, explains ~14% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.700× | -3.4 | 0.24 | 10/41 (PANC-1, NCI-H23, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.743× | -3.3 | 0.24 | 13/42 (PANC-1, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12572. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 22.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +11.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.59× (z +9.9) | — |
| [[A549 (line)]] | wt | 6.01 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.68× (z +11.3) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[HOP62 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.121× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 5.80 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0681× (z -9.0) ⚠ cell-cycle shift, explains ~14% of this change |
| [[NCI-H2030 (line)]] | alt | 7.63 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +11.3) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H23 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 4.68 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +9.0) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[A-172 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.717 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.759 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12572), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DEPDC1]] | +0.73 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[ATF7IP]] | +0.68 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[ASPM]] | +0.68 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[KNSTRN]] | +0.67 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[CCNB1]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[NHLRC2]] | +0.67 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[ZNF253]] | +0.67 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[PLK1]] | +0.67 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[ZMYM1]] | +0.65 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[AURKA]] | +0.65 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[HMMR]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[MDC1]] | +0.64 | +0.68 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QSOX1]] | -0.58 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[DPM1]] | -0.57 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[IGSF8]] | -0.56 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[MFN1]] | -0.56 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ZDHHC9]] | -0.55 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[KDELR1]] | -0.53 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[DHDDS]] | -0.53 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[SEZ6L2]] | -0.53 | -0.42 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF23]] | B | HYLS1 activity raises KIF23's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 2.09× lower at baseline in the lines without HYLS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent; its own permutation p |
| [[NDC80]] | B | HYLS1 activity raises NDC80's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 1.99× lower at baseline in the lines without HYLS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent; its own permutation p |
| [[CENPA]] | B | HYLS1 activity raises CENPA's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 1.53× lower at baseline in the lines without HYLS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent; its own permutation p |
| [[NUP62]] | B | HYLS1 activity raises NUP62's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 1.30× lower at baseline in the lines without HYLS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent; its own permutation p |
| [[ARHGAP11A]] | B | HYLS1 activity raises ARHGAP11A's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 1.76× lower at baseline in the lines without HYLS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent |
| [[CCDC102A]] | B | HYLS1 activity raises CCDC102A's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 2.26× lower at baseline in the lines without HYLS1 | 0.064 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent |
| [[PHF19]] | B | HYLS1 activity raises PHF19's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 1.78× lower at baseline in the lines without HYLS1 | 0.076 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent |
| [[CDC20]] | B | HYLS1 activity raises CDC20's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 2.12× lower at baseline in the lines without HYLS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent |
| [[MKI67]] | B | HYLS1 activity raises MKI67's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 1.80× lower at baseline in the lines without HYLS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent |
| [[CENPF]] | B | HYLS1 activity raises CENPF's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 2.10× lower at baseline in the lines without HYLS1 | 0.086 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent |
| [[NUCKS1]] | B | HYLS1 activity raises NUCKS1's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 1.48× lower at baseline in the lines without HYLS1 | 0.093 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent |
| [[NCAPG]] | B | HYLS1 activity raises NCAPG's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 1.88× lower at baseline in the lines without HYLS1 | 0.097 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.588). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.3, -57.7); signed map (-52.4, -45.2). **Vector** length 64.5, 11.0% of its response variance represented; |z| ≥ 3 in 759 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.54 to 28); *Condensation of Prometaphase Chromosomes* (reactome, mean cos +0.51 to 8); *Polo-like kinase mediated events* (reactome, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +5.4 | +13.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.1 | +10.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.2 | +5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.8 | +4.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.3 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +1.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.4 | +1.6 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.3 | +1.3 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -2.4 | -1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -1.9 | -3.3 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.2 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.3 | -2.8 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.2 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | HYLS1 centriolar and ciliogenesis associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:125,883,614-125,900,646 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32915 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96M11](https://www.uniprot.org/uniprotkb/Q96M11) (Centriolar and ciliogenesis-associated protein HYLS1):

> Plays a role in ciliogenesis.

**Summary**, from NCBI Gene [219844](https://www.ncbi.nlm.nih.gov/gene/219844):

> This gene encodes a protein localized to the cytoplasm. Mutations in this gene are associated with hydrolethalus syndrome. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:26558](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26558) · Entrez [219844](https://www.ncbi.nlm.nih.gov/gene/219844) · UniProt [Q96M11](https://www.uniprot.org/uniprotkb/Q96M11) · Ensembl [ENSG00000198331](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198331)

## Data

Gene col 12572: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12572); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12572, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12572]; `tensor/DDL_lfc|DDL_z.npy` [12572]; `embed/gene_vectors.npy` [12572]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12572 or target_col == 12572). Every well: [[HYLS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HYLS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
