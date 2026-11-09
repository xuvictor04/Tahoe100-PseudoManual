---
symbol: "EXOC3"
type: "gene"
col: 11081
ensembl_id: "ENSG00000180104"
name: "exocyst complex component 3"
location: "5p15.33"
module: 127
arm: "+"
pooled_cpm: 50.02
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# EXOC3

*exocyst complex component 3* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.36× (z +9.8, q 9e-20, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.567× (z -18.0, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF40]] (+0.64, fdr 1e-05), [[SUDS3]] (+0.64, fdr 1e-05), [[PRPF31]] (+0.64, fdr 1e-05); moves opposite to [[PTGR3]] (-0.53, fdr 4e-05), [[SATB2]] (-0.53, fdr 3e-05), [[TRIM7]] (-0.52, fdr 1e-04).
> It is in [[Module 127]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11081.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +9.8 | 9e-20 | 26/48 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.95×** | +7.8 | 2e-12 | 36/49 (SW480, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.53×** | +5.0 | 1e-04 | 24/48 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.48×** | +4.6 | 7e-04 | 17/49 (Hs 766T, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.2 | 0.14 | 20/48 (Hs 766T, SHP-77, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 1.15× | +3.1 | 0.14 | 12/48 (A-427, HT-29, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.04× | +3.1 | 0.14 | 0/49 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.1 | 0.14 | 19/48 (HOP62, SHP-77, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11081.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.567×** | -18.0 | 0e+00 | 43/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.734×** | -6.7 | 8e-09 | 29/48 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.748×** | -6.5 | 2e-08 | 26/48 (NCI-H23, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.780×** | -5.4 | 1e-05 | 26/49 (SW480, RKO, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.890× | -3.7 | 0.023 | 11/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.849× | -3.7 | 0.023 | 15/48 (NCI-H661, NCI-H1792, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | 0.865× | -3.1 | 0.14 | 10/48 (HOP62, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11081. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 62.8 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -17.5) |
| [[H4 (line)]] | wt | 64.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +18.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -9.3) |
| [[HS-578T (line)]] | alt | 56.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -11.2) |
| [[NCI-H2030 (line)]] | alt | 45.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 46.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -17.1) |
| [[PANC-1 (line)]] | alt | 44.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -10.1) |
| [[A-172 (line)]] | wt | 41.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -9.2) |
| [[A-427 (line)]] | wt | 57.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -16.3) |
| [[A498 (line)]] | wt | 44.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.2) | — |
| [[A549 (line)]] | wt | 43.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 55.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -9.3) |
| [[COLO 205 (line)]] | alt | 86.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -10.8) |
| [[HCT15 (line)]] | alt | 67.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -9.3) |
| [[Hs 766T (line)]] | wt | 62.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -10.4) |
| [[HT-29 (line)]] | alt | 65.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 45.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -9.5) |
| [[KATO III (line)]] | alt | 49.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -11.5) |
| [[LoVo (line)]] | wt | 56.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -11.2) |
| [[LS 180 (line)]] | wt | 57.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 40.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -14.6) |
| [[NCI-H23 (line)]] | alt | 19.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.9) | — |
| [[RKO (line)]] | wt | 37.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -8.7) ⚠ cell-cycle shift, explains ~22% of this change |
| [[RPMI-7951 (line)]] | alt | 52.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 24.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -9.2) |
| [[SW 1271 (line)]] | alt | 52.3 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0719× (z -10.0) ⚠ toxic; unreliable plate only |
| [[SW1417 (line)]] | alt | 58.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -13.1) |
| [[SW48 (line)]] | wt | 43.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0730× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 72.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11081), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF40]] | +0.64 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[SUDS3]] | +0.64 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[PRPF31]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[VPS41]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[DMAP1]] | +0.59 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[BAP1]] | +0.58 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[STEEP1]] | +0.57 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[GRIPAP1]] | +0.57 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[SMIM7]] | +0.57 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[VPS11]] | +0.55 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SNAP47]] | +0.55 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[HIF1AN]] | +0.55 | +0.54 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTGR3]] | -0.53 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[SATB2]] | -0.53 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[TRIM7]] | -0.52 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[LRR1]] | -0.52 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[C9orf40]] | -0.51 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[ING2-DT]] | -0.51 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[PRKCE]] | -0.50 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[ELOVL6]] | -0.49 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[KLHL29]] | -0.49 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[ENDOG]] | -0.48 | -0.22 / -0.49 | both halves | 6e-04 |  |
| [[TBC1D4]] | -0.48 | -0.43 / -0.44 | both halves | 3e-05 | pathway: Translocation of SLC2A4 (GLUT4) to the plasma membrane |
| [[TRIM36]] | -0.47 | -0.35 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises EXOC3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-32.8, -3.2); signed map (-13.6, -29.0). **Vector** length 83.1, 15.9% of its response variance represented; |z| ≥ 3 in 827 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +3.9 | +7.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | +3.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.4 | +3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.0 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +5.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | -1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.0 | -18.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -6.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -5.7 | -5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.2 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | exocyst complex component 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.33 — chr5:443,175-471,937 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Sec6; previously SEC6L1 |
| Gene groups (HGNC) | Exocyst complex |
| Reactome | 10 pathways, smallest: VxPx cargo-targeting to cilium; Insulin processing; Peptide hormone metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O60645](https://www.uniprot.org/uniprotkb/O60645) (Exocyst complex component 3):

> Component of the exocyst complex involved in the docking of exocytic vesicles with fusion sites on the plasma membrane.

**Summary**, from NCBI Gene [11336](https://www.ncbi.nlm.nih.gov/gene/11336):

> The protein encoded by this gene is a component of the exocyst complex, a multiple protein complex essential for targeting exocytic vesicles to specific docking sites on the plasma membrane. Though best characterized in yeast, the component proteins and functions of exocyst complex have been demonstrated to be highly conserved in higher eukaryotes. At least eight components of the exocyst complex, including this protein, are found to interact with the actin cytoskeletal remodeling and vesicle …

**Accessions** — [HGNC:30378](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30378) · Entrez [11336](https://www.ncbi.nlm.nih.gov/gene/11336) · UniProt [O60645](https://www.uniprot.org/uniprotkb/O60645) · Ensembl [ENSG00000180104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180104)

## Data

Gene col 11081: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11081); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11081, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11081]; `tensor/DDL_lfc|DDL_z.npy` [11081]; `embed/gene_vectors.npy` [11081]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11081 or target_col == 11081). Every well: [[EXOC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXOC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
