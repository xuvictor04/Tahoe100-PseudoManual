---
symbol: "POLN"
type: "gene"
col: 5153
ensembl_id: "ENSG00000130997"
name: "DNA polymerase nu"
location: "4p16.3"
module: 39
arm: "+"
pooled_cpm: 19.22
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# POLN

*DNA polymerase nu* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.02× (z +20.4, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Pyridoxine (hydrochloride) (drug)]] 5 µM: 0.782× (z -4.4, q 0.006, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H2030 0.158×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMBD1P]] (+0.68, fdr 7e-06), [[AVIL]] (+0.66, fdr 7e-06), [[FLJ46284]] (+0.65, fdr 9e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADORA1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5153.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.02×** | +20.4 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.38×** | +15.5 | 0e+00 | 44/47 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.24×** | +14.8 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.91×** | +13.5 | 2e-39 | 44/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +7.8 | 1e-12 | 29/47 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +7.6 | 3e-12 | 31/42 (HT-29, J82, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +6.0 | 2e-07 | 28/47 (A-172, C32, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +5.9 | 2e-07 | 28/47 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.52×** | +5.3 | 9e-06 | 28/48 (SW480, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.52×** | +5.0 | 3e-05 | 25/47 (SW480, NCI-H2347, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.7 | 1e-04 | 22/48 (SW480, HT-29, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.45×** | +4.7 | 1e-04 | 27/48 (NCI-H2347, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +4.2 | 0.001 | 25/48 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +4.1 | 0.001 | 22/47 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.82×** | +4.0 | 0.003 | 20/47 (HOP62, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.006 | 21/48 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5153.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H2030 0.158×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.782×** | -4.4 | 0.006 | 23/48 (A-172, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.764× | -3.4 | 0.14 | 16/48 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | 0.602× | -3.4 | 0.14 | 12/43 (SK-MEL-2, A498, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.762× | -3.2 | 0.19 | 16/46 (H4, HepG2/C3A, …) | inconsistent across doses | low cells (technical?) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.778× | -3.0 | 0.29 | 14/47 (hTERT-HPNE, SNU-423, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5153. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.6 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 9.18× (z +14.1) | — |
| [[SW480 (line)]] | alt | 19.1 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.10× (z +16.2) | — |
| [[A-172 (line)]] | wt | 17.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.75× (z +10.3) | — |
| [[J82 (line)]] | alt | 27.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.00× (z +13.4) | — |
| [[KATO III (line)]] | alt | 22.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.15× (z +13.4) | — |
| [[LoVo (line)]] | wt | 24.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +16.0) | — |
| [[NCI-H1792 (line)]] | alt | 14.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +16.7) | — |
| [[PANC-1 (line)]] | alt | 16.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.30× (z +12.4) | — |
| [[A-427 (line)]] | wt | 17.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.13× (z +10.1) | — |
| [[A498 (line)]] | wt | 13.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.58× (z +14.8) | — |
| [[A549 (line)]] | wt | 15.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.00× (z +11.0) | — |
| [[BT-474 (line)]] | alt | 22.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.85× (z +9.7) | — |
| [[C32 (line)]] | wt | 14.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 18.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 33.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.51× (z +9.8) | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.71× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 13.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.81× (z +12.4) | — |
| [[LOX-IMVI (line)]] | wt | 26.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.58× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 23.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 12.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.83× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.158× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 23.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +11.0) | — |
| [[RKO (line)]] | wt | 15.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.50× (z +11.9) | — |
| [[SK-MEL-2 (line)]] | alt | 13.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 8.08× (z +10.1) | — |
| [[AsPC-1 (line)]] | alt | 13.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.02× (z +9.1) | — |
| [[C-33 A (line)]] | alt | 27.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.65× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 23.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.60× (z +13.1) | — |
| [[Hs 766T (line)]] | wt | 11.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.74× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 11.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.50× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 14.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.09× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 19.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.53× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 26.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.37× (z +11.5) | — |
| [[SW1417 (line)]] | alt | 13.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.67× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5153), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMBD1P]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[AVIL]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[FLJ46284]] | +0.65 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[SLC5A11]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[SLC4A5]] | +0.64 | +0.71 / +0.58 | both halves | 8e-06 |  |
| [[SLC7A9]] | +0.64 | +0.72 / +0.43 | both halves | 3e-05 |  |
| [[ADCY10P1]] | +0.63 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[SLC23A3]] | +0.63 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[FLACC1]] | +0.63 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[SLC22A14]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[IMPA1P1]] | +0.62 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[PDC-AS1]] | +0.62 | +0.67 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADORA1]] | B | ADORA1 activity raises POLN's level | lines that do not express ADORA1 (7) vs lines expressing it (43) | 1.62× lower at baseline in the lines without ADORA1 | 0.009 | ⚠ within organs, on part of the lines; also absent: DRAM1, HHAT, SUGCT; maybe low, not absent |
| [[IMPA1P1]] | B | IMPA1P1 activity raises POLN's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.59× lower at baseline in the lines without IMPA1P1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.591). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.3, -15.9); signed map (15.0, 7.1). **Vector** length 82.0, 17.5% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Filgotinib (drug)]] 5 µM |  | +4.0 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +6.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.4 | +5.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.1 | +4.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.5 | +20.4 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +2.2 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -3.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.6 | -3.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -1.5 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -2.2 | -2.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | DNA polymerase nu |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:2,071,918-2,242,121 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | DNA polymerases |
| Reactome | 2 pathways, smallest: Fanconi Anemia Pathway; DNA Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z5Q5](https://www.uniprot.org/uniprotkb/Q7Z5Q5) (DNA polymerase nu):

> DNA polymerase with very low fidelity that catalyzes considerable misincorporation by inserting dTTP opposite a G template, and dGTP opposite a T template. Is the least accurate of the DNA polymerase A family (i.e. POLG, POLN and POLQ). Can perform accurate translesion DNA synthesis (TLS) past a 5S-thymine glycol. Can perform efficient strand displacement past a nick or a gap and gives rise to an amount of product similar to that on non-damaged template. Has no exonuclease activity. Error-prone …

**Summary**, from NCBI Gene [353497](https://www.ncbi.nlm.nih.gov/gene/353497):

> This gene encodes a DNA polymerase type-A family member. The encoded protein plays a role in DNA repair and homologous recombination. This gene shares its 5' exons with some transcripts from overlapping GeneID: 79441, which encodes an augmentin-like protein complex subunit. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:18870](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18870) · Entrez [353497](https://www.ncbi.nlm.nih.gov/gene/353497) · UniProt [Q7Z5Q5](https://www.uniprot.org/uniprotkb/Q7Z5Q5) · Ensembl [ENSG00000130997](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130997)

## Data

Gene col 5153: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5153); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5153, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5153]; `tensor/DDL_lfc|DDL_z.npy` [5153]; `embed/gene_vectors.npy` [5153]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5153 or target_col == 5153). Every well: [[POLN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
