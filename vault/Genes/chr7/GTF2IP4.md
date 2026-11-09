---
symbol: "GTF2IP4"
type: "gene"
col: 13899
ensembl_id: "ENSG00000233369"
name: "general transcription factor IIi pseudogene 4"
location: "7q11.23"
module: 204
arm: "+"
pooled_cpm: 3.67
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 13
n_dd_up_clean: 16
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/204"]
generated_by: "tahoemap"
---

# GTF2IP4

*general transcription factor IIi pseudogene 4* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.47× (z +10.6, q 2e-23, up in 34 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.500× (z -8.0, q 5e-13, down in 23 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CASTOR2]] (+0.73, fdr 7e-06), [[PLEKHH3]] (+0.67, fdr 1e-05), [[LAPTM4A]] (+0.66, fdr 1e-05); moves opposite to [[NIP7]] (-0.67, fdr 7e-06), [[TRMT5]] (-0.65, fdr 7e-06), [[EMG1]] (-0.65, fdr 1e-05).
> It is in [[Module 204]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TSPAN33]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13899.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.47×** | +10.6 | 2e-23 | 34/44 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +9.9 | 2e-20 | 3/7 (HepG2/C3A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.29×** | +9.7 | 7e-20 | 35/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.17×** | +9.1 | 2e-17 | 29/44 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.04×** | +8.3 | 9e-15 | 29/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.4 | 2e-11 | 15/34 (BT-474, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +7.3 | 2e-11 | 18/44 (SW480, SNU-423, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.83×** | +7.0 | 1e-10 | 15/34 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.63×** | +5.7 | 7e-07 | 8/46 (PANC-1, HT-29, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.22×** | +4.9 | 6e-05 | 2/37 (SW480, LoVo) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.51×** | +4.9 | 6e-05 | 8/33 (PANC-1, HS-578T, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.43×** | +4.2 | 0.001 | 5/47 (LoVo, PANC-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +4.2 | 0.001 | 7/37 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +3.8 | 0.006 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.36×** | +3.7 | 0.010 | 5/26 (HepG2/C3A, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.020 | 8/40 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.036 | 2/42 (LOX-IMVI, AsPC-1) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13899.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.500×** | -8.0 | 5e-13 | 23/33 (SNU-423, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.609×** | -5.7 | 3e-06 | 22/44 (A-172, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **0.651×** | -5.0 | 1e-04 | 14/36 (PANC-1, C32, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.671×** | -4.4 | 0.001 | 10/38 (LOX-IMVI, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~15% here); composition shift |
| [[Thymol (drug)]] 5 µM |  | **0.771×** | -4.2 | 0.002 | 12/43 (hTERT-HPNE, SHP-77, …) | top dose only | position effect removed |
| [[Simotinib (drug)]] 0.05 µM |  | **0.674×** | -4.2 | 0.002 | 11/38 (NCI-H460, A-427, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.562×** | -3.5 | 0.032 | 7/36 (NCI-H2347, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.739×** | -3.5 | 0.032 | 6/45 (H4, A-172, …) | rises with dose | position effect removed |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.739×** | -3.5 | 0.032 | 3/45 (SK-MEL-2, LoVo, …) | inconsistent across doses | position effect removed |
| [[Berbamine (drug)]] 0.5 µM |  | **0.748×** | -3.4 | 0.044 | 9/40 (Panc 03.27, AN3 CA, …) | inconsistent across doses | position effect removed |
| [[Entecavir (monohydrate) (drug)]] 0.05 µM |  | **0.732×** | -3.3 | 0.044 | 7/38 (C-33 A, AN3 CA, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.753×** | -3.3 | 0.051 | 9/45 (NCI-H460, SW48, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.754×** | -3.2 | 0.051 | 15/41 (NCI-H460, A-172, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13899. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 3.39 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0633× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 5.12 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0842× (z -12.9) |
| [[SNU-423 (line)]] | alt | 4.90 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0497× (z -10.3) |
| [[A-172 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13899), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASTOR2]] | +0.73 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[PLEKHH3]] | +0.67 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[LAPTM4A]] | +0.66 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[SLC25A23]] | +0.66 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[PPP1R2]] | +0.65 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[STRN]] | +0.64 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[HMGN3]] | +0.63 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ARL3]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[MYPOP]] | +0.63 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[HDAC3]] | +0.62 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[CAT]] | +0.62 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[SLC9A6]] | +0.61 | +0.61 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIP7]] | -0.67 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[TRMT5]] | -0.65 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[EMG1]] | -0.65 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.65 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[METTL1]] | -0.64 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[RPL7L1]] | -0.64 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[NOL11]] | -0.64 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[TAF2]] | -0.63 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[ZNF614]] | -0.63 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[GPATCH4]] | -0.63 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[CYREN]] | -0.62 | -0.65 / -0.39 | both halves | 5e-05 |  |
| [[ICE2]] | -0.62 | -0.60 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN33]] | B | TSPAN33 activity raises GTF2IP4's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.42× lower at baseline in the lines without TSPAN33 | 0.022 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 204]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.54; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.9, -8.6); signed map (-29.9, -5.1). **Vector** length 54.7, 7.32% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.3 | +2.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.3 | +8.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.1 | +10.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +5.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -8.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -5.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.3 | -4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +0.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -3.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.7 | -0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIi pseudogene 4 |
| Locus type | pseudogene |
| Location | 7q11.23 — chr7:73,175,415-73,205,441 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51716](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51716) · Entrez [100093631](https://www.ncbi.nlm.nih.gov/gene/100093631) · Ensembl [ENSG00000233369](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233369)

## Data

Gene col 13899: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13899); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13899, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13899]; `tensor/DDL_lfc|DDL_z.npy` [13899]; `embed/gene_vectors.npy` [13899]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13899 or target_col == 13899). Every well: [[GTF2IP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF2IP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
