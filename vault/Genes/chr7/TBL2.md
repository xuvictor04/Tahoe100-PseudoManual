---
symbol: "TBL2"
type: "gene"
col: 2790
ensembl_id: "ENSG00000106638"
name: "transducin beta like 2"
location: "7q11.23"
module: 12
arm: "+"
pooled_cpm: 25.27
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 15
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# TBL2

*transducin beta like 2* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.66× (z +10.5, q 4e-23, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.583× (z -10.8, q 1e-24, down in 33 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Verteporfin (drug)]] 5 µM: 0.654× (z -8.5, q 5e-15, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF805]] (+0.63, fdr 2e-05), [[GZF1]] (+0.63, fdr 2e-05), [[ALG2]] (+0.62, fdr 1e-05); moves opposite to [[CYRIB]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KLHL9]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2790.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +10.5 | 4e-23 | 30/47 (LS 180, SW480, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +8.5 | 8e-15 | 27/48 (SW480, RKO, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +6.4 | 3e-08 | 26/47 (AsPC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +6.1 | 2e-07 | 19/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 1.20× | +5.3 | 1e-05 | 21/47 (SW480, PANC-1, …) | all doses, flat | composition shift |
| [[Terfenadine (drug)]] 0.5 µM |  | **1.24×** | +4.5 | 5e-04 | 12/48 (NCI-H460, A498, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.51×** | +4.4 | 7e-04 | 18/46 (NCI-H2347, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~21% of this change | **1.23×** | +4.4 | 9e-04 | 19/44 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.018 | 13/46 (HOP62, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.060 | 8/47 (NCI-H1792, RKO, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.065 | 4/48 (LS 180, HEC-1-A, …) | two highest doses |  |
| [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.13 | 7/47 (J82, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2790.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.583×** | -10.8 | 1e-24 | 33/46 (SNU-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.654×** | -8.5 | 5e-15 | 35/48 (A498, A-427, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.691×** | -7.7 | 2e-12 | 24/43 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.693×** | -7.4 | 2e-11 | 17/32 (C32, A549, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.709×** | -7.2 | 9e-11 | 22/48 (KATO III, C32, …) | two highest doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.557×** | -6.4 | 2e-08 | 16/30 (HS-578T, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.744×** | -6.2 | 5e-08 | 25/48 (NCI-H1792, HS-578T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.750×** | -6.0 | 1e-07 | 26/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.752×** | -6.0 | 2e-07 | 22/48 (KATO III, LS 180, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.768×** | -5.5 | 2e-06 | 22/48 (SW 900, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.769×** | -5.5 | 2e-06 | 23/48 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | **0.790×** | -4.9 | 4e-05 | 21/47 (LoVo, RKO, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.791×** | -4.9 | 4e-05 | 18/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | 0.857× | -4.6 | 2e-04 | 8/48 (NCI-H661, LoVo, …) | top dose only | position effect removed |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.832×** | -3.7 | 0.008 | 12/47 (SW 1271, NCI-H460, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.883× | -3.7 | 0.008 | 14/48 (HOP62, SNU-1, …) | top dose only | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.745×** | -3.2 | 0.040 | 8/47 (C32, AN3 CA, …) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.898× | -3.2 | 0.042 | 9/48 (COLO 205, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.865× | -3.0 | 0.063 | 8/47 (A549, NCI-H1573, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2790. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 20.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0838× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[AsPC-1 (line)]] | alt | 28.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[C32 (line)]] | wt | 31.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0856× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[KATO III (line)]] | alt | 43.2 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.386× (z -8.6) |
| [[LoVo (line)]] | wt | 28.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.279× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[NCI-H1573 (line)]] | alt | 22.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SW 900 (line)]] | alt | 25.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -10.4) |
| [[SW480 (line)]] | alt | 22.2 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.40× (z +9.5) | — |
| [[A-172 (line)]] | wt | 35.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[BT-474 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.240× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[CHP-212 (line)]] | wt | 17.8 | 0 | 1 | — | [[Larotrectinib (drug)]] 0.5 µM 0.0650× (z -8.5) |
| [[HS-578T (line)]] | alt | 35.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.139× (z -9.2) ⚠ toxic |
| [[LS 180 (line)]] | wt | 19.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H23 (line)]] | alt | 20.4 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.266× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[RKO (line)]] | wt | 19.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.177× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[RPMI-7951 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -11.1) ⚠ cell-cycle shift, explains ~73% of this change |
| [[SK-MEL-2 (line)]] | alt | 29.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -11.4) ⚠ cell-cycle shift, explains ~73% of this change |
| [[SNU-1 (line)]] | wt | 23.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.151× (z -8.9) ⚠ toxic |
| [[SW1417 (line)]] | alt | 27.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A-427 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2790), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF805]] | +0.63 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[GZF1]] | +0.63 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[ALG2]] | +0.62 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[COG1]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[EXOC8]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[CREB3]] | +0.60 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[EMC9]] | +0.60 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[THAP5]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ZNF550]] | +0.60 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[NME6]] | +0.60 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[RBAK]] | +0.60 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[YIF1A]] | +0.59 | +0.67 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYRIB]] | -0.54 | -0.58 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLHL9]] | C | KLHL9 activity lowers TBL2's level | lines that do not express KLHL9 (3) vs lines expressing it (47) | 1.64× higher at baseline in the lines without KLHL9 | 0.085 | ⚠ few lines (3 vs 47); across organs; also absent: MTAP, TMEM117, CFL1P1-1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.512). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-32.9, 0.8); signed map (-6.1, -21.9). **Vector** length 96.8, 20.4% of its response variance represented; |z| ≥ 3 in 852 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.6 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.6 | +10.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +5.1 | +5.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~21% of this change | +4.9 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +6.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +3.6 |
|  | [[Lipoic acid (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +2.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.6 | -10.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | -3.9 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -3.6 | -7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | -3.1 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.7 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -7.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -8.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.7 | -1.9 |
|  | [[Pentamidine (isethionate) (drug)]] 5 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | transducin beta like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:73,567,537-73,578,791 (-) |
| Ensembl biotype | protein_coding |
| Also known as | WS-betaTRP, WBSCR13, DKFZP43N024 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q9Y4P3](https://www.uniprot.org/uniprotkb/Q9Y4P3) carries no function annotation.

**Summary**, from NCBI Gene [26608](https://www.ncbi.nlm.nih.gov/gene/26608):

> This gene encodes a member of the beta-transducin protein family. Most proteins of the beta-transducin family are involved in regulatory functions. This protein is possibly involved in some intracellular signaling pathway. This gene is deleted in Williams-Beuren syndrome, a developmental disorder caused by deletion of multiple genes at 7q11.23. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11586](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11586) · Entrez [26608](https://www.ncbi.nlm.nih.gov/gene/26608) · UniProt [Q9Y4P3](https://www.uniprot.org/uniprotkb/Q9Y4P3) · Ensembl [ENSG00000106638](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106638)

## Data

Gene col 2790: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2790); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2790, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2790]; `tensor/DDL_lfc|DDL_z.npy` [2790]; `embed/gene_vectors.npy` [2790]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2790 or target_col == 2790). Every well: [[TBL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
