---
symbol: "TCIM"
type: "gene"
col: 10764
ensembl_id: "ENSG00000176907"
name: "transcriptional and immune response regulator"
location: "8p11.21"
module: 167
arm: "+"
pooled_cpm: 28.22
n_lines_expressing: 25
n_dd_up: 8
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/167"]
generated_by: "tahoemap"
---

# TCIM

*transcriptional and immune response regulator* — 8p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.39× (z +7.7, q 7e-12, up in 6 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.50× (z +5.1, q 1e-04, up in 12 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AsPC-1 9.51×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.453× (z -6.9, q 3e-09, down in 20 of 23 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02015]] (+0.73, fdr 7e-06), [[FLRT3]] (+0.65, fdr 7e-06), [[RHCG]] (+0.65, fdr 1e-05).
> It is in [[Module 167]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TNFRSF21]] → it (grade B ⚠); 2 go from it, the strongest it → [[EXT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10764.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AsPC-1 9.51×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.39×** | +7.7 | 7e-12 | 6/24 (J82, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +5.1 | 1e-04 | 12/23 (RPMI-7951, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +4.5 | 0.001 | 5/19 (J82, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +4.4 | 0.001 | 2/20 (J82, Hs 766T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.4 | 0.001 | 6/21 (BT-474, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.87×** | +3.4 | 0.054 | 9/22 (NCI-H2347, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.44×** | +3.3 | 0.084 | 0/22 | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.43×** | +3.2 | 0.095 | 0/21 | inconsistent across doses | low cells (technical?) |
| [[Lactate (calcium) (drug)]] 5 µM |  | 1.40× | +3.0 | 0.15 | 0/23 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10764.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.453×** | -6.9 | 3e-09 | 20/23 (SW 900, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.556×** | -5.1 | 9e-05 | 20/23 (A549, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.575×** | -4.8 | 3e-04 | 21/23 (SW 900, A549, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.585×** | -4.7 | 4e-04 | 18/23 (BT-474, SW 900, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.596×** | -4.5 | 7e-04 | 16/23 (NCI-H2030, SNU-423, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.718×** | -4.0 | 0.005 | 17/24 (SW 900, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.646×** | -3.8 | 0.012 | 20/23 (A549, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.486×** | -3.3 | 0.080 | 15/22 (BT-474, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.769×** | -3.2 | 0.087 | 14/23 (SHP-77, LS 180, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.698× | -3.1 | 0.11 | 10/23 (Panc 03.27, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10764. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 40.7 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0520× (z -17.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0225× (z -15.9) |
| [[NCI-H23 (line)]] | alt | 132 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0715× (z -18.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0795× (z -12.6) |
| [[A549 (line)]] | wt | 235 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0824× (z -20.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0693× (z -15.3) |
| [[HepG2_C3A (line)]] | wt | 177 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -13.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.140× (z -10.8) |
| [[SW 900 (line)]] | alt | 141 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -14.0) |
| [[SHP-77 (line)]] | alt | 51.0 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -10.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.126× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 144 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0768× (z -24.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 18.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0789× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.125× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 73.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -9.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.208× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 39.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 9.51× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HS-578T (line)]] | alt | 7.18 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0279× (z -12.4) |
| [[LS 180 (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 16.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0719× (z -10.6) |
| [[A-172 (line)]] | wt | 4.28 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.89 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.77 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.71 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.88 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.31 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.57 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.11 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.35 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.70 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10764), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02015]] | +0.73 | +0.68 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[FLRT3]] | +0.65 | +0.62 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[RHCG]] | +0.65 | +0.52 / +0.68 | both halves | 1e-05 | **novel candidate** |
| [[AHR]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[KYNU]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[RORB]] | +0.62 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[IL6]] | +0.62 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[SERPINB4]] | +0.61 | +0.62 / +0.57 | both halves | 8e-06 |  |
| [[TNIP3]] | +0.60 | +0.36 / +0.66 | both halves | 1e-04 |  |
| [[CYP1B1]] | +0.60 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[C2CD4A]] | +0.60 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[EPAS1]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF21]] | B | TNFRSF21 activity raises TCIM's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 3.02× lower at baseline in the lines without TNFRSF21 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[LINC01348]] | B | LINC01348 activity raises TCIM's level | lines that do not express LINC01348 (10) vs lines expressing it (40) | 2.85× lower at baseline in the lines without LINC01348 | 0.044 | ⚠ within organs, on part of the lines; also absent: ARHGAP42, RIPK4, ABCC3; maybe low, not absent |
| [[AQP3]] | B | AQP3 activity raises TCIM's level | lines that do not express AQP3 (19) vs lines expressing it (31) | 2.09× lower at baseline in the lines without AQP3 | 0.064 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[EREG]] | B | EREG activity raises TCIM's level | lines that do not express EREG (26) vs lines expressing it (24) | 1.47× lower at baseline in the lines without EREG | 0.083 | ⚠ within organs, on part of the lines; also absent: DPP4, IL20RA, HS3ST1 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EXT1]] | B | TCIM activity raises EXT1's level | lines that do not express TCIM (25) vs lines expressing it (25) | 1.60× lower at baseline in the lines without TCIM | 0.083 | ⚠ within organs, on part of the lines; also absent: LUM, ZNF626, ADAM28 |
| [[AQP3]] | B | TCIM activity raises AQP3's level | lines that do not express TCIM (25) vs lines expressing it (25) | 1.63× lower at baseline in the lines without TCIM | 0.088 | ⚠ within organs, on part of the lines; also absent: LUM, ZNF626, ADAM28 |

## Where it sits

- **Module**: [[Module 167]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.748). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.7, 22.0); signed map (50.9, 23.7). **Vector** length 76.8, 22.3% of its response variance represented; |z| ≥ 3 in 685 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | -0.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +1.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +1.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +3.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.8 | +1.1 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -3.1 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -4.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | transcriptional and immune response regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.21 — chr8:40,153,482-40,155,310 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TC-1, hTC-1, TC1; previously C8orf4 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NR00](https://www.uniprot.org/uniprotkb/Q9NR00) (Transcriptional and immune response regulator):

> Seems to be involved in the regulation of cell growth an differentiation, may play different and opposite roles depending on the tissue or cell type. May enhance the WNT-CTNNB1 pathway by relieving antagonistic activity of CBY1. Enhances the proliferation of follicular dendritic cells. Plays a role in the mitogen-activated MAPK2/3 signaling pathway, positively regulates G1-to-S-phase transition of the cell cycle. In endothelial cells, enhances key inflammatory mediators and inflammatory …

**Summary**, from NCBI Gene [56892](https://www.ncbi.nlm.nih.gov/gene/56892):

> This gene encodes a small, monomeric, predominantly unstructured protein that functions as a positive regulator of the Wnt/beta-catenin signaling pathway. This protein interacts with a repressor of beta-catenin mediated transcription at nuclear speckles. It is thought to competitively block interactions of the repressor with beta-catenin, resulting in up-regulation of beta-catenin target genes. The encoded protein may also play a role in the NF-kappaB and ERK1/2 signaling pathways. Expression …

**Accessions** — [HGNC:1357](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1357) · Entrez [56892](https://www.ncbi.nlm.nih.gov/gene/56892) · UniProt [Q9NR00](https://www.uniprot.org/uniprotkb/Q9NR00) · Ensembl [ENSG00000176907](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176907)

## Data

Gene col 10764: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10764); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10764, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10764]; `tensor/DDL_lfc|DDL_z.npy` [10764]; `embed/gene_vectors.npy` [10764]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10764 or target_col == 10764). Every well: [[TCIM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCIM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
