---
symbol: "FRMD6-AS2"
type: "gene"
col: 15111
ensembl_id: "ENSG00000258537"
name: "FRMD6 antisense RNA 2"
location: "14q22.1"
module: 80
arm: "+"
pooled_cpm: 13.68
n_lines_expressing: 47
n_dd_up: 21
n_dd_down: 6
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# FRMD6-AS2

*FRMD6 antisense RNA 2* — 14q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.99× (z +22.0, q 0e+00, up in 38 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.641× (z -6.3, q 2e-07, down in 21 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC8C-DT]] (+0.67, fdr 1e-05), [[SLC9B1]] (+0.66, fdr 8e-06), [[LINC00513]] (+0.66, fdr 7e-06); moves opposite to [[TTLL5]] (-0.63, fdr 1e-05), [[SPIDR]] (-0.57, fdr 4e-05), [[SMCHD1]] (-0.53, fdr 7e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FRMD6]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Lonafarnib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15111.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.99×** | +22.0 | 0e+00 | 38/42 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.65×** | +10.0 | 4e-21 | 25/42 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.58×** | +9.2 | 4e-18 | 25/45 (HS-578T, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +8.3 | 1e-14 | 27/44 (Panc 03.27, SW 900, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.73×** | +7.2 | 6e-11 | 16/28 (C32, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.62×** | +6.8 | 9e-10 | 25/44 (SK-MEL-2, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +5.8 | 5e-07 | 22/41 (A-172, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +5.8 | 6e-07 | 18/45 (SW480, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +5.1 | 2e-05 | 16/44 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.42×** | +5.0 | 3e-05 | 18/44 (Panc 03.27, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.9 | 4e-05 | 18/39 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.9 | 5e-05 | 19/45 (HOP62, HS-578T, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.40×** | +4.7 | 9e-05 | 12/45 (LOX-IMVI, BT-474, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +4.4 | 4e-04 | 15/45 (H4, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +4.3 | 6e-04 | 15/45 (RKO, A498, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.013 | 13/43 (HS-578T, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.58×** | +3.4 | 0.024 | 6/39 (HS-578T, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.024 | 7/45 (J82, C32, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.080 | 9/44 (SK-MEL-2, NCI-H460, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +2.9 | 0.097 | 12/44 (H4, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15111.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.641×** | -6.3 | 2e-07 | 21/44 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.723×** | -4.6 | 0.001 | 14/44 (PANC-1, H4, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.723×** | -4.4 | 0.002 | 18/38 (NCI-H23, PANC-1, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.743×** | -4.2 | 0.004 | 19/45 (PANC-1, A549, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.760×** | -3.9 | 0.011 | 11/45 (J82, RKO, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.920× | -3.8 | 0.013 | 5/45 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.634×** | -3.4 | 0.059 | 12/41 (Hs 766T, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | 0.799× | -3.2 | 0.11 | 11/44 (SW 1271, SNU-423, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 0.5 µM |  | 0.805× | -3.1 | 0.13 | 7/44 (RPMI-7951, SNU-423, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.807× | -3.0 | 0.13 | 11/45 (SW 1088, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15111. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 23.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 21.4 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.226× (z -9.8) |
| [[HOP62 (line)]] | alt | 17.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.16× (z +13.1) | — |
| [[HS-578T (line)]] | alt | 15.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 40.7 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -11.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.281× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 13.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +9.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.119× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[RKO (line)]] | wt | 41.6 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -10.8) |
| [[SHP-77 (line)]] | alt | 8.45 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +8.6) | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.130× (z -8.5) |
| [[A-172 (line)]] | wt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +11.6) | — |
| [[A498 (line)]] | wt | 5.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.54× (z +12.9) | — |
| [[BT-474 (line)]] | alt | 14.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +8.9) | — |
| [[C-33 A (line)]] | alt | 9.49 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0761× (z -9.0) |
| [[C32 (line)]] | wt | 13.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 17.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +9.1) | — |
| [[H4 (line)]] | wt | 15.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.78× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 5.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0750× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 14.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +11.3) | — |
| [[NCI-H460 (line)]] | wt | 16.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +12.1) | — |
| [[RPMI-7951 (line)]] | alt | 14.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 18.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 8.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.45× (z +11.5) | — |
| [[SW480 (line)]] | alt | 6.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +9.8) | — |
| [[A-427 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.69 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15111), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC8C-DT]] | +0.67 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[SLC9B1]] | +0.66 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[LINC00513]] | +0.66 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[BCL10-AS1]] | +0.65 | +0.53 / +0.54 | both halves | 1e-05 | same gene group |
| [[CDK6-AS1]] | +0.64 | +0.58 / +0.49 | both halves | 1e-05 | same gene group |
| [[HSDL2-AS1]] | +0.64 | +0.60 / +0.43 | both halves | 3e-05 | same gene group |
| [[OOEP]] | +0.64 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[GSK3B-DT]] | +0.63 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[RGS20]] | +0.62 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[BHLHE40-AS1]] | +0.62 | +0.56 / +0.41 | both halves | 4e-05 | same gene group |
| [[MMRN2]] | +0.61 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[LTO1]] | +0.61 | +0.56 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTLL5]] | -0.63 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[SPIDR]] | -0.57 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[SMCHD1]] | -0.53 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[RALGAPA2]] | -0.53 | -0.38 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMD6]] | B | FRMD6 activity raises FRMD6-AS2's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 2.78× lower at baseline in the lines without FRMD6 | 4e-04 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers FRMD6-AS2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC16A2]] | B | SLC16A2 activity raises FRMD6-AS2's level | lines that do not express SLC16A2 (14) vs lines expressing it (36) | 2.13× lower at baseline in the lines without SLC16A2 | 0.034 | ⚠ within organs, on part of the lines; also absent: SLC2A3, LOXL2, ENSG00000234405 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Lonafarnib (drug)]] 5 µM | C | [[DENND5A]], FRMD6-AS2, [[SPIRE1]] activity raises the cells' numbers under Lonafarnib 5 µM (protects the cells) | lines that do not express DENND5A, FRMD6-AS2, SPIRE1 (3) vs lines expressing them (45) | the lines without DENND5A, FRMD6-AS2, SPIRE1: 0.11× the cells of the other lines | 0.027 | ⚠ few lines (3 vs 47); across organs; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23; co-absent genes |
| [[FRMD6]] | C | FRMD6-AS2 activity raises FRMD6's level | lines that do not express FRMD6-AS2 (3) vs lines expressing it (47) | 8.69× lower at baseline in the lines without FRMD6-AS2 | 0.032 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23 |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.628). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.4, 12.4); signed map (28.0, 0.2). **Vector** length 95.7, 20.8% of its response variance represented; |z| ≥ 3 in 915 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +22.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.2 | +8.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +6.7 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.5 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +5.8 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | -3.0 | -4.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.9 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -4.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | -1.6 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | FRMD6 antisense RNA 2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q22.1 — chr14:51,379,509-51,651,744 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43637](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43637) · Entrez [100874185](https://www.ncbi.nlm.nih.gov/gene/100874185) · Ensembl [ENSG00000258537](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258537)

## Data

Gene col 15111: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15111); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15111, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15111]; `tensor/DDL_lfc|DDL_z.npy` [15111]; `embed/gene_vectors.npy` [15111]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15111 or target_col == 15111). Every well: [[FRMD6-AS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRMD6-AS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
