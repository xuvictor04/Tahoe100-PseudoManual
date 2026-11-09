---
symbol: "SEC61A2"
type: "gene"
col: 801
ensembl_id: "ENSG00000065665"
name: "SEC61 translocon subunit alpha 2"
location: "10p14"
module: 219
arm: "+"
pooled_cpm: 18.46
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 17
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/219"]
generated_by: "tahoemap"
---

# SEC61A2

*SEC61 translocon subunit alpha 2* — 10p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.25× (z +12.3, q 7e-32, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.612× (z -5.1, q 2e-04, down in 16 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Carbamazepine (drug)]] 5 µM: 0.709× (z -3.7, q 0.056, down in 15 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WHAMMP1]] (+0.72, fdr 7e-06), [[NAPB]] (+0.72, fdr 7e-06), [[DCUN1D4]] (+0.68, fdr 7e-06); moves opposite to [[CWC22]] (-0.69, fdr 7e-06), [[TAF2]] (-0.68, fdr 7e-06), [[RPL7L1]] (-0.67, fdr 7e-06).
> It is in [[Module 219]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 801.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +12.3 | 7e-32 | 43/47 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.42×** | +9.4 | 1e-18 | 45/47 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.15×** | +8.2 | 7e-14 | 41/47 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.14×** | +8.1 | 7e-14 | 44/47 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.97×** | +7.2 | 5e-11 | 41/47 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +6.8 | 1e-09 | 31/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +6.6 | 4e-09 | 34/46 (SK-MEL-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.63×** | +5.2 | 2e-05 | 31/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +5.0 | 4e-05 | 29/47 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +4.9 | 5e-05 | 29/47 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +4.8 | 7e-05 | 27/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.6 | 2e-04 | 27/46 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.51×** | +4.4 | 5e-04 | 24/47 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.46×** | +4.0 | 0.002 | 21/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.009 | 24/47 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.90×** | +3.6 | 0.013 | 15/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +3.5 | 0.016 | 16/47 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 801.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.612×** | -5.1 | 2e-04 | 16/30 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Carbamazepine (drug)]] 5 µM |  | **0.709×** | -3.7 | 0.056 | 15/47 (HEC-1-A, HepG2/C3A, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM |  | **0.791×** | -3.6 | 0.059 | 16/48 (NCI-H2347, SW1417, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.708×** | -3.4 | 0.080 | 14/37 (A-172, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.648×** | -3.3 | 0.094 | 16/47 (SNU-423, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.728× | -3.2 | 0.14 | 13/47 (SW 1271, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 801. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 13.0 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.39× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.0501× (z -21.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 14.2 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.64× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 9.64 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.77× (z +9.2) | — |
| [[A-172 (line)]] | wt | 28.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0981× (z -15.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 31.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -11.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 16.7 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0818× (z -10.2) |
| [[HOP62 (line)]] | alt | 14.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 12.9 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0849× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 20.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 17.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.37× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 16.9 | 0 | 1 | — | [[vincristine (drug)]] 5 µM 0.0625× (z -10.1) |
| [[NCI-H661 (line)]] | alt | 37.7 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0475× (z -9.0) |
| [[SHP-77 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 16.2 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0901× (z -11.3) |
| [[SW1417 (line)]] | alt | 34.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -9.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 22.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +8.8) | — |
| [[A-427 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 801), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WHAMMP1]] | +0.72 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[NAPB]] | +0.72 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[DCUN1D4]] | +0.68 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[USP3]] | +0.67 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[SEC11A]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 527 |
| [[DHRS1]] | +0.65 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[ELMO2]] | +0.65 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[RNF38]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[UBTD1]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[PDXP]] | +0.63 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[SLC9A6]] | +0.63 | +0.67 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CWC22]] | -0.69 | -0.66 / -0.68 | both halves | 7e-06 |  |
| [[TAF2]] | -0.68 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[RPL7L1]] | -0.67 | -0.60 / -0.68 | both halves | 7e-06 | STRING 832 |
| [[CEBPZ]] | -0.66 | -0.70 / -0.62 | both halves | 7e-06 |  |
| [[ZBTB38]] | -0.65 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[NSRP1]] | -0.65 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[FBXO38]] | -0.64 | -0.61 / -0.67 | both halves | 7e-06 |  |
| [[TUT7]] | -0.64 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[ZNF268]] | -0.63 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[PPP1R10]] | -0.63 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[BPTF]] | -0.63 | -0.66 / -0.59 | both halves | 7e-06 |  |
| [[LARP7]] | -0.62 | -0.61 / -0.58 | both halves | 8e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SEC61A2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 219]]; 11 genes; every member is in the + arm (projection on the module's main direction -0.726). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.44; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.9, -9.4); signed map (-31.4, -17.5). **Vector** length 81.5, 18.3% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +12.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +6.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +1.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +1.5 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | +1.5 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.3 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.3 | +1.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | +0.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.6 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | +2.3 |
|  | [[(S)-Crizotinib (drug)]] 0.5 µM |  | -1.7 | -2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | +0.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | SEC61 translocon subunit alpha 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p14 — chr10:12,129,637-12,169,961 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10578 |
| Gene groups (HGNC) | Sec61 complex subunits |
| Reactome | 6 pathways, smallest: ER-Phagosome pathway; Antigen processing-Cross presentation; Cotranslational targeting of proteins to the endoplasmic reticulum |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9S3](https://www.uniprot.org/uniprotkb/Q9H9S3) (Protein transport protein Sec61 subunit alpha isoform 2):

> Component of SEC61 channel-forming translocon complex that mediates transport of signal peptide-containing precursor polypeptides across the endoplasmic reticulum (ER). Forms a ribosome receptor and a gated pore in the ER membrane, both functions required for cotranslational translocation of nascent polypeptides.

**Summary**, from NCBI Gene [55176](https://www.ncbi.nlm.nih.gov/gene/55176):

> The protein encoded by this gene has similarity to a mouse protein which suggests a role in the insertion of secretory and membrane polypeptides into the endoplasmic reticulum. It may also be required for the assembly of membrane and secretory proteins. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:17702](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17702) · Entrez [55176](https://www.ncbi.nlm.nih.gov/gene/55176) · UniProt [Q9H9S3](https://www.uniprot.org/uniprotkb/Q9H9S3) · Ensembl [ENSG00000065665](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065665)

## Data

Gene col 801: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 801); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 801, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 801]; `tensor/DDL_lfc|DDL_z.npy` [801]; `embed/gene_vectors.npy` [801]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 801 or target_col == 801). Every well: [[SEC61A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC61A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
