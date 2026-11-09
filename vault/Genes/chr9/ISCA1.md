---
symbol: "ISCA1"
type: "gene"
col: 5646
ensembl_id: "ENSG00000135070"
name: "iron-sulfur cluster assembly 1"
location: "9q21.33"
module: 105
arm: "+"
pooled_cpm: 24.47
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# ISCA1

*iron-sulfur cluster assembly 1* — 9q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.62× (z +8.3, q 7e-14, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.693× (z -9.0, q 2e-16, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EEF1AKMT4]] (+0.63, fdr 8e-06), [[NGLY1]] (+0.63, fdr 7e-06), [[CRYBB2P1-1]] (+0.61, fdr 7e-06); moves opposite to [[HNRNPD]] (-0.59, fdr 4e-05), [[SENP1]] (-0.57, fdr 1e-05), [[VEZF1]] (-0.57, fdr 1e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5646.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.62×** | +8.3 | 7e-14 | 36/47 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +7.3 | 6e-11 | 27/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +7.0 | 4e-10 | 31/48 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.93×** | +5.9 | 4e-07 | 26/47 (MIA PaCa-2, C32, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.1 | 4e-05 | 17/48 (AsPC-1, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.8 | 0.012 | 15/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.012 | 19/47 (LoVo, PANC-1, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.17× | +3.7 | 0.013 | 7/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.019 | 11/48 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.6 | 0.019 | 14/48 (SW480, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.023 | 19/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.14× | +3.2 | 0.056 | 13/48 (NCI-H2347, A-172, …) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5646.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.693×** | -9.0 | 2e-16 | 30/48 (NCI-H2030, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.588×** | -8.8 | 3e-16 | 33/48 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.710×** | -5.9 | 6e-07 | 23/47 (A-172, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.734×** | -5.2 | 4e-05 | 18/34 (A549, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Busulfan (drug)]] 0.05 µM |  | **0.803×** | -3.8 | 0.017 | 9/48 (SW 1271, J82, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.809×** | -3.6 | 0.030 | 18/41 (A-172, C-33 A, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.676×** | -3.5 | 0.031 | 14/48 (A-427, H4, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.810×** | -3.5 | 0.031 | 18/48 (SK-MEL-2, NCI-H23, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.873× | -3.2 | 0.077 | 11/48 (C32, LS 180, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.833× | -3.0 | 0.13 | 12/47 (A-172, SW48, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5646. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 28.1 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.265× (z -11.0) |
| [[AN3 CA (line)]] | alt | 70.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -8.9) |
| [[C-33 A (line)]] | alt | 27.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 16.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.176× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 45.8 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.362× (z -9.5) |
| [[PANC-1 (line)]] | alt | 15.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.280× (z -10.3) |
| [[SNU-423 (line)]] | alt | 41.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.308× (z -9.6) |
| [[A549 (line)]] | wt | 25.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -13.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[C32 (line)]] | wt | 38.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.229× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[COLO 205 (line)]] | alt | 11.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0815× (z -9.2) |
| [[HCT15 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H2030 (line)]] | alt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -10.6) |
| [[A-427 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5646), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEF1AKMT4]] | +0.63 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[NGLY1]] | +0.63 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[CRYBB2P1-1]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[STK32C]] | +0.61 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[C9orf153]] | +0.60 | +0.51 / +0.68 | both halves | 1e-05 | ⚠ same locus (4.9 kb, same strand: neighbours can correlate without regulation) |
| [[QPCTL]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[TBC1D22A-DT]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[SCAI]] | +0.59 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[C9orf72]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[NDUFAF7]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[POM121]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[NQO2]] | +0.58 | +0.49 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[GNRH1]] | +0.58 | +0.60 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPD]] | -0.59 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[SENP1]] | -0.57 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[VEZF1]] | -0.57 | -0.53 / -0.52 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[GOPC]] | -0.56 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[CSTF2T]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[ZFP91]] | -0.55 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[MIS12]] | -0.55 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[FAM111A]] | -0.55 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[TIA1]] | -0.54 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[AJUBA]] | -0.54 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[ZNF644]] | -0.54 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[ROCK2]] | -0.54 | -0.54 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.658). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.3, -20.9); signed map (-41.7, 24.4). **Vector** length 92.3, 19.0% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +5.6 | +8.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.5 | +7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.8 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +5.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.6 | -8.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.7 | -3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | -9.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -2.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.7 | -3.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | iron-sulfur cluster assembly 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.33 — chr9:86,264,546-86,283,102 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4276, ISA1, hIscA, hIscA1; previously HBLD2 |
| Gene groups (HGNC) | Mitochondrial iron-sulfur assembly components |
| Hallmark sets | HEME_METABOLISM, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 4 pathways, smallest: Mitochondrial iron-sulfur cluster biogenesis; Maturation of TCA enzymes and regulation of TCA cycle; Citric acid cycle (TCA cycle) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUE6](https://www.uniprot.org/uniprotkb/Q9BUE6) (Iron-sulfur cluster assembly 1 homolog, mitochondrial):

> Involved in the maturation of mitochondrial 4Fe-4S proteins functioning late in the iron-sulfur cluster assembly pathway. Probably involved in the binding of an intermediate of Fe/S cluster assembly.

**Summary**, from NCBI Gene [81689](https://www.ncbi.nlm.nih.gov/gene/81689):

> ISCA1 is a mitochondrial protein involved in the biogenesis and assembly of iron-sulfur clusters, which play a role in electron-transfer reactions (Cozar-Castellano et al., 2004 [PubMed 15262227]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:28660](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28660) · Entrez [81689](https://www.ncbi.nlm.nih.gov/gene/81689) · UniProt [Q9BUE6](https://www.uniprot.org/uniprotkb/Q9BUE6) · Ensembl [ENSG00000135070](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135070)

## Data

Gene col 5646: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5646); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5646, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5646]; `tensor/DDL_lfc|DDL_z.npy` [5646]; `embed/gene_vectors.npy` [5646]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5646 or target_col == 5646). Every well: [[ISCA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ISCA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
