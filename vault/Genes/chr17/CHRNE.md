---
symbol: "CHRNE"
type: "gene"
col: 2964
ensembl_id: "ENSG00000108556"
name: "cholinergic receptor nicotinic epsilon subunit"
location: "17p13.2"
module: 38
arm: "+"
pooled_cpm: 9.65
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 11
n_dd_up_clean: 15
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# CHRNE

*cholinergic receptor nicotinic epsilon subunit* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.10× (z +14.0, q 7e-42, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.533× (z -8.4, q 2e-14, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYCE2]] (+0.69, fdr 7e-06), [[SRRM5]] (+0.69, fdr 7e-06), [[ISY1-RAB43]] (+0.68, fdr 1e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ASGR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2964.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +14.0 | 7e-42 | 38/45 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.57×** | +12.6 | 6e-34 | 42/47 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +11.4 | 1e-27 | 31/46 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.23×** | +10.7 | 1e-24 | 37/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.10×** | +9.9 | 3e-21 | 36/47 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +8.3 | 9e-15 | 29/47 (NCI-H460, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +6.0 | 1e-07 | 24/47 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +5.2 | 1e-05 | 19/48 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +5.1 | 2e-05 | 19/38 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.4 | 7e-04 | 21/43 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +4.2 | 0.001 | 11/45 (LoVo, A549, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.003 | 8/47 (A549, A-172, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.0 | 0.003 | 11/45 (AsPC-1, MIA PaCa-2, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.77×** | +4.0 | 0.003 | 7/47 (MIA PaCa-2, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.009 | 17/45 (HCT15, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.029 | 10/46 (RPMI-7951, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.3 | 0.033 | 9/48 (A-427, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2964.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.533×** | -8.4 | 2e-14 | 29/47 (KATO III, AsPC-1, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.562×** | -7.4 | 3e-11 | 24/39 (HCT15, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.622×** | -6.1 | 2e-07 | 20/45 (MIA PaCa-2, J82, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.645×** | -5.9 | 6e-07 | 22/46 (PANC-1, SW480, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.679×** | -5.2 | 2e-05 | 22/47 (NCI-H1792, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.686×** | -5.0 | 4e-05 | 18/47 (SW480, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.734×** | -4.2 | 0.003 | 18/46 (A-172, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.830×** | -3.5 | 0.027 | 21/48 (RPMI-7951, LS 180, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.766×** | -3.4 | 0.042 | 10/43 (BT-474, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.770×** | -3.4 | 0.042 | 11/44 (SW48, NCI-H23, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.629×** | -3.2 | 0.060 | 15/43 (KATO III, PANC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2964. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 17.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.51× (z +10.3) | [[Digitoxin (drug)]] 5 µM 0.320× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H460 (line)]] | wt | 8.68 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +10.4) | [[Digitoxin (drug)]] 5 µM 0.212× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[PANC-1 (line)]] | alt | 10.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -9.1) |
| [[A-427 (line)]] | wt | 14.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -12.3) |
| [[A549 (line)]] | wt | 14.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 3.49 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0413× (z -10.1) |
| [[C32 (line)]] | wt | 8.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0507× (z -13.0) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 17.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +8.7) | — |
| [[KATO III (line)]] | alt | 7.49 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0921× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 10.0 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0651× (z -12.6) |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.103× (z -8.5) |
| [[SNU-1 (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0600× (z -10.6) ⚠ cell-cycle shift, explains ~3% of this change |
| [[SNU-423 (line)]] | alt | 7.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +9.7) | — |
| [[A-172 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2964), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYCE2]] | +0.69 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[SRRM5]] | +0.69 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[ISY1-RAB43]] | +0.68 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[MYO15A]] | +0.67 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[TINCR]] | +0.67 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[ATP2A1]] | +0.67 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[PIWIL2]] | +0.65 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[PYY]] | +0.65 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[HAVCR2]] | +0.65 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[TMEM269]] | +0.65 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[LAMB2P1]] | +0.65 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[SLC9A5]] | +0.64 | +0.68 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASGR1]] | B | ASGR1 activity raises CHRNE's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.90× lower at baseline in the lines without ASGR1 | 0.002 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[RUNDC3A-AS1]] | B | RUNDC3A-AS1 activity raises CHRNE's level | lines that do not express RUNDC3A-AS1 (5) vs lines expressing it (45) | 1.67× lower at baseline in the lines without RUNDC3A-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ERO1B, TEX14, TCTN1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.719). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.6, -19.5); signed map (12.6, 11.5). **Vector** length 69.9, 11.8% of its response variance represented; |z| ≥ 3 in 1,094 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.6 | +8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +11.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +5.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +14.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.7 | +2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | -0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +0.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.3 | -3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -6.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.1 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.0 | -5.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | cholinergic receptor nicotinic epsilon subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:4,897,771-4,934,438 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ACHRE |
| Gene groups (HGNC) | Cholinergic receptors nicotinic subunits |
| Reactome | 5 pathways, smallest: Acetylcholine binding and downstream events; Postsynaptic nicotinic acetylcholine receptors; Neurotransmitter receptors and postsynaptic signal transmission |
| Matched by | ensembl_id |

**Function**, from UniProt [Q04844](https://www.uniprot.org/uniprotkb/Q04844) (Acetylcholine receptor subunit epsilon):

> After binding acetylcholine, the AChR responds by an extensive change in conformation that affects all subunits and leads to opening of an ion-conducting channel across the plasma membrane.

**Summary**, from NCBI Gene [1145](https://www.ncbi.nlm.nih.gov/gene/1145):

> Acetylcholine receptors at mature mammalian neuromuscular junctions are pentameric protein complexes composed of four subunits in the ratio of two alpha subunits to one beta, one epsilon, and one delta subunit. The acetylcholine receptor changes subunit composition shortly after birth when the epsilon subunit replaces the gamma subunit seen in embryonic receptors. Mutations in the epsilon subunit are associated with congenital myasthenic syndrome. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:1966](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1966) · Entrez [1145](https://www.ncbi.nlm.nih.gov/gene/1145) · UniProt [Q04844](https://www.uniprot.org/uniprotkb/Q04844) · Ensembl [ENSG00000108556](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108556)

## Data

Gene col 2964: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2964); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2964, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2964]; `tensor/DDL_lfc|DDL_z.npy` [2964]; `embed/gene_vectors.npy` [2964]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2964 or target_col == 2964). Every well: [[CHRNE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHRNE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
