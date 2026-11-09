---
symbol: "CYP24A1"
type: "gene"
col: 311
ensembl_id: "ENSG00000019186"
name: "cytochrome P450 family 24 subfamily A member 1"
location: "20q13.2"
module: 19
arm: "+"
pooled_cpm: 55.69
n_lines_expressing: 11
n_dd_up: 13
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 10
direction_downstream: 12
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# CYP24A1

*cytochrome P450 family 24 subfamily A member 1* — 20q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.46× (z +10.5, q 4e-23, up in 2 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.96× (z +8.1, q 2e-13, up in 9 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.438× (z -7.0, q 1e-09, down in 7 of 9 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UPK1B]] (+0.68, fdr 1e-05), [[ITIH2]] (+0.64, fdr 3e-05), [[RSPO3]] (+0.64, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[UPK1B]] → it (grade C ⚠); 12 go from it, the strongest it → [[LMTK3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 311.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.46×** | +10.5 | 4e-23 | 2/8 (A-427, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.96×** | +8.1 | 2e-13 | 9/9 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.56×** | +7.6 | 4e-12 | 1/8 (A-427) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.19×** | +6.7 | 4e-09 | 9/9 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +5.4 | 6e-06 | 2/8 (NCI-H2030, A-427) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.78×** | +4.5 | 6e-04 | 2/9 (A-427, NCI-H1573) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.04×** | +4.2 | 0.002 | 4/9 (CFPAC-1, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.044 | 6/10 (HepG2/C3A, A549, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.3 | 0.057 | 1/10 (A-427) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.45×** | +3.2 | 0.090 | 3/9 (A549, CFPAC-1, …) | inconsistent across doses |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.44×** | +3.1 | 0.090 | 3/9 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.70×** | +3.1 | 0.090 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.69×** | +3.1 | 0.097 | 2/9 (CFPAC-1, HepG2/C3A) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.29× | +3.0 | 0.10 | 3/9 (SW1417, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 311.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.438×** | -7.0 | 1e-09 | 7/9 (NCI-H1573, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.582×** | -6.5 | 3e-08 | 8/9 (NCI-H1573, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.536×** | -5.1 | 7e-05 | 8/9 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.607×** | -4.2 | 0.003 | 3/9 (NCI-H1573, A549, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.633×** | -3.9 | 0.011 | 3/9 (NCI-H1573, CFPAC-1, …) | two highest doses | position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.634×** | -3.9 | 0.011 | 4/9 (NCI-H1573, CFPAC-1, …) | all doses, flat | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.639×** | -3.8 | 0.012 | 7/9 (CFPAC-1, NCI-H2030, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.885× | -3.6 | 0.024 | 1/11 (NCI-H23) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.652×** | -3.3 | 0.051 | 1/9 (NCI-H23) | inconsistent across doses | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **0.677×** | -3.3 | 0.053 | 5/9 (NCI-H1573, CFPAC-1, …) | top dose only | position effect removed |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.666×** | -3.2 | 0.059 | 0/9 | inconsistent across doses | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.685×** | -3.2 | 0.064 | 0/9 | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.777× | -3.0 | 0.11 | 4/9 (NCI-H1573, CFPAC-1, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 311. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 935 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0106× (z -36.2) |
| [[A549 (line)]] | wt | 472 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0686× (z -18.0) |
| [[NCI-H2030 (line)]] | alt | 347 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0929× (z -17.7) |
| [[CFPAC-1 (line)]] | alt | 59.5 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 5.19× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.0701× (z -14.9) |
| [[HepG2_C3A (line)]] | wt | 132 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0764× (z -18.6) |
| [[NCI-H2347 (line)]] | alt | 21.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -12.2) |
| [[SW1417 (line)]] | alt | 34.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -12.2) |
| [[A-172 (line)]] | wt | 5.17 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.89 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.11 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.43 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.94 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.19 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.88 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.09 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.14 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.11 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.17 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.78 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.98 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.51 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.40 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 9.25 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.50 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.02 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.81 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.65 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.96 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.90 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.25 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.14 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.96 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.95 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.31 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.28 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.85 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 10.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 311), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UPK1B]] | +0.68 | +0.71 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[ITIH2]] | +0.64 | +0.70 / +0.43 | both halves | 3e-05 | **novel candidate** |
| [[RSPO3]] | +0.64 | +0.59 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[IGFBP1]] | +0.64 | +0.68 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[XDH]] | +0.63 | +0.55 / +0.59 | both halves | 1e-05 | **novel candidate** |
| [[SMOC1]] | +0.62 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[CSGALNACT1]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[RAB27B]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[TIMD4]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[TARID]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[LGSN]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[EYA2]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UPK1B]] | C | UPK1B activity raises CYP24A1's level | lines that do not express UPK1B (39) vs lines expressing it (11) | 5.24× lower at baseline in the lines without UPK1B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CES1, CGA, SLC15A5; maybe low, not absent; co-absent with the target |
| [[FGA]] | C | FGA activity raises CYP24A1's level | lines that do not express FGA (43) vs lines expressing it (7) | 9.41× lower at baseline in the lines without FGA | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |
| [[GPR141]] | C | GPR141 activity raises CYP24A1's level | lines that do not express GPR141 (39) vs lines expressing it (11) | 4.66× lower at baseline in the lines without GPR141 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NRG3, S100A8, LINC00879; co-absent with the target |
| [[MUC16]] | C | MUC16 activity raises CYP24A1's level | lines that do not express MUC16 (38) vs lines expressing it (12) | 3.94× lower at baseline in the lines without MUC16 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4; co-absent with the target |
| [[TIMD4]] | C | TIMD4 activity raises CYP24A1's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 4.10× lower at baseline in the lines without TIMD4 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA; co-absent with the target |
| [[VNN1]] | C | VNN1 activity raises CYP24A1's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.05× lower at baseline in the lines without VNN1 | 0.057 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B; co-absent with the target |
| [[ITIH2]] | C | ITIH2 activity raises CYP24A1's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 4.46× lower at baseline in the lines without ITIH2 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH; co-absent with the target |
| [[SYT13]] | C | SYT13 activity raises CYP24A1's level | lines that do not express SYT13 (33) vs lines expressing it (17) | 3.03× lower at baseline in the lines without SYT13 | 0.062 | ⚠ within organs, on part of the lines; also absent: SCEL, HS3ST1, FGFBP1; co-absent with the target |
| [[ATP10A]] | C | ATP10A activity raises CYP24A1's level | lines that do not express ATP10A (25) vs lines expressing it (25) | 2.77× lower at baseline in the lines without ATP10A | 0.078 | ⚠ within organs, on part of the lines; also absent: STAC, SALL1, TGFBI; co-absent with the target |
| [[TSHZ2]] | C | TSHZ2 activity raises CYP24A1's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 2.06× lower at baseline in the lines without TSHZ2 | 0.098 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 5, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMTK3]] | B | CYP24A1 activity raises LMTK3's level | lines that do not express CYP24A1 (39) vs lines expressing it (11) | 2.65× lower at baseline in the lines without CYP24A1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, S100A9, FGG |
| [[FGD6]] | B | CYP24A1 activity raises FGD6's level | lines that do not express CYP24A1 (39) vs lines expressing it (11) | 3.06× lower at baseline in the lines without CYP24A1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, S100A9, FGG |
| [[XDH]] | B | CYP24A1 activity raises XDH's level | lines that do not express CYP24A1 (39) vs lines expressing it (11) | 3.15× lower at baseline in the lines without CYP24A1 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, S100A9, FGG |
| [[PTP4A1]] | B | CYP24A1 activity raises PTP4A1's level | lines that do not express CYP24A1 (39) vs lines expressing it (11) | 2.41× lower at baseline in the lines without CYP24A1 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, S100A9, FGG |
| [[ODF3B]] | B | CYP24A1 activity raises ODF3B's level | lines that do not express CYP24A1 (39) vs lines expressing it (11) | 2.34× lower at baseline in the lines without CYP24A1 | 0.0998 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, S100A9, FGG |
| [[ATP10A]] | C | CYP24A1 activity raises ATP10A's level | lines that do not express CYP24A1 (39) vs lines expressing it (11) | 5.16× lower at baseline in the lines without CYP24A1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, S100A9, FGG; co-absent with the target |
| [[RHOV]] | C | CYP24A1 activity raises RHOV's level | lines that do not express CYP24A1 (39) vs lines expressing it (11) | 3.81× lower at baseline in the lines without CYP24A1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, S100A9, FGG; co-absent with the target |
| [[MUC16]] | C | CYP24A1 activity raises MUC16's level | lines that do not express CYP24A1 (39) vs lines expressing it (11) | 5.07× lower at baseline in the lines without CYP24A1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, S100A9, FGG; co-absent with the target |
| [[TESC]] | C | CYP24A1 activity raises TESC's level | lines that do not express CYP24A1 (39) vs lines expressing it (11) | 3.35× lower at baseline in the lines without CYP24A1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, S100A9, FGG; co-absent with the target |
| [[HAVCR1]] | C | CYP24A1 activity raises HAVCR1's level | lines that do not express CYP24A1 (39) vs lines expressing it (11) | 2.44× lower at baseline in the lines without CYP24A1 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, S100A9, FGG; co-absent with the target |
| [[FGA]] | C | CYP24A1 activity raises FGA's level | lines that do not express CYP24A1 (39) vs lines expressing it (11) | 3.72× lower at baseline in the lines without CYP24A1 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, S100A9, FGG; co-absent with the target |
| [[IGFBP1]] | C | CYP24A1 activity raises IGFBP1's level | lines that do not express CYP24A1 (39) vs lines expressing it (11) | 3.94× lower at baseline in the lines without CYP24A1 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, S100A9, FGG; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.252). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.3, 45.1); signed map (52.4, 25.9). **Vector** length 49.4, 20.7% of its response variance represented; |z| ≥ 3 in 286 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +0.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +4.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.6 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -3.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.1 | -7.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -3.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.0 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome P450 family 24 subfamily A member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.2 — chr20:54,153,446-54,173,986 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CP24, P450-CC24, lncBCAS1-4_1; previously CYP24 |
| Gene groups (HGNC) | Cytochrome P450 family 24 |
| Reactome | 9 pathways, smallest: Vitamins; Vitamin D (calciferol) metabolism; Metabolic disorders of biological oxidation enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07973](https://www.uniprot.org/uniprotkb/Q07973) (1,25-dihydroxyvitamin D(3) 24-hydroxylase, mitochondrial):

> A cytochrome P450 monooxygenase with a key role in vitamin D catabolism and calcium homeostasis. Via C24- and C23-oxidation pathways, catalyzes the inactivation of both the vitamin D precursor calcidiol (25-hydroxyvitamin D(3)) and the active hormone calcitriol (1-alpha,25-dihydroxyvitamin D(3)). With initial hydroxylation at C-24 (via C24-oxidation pathway), performs a sequential 6-step oxidation of calcitriol leading to the formation of the biliary metabolite calcitroic acid. With initial …

**Summary**, from NCBI Gene [1591](https://www.ncbi.nlm.nih.gov/gene/1591):

> This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. This mitochondrial protein initiates the degradation of 1,25-dihydroxyvitamin D3, the physiologically active form of vitamin D3, by hydroxylation of the side chain. In regulating the level of vitamin D3, this enzyme plays a role in calcium homeostasis and the …

**Accessions** — [HGNC:2602](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2602) · Entrez [1591](https://www.ncbi.nlm.nih.gov/gene/1591) · UniProt [Q07973](https://www.uniprot.org/uniprotkb/Q07973) · Ensembl [ENSG00000019186](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000019186)

## Data

Gene col 311: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 311); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 311, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 311]; `tensor/DDL_lfc|DDL_z.npy` [311]; `embed/gene_vectors.npy` [311]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 311 or target_col == 311). Every well: [[CYP24A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP24A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
