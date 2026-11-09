---
symbol: "TMEM74B"
type: "gene"
col: 4689
ensembl_id: "ENSG00000125895"
name: "transmembrane protein 74B"
location: "20p13"
module: 103
arm: "+"
pooled_cpm: 3.09
n_lines_expressing: 45
n_dd_up: 1
n_dd_down: 32
n_dd_up_clean: 1
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# TMEM74B

*transmembrane protein 74B* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM: 1.49× (z +3.8, q 0.094, up in 7 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.317× (z -15.4, q 0e+00, down in 30 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C2orf72]] (+0.71, fdr 7e-06), [[ISM2]] (+0.63, fdr 7e-06), [[PDZD4]] (+0.56, fdr 1e-05); moves opposite to [[EFCAB10]] (-0.46, fdr 1e-04), [[EGFEM1P]] (-0.46, fdr 1e-04), [[NRP1]] (-0.45, fdr 3e-04).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4689.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | **1.49×** | +3.8 | 0.094 | 7/32 (SW480, A-427, …) | two highest doses | position effect removed |
| [[Ferulic acid (drug)]] 0.5 µM |  | 1.41× | +3.3 | 0.32 | 2/36 (A549, NCI-H2030) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4689.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.317×** | -15.4 | 0e+00 | 30/33 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.216×** | -14.5 | 3e-45 | 33/39 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.215×** | -14.0 | 2e-42 | 31/37 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.263×** | -12.7 | 1e-34 | 28/31 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.286×** | -11.9 | 1e-30 | 31/39 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.306×** | -11.2 | 2e-27 | 29/39 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.393×** | -8.9 | 5e-17 | 26/38 (A-172, HT-29, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.402×** | -8.6 | 4e-16 | 26/39 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.414×** | -8.1 | 5e-14 | 19/24 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.583×** | -7.2 | 2e-11 | 19/31 (MIA PaCa-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.477×** | -7.0 | 1e-10 | 21/38 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.532×** | -6.0 | 1e-07 | 15/39 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.555×** | -5.6 | 9e-07 | 17/38 (H4, SK-MEL-2, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.589×** | -5.0 | 2e-05 | 12/39 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.622×** | -4.5 | 2e-04 | 15/37 (NCI-H1792, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.436×** | -4.1 | 0.001 | 13/30 (RKO, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.650×** | -4.1 | 0.001 | 11/38 (hTERT-HPNE, SW1417, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.659×** | -4.0 | 0.002 | 15/36 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~25% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.452×** | -3.9 | 0.002 | 13/36 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.58 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4689. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 4.97 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -12.3) |
| [[LoVo (line)]] | wt | 5.54 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -13.7) |
| [[MIA PaCa-2 (line)]] | alt | 6.18 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.00912× (z -18.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0553× (z -16.3) |
| [[PANC-1 (line)]] | alt | 1.87 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0254× (z -12.1) |
| [[A-172 (line)]] | wt | 3.40 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0762× (z -12.1) |
| [[A549 (line)]] | wt | 6.08 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0670× (z -15.6) |
| [[HOP62 (line)]] | alt | 7.20 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0693× (z -17.2) |
| [[RKO (line)]] | wt | 13.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -13.4) |
| [[C-33 A (line)]] | alt | 7.36 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 3.87 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0393× (z -10.3) |
| [[SW480 (line)]] | alt | 2.96 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0444× (z -19.0) |
| [[HepG2_C3A (line)]] | wt | 7.91 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -10.4) |
| [[HT-29 (line)]] | alt | 3.44 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0665× (z -8.5) |
| [[J82 (line)]] | alt | 2.32 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0849× (z -9.7) |
| [[SNU-423 (line)]] | alt | 2.83 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0657× (z -10.5) |
| [[A-427 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.500 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.897 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.917 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.998 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.457 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.388 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.423 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4689), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2orf72]] | +0.71 | +0.71 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[ISM2]] | +0.63 | +0.58 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[PDZD4]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[CPNE5]] | +0.52 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[SEC14L4]] | +0.51 | +0.52 / +0.30 | both halves | 2e-04 |  |
| [[ACADS]] | +0.51 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[TLE6]] | +0.50 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[EFEMP2]] | +0.50 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[MAP3K15]] | +0.49 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[ENGASE]] | +0.49 | +0.34 / +0.38 | both halves | 1e-04 |  |
| [[APLN]] | +0.49 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[SMARCD3]] | +0.48 | +0.48 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB10]] | -0.46 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[EGFEM1P]] | -0.46 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[NRP1]] | -0.45 | -0.40 / -0.26 | both halves | 3e-04 |  |
| [[TBC1D5]] | -0.44 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[STAG1]] | -0.44 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[PTPRK]] | -0.44 | -0.46 / -0.37 | both halves | 7e-05 |  |
| [[STPG2]] | -0.43 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[DIO2]] | -0.42 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[ATXN7L1]] | -0.41 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[CDKN2B-AS1]] | -0.40 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[FAP]] | -0.40 | -0.39 / -0.22 | both halves | 6e-04 |  |
| [[EXOC4]] | -0.40 | -0.41 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TMEM74B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.590). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (5.8, 44.8); signed map (-29.9, 34.8). **Vector** length 50.4, 6.74% of its response variance represented; |z| ≥ 3 in 1,048 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +0.8 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +1.1 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +3.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.0 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.0 | -12.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.7 | -7.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.7 | -14.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -8.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.3 | -8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -3.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | -1.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 74B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:1,180,561-1,185,415 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11190; previously C20orf46 |
| Matched by | ensembl_id |

UniProt [Q9NUR3](https://www.uniprot.org/uniprotkb/Q9NUR3) carries no function annotation.

**Summary**, from NCBI Gene [55321](https://www.ncbi.nlm.nih.gov/gene/55321):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15893](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15893) · Entrez [55321](https://www.ncbi.nlm.nih.gov/gene/55321) · UniProt [Q9NUR3](https://www.uniprot.org/uniprotkb/Q9NUR3) · Ensembl [ENSG00000125895](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125895)

## Data

Gene col 4689: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4689); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4689, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4689]; `tensor/DDL_lfc|DDL_z.npy` [4689]; `embed/gene_vectors.npy` [4689]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4689 or target_col == 4689). Every well: [[TMEM74B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM74B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
