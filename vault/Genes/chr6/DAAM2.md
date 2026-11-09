---
symbol: "DAAM2"
type: "gene"
col: 7067
ensembl_id: "ENSG00000146122"
name: "dishevelled associated activator of morphogenesis 2"
location: "6p21.2"
module: 104
arm: "+"
pooled_cpm: 2.6
n_lines_expressing: 23
n_dd_up: 32
n_dd_down: 1
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 31
direction_downstream: 12
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# DAAM2

*dishevelled associated activator of morphogenesis 2* — 6p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.30× (z +12.2, q 2e-31, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.94× (z +7.1, q 1e-10, up in 1 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.537× (z -4.7, q 0.001, down in 9 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.184×, C32 0.337×; ⚠ cell-cycle shift, explains ~39% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.316×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF175]] (+0.71, fdr 7e-06), [[SRPX]] (+0.68, fdr 1e-05), [[ITGA8]] (+0.63, fdr 1e-05); moves opposite to [[SLAMF7]] (-0.56, fdr 1e-05), [[ANKRD30B]] (-0.51, fdr 6e-05), [[ROR1-AS1]] (-0.47, fdr 4e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 31 arrows point to it, the strongest [[LEF1]] → it (grade B ⚠); 12 go from it, the strongest it → [[CACNA1C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7067.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.30×** | +12.2 | 2e-31 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.67×** | +9.9 | 1e-20 | 2/6 (RPMI-7951, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.25×** | +7.7 | 2e-12 | 1/3 (SK-MEL-2) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +7.1 | 1e-10 | 1/11 (SNU-423) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.90×** | +6.9 | 5e-10 | 10/17 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +4.9 | 1e-04 | 1/6 (C32) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.89×** | +4.9 | 1e-04 | 9/12 (RPMI-7951, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.37×** | +4.7 | 2e-04 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.84×** | +4.7 | 2e-04 | 7/13 (RPMI-7951, SK-MEL-2, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +4.6 | 3e-04 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.92×** | +4.3 | 0.001 | 0/2 | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +4.1 | 0.002 | 6/14 (NCI-H2347, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.0 | 0.002 | 0/9 | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.67×** | +3.9 | 0.004 | 6/11 (RPMI-7951, SK-MEL-2, …) | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.04×** | +3.9 | 0.004 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.63×** | +3.7 | 0.007 | 7/14 (SK-MEL-2, RPMI-7951, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.008 | 1/17 (NCI-H23) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.009 | 6/16 (SK-MEL-2, RPMI-7951, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +3.5 | 0.012 | 2/9 (NCI-H2347, H4) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.59×** | +3.5 | 0.012 | 7/12 (RPMI-7951, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.58×** | +3.5 | 0.013 | 6/14 (SK-MEL-2, RPMI-7951, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +3.4 | 0.015 | 7/15 (RPMI-7951, SK-MEL-2, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.54×** | +3.2 | 0.035 | 2/13 (C32, NCI-H2347) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7067.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.184×, C32 0.337×; ⚠ cell-cycle shift, explains ~39% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.316×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.537×** | -4.7 | 0.001 | 9/14 (C32, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7067. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 78.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 8.04 | 1 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 19.8× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -10.3) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A-172 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.412 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.390 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.543 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.659 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.814 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.535 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.422 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.438 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.597 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.369 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.790 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.760 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.416 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.576 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.433 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.662 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.749 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.522 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.403 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7067), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF175]] | +0.71 | +0.67 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[SRPX]] | +0.68 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[ITGA8]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[GHR]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[DCN]] | +0.60 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[SH3RF3]] | +0.60 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[FN1]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ELMO1]] | +0.59 | +0.41 / +0.63 | both halves | 4e-05 | **novel candidate** |
| [[RIPOR2]] | +0.59 | +0.46 / +0.67 | both halves | 3e-05 | same gene group |
| [[ITGA10]] | +0.58 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[PDGFRA]] | +0.57 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[HSD11B1]] | +0.56 | +0.37 / +0.69 | both halves | 9e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLAMF7]] | -0.56 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[ANKRD30B]] | -0.51 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[ROR1-AS1]] | -0.47 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ANXA10]] | -0.44 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[FGF5]] | -0.44 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[SIRLNT]] | -0.43 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[LRIG1]] | -0.42 | -0.30 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 3, C 28. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LEF1]] | B | LEF1 activity raises DAAM2's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 2.14× lower at baseline in the lines without LEF1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1 |
| [[ANGPT1]] | B | ANGPT1 activity raises DAAM2's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 2.01× lower at baseline in the lines without ANGPT1 | 0.051 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5 |
| [[CTTNBP2]] | B | CTTNBP2 activity raises DAAM2's level | lines that do not express CTTNBP2 (31) vs lines expressing it (19) | 1.83× lower at baseline in the lines without CTTNBP2 | 0.054 | ⚠ within organs, on part of the lines; also absent: DCT, ENSG00000266976, TYR |
| [[ANKRD30B]] | C | ANKRD30B activity raises DAAM2's level | lines that do not express ANKRD30B (35) vs lines expressing it (15) | 3.17× lower at baseline in the lines without ANKRD30B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMPH, GYPC, GDNF; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises DAAM2's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 3.96× lower at baseline in the lines without AEBP1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[LEF1-AS1]] | C | LEF1-AS1 activity raises DAAM2's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 2.55× lower at baseline in the lines without LEF1-AS1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent; co-absent with the target |
| [[C10orf90]] | C | C10orf90 activity raises DAAM2's level | lines that do not express C10orf90 (35) vs lines expressing it (15) | 3.23× lower at baseline in the lines without C10orf90 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GRIN2A, LINC01242, ADGRG7; maybe low, not absent; co-absent with the target |
| [[GYPC]] | C | GYPC activity raises DAAM2's level | lines that do not express GYPC (35) vs lines expressing it (15) | 3.14× lower at baseline in the lines without GYPC | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4; co-absent with the target |
| [[EDNRB]] | C | EDNRB activity raises DAAM2's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 2.60× lower at baseline in the lines without EDNRB | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[LINC01242]] | C | LINC01242 activity raises DAAM2's level | lines that do not express LINC01242 (42) vs lines expressing it (8) | 3.15× lower at baseline in the lines without LINC01242 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, LINC00879, ENSG00000234426; maybe low, not absent; co-absent with the target |
| [[TDRD9]] | C | TDRD9 activity raises DAAM2's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 2.80× lower at baseline in the lines without TDRD9 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT; co-absent with the target |
| [[TYR]] | C | TYR activity raises DAAM2's level | lines that do not express TYR (43) vs lines expressing it (7) | 5.22× lower at baseline in the lines without TYR | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 1, C 11.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA1C]] | B | DAAM2 activity raises CACNA1C's level | lines that do not express DAAM2 (27) vs lines expressing it (23) | 3.00× lower at baseline in the lines without DAAM2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, ZNF471, SDC2; maybe low, not absent |
| [[GYPC]] | C | DAAM2 activity raises GYPC's level | lines that do not express DAAM2 (27) vs lines expressing it (23) | 4.30× lower at baseline in the lines without DAAM2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, ZNF471, SDC2; maybe low, not absent; co-absent with the target |
| [[FN1]] | C | DAAM2 activity raises FN1's level | lines that do not express DAAM2 (27) vs lines expressing it (23) | 7.43× lower at baseline in the lines without DAAM2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, ZNF471, SDC2; maybe low, not absent; co-absent with the target |
| [[ENPP2]] | C | DAAM2 activity raises ENPP2's level | lines that do not express DAAM2 (27) vs lines expressing it (23) | 3.04× lower at baseline in the lines without DAAM2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, ZNF471, SDC2; maybe low, not absent; co-absent with the target |
| [[AEBP1]] | C | DAAM2 activity raises AEBP1's level | lines that do not express DAAM2 (27) vs lines expressing it (23) | 2.89× lower at baseline in the lines without DAAM2 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, ZNF471, SDC2; maybe low, not absent; co-absent with the target |
| [[SRPX]] | C | DAAM2 activity raises SRPX's level | lines that do not express DAAM2 (27) vs lines expressing it (23) | 3.60× lower at baseline in the lines without DAAM2 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, ZNF471, SDC2; maybe low, not absent; co-absent with the target |
| [[SMIM10]] | C | DAAM2 activity raises SMIM10's level | lines that do not express DAAM2 (27) vs lines expressing it (23) | 1.55× lower at baseline in the lines without DAAM2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, ZNF471, SDC2; maybe low, not absent; co-absent with the target |
| [[ANKRD30B]] | C | DAAM2 activity raises ANKRD30B's level | lines that do not express DAAM2 (27) vs lines expressing it (23) | 2.26× lower at baseline in the lines without DAAM2 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, ZNF471, SDC2; maybe low, not absent; co-absent with the target |
| [[C10orf90]] | C | DAAM2 activity raises C10orf90's level | lines that do not express DAAM2 (27) vs lines expressing it (23) | 2.41× lower at baseline in the lines without DAAM2 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, ZNF471, SDC2; maybe low, not absent; co-absent with the target |
| [[SLAMF7]] | C | DAAM2 activity raises SLAMF7's level | lines that do not express DAAM2 (27) vs lines expressing it (23) | 2.21× lower at baseline in the lines without DAAM2 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, ZNF471, SDC2; maybe low, not absent; co-absent with the target |
| [[LOXL3]] | C | DAAM2 activity raises LOXL3's level | lines that do not express DAAM2 (27) vs lines expressing it (23) | 2.49× lower at baseline in the lines without DAAM2 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, ZNF471, SDC2; maybe low, not absent; co-absent with the target |
| [[PAX3]] | C | DAAM2 activity raises PAX3's level | lines that do not express DAAM2 (27) vs lines expressing it (23) | 3.14× lower at baseline in the lines without DAAM2 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, ZNF471, SDC2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.737). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (53.1, 24.4); signed map (25.2, 39.0). **Vector** length 40.1, 9.83% of its response variance represented; |z| ≥ 3 in 466 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.5 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +7.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +12.2 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.6 | +4.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.6 | +4.9 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.6 | +3.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.6 | +3.7 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -1.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.7 | -2.4 |
|  | [[Encorafenib (drug)]] 5 µM |  | -0.7 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | dishevelled associated activator of morphogenesis 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.2 — chr6:39,792,298-39,904,877 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0381, NPHS24 |
| Gene groups (HGNC) | Armadillo like helical domain containing; Formins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86T65](https://www.uniprot.org/uniprotkb/Q86T65) (Disheveled-associated activator of morphogenesis 2):

> Key regulator of the Wnt signaling pathway, which is required for various processes during development, such as dorsal patterning, determination of left/right symmetry or myelination in the central nervous system. Acts downstream of Wnt ligands and upstream of beta-catenin (CTNNB1). Required for canonical Wnt signaling pathway during patterning in the dorsal spinal cord by promoting the aggregation of Disheveled (Dvl) complexes, thereby clustering and formation of Wnt receptor signalosomes and …

**Summary**, from NCBI Gene [23500](https://www.ncbi.nlm.nih.gov/gene/23500):

> Predicted to enable actin binding activity and small GTPase binding activity. Involved in several processes, including podocyte cell migration; regulation of actin filament polymerization; and regulation of filopodium assembly. Located in nucleoplasm. Implicated in nephrotic syndrome type 24. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18143](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18143) · Entrez [23500](https://www.ncbi.nlm.nih.gov/gene/23500) · UniProt [Q86T65](https://www.uniprot.org/uniprotkb/Q86T65) · Ensembl [ENSG00000146122](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146122)

## Data

Gene col 7067: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7067); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7067, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7067]; `tensor/DDL_lfc|DDL_z.npy` [7067]; `embed/gene_vectors.npy` [7067]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7067 or target_col == 7067). Every well: [[DAAM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DAAM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
