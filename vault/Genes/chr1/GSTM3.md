---
symbol: "GSTM3"
type: "gene"
col: 5522
ensembl_id: "ENSG00000134202"
name: "glutathione S-transferase mu 3"
location: "1p13.3"
module: 93
arm: "+"
pooled_cpm: 8.85
n_lines_expressing: 36
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# GSTM3

*glutathione S-transferase mu 3* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.09× (z +15.7, q 0e+00, up in 30 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (A-172 0.0498×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.199×; ⚠ cell-cycle shift, explains ~80% of this change); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (HOP62 0.0785×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSPA2]] (+0.60, fdr 1e-05), [[MAP1LC3B2]] (+0.56, fdr 5e-05), [[TENT5C]] (+0.53, fdr 1e-05); moves opposite to [[NUDCD3]] (-0.54, fdr 2e-05), [[ACSF3]] (-0.50, fdr 4e-04), [[TIMM23B]] (-0.49, fdr 3e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CD40]] → it (grade B ⚠); 3 go from it, the strongest it → [[MIR9-1HG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5522.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.09×** | +15.7 | 0e+00 | 30/33 (LoVo, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.49×** | +8.9 | 1e-16 | 20/25 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.37×** | +8.1 | 8e-14 | 10/15 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +6.7 | 4e-09 | 27/33 (SW1417, C32, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +6.2 | 8e-08 | 22/34 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.1 | 1e-07 | 17/34 (SW1417, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.80×** | +5.8 | 6e-07 | 22/34 (A498, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.09×** | +5.6 | 1e-06 | 12/18 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.78×** | +5.6 | 1e-06 | 21/34 (PANC-1, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +5.5 | 3e-06 | 20/29 (CFPAC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.55×** | +4.3 | 1e-03 | 12/26 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.35×** | +4.1 | 0.002 | 17/33 (CFPAC-1, SW 900, …) | top dose only | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.003 | 14/33 (NCI-H23, H4, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.018 | 13/32 (NCI-H2347, BT-474, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.43×** | +3.5 | 0.019 | 12/33 (A498, SW1417, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.037 | 11/32 (CFPAC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5522.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (A-172 0.0498×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.199×; ⚠ cell-cycle shift, explains ~80% of this change); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (HOP62 0.0785×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.739× | -3.0 | 0.71 | 9/33 (J82, NCI-H661, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5522. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.52 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.43× (z +8.6) | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0498× (z -12.2) |
| [[HOP62 (line)]] | alt | 3.42 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +8.7) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0785× (z -9.0) |
| [[PANC-1 (line)]] | alt | 11.6 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +8.7) | — |
| [[A549 (line)]] | wt | 2.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 27.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +8.6) | — |
| [[H4 (line)]] | wt | 18.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +9.3) | — |
| [[LoVo (line)]] | wt | 2.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +12.1) | — |
| [[NCI-H2347 (line)]] | alt | 11.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 11.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.55× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 20.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -9.5) ⚠ cell-cycle shift, explains ~80% of this change |
| [[SW 900 (line)]] | alt | 6.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.26× (z +10.1) | — |
| [[A-427 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.807 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.801 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.893 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.904 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.895 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5522), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPA2]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_SPERMATOGENESIS |
| [[MAP1LC3B2]] | +0.56 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[TENT5C]] | +0.53 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[CD40]] | +0.53 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[UBB]] | +0.53 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[CSRP2]] | +0.53 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[PCDH10]] | +0.52 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[SNAI1]] | +0.51 | +0.37 / +0.57 | both halves | 9e-05 |  |
| [[SKP1]] | +0.51 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[MYLIP]] | +0.50 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[SLC41A1]] | +0.50 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[SDAD1P1]] | +0.50 | +0.43 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDCD3]] | -0.54 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[ACSF3]] | -0.50 | -0.25 / -0.51 | both halves | 4e-04 |  |
| [[TIMM23B]] | -0.49 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[TREX2]] | -0.49 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[ENTPD5]] | -0.47 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[ORC5]] | -0.46 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[ZSWIM9]] | -0.46 | -0.21 / -0.33 | both halves | 7e-04 |  |
| [[NUP93]] | -0.46 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[ATAD3B]] | -0.46 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[COG2]] | -0.45 | -0.16 / -0.40 | ⚠ not reproduced | 0.001 |  |
| [[EIF2B3]] | -0.45 | -0.22 / -0.35 | both halves | 6e-04 |  |
| [[DDX55]] | -0.45 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[E4F1]] | -0.45 | -0.47 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD40]] | B | CD40 activity raises GSTM3's level | lines that do not express CD40 (22) vs lines expressing it (28) | 2.06× lower at baseline in the lines without CD40 | 0.043 | ⚠ within organs, on part of the lines; also absent: ZNF528-AS1, TNFRSF9, TMEM156 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR9-1HG]] | B | GSTM3 activity strengthens MIR9-1HG's drug response | lines that do not express GSTM3 (14) vs lines expressing it (31) | the lines without GSTM3 respond 0.57× as strongly (z diff +1.37); strongest at Homoharringtonine 5 µM: 1.39x vs 2.96x (z diff +3.1) | 0.058 | ⚠ within organs, on part of the lines; also absent: ESYT3, CADM1, TGFB1I1; target measured in part of the lines; artifact flags |
| [[DDX51]] | B | GSTM3 activity raises DDX51's level | lines that do not express GSTM3 (14) vs lines expressing it (36) | 1.11× lower at baseline in the lines without GSTM3 | 0.073 | ⚠ within organs, on part of the lines; also absent: ESYT3, CADM1, TGFB1I1 |
| [[CD40]] | B | GSTM3 activity raises CD40's level | lines that do not express GSTM3 (14) vs lines expressing it (36) | 2.33× lower at baseline in the lines without GSTM3 | 0.090 | ⚠ within organs, on part of the lines; also absent: ESYT3, CADM1, TGFB1I1 |

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.570). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.9, -28.2); signed map (1.1, 18.0). **Vector** length 47.1, 8.49% of its response variance represented; |z| ≥ 3 in 545 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +15.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.2 | +3.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.0 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +6.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.2 | +0.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.2 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +6.1 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -1.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -1.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.0 | +0.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.9 | -0.6 |
|  | [[EX229 (drug)]] 5 µM |  | -0.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | glutathione S-transferase mu 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:109,733,932-109,741,038 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GST5, GSTM3TV2 |
| Gene groups (HGNC) | Soluble glutathione S-transferases |
| Hallmark sets | APICAL_SURFACE, SPERMATOGENESIS |
| Reactome | 3 pathways, smallest: Glutathione conjugation; Phase II - Conjugation of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [P21266](https://www.uniprot.org/uniprotkb/P21266) (Glutathione S-transferase Mu 3):

> Glutathione S-transferase that catalyzes the conjugation of reduced glutathione to electrophilic substrates, probably contributing to detoxification of endogenous and exogenous toxic compounds. In vitro, acts on 1-chloro-2,4-dinitrobenzene, ethacrynic acid, trans-alk-2-enals, trans-hex-2-enal, trans-oct-2-enal, trans-non-2-enal, 4-hydroxynonenal and 4-hydroxydecenal. A glutathione peroxidase activity toward H2O2 and cumene hydroperoxide has been reported, but was not confirmed in another study. …

**Summary**, from NCBI Gene [2947](https://www.ncbi.nlm.nih.gov/gene/2947):

> Cytosolic and membrane-bound forms of glutathione S-transferase are encoded by two distinct supergene families. At present, eight distinct classes of the soluble cytoplasmic mammalian glutathione S-transferases have been identified: alpha, kappa, mu, omega, pi, sigma, theta and zeta. This gene encodes a glutathione S-transferase that belongs to the mu class. The mu class of enzymes functions in the detoxification of electrophilic compounds, including carcinogens, therapeutic drugs, …

**Accessions** — [HGNC:4635](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4635) · Entrez [2947](https://www.ncbi.nlm.nih.gov/gene/2947) · UniProt [P21266](https://www.uniprot.org/uniprotkb/P21266) · Ensembl [ENSG00000134202](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134202)

## Data

Gene col 5522: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5522); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5522, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5522]; `tensor/DDL_lfc|DDL_z.npy` [5522]; `embed/gene_vectors.npy` [5522]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5522 or target_col == 5522). Every well: [[GSTM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSTM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
