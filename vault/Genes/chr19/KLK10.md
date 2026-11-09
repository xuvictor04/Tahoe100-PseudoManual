---
symbol: "KLK10"
type: "gene"
col: 4972
ensembl_id: "ENSG00000129451"
name: "kallikrein related peptidase 10"
location: "19q13.41"
module: 73
arm: "+"
pooled_cpm: 32.57
n_lines_expressing: 16
n_dd_up: 3
n_dd_down: 18
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 110
direction_downstream: 141
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# KLK10

*kallikrein related peptidase 10* — 19q13.41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.34× (z +10.7, q 5e-24, up in 4 of 13 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.478× (z -7.6, q 7e-12, down in 14 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLK11]] (+0.90, fdr 7e-06, ⚠ same locus), [[TFF2]] (+0.86, fdr 7e-06), [[HS3ST1]] (+0.78, fdr 7e-06), [[SERPINB5]] (+0.77, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 110 arrows point to it, the strongest [[LANCL3]] → it (grade B ⚠); 141 go from it, the strongest it → [[JUP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4972.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.34×** | +10.7 | 5e-24 | 4/13 (Panc 03.27, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.90×** | +9.6 | 3e-19 | 4/11 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.21×** | +5.3 | 2e-05 | 3/13 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.59× | +3.3 | 0.16 | 4/14 (SW1417, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Peretinoin (drug)]] 5 µM |  | 1.55× | +3.1 | 0.24 | 10/14 (AsPC-1, NCI-H1573, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4972.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.478×** | -7.6 | 7e-12 | 14/14 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.352×** | -7.6 | 7e-12 | 13/14 (KATO III, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.383×** | -7.0 | 5e-10 | 14/14 (KATO III, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.473×** | -5.5 | 6e-06 | 13/14 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.476×** | -5.4 | 7e-06 | 14/14 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.599×** | -5.1 | 4e-05 | 7/14 (SW48, Hs 766T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.497×** | -4.9 | 7e-05 | 13/14 (KATO III, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.533×** | -4.6 | 3e-04 | 13/14 (AsPC-1, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.656×** | -4.4 | 8e-04 | 11/14 (AsPC-1, SW48, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.531×** | -4.3 | 0.001 | 10/14 (SW48, LS 180, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.537×** | -4.2 | 0.002 | 10/14 (SW48, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.577×** | -4.0 | 0.003 | 12/14 (KATO III, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.601×** | -3.7 | 0.009 | 1/14 (HEC-1-A) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.623×** | -3.5 | 0.022 | 11/14 (SW1417, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.632×** | -3.3 | 0.031 | 13/14 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **0.653×** | -3.1 | 0.067 | 8/14 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.394×** | -3.0 | 0.081 | 11/14 (KATO III, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.665×** | -3.0 | 0.092 | 12/14 (KATO III, HT-29, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4972. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 278 | 0 | 17 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0717× (z -21.2) |
| [[KATO III (line)]] | alt | 191 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0355× (z -26.2) |
| [[LoVo (line)]] | wt | 40.5 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0694× (z -18.8) |
| [[LS 180 (line)]] | wt | 144 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0374× (z -25.0) |
| [[AsPC-1 (line)]] | alt | 475 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -13.8) |
| [[HT-29 (line)]] | alt | 105 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0399× (z -18.9) |
| [[CFPAC-1 (line)]] | alt | 73.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -16.6) |
| [[HCT15 (line)]] | alt | 31.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 84.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -14.9) |
| [[SW1417 (line)]] | alt | 80.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -12.7) |
| [[COLO 205 (line)]] | alt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0873× (z -11.8) |
| [[A-172 (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.20 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.13 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.15 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.30 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.67 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4972), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLK11]] | +0.90 | +0.88 / +0.87 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ESTROGEN_RESPONSE_LATE; STRING 825; ⚠ same locus (2.0 kb, same strand: neighbours can correlate without regulation) |
| [[TFF2]] | +0.86 | +0.82 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[HS3ST1]] | +0.78 | +0.83 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[SERPINB5]] | +0.77 | +0.80 / +0.69 | both halves | 7e-06 | STRING 501 |
| [[DSG3]] | +0.76 | +0.82 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[SLC6A20]] | +0.76 | +0.82 / +0.71 | both halves | 7e-06 |  |
| [[NPSR1]] | +0.75 | +0.79 / +0.66 | both halves | 7e-06 |  |
| [[FERMT1]] | +0.75 | +0.74 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[CEACAM6]] | +0.74 | +0.74 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS4]] | +0.72 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[GJB3]] | +0.72 | +0.76 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[CTSE]] | +0.72 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[KIAA0040]] | +0.72 | +0.77 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*110 arrows, 110 of them with an alert ⚠; grade A 0, B 10, C 100. Shown: the 12 strongest; 98 more arrows (98 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LANCL3]] | B | LANCL3 activity raises KLK10's level | lines that do not express LANCL3 (21) vs lines expressing it (29) | 2.60× lower at baseline in the lines without LANCL3 | 0.015 | ⚠ within organs, on part of the lines; also absent: PLAT, HTR1F, ENSG00000289153 |
| [[NOSTRIN]] | B | NOSTRIN activity raises KLK10's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 3.71× lower at baseline in the lines without NOSTRIN | 0.023 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[TJP2]] | B | TJP2 activity raises KLK10's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 3.30× lower at baseline in the lines without TJP2 | 0.036 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[PCDH11X]] | B | PCDH11X activity raises KLK10's level | lines that do not express PCDH11X (15) vs lines expressing it (35) | 3.55× lower at baseline in the lines without PCDH11X | 0.042 | ⚠ within organs, on part of the lines; also absent: XDH, CRYBG2, SPATA6L; maybe low, not absent |
| [[JUP]] | B | JUP activity raises KLK10's level | lines that do not express JUP (16) vs lines expressing it (34) | 3.94× lower at baseline in the lines without JUP | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[ZNF860]] | B | ZNF860 activity raises KLK10's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 3.28× lower at baseline in the lines without ZNF860 | 0.049 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[SEMA3B]] | B | SEMA3B activity raises KLK10's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 3.00× lower at baseline in the lines without SEMA3B | 0.050 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[GRHL3]] | B | GRHL3 activity raises KLK10's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 4.04× lower at baseline in the lines without GRHL3 | 0.060 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[ZBTB7C]] | B | ZBTB7C activity raises KLK10's level | lines that do not express ZBTB7C (25) vs lines expressing it (25) | 1.74× lower at baseline in the lines without ZBTB7C | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000290808, FSTL4, PPARGC1A |
| [[GPRC5A]] | B | GPRC5A activity raises KLK10's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 3.16× lower at baseline in the lines without GPRC5A | 0.097 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[KLK11]] | C | KLK11 activity raises KLK10's level | lines that do not express KLK11 (40) vs lines expressing it (10) | 22.09× lower at baseline in the lines without KLK11 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC17, LYZ; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises KLK10's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 10.99× lower at baseline in the lines without TMPRSS4 | 2e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |

