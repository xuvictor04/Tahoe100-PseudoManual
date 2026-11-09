---
symbol: "A4GALT"
type: "gene"
col: 4870
ensembl_id: "ENSG00000128274"
name: "alpha 1,4-galactosyltransferase (P1PK blood group)"
location: "22q13.2"
module: 113
arm: "+"
pooled_cpm: 5.66
n_lines_expressing: 36
n_dd_up: 10
n_dd_down: 20
n_dd_up_clean: 10
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 9
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# A4GALT

*alpha 1,4-galactosyltransferase (P1PK blood group)* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.66× (z +7.0, q 2e-09, up in 17 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.485× (z -10.0, q 9e-21, down in 23 of 28 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP2B4]] (+0.61, fdr 3e-05), [[DUSP1]] (+0.58, fdr 1e-04), [[RHOB]] (+0.56, fdr 3e-05); moves opposite to [[GARS1-DT]] (-0.47, fdr 1e-04), [[METTL21A]] (-0.46, fdr 1e-04), [[LAMTOR5-AS1]] (-0.43, fdr 3e-04).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TLR2]] → it (grade B ⚠); 9 go from it, the strongest it → [[B4GALT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4870.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +7.0 | 2e-09 | 17/32 (A498, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +4.7 | 9e-04 | 10/30 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.54×** | +4.2 | 0.004 | 11/29 (A498, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.1 | 0.007 | 6/34 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +4.0 | 0.008 | 10/31 (A498, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.020 | 8/30 (Hs 766T, LoVo, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.69×** | +3.6 | 0.022 | 6/28 (NCI-H460, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.43×** | +3.5 | 0.032 | 5/31 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.043 | 8/31 (NCI-H460, Hs 766T, …) | two highest doses | low cells (technical?) |
| [[Econazole (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.053 | 6/32 (Hs 766T, A498, …) | top dose only | position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.097 | 1/32 (NCI-H460) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4870.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.485×** | -10.0 | 9e-21 | 23/28 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.495×** | -6.9 | 2e-09 | 16/32 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.525×** | -6.3 | 6e-08 | 15/31 (A498, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.328×** | -5.7 | 2e-06 | 20/28 (NCI-H1792, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.437×** | -4.2 | 0.002 | 11/27 (SK-MEL-2, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.650×** | -4.2 | 0.002 | 12/31 (HOP62, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.647×** | -4.1 | 0.003 | 16/26 (SK-MEL-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.745×** | -4.1 | 0.003 | 14/27 (SK-MEL-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.665×** | -3.8 | 0.008 | 15/28 (A-172, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.684×** | -3.7 | 0.012 | 12/31 (hTERT-HPNE, A498, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.674×** | -3.6 | 0.014 | 14/31 (A498, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.681×** | -3.6 | 0.014 | 14/23 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.495×** | -3.6 | 0.014 | 8/26 (Hs 766T, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.695×** | -3.4 | 0.025 | 13/30 (SK-MEL-2, LoVo, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.624×** | -3.3 | 0.038 | 6/32 (HCT15, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.719×** | -3.2 | 0.044 | 14/31 (A498, HepG2/C3A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.720×** | -3.2 | 0.044 | 9/33 (LoVo, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4870. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 28.7 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0974× (z -17.6) |
| [[A498 (line)]] | wt | 21.9 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 4.12× (z +10.2) | [[Bortezomib (drug)]] 0.05 µM 0.193× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 17.8 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 13.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -9.0) |
| [[HOP62 (line)]] | alt | 4.27 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0845× (z -9.0) |
| [[HS-578T (line)]] | alt | 8.55 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 5.86 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0523× (z -15.0) |
| [[A-172 (line)]] | wt | 5.66 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.105× (z -8.7) |
| [[Hs 766T (line)]] | wt | 10.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -11.1) |
| [[HT-29 (line)]] | alt | 4.81 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0625× (z -8.7) |
| [[LoVo (line)]] | wt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -9.3) |
| [[SW 900 (line)]] | alt | 6.38 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -10.6) |
| [[A-427 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.310 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.339 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.295 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.421 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.329 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.358 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.390 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.33 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4870), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP2B4]] | +0.61 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[DUSP1]] | +0.58 | +0.34 / +0.66 | both halves | 1e-04 |  |
| [[RHOB]] | +0.56 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[ARRDC2]] | +0.55 | +0.26 / +0.65 | both halves | 4e-04 |  |
| [[ARL4D]] | +0.55 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[AKAP13]] | +0.54 | +0.36 / +0.53 | both halves | 1e-04 |  |
| [[KIF13B]] | +0.53 | +0.34 / +0.52 | both halves | 1e-04 |  |
| [[CEBPB]] | +0.53 | +0.35 / +0.65 | both halves | 1e-04 |  |
| [[TNIP2]] | +0.53 | +0.31 / +0.57 | both halves | 2e-04 |  |
| [[MT1E]] | +0.53 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[ID1]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[MAP1S]] | +0.52 | +0.39 / +0.51 | both halves | 5e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GARS1-DT]] | -0.47 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[METTL21A]] | -0.46 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[LAMTOR5-AS1]] | -0.43 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[DEPDC4]] | -0.42 | -0.31 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLR2]] | B | TLR2 activity raises A4GALT's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 2.02× lower at baseline in the lines without TLR2 | 0.011 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B4GALT1]] | B | A4GALT activity raises B4GALT1's level | lines that do not express A4GALT (14) vs lines expressing it (36) | 1.65× lower at baseline in the lines without A4GALT | 0.019 | ⚠ within organs, on part of the lines; also absent: HTR1D, PAPSS2, NT5E |
| [[PLCD3]] | B | A4GALT activity raises PLCD3's level | lines that do not express A4GALT (14) vs lines expressing it (36) | 1.22× lower at baseline in the lines without A4GALT | 0.022 | ⚠ within organs, on part of the lines; also absent: HTR1D, PAPSS2, NT5E |
| [[UBE2E2]] | B | A4GALT activity raises UBE2E2's level | lines that do not express A4GALT (14) vs lines expressing it (36) | 2.95× lower at baseline in the lines without A4GALT | 0.039 | ⚠ within organs, on part of the lines; also absent: HTR1D, PAPSS2, NT5E |
| [[PLIN3]] | B | A4GALT activity raises PLIN3's level | lines that do not express A4GALT (14) vs lines expressing it (36) | 1.58× lower at baseline in the lines without A4GALT | 0.049 | ⚠ within organs, on part of the lines; also absent: HTR1D, PAPSS2, NT5E |
| [[ZFAND5]] | B | A4GALT activity raises ZFAND5's level | lines that do not express A4GALT (14) vs lines expressing it (36) | 1.09× lower at baseline in the lines without A4GALT | 0.058 | ⚠ within organs, on part of the lines; also absent: HTR1D, PAPSS2, NT5E |
| [[TLR2]] | B | A4GALT activity raises TLR2's level | lines that do not express A4GALT (14) vs lines expressing it (36) | 2.36× lower at baseline in the lines without A4GALT | 0.061 | ⚠ within organs, on part of the lines; also absent: HTR1D, PAPSS2, NT5E |
| [[LRRC8E]] | B | A4GALT activity raises LRRC8E's level | lines that do not express A4GALT (14) vs lines expressing it (36) | 1.59× lower at baseline in the lines without A4GALT | 0.090 | ⚠ within organs, on part of the lines; also absent: HTR1D, PAPSS2, NT5E |
| [[AHNAK2]] | B | A4GALT activity raises AHNAK2's level | lines that do not express A4GALT (14) vs lines expressing it (36) | 2.15× lower at baseline in the lines without A4GALT | 0.092 | ⚠ within organs, on part of the lines; also absent: HTR1D, PAPSS2, NT5E |
| cells under [[SBI-0640756 (drug)]] 5 µM | B | A4GALT activity lowers the cells' numbers under SBI-0640756 5 µM (makes them more sensitive) | lines that do not express A4GALT (14) vs lines expressing it (34) | the lines without A4GALT: 1.20× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: HTR1D, PAPSS2, NT5E |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.3, 12.1); signed map (12.8, 30.8). **Vector** length 72.1, 16.0% of its response variance represented; |z| ≥ 3 in 758 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.9 | +4.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +4.2 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.9 | +2.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.8 | +2.7 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.4 | -1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.0 | -4.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.7 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | alpha 1,4-galactosyltransferase (P1PK blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:42,692,121-42,721,298 (-) |
| Ensembl biotype | protein_coding |
| Also known as | A14GALT, Gb3S, P(k); previously P1 |
| Gene groups (HGNC) | Alpha 1,4-glycosyltransferases; Blood group antigens |
| Reactome | 4 pathways, smallest: Glycosphingolipid biosynthesis; Glycosphingolipid metabolism; Sphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPC4](https://www.uniprot.org/uniprotkb/Q9NPC4) (Lactosylceramide 4-alpha-galactosyltransferase):

> Glycosyltransferase involved in biosynthesis of P1, P(k) and the rare NOR antigens of P1PK histo-blood group system. Catalyzes the transfer of galactose from UDP-alpha-D-galactose in an alpha1,4 linkage to lactosylceramide/beta-D-galactosyl-(1->4)-beta-D-glucosyl-(1<->1)-ceramide(d18:1(4E)) to produce globotriaosylceramide/globoside Gb3Cer (d18:1(4E)), also known as P(k) antigen or CD77. Globoside Gb3Cer/P(k)/CD77 is a root structure in biosynthesis pathway of neutral glycosphingolipids of the …

**Summary**, from NCBI Gene [53947](https://www.ncbi.nlm.nih.gov/gene/53947):

> The protein encoded by this gene catalyzes the transfer of galactose to lactosylceramide to form globotriaosylceramide, which has been identified as the P(k) antigen of the P blood group system. This protein, a type II membrane protein found in the Golgi, is also required for the synthesis of the bacterial verotoxins receptor. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:18149](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18149) · Entrez [53947](https://www.ncbi.nlm.nih.gov/gene/53947) · UniProt [Q9NPC4](https://www.uniprot.org/uniprotkb/Q9NPC4) · Ensembl [ENSG00000128274](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128274)

## Data

Gene col 4870: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4870); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4870, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4870]; `tensor/DDL_lfc|DDL_z.npy` [4870]; `embed/gene_vectors.npy` [4870]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4870 or target_col == 4870). Every well: [[A4GALT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/A4GALT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
