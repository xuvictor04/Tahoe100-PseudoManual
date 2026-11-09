---
symbol: "BRMS1"
type: "gene"
col: 10520
ensembl_id: "ENSG00000174744"
name: "BRMS1 transcriptional repressor and anoikis regulator"
location: "11q13.2"
module: 107
arm: "+"
pooled_cpm: 10.84
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# BRMS1

*BRMS1 transcriptional repressor and anoikis regulator* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.24× (z +11.8, q 3e-29, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.699× (z -4.0, q 0.044, down in 21 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.170×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (BT-474 0.0917×); [[Vortioxetine (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0724×; ⚠ toxic); [[Saquinavir (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0852×); [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0811×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSR3]] (+0.66, fdr 7e-06), [[LRRC47]] (+0.65, fdr 7e-06), [[FTSJ3]] (+0.65, fdr 1e-05); moves opposite to [[TUBA1B]] (-0.50, fdr 3e-05), [[H2AZ2]] (-0.49, fdr 1e-04), [[RHOBTB3]] (-0.47, fdr 1e-04).
> It is in [[Module 107]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10520.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +11.8 | 3e-29 | 42/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.75×** | +11.2 | 1e-26 | 46/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.73×** | +11.1 | 2e-26 | 42/47 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.11×** | +8.3 | 2e-14 | 26/34 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.10×** | +8.2 | 2e-14 | 39/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +8.0 | 1e-13 | 34/39 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.93×** | +7.0 | 2e-10 | 12/16 (SW480, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.44×** | +5.4 | 4e-06 | 21/43 (LS 180, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.62×** | +5.3 | 7e-06 | 23/41 (A549, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +5.3 | 7e-06 | 27/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.49×** | +5.3 | 7e-06 | 29/46 (SW480, A-427, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.62×** | +5.2 | 1e-05 | 26/47 (NCI-H460, SNU-423, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.61×** | +5.1 | 2e-05 | 22/45 (SW480, AsPC-1, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +4.9 | 3e-05 | 22/44 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.7 | 1e-04 | 22/48 (MIA PaCa-2, A498, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +4.6 | 1e-04 | 21/47 (HOP62, NCI-H460, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +4.1 | 0.001 | 17/47 (SW1417, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +4.1 | 0.001 | 18/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +4.1 | 0.001 | 20/47 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +4.0 | 0.002 | 19/45 (NCI-H1573, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +3.4 | 0.015 | 13/43 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.026 | 12/47 (HOP62, NCI-H460, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10520.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.170×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (BT-474 0.0917×); [[Vortioxetine (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0724×; ⚠ toxic); [[Saquinavir (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0852×); [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0811×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.699×** | -4.0 | 0.044 | 21/46 (NCI-H2347, A498, …) | two highest doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.732× | -3.4 | 0.16 | 16/47 (CHP-212, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10520. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 7.42 | 0 | 2 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0724× (z -9.3) ⚠ toxic · without an alert: [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0811× (z -8.9) |
| [[SW480 (line)]] | alt | 13.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +10.1) | — |
| [[A549 (line)]] | wt | 10.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 12.3 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0917× (z -9.9) |
| [[KATO III (line)]] | alt | 11.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[PANC-1 (line)]] | alt | 13.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 5.80 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0852× (z -9.0) |
| [[A-172 (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.77 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10520), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSR3]] | +0.66 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[LRRC47]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[FTSJ3]] | +0.65 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[GCC1]] | +0.65 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[UCK1]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[PTPN23]] | +0.62 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[ZNF343]] | +0.60 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[TFIP11]] | +0.59 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[ZNF581]] | +0.58 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[WDR83]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[TADA2B]] | +0.57 | +0.51 / +0.61 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |
| [[PEX16]] | +0.57 | +0.54 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBA1B]] | -0.50 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[H2AZ2]] | -0.49 | -0.47 / -0.35 | both halves | 1e-04 | pathway: Chromatin modifying enzymes |
| [[RHOBTB3]] | -0.47 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[ATP1B3]] | -0.46 | -0.50 / -0.35 | both halves | 1e-04 | pathway: Potential therapeutics for SARS |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BRMS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.755). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.2, -3.2); signed map (-10.6, -25.7). **Vector** length 60.8, 10.1% of its response variance represented; |z| ≥ 3 in 859 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.5 | +5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +11.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.9 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +5.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +4.7 |
| fall | [[Tucidinostat (drug)]] 0.5 µM |  | -4.0 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -2.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.7 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | +0.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | BRMS1 transcriptional repressor and anoikis regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:66,337,333-66,345,125 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564A063 |
| Reactome | 6 pathways, smallest: HDACs deacetylate histones; Potential therapeutics for SARS; Chromatin modifying enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCU9](https://www.uniprot.org/uniprotkb/Q9HCU9) (Breast cancer metastasis-suppressor 1):

> Transcriptional repressor. Down-regulates transcription activation by NF-kappa-B by promoting the deacetylation of RELA at 'Lys-310'. Promotes HDAC1 binding to promoter regions. Down-regulates expression of anti-apoptotic genes that are controlled by NF-kappa-B. Promotes apoptosis in cells that have inadequate adherence to a substrate, a process called anoikis, and may thereby inhibit metastasis. May be a mediator of metastasis suppression in breast carcinoma.

**Summary**, from NCBI Gene [25855](https://www.ncbi.nlm.nih.gov/gene/25855):

> This gene reduces the metastatic potential, but not the tumorogenicity, of human breast cancer and melanoma cell lines. The protein encoded by this gene localizes primarily to the nucleus and is a component of the mSin3a family of histone deacetylase complexes (HDAC). The protein contains two coiled-coil motifs and several imperfect leucine zipper motifs. Alternative splicing results in two transcript variants encoding different isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17262](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17262) · Entrez [25855](https://www.ncbi.nlm.nih.gov/gene/25855) · UniProt [Q9HCU9](https://www.uniprot.org/uniprotkb/Q9HCU9) · Ensembl [ENSG00000174744](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174744)

## Data

Gene col 10520: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10520); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10520, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10520]; `tensor/DDL_lfc|DDL_z.npy` [10520]; `embed/gene_vectors.npy` [10520]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10520 or target_col == 10520). Every well: [[BRMS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRMS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
