---
symbol: "OLR1"
type: "gene"
col: 10377
ensembl_id: "ENSG00000173391"
name: "oxidized low density lipoprotein receptor 1"
location: "12p13.2"
module: 66
arm: "+"
pooled_cpm: 13.83
n_lines_expressing: 10
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# OLR1

*oxidized low density lipoprotein receptor 1* — 12p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.17× (z +9.8, q 4e-20, up in 6 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.63× (z +9.4, q 1e-18, up in 4 of 7 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Artesunate (drug)]] 0.5 µM: 0.580× (z -3.8, q 0.094, down in 1 of 8 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.256×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM52B]] (+0.82, fdr 7e-06, ⚠ same locus), [[TNFAIP6]] (+0.73, fdr 7e-06), [[AKR1B1]] (+0.69, fdr 7e-06), [[ROS1]] (+0.68, fdr 1e-05); moves opposite to [[WDR37]] (-0.53, fdr 3e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[TMEM52B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10377.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.17×** | +9.8 | 4e-20 | 6/6 (J82, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.63×** | +9.4 | 1e-18 | 4/7 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.18×** | +9.3 | 2e-18 | 3/5 (J82, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +8.0 | 3e-13 | 3/7 (HOP62, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.37×** | +7.7 | 2e-12 | 2/5 (J82, NCI-H23) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.87×** | +7.3 | 4e-11 | 5/8 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.45×** | +5.9 | 4e-07 | 4/7 (HOP62, J82, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.19×** | +5.4 | 4e-06 | 3/6 (HCT15, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.27×** | +5.4 | 5e-06 | 4/7 (NCI-H23, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.71×** | +5.2 | 9e-06 | 4/8 (HOP62, J82, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +5.0 | 2e-05 | 6/8 (J82, A-172, …) | rises with dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +4.2 | 0.001 | 1/8 (A549) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **2.18×** | +3.7 | 0.010 | 1/7 (A-427) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +3.7 | 0.010 | 1/6 (J82) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +3.6 | 0.012 | 2/8 (HOP62, J82) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.68×** | +3.6 | 0.012 | 5/8 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.021 | 6/8 (HOP62, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +3.4 | 0.022 | 5/8 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.61×** | +3.3 | 0.031 | 1/8 (A-172) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.97×** | +3.2 | 0.036 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +3.2 | 0.036 | 3/8 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.55×** | +3.0 | 0.063 | 0/8 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10377.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.256×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | **0.580×** | -3.8 | 0.094 | 1/8 (H4) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.640× | -3.1 | 0.58 | 4/8 (NCI-H23, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10377. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.38 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 3.68 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 54.1× (z +13.4) | — |
| [[J82 (line)]] | alt | 144 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 6.87× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 96.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -8.8) |
| [[A-427 (line)]] | wt | 305 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.719 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.794 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.773 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.868 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.808 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.877 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.857 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.723 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.703 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.826 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.693 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.644 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.768 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.739 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.760 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.747 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.785 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.766 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.899 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.816 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.828 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.32 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10377), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM52B]] | +0.82 | +0.80 / +0.80 | both halves | 7e-06 | STRING 614; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[TNFAIP6]] | +0.73 | +0.61 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[AKR1B1]] | +0.69 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[ROS1]] | +0.68 | +0.51 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[C1QTNF1-AS1]] | +0.68 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[LINC02605]] | +0.63 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[KCNT2]] | +0.63 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[VCAM1]] | +0.62 | +0.64 / +0.49 | both halves | 1e-05 | STRING 613 |
| [[KYNU]] | +0.62 | +0.45 / +0.56 | both halves | 3e-05 | pathway: HALLMARK_COMPLEMENT |
| [[MYPN]] | +0.62 | +0.49 / +0.59 | both halves | 2e-05 |  |
| [[DIO2]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[SEMA3C]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[EDIL3-DT]] | +0.59 | +0.39 / +0.55 | both halves | 5e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR37]] | -0.53 | -0.50 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers OLR1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TMEM52B]] | C | TMEM52B activity raises OLR1's level | lines that do not express TMEM52B (39) vs lines expressing it (11) | 6.80× lower at baseline in the lines without TMEM52B | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OLR1, HOXD11, ENSG00000230258; co-absent with the target |
| [[TRIM58]] | C | TRIM58 activity raises OLR1's level | lines that do not express TRIM58 (31) vs lines expressing it (19) | 2.62× lower at baseline in the lines without TRIM58 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000235749, MME, FGF20; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM52B]] | C | OLR1 activity raises TMEM52B's level | lines that do not express OLR1 (40) vs lines expressing it (10) | 3.94× lower at baseline in the lines without OLR1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM52B, ENSG00000230258, PSG9; co-absent with the target |
| [[TRIM58]] | C | OLR1 activity raises TRIM58's level | lines that do not express OLR1 (40) vs lines expressing it (10) | 2.03× lower at baseline in the lines without OLR1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM52B, ENSG00000230258, PSG9; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.7, 22.6); signed map (46.0, 21.3). **Vector** length 35.6, 13.3% of its response variance represented; |z| ≥ 3 in 230 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +9.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.1 | +3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +5.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.3 | +2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.3 | +3.4 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | +0.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -0.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.7 | -1.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | oxidized low density lipoprotein receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.2 — chr12:10,158,301-10,172,138 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LOX-1, SCARE1, CLEC8A |
| Gene groups (HGNC) | Scavenger receptors; C-type lectin domain containing; Dectin 1 cluster |
| Hallmark sets | ANGIOGENESIS, COAGULATION, INFLAMMATORY_RESPONSE, COMPLEMENT, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 4 pathways, smallest: Cell surface interactions at the vascular wall; Neutrophil degranulation; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [P78380](https://www.uniprot.org/uniprotkb/P78380) (Oxidized low-density lipoprotein receptor 1):

> Receptor that mediates the recognition, internalization and degradation of oxidatively modified low density lipoprotein (oxLDL) by vascular endothelial cells. OxLDL is a marker of atherosclerosis that induces vascular endothelial cell activation and dysfunction, resulting in pro-inflammatory responses, pro-oxidative conditions and apoptosis. Its association with oxLDL induces the activation of NF-kappa-B through an increased production of intracellular reactive oxygen and a variety of …

**Summary**, from NCBI Gene [4973](https://www.ncbi.nlm.nih.gov/gene/4973):

> This gene encodes a low density lipoprotein receptor that belongs to the C-type lectin superfamily. This gene is regulated through the cyclic AMP signaling pathway. The encoded protein binds, internalizes and degrades oxidized low-density lipoprotein. This protein may be involved in the regulation of Fas-induced apoptosis. This protein may play a role as a scavenger receptor. Mutations of this gene have been associated with atherosclerosis, risk of myocardial infarction, and may modify the risk …

**Accessions** — [HGNC:8133](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8133) · Entrez [4973](https://www.ncbi.nlm.nih.gov/gene/4973) · UniProt [P78380](https://www.uniprot.org/uniprotkb/P78380) · Ensembl [ENSG00000173391](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173391)

## Data

Gene col 10377: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10377); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10377, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10377]; `tensor/DDL_lfc|DDL_z.npy` [10377]; `embed/gene_vectors.npy` [10377]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10377 or target_col == 10377). Every well: [[OLR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OLR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
