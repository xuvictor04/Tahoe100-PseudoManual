---
symbol: "GHRLOS"
type: "gene"
col: 14229
ensembl_id: "ENSG00000240288"
name: "ghrelin opposite strand/antisense RNA"
location: "3p25.3"
module: 47
arm: "+"
pooled_cpm: 4.54
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 8
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# GHRLOS

*ghrelin opposite strand/antisense RNA* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Filgotinib (drug)]] 5 µM: 1.57× (z +4.3, q 0.010, up in 12 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.381× (z -9.1, q 5e-17, down in 34 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2347 0.141×, SK-MEL-2 0.167×, PANC-1 0.319×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.0818×, HOP62 0.0581×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.157×, HOP62 0.143×); [[Ritonavir (drug)]] 0.5 µM in 1 line (A549 0.0635×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIMM23B-AGAP6]] (+0.63, fdr 1e-05), [[NPIPB11]] (+0.63, fdr 1e-05), [[SMG1P6]] (+0.63, fdr 3e-05); moves opposite to [[RAB30]] (-0.60, fdr 7e-05), [[SNX2]] (-0.60, fdr 1e-05), [[RCOR3]] (-0.60, fdr 1e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FAM20C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14229.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | **1.57×** | +4.3 | 0.010 | 12/46 (A549, NCI-H1792, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +3.5 | 0.094 | 3/9 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.5 | 0.094 | 8/47 (LOX-IMVI, A-172, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.25× | +3.0 | 0.35 | 13/40 (LoVo, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14229.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2347 0.141×, SK-MEL-2 0.167×, PANC-1 0.319×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.0818×, HOP62 0.0581×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.157×, HOP62 0.143×); [[Ritonavir (drug)]] 0.5 µM in 1 line (A549 0.0635×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.381×** | -9.1 | 5e-17 | 34/46 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.407×** | -8.5 | 5e-15 | 24/33 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.326×** | -8.5 | 5e-15 | 28/44 (MIA PaCa-2, A549, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.446×** | -6.1 | 2e-07 | 18/30 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.532×** | -5.6 | 2e-06 | 21/45 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.552×** | -5.6 | 2e-06 | 20/43 (A-427, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.693×** | -4.9 | 8e-05 | 17/39 (NCI-H2347, SK-MEL-2, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.694×** | -3.4 | 0.041 | 19/46 (HOP62, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14229. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 6.52 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0581× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.143× (z -8.7) |
| [[PANC-1 (line)]] | alt | 6.06 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0818× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.157× (z -9.7) |
| [[C32 (line)]] | wt | 6.22 | 0 | 2 (2 ⚠) | — | [[Plicamycin (drug)]] 5 µM 0.0732× (z -10.1) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 7.34 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.101× (z -9.9) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 4.66 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0635× (z -8.9) |
| [[H4 (line)]] | wt | 6.74 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.0332× (z -10.2) ⚠ cell-cycle shift, explains ~51% of this change |
| [[MIA PaCa-2 (line)]] | alt | 7.82 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0697× (z -9.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H2030 (line)]] | alt | 4.69 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0699× (z -9.2) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H2347 (line)]] | alt | 3.03 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 6.18 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.990 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14229), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM23B-AGAP6]] | +0.63 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[NPIPB11]] | +0.63 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[SMG1P6]] | +0.63 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[BRD9]] | +0.62 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[MYH3]] | +0.62 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[MSANTD1]] | +0.61 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[QRICH2]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[EFCAB8]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[CHADL]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[PARVG]] | +0.60 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[BLZF2P]] | +0.60 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[CYP2D7]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB30]] | -0.60 | -0.38 / -0.64 | both halves | 7e-05 |  |
| [[SNX2]] | -0.60 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[RCOR3]] | -0.60 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[KBTBD3]] | -0.58 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[LCA5]] | -0.58 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[PTPN13]] | -0.56 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[PHF21A]] | -0.56 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[ATP5PO]] ⚠ | -0.55 | -0.34 / -0.54 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[DPM3]] | -0.55 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[PREPL]] | -0.54 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[PEX2]] | -0.54 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[CXADR]] | -0.54 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[SLC25A27]] | -0.52 | -0.55 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM20C]] | B | FAM20C activity raises GHRLOS's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 1.44× lower at baseline in the lines without FAM20C | 0.090 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.563). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.0, -14.4); signed map (15.3, 3.0). **Vector** length 50.1, 6.02% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.0 | +1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +0.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +1.7 | +3.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.6 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.2 | +1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +4.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.0 | +0.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.0 | -8.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | +0.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | ghrelin opposite strand/antisense RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p25.3 — chr3:10,285,754-10,294,903 (+) |
| Ensembl biotype | lncRNA |
| Also known as | NCRNA00068, GHRL-AS1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100126793](https://www.ncbi.nlm.nih.gov/gene/100126793):

> This gene is an antisense gene of the ghrelin/obestatin prepropeptide gene. Alternatively spliced transcript variants have been identified and they may function as non-coding regulatory RNAs. [provided by RefSeq, Jan 2013]

**Accessions** — [HGNC:33885](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33885) · Entrez [100126793](https://www.ncbi.nlm.nih.gov/gene/100126793) · Ensembl [ENSG00000240288](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240288)

## Data

Gene col 14229: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14229); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14229, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14229]; `tensor/DDL_lfc|DDL_z.npy` [14229]; `embed/gene_vectors.npy` [14229]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14229 or target_col == 14229). Every well: [[GHRLOS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GHRLOS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
