---
symbol: "AKR1A1"
type: "gene"
col: 3908
ensembl_id: "ENSG00000117448"
name: "aldo-keto reductase family 1 member A1"
location: "1p34.1"
module: 49
arm: "+"
pooled_cpm: 43.98
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 17
n_dd_up_clean: 6
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# AKR1A1

*aldo-keto reductase family 1 member A1* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 1.68× (z +5.3, q 6e-05, up in 36 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.499× (z -14.1, q 2e-42, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC17A5]] (+0.77, fdr 7e-06), [[PRRC1]] (+0.74, fdr 7e-06), [[COG6]] (+0.73, fdr 7e-06); moves opposite to [[ZMYND11]] (-0.66, fdr 1e-05), [[EIF4G2]] (-0.64, fdr 1e-05), [[TRIP12]] (-0.61, fdr 2e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3908.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.68×** | +5.3 | 6e-05 | 36/46 (A-427, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +4.9 | 3e-04 | 29/48 (SW480, J82, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.8 | 3e-04 | 0/48 | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.70×** | +3.9 | 0.010 | 26/48 (SW480, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.46×** | +3.9 | 0.010 | 23/48 (SW480, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.42×** | +3.6 | 0.027 | 19/48 (MIA PaCa-2, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.57×** | +3.3 | 0.061 | 18/48 (SW480, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.061 | 19/48 (SW480, SNU-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3908.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.499×** | -14.1 | 2e-42 | 42/48 (RKO, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.670×** | -8.1 | 1e-13 | 35/47 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.592×** | -7.5 | 7e-12 | 39/48 (HS-578T, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.579×** | -7.5 | 7e-12 | 32/48 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.592×** | -7.5 | 7e-12 | 32/48 (SW 1088, RKO, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.640×** | -6.4 | 2e-08 | 33/48 (AsPC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.739×** | -6.1 | 9e-08 | 32/48 (Hs 766T, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.662×** | -5.9 | 3e-07 | 33/48 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.713×** | -4.8 | 8e-05 | 26/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.717×** | -4.5 | 4e-04 | 26/47 (Panc 03.27, RKO, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.558×** | -4.3 | 9e-04 | 28/49 (LoVo, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.748×** | -4.1 | 0.002 | 25/48 (AsPC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.758×** | -4.0 | 0.003 | 21/48 (HS-578T, SW 900, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.598×** | -3.8 | 0.007 | 24/48 (SNU-1, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.771×** | -3.7 | 0.008 | 21/48 (SW 1088, H4, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.771×** | -3.4 | 0.022 | 23/47 (A-172, A549, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3908. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 70.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -20.0) |
| [[A498 (line)]] | wt | 67.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -18.2) |
| [[AsPC-1 (line)]] | alt | 33.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -20.1) |
| [[NCI-H2030 (line)]] | alt | 55.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -13.8) |
| [[NCI-H2347 (line)]] | alt | 47.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -16.0) |
| [[RKO (line)]] | wt | 54.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -20.6) |
| [[H4 (line)]] | wt | 73.5 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.232× (z -10.0) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -8.8) |
| [[Hs 766T (line)]] | wt | 59.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -12.6) |
| [[LoVo (line)]] | wt | 71.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 41.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -9.4) |
| [[SW 1088 (line)]] | alt | 62.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0487× (z -9.4) |
| [[A-427 (line)]] | wt | 55.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -17.8) |
| [[CFPAC-1 (line)]] | alt | 41.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -11.3) |
| [[HOP62 (line)]] | alt | 34.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -9.5) |
| [[KATO III (line)]] | alt | 45.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 27.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -11.9) |
| [[SHP-77 (line)]] | alt | 36.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW 900 (line)]] | alt | 32.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -8.5) |
| [[SW1417 (line)]] | alt | 33.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -9.4) |
| [[SW48 (line)]] | wt | 84.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -10.5) |
| [[SW480 (line)]] | alt | 43.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -12.6) |
| [[A-172 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 98.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 67.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3908), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC17A5]] | +0.77 | +0.77 / +0.69 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[PRRC1]] | +0.74 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[COG6]] | +0.73 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[GORASP2]] | +0.72 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[PDIA5]] | +0.72 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[TMEM120B]] | +0.71 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[GFPT1]] | +0.71 | +0.74 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[EIF2AK3]] | +0.71 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[SSR2]] | +0.70 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[NCK1]] | +0.70 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ELP2]] | +0.69 | +0.71 / +0.57 | both halves | 9e-06 |  |
| [[RINT1]] | +0.69 | +0.65 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND11]] | -0.66 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.64 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[TRIP12]] | -0.61 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[TUG1]] | -0.60 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[CPSF2]] | -0.60 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[HNRNPK]] | -0.59 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[TASOR]] | -0.59 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[IL6ST]] | -0.59 | -0.50 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.712). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.9, -33.6); signed map (-50.4, 9.3). **Vector** length 125, 36.9% of its response variance represented; |z| ≥ 3 in 824 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cotranslational targeting of proteins to the endoplasmic reticulum* (reactome, mean cos +0.53 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.2 | +4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.9 | +5.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +0.4 |
|  | [[EX229 (drug)]] 5 µM |  | +4.1 | +3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +0.4 |
|  | [[EX229 (drug)]] 0.5 µM |  | +3.9 | +3.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.9 | +2.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.8 | +3.9 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.3 | -7.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.2 | -5.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.3 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -8.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.2 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | aldo-keto reductase family 1 member A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:45,550,543-45,570,049 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ALR, DD3 |
| Gene groups (HGNC) | Aldo-keto reductases |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 5 pathways, smallest: Formation of xylulose-5-phosphate; Glutathione conjugation; Phase II - Conjugation of compounds |
| Matched by | ensembl_id |

**Function**, from UniProt [P14550](https://www.uniprot.org/uniprotkb/P14550) (Aldo-keto reductase family 1 member A1):

> Catalyzes the NADPH-dependent reduction of a wide variety of carbonyl-containing compounds to their corresponding alcohols. Displays enzymatic activity towards endogenous metabolites such as aromatic and aliphatic aldehydes, ketones, monosaccharides and bile acids, with a preference for negatively charged substrates, such as glucuronate and succinic semialdehyde. Functions as a detoxifying enzyme by reducing a range of toxic aldehydes (By similarity). Reduces methylglyoxal and 3-deoxyglucosone, …

**Summary**, from NCBI Gene [10327](https://www.ncbi.nlm.nih.gov/gene/10327):

> This gene encodes a member of the aldo/keto reductase superfamily, which consists of more than 40 known enzymes and proteins. This member, also known as aldehyde reductase, is involved in the reduction of biogenic and xenobiotic aldehydes and is present in virtually every tissue. Multiple alternatively spliced transcript variants of this gene exist, all encoding the same protein. [provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:380](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:380) · Entrez [10327](https://www.ncbi.nlm.nih.gov/gene/10327) · UniProt [P14550](https://www.uniprot.org/uniprotkb/P14550) · Ensembl [ENSG00000117448](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117448)

## Data

Gene col 3908: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3908); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3908, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3908]; `tensor/DDL_lfc|DDL_z.npy` [3908]; `embed/gene_vectors.npy` [3908]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3908 or target_col == 3908). Every well: [[AKR1A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKR1A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