### Downstream of this gene

*141 arrows, 141 of them with an alert ⚠; grade A 0, B 43, C 98. Shown: the 12 strongest; 129 more arrows (129 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JUP]] | B | KLK10 activity raises JUP's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 6.12× lower at baseline in the lines without KLK10 | 6e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[ARHGAP27]] | B | KLK10 activity raises ARHGAP27's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 3.24× lower at baseline in the lines without KLK10 | 7e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[EPS8L1]] | B | KLK10 activity raises EPS8L1's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 4.63× lower at baseline in the lines without KLK10 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[GJB2]] | B | KLK10 activity raises GJB2's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 3.83× lower at baseline in the lines without KLK10 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[EPHA2-AS1]] | B | KLK10 activity raises EPHA2-AS1's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 2.84× lower at baseline in the lines without KLK10 | 0.003 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[TJP2]] | B | KLK10 activity raises TJP2's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 3.58× lower at baseline in the lines without KLK10 | 0.003 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[SDC1]] | B | KLK10 activity raises SDC1's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 2.78× lower at baseline in the lines without KLK10 | 0.004 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[IL22RA1]] | B | KLK10 activity raises IL22RA1's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 3.21× lower at baseline in the lines without KLK10 | 0.004 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[RDH13]] | B | KLK10 activity raises RDH13's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 2.57× lower at baseline in the lines without KLK10 | 0.005 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[ABHD11]] | B | KLK10 activity raises ABHD11's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 3.02× lower at baseline in the lines without KLK10 | 0.005 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[UNC13D]] | B | KLK10 activity raises UNC13D's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 3.07× lower at baseline in the lines without KLK10 | 0.006 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[KRT8]] | B | KLK10 activity raises KRT8's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 4.17× lower at baseline in the lines without KLK10 | 0.006 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.838). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (14.0, 53.4); signed map (67.4, 9.4). **Vector** length 84.4, 39.9% of its response variance represented; |z| ≥ 3 in 533 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | -0.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.6 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -4.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.8 | -1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | kallikrein related peptidase 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.41 — chr19:51,012,739-51,020,175 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NES1; previously PRSSL1 |
| Gene groups (HGNC) | Kallikreins |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [O43240](https://www.uniprot.org/uniprotkb/O43240) (Kallikrein-10):

> Has a tumor-suppressor role for NES1 in breast and prostate cancer.

**Summary**, from NCBI Gene [5655](https://www.ncbi.nlm.nih.gov/gene/5655):

> Kallikreins are a subgroup of serine proteases having diverse physiological functions. Growing evidence suggests that many kallikreins are implicated in carcinogenesis and some have potential as novel cancer and other disease biomarkers. This gene is one of the fifteen kallikrein subfamily members located in a cluster on chromosome 19. Its encoded protein is secreted and may play a role in suppression of tumorigenesis in breast and prostate cancers. Alternate splicing of this gene results in …

**Accessions** — [HGNC:6358](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6358) · Entrez [5655](https://www.ncbi.nlm.nih.gov/gene/5655) · UniProt [O43240](https://www.uniprot.org/uniprotkb/O43240) · Ensembl [ENSG00000129451](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129451)

## Data

Gene col 4972: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4972); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4972, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4972]; `tensor/DDL_lfc|DDL_z.npy` [4972]; `embed/gene_vectors.npy` [4972]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4972 or target_col == 4972). Every well: [[KLK10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLK10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
