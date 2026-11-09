---
symbol: "SHOC1"
type: "gene"
col: 9081
ensembl_id: "ENSG00000165181"
name: "shortage in chiasmata 1"
location: "9q31.3"
module: 21
arm: "+"
pooled_cpm: 7.26
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# SHOC1

*shortage in chiasmata 1* — 9q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.10× (z +14.0, q 1e-41, up in 34 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.669× (z -5.2, q 1e-04, down in 16 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.302×, BT-474 0.219×; ⚠ cell-cycle shift, explains ~21% of this change); [[Vilanterol (drug)]] 0.5 µM in 1 line (HS-578T 0.0749×); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H2030 0.164×; ⚠ cell-cycle shift, explains ~25% of this change); [[Furosemide (drug)]] 0.5 µM in 1 line (Panc 03.27 0.122×); [[Resveratrol (drug)]] 0.05 µM in 1 line (Hs 766T 0.0900×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCN1A-AS1]] (+0.66, fdr 1e-05), [[DPYD-AS1]] (+0.66, fdr 2e-05), [[EHBP1-AS1]] (+0.65, fdr 2e-05); moves opposite to [[PHF6]] (-0.50, fdr 2e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9081.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +14.0 | 1e-41 | 34/45 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.07×** | +9.7 | 1e-19 | 22/31 (A549, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +7.6 | 8e-12 | 7/12 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.65×** | +6.7 | 3e-09 | 24/47 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +6.2 | 6e-08 | 8/22 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +4.8 | 1e-04 | 13/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.005 | 11/48 (SW 900, HS-578T, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.007 | 9/38 (A-172, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.74×** | +3.8 | 0.008 | 0/12 | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.009 | 9/41 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.010 | 10/46 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.010 | 7/47 (HEC-1-A, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.021 | 3/45 (NCI-H460, RKO, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.30×** | +3.4 | 0.024 | 14/40 (LS 180, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.029 | 3/45 (NCI-H23, NCI-H460, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.029 | 9/46 (H4, SNU-423, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9081.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.302×, BT-474 0.219×; ⚠ cell-cycle shift, explains ~21% of this change); [[Vilanterol (drug)]] 0.5 µM in 1 line (HS-578T 0.0749×); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H2030 0.164×; ⚠ cell-cycle shift, explains ~25% of this change); [[Furosemide (drug)]] 0.5 µM in 1 line (Panc 03.27 0.122×); [[Resveratrol (drug)]] 0.05 µM in 1 line (Hs 766T 0.0900×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.669×** | -5.2 | 1e-04 | 16/46 (NCI-H2030, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.911× | -4.4 | 0.003 | 15/48 (NCI-H2347, HepG2/C3A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.736×** | -4.1 | 0.008 | 10/46 (NCI-H2030, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.761×** | -3.6 | 0.040 | 10/47 (NCI-H2030, BT-474, …) | top dose only | position effect removed |
| [[Larotrectinib (drug)]] 5 µM |  | 0.841× | -3.3 | 0.12 | 11/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.787× | -3.2 | 0.13 | 10/47 (NCI-H2030, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9081. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 6.43 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 13.4× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 36.7 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.164× (z -9.4) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A549 (line)]] | wt | 5.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -8.6) ⚠ cell-cycle shift, explains ~21% of this change |
| [[Hs 766T (line)]] | wt | 6.29 | 0 | 1 | — | [[Resveratrol (drug)]] 0.05 µM 0.0900× (z -8.9) |
| [[HS-578T (line)]] | alt | 5.09 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0749× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 8.60 | 0 | 1 | — | [[Furosemide (drug)]] 0.5 µM 0.122× (z -9.1) |
| [[A-172 (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9081), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCN1A-AS1]] | +0.66 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[DPYD-AS1]] | +0.66 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[EHBP1-AS1]] | +0.65 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[TICAM2-AS1]] | +0.63 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[CTDSPL2-DT]] | +0.62 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[C2CD5-AS1]] | +0.62 | +0.40 / +0.65 | both halves | 5e-05 |  |
| [[ZNF451-AS1]] | +0.61 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[IL1RAPL2]] | +0.61 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[CHMP3-AS1]] | +0.60 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[MMP24]] | +0.60 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[LANCL1-AS1]] | +0.59 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[PKD2L2]] | +0.59 | +0.42 / +0.60 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF6]] | -0.50 | -0.29 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SHOC1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.630). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.4, 28.2); signed map (33.7, 8.0). **Vector** length 58.4, 7.55% of its response variance represented; |z| ≥ 3 in 900 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.7 | +2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +1.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.0 | -4.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -1.9 | -3.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -0.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -0.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | shortage in chiasmata 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.3 — chr9:111,686,171-111,795,008 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32779, Zip2, MZIP2; previously C9orf84 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VXU9](https://www.uniprot.org/uniprotkb/Q5VXU9) (Protein shortage in chiasmata 1 ortholog):

> ATPase required during meiosis for the formation of crossover recombination intermediates (By similarity). Binds DNA: preferentially binds to single-stranded DNA and DNA branched structures. Does not show nuclease activity in vitro, but shows ATPase activity, which is stimulated by the presence of single-stranded DNA. Plays a key role in homologous recombination and crossing-over in meiotic prophase I in male and female germ cells (By similarity). Required for proper synaptonemal complex …

**Summary**, from NCBI Gene [158401](https://www.ncbi.nlm.nih.gov/gene/158401):

> Enables ATP hydrolysis activity and single-stranded DNA binding activity. Predicted to be involved in resolution of meiotic recombination intermediates and synaptonemal complex assembly. Predicted to be located in chromosome. Predicted to be active in condensed nuclear chromosome. Implicated in spermatogenic failure 75. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26535](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26535) · Entrez [158401](https://www.ncbi.nlm.nih.gov/gene/158401) · UniProt [Q5VXU9](https://www.uniprot.org/uniprotkb/Q5VXU9) · Ensembl [ENSG00000165181](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165181)

## Data

Gene col 9081: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9081); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9081, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9081]; `tensor/DDL_lfc|DDL_z.npy` [9081]; `embed/gene_vectors.npy` [9081]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9081 or target_col == 9081). Every well: [[SHOC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHOC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
