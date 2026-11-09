---
symbol: "SLC14A2"
type: "gene"
col: 5387
ensembl_id: "ENSG00000132874"
name: "solute carrier family 14 member 2"
location: "18q12.3"
module: 166
arm: "+"
pooled_cpm: 3.1
n_lines_expressing: 48
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 13
direction_downstream: 0
tags: ["gene", "module/166"]
generated_by: "tahoemap"
---

# SLC14A2

*solute carrier family 14 member 2* — 18q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.63× (z +16.2, q 0e+00, up in 16 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.636× (z -4.0, q 0.032, down in 9 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (RPMI-7951 0.0168×, SNU-423 0.0239×; ⚠ toxic; cell-cycle shift, explains ~2% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SNU-423 0.0481×, RPMI-7951 0.115×); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (RPMI-7951 0.0530×, SNU-423 0.0347×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (RPMI-7951 0.0351×); [[Digitoxin (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0802×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01500]] (+0.81, fdr 7e-06), [[CFAP20DC-DT]] (+0.77, fdr 7e-06), [[RBFOX1]] (+0.70, fdr 7e-06).
> It is in [[Module 166]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5387.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.63×** | +16.2 | 0e+00 | 16/23 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.15×** | +12.6 | 6e-34 | 3/8 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.99×** | +11.8 | 8e-30 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.96×** | +9.6 | 9e-20 | 25/39 (BT-474, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.10×** | +9.3 | 1e-18 | 12/26 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.71×** | +8.2 | 3e-14 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.81×** | +5.3 | 1e-05 | 1/6 (SW480) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.7 | 2e-04 | 7/42 (A549, NCI-H460, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +4.7 | 2e-04 | 6/17 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +4.3 | 9e-04 | 10/41 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +4.1 | 0.002 | 4/26 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +4.1 | 0.002 | 6/27 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +4.0 | 0.002 | 5/31 (C32, HEC-1-A, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.20×** | +3.7 | 0.010 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.17×** | +3.6 | 0.013 | 0/3 | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.038 | 0/17 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5387.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (RPMI-7951 0.0168×, SNU-423 0.0239×; ⚠ toxic; cell-cycle shift, explains ~2% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SNU-423 0.0481×, RPMI-7951 0.115×); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (RPMI-7951 0.0530×, SNU-423 0.0347×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (RPMI-7951 0.0351×); [[Digitoxin (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0802×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.636×** | -4.0 | 0.032 | 9/41 (A-172, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.667×** | -3.6 | 0.086 | 10/35 (RPMI-7951, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5387. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 76.3 | 0 | 10 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0168× (z -13.3) ⚠ toxic; cell-cycle shift, explains ~2% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0351× (z -11.4) |
| [[SNU-423 (line)]] | alt | 27.3 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0359× (z -13.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0481× (z -11.9) |
| [[A-172 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.709 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.940 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.896 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.957 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.903 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.790 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.913 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.776 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.926 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.966 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.757 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.889 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.997 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.866 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5387), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01500]] | +0.81 | +0.71 / +0.83 | both halves | 7e-06 |  |
| [[CFAP20DC-DT]] | +0.77 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[RBFOX1]] | +0.70 | +0.67 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[KCNIP1]] | +0.70 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[SLC8A1-AS1]] | +0.69 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[LINC01358]] | +0.68 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[LDB2]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[SEMA6D]] | +0.67 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[GRIN2A]] | +0.67 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[LINC01151]] | +0.66 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[VCAN-AS1]] | +0.66 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[SYNDIG1]] | +0.65 | +0.58 / +0.65 | both halves | 8e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC14A2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KCNE4]] | B | KCNE4 activity raises SLC14A2's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 2.58× lower at baseline in the lines without KCNE4 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN |
| [[HTRA3]] | B | HTRA3 activity raises SLC14A2's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 1.83× lower at baseline in the lines without HTRA3 | 0.041 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| [[PDGFRB]] | B | PDGFRB activity raises SLC14A2's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.46× lower at baseline in the lines without PDGFRB | 0.046 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[SLC24A3]] | B | SLC24A3 activity raises SLC14A2's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 1.68× lower at baseline in the lines without SLC24A3 | 0.053 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent |
| [[IGFBP5]] | B | IGFBP5 activity raises SLC14A2's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 2.06× lower at baseline in the lines without IGFBP5 | 0.059 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2 |
| [[ITGA11]] | B | ITGA11 activity raises SLC14A2's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.25× lower at baseline in the lines without ITGA11 | 0.069 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |
| [[HTR1F]] | B | HTR1F activity raises SLC14A2's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 1.95× lower at baseline in the lines without HTR1F | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent |
| [[DIRC3]] | B | DIRC3 activity raises SLC14A2's level | lines that do not express DIRC3 (19) vs lines expressing it (31) | 1.76× lower at baseline in the lines without DIRC3 | 0.081 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent |
| [[LINC01411]] | B | LINC01411 activity raises SLC14A2's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 2.60× lower at baseline in the lines without LINC01411 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032 |
| [[KC6]] | B | KC6 activity raises SLC14A2's level | lines that do not express KC6 (32) vs lines expressing it (18) | 2.27× lower at baseline in the lines without KC6 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1 |
| [[OR9Q1]] | B | OR9Q1 activity raises SLC14A2's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 1.99× lower at baseline in the lines without OR9Q1 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 166]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.772). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.3, 26.2); signed map (29.7, 15.3). **Vector** length 53.2, 7.82% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +16.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +12.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +0.9 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.0 | +3.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -4.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -0.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 14 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.3 — chr18:45,212,995-45,683,688 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HUT2, UT2 |
| Gene groups (HGNC) | Solute carrier family 14 |
| Reactome | 3 pathways, smallest: SLC-mediated transport of organic cations; SLC-mediated transmembrane transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15849](https://www.uniprot.org/uniprotkb/Q15849) (Urea transporter 2):

> [Isoform 1]: Mediates the transport of urea driven by a concentration gradient across the cell membrane of the renal inner medullary collecting duct which is critical to the urinary concentrating mechanism.; [Isoform 2]: Mediates the transport of urea driven by a concentration gradient across the cell membrane of the kidney inner medullary collecting duct which is critical to the urinary concentrating mechanism.

**Summary**, from NCBI Gene [8170](https://www.ncbi.nlm.nih.gov/gene/8170):

> The protein encoded by this gene belongs to the urea transporter family. In mammalian cells, urea is the chief end product of nitrogen catabolism, and plays an important role in the urinary concentration mechanism. This protein is expressed in the inner medulla of the kidney, and mediates rapid transepithelial urea transport across the inner medullary collecting duct. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:10919](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10919) · Entrez [8170](https://www.ncbi.nlm.nih.gov/gene/8170) · UniProt [Q15849](https://www.uniprot.org/uniprotkb/Q15849) · Ensembl [ENSG00000132874](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132874)

## Data

Gene col 5387: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5387); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5387, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5387]; `tensor/DDL_lfc|DDL_z.npy` [5387]; `embed/gene_vectors.npy` [5387]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5387 or target_col == 5387). Every well: [[SLC14A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC14A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
