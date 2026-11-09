---
symbol: "AS3MT"
type: "gene"
col: 13203
ensembl_id: "ENSG00000214435"
name: "arsenite methyltransferase"
location: "10q24.32"
module: 37
arm: "+"
pooled_cpm: 7.32
n_lines_expressing: 48
n_dd_up: 16
n_dd_down: 14
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# AS3MT

*arsenite methyltransferase* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.97× (z +9.3, q 1e-17, up in 8 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.52× (z +8.4, q 1e-14, up in 24 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.479× (z -10.6, q 2e-23, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BORCS7-ASMT]] (+0.77, fdr 7e-06, ⚠ same locus), [[TMED6]] (+0.69, fdr 7e-06), [[CCDC62]] (+0.67, fdr 8e-06), [[KMT2E-AS1]] (+0.66, fdr 6e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13203.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +9.3 | 1e-17 | 8/12 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +8.4 | 1e-14 | 24/41 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +8.1 | 1e-13 | 21/35 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +7.5 | 9e-12 | 14/31 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +6.5 | 1e-08 | 17/38 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +5.6 | 2e-06 | 18/45 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.26×** | +4.7 | 2e-04 | 13/46 (A-172, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +4.3 | 1e-03 | 10/23 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.003 | 8/44 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.006 | 7/46 (PANC-1, RKO, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.009 | 13/41 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.30×** | +3.7 | 0.011 | 9/42 (NCI-H460, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.27×** | +3.3 | 0.036 | 6/43 (NCI-H460, A549, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.036 | 15/45 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.055 | 12/44 (SNU-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Gefitinib (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.073 | 3/46 (SNU-1, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13203.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.479×** | -10.6 | 2e-23 | 30/45 (Panc 03.27, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.511×** | -9.6 | 1e-19 | 28/43 (NCI-H1792, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.639×** | -6.4 | 2e-08 | 19/45 (A-172, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.644×** | -6.3 | 3e-08 | 20/45 (J82, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.657×** | -6.1 | 2e-07 | 21/45 (SHP-77, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.654×** | -5.9 | 4e-07 | 17/44 (C32, NCI-H2030, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.516×** | -5.0 | 6e-05 | 11/33 (A549, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.533×** | -4.7 | 2e-04 | 11/43 (NCI-H1573, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.566×** | -4.3 | 0.001 | 8/45 (RKO, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.780×** | -3.6 | 0.019 | 17/41 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.795×** | -3.3 | 0.045 | 11/42 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.804×** | -3.2 | 0.074 | 12/45 (RKO, NCI-H1792, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.860× | -3.1 | 0.077 | 8/45 (NCI-H2030, C32, …) | rises with dose |  |
| [[Infigratinib (drug)]] 0.05 µM |  | **0.797×** | -3.1 | 0.077 | 5/44 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.669×** | -3.0 | 0.092 | 11/40 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13203. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 7.34 | 0 | 3 | — | [[Simotinib (drug)]] 0.05 µM 0.0907× (z -10.0) |
| [[BT-474 (line)]] | alt | 7.97 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.117× (z -8.8) |
| [[C-33 A (line)]] | alt | 10.9 | 0 | 1 | — | [[Malotilate (drug)]] 0.05 µM 0.0671× (z -10.7) |
| [[C32 (line)]] | wt | 7.41 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0803× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 18.3 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.114× (z -10.4) |
| [[J82 (line)]] | alt | 7.85 | 0 | 1 (1 ⚠) | — | [[OTS514 (drug)]] 0.05 µM 0.155× (z -8.5) ⚠ transcription drop |
| [[LOX-IMVI (line)]] | wt | 5.83 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0690× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -8.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1573 (line)]] | alt | 9.87 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 4.42 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0873× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 10.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.174× (z -8.8) |
| [[SHP-77 (line)]] | alt | 13.2 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.190× (z -8.9) |
| [[SNU-423 (line)]] | alt | 4.29 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 5 µM 0.0750× (z -8.7) |
| [[SW 900 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.139× (z -8.9) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.87 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13203), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 7 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BORCS7-ASMT]] | +0.77 | +0.75 / +0.61 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[TMED6]] | +0.69 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[CCDC62]] | +0.67 | +0.60 / +0.57 | both halves | 8e-06 |  |
| [[KMT2E-AS1]] | +0.66 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[MFSD2B]] | +0.65 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[DCAF4L1]] | +0.65 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[LINC02936]] | +0.65 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[TERB1]] | +0.65 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[BORCS7]] | +0.64 | +0.54 / +0.46 | both halves | 3e-05 | STRING 851; ⚠ same locus (4.5 kb, same strand: neighbours can correlate without regulation) |
| [[CASS4]] | +0.64 | +0.56 / +0.37 | both halves | 8e-05 |  |
| [[PRC1-AS1]] | +0.64 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[GTF2IRD2]] | +0.64 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[FAM184B]] | +0.64 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[MAP7D2]] | +0.64 | +0.65 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AS3MT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP7D2]] | C | MAP7D2 activity raises AS3MT's level | lines that do not express MAP7D2 (3) vs lines expressing it (47) | 1.44× lower at baseline in the lines without MAP7D2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LINC01482, TNNI3K, AOAH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.630). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.4, -15.5); signed map (15.2, 5.0). **Vector** length 73.1, 11.6% of its response variance represented; |z| ≥ 3 in 1,023 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | +9.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.6 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.9 | +2.3 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.7 | -9.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.0 | -10.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.3 | -6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.7 | -6.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -5.9 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.8 | -5.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | arsenite methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:102,869,470-102,901,899 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CYT19 |
| Gene groups (HGNC) | 7BS small molecule methyltransferases; Small molecule methyltransferases |
| Reactome | 3 pathways, smallest: Methylation; Phase II - Conjugation of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBK9](https://www.uniprot.org/uniprotkb/Q9HBK9) (Arsenite methyltransferase):

> Catalyzes the transfer of a methyl group from AdoMet to trivalent arsenicals producing methylated and dimethylated arsenicals. It methylates arsenite to form methylarsonate, Me-AsO(3)H(2), which is reduced by methylarsonate reductase to methylarsonite, Me-As(OH)2. Methylarsonite is also a substrate and it is converted into the much less toxic compound dimethylarsinate (cacodylate), Me(2)As(O)-OH.

**Summary**, from NCBI Gene [57412](https://www.ncbi.nlm.nih.gov/gene/57412):

> AS3MT catalyzes the transfer of a methyl group from S-adenosyl-L-methionine (AdoMet) to trivalent arsenical and may play a role in arsenic metabolism (Lin et al., 2002 [PubMed 11790780]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:17452](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17452) · Entrez [57412](https://www.ncbi.nlm.nih.gov/gene/57412) · UniProt [Q9HBK9](https://www.uniprot.org/uniprotkb/Q9HBK9) · Ensembl [ENSG00000214435](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214435)

## Data

Gene col 13203: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13203); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13203, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13203]; `tensor/DDL_lfc|DDL_z.npy` [13203]; `embed/gene_vectors.npy` [13203]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13203 or target_col == 13203). Every well: [[AS3MT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AS3MT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
