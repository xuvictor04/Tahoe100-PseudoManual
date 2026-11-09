---
symbol: "GYPC"
type: "gene"
col: 5897
ensembl_id: "ENSG00000136732"
name: "glycophorin C (Gerbich blood group)"
location: "2q14.3"
module: 13
arm: "+"
pooled_cpm: 5.04
n_lines_expressing: 15
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 17
direction_downstream: 35
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# GYPC

*glycophorin C (Gerbich blood group)* — 2q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.70× (z +11.5, q 1e-27, up in 5 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Verteporfin (drug)]] 5 µM: 1.75× (z +3.5, q 0.045, up in 2 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.379× (z -6.4, q 8e-08, down in 12 of 12 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 8 lines (C32 0.136×, RPMI-7951 0.111×, SK-MEL-2 0.117×, H4 0.128×, …); [[Panobinostat (drug)]] 5 µM in 5 lines (HOP62 0.0185×, H4 0.0495×, HS-578T 0.0762×, C32 0.125×, …; ⚠ cell-cycle shift, explains ~30% of this change); [[Belinostat (drug)]] 5 µM in 5 lines (H4 0.0682×, hTERT-HPNE 0.0864×, RPMI-7951 0.162×, HOP62 0.176×, …); [[Panobinostat (drug)]] 0.05 µM in 1 line (H4 0.132×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC43A3]] (+0.58, fdr 1e-05), [[CTHRC1]] (+0.56, fdr 2e-05), [[WNT5A]] (+0.56, fdr 1e-05); moves opposite to [[CPA4]] (-0.55, fdr 1e-05), [[PRDX1]] (-0.52, fdr 2e-05), [[GUCY1B1]] (-0.44, fdr 3e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[TBX3]] → it (grade B ⚠); 35 go from it, the strongest it → [[TBX3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5897.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.70×** | +11.5 | 1e-27 | 5/10 (J82, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.15×** | +10.4 | 9e-23 | 1/9 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.06×** | +6.8 | 2e-09 | 3/9 (J82, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.87×** | +4.1 | 0.006 | 5/9 (A-172, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Verteporfin (drug)]] 5 µM |  | **1.75×** | +3.5 | 0.045 | 2/12 (J82, HOP62) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +3.5 | 0.045 | 3/10 (A-172, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.045 | 3/13 (RPMI-7951, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.25×** | +3.4 | 0.050 | 3/10 (RPMI-7951, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.64×** | +3.3 | 0.054 | 1/9 (HOP62) | top dose only | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.3 | 0.058 | 1/10 (RPMI-7951) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.61×** | +3.1 | 0.089 | 2/13 (C32, SK-MEL-2) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.1 | 0.089 | 2/10 (C32, SK-MEL-2) | top dose only | cell-cycle shift (explains ~9% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.09×** | +3.1 | 0.089 | 0/9 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +3.1 | 0.089 | 1/10 (A-172) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.0 | 0.097 | 5/12 (A-172, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5897.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 8 lines (C32 0.136×, RPMI-7951 0.111×, SK-MEL-2 0.117×, H4 0.128×, …); [[Panobinostat (drug)]] 5 µM in 5 lines (HOP62 0.0185×, H4 0.0495×, HS-578T 0.0762×, C32 0.125×, …; ⚠ cell-cycle shift, explains ~30% of this change); [[Belinostat (drug)]] 5 µM in 5 lines (H4 0.0682×, hTERT-HPNE 0.0864×, RPMI-7951 0.162×, HOP62 0.176×, …); [[Panobinostat (drug)]] 0.05 µM in 1 line (H4 0.132×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.379×** | -6.4 | 8e-08 | 12/12 (H4, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.595× | -3.4 | 0.16 | 11/13 (C32, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~16% here); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | 0.632× | -3.2 | 0.23 | 7/13 (HOP62, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | 0.412× | -3.1 | 0.23 | 10/13 (C32, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.632× | -3.1 | 0.23 | 6/13 (H4, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5897. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 42.5 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -13.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.136× (z -13.2) |
| [[H4 (line)]] | wt | 64.5 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0495× (z -17.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0682× (z -15.4) |
| [[HOP62 (line)]] | alt | 12.0 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0185× (z -19.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.111× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 44.8 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0831× (z -12.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0864× (z -12.7) |
| [[RPMI-7951 (line)]] | alt | 53.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.111× (z -12.5) |
| [[SK-MEL-2 (line)]] | alt | 34.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -12.4) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.117× (z -12.0) |
| [[HS-578T (line)]] | alt | 23.3 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0762× (z -13.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.117× (z -11.5) |
| [[A-172 (line)]] | wt | 15.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.166× (z -8.6) |
| [[J82 (line)]] | alt | 6.24 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +9.1) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[A-427 (line)]] | wt | 0.320 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.394 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.389 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.653 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.460 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.425 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.355 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.375 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.640 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.391 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.913 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.340 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.436 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.709 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.427 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.511 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.556 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.371 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5897), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC43A3]] | +0.58 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[CTHRC1]] | +0.56 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[WNT5A]] | +0.56 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[PDGFRA]] | +0.52 | +0.50 / +0.53 | both halves | 1e-05 | same gene group; STRING 534 |
| [[CYGB]] | +0.49 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[MAGI2]] | +0.48 | +0.46 / +0.35 | both halves | 1e-04 |  |
| [[C10orf90]] | +0.48 | +0.60 / +0.29 | both halves | 2e-04 |  |
| [[TWIST1]] | +0.47 | +0.49 / +0.34 | both halves | 1e-04 |  |
| [[MAGI2-AS3]] | +0.46 | +0.49 / +0.28 | both halves | 3e-04 |  |
| [[MME]] | +0.45 | +0.51 / +0.31 | both halves | 2e-04 | same gene group |
| [[MCCC1]] | +0.45 | +0.29 / +0.47 | both halves | 2e-04 |  |
| [[PRRX1]] | +0.45 | +0.45 / +0.31 | both halves | 2e-04 | pathway: HALLMARK_KRAS_SIGNALING_UP |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPA4]] | -0.55 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[PRDX1]] | -0.52 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[GUCY1B1]] | -0.44 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[KRT14]] | -0.44 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[ARPC5]] | -0.43 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[HSP90AA1]] | -0.40 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[CNN3]] | -0.40 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[FLNC]] | -0.40 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[DSG2]] | -0.40 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[FAM20B]] | -0.39 | -0.24 / -0.43 | both halves | 4e-04 |  |
| [[PSME4]] | -0.39 | -0.29 / -0.36 | both halves | 2e-04 |  |
| [[MAP1A]] | -0.38 | -0.31 / -0.34 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 1, C 16. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBX3]] | B | TBX3 activity raises GYPC's level | lines that do not express TBX3 (10) vs lines expressing it (40) | 2.45× lower at baseline in the lines without TBX3 | 0.074 | ⚠ within organs, on part of the lines |
| [[CPA4]] | C | CPA4 activity raises GYPC's level | lines that do not express CPA4 (26) vs lines expressing it (24) | 4.63× lower at baseline in the lines without CPA4 | 0.002 | ⚠ within organs, on part of the lines; also absent: GYPC, FLI1, IL6; co-absent with the target |
| [[C10orf90]] | C | C10orf90 activity raises GYPC's level | lines that do not express C10orf90 (35) vs lines expressing it (15) | 5.94× lower at baseline in the lines without C10orf90 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GRIN2A, LINC01242, ADGRG7; maybe low, not absent; co-absent with the target |
| [[DAAM2]] | C | DAAM2 activity raises GYPC's level | lines that do not express DAAM2 (27) vs lines expressing it (23) | 4.30× lower at baseline in the lines without DAAM2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, ZNF471, SDC2; maybe low, not absent; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises GYPC's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 6.02× lower at baseline in the lines without AEBP1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[TWIST1]] | C | TWIST1 activity raises GYPC's level | lines that do not express TWIST1 (26) vs lines expressing it (24) | 3.84× lower at baseline in the lines without TWIST1 | 0.013 | ⚠ within organs, on part of the lines; also absent: PCDH10, MDGA2, FAP; co-absent with the target |
| [[FOXC2]] | C | FOXC2 activity raises GYPC's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 3.16× lower at baseline in the lines without FOXC2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT; co-absent with the target |
| [[HS3ST3A1]] | C | HS3ST3A1 activity raises GYPC's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 5.32× lower at baseline in the lines without HS3ST3A1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1; co-absent with the target |
| [[COL6A3]] | C | COL6A3 activity raises GYPC's level | lines that do not express COL6A3 (39) vs lines expressing it (11) | 5.28× lower at baseline in the lines without COL6A3 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000222032, LINC01242, ENSG00000287474; co-absent with the target |
| [[MME]] | C | MME activity raises GYPC's level | lines that do not express MME (30) vs lines expressing it (20) | 4.79× lower at baseline in the lines without MME | 0.044 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC; co-absent with the target |
| [[CNRIP1]] | C | CNRIP1 activity raises GYPC's level | lines that do not express CNRIP1 (25) vs lines expressing it (25) | 4.44× lower at baseline in the lines without CNRIP1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047; co-absent with the target |
| [[PDGFRA]] | C | PDGFRA activity raises GYPC's level | lines that do not express PDGFRA (29) vs lines expressing it (21) | 4.02× lower at baseline in the lines without PDGFRA | 0.058 | ⚠ within organs, on part of the lines; also absent: LRCH2, MAGI2-AS3, THY1; co-absent with the target |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 14, C 21. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBX3]] | B | GYPC activity raises TBX3's level | lines that do not express GYPC (35) vs lines expressing it (15) | 3.07× lower at baseline in the lines without GYPC | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |
| [[KLF9]] | B | GYPC activity raises KLF9's level | lines that do not express GYPC (35) vs lines expressing it (15) | 2.77× lower at baseline in the lines without GYPC | 0.014 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |
| [[CLEC2D]] | B | GYPC activity raises CLEC2D's level | lines that do not express GYPC (35) vs lines expressing it (15) | 2.33× lower at baseline in the lines without GYPC | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |
| [[PRDX1]] | B | GYPC activity lowers PRDX1's level | lines that do not express GYPC (35) vs lines expressing it (15) | 1.44× higher at baseline in the lines without GYPC | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |
| [[TSPAN4]] | B | GYPC activity raises TSPAN4's level | lines that do not express GYPC (35) vs lines expressing it (15) | 2.38× lower at baseline in the lines without GYPC | 0.051 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |
| [[SMIM3]] | B | GYPC activity raises SMIM3's level | lines that do not express GYPC (35) vs lines expressing it (15) | 2.32× lower at baseline in the lines without GYPC | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |
| [[UAP1L1]] | B | GYPC activity raises UAP1L1's level | lines that do not express GYPC (35) vs lines expressing it (15) | 1.82× lower at baseline in the lines without GYPC | 0.059 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |
| [[RILPL2]] | B | GYPC activity raises RILPL2's level | lines that do not express GYPC (35) vs lines expressing it (15) | 1.24× lower at baseline in the lines without GYPC | 0.062 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |
| [[PTGES3]] | B | GYPC activity lowers PTGES3's level | lines that do not express GYPC (35) vs lines expressing it (15) | 1.32× higher at baseline in the lines without GYPC | 0.066 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |
| [[CYGB]] | B | GYPC activity raises CYGB's level | lines that do not express GYPC (35) vs lines expressing it (15) | 2.20× lower at baseline in the lines without GYPC | 0.067 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |
| [[SH3RF3]] | B | GYPC activity raises SH3RF3's level | lines that do not express GYPC (35) vs lines expressing it (15) | 2.97× lower at baseline in the lines without GYPC | 0.072 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |
| [[PSME4]] | B | GYPC activity lowers PSME4's level | lines that do not express GYPC (35) vs lines expressing it (15) | 1.21× higher at baseline in the lines without GYPC | 0.087 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.219). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.3, 20.0); signed map (26.7, 41.1). **Vector** length 46.4, 15.5% of its response variance represented; |z| ≥ 3 in 351 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.7 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +1.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.3 | +2.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +2.4 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -2.9 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.2 | -3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | +0.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | glycophorin C (Gerbich blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.3 — chr2:126,656,133-126,696,667 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GPC, GYPD, Ge, CD236, CD236R, GPD |
| Gene groups (HGNC) | Blood group antigens; CD molecules |
| Hallmark sets | KRAS_SIGNALING_UP, HEME_METABOLISM |
| Reactome | 2 pathways, smallest: Cell surface interactions at the vascular wall; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [P04921](https://www.uniprot.org/uniprotkb/P04921) (Glycophorin-C):

> This protein is a minor sialoglycoprotein in human erythrocyte membranes. The blood group Gerbich antigens and receptors for Plasmodium falciparum merozoites are most likely located within the extracellular domain. Glycophorin-C plays an important role in regulating the stability of red cells.

**Summary**, from NCBI Gene [2995](https://www.ncbi.nlm.nih.gov/gene/2995):

> Glycophorin C (GYPC) is an integral membrane glycoprotein. It is a minor species carried by human erythrocytes, but plays an important role in regulating the mechanical stability of red cells. A number of glycophorin C mutations have been described. The Gerbich and Yus phenotypes are due to deletion of exon 3 and 2, respectively. The Webb and Duch antigens, also known as glycophorin D, result from single point mutations of the glycophorin C gene. The glycophorin C protein has very little …

**Accessions** — [HGNC:4704](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4704) · Entrez [2995](https://www.ncbi.nlm.nih.gov/gene/2995) · UniProt [P04921](https://www.uniprot.org/uniprotkb/P04921) · Ensembl [ENSG00000136732](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136732)

## Data

Gene col 5897: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5897); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5897, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5897]; `tensor/DDL_lfc|DDL_z.npy` [5897]; `embed/gene_vectors.npy` [5897]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5897 or target_col == 5897). Every well: [[GYPC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GYPC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
