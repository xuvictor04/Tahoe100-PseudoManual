---
symbol: "INHBB"
type: "gene"
col: 8630
ensembl_id: "ENSG00000163083"
name: "inhibin subunit beta B"
location: "2q14.2"
module: 100
arm: "+"
pooled_cpm: 11.56
n_lines_expressing: 19
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# INHBB

*inhibin subunit beta B* — 2q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.74× (z +12.5, q 2e-33, up in 12 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.59× (z +9.7, q 9e-20, up in 9 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (NCI-H2030 0.0816×, Hs 766T 0.0455×, SW480 0.226×, A498 0.218×, …); [[Panobinostat (drug)]] 0.5 µM in 3 lines (BT-474 0.0660×, SW480 0.180×, SW1417 0.174×; ⚠ cell-cycle shift, explains ~25% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (SW480 0.112×, SW1417 0.183×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.0799×).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CACNG4]] (+0.56, fdr 1e-05), [[LINC00842]] (+0.49, fdr 4e-05), [[PPP1R14A]] (+0.46, fdr 1e-04); moves opposite to [[ZNF558]] (-0.39, fdr 2e-04), [[ZNF222]] (-0.38, fdr 2e-04), [[MCL1]] (-0.36, fdr 3e-04).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ENTREP2]] → it (grade C ⚠); 1 goes from it, the strongest it → [[LINC00842]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8630.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.74×** | +12.5 | 2e-33 | 12/13 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.89×** | +12.1 | 5e-31 | 11/12 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.59×** | +9.7 | 9e-20 | 9/15 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.66×** | +8.6 | 1e-15 | 10/12 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +5.5 | 4e-06 | 6/17 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.28×** | +5.2 | 2e-05 | 7/14 (SW480, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +3.7 | 0.015 | 8/15 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +3.4 | 0.041 | 4/17 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.59×** | +3.3 | 0.058 | 5/16 (NCI-H1573, SW480, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.58×** | +3.3 | 0.061 | 4/14 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 2.24× | +3.0 | 0.13 | 7/16 (PANC-1, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8630.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (NCI-H2030 0.0816×, Hs 766T 0.0455×, SW480 0.226×, A498 0.218×, …); [[Panobinostat (drug)]] 0.5 µM in 3 lines (BT-474 0.0660×, SW480 0.180×, SW1417 0.174×; ⚠ cell-cycle shift, explains ~25% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (SW480 0.112×, SW1417 0.183×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.0799×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.620× | -3.4 | 0.16 | 10/16 (HOP62, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | 0.582× | -3.4 | 0.16 | 10/16 (NCI-H2030, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | 0.418× | -3.3 | 0.16 | 6/15 (Hs 766T, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | 0.420× | -3.3 | 0.16 | 3/16 (Hs 766T, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.436× | -3.1 | 0.18 | 1/16 (Hs 766T) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.739× | -3.1 | 0.18 | 14/15 (NCI-H2030, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.654× | -3.1 | 0.18 | 1/17 (SW1417) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8630. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 58.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.71× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -13.1) |
| [[SW480 (line)]] | alt | 65.2 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -16.0) |
| [[SW1417 (line)]] | alt | 35.0 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.174× (z -10.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.183× (z -10.0) |
| [[BT-474 (line)]] | alt | 52.8 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0660× (z -14.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.196× (z -11.9) |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0455× (z -16.3) |
| [[NCI-H2030 (line)]] | alt | 35.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0816× (z -18.8) |
| [[A549 (line)]] | wt | 5.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.1× (z +15.6) | — |
| [[HOP62 (line)]] | alt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -11.3) |
| [[SNU-423 (line)]] | alt | 11.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.2× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.855 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.983 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.918 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.998 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.899 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.831 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.515 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.697 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.692 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.859 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.841 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.837 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8630), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACNG4]] | +0.56 | +0.59 / +0.49 | both halves | 1e-05 | **novel candidate** |
| [[LINC00842]] | +0.49 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[PPP1R14A]] | +0.46 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[COBL]] | +0.45 | +0.36 / +0.35 | both halves | 1e-04 |  |
| [[LMO3]] | +0.45 | +0.30 / +0.38 | both halves | 2e-04 |  |
| [[EPB41L4A]] | +0.43 | +0.40 / +0.33 | both halves | 1e-04 |  |
| [[HOPX]] | +0.41 | +0.26 / +0.35 | both halves | 4e-04 |  |
| [[SLC7A6]] | +0.40 | +0.35 / +0.33 | both halves | 1e-04 |  |
| [[ATAD3C]] | +0.39 | +0.37 / +0.27 | both halves | 3e-04 |  |
| [[EFHD1]] | +0.39 | +0.25 / +0.42 | both halves | 4e-04 |  |
| [[ATP6V0E2]] | +0.39 | +0.38 / +0.47 | both halves | 7e-05 |  |
| [[PSG1]] | +0.38 | +0.32 / +0.36 | both halves | 2e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF558]] | -0.39 | -0.30 / -0.36 | both halves | 2e-04 |  |
| [[ZNF222]] | -0.38 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[MCL1]] | -0.36 | -0.32 / -0.28 | both halves | 3e-04 |  |
| [[ZNF160]] | -0.35 | -0.35 / -0.22 | both halves | 6e-04 |  |
| [[HLA-K]] | -0.35 | -0.41 / -0.29 | both halves | 2e-04 |  |
| [[IL1RL1]] | -0.35 | -0.33 / -0.22 | both halves | 6e-04 |  |
| [[HIF1AN]] | -0.35 | -0.34 / -0.26 | both halves | 4e-04 |  |
| [[NPAS2]] | -0.34 | -0.33 / -0.21 | both halves | 6e-04 |  |
| [[MIR30DHG]] | -0.34 | -0.27 / -0.38 | both halves | 3e-04 |  |
| [[KYAT3]] | -0.34 | -0.36 / -0.32 | both halves | 2e-04 |  |
| [[SQOR]] | -0.34 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[TANK]] | -0.34 | -0.26 / -0.30 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENTREP2]] | C | ENTREP2 activity raises INHBB's level | lines that do not express ENTREP2 (22) vs lines expressing it (28) | 2.02× lower at baseline in the lines without ENTREP2 | 0.029 | ⚠ within organs, on part of the lines; also absent: TBX1, JPH3, MAPK4; maybe low, not absent; co-absent with the target |
| [[PSG1]] | C | PSG1 activity raises INHBB's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 2.70× lower at baseline in the lines without PSG1 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00842]] | C | INHBB activity raises LINC00842's level | lines that do not express INHBB (31) vs lines expressing it (19) | 1.59× lower at baseline in the lines without INHBB | 0.097 | ⚠ within organs, on part of the lines; also absent: CYP24A1, GSDMC, S100A9; co-absent with the target |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.261). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.2, 43.6); signed map (52.0, 17.0). **Vector** length 41.5, 11.2% of its response variance represented; |z| ≥ 3 in 350 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +9.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.3 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +2.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.6 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +2.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.0 | -3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -3.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -3.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -3.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | inhibin subunit beta B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.2 — chr2:120,346,136-120,351,803 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Inhibin subunits |
| Hallmark sets | ALLOGRAFT_REJECTION, ESTROGEN_RESPONSE_EARLY, P53_PATHWAY |
| Reactome | 6 pathways, smallest: Antagonism of Activin by Follistatin; Glycoprotein hormones; Peptide hormone biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P09529](https://www.uniprot.org/uniprotkb/P09529) (Inhibin beta B chain):

> Inhibins and activins inhibit and activate, respectively, the secretion of follitropin by the pituitary gland. Inhibins/activins are involved in regulating a number of diverse functions such as hypothalamic and pituitary hormone secretion, gonadal hormone secretion, germ cell development and maturation, erythroid differentiation, insulin secretion, nerve cell survival, embryonic axial development or bone growth, depending on their subunit composition. Inhibins appear to oppose the functions of …

**Summary**, from NCBI Gene [3625](https://www.ncbi.nlm.nih.gov/gene/3625):

> This gene encodes a member of the TGF-beta (transforming growth factor-beta) superfamily of proteins. The encoded preproprotein is proteolytically processed to generate a subunit of the dimeric activin and inhibin protein complexes. These complexes activate and inhibit, respectively, follicle stimulating hormone secretion from the pituitary gland. Polymorphisms near this gene are associated with pre-eclampsia in female human patients. [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:6067](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6067) · Entrez [3625](https://www.ncbi.nlm.nih.gov/gene/3625) · UniProt [P09529](https://www.uniprot.org/uniprotkb/P09529) · Ensembl [ENSG00000163083](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163083)

## Data

Gene col 8630: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8630); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8630, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8630]; `tensor/DDL_lfc|DDL_z.npy` [8630]; `embed/gene_vectors.npy` [8630]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8630 or target_col == 8630). Every well: [[INHBB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INHBB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
