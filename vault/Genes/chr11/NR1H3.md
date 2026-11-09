---
symbol: "NR1H3"
type: "gene"
col: 362
ensembl_id: "ENSG00000025434"
name: "nuclear receptor subfamily 1 group H member 3"
location: "11p11.2"
module: 23
arm: "+"
pooled_cpm: 9.06
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 14
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# NR1H3

*nuclear receptor subfamily 1 group H member 3* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.32× (z +5.1, q 2e-04, up in 20 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.536× (z -7.8, q 3e-12, down in 23 of 36 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.637× (z -5.9, q 6e-07, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TERF2IP]] (+0.73, fdr 7e-06), [[LAMB2P1]] (+0.73, fdr 7e-06), [[GTF2IRD2B]] (+0.63, fdr 7e-06); moves opposite to [[PFN2]] (-0.59, fdr 1e-05), [[GALNT1]] (-0.59, fdr 3e-05), [[ICMT]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TP53]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 362.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.1 | 2e-04 | 20/43 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +4.9 | 3e-04 | 17/46 (KATO III, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +4.3 | 0.003 | 14/45 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.005 | 14/47 (SNU-423, PANC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.46×** | +4.1 | 0.005 | 7/44 (SW1417, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.9 | 0.010 | 13/43 (NCI-H460, COLO 205, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.064 | 8/40 (KATO III, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.28× | +3.1 | 0.12 | 12/37 (Panc 03.27, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.27× | +3.1 | 0.12 | 8/47 (KATO III, LoVo, …) | inconsistent across doses |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | 1.18× | +3.0 | 0.14 | 6/48 (A498, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 362.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.536×** | -7.8 | 3e-12 | 23/36 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.599×** | -6.7 | 7e-09 | 27/47 (HT-29, A498, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.617×** | -6.3 | 6e-08 | 25/43 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.637×** | -5.9 | 6e-07 | 22/47 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.639×** | -5.8 | 6e-07 | 22/47 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.698×** | -4.7 | 2e-04 | 15/31 (HS-578T, NCI-H1792, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.645×** | -4.7 | 2e-04 | 17/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.690×** | -4.6 | 2e-04 | 14/45 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.507×** | -4.6 | 2e-04 | 14/30 (NCI-H460, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.694×** | -4.5 | 4e-04 | 20/43 (Panc 03.27, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.765×** | -3.5 | 0.026 | 16/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.608×** | -3.4 | 0.032 | 12/41 (C-33 A, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Asciminib (drug)]] 0.05 µM |  | **0.786×** | -3.1 | 0.073 | 12/46 (SW 1271, CHP-212, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.792×** | -3.0 | 0.099 | 7/48 (NCI-H460, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 362. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 12.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.98× (z +15.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.184× (z -9.9) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 10.1 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -12.1) |
| [[NCI-H1792 (line)]] | alt | 9.27 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW480 (line)]] | alt | 12.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.273× (z -9.4) |
| [[C32 (line)]] | wt | 5.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.54× (z +9.3) | — |
| [[COLO 205 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0898× (z -10.0) ⚠ toxic |
| [[HCT15 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -9.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 6.68 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0790× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H460 (line)]] | wt | 5.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +10.7) | — |
| [[RPMI-7951 (line)]] | alt | 7.90 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0713× (z -9.7) |
| [[A-172 (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 362), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERF2IP]] | +0.73 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[LAMB2P1]] | +0.73 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[GTF2IRD2B]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ZNF226]] | +0.62 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[TMEM269]] | +0.62 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[ANKRA2]] | +0.61 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[LINC01772]] | +0.61 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[HAVCR2]] | +0.61 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[KLC4]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[CDKL3]] | +0.60 | +0.70 / +0.46 | both halves | 3e-05 |  |
| [[TMEM91]] | +0.60 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[ZSWIM3]] | +0.59 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PFN2]] | -0.59 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[GALNT1]] | -0.59 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[ICMT]] | -0.59 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.58 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[DNM1L]] | -0.57 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[BLTP2]] | -0.57 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[DYNC1H1]] | -0.57 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[CS]] | -0.57 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[JAM3]] | -0.56 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[RSU1]] | -0.55 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[YWHAQ]] | -0.55 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[SIGMAR1]] | -0.55 | -0.51 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | C | TP53 activity weakens NR1H3's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 1.44× as strongly (z diff -0.74); strongest at Ouabain (Octahydrate) 5 µM: 0.45x vs 0.99x (z diff -3.5) | 0.593 over the table, 0.031 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.587). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-9.0, 27.0); signed map (3.0, -3.2). **Vector** length 70.3, 12.3% of its response variance represented; |z| ≥ 3 in 776 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.4 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.7 | +1.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | -0.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +1.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -6.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -2.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.5 | -7.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.3 | -5.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor subfamily 1 group H member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:47,248,300-47,269,033 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LXR-a, RLD-1, LXRa |
| Gene groups (HGNC) | Nuclear receptor subfamily 1 group H |
| Reactome | 19 pathways, smallest: NR1H2 & NR1H3 regulate gene expression linked to triglyceride lipolysis in adipose; NR1H2 & NR1H3 regulate gene expression linked to gluconeogenesis; NR1H2 & NR1H3 regulate gene expression to limit cholesterol uptake |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13133](https://www.uniprot.org/uniprotkb/Q13133) (Oxysterols receptor LXR-alpha):

> Nuclear receptor that exhibits a ligand-dependent transcriptional activation activity. Interaction with retinoic acid receptor (RXR) shifts RXR from its role as a silent DNA-binding partner to an active ligand-binding subunit in mediating retinoid responses through target genes defined by LXRES. LXRES are DR4-type response elements characterized by direct repeats of two similar hexanuclotide half-sites spaced by four nucleotides (By similarity). Plays an important role in the regulation of …

**Summary**, from NCBI Gene [10062](https://www.ncbi.nlm.nih.gov/gene/10062):

> The protein encoded by this gene belongs to the NR1 subfamily of the nuclear receptor superfamily. The NR1 family members are key regulators of macrophage function, controlling transcriptional programs involved in lipid homeostasis and inflammation. This protein is highly expressed in visceral organs, including liver, kidney and intestine. It forms a heterodimer with retinoid X receptor (RXR), and regulates expression of target genes containing retinoid response elements. Studies in mice …

**Accessions** — [HGNC:7966](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7966) · Entrez [10062](https://www.ncbi.nlm.nih.gov/gene/10062) · UniProt [Q13133](https://www.uniprot.org/uniprotkb/Q13133) · Ensembl [ENSG00000025434](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000025434)

## Data

Gene col 362: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 362); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 362, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 362]; `tensor/DDL_lfc|DDL_z.npy` [362]; `embed/gene_vectors.npy` [362]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 362 or target_col == 362). Every well: [[NR1H3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NR1H3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
