---
symbol: "AEBP1"
type: "gene"
col: 2786
ensembl_id: "ENSG00000106624"
name: "AE binding protein 1"
location: "7p13"
module: 87
arm: "+"
pooled_cpm: 4.3
n_lines_expressing: 11
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 51
direction_downstream: 59
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# AEBP1

*AE binding protein 1* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.49× (z +11.2, q 3e-26, up in 3 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.49× (z +8.0, q 2e-13, up in 0 of 6 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.517× (z -4.0, q 0.040, down in 6 of 7 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (C32 0.0421×, SK-MEL-2 0.0951×, RPMI-7951 0.253×, hTERT-HPNE 0.259×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (C32 0.0220×, hTERT-HPNE 0.173×); [[Verteporfin (drug)]] 5 µM in 2 lines (SK-MEL-2 0.102×, hTERT-HPNE 0.166×); [[Harringtonine (drug)]] 5 µM in 2 lines (C32 0.150×, RPMI-7951 0.195×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FCRLA]] (+0.79, fdr 7e-06), [[LOXL3]] (+0.77, fdr 7e-06), [[A2M]] (+0.72, fdr 7e-06); moves opposite to [[PATJ]] (-0.46, fdr 3e-04), [[PYDC2-AS1]] (-0.44, fdr 1e-04).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 51 arrows point to it, the strongest [[GYPC]] → it (grade C ⚠); 59 go from it, the strongest it → [[TMEM45A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2786.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.49×** | +11.2 | 3e-26 | 3/4 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.24×** | +10.3 | 2e-22 | 3/6 (RPMI-7951, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.49×** | +8.0 | 2e-13 | 0/6 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.36×** | +7.0 | 5e-10 | 3/5 (RPMI-7951, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.42×** | +5.2 | 2e-05 | 1/7 (NCI-H1792) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.94×** | +3.9 | 0.007 | 0/7 | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.88×** | +3.9 | 0.007 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.23×** | +3.8 | 0.010 | 1/4 (hTERT-HPNE) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +3.8 | 0.011 | 0/7 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +3.6 | 0.016 | 1/7 (SK-MEL-2) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +3.6 | 0.019 | 2/7 (CHP-212, SK-MEL-2) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.48×** | +3.5 | 0.025 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.88×** | +3.4 | 0.026 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.66×** | +3.1 | 0.066 | 0/7 | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.25×** | +3.1 | 0.072 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.25×** | +3.1 | 0.072 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2786.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (C32 0.0421×, SK-MEL-2 0.0951×, RPMI-7951 0.253×, hTERT-HPNE 0.259×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (C32 0.0220×, hTERT-HPNE 0.173×); [[Verteporfin (drug)]] 5 µM in 2 lines (SK-MEL-2 0.102×, hTERT-HPNE 0.166×); [[Harringtonine (drug)]] 5 µM in 2 lines (C32 0.150×, RPMI-7951 0.195×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.517×** | -4.0 | 0.040 | 6/7 (C32, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.574× | -3.5 | 0.11 | 3/7 (SK-MEL-2, C32, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.553× | -3.4 | 0.11 | 0/7 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2786. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 67.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0421× (z -24.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0220× (z -20.6) |
| [[hTERT-HPNE (line)]] | wt | 49.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -10.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 43.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0951× (z -16.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.102× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 91.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -11.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.195× (z -9.6) |
| [[CHP-212 (line)]] | wt | 31.1 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.05 µM 0.0635× (z -9.2) |
| [[A-172 (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.315 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.403 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.315 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.692 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.334 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.378 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.666 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.361 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.302 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.410 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.482 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.425 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.555 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.623 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.385 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2786), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCRLA]] | +0.79 | +0.84 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[LOXL3]] | +0.77 | +0.77 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[A2M]] | +0.72 | +0.69 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[COL1A2]] | +0.69 | +0.66 / +0.65 | both halves | 7e-06 | STRING 578 |
| [[COL19A1]] | +0.69 | +0.60 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[C10orf90]] | +0.66 | +0.72 / +0.57 | both halves | 8e-06 |  |
| [[SOX10]] | +0.66 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[CSPG4]] | +0.66 | +0.68 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[CTHRC1]] | +0.66 | +0.64 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[SDC2]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[MIR3681HG]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[MDGA2]] | +0.62 | +0.64 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PATJ]] | -0.46 | -0.50 / -0.27 | both halves | 3e-04 | same gene group |
| [[PYDC2-AS1]] | -0.44 | -0.52 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*51 arrows, 51 of them with an alert ⚠; grade A 0, B 0, C 51. Shown: the 12 strongest; 39 more arrows (39 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GYPC]] | C | GYPC activity raises AEBP1's level | lines that do not express GYPC (35) vs lines expressing it (15) | 4.02× lower at baseline in the lines without GYPC | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4; co-absent with the target |
| [[TDRD9]] | C | TDRD9 activity raises AEBP1's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 4.01× lower at baseline in the lines without TDRD9 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT; co-absent with the target |
| [[COL19A1]] | C | COL19A1 activity raises AEBP1's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 5.74× lower at baseline in the lines without COL19A1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[EDNRB]] | C | EDNRB activity raises AEBP1's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 4.65× lower at baseline in the lines without EDNRB | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[TYR]] | C | TYR activity raises AEBP1's level | lines that do not express TYR (43) vs lines expressing it (7) | 8.62× lower at baseline in the lines without TYR | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[TIMP3]] | C | TIMP3 activity raises AEBP1's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 4.44× lower at baseline in the lines without TIMP3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1; co-absent with the target |
| [[LOXL3]] | C | LOXL3 activity raises AEBP1's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 2.78× lower at baseline in the lines without LOXL3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent; co-absent with the target |
| [[A2M]] | C | A2M activity raises AEBP1's level | lines that do not express A2M (42) vs lines expressing it (8) | 6.53× lower at baseline in the lines without A2M | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |
| [[CARMN]] | C | CARMN activity raises AEBP1's level | lines that do not express CARMN (40) vs lines expressing it (10) | 4.57× lower at baseline in the lines without CARMN | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN; co-absent with the target |
| [[SPARC]] | C | SPARC activity raises AEBP1's level | lines that do not express SPARC (34) vs lines expressing it (16) | 4.59× lower at baseline in the lines without SPARC | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032; co-absent with the target |
| [[RNF175]] | C | RNF175 activity raises AEBP1's level | lines that do not express RNF175 (30) vs lines expressing it (20) | 3.73× lower at baseline in the lines without RNF175 | 0.008 | ⚠ within organs, on part of the lines; also absent: SCG2, ENSG00000266450, MIR493HG; co-absent with the target |
| [[LINC01242]] | C | LINC01242 activity raises AEBP1's level | lines that do not express LINC01242 (42) vs lines expressing it (8) | 3.49× lower at baseline in the lines without LINC01242 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, LINC00879, ENSG00000234426; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*59 arrows, 59 of them with an alert ⚠; grade A 0, B 8, C 51. Shown: the 12 strongest; 47 more arrows (47 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM45A]] | B | AEBP1 activity raises TMEM45A's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 4.89× lower at baseline in the lines without AEBP1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1 |
| [[DIRC3]] | B | AEBP1 activity raises DIRC3's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 5.14× lower at baseline in the lines without AEBP1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1 |
| [[TRIB2]] | B | AEBP1 activity raises TRIB2's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 5.59× lower at baseline in the lines without AEBP1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1 |
| [[ZCCHC24]] | B | AEBP1 activity raises ZCCHC24's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 2.87× lower at baseline in the lines without AEBP1 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1 |
| [[MMP14]] | B | AEBP1 activity raises MMP14's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 4.27× lower at baseline in the lines without AEBP1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1 |
| [[ARL10]] | B | AEBP1 activity raises ARL10's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 2.90× lower at baseline in the lines without AEBP1 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1 |
| [[BOC]] | B | AEBP1 activity raises BOC's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 3.54× lower at baseline in the lines without AEBP1 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1 |
| [[FZD1]] | B | AEBP1 activity raises FZD1's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 1.81× lower at baseline in the lines without AEBP1 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1 |
| [[MIR3681HG]] | C | AEBP1 activity raises MIR3681HG's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 12.64× lower at baseline in the lines without AEBP1 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[PRRX1]] | C | AEBP1 activity raises PRRX1's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 12.49× lower at baseline in the lines without AEBP1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[LOXL3]] | C | AEBP1 activity raises LOXL3's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 6.45× lower at baseline in the lines without AEBP1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[SRPX]] | C | AEBP1 activity raises SRPX's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 5.66× lower at baseline in the lines without AEBP1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.719). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.5, 27.6); signed map (28.3, 40.4). **Vector** length 27.6, 10.5% of its response variance represented; |z| ≥ 3 in 146 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.5 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.6 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.5 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.5 | -0.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -0.8 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.6 | -1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | -0.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -0.5 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.5 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.5 | -2.6 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.4 | -2.5 |
|  | [[Encorafenib (drug)]] 5 µM |  | -0.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | AE binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p13 — chr7:44,104,345-44,114,562 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ACLP |
| Gene groups (HGNC) | M14 carboxypeptidases; MicroRNA protein coding host genes |
| Hallmark sets | MYOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUX7](https://www.uniprot.org/uniprotkb/Q8IUX7) (Adipocyte enhancer-binding protein 1):

> [Isoform 1]: As a positive regulator of collagen fibrillogenesis, it is probably involved in the organization and remodeling of the extracellular matrix.; [Isoform 2]: May positively regulate MAP-kinase activity in adipocytes, leading to enhanced adipocyte proliferation and reduced adipocyte differentiation. May also positively regulate NF-kappa-B activity in macrophages by promoting the phosphorylation and subsequent degradation of I-kappa-B-alpha (NFKBIA), leading to enhanced macrophage …

**Summary**, from NCBI Gene [165](https://www.ncbi.nlm.nih.gov/gene/165):

> This gene encodes a member of carboxypeptidase A protein family. The encoded protein may function as a transcriptional repressor and play a role in adipogenesis and smooth muscle cell differentiation. Studies in mice suggest that this gene functions in wound healing and abdominal wall development. Overexpression of this gene is associated with glioblastoma. [provided by RefSeq, May 2013]

**Accessions** — [HGNC:303](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:303) · Entrez [165](https://www.ncbi.nlm.nih.gov/gene/165) · UniProt [Q8IUX7](https://www.uniprot.org/uniprotkb/Q8IUX7) · Ensembl [ENSG00000106624](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106624)

## Data

Gene col 2786: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2786); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2786, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2786]; `tensor/DDL_lfc|DDL_z.npy` [2786]; `embed/gene_vectors.npy` [2786]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2786 or target_col == 2786). Every well: [[AEBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AEBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
