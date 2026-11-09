---
symbol: "IGFBP1"
type: "gene"
col: 7113
ensembl_id: "ENSG00000146678"
name: "insulin like growth factor binding protein 1"
location: "7p12.3"
module: 8
arm: "+"
pooled_cpm: 20.7
n_lines_expressing: 11
n_dd_up: 7
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 28
direction_downstream: 35
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# IGFBP1

*insulin like growth factor binding protein 1* — 7p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.18× (z +10.7, q 5e-24, up in 4 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 1.84× (z +3.6, q 0.045, up in 3 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.418× (z -5.1, q 2e-04, down in 9 of 9 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITIH2]] (+0.82, fdr 1e-05), [[CP]] (+0.69, fdr 7e-06), [[CD38]] (+0.67, fdr 1e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[SLC16A4]] → it (grade B ⚠); 35 go from it, the strongest it → [[LINC01504]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7113.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.18×** | +10.7 | 5e-24 | 4/8 (AsPC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.50×** | +7.1 | 4e-10 | 5/8 (AsPC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.90×** | +5.8 | 1e-06 | 3/8 (SNU-423, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.84×** | +3.6 | 0.045 | 3/9 (SNU-423, A549, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 5 µM |  | **3.16×** | +3.5 | 0.046 | 2/9 (HepG2/C3A, A549) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.95×** | +3.4 | 0.055 | 5/9 (AsPC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.75×** | +3.3 | 0.085 | 1/9 (HS-578T) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Sulfatinib (drug)]] 5 µM |  | 1.74× | +3.1 | 0.11 | 2/9 (HepG2/C3A, CFPAC-1) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 5 µM |  | 1.73× | +3.1 | 0.11 | 4/9 (SNU-423, HepG2/C3A, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.45× | +3.1 | 0.11 | 4/9 (AsPC-1, SNU-423, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.69× | +3.1 | 0.11 | 3/9 (SNU-423, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | 1.68× | +3.0 | 0.11 | 1/9 (COLO 205) | top dose only |  |
| [[Alpelisib (drug)]] 5 µM |  | 2.66× | +3.0 | 0.11 | 4/9 (AsPC-1, A549, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7113.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.418×** | -5.1 | 2e-04 | 9/9 (CFPAC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~23% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.559×** | -4.8 | 4e-04 | 8/9 (HepG2/C3A, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.466×** | -4.3 | 0.002 | 8/9 (HepG2/C3A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.480×** | -4.3 | 0.002 | 8/9 (A549, HepG2/C3A, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.511×** | -3.9 | 0.009 | 8/9 (A549, COLO 205, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.549×** | -3.5 | 0.035 | 7/9 (COLO 205, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.318×** | -3.5 | 0.035 | 8/9 (CFPAC-1, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.542×** | -3.3 | 0.061 | 4/9 (HepG2/C3A, NCI-H2030, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.562× | -3.1 | 0.11 | 1/9 (COLO 205) | inconsistent across doses | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.592× | -3.1 | 0.12 | 0/9 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.49 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7113. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 112 | 0 | 6 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0191× (z -13.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0772× (z -12.7) |
| [[HepG2_C3A (line)]] | wt | 1,009 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0328× (z -22.9) |
| [[CFPAC-1 (line)]] | alt | 58.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0663× (z -17.3) |
| [[COLO 205 (line)]] | alt | 19.4 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0260× (z -10.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.0458× (z -8.8) |
| [[SNU-423 (line)]] | alt | 23.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0275× (z -19.2) |
| [[AsPC-1 (line)]] | alt | 63.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0861× (z -12.1) |
| [[HS-578T (line)]] | alt | 7.61 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0294× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 30.3 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0148× (z -9.4) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.39 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.04 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.26 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.01 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.96 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.43 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7113), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITIH2]] | +0.82 | +0.82 / +0.51 | both halves | 1e-05 | pathway: Post-translational protein phosphorylation; STRING 489 |
| [[CP]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[CD38]] | +0.67 | +0.52 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[CYP24A1]] | +0.64 | +0.68 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[DSCAML1]] | +0.58 | +0.46 / +0.50 | both halves | 3e-05 | **novel candidate** |
| [[FGA]] | +0.57 | +0.58 / +0.47 | both halves | 2e-05 | pathway: Post-translational protein phosphorylation; STRING 706 |
| [[TARID]] | +0.56 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[PON3]] | +0.56 | +0.53 / +0.37 | both halves | 8e-05 |  |
| [[TIMD4]] | +0.56 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[CSGALNACT1]] | +0.54 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[HAVCR1]] | +0.53 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[FXYD2]] | +0.50 | +0.40 / +0.37 | both halves | 9e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 3, C 25. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A4]] | B | SLC16A4 activity raises IGFBP1's level | lines that do not express SLC16A4 (15) vs lines expressing it (35) | 1.92× lower at baseline in the lines without SLC16A4 | 0.076 | ⚠ within organs, on part of the lines; also absent: TNFRSF10C, LYPD3, GNAS-AS1; maybe low, not absent |
| [[CASP10]] | B | CASP10 activity raises IGFBP1's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.34× lower at baseline in the lines without CASP10 | 0.082 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[HDAC6]] | B | HDAC6 activity raises IGFBP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FGA]] | C | FGA activity raises IGFBP1's level | lines that do not express FGA (43) vs lines expressing it (7) | 14.32× lower at baseline in the lines without FGA | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |
| [[ITIH2]] | C | ITIH2 activity raises IGFBP1's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 8.36× lower at baseline in the lines without ITIH2 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH; co-absent with the target |
| [[FXYD2]] | C | FXYD2 activity raises IGFBP1's level | lines that do not express FXYD2 (38) vs lines expressing it (12) | 3.82× lower at baseline in the lines without FXYD2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSCAML1, ITIH2, FGA; co-absent with the target |
| [[POU5F1]] | C | POU5F1 activity raises IGFBP1's level | lines that do not express POU5F1 (27) vs lines expressing it (23) | 3.19× lower at baseline in the lines without POU5F1 | 0.008 | ⚠ within organs, on part of the lines; also absent: P2RY2, C4BPB, UGT1A6; co-absent with the target |
| [[TIMD4]] | C | TIMD4 activity raises IGFBP1's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 4.76× lower at baseline in the lines without TIMD4 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA; co-absent with the target |
| [[FGG]] | C | FGG activity raises IGFBP1's level | lines that do not express FGG (42) vs lines expressing it (8) | 7.25× lower at baseline in the lines without FGG | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB; co-absent with the target |
| [[DUOX2]] | C | DUOX2 activity raises IGFBP1's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 3.01× lower at baseline in the lines without DUOX2 | 0.012 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB; co-absent with the target |
| [[HAVCR1]] | C | HAVCR1 activity raises IGFBP1's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 4.18× lower at baseline in the lines without HAVCR1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA; co-absent with the target |
| [[APOL1]] | C | APOL1 activity raises IGFBP1's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.31× lower at baseline in the lines without APOL1 | 0.022 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1; co-absent with the target |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 11, C 24. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01504]] | B | IGFBP1 activity raises LINC01504's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 1.38× lower at baseline in the lines without IGFBP1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2 |
| [[ODF3B]] | B | IGFBP1 activity raises ODF3B's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 2.53× lower at baseline in the lines without IGFBP1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2 |
| [[SPATA6L]] | B | IGFBP1 activity raises SPATA6L's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 2.05× lower at baseline in the lines without IGFBP1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2 |
| [[AADACL2-AS1]] | B | IGFBP1 activity raises AADACL2-AS1's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 1.60× lower at baseline in the lines without IGFBP1 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2 |
| [[EHBP1-AS1]] | B | IGFBP1 activity raises EHBP1-AS1's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 1.16× lower at baseline in the lines without IGFBP1 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2 |
| [[FMO5]] | B | IGFBP1 activity raises FMO5's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 2.03× lower at baseline in the lines without IGFBP1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2 |
| [[SESTD1]] | B | IGFBP1 activity raises SESTD1's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 2.27× lower at baseline in the lines without IGFBP1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2 |
| [[TYMP]] | B | IGFBP1 activity raises TYMP's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 3.13× lower at baseline in the lines without IGFBP1 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2 |
| [[XDH]] | B | IGFBP1 activity raises XDH's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 2.99× lower at baseline in the lines without IGFBP1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2 |
| [[DEPTOR]] | B | IGFBP1 activity raises DEPTOR's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 1.71× lower at baseline in the lines without IGFBP1 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2 |
| [[IGSF11]] | B | IGFBP1 activity raises IGSF11's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 1.76× lower at baseline in the lines without IGFBP1 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2 |
| [[POU5F1]] | C | IGFBP1 activity raises POU5F1's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 4.25× lower at baseline in the lines without IGFBP1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.380). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.2, 44.7); signed map (52.0, 26.2). **Vector** length 36.0, 12.5% of its response variance represented; |z| ≥ 3 in 236 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +3.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +1.8 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | -0.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.0 | +3.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +2.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -3.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.8 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.7 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.7 | -1.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -0.7 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | insulin like growth factor binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p12.3 — chr7:45,888,360-45,893,660 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IGF-BP25, AFBP, hIGFBP-1, PP12; previously IBP1 |
| Gene groups (HGNC) | Insulin like growth factor binding proteins |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, XENOBIOTIC_METABOLISM, HYPOXIA |
| Reactome | 9 pathways, smallest: FOXO-mediated transcription of oxidative stress, metabolic and neuronal genes; ATF4 activates genes in response to endoplasmic reticulum  stress; PERK regulates gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [P08833](https://www.uniprot.org/uniprotkb/P08833) (Insulin-like growth factor-binding protein 1):

> Multifunctional protein that plays a critical role in regulating the availability of IGFs such as IGF1 and IGF2 to their receptors and thereby regulates IGF-mediated cellular processes including cell migration, proliferation, differentiation or apoptosis in a cell-type specific manner. Also plays a positive role in cell migration by interacting with integrin ITGA5:ITGB1 through its RGD motif. Mechanistically, binding to integrins leads to activation of focal adhesion kinase/PTK2 and stimulation …

**Summary**, from NCBI Gene [3484](https://www.ncbi.nlm.nih.gov/gene/3484):

> This gene is a member of the insulin-like growth factor binding protein (IGFBP) family and encodes a protein with an IGFBP N-terminal domain and a thyroglobulin type-I domain. The encoded protein, mainly expressed in the liver, circulates in the plasma and binds both insulin-like growth factors (IGFs) I and II, prolonging their half-lives and altering their interaction with cell surface receptors. This protein is important in cell migration and metabolism. Low levels of this protein may be …

**Accessions** — [HGNC:5469](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5469) · Entrez [3484](https://www.ncbi.nlm.nih.gov/gene/3484) · UniProt [P08833](https://www.uniprot.org/uniprotkb/P08833) · Ensembl [ENSG00000146678](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146678)

## Data

Gene col 7113: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7113); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7113, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7113]; `tensor/DDL_lfc|DDL_z.npy` [7113]; `embed/gene_vectors.npy` [7113]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7113 or target_col == 7113). Every well: [[IGFBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGFBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
