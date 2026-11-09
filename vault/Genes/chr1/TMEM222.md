---
symbol: "TMEM222"
type: "gene"
col: 11823
ensembl_id: "ENSG00000186501"
name: "transmembrane protein 222"
location: "1p36.11"
module: 114
arm: "+"
pooled_cpm: 15.52
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# TMEM222

*transmembrane protein 222* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.74× (z +9.0, q 2e-16, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.711× (z -5.6, q 2e-05, down in 23 of 48 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.717× (z -5.4, q 2e-05, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPN2]] (+0.67, fdr 7e-06), [[ZNF721]] (+0.64, fdr 2e-05), [[LAMTOR1]] (+0.63, fdr 8e-06); moves opposite to [[USP9X]] (-0.50, fdr 3e-05), [[SPAG9]] (-0.48, fdr 2e-04), [[AFDN]] (-0.47, fdr 5e-04).
> It is in [[Module 114]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11823.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +9.0 | 2e-16 | 39/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +8.4 | 2e-14 | 35/46 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.63×** | +7.9 | 4e-13 | 34/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +7.4 | 1e-11 | 29/43 (SW 900, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +7.0 | 3e-10 | 31/47 (HT-29, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +6.3 | 2e-08 | 25/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +5.9 | 3e-07 | 25/47 (SHP-77, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.88×** | +5.4 | 6e-06 | 20/48 (KATO III, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.26×** | +5.2 | 1e-05 | 20/48 (CFPAC-1, LOX-IMVI, …) | top dose only | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.2 | 1e-05 | 21/47 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +4.4 | 5e-04 | 20/47 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.19× | +3.9 | 0.004 | 12/48 (Hs 766T, A498, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.29×** | +3.6 | 0.013 | 15/35 (SW480, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.6 | 0.013 | 5/24 (SW480, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.015 | 9/45 (HOP62, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.44×** | +3.1 | 0.066 | 13/45 (KATO III, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.074 | 9/48 (MIA PaCa-2, AN3 CA, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11823.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.711×** | -5.6 | 2e-05 | 23/48 (PANC-1, NCI-H2347, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.717×** | -5.4 | 2e-05 | 25/48 (PANC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.731×** | -5.1 | 6e-05 | 22/47 (PANC-1, BT-474, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.819×** | -4.5 | 6e-04 | 20/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.757×** | -4.5 | 6e-04 | 16/48 (PANC-1, NCI-H2347, …) | all doses, flat |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.800×** | -3.6 | 0.025 | 16/48 (HOP62, A-427, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.662×** | -3.5 | 0.036 | 11/48 (NCI-H23, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.823× | -3.1 | 0.16 | 11/47 (SK-MEL-2, NCI-H661, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11823. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 17.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -11.2) |
| [[BT-474 (line)]] | alt | 9.85 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0934× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 14.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.132× (z -11.0) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0822× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -11.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SNU-423 (line)]] | alt | 14.3 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.195× (z -9.4) |
| [[SW480 (line)]] | alt | 19.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +9.6) | — |
| [[A-172 (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11823), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPN2]] | +0.67 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[ZNF721]] | +0.64 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[LAMTOR1]] | +0.63 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[URM1]] | +0.61 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[PIGC]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[MTG2]] | +0.60 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[ZNF586]] | +0.59 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[ZKSCAN2-DT]] | +0.58 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[ZBTB8OS]] | +0.58 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[DOHH]] | +0.58 | +0.57 / +0.38 | both halves | 6e-05 |  |
| [[ZNF785]] | +0.58 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[MUL1]] | +0.57 | +0.61 / +0.50 | both halves | 1e-05 | STRING 531 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP9X]] | -0.50 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SPAG9]] | -0.48 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[AFDN]] | -0.47 | -0.23 / -0.50 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises TMEM222's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises TMEM222's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.686). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.3, 11.0); signed map (2.2, -4.9). **Vector** length 73.0, 13.4% of its response variance represented; |z| ≥ 3 in 751 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.6 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +5.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +3.1 | +5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +2.9 | +7.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +3.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.5 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +1.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +1.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | -4.0 | -1.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.6 | -5.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.5 | -5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -3.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.5 | -0.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 222 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:27,322,145-27,336,400 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564D0478; previously C1orf160 |
| Matched by | ensembl_id |

UniProt [Q9H0R3](https://www.uniprot.org/uniprotkb/Q9H0R3) carries no function annotation.

**Summary**, from NCBI Gene [84065](https://www.ncbi.nlm.nih.gov/gene/84065):

> Located in dendrite. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25363](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25363) · Entrez [84065](https://www.ncbi.nlm.nih.gov/gene/84065) · UniProt [Q9H0R3](https://www.uniprot.org/uniprotkb/Q9H0R3) · Ensembl [ENSG00000186501](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186501)

## Data

Gene col 11823: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11823); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11823, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11823]; `tensor/DDL_lfc|DDL_z.npy` [11823]; `embed/gene_vectors.npy` [11823]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11823 or target_col == 11823). Every well: [[TMEM222 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM222.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
