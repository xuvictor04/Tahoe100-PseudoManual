---
symbol: "BFSP1"
type: "gene"
col: 4682
ensembl_id: "ENSG00000125864"
name: "beaded filament structural protein 1"
location: "20p12.1"
module: 80
arm: "+"
pooled_cpm: 6.66
n_lines_expressing: 47
n_dd_up: 26
n_dd_down: 6
n_dd_up_clean: 20
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# BFSP1

*beaded filament structural protein 1* — 20p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.26× (z +13.7, q 6e-40, up in 27 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.639× (z -5.3, q 7e-05, down in 15 of 44 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CUBN]] (+0.67, fdr 1e-05), [[DPY19L2P2]] (+0.64, fdr 7e-06), [[ADGRL4]] (+0.63, fdr 1e-05); moves opposite to [[RAB40B]] (-0.54, fdr 3e-04), [[LCMT1]] (-0.54, fdr 1e-04), [[DHTKD1]] (-0.53, fdr 1e-04).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4682.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +13.7 | 6e-40 | 27/37 (Hs 766T, HOP62, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.25×** | +9.2 | 6e-18 | 6/9 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +8.2 | 4e-14 | 12/24 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +8.1 | 5e-14 | 19/39 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.95×** | +8.0 | 2e-13 | 26/41 (HOP62, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.85×** | +7.3 | 3e-11 | 19/34 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +7.0 | 3e-10 | 17/44 (MIA PaCa-2, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.78×** | +6.8 | 7e-10 | 19/45 (C32, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +6.7 | 2e-09 | 22/44 (SW480, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.6 | 2e-09 | 21/44 (BT-474, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.70×** | +6.3 | 1e-08 | 18/43 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +6.3 | 2e-08 | 11/16 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +5.1 | 1e-05 | 15/41 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +5.0 | 2e-05 | 12/32 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +4.8 | 5e-05 | 16/41 (LOX-IMVI, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.001 | 11/36 (BT-474, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.75×** | +3.5 | 0.015 | 7/29 (PANC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.017 | 13/43 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4682.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.639×** | -5.3 | 7e-05 | 15/44 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.456×** | -4.9 | 3e-04 | 12/40 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.704×** | -4.2 | 0.006 | 12/36 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.791×** | -3.9 | 0.013 | 13/44 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.734×** | -3.7 | 0.028 | 12/44 (NCI-H1573, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.739×** | -3.6 | 0.033 | 11/42 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.773× | -3.0 | 0.19 | 8/42 (NCI-H2030, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4682. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.175× (z -13.1) |
| [[A-172 (line)]] | wt | 5.75 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.40× (z +11.8) | [[Penfluridol (drug)]] 5 µM 0.0740× (z -9.9) |
| [[Hs 766T (line)]] | wt | 7.30 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +8.5) | [[Norepinephrine (hydrochloride) (drug)]] 0.5 µM 0.0626× (z -10.9) |
| [[A-427 (line)]] | wt | 4.39 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0643× (z -8.8) |
| [[C32 (line)]] | wt | 44.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -10.4) |
| [[HOP62 (line)]] | alt | 6.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 3.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.88× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 3.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +11.3) | — |
| [[NCI-H2030 (line)]] | alt | 3.73 | 0 | 1 | — | [[Dexamethasone (drug)]] 0.5 µM 0.0578× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 10.0 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0849× (z -9.0) |
| [[A498 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4682), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CUBN]] | +0.67 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[DPY19L2P2]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ADGRL4]] | +0.63 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[PLEKHA8P1]] | +0.63 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[LINC01762]] | +0.60 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[NQO1-DT]] | +0.60 | +0.66 / +0.40 | both halves | 5e-05 |  |
| [[MMRN2]] | +0.59 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[LPXN]] | +0.59 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[TLR6]] | +0.59 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[CFAP54]] | +0.58 | +0.57 / +0.38 | both halves | 6e-05 |  |
| [[LINC02542]] | +0.57 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[DENND5B-AS1]] | +0.57 | +0.68 / +0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[DPY19L2]] | +0.57 | +0.58 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB40B]] | -0.54 | -0.57 / -0.27 | both halves | 3e-04 |  |
| [[LCMT1]] | -0.54 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[DHTKD1]] | -0.53 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[WDR5]] | -0.52 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[RAP1A]] | -0.52 | -0.58 / -0.31 | both halves | 2e-04 |  |
| [[ZDHHC9]] | -0.52 | -0.57 / -0.37 | both halves | 7e-05 |  |
| [[SLC35A3]] | -0.52 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[GNB2]] | -0.52 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[PDPR2P]] | -0.52 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[SDHAP1]] | -0.51 | -0.59 / -0.27 | both halves | 3e-04 |  |
| [[MTMR12]] | -0.51 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[PSMD9]] | -0.51 | -0.51 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BFSP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.617). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.8, 16.2); signed map (27.6, 3.9). **Vector** length 64.9, 9.88% of its response variance represented; |z| ≥ 3 in 1,022 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.2 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +13.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.6 | +7.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +6.3 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -0.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.4 | -4.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | beaded filament structural protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.1 — chr20:17,493,905-17,569,220 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CP94, CP115, LIFL-H, filensin |
| Gene groups (HGNC) | Beaded filament structural proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12934](https://www.uniprot.org/uniprotkb/Q12934) (Filensin):

> Required for the correct formation of lens intermediate filaments as part of a complex composed of BFSP1, BFSP2 and CRYAA. Involved in altering the calcium regulation of MIP water permeability.

**Summary**, from NCBI Gene [631](https://www.ncbi.nlm.nih.gov/gene/631):

> This gene encodes a lens-specific intermediate filament-like protein named filensin. The encoded protein is expressed in lens fiber cells after differentiation has begun. This protein functions as a component of the beaded filament which is a cytoskeletal structure found in lens fiber cells. Mutations in this gene are the cause of autosomal recessive cortical juvenile-onset cataract. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:1040](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1040) · Entrez [631](https://www.ncbi.nlm.nih.gov/gene/631) · UniProt [Q12934](https://www.uniprot.org/uniprotkb/Q12934) · Ensembl [ENSG00000125864](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125864)

## Data

Gene col 4682: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4682); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4682, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4682]; `tensor/DDL_lfc|DDL_z.npy` [4682]; `embed/gene_vectors.npy` [4682]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4682 or target_col == 4682). Every well: [[BFSP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BFSP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
