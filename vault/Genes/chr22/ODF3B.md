---
symbol: "ODF3B"
type: "gene"
col: 10885
ensembl_id: "ENSG00000177989"
name: "ciliary microtubule associated protein 1B"
location: "22q13.33"
module: 167
arm: "+"
pooled_cpm: 3.75
n_lines_expressing: 37
n_dd_up: 4
n_dd_down: 26
n_dd_up_clean: 2
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 32
direction_downstream: 41
tags: ["gene", "module/167"]
generated_by: "tahoemap"
---

# ODF3B

*ciliary microtubule associated protein 1B* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.04× (z +4.5, q 0.004, up in 1 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 1.79× (z +3.7, q 0.041, up in 14 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.301× (z -7.8, q 3e-12, down in 27 of 33 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.345× (z -7.0, q 7e-10, down in 24 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TYMP]] (+0.85, fdr 7e-06, ⚠ same locus), [[CFB]] (+0.73, fdr 7e-06), [[HLA-F]] (+0.70, fdr 1e-05), [[IRF7]] (+0.70, fdr 1e-05).
> It is in [[Module 167]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 32 arrows point to it, the strongest [[MX1]] → it (grade B ⚠); 41 go from it, the strongest it → [[OAS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10885.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +4.5 | 0.004 | 1/6 (PANC-1) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +4.0 | 0.017 | 4/19 (NCI-H2030, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.79×** | +3.7 | 0.041 | 14/33 (NCI-H2030, AsPC-1, …) | rises with dose | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.41×** | +3.6 | 0.044 | 5/25 (NCI-H460, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 2.20× | +3.2 | 0.14 | 5/28 (RKO, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.5 µM |  | 1.60× | +3.1 | 0.19 | 11/29 (SW 900, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 1.61× | +3.0 | 0.19 | 10/31 (RKO, KATO III, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.52× | +3.0 | 0.19 | 4/33 (MIA PaCa-2, RKO, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10885.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.301×** | -7.8 | 3e-12 | 27/33 (A549, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.316×** | -7.5 | 1e-11 | 23/33 (NCI-H1573, Panc 03.27, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.345×** | -7.0 | 7e-10 | 24/33 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.508×** | -6.2 | 5e-08 | 19/25 (NCI-H2347, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.385×** | -6.2 | 5e-08 | 23/33 (NCI-H2347, A549, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.386×** | -6.2 | 5e-08 | 23/33 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.396×** | -5.7 | 9e-07 | 18/31 (KATO III, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.420×** | -5.7 | 1e-06 | 22/33 (Panc 03.27, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.464×** | -4.8 | 9e-05 | 13/30 (A549, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.486×** | -4.7 | 1e-04 | 22/33 (A549, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.613×** | -4.5 | 3e-04 | 19/32 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.536×** | -4.1 | 0.002 | 18/27 (RPMI-7951, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.540×** | -4.0 | 0.002 | 18/33 (RPMI-7951, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.540×** | -4.0 | 0.002 | 14/27 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.561×** | -3.8 | 0.006 | 19/33 (COLO 205, RPMI-7951, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.569×** | -3.7 | 0.009 | 15/32 (HOP62, PANC-1, …) | rises with dose | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.569×** | -3.5 | 0.012 | 5/33 (CFPAC-1, MIA PaCa-2, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.325×** | -3.3 | 0.026 | 10/25 (A549, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.605×** | -3.3 | 0.028 | 14/32 (Panc 03.27, BT-474, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.329×** | -3.3 | 0.028 | 14/32 (A549, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.80 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10885. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 8.51 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0126× (z -15.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.126× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 5.34 | 0 | 3 (1 ⚠) | — | [[Tofacitinib (drug)]] 0.5 µM 0.0325× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 4.46 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0531× (z -8.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0536× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 13.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 17.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -8.6) |
| [[KATO III (line)]] | alt | 9.40 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.139× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 9.08 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0393× (z -9.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H2347 (line)]] | alt | 6.64 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0672× (z -13.5) |
| [[A-172 (line)]] | wt | 0.269 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.222 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.849 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.244 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.266 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.599 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.962 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.717 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.378 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.618 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10885), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYMP]] | +0.85 | +0.77 / +0.87 | both halves | 7e-06 | STRING 497; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[CFB]] | +0.73 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[HLA-F]] | +0.70 | +0.55 / +0.77 | both halves | 1e-05 |  |
| [[IRF7]] | +0.70 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[GBP2]] | +0.66 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[IFI44L]] | +0.65 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[OAS1]] | +0.65 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[DHX58]] | +0.64 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[TMEM140]] | +0.64 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[MX1]] | +0.64 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[OASL]] | +0.64 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[IFIH1]] | +0.64 | +0.46 / +0.73 | both halves | 3e-05 |  |
| [[PSMB9]] | +0.63 | +0.46 / +0.71 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 31, C 1. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MX1]] | B | MX1 activity raises ODF3B's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.06× lower at baseline in the lines without MX1 | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[FGA]] | B | FGA activity raises ODF3B's level | lines that do not express FGA (43) vs lines expressing it (7) | 3.14× lower at baseline in the lines without FGA | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG |
| [[FGB]] | B | FGB activity raises ODF3B's level | lines that do not express FGB (42) vs lines expressing it (8) | 2.76× lower at baseline in the lines without FGB | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2 |
| [[IFI27]] | B | IFI27 activity raises ODF3B's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 2.11× lower at baseline in the lines without IFI27 | 0.008 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[ITIH2]] | B | ITIH2 activity raises ODF3B's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 1.89× lower at baseline in the lines without ITIH2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH |
| [[OAS1]] | B | OAS1 activity raises ODF3B's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.06× lower at baseline in the lines without OAS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[KYNU]] | B | KYNU activity raises ODF3B's level | lines that do not express KYNU (29) vs lines expressing it (21) | 1.98× lower at baseline in the lines without KYNU | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |
| [[IGFBP1]] | B | IGFBP1 activity raises ODF3B's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 2.53× lower at baseline in the lines without IGFBP1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2 |
| [[RSAD2]] | B | RSAD2 activity raises ODF3B's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.05× lower at baseline in the lines without RSAD2 | 0.015 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[CP]] | B | CP activity raises ODF3B's level | lines that do not express CP (39) vs lines expressing it (11) | 2.28× lower at baseline in the lines without CP | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |
| [[CASP10]] | B | CASP10 activity raises ODF3B's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.01× lower at baseline in the lines without CASP10 | 0.016 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[GBP4]] | B | GBP4 activity raises ODF3B's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.82× lower at baseline in the lines without GBP4 | 0.022 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |

### Downstream of this gene

*41 arrows, 41 of them with an alert ⚠; grade A 0, B 40, C 1. Shown: the 12 strongest; 29 more arrows (29 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS1]] | B | ODF3B activity raises OAS1's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 3.07× lower at baseline in the lines without ODF3B | 0.006 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[RIGI]] | B | ODF3B activity raises RIGI's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 1.63× lower at baseline in the lines without ODF3B | 0.006 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[PLSCR1]] | B | ODF3B activity raises PLSCR1's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 2.26× lower at baseline in the lines without ODF3B | 0.007 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[OAS2]] | B | ODF3B activity raises OAS2's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 2.95× lower at baseline in the lines without ODF3B | 0.007 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[HELZ2]] | B | ODF3B activity raises HELZ2's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 1.88× lower at baseline in the lines without ODF3B | 0.008 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[ISG15]] | B | ODF3B activity raises ISG15's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 1.99× lower at baseline in the lines without ODF3B | 0.012 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[IFI27]] | B | ODF3B activity raises IFI27's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 3.17× lower at baseline in the lines without ODF3B | 0.017 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[CMPK2]] | B | ODF3B activity raises CMPK2's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 1.98× lower at baseline in the lines without ODF3B | 0.018 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[IFI35]] | B | ODF3B activity raises IFI35's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 1.74× lower at baseline in the lines without ODF3B | 0.018 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[IFIH1]] | B | ODF3B activity raises IFIH1's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 1.95× lower at baseline in the lines without ODF3B | 0.021 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[NMI]] | B | ODF3B activity raises NMI's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 1.76× lower at baseline in the lines without ODF3B | 0.023 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[PSMB10]] | B | ODF3B activity raises PSMB10's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 1.12× lower at baseline in the lines without ODF3B | 0.026 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |

## Where it sits

- **Module**: [[Module 167]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.9, 50.1); signed map (61.2, 28.0). **Vector** length 62.3, 13.2% of its response variance represented; |z| ≥ 3 in 791 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.1 | +3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.0 | +3.6 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -3.1 | -4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -7.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.1 | -3.3 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.1 | -3.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ciliary microtubule associated protein 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,529,710-50,532,506 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FAP123; previously ODF3B |
| Matched by | ensembl_id |

UniProt [A8MYP8](https://www.uniprot.org/uniprotkb/A8MYP8) carries no function annotation.

**Summary**, from NCBI Gene [440836](https://www.ncbi.nlm.nih.gov/gene/440836):

> Predicted to be located in motile cilium. Predicted to be active in cytoskeleton. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:34388](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34388) · Entrez [440836](https://www.ncbi.nlm.nih.gov/gene/440836) · UniProt [A8MYP8](https://www.uniprot.org/uniprotkb/A8MYP8) · Ensembl [ENSG00000177989](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177989)

## Data

Gene col 10885: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10885); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10885, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10885]; `tensor/DDL_lfc|DDL_z.npy` [10885]; `embed/gene_vectors.npy` [10885]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10885 or target_col == 10885). Every well: [[ODF3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ODF3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
