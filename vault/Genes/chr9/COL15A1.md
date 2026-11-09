---
symbol: "COL15A1"
type: "gene"
col: 12845
ensembl_id: "ENSG00000204291"
name: "collagen type XV alpha 1 chain"
location: "9q22.33"
module: 13
arm: "+"
pooled_cpm: 4.28
n_lines_expressing: 22
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 57
direction_downstream: 56
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# COL15A1

*collagen type XV alpha 1 chain* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.48× (z +12.3, q 5e-32, up in 1 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.99× (z +8.3, q 1e-14, up in 12 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.615× (z -4.2, q 0.017, down in 11 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETBP1]] (+0.69, fdr 7e-06), [[NMNAT2]] (+0.67, fdr 9e-06), [[ITGA11]] (+0.66, fdr 1e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 57 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 56 go from it, the strongest it → [[PPFIBP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12845.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.48×** | +12.3 | 5e-32 | 1/6 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.89×** | +10.7 | 2e-24 | 2/5 (HOP62, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.18×** | +9.9 | 1e-20 | 4/10 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.99×** | +8.3 | 1e-14 | 12/19 (NCI-H460, HS-578T, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +7.4 | 1e-11 | 2/16 (A549, HOP62) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +5.8 | 7e-07 | 3/12 (SK-MEL-2, C32, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.57×** | +5.4 | 6e-06 | 3/15 (HS-578T, SNU-423, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +4.7 | 2e-04 | 6/18 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.73×** | +4.5 | 5e-04 | 3/13 (NCI-H1792, hTERT-HPNE, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.4 | 6e-04 | 4/19 (SNU-423, A549, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.53×** | +4.1 | 0.002 | 1/6 (NCI-H460) | top dose only | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.92×** | +4.0 | 0.003 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.34×** | +3.8 | 0.007 | 0/8 | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.28×** | +3.7 | 0.010 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.53×** | +3.5 | 0.019 | 2/14 (HOP62, A549) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.51×** | +3.2 | 0.043 | 0/14 | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +3.0 | 0.095 | 3/19 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12845.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.615×** | -4.2 | 0.017 | 11/18 (RPMI-7951, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.636×** | -3.9 | 0.029 | 10/18 (NCI-H460, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.673×** | -3.4 | 0.099 | 4/18 (hTERT-HPNE, NCI-H460, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.757×** | -3.4 | 0.099 | 6/18 (NCI-H460, H4, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.663× | -3.3 | 0.12 | 5/18 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.777× | -3.1 | 0.19 | 3/20 (BT-474, H4, …) | top dose only |  |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.703× | -3.0 | 0.19 | 3/17 (A549, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12845. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 105 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.00544× (z -27.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0793× (z -19.0) |
| [[NCI-H460 (line)]] | wt | 10.9 | 0 | 6 (2 ⚠) | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0512× (z -14.9) |
| [[hTERT-HPNE (line)]] | wt | 30.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -10.2) |
| [[HOP62 (line)]] | alt | 15.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.7) |
| [[LoVo (line)]] | wt | 2.83 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0406× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.429 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.924 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.827 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.585 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.673 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.721 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.947 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.409 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.719 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.511 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.592 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.444 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12845), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETBP1]] | +0.69 | +0.66 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[NMNAT2]] | +0.67 | +0.57 / +0.63 | both halves | 9e-06 | **novel candidate** |
| [[ITGA11]] | +0.66 | +0.57 / +0.69 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[ANGPTL2]] | +0.66 | +0.51 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[APCDD1L]] | +0.65 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[DOCK2]] | +0.65 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[INSYN2B]] | +0.65 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[SDC2]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[SLC14A2]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[LINC01411]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[DKK3]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[SORCS2]] | +0.60 | +0.41 / +0.63 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*57 arrows, 57 of them with an alert ⚠; grade A 0, B 2, C 55. Shown: the 12 strongest; 45 more arrows (45 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers COL15A1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[COL13A1]] | B | COL13A1 activity raises COL15A1's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 2.11× lower at baseline in the lines without COL13A1 | 0.084 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[PDGFRB]] | C | PDGFRB activity raises COL15A1's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 3.97× lower at baseline in the lines without PDGFRB | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[LINC01583]] | C | LINC01583 activity raises COL15A1's level | lines that do not express LINC01583 (28) vs lines expressing it (22) | 3.67× lower at baseline in the lines without LINC01583 | 6e-04 | ⚠ within organs, on part of the lines; also absent: INSYN2B, ADAM12, ZEB2; co-absent with the target |
| [[SPOCK1]] | C | SPOCK1 activity raises COL15A1's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 3.64× lower at baseline in the lines without SPOCK1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises COL15A1's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 4.46× lower at baseline in the lines without LINC01411 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[C10orf90]] | C | C10orf90 activity raises COL15A1's level | lines that do not express C10orf90 (35) vs lines expressing it (15) | 3.85× lower at baseline in the lines without C10orf90 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GRIN2A, LINC01242, ADGRG7; maybe low, not absent; co-absent with the target |
| [[SIRLNT]] | C | SIRLNT activity raises COL15A1's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 3.33× lower at baseline in the lines without SIRLNT | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1; co-absent with the target |
| [[SEMA5A]] | C | SEMA5A activity raises COL15A1's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 2.84× lower at baseline in the lines without SEMA5A | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH; co-absent with the target |
| [[ADAM12]] | C | ADAM12 activity raises COL15A1's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 3.54× lower at baseline in the lines without ADAM12 | 0.003 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1; co-absent with the target |
| [[HTR1F]] | C | HTR1F activity raises COL15A1's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 3.40× lower at baseline in the lines without HTR1F | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent; co-absent with the target |
| [[CDH13]] | C | CDH13 activity raises COL15A1's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 3.56× lower at baseline in the lines without CDH13 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |

### Downstream of this gene

*56 arrows, 56 of them with an alert ⚠; grade A 0, B 7, C 49. Shown: the 12 strongest; 44 more arrows (44 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPFIBP1]] | B | COL15A1 activity raises PPFIBP1's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 1.71× lower at baseline in the lines without COL15A1 | 0.003 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC |
| [[MYO10]] | B | COL15A1 activity raises MYO10's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 1.97× lower at baseline in the lines without COL15A1 | 0.033 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC |
| [[COL13A1]] | B | COL15A1 activity raises COL13A1's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 3.63× lower at baseline in the lines without COL15A1 | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC |
| [[PRSS23]] | B | COL15A1 activity raises PRSS23's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 2.40× lower at baseline in the lines without COL15A1 | 0.037 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC |
| [[BOC]] | B | COL15A1 activity raises BOC's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 2.21× lower at baseline in the lines without COL15A1 | 0.069 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC |
| [[SLCO1C1]] | B | COL15A1 activity raises SLCO1C1's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 1.53× lower at baseline in the lines without COL15A1 | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC |
| [[PCDHGC3]] | B | COL15A1 activity raises PCDHGC3's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 2.49× lower at baseline in the lines without COL15A1 | 0.082 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC |
| [[INSYN2B]] | C | COL15A1 activity raises INSYN2B's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 5.82× lower at baseline in the lines without COL15A1 | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC; co-absent with the target |
| [[BMPER]] | C | COL15A1 activity raises BMPER's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 4.53× lower at baseline in the lines without COL15A1 | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC; co-absent with the target |
| [[LINC01583]] | C | COL15A1 activity raises LINC01583's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 3.66× lower at baseline in the lines without COL15A1 | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC; co-absent with the target |
| [[IL1B]] | C | COL15A1 activity raises IL1B's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 4.09× lower at baseline in the lines without COL15A1 | 0.005 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC; co-absent with the target |
| [[GDNF-AS1]] | C | COL15A1 activity raises GDNF-AS1's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 2.51× lower at baseline in the lines without COL15A1 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.717). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.4, 16.1); signed map (22.1, 46.0). **Vector** length 49.9, 11.8% of its response variance represented; |z| ≥ 3 in 549 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +10.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +0.5 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +1.0 | +1.5 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.0 | +0.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -3.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -2.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.8 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | collagen type XV alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.33 — chr9:98,943,179-99,070,787 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Collagen proteoglycans; Multiplexin collagens |
| Hallmark sets | MYOGENESIS, ADIPOGENESIS |
| Reactome | 7 pathways, smallest: Collagen chain trimerization; Collagen degradation; Assembly of collagen fibrils and other multimeric structures |
| Matched by | ensembl_id |

**Function**, from UniProt [P39059](https://www.uniprot.org/uniprotkb/P39059) (Collagen alpha-1(XV) chain):

> Structural protein that stabilizes microvessels and muscle cells, both in heart and in skeletal muscle.; Restin potently inhibits angiogenesis.

**Summary**, from NCBI Gene [1306](https://www.ncbi.nlm.nih.gov/gene/1306):

> This gene encodes the alpha chain of type XV collagen, a member of the FACIT collagen family (fibril-associated collagens with interrupted helices). Type XV collagen has a wide tissue distribution but the strongest expression is localized to basement membrane zones so it may function to adhere basement membranes to underlying connective tissue stroma. The proteolytically produced C-terminal fragment of type XV collagen is restin, a potentially antiangiogenic protein that is closely related to …

**Accessions** — [HGNC:2192](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2192) · Entrez [1306](https://www.ncbi.nlm.nih.gov/gene/1306) · UniProt [P39059](https://www.uniprot.org/uniprotkb/P39059) · Ensembl [ENSG00000204291](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204291)

## Data

Gene col 12845: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12845); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12845, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12845]; `tensor/DDL_lfc|DDL_z.npy` [12845]; `embed/gene_vectors.npy` [12845]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12845 or target_col == 12845). Every well: [[COL15A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL15A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
