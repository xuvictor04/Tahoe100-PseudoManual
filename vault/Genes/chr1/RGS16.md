---
symbol: "RGS16"
type: "gene"
col: 6716
ensembl_id: "ENSG00000143333"
name: "regulator of G protein signaling 16"
location: "1q25.3"
module: 61
arm: "+"
pooled_cpm: 4.1
n_lines_expressing: 37
n_dd_up: 43
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# RGS16

*regulator of G protein signaling 16* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (19 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.84× (z +22.8, q 0e+00, up in 29 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.146×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.265×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (CFPAC-1 0.0464×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNAI1]] (+0.63, fdr 3e-05), [[CNTN4]] (+0.53, fdr 3e-05), [[KCNIP4]] (+0.53, fdr 4e-05); moves opposite to [[NCBP3]] (-0.48, fdr 1e-04), [[ERGIC2]] (-0.47, fdr 2e-04), [[MTOR]] (-0.46, fdr 1e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PLTP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 19 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6716.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.84×** | +22.8 | 0e+00 | 29/30 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **7.94×** | +16.2 | 0e+00 | 32/33 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.12×** | +15.7 | 0e+00 | 20/28 (hTERT-HPNE, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **6.38×** | +14.5 | 1e-45 | 33/34 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **3.65×** | +14.3 | 2e-44 | 31/33 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **4.65×** | +12.0 | 2e-31 | 29/34 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **3.83×** | +10.1 | 4e-22 | 19/33 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.09×** | +8.8 | 7e-17 | 24/34 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **3.20×** | +8.8 | 1e-16 | 13/23 (NCI-H460, SHP-77, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.99×** | +8.6 | 5e-16 | 29/32 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.97×** | +8.5 | 8e-16 | 21/32 (SW480, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.11×** | +8.2 | 8e-15 | 13/33 (A-172, HEC-1-A, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.87×** | +7.9 | 9e-14 | 12/16 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.97×** | +7.9 | 1e-13 | 2/8 (NCI-H460, CFPAC-1) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.61×** | +7.5 | 2e-12 | 18/29 (J82, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.05×** | +5.6 | 6e-07 | 17/34 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.93×** | +4.4 | 3e-04 | 11/28 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **2.73×** | +4.1 | 9e-04 | 10/26 (NCI-H460, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.65×** | +4.0 | 0.002 | 7/24 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.62×** | +3.9 | 0.002 | 4/31 (NCI-H2347, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6716.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.146×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.265×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (CFPAC-1 0.0464×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bimiralisib (drug)]] 5 µM |  | 0.462× | -3.2 | 0.47 | 5/32 (SHP-77, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Erlotinib (drug)]] 5 µM |  | 0.661× | -3.1 | 0.47 | 6/32 (A-172, SW 900, …) | top dose only | position effect removed |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.670× | -3.0 | 0.47 | 11/32 (HEC-1-A, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.85 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6716. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.4 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.48× (z +14.1) | — |
| [[NCI-H2347 (line)]] | alt | 1.90 | 4 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 15.8× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 3.31 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.5× (z +11.8) | [[Clobetasol propionate (drug)]] 0.05 µM 0.0464× (z -8.6) |
| [[A-172 (line)]] | wt | 13.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.95× (z +11.9) | — |
| [[hTERT-HPNE (line)]] | wt | 5.13 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.9× (z +11.3) | — |
| [[J82 (line)]] | alt | 1.21 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.5× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 27.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.265× (z -9.2) |
| [[SW480 (line)]] | alt | 3.30 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +12.8) | — |
| [[HEC-1-A (line)]] | alt | 1.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 60.5× (z +12.6) | — |
| [[HT-29 (line)]] | alt | 6.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.31× (z +8.6) | — |
| [[KATO III (line)]] | alt | 3.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.99× (z +9.7) | — |
| [[LoVo (line)]] | wt | 6.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 10.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.15× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 3.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.79× (z +9.7) | — |
| [[A-427 (line)]] | wt | 0.882 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.792 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.810 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.918 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.666 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.979 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.405 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.378 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.846 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.697 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6716), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAI1]] | +0.63 | +0.44 / +0.72 | both halves | 3e-05 |  |
| [[CNTN4]] | +0.53 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[KCNIP4]] | +0.53 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[TLL2]] | +0.53 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[GRIP2]] | +0.52 | +0.32 / +0.57 | both halves | 2e-04 |  |
| [[TPBG]] | +0.52 | +0.30 / +0.47 | both halves | 2e-04 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[VEGFA]] | +0.52 | +0.28 / +0.46 | both halves | 3e-04 |  |
| [[PTPRT]] | +0.52 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[DIRC3-AS1]] | +0.52 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[TNFRSF10B]] | +0.51 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[MTUS2]] | +0.51 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[RUNX3]] | +0.51 | +0.34 / +0.48 | both halves | 1e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCBP3]] | -0.48 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[ERGIC2]] | -0.47 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[MTOR]] | -0.46 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[SMARCC2]] | -0.45 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[AP3M1]] | -0.45 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[YLPM1]] | -0.44 | -0.22 / -0.44 | both halves | 6e-04 |  |
| [[VPS50]] | -0.43 | -0.20 / -0.53 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RGS16's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLTP]] | B | RGS16 activity raises PLTP's level | lines that do not express RGS16 (13) vs lines expressing it (37) | 1.98× lower at baseline in the lines without RGS16 | 0.076 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.538). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.7, 27.7); signed map (29.8, 20.3). **Vector** length 61.1, 11.3% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +14.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +22.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +2.1 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +3.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.5 | +3.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.4 | +4.0 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -1.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | regulator of G protein signaling 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:182,598,623-182,604,389 (-) |
| Ensembl biotype | protein_coding |
| Also known as | A28-RGS14, RGS-r |
| Gene groups (HGNC) | Regulators of G-protein signaling |
| Hallmark sets | INFLAMMATORY_RESPONSE, KRAS_SIGNALING_UP, IL2_STAT5_SIGNALING, P53_PATHWAY |
| Reactome | 5 pathways, smallest: G alpha (z) signalling events; G alpha (q) signalling events; G alpha (i) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [O15492](https://www.uniprot.org/uniprotkb/O15492) (Regulator of G protein signaling 16):

> Regulates G protein-coupled receptor signaling cascades. Inhibits signal transduction by increasing the GTPase activity of G protein alpha subunits, thereby driving them into their inactive GDP-bound form. Plays an important role in the phototransduction cascade by regulating the lifetime and effective concentration of activated transducin alpha. May regulate extra and intracellular mitogenic signals (By similarity).

**Summary**, from NCBI Gene [6004](https://www.ncbi.nlm.nih.gov/gene/6004):

> The protein encoded by this gene belongs to the 'regulator of G protein signaling' family. It inhibits signal transduction by increasing the GTPase activity of G protein alpha subunits. It also may play a role in regulating the kinetics of signaling in the phototransduction cascade. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9997](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9997) · Entrez [6004](https://www.ncbi.nlm.nih.gov/gene/6004) · UniProt [O15492](https://www.uniprot.org/uniprotkb/O15492) · Ensembl [ENSG00000143333](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143333)

## Data

Gene col 6716: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6716); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6716, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6716]; `tensor/DDL_lfc|DDL_z.npy` [6716]; `embed/gene_vectors.npy` [6716]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6716 or target_col == 6716). Every well: [[RGS16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RGS16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
