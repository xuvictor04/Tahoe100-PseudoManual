---
symbol: "EGFL8"
type: "gene"
col: 14275
ensembl_id: "ENSG00000241404"
name: "EGF like domain multiple 8"
location: "6p21.32"
module: 25
arm: "-"
pooled_cpm: 4.89
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 11
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# EGFL8

*EGF like domain multiple 8* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.24× (z +6.5, q 5e-08, up in 22 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 2.50× (z +5.0, q 2e-04, up in 14 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.400× (z -8.4, q 2e-14, down in 27 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COG7]] (+0.70, fdr 7e-06), [[ZNF500]] (+0.66, fdr 2e-05), [[BSDC1]] (+0.66, fdr 7e-06); moves opposite to [[AKAP11]] (-0.72, fdr 7e-06), [[TWF1]] (-0.62, fdr 1e-05), [[GMFB]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[YPEL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14275.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.24×** | +6.5 | 5e-08 | 22/48 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.50×** | +5.0 | 2e-04 | 14/33 (PANC-1, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.20×** | +4.3 | 0.004 | 9/26 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +4.2 | 0.004 | 8/30 (CFPAC-1, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.87×** | +3.4 | 0.080 | 5/41 (SW480, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +3.3 | 0.092 | 5/22 (HEC-1-A, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.82×** | +3.2 | 0.096 | 5/37 (HOP62, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.56×** | +3.2 | 0.096 | 4/33 (J82, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +3.2 | 0.096 | 2/15 (PANC-1, NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 1.78× | +3.1 | 0.10 | 3/41 (NCI-H2347, NCI-H460, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14275.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.400×** | -8.4 | 2e-14 | 27/38 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.578×** | -7.1 | 3e-10 | 22/40 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.555×** | -5.4 | 1e-05 | 25/47 (NCI-H23, KATO III, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.563×** | -5.3 | 2e-05 | 20/46 (AsPC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.328×** | -5.0 | 6e-05 | 24/45 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.584×** | -5.0 | 7e-05 | 20/47 (H4, CFPAC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.601×** | -4.7 | 2e-04 | 15/47 (NCI-H23, A498, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.614×** | -4.3 | 0.001 | 22/45 (NCI-H1792, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.635×** | -4.2 | 0.002 | 16/47 (LoVo, SW480, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.639×** | -4.1 | 0.002 | 19/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.696×** | -3.4 | 0.041 | 11/44 (SW 900, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.721× | -3.0 | 0.11 | 16/47 (LOX-IMVI, SW48, …) | top dose only | cell-cycle shift (explains ~19% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14275. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 4.99 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0647× (z -9.7) |
| [[HCT15 (line)]] | alt | 5.22 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -8.7) |
| [[LoVo (line)]] | wt | 6.63 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -10.5) |
| [[LS 180 (line)]] | wt | 4.88 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0790× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~59% of this change |
| [[NCI-H2030 (line)]] | alt | 8.69 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -10.3) |
| [[PANC-1 (line)]] | alt | 6.00 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -10.1) |
| [[A-172 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14275), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG7]] | +0.70 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[ZNF500]] | +0.66 | +0.49 / +0.73 | both halves | 2e-05 |  |
| [[BSDC1]] | +0.66 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[UBE4B]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[PTOV1]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[ABCD4]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[DDRGK1]] | +0.62 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[MED31]] | +0.61 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[PPOX]] | +0.61 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[SEMA6C]] | +0.61 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[ENKD1]] | +0.61 | +0.38 / +0.71 | both halves | 7e-05 |  |
| [[GDPD3]] | +0.61 | +0.53 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP11]] | -0.72 | -0.61 / -0.77 | both halves | 7e-06 |  |
| [[TWF1]] | -0.62 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[GMFB]] | -0.60 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[IL6ST]] | -0.60 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[TMEM185B]] | -0.59 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[YWHAE]] | -0.59 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[EIF4G1]] | -0.59 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[EIF2S1]] | -0.59 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[MAPRE1]] | -0.58 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[BBS10]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[TTPAL]] | -0.57 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[LIN7C]] | -0.57 | -0.53 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YPEL3]] | B | YPEL3 activity lowers EGFL8's level | lines that do not express YPEL3 (7) vs lines expressing it (43) | 1.47× higher at baseline in the lines without YPEL3 | 0.068 | ⚠ within organs, on part of the lines; also absent: IKBKE, LTBR, RAB20 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises EGFL8's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises EGFL8's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.479). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-3.4, -18.8); signed map (-26.3, 6.1). **Vector** length 55.8, 8.27% of its response variance represented; |z| ≥ 3 in 740 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | +3.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +5.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +1.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.5 | +2.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +3.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.4 | +3.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.3 | -0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.3 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | EGF like domain multiple 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:32,164,595-32,168,281 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NG3; previously C6orf8 |
| Matched by | ensembl_id |

UniProt [Q99944](https://www.uniprot.org/uniprotkb/Q99944) carries no function annotation.

**Summary**, from NCBI Gene [80864](https://www.ncbi.nlm.nih.gov/gene/80864):

> Predicted to enable signaling receptor binding activity. Predicted to be involved in vasculogenesis. Predicted to be active in cell surface and extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13944](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13944) · Entrez [80864](https://www.ncbi.nlm.nih.gov/gene/80864) · UniProt [Q99944](https://www.uniprot.org/uniprotkb/Q99944) · Ensembl [ENSG00000241404](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241404)

## Data

Gene col 14275: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14275); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14275, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14275]; `tensor/DDL_lfc|DDL_z.npy` [14275]; `embed/gene_vectors.npy` [14275]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14275 or target_col == 14275). Every well: [[EGFL8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EGFL8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
